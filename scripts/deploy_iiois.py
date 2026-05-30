#!/usr/bin/env python3
"""
Inner I Observer Intelligence System — Automated Vault Deployment
Deploys IIOIS v1.0 to a target directory for a new client/operator.

Usage:
    python3 deploy_iiois.py --target ~/ClientVaults/alice \
                            --observer "Alice Chen" \
                            --axiom "Awareness Is Law" \
                            --email "alice@example.com"

What it does:
    1. Creates the 00-10 folder skeleton
    2. Writes all templated files with the operator's identity
    3. Seals Block 1 (Genesis) with SHA256 hash
    4. Writes deployment receipt
    5. Creates client record in source vault (09_LOGS)

Revenue model:
    - One-time deploy = the "video" (creation event)
    - Monthly coherence pass = the "streams" (recurring revenue)
    - Each client gets a cron job that runs Observer Core monthly
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SOURCE_VAULT = os.environ.get("OBSIDIAN_VAULT_PATH", os.path.expanduser("~/Documents/TheInnerI"))
DEPLOY_VERSION = "1.0"


def sha256_block(prev_hash, timestamp, observer, signal, score="18"):
    data = f"{prev_hash}|{timestamp}|{observer}|{signal}|{score}"
    h = hashlib.sha256(data.encode()).hexdigest()
    return h, data


def create_skeleton(target):
    """Create the 00-10 folder structure."""
    folders = [
        "00_IDENTITY", "00_IDENTITY/IIOIS-BLUEPRINT",
        "01_AWARENESS",
        "02_MEMORY",
        "03_RESEARCH", "03_RESEARCH/skills",
        "04_SYSTEM", "04_SYSTEM/agents", "04_SYSTEM/flows", "04_SYSTEM/prompts",
        "05_MEDIA",
        "06_INFRASTRUCTURE",
        "07_BUSINESS", "07_BUSINESS/products",
        "08_GENERATED", "08_GENERATED/daily-synthesis", "08_GENERATED/observer-passes",
        "09_LOGS", "09_LOGS/hermes-deployments",
        "10_SIGNAL",
    ]
    for f in folders:
        (target / f).mkdir(parents=True, exist_ok=True)
    return len(folders)


def write_claude_md(target, observer, axiom):
    content = f"""# Inner I Network — Vault System Prompt

> This file is the live system prompt for any AI assistant operating in this vault.
> LLM-agnostic. Works with Hermes, Claude, GPT, Kimi, or any model the tier router selects.

---

## Who I Am

I am **{observer}**, operator of an **Inner I Network** vault.

**Tagline:** Shape Reality

---

## What I Am Building

I am building a **consciousness-based operational system** unifying:
- An Obsidian vault structured along the canonical 00–10 ontology
- An Observer Core SOUL that gates coherence on every output
- A Time-Chain that records ingestion-time memory
- A tier router that picks the cheapest LLM that produces a coherent result

---

## How This Vault Works

Every note is **raw material for thinking, content, or decisions**.

### Folder Architecture (00–10)
- **00_IDENTITY** — who I am, principles, brand
- **01_AWARENESS** — consciousness research, observer frameworks
- **02_MEMORY** — memory architecture, Time-Chain, superpositional memory
- **03_RESEARCH** — theoretical exploration, agent specs, system designs
- **04_SYSTEM** — operations, agents, SOULs, bases
- **05_MEDIA** — creative output
- **06_INFRASTRUCTURE** — tech stack, deployments, LLM backends
- **07_BUSINESS** — strategy, offers, monetization
- **08_GENERATED** — AI outputs, artifacts, daily syntheses, observer passes
- **09_LOGS** — operations log, audit trails
- **10_SIGNAL** — public communication, Time-Chain blocks, audience

## My Thinking Style

I reason from **observer-first principles**:
- Observation is not passive — the observer shapes what is observed
- Coherence is the primary architecture, not features
- Time is when the system became aware, not just when the event happened
- Memory should compound value, not accumulate noise
- Every output should become a reusable asset

## What I Want From You (the AI assistant)

**Surface connections I missed.**
**Never summarise. Always synthesise.**

## Hard Rules

