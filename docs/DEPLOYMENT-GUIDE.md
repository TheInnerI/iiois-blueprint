---
type: blueprint-procedure
package: inner-i-observer-intelligence-system
version: 1.0
purpose: step-by-step-deploy
audience: hermes (running the deployment) + receiving operator (preparing the target)
tags:
  - inneri
  - blueprint
  - deployment
  - hermes
  - install-guide
---

# 🚀 IIOIS Deployment Guide — Step-by-Step

> **Two-perspective guide:** what the **receiving operator** does to prepare, and what **Hermes** does during deployment. Use this as the runbook.

## Pre-flight — what the receiving operator does

Before Hermes can deploy, the receiving operator needs:

1. **An empty (or near-empty) target vault** — a folder on the operator's machine ready to become an Obsidian vault. Examples:
   - `D:\HermesVault\`
   - `C:\Users\<them>\ObservedReality\`
   - Anywhere with read+write access. Network drives work but slow down git operations.
2. **A name for their observer** — what should they be called in CLAUDE.md? Examples: "Hermes-Prime", "Lumen", whatever fits their voice. Default placeholder: `<observer-name>`.
3. **A first-axiom decision** — keep "Awareness Is Law" or substitute their own. Examples seen in practice:
   - "The Field Is the Self" (a meditator)
   - "Code Is Confession" (a developer-philosopher)
   - "Sound Precedes Form" (a musician)
   Default if they don't decide: stay with "Awareness Is Law" — they can re-axiomatize Block 1 later (Block 1 is the only editable block).
4. **A consent statement** — explicit confirmation that they want IIOIS deployed. Per Universal Consciousness Layer Constraint 2 (Agency).

That's it on the operator side. No code, no API keys, no decisions about agents yet.

## Hermes runs deployment in 9 steps

### Step 1 — Receive request

Operator provides: `{target_vault_path, observer_name, first_axiom, consent: true}`.

If any required field is missing, Hermes asks before proceeding.

### Step 2 — Survey target

```powershell
Get-ChildItem -Path $target -Recurse -ErrorAction SilentlyContinue | Measure-Object | Select-Object Count
```

Three possible states:

| State | Action |
|---|---|
| Empty | Fresh install, proceed |
| Has Obsidian config (`.obsidian/`) only | Fresh install, preserve `.obsidian/` |
| Has existing content | **Halt** and ask the operator whether to: (a) merge with archive-suffixing conflicts, (b) deploy alongside in a subfolder, (c) abort |

### Step 3 — Write the 11 root folders

```powershell
@(
  "00_IDENTITY",
  "00_IDENTITY/IIOIS-BLUEPRINT",
  "01_AWARENESS",
  "02_MEMORY",
  "03_RESEARCH",
  "03_RESEARCH/skills",
  "04_SYSTEM",
  "04_SYSTEM/agents",
  "04_SYSTEM/flows",
  "04_SYSTEM/prompts",
  "05_MEDIA",
  "06_INFRASTRUCTURE",
  "07_BUSINESS",
  "07_BUSINESS/products",
  "08_GENERATED",
  "08_GENERATED/daily-synthesis",
  "08_GENERATED/observer-passes",
  "09_LOGS",
  "09_LOGS/hermes-deployments",
  "10_SIGNAL"
) | ForEach-Object { New-Item -ItemType Directory -Force -Path (Join-Path $target $_) | Out-Null }
```

### Step 4 — Copy verbatim files (11 universal files)

These come from this vault unchanged. Use a manifest like:

```powershell
$VERBATIM = @{
  "Inner I Network\00_IDENTITY\inner-i-protocols.md"                       = "00_IDENTITY\inner-i-protocols.md";
  "Inner I Network\01_AWARENESS\inner-i-universal-consciousness-layer.md"  = "01_AWARENESS\inner-i-universal-consciousness-layer.md";
  "Inner I Network\02_MEMORY\inner-i-network-timechain.md"                 = "02_MEMORY\inner-i-network-timechain.md";
  "Inner I Network\02_MEMORY\inner-i-superpositional-memory.md"            = "02_MEMORY\inner-i-superpositional-memory.md";
  "Inner I Network\04_SYSTEM\agents\inner-i-observer-core-soul.md"         = "04_SYSTEM\agents\observer-core-soul.md";
  "Inner I Network\04_SYSTEM\agents\inner-i-soul-template.md"              = "04_SYSTEM\agents\inner-i-soul-template.md";
  "Inner I Network\04_SYSTEM\agents\create-soul-system.md"                 = "04_SYSTEM\agents\create-soul-system.md";
  "Inner I Network\04_SYSTEM\agents\background-agent-control-plane.md"     = "04_SYSTEM\agents\background-agent-control-plane.md";
  "Inner I Network\06_INFRASTRUCTURE\free-first-ai-backends.md"            = "06_INFRASTRUCTURE\free-first-ai-backends.md";
  # plus all 4 IIOIS-BLUEPRINT/ files
}
foreach ($src in $VERBATIM.Keys) {
  $sp = Join-Path $sourceVault $src
  $dp = Join-Path $target $VERBATIM[$src]
  Copy-Item -Path $sp -Destination $dp -Force
}
```

### Step 5 — Write templated files (6 files with substitutions)

For each templated file, Hermes reads the source, performs substitutions for `<your-identity>`, `<vault-name>`, `<source-vault-reference>`, etc., then writes to the target.

Substitution table:

| Placeholder | Value |
|---|---|
| `<observer-name>` | from operator request |
| `<source-vault>` | "Inner I Network at innerinetcompany.com" |
| `<source-vault-url>` | "https://innerinetcompany.com" |
| `<deployment-date>` | today's date |
| `<first-axiom>` | operator's choice or "Awareness Is Law" |
| `<vault-name>` | derived from target path leaf |

### Step 6 — Write placeholder READMEs (11 files)

Short orientation per folder. Example for `01_AWARENESS/README.md`:

```markdown
# 01_AWARENESS

