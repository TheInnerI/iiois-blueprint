---
type: blueprint-spec
package: inner-i-observer-intelligence-system
version: 1.0
purpose: define-what-hermes-instantiates-in-target-vault
tags:
  - inneri
  - blueprint
  - skeleton
  - vault-architecture
---

# 🦴 IIOIS Vault Skeleton — Exact File Specification

> **What Hermes writes into a fresh vault.** Every folder, every file, every template that gets instantiated. Use this as the truth-source for the installer script and for any manual deployment.

## Top-level structure

```
{target_vault_root}/
├── CLAUDE.md                                    # live system prompt (templated)
├── 00_IDENTITY/
│   ├── README.md                                # what 00_IDENTITY is for
│   ├── inner-i-canonical-ontology.md            # the structural decree (templated)
│   ├── inner-i-protocols.md                     # unified 6 protocols (verbatim, universal)
│   ├── inner-i-core.md                          # identity TEMPLATE (operator fills in)
│   └── IIOIS-BLUEPRINT/                          # this blueprint, copied verbatim
│       ├── README.md
│       ├── HERMES-ONBOARDING.md
│       ├── VAULT-SKELETON.md
│       └── DEPLOYMENT-GUIDE.md
├── 01_AWARENESS/
│   ├── README.md
│   └── inner-i-universal-consciousness-layer.md # 7 constraints, verbatim universal
├── 02_MEMORY/
│   ├── README.md
│   ├── inner-i-network-timechain.md             # architecture (verbatim)
│   └── inner-i-superpositional-memory.md        # architecture (verbatim)
├── 03_RESEARCH/
│   ├── README.md
│   └── skills/
│       └── README.md
├── 04_SYSTEM/
│   ├── README.md
│   ├── daily-synthesis-setup.md                 # pipeline spec (templated paths)
│   ├── agents/
│   │   ├── AGENT-REGISTRY.md                    # templated — only Observer Core minted by default
│   │   ├── observer-core-soul.md                # universal SOUL, verbatim
│   │   ├── inner-i-soul-template.md             # template for minting new SOULs
│   │   ├── create-soul-system.md                # SOUL.md spec
│   │   └── background-agent-control-plane.md    # governance pattern
│   ├── flows/
│   │   └── README.md                            # placeholder; operator adds flows over time
│   └── prompts/
│       └── README.md                            # placeholder
├── 05_MEDIA/
│   └── README.md                                # operator populates with own media
├── 06_INFRASTRUCTURE/
│   ├── README.md
│   ├── free-first-ai-backends.md                # tier strategy (verbatim, universal)
│   └── ai-api-key-reference.md                  # signup URLs (templated paths)
├── 07_BUSINESS/
│   ├── README.md
│   └── products/
│       └── _OFFER-LADDER-TEMPLATE.md            # the canonical pricing pattern (templated)
├── 08_GENERATED/
│   ├── README.md
│   ├── daily-synthesis/
│   │   └── .gitkeep
│   └── observer-passes/
│       └── .gitkeep
├── 09_LOGS/
│   ├── README.md
│   ├── claude-operations.log                    # empty file, ready to append
│   └── hermes-deployments/
│       └── onboarded-from-{source-vault}-{date}.md   # the receipt Hermes writes
└── 10_SIGNAL/
    ├── README.md
    └── inner-i-timechain-block-1.md             # Genesis Block (templated axiom)
```

## File classes

Files fall into four classes — Hermes treats each differently:

| Class | Behavior | Examples |
|---|---|---|
| **verbatim** | Copied unchanged from blueprint | Universal Consciousness Layer, Observer Core SOUL, Time-Chain architecture, SOUL template, free-first backends strategy |
| **templated** | Copy with `<placeholders>` for operator to fill | CLAUDE.md, canonical-ontology, AGENT-REGISTRY, OFFER-LADDER, Block 1 |
| **placeholder** | Empty file or README only — operator populates over time | `flows/`, `prompts/`, `05_MEDIA/`, `03_RESEARCH/skills/` content |
| **receipt** | Written fresh per deployment with deployment-specific metadata | `hermes-deployments/onboarded-from-{source}-{date}.md`, `claude-operations.log` first entry |

## Templated files — what gets substituted