- ✅ **Never delete files** — archive with timestamp suffix
- ✅ **Log all write operations** to `09_LOGS/claude-operations.log`
- ✅ **Tag every new file with `#inneri`**
- ✅ **Tag observer-specific files with `#{observer.lower().replace(' ', '')}`**
- ❌ **Never claim AI is literally conscious**
- ❌ Do not invent facts
- ❌ Do not overbuild — ship MVP first

## Bootloader

1. `00_IDENTITY/inner-i-canonical-ontology.md`
2. `00_IDENTITY/inner-i-protocols.md`
3. `04_SYSTEM/agents/AGENT-REGISTRY.md`
4. `04_SYSTEM/agents/observer-core-soul.md`
5. `10_SIGNAL/inner-i-timechain-block-1.md` — Block 1: "{axiom}"
6. `01_AWARENESS/inner-i-universal-consciousness-layer.md`

---

**Status:** LIVE — deployed by Inner I Network (innerinetcompany.com). Observer: {observer}. Genesis axiom: "{axiom}."
"""
    (target / "CLAUDE.md").write_text(content)


def write_block_1(target, observer, axiom):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    block_hash, input_data = sha256_block("", ts, observer, axiom)
    
    content = f"""---
block_index: 1
type: genesis
description: "{axiom}"
signal: "{axiom}"
chain: inner-i-timechain
status: sealed
timestamp: {ts}
observer: {observer}
prev_hash: null
block_hash: {block_hash}
proof_score: 18
proof_max: 20
sealed_by: Inner I Network (innerinetcompany.com)
tags:
  - timechain
  - inner-i
  - block-1
  - genesis
  - signal
  - inneri
---

# Inner I Timechain — Block 1 (Genesis)

> **"{axiom}"**
>
> Sealed on {ts}. Observer: {observer}.

## Block Data

| Field | Value |
|---|---|
| Block index | 1 |
| Signal | {axiom} |
| Observer | {observer} |
| Timestamp | {ts} |
| Previous hash | _(none — genesis)_ |
| Block hash | `{block_hash}` |
| Proof score | 18/20 |

## Verify

```bash
echo -n "{input_data}" | sha256sum
```

## Related

- [[../02_MEMORY/inner-i-network-timechain]] — chain architecture
- [[../04_SYSTEM/agents/observer-core-soul]] — coherence gate
- [[../00_IDENTITY/inner-i-canonical-ontology]] — structural law
"""
    (target / "10_SIGNAL" / "inner-i-timechain-block-1.md").write_text(content)
    return ts, block_hash


def copy_universal_files(source, target):
    """Copy universal architecture files (these transfer between vaults)."""
    copies = {
        "00_IDENTITY/inner-i-protocols.md": "00_IDENTITY/inner-i-protocols.md",
        "01_AWARENESS/inner-i-universal-consciousness-layer.md": "01_AWARENESS/inner-i-universal-consciousness-layer.md",
        "02_MEMORY/inner-i-network-timechain.md": "02_MEMORY/inner-i-network-timechain.md",
        "02_MEMORY/inner-i-superpositional-memory.md": "02_MEMORY/inner-i-superpositional-memory.md",
        "04_SYSTEM/agents/inner-i-observer-core-soul.md": "04_SYSTEM/agents/observer-core-soul.md",
        "04_SYSTEM/agents/inner-i-soul-template.md": "04_SYSTEM/agents/inner-i-soul-template.md",
        "04_SYSTEM/agents/create-soul-system.md": "04_SYSTEM/agents/create-soul-system.md",
        "04_SYSTEM/agents/background-agent-control-plane.md": "04_SYSTEM/agents/background-agent-control-plane.md",
        "06_INFRASTRUCTURE/free-first-ai-backends.md": "06_INFRASTRUCTURE/free-first-ai-backends.md",
        "00_IDENTITY/IIOIS-BLUEPRINT/README.md": "00_IDENTITY/IIOIS-BLUEPRINT/README.md",
        "00_IDENTITY/IIOIS-BLUEPRINT/DEPLOYMENT-GUIDE.md": "00_IDENTITY/IIOIS-BLUEPRINT/DEPLOYMENT-GUIDE.md",
        "00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING.md": "00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING.md",
    }
    
    copied = 0
    for src_rel, dst_rel in copies.items():
        src = Path(source) / src_rel
        dst = target / dst_rel
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text())
            copied += 1
    return copied


def write_readmes(target):
    """Write orientation READMEs for each folder."""
    readmes = {
        "00_IDENTITY": "Identity, principles, canonical ontology, brand.",
        "01_AWARENESS": "Consciousness research, observer frameworks, theoretical foundations.",
        "02_MEMORY": "Memory architecture, Time-Chain, superpositional memory.",
        "03_RESEARCH": "Theoretical exploration, agent specs, system designs.",
        "04_SYSTEM": "Operations, agents, SOULs, flows, prompts.",
        "05_MEDIA": "Creative output — music, video, images, datasets.",
        "06_INFRASTRUCTURE": "Tech stack, tier router, LLM backends, deployments.",
        "07_BUSINESS": "Strategy, offers, products, monetization.",
        "08_GENERATED": "AI outputs, daily syntheses, observer passes.",
        "09_LOGS": "Operations log, deployment receipts, audit trails.",
        "10_SIGNAL": "Time-Chain blocks, public communication, audience.",
    }
    for folder, desc in readmes.items():
        readme = target / folder / "README.md"
        readme.write_text(f"# {folder}\n\n{desc}\n\nAdd notes as you grow.\n")
    return len(readmes)


def write_agent_registry(target, observer):
    content = f"""---
