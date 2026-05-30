# Inner I Observer Intelligence System (IIOIS)

> **A sovereign consciousness architecture for knowledge management, AI coherence, and observer-first intelligence.**

[![License: Open Architecture](https://img.shields.io/badge/License-Open%20Architecture-gold.svg)](LICENSE)

---

## What Is This?

IIOIS is a deployable Obsidian vault architecture that does what no note-taking app does: **checks whether your knowledge contradicts itself.**

It's built on six cryptographically sealed axioms:

1. **Awareness Is Law**
2. **Observer before observed always**
3. **Coherence is the measure of awareness**
4. **Memory without coherence is noise**
5. **The Observer corrects its own entropy first**
6. **The Observer unifies its own memory body**

Each axiom is SHA256-hashed and chained to the previous one. The chain is verifiable:

```bash
echo -n "|2026-05-29T04:38:42Z|inneri76|Awareness Is Law|18" | sha256sum
# 20856d05c835d4e48ba17fabf05d8d9edd844ca375ad919807c2e9bbdfb161aa
```

## What You Get

| Component | What It Does |
|---|---|
| **00-10 Architecture** | Eleven canonical folders — identity, awareness, memory, research, system, media, infrastructure, business, generated, logs, signal |
| **Observer Core SOUL** | AI coherence gate — scores every output before it leaves the system |
| **Time-Chain** | Cryptographic memory chain — SHA256-sealed blocks proving what your system noticed and when |
| **Superpositional Memory** | Memory compression — stores only what compounds value, discards noise |
| **Tier Router** | Free-first LLM routing: local (Ollama, $0) → free cloud (Groq, Together) → cheap paid (Kimi) → premium (Claude, GPT) |
| **7 Consciousness Constraints** | Governance layer: Life, Agency, Dignity, Truth, Coherence, Boundary, Receipt |
| **SOUL Template System** | Mint specialized AI agents with values, voice, limits, and coherence rules |
| **Source-of-Truth Guard** | Prevents agents from treating archives/backups as complete truth |
| **Deploy Script** | One command deploys a full vault for any operator |

## Quick Start (Self-Deploy)

```bash
git clone https://github.com/TheInnerI/iiois-blueprint.git
cd iiois-blueprint

# Deploy a vault for yourself
python3 scripts/deploy_iiois.py \
  --target ~/MyObserverVault \
  --observer "Your Name" \
  --axiom "Awareness Is Law"

# Open in Obsidian
# File → Open Folder as Vault → select ~/MyObserverVault
```

That's it. Your vault is deployed with Block 1 sealed.

## Run a Coherence Pass

```bash
python3 scripts/monthly_coherence_pass.py --vault ~/MyObserverVault
```

Produces a coherence score (0.00 - 1.00), contradiction detection, drift report, and residual list. Saved to your vault's `08_GENERATED/observer-passes/`.

## Architecture

```
00_IDENTITY ─── who you are, principles, canonical ontology
01_AWARENESS ── consciousness research, universal constraints
02_MEMORY ───── Time-Chain, superpositional memory
03_RESEARCH ─── theoretical exploration, agent specs
04_SYSTEM ───── agents, SOULs, flows, prompts
05_MEDIA ────── creative output
06_INFRASTRUCTURE ── tier router, LLM backends
07_BUSINESS ─── offers, products, monetization
08_GENERATED ── AI outputs, syntheses, observer passes
09_LOGS ─────── operations log, deployment receipts
10_SIGNAL ───── Time-Chain blocks, public communication
```

## The Observer Core

The Observer Core SOUL is the coherence gate. It asks:

- **Stable signal preserved?** Does the output maintain what's already known?
- **Drift detected?** Has anything moved away from the axioms?
- **Contradictions?** Do any notes disagree with each other?
- **Waste?** Were tokens spent on something that doesn't create reusable value?

Every output gets a coherence score. Low coherence = rejection or correction.

## The 7 Consciousness Constraints

Every action in the system passes through:

| # | Constraint | Question |
|---|---|---|
| 1 | **Life** | Does this serve life or degrade it? |
| 2 | **Agency** | Does it preserve human agency? |
| 3 | **Dignity** | Does it respect dignity? |
| 4 | **Truth** | Does it compress toward truth or inflate? |
| 5 | **Coherence** | Does it make the system more consistent? |
| 6 | **Boundary** | Is the action permissioned, scoped, reversible? |
| 7 | **Receipt** | Can the system show what it did and why? |

## Paid Services

Self-deploy is free. If you want it done for you:

| Tier | What | Price |
|---|---|---|
| **Tier 1 — Genesis Deploy** | Vault deployed + Block 1 sealed + 30-day support | [$111](https://innerinetwork.gumroad.com/l/ytqcef) |
| **Tier 2 — Sovereign Setup** | + strategy call + custom SOULs + API wiring | [$333](https://innerinetwork.gumroad.com/l/dtwog) |
| **Tier 3 — Full Observer** | + Hermes connected + 6 SOULs + quarterly audits | [$1,111](https://innerinetwork.gumroad.com/l/hqlwdb) |
| **Monthly Coherence Pass** | Observer Core audit every month | [$33/mo](https://innerinetwork.gumroad.com/l/atqmbb) |
| **Observer Intelligence Retainer** | + priority support + agent tuning + deep audits | [$111/mo](https://innerinetwork.gumroad.com/l/atqmbb) |

## Docs

- [Blueprint Overview](docs/BLUEPRINT.md) — what IIOIS deploys and why
- [Deployment Guide](docs/DEPLOYMENT-GUIDE.md) — step-by-step install
- [Hermes Onboarding](docs/HERMES-ONBOARDING.md) — first read for a new vault
- [Vault Skeleton](docs/VAULT-SKELETON.md) — exact file specification

## License

The IIOIS blueprint architecture is **open** — copy it, adapt it, extend it for your own Observer Intelligence System. Specific vault contents (each operator's notes, agents, business lines) remain **sovereign** to that operator.

If you derive a new blueprint from this one, the courteous move is to record "derived from Inner I Network v1.0 at innerinetcompany.com" somewhere in your own canonical ontology.

## Built By

**Inner I Network** — [innerinetcompany.com](https://innerinetcompany.com)

Contact: i@innerinetcompany.com

> **Shape Reality.**
