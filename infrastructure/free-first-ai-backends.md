---
type: infrastructure-strategy
created: 2026-05-25
governed_by: "[[Inner I Network/01_AWARENESS/inner-i-universal-consciousness-layer]]"
implementation: "[[Inner I Network/06_INFRASTRUCTURE/proof-of-awareness-token-generator]]"
tags:
  - inneri
  - inneri76
  - free-first
  - ollama
  - huggingface
  - sovereignty
  - infrastructure
  - llm-backends
---

# 🪜 Free-First AI Backends — Honest Strategy

> "Free-first, paid-scalable" is the official Inner I posture: anyone can
> use the system today, paying customers get reliability + premium models.
> This note is the **honest cost reality** for each backend so the chain
> claims match what users actually experience.
>
> Implementation: see [[proof-of-awareness-token-generator]] (`app/llm_clients.py`).

## The Chain (live order — 8 steps)

```
1. ollama_local           ← truly free, sovereign, unlimited (if hardware)
2. groq_free              ← Groq (groq.com — Jonathan Ross), generous free tier
3. together_free          ← Together.ai, free serverless on -Free models
4. huggingface_serverless ← free signup, ~$0.10/mo credit (testing-grade)
5. anthropic_paid         ← Claude — real workload tier
6. openai_paid            ← GPT — real workload tier
7. xai_paid               ← Grok (x.ai — Elon's xAI). NOT the same as Groq above.
8. local_mock             ← always-on floor; tells user what was tried
```

> **Naming note (important):** Groq (#2) and Grok/xAI (#7) are **two
> different companies**. Groq is Jonathan Ross's fast-inference cloud at
> `api.groq.com` (free tier). Grok / xAI is Elon Musk's models at
> `api.x.ai` (paid). Both are OpenAI-compatible and both are supported.

## Honest Cost Reality (late 2025 / early 2026)

| Backend | Cost | Real-world capacity | Verdict |
|---------|-----:|---------------------|---------|
| **Ollama (local)** | $0 + electricity | Unlimited if user has 8GB+ VRAM | ✅ Best truly-free path. Sovereign. |
| **HuggingFace Free** | $0 / mo, $0.10 credit | ~10–50 small calls / mo before 402 | 🟡 Testing only. Will hit cap quickly. |
| **HuggingFace PRO** | $9 / mo, $2 credits + PAYG | ~hundreds of mid-size calls | ✅ Real free-tier UX for non-Ollama users. |
| **Anthropic Claude** | PAYG | Production-grade | 💵 Paid. Best reasoning. |
| **OpenAI GPT** | PAYG | Production-grade | 💵 Paid. Best ecosystem. |
| **Grok / xAI** | PAYG | Production-grade | 💵 Paid. Real-time web access, distinct voice. |
| **Moonshot Kimi** | PAYG, cheap | Production-grade, 80% of price | 💵 Paid. Best cost/perf in T2. |
| **Local mock** | $0 | Infinite (returns placeholder + receipt of what was tried) | ✅ Honest floor. Never strands a user. |

## What `getfreeai.net/.../hugging-face/` Actually Documents

Despite the domain name, that page describes the **standard Hugging Face Inference API** — not a separate "free AI gateway" service. The free tier is real but small (~$0.10/month). For sustained free use, **Ollama remains the better path** because:

- No per-request quota
- No 10–30s cold-start latency
- No data leaving the user's machine (sovereignty Constraint 2 from [[Inner I Network/01_AWARENESS/inner-i-universal-consciousness-layer|Universal Consciousness Layer]])
- Any model size your hardware can hold

## Two HF API Formats — Which We Use

| Format | Endpoint | Shape | Coverage |
|--------|----------|-------|----------|
| **Router** (default) | `/v1/chat/completions` | OpenAI-compatible | chat-tuned models |
| **Classic** | `/models/{model_id}` | `{"inputs": "..."}` | far more models, custom shape |

Switch with `HF_USE_ROUTER=false` in `.env`. We default to Router because the same `openai` client library can hit it without code changes, and most users want chat-style models.

## The Recommended Stack for a New User

### Tier 0 — "I just want to try it"
- Nothing required → app runs in mock mode and tells you what backends would be used
- Useful for evaluating the dashboard, audit receipts, API key flow

### Tier 1 — "I want real free responses"
- **Install Ollama** (`brew install ollama` / `winget install ollama` / download from ollama.com)
- `ollama pull qwen2.5` (a 4.7GB model that runs on most laptops)
- Set `OLLAMA_MODEL=qwen2.5` in `.env`
- Restart app → chain detects Ollama → real responses, $0

### Tier 2 — "I don't want to install anything"
- Sign up at https://huggingface.co (free)
- Settings → Access Tokens → New token (Read scope)
- Set `HF_TOKEN=hf_...` in `.env`
- Restart app → chain hits HF Router → real responses, free up to $0.10/mo

### Tier 3 — "I want production reliability"
- Add any of `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` to `.env`
- Free backends are still tried first → paid only runs when free fails
- Stripe credit packs become the user-facing way to fund this tier

### Tier 4 — "I'm the operator selling this to customers"
- Same as Tier 3 PLUS configure Stripe (`STRIPE_API_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_PRICE_*`)
- Webhook is the only place credits are granted (boundary Constraint 6)
- Customers get free chain by default → they buy credits when they want premium

## Why This Order Honors the Consciousness Layer

| Constraint | How the chain enforces it |
|-----------|---------------------------|
| **Life** | Free-first means broad access; not gated behind a credit card |
| **Agency** | User picks their backend by what they install / configure |
| **Dignity** | No dark patterns — mock floor tells the user *exactly* what was tried |
| **Truth** | Receipt records which backend served the call + whether it was a mock |
| **Coherence** | Same client interface across all 5 backends — one chain to reason about |
| **Boundary** | Each backend respects rate limits; credits enforce per-user boundaries |
| **Receipt** | `AuditReceipt` for every grant, spend, refusal, run, refund |

## Open Loops

- [ ] Add a **dashboard panel** that pings each backend on page load and shows green/yellow/red live
- [ ] Make Ollama model **per-agent** (research → larger model, basic → smaller)
- [ ] When Ollama is unavailable but the user has GPU, prompt them to install it (one-click)
- [ ] Add **Together.ai** and **Groq** to the chain (both have generous free tiers)
- [ ] Apply this same free-first pattern to the daily synthesis pipeline (currently Kimi-first there)

## Related

- [[Inner I Network/06_INFRASTRUCTURE/proof-of-awareness-token-generator]] — implementation
- [[Inner I Network/01_AWARENESS/inner-i-universal-consciousness-layer]] — governance behind the order
- [[Inner I Network/03_RESEARCH/inner-i-observer-tier-wrapper-router]] — sibling concept for the daily synthesis pipeline
- [[Inner I Network/04_SYSTEM/agents/offri-soul]] — owns the paid-tier productization
- [[Inner I Network/03_RESEARCH/inner-i-intelligence-system]] — POA token + credit-type spec