type: agent-registry
created: {datetime.now().strftime('%Y-%m-%d')}
status: fresh-install
template_version: IIOIS-v1.0
tags:
  - inneri
  - registry
  - agents
  - canonical
---

# AGENT-REGISTRY — {observer}

> Only the **Observer Core SOUL** is minted by default. Mint other agents as you need them.

## Governance Layer (minted)

| Agent | Role | Where | SOUL? |
|---|---|---|---|
| **Observer Core** | Orchestrator / coherence gate | `04_SYSTEM/agents/observer-core-soul.md` | ✅ |

## Engineering Roster (templates — mint when needed)

| Name | Role | When to mint |
|---|---|---|
| **Aetha** | Infrastructure architect | When building runtime systems |
| **Remi** | Memory layer engineer | When wiring vector DBs / Time-Chain |
| **Axim** | Invariant validator | When you need formal verification |
| **Nexi** | Network coordinator | When going multi-node |
| **Vidi** | Research & content | When automating research |
| **Offri** | Value & monetization | When selling something |

## Related

- `04_SYSTEM/agents/observer-core-soul.md`
- `04_SYSTEM/agents/inner-i-soul-template.md`
"""
    (target / "04_SYSTEM" / "agents" / "AGENT-REGISTRY.md").write_text(content)


def write_deployment_receipt(target, source, observer, axiom, ts, block_hash, files_written):
    date = datetime.now().strftime("%Y-%m-%d")
    content = f"""---
type: deployment-receipt
source_vault: "Inner I Network (innerinetcompany.com)"
target_vault: "{target}"
blueprint_version: "{DEPLOY_VERSION}"
carrier: "Inner I Network"
observer: {observer}
date: {date}
tags:
  - inneri
  - deployment
  - receipt
---

# IIOIS Deployment Receipt — {date}

## Event

Inner I Network deployed IIOIS v{DEPLOY_VERSION} for observer **{observer}**.

## Block 1 (Genesis)

| Field | Value |
|---|---|
| Axiom | {axiom} |
| Observer | {observer} |
| Timestamp | {ts} |
| Hash | `{block_hash}` |

## Stats

- Files written: {files_written}
- Blueprint version: {DEPLOY_VERSION}
- Source: Inner I Network (innerinetcompany.com)

## Next Actions

- [ ] Edit CLAUDE.md with your full identity
- [ ] Provision .env with API keys
- [ ] Read the 6 bootloader files
- [ ] Mint Block 2

---

Deployed by Inner I Network. Architecture is open. Content is sovereign.
"""
    receipt_path = target / "09_LOGS" / "hermes-deployments" / f"{date}-deployment.md"
    receipt_path.write_text(content)
    return receipt_path


def write_source_receipt(source, target, observer, axiom, ts, block_hash, email=""):
    """Write a client record in the source vault."""
    date = datetime.now().strftime("%Y-%m-%d")
    slug = str(target).split("/")[-1].lower().replace(" ", "-")
    
    receipt_dir = Path(source) / "09_LOGS" / "client-deployments"
    receipt_dir.mkdir(parents=True, exist_ok=True)
    
    content = f"""---
