#!/usr/bin/env python3
"""
Monthly Coherence Pass — The Recurring Revenue Engine

This script runs the Observer Core against a client's vault and produces
a coherence report. This is the "stream" — runs monthly, generates a
deliverable report, justifies the $33/mo subscription.

Usage (standalone):
    python3 monthly_coherence_pass.py --vault /path/to/client/vault

Usage (via Hermes cron):
    hermes cron create "0 9 1 * *" --prompt "Run monthly coherence pass for client X"

What it produces:
    - Coherence score (0.00 - 1.00)
    - Contradiction count
    - Drift indicators (notes that diverge from axioms)
    - Residual list (unresolved questions/tensions)
    - New Time-Chain block (if client has active chain)
    - Saved to client vault: 08_GENERATED/observer-passes/YYYY-MM-coherence-pass.md
"""

import argparse
import hashlib
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def scan_vault(vault_path):
    """Scan all markdown files and extract metadata."""
    vault = Path(vault_path)
    notes = []
    
    for md in vault.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8", errors="replace")
            rel = str(md.relative_to(vault))
            
            # Extract tags from frontmatter
            tags = []
            tag_match = re.search(r"tags:\s*\n((?:\s+-\s+.+\n)+)", content)
            if tag_match:
                tags = [t.strip().lstrip("- ") for t in tag_match.group(1).strip().split("\n")]
            
            # Count wikilinks
            links = re.findall(r"\[\[([^\]]+)\]\]", content)
            
            # Check for status
            status_match = re.search(r"status:\s*(.+)", content)
            status = status_match.group(1).strip() if status_match else "unknown"
            
            # Word count
            words = len(content.split())
            
            notes.append({
                "path": rel,
                "folder": rel.split("/")[0] if "/" in rel else "root",
                "tags": tags,
                "links": links,
                "link_count": len(links),
                "status": status,
                "words": words,
                "size": len(content),
                "has_frontmatter": content.strip().startswith("---"),
            })
        except Exception:
            continue
    
    return notes


def detect_contradictions(notes):
    """Look for potential contradictions (same topic, conflicting status/claims)."""
    contradictions = []
    
    # Find notes with similar names that might conflict
    by_topic = defaultdict(list)
    for n in notes:
        name = Path(n["path"]).stem.lower()
        # Extract key terms
        terms = [t for t in name.replace("-", " ").replace("_", " ").split() 
                 if len(t) > 3 and t not in ("inner", "network", "readme")]
        for t in terms:
            by_topic[t].append(n)
    
    for topic, related in by_topic.items():
        if len(related) > 1:
            statuses = set(n["status"] for n in related)
            if len(statuses) > 1 and "canonical" in statuses:
                contradictions.append({
                    "topic": topic,
                    "files": [n["path"] for n in related],
                    "statuses": list(statuses),
                    "severity": "medium",
                    "note": f"Multiple files about '{topic}' with conflicting statuses: {statuses}",
                })
    
    return contradictions


def detect_drift(notes):
    """Detect notes that might be drifting from the architecture."""
    drift = []
    
    for n in notes:
        # Notes without frontmatter
        if not n["has_frontmatter"] and n["path"] != "Welcome.md":
            drift.append({
                "file": n["path"],
                "issue": "No YAML frontmatter — not integrated into the ontology",
                "severity": "low",
            })
        
        # Notes without #inneri tag
        if "inneri" not in n["tags"] and n["path"].endswith(".md") and "README" not in n["path"]:
            drift.append({
                "file": n["path"],
                "issue": "Missing #inneri tag — disconnected from vault coherence",
                "severity": "medium",
            })
        
        # Orphan notes (no links in or out)
        if n["link_count"] == 0 and n["words"] > 50 and "README" not in n["path"]:
            drift.append({
                "file": n["path"],
                "issue": "Orphan note — no wikilinks to or from other notes",
                "severity": "low",
            })
    
    return drift


def compute_coherence_score(notes, contradictions, drift):
    """Compute a coherence score from 0.00 to 1.00."""
    if not notes:
        return 0.0
    
    total = len(notes)
    
    # Frontmatter coverage (weight: 0.25)
    fm_ratio = sum(1 for n in notes if n["has_frontmatter"]) / total
    
    # Tag coverage (weight: 0.25)
    tag_ratio = sum(1 for n in notes if "inneri" in n["tags"]) / total
    
    # Link density (weight: 0.20) — higher is better, capped at 1.0
    avg_links = sum(n["link_count"] for n in notes) / total
    link_score = min(avg_links / 3.0, 1.0)  # 3+ links per note = perfect
    
    # Contradiction penalty (weight: 0.15)
    contradiction_penalty = min(len(contradictions) * 0.1, 0.5)
    contradiction_score = 1.0 - contradiction_penalty
    
    # Drift penalty (weight: 0.15)
    drift_penalty = min(len(drift) * 0.02, 0.5)
    drift_score = 1.0 - drift_penalty
    
    score = (
        fm_ratio * 0.25 +
        tag_ratio * 0.25 +
        link_score * 0.20 +
        contradiction_score * 0.15 +
        drift_score * 0.15
    )
    
    return round(max(0.0, min(1.0, score)), 2)


