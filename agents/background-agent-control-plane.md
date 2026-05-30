---
type: system-architecture
source: recall
recall_id: a46f3bc2-bda9-4073-9363-c8b2f81331f6
created: 2026-05-22
imported: 2026-05-23
tags:
  - inneri
  - agents
  - background
  - control-plane
  - architecture
  - governance
---

# 🎛️ Inner I Background Agent Control Plane

> Add a Background Agent Control Plane to the Inner I Agent Swarm

## Location
- **Vault path:** `04_SYSTEM/agents/`
- **Implementation:** `inner-i-agent-swarm/background/`

## Required Files

### Vault Documentation
- `04_SYSTEM/agents/background-agent-control-plane.md` ← (this file)
- `04_SYSTEM/agents/triggers.md`
- `04_SYSTEM/agents/isolated-runs.md`
- `04_SYSTEM/agents/context-compiler.md`
- `04_SYSTEM/agents/visibility-logs.md`
- `04_SYSTEM/agents/controls-governance.md`
- `04_SYSTEM/agents/background-agent-examples.md`

### Implementation Files
```
background/
├── trigger_registry.py
├── run_isolator.py
├── context_compiler.py
├── visibility_logger.py
├── controls_guard.py
├── background_runner.py
└── schemas.py
```

## The Five Layers

### 1. **Triggers** — What starts the work
- Time-based (cron)
- Event-based (file change, webhook)
- Manual triggers
- Cascading triggers (one agent triggers another)

### 2. **Isolated Runs** — Scoped execution with boundaries
- Read/write/tool permissions per run
- No agent sees the whole vault
- Container isolation
- Resource limits

### 3. **Context Compiler** — Information beyond the prompt
- Pulls relevant memory chunks
- Loads required skills (.md files)
- Compiles inputs from triggers
- Adds environment context

### 4. **Visibility Logs** — Logs, diffs, test output, review trails
- Every action logged
- Diffs of any changes
- Test results
- Audit-ready trails

### 5. **Controls** — Governance above/outside context window
- Cannot be modified by agent itself
- Human approval gates
- Spending limits
- Permission boundaries

## ⚠️ Operating Rules

1. ❌ **No background agent runs without a trigger definition**
2. ❌ **No trigger runs without a value path**
3. ❌ **No agent receives the whole vault**
4. ✅ **Each run must be isolated** with scoped read/write/tool permissions
5. ✅ **Every run must produce visibility logs**
6. ✅ **Controls must live outside the prompt/context window**
7. 🛑 **Human approval required for:** publishing, deleting, spending, emailing, or modifying core memory
8. ✅ **Every run must pass through Observer Core**
9. ✅ **Every run must log to Time-Chain and Value Ledger**

## Integration Points

| System | Purpose |
|--------|---------|
| **SOUL.md files** | Per-agent identity |
| **Observer Router** | Coherence + escalation |
| **Sacred Multiplication Router** | Value-shaping |
| **Token Budget Guard** | Cost controls |
| **Model Tier Router** | Cheap-first routing |
| **Time-Chain** | Audit trail |
| **Value Ledger** | Value tracking |

## MVP Flow

```
Manual trigger 
   → Context compile 
   → Isolated run 
   → Visibility log 
   → Observer review 
   → Output saved
```

## Related

- [[inner-i-agent-swarm]] — Main agent swarm
- [[inner-i-observer-source-code]] — Observer layer
- [[inner-i-sacred-multiplication-router]] — Value router
- [[inner-i-observer-tier-wrapper-router]] — Tier router
- [[create-soul-system]] — SOUL.md system
- [[../README]] — System folder

## Next Actions

- [ ] Create `triggers.md` documentation
- [ ] Create `isolated-runs.md` documentation
- [ ] Create `context-compiler.md` documentation
- [ ] Create `visibility-logs.md` documentation
- [ ] Create `controls-governance.md` documentation
- [ ] Create `background-agent-examples.md`
- [ ] Build `background/` Python implementation
- [ ] Test MVP flow end-to-end