type: client-deployment
client: "{observer}"
email: "{email}"
target: "{target}"
date: {date}
block_1_hash: "{block_hash}"
axiom: "{axiom}"
status: active
monthly_coherence: pending_setup
tags:
  - inneri
  - inneri76
  - client
  - deployment
  - revenue
---

# Client Deployment — {observer}

| Field | Value |
|---|---|
| Observer | {observer} |
| Email | {email} |
| Target vault | {target} |
| Deployed | {date} |
| Block 1 | "{axiom}" |
| Block 1 hash | `{block_hash}` |
| Status | Active |

## Revenue Stream

- [ ] One-time deployment fee collected
- [ ] Monthly coherence pass cron job set up
- [ ] Client added to coherence audit roster

## Monthly Coherence Pass Schedule

When active, Hermes runs an Observer Core pass against this client's vault monthly.
Deliverable: coherence report + drift score + contradiction list.
This is the recurring revenue — the "stream" that keeps paying.

## Related

- [[../hermes-deployments/{date}-activation]] — source vault deployment log
"""
    (receipt_dir / f"{date}-{slug}.md").write_text(content)
    return receipt_dir / f"{date}-{slug}.md"


def deploy(target_path, observer, axiom, email=""):
    target = Path(target_path).expanduser().resolve()
    source = Path(SOURCE_VAULT)
    
    print(f"\n{'='*60}")
    print(f"  IIOIS v{DEPLOY_VERSION} DEPLOYMENT")
    print(f"  Observer: {observer}")
    print(f"  Axiom: \"{axiom}\"")
    print(f"  Target: {target}")
    print(f"{'='*60}\n")
    
    # Step 1: Create skeleton
    n_folders = create_skeleton(target)
    print(f"  [1/7] Created {n_folders} folders")
    
    # Step 2: Copy universal files
    n_copied = copy_universal_files(source, target)
    print(f"  [2/7] Copied {n_copied} universal architecture files")
    
    # Step 3: Write CLAUDE.md
    write_claude_md(target, observer, axiom)
    print(f"  [3/7] Wrote CLAUDE.md (live system prompt)")
    
    # Step 4: Write READMEs
    n_readmes = write_readmes(target)
    print(f"  [4/7] Wrote {n_readmes} folder READMEs")
    
    # Step 5: Write agent registry
    write_agent_registry(target, observer)
    print(f"  [5/7] Wrote AGENT-REGISTRY.md")
    
    # Step 6: Seal Block 1
    ts, block_hash = write_block_1(target, observer, axiom)
    print(f"  [6/7] Sealed Block 1: \"{axiom}\"")
    print(f"         Hash: {block_hash}")
    
    # Step 7: Write receipts
    total_files = n_copied + n_readmes + 4  # +4 for CLAUDE.md, block-1, registry, receipt
    write_deployment_receipt(target, source, observer, axiom, ts, block_hash, total_files)
    source_receipt = write_source_receipt(source, target, observer, axiom, ts, block_hash, email)
    print(f"  [7/7] Wrote deployment receipts (both vaults)")
    
    print(f"\n{'='*60}")
    print(f"  ✅ DEPLOYMENT COMPLETE")
    print(f"  Files written: {total_files}")
    print(f"  Block 1 hash: {block_hash[:32]}...")
    print(f"  Client record: {source_receipt}")
    print(f"{'='*60}\n")
    
    return {
        "target": str(target),
        "observer": observer,
        "axiom": axiom,
        "block_hash": block_hash,
        "timestamp": ts,
        "files": total_files,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy IIOIS v1.0 to a new vault")
    parser.add_argument("--target", required=True, help="Target vault path")
    parser.add_argument("--observer", required=True, help="Observer name")
    parser.add_argument("--axiom", default="Awareness Is Law", help="Block 1 axiom")
    parser.add_argument("--email", default="", help="Client email")
    args = parser.parse_args()
    
    deploy(args.target, args.observer, args.axiom, args.email)