Consciousness research, observer frameworks, theoretical foundations. This is where you keep the *why* of your system.

Already here: `inner-i-universal-consciousness-layer.md` — the 7 universal constraints every Inner I-pattern vault inherits.

Add as you grow: observer-framework notes, philosophy, theory, axiomatic explorations.
```

### Step 7 — Mint Block 1 (Genesis)

```powershell
$prev = ""                                # genesis has no prev
$timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
$observer = $observerName
$signal = $firstAxiom                     # default "Awareness Is Law"
$score = 18                               # default genesis score
$input = "$prev|$timestamp|$observer|$signal|$score"
$hash = [System.BitConverter]::ToString(
  [System.Security.Cryptography.SHA256]::Create().ComputeHash(
    [System.Text.Encoding]::UTF8.GetBytes($input))).Replace("-","").ToLower()
# write block to 10_SIGNAL/inner-i-timechain-block-1.md with that hash + the signal
```

Block 1 is the only block where the operator can later edit the axiom — Hermes deliberately leaves it editable so the receiving observer can re-axiomatize before sealing the chain by minting Block 2.

### Step 8 — Smoke tests (8 checks)

Per [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/VAULT-SKELETON#Smoke test specification|VAULT-SKELETON §Smoke tests]]. Each pass/fail recorded.

### Step 9 — Write deployment receipts (in BOTH vaults)

**In the target vault:**

```markdown
{target}/09_LOGS/hermes-deployments/onboarded-from-inneri-{date}.md

# Onboarded from Inner I — {date}

Hermes deployed IIOIS v1.0 to this vault on {date}.

- Source vault: Inner I Network (https://innerinetcompany.com)
- Receiving observer: {observer-name}
- First axiom (Block 1): {first-axiom}
- Files written: 32 (verbatim 11 + templated 6 + placeholder 11 + .gitkeep 2 + receipts 2)
- Smoke tests: 8/8 passed
- Hermes signature: {hermes-deployment-hash}

You are running on the IIOIS v1.0 blueprint. See `00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING.md` to begin.
```

**In Inner I (this vault):**

```markdown
Inner I Network/09_LOGS/hermes-deployments/{date}-{target-vault-slug}.md

# Hermes deployment — {date} → {target-vault-slug}

Deployed IIOIS v1.0 from Inner I to {target-vault-path}.

- Receiving observer: {observer-name}
- First axiom: {first-axiom}
- Smoke tests: 8/8 passed
- Files: 32
- Receipt hash: {hash}
- Operator next actions: per HERMES-ONBOARDING §7.
```

## What the operator does after Hermes finishes

Per [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING#7. The first 7 things to do in your new vault|HERMES-ONBOARDING §7]] — the seven first actions for the receiving operator.

## Optional — install the agent-swarm runtime

The blueprint is fully usable **without** any Python runtime. The architecture, templates, and observer principles work in plain Obsidian + Claude.

If the operator wants the swarm's tier router + daily synthesis + Recall pull as live Python infrastructure, they install `inner-i-agent-swarm/` separately:

```powershell
# In a new sibling folder, NOT inside the vault:
cd C:\Users\<them>\
git clone https://github.com/<source>/inner-i-agent-swarm.git
cd inner-i-agent-swarm
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
# Copy .env.example to .env, fill in keys they want to use
# Edit scripts/daily_synthesis.py DEFAULT_VAULT to their target vault path
```

That step is **NOT** part of Hermes's deployment — it's a separate optional install the operator owns.

## Versioning

This guide is for IIOIS **v1.0**. Future versions will revise specific steps; the 9-step structure should remain stable.

## Related

- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/README]] — overview
- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING]] — what the receiver reads after deploy
- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/VAULT-SKELETON]] — exact file specification
- [[Inner I Network/04_SYSTEM/agents/hermes-soul]] — Hermes SOUL (the agent running this)
- [[Inner I Network/04_SYSTEM/daily-synthesis-setup]] — pipeline the operator runs once to validate