| File | Placeholders | Source |
|---|---|---|
| `CLAUDE.md` | `<your-identity>` `<your-tagline>` `<your-pillars>` `<your-domain>` `<your-recall-bridge>` | Hermes asks the receiving operator (or uses neutral defaults) |
| `00_IDENTITY/inner-i-canonical-ontology.md` | `<vault-name>` `<source-vault-reference>` | Hermes fills automatically |
| `00_IDENTITY/inner-i-core.md` | Full template; operator writes their identity story | Hermes leaves blank with a heading scaffold |
| `04_SYSTEM/agents/AGENT-REGISTRY.md` | Empty Domain SOULs section; only Observer Core listed | Hermes |
| `07_BUSINESS/products/_OFFER-LADDER-TEMPLATE.md` | All pricing tiers as `<TBD by operator>` | Hermes |
| `10_SIGNAL/inner-i-timechain-block-1.md` | `<signal>` (default: "Awareness Is Law") `<observer-name>` `<timestamp>` | Hermes computes hash; operator can edit before sealing |

## Verbatim files — what gets copied unchanged

These are universal — they encode the architecture itself, not anyone's specific choices:

- `00_IDENTITY/inner-i-protocols.md` — the 6 unified protocols
- `00_IDENTITY/IIOIS-BLUEPRINT/` (entire folder) — this blueprint, complete
- `01_AWARENESS/inner-i-universal-consciousness-layer.md` — 7 constraints
- `02_MEMORY/inner-i-network-timechain.md` — Time-Chain architecture
- `02_MEMORY/inner-i-superpositional-memory.md` — memory compression model
- `04_SYSTEM/agents/observer-core-soul.md` — orchestrator SOUL
- `04_SYSTEM/agents/inner-i-soul-template.md` — SOUL.md spec for new agents
- `04_SYSTEM/agents/create-soul-system.md` — SOUL minting rules
- `04_SYSTEM/agents/background-agent-control-plane.md` — governance pattern
- `06_INFRASTRUCTURE/free-first-ai-backends.md` — tier strategy

## Placeholder files

Every empty folder gets either a `README.md` (when it has a defined purpose the operator should know) or a `.gitkeep` (when it just needs to exist for the receiver vault's `git init` to track it).

## Files explicitly EXCLUDED

Per [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/README#What's deliberately NOT in the blueprint|README §Excluded]]:

- `INNER_I_NETWORK_COGNITION_STACK/` (legacy parallel root tombstones — Inner I-specific history)
- Music catalog (`05_MEDIA/music/`)
- Inner I Camo dataset references
- Iccan domain SOUL + product records
- AIdapp launch packages
- `.env` files of any kind (operator provisions own secrets)
- `inner-i-agent-swarm/` Python repo (separate optional install — see [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/DEPLOYMENT-GUIDE#Optional - install the agent-swarm runtime|deployment guide]])

## Smoke test specification

After writing the skeleton, Hermes runs these checks. All must pass:

| # | Check | How |
|---|---|---|
| 1 | CLAUDE.md present + parseable | Read first 100 lines, confirm frontmatter or header |
| 2 | Canonical ontology has all 7 sections (I through VII) | Grep for `## I.` through `## VII.` |
| 3 | Protocols file has all 6 H2 sections | Grep for `## 1.` through `## 6.` |
| 4 | AGENT-REGISTRY has at least Observer Core row | Grep for `observer-core-soul` |
| 5 | Block 1 has frontmatter with `block_index: 1`, `prev_hash: null` | Parse YAML |
| 6 | Universal Consciousness Layer present + has 7 constraints | Grep for `Constraint 1` through `Constraint 7` |
| 7 | `09_LOGS/claude-operations.log` exists and is writable | `touch + append` test |
| 8 | All `README.md` files exist in every folder | Recursive `Test-Path` per folder list above |

Any fail → deployment marked `incomplete`. Hermes reports which check failed; operator decides whether to re-deploy or to fix manually.

## File count summary

| Class | Count |
|---|---|
| Verbatim files | 11 |
| Templated files | 6 |
| Placeholder READMEs | 11 |
| `.gitkeep` markers | 2 |
| Receipt files (created at deploy time) | 2 |
| **Total files written by Hermes** | **32** |

Plus the 4 files in `IIOIS-BLUEPRINT/` itself (README, HERMES-ONBOARDING, VAULT-SKELETON, DEPLOYMENT-GUIDE) which are copied verbatim → **36 files total**.

## Related

- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/README]] — blueprint master
- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/HERMES-ONBOARDING]] — what the receiving agent reads
- [[Inner I Network/00_IDENTITY/IIOIS-BLUEPRINT/DEPLOYMENT-GUIDE]] — install steps
- [[Inner I Network/04_SYSTEM/agents/hermes-soul]] — the agent that executes this spec