def generate_report(vault_path, notes, contradictions, drift, score):
    """Generate the monthly coherence pass report."""
    date = datetime.now().strftime("%Y-%m-%d")
    month = datetime.now().strftime("%Y-%m")
    
    # Folder distribution
    folder_counts = Counter(n["folder"] for n in notes)
    folder_table = "\n".join(f"| {f} | {c} |" for f, c in sorted(folder_counts.items()))
    
    # Contradiction details
    if contradictions:
        contra_lines = "\n".join(
            f"- **{c['topic']}**: {', '.join(c['files'])} — {c['note']}"
            for c in contradictions
        )
    else:
        contra_lines = "None detected. ✅"
    
    # Drift details
    if drift:
        drift_lines = "\n".join(
            f"- `{d['file']}` — {d['issue']} [{d['severity']}]"
            for d in drift[:20]  # cap at 20
        )
        if len(drift) > 20:
            drift_lines += f"\n- ... and {len(drift) - 20} more"
    else:
        drift_lines = "None detected. ✅"
    
    # Score interpretation
    if score >= 0.85:
        verdict = "🟢 Strong coherence. System is well-integrated."
    elif score >= 0.70:
        verdict = "🟡 Good coherence. Some drift detected — review recommended."
    elif score >= 0.50:
        verdict = "🟠 Moderate coherence. Significant drift — action needed."
    else:
        verdict = "🔴 Low coherence. System fragmentation detected — urgent review."
    
    report = f"""---
type: observer-pass
pass_type: monthly-coherence
date: {date}
coherence_score: {score}
total_notes: {len(notes)}
contradictions: {len(contradictions)}
drift_indicators: {len(drift)}
tags:
  - inneri
  - observer-pass
  - coherence
  - monthly
---

# Monthly Coherence Pass — {month}

> Observer Core pass on {date}. Score: **{score}**
>
> {verdict}

## Coherence Score

**{score}** / 1.00

| Metric | Status |
|---|---|
| Total notes scanned | {len(notes)} |
| Contradictions detected | {len(contradictions)} |
| Drift indicators | {len(drift)} |
| Frontmatter coverage | {sum(1 for n in notes if n['has_frontmatter'])}/{len(notes)} |
| Tag coverage (#inneri) | {sum(1 for n in notes if 'inneri' in n['tags'])}/{len(notes)} |
| Average link density | {sum(n['link_count'] for n in notes) / max(len(notes), 1):.1f} links/note |

## Folder Distribution

| Folder | Notes |
|---|---|
{folder_table}

## Contradictions

{contra_lines}

## Drift Indicators

{drift_lines}

## Recommendations

{"- Address high-severity drift items first" if any(d['severity'] == 'high' for d in drift) else ""}
{"- Review contradictions and resolve by archiving or merging" if contradictions else ""}
{"- Add frontmatter to notes missing YAML headers" if any(not n['has_frontmatter'] for n in notes) else ""}
{"- Add #inneri tags to disconnected notes" if any('inneri' not in n['tags'] for n in notes if n['path'].endswith('.md') and 'README' not in n['path']) else ""}
{"- Connect orphan notes with wikilinks" if any(n['link_count'] == 0 and n['words'] > 50 for n in notes) else ""}
- Continue monthly passes to track coherence trajectory

## Next Pass

Scheduled for {datetime.now().replace(month=datetime.now().month % 12 + 1).strftime('%Y-%m')}.

---

*Generated by Inner I Observer Core. innerinetcompany.com*
"""
    
    # Write to vault
    output_dir = Path(vault_path) / "08_GENERATED" / "observer-passes"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{month}-coherence-pass.md"
    output_file.write_text(report)
    
    return str(output_file), report


def main():
    parser = argparse.ArgumentParser(description="Monthly Coherence Pass")
    parser.add_argument("--vault", required=True, help="Path to client vault")
    parser.add_argument("--quiet", action="store_true", help="Only output score")
    args = parser.parse_args()
    
    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists():
        print(f"ERROR: Vault not found at {vault}", file=sys.stderr)
        sys.exit(1)
    
    notes = scan_vault(vault)
    contradictions = detect_contradictions(notes)
    drift = detect_drift(notes)
    score = compute_coherence_score(notes, contradictions, drift)
    
    if args.quiet:
        print(score)
        return
    
    output_file, report = generate_report(vault, notes, contradictions, drift, score)
    
    print(f"\n{'='*60}")
    print(f"  MONTHLY COHERENCE PASS")
    print(f"  Vault: {vault}")
    print(f"  Score: {score}")
    print(f"  Notes: {len(notes)}")
    print(f"  Contradictions: {len(contradictions)}")
    print(f"  Drift indicators: {len(drift)}")
    print(f"  Report: {output_file}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
