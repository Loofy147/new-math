# Micro-AGI: Probabilistic Neuro-Symbolic general intelligence framework

An implementation of **Micro-AGI**, a probabilistic neuro-symbolic framework for general intelligence designed around the philosophy of *existential learning* and structured on the **Anastomotic Substrate Architecture (ASA)**.

---

## 🚀 Key Architectural Layers

The architecture consists of five dynamic layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    Layer 4: Noetikon Layer                  │
│          (ما وراء المعرفة – الإشراف والتطور الذاتي)         │
├─────────────────────────────────────────────────────────────┤
│                    Layer 3: Praxis Engine                   │
│        (التعديل الوجداني – المحاكاة العاطفية والدافعية)     │
├─────────────────────────────────────────────────────────────┤
│                Layer 2: World Model / Reasoning             │
│          (التمثيل السببي – المحاكاة والتخطيط)              │
├─────────────────────────────────────────────────────────────┤
│                Layer 1: Cognitive Partition                 │
│        (الذاكرة العاملة – التنسيق والتصيغ المعرفي)          │
├─────────────────────────────────────────────────────────────┤
│                    Layer 0: Interface Layer                 │
│               (التفاعل اللغوي – الواجهة السطحية)            │
└─────────────────────────────────────────────────────────────┘
```

1. **Layer 0 (Interface Layer):** Handles lightweight linguistic encoding/decoding and basic query parsing.
2. **Layer 1 (Cognitive Partition):** Hosts Working Memory, calculates cognitive complexity ($\kappa_i$), and performs query routing via a threshold gate.
3. **Layer 2 (World Model / Reasoning Substrate):** Executes symbolic calculations using `SymPy` and maps state relationships dynamically through a `NetworkX` causal graph. (e.g. Innovative Gravity model: $F = \frac{G m_1 m_2}{r^2} \cdot e^{-\lambda r}$).
4. **Layer 3 (Praxis Engine):** Models internal cognitive friction, evaluates valence/motivation, and ensures objective alignment.
5. **Layer 4 (Noetikon Layer):** Performs metacognition. Coordinates self-evolution using genetic algorithms (`deap`), tracks consistency via a Coherence Supervisor and Reflexive Operator $R$, and preserves memory continuity with a Narrative Identity System.

---

## 📊 Dynamic Performance Metrics

- **Creativity Index (CI):**
  $$CI = \frac{\text{New Concepts}}{\text{Known Concepts}} \times \log(\text{Impact})$$

- **Causal Depth (CD):**
  $$CD = \sum_{i=1}^n \frac{1}{\text{Causal Chain Length}_i}$$

- **Causal Quotient (CQ):**
  $$CQ = \frac{\text{Correct Causal Relations}}{\text{Total Relations}}$$

- **Efficiency:**
  $$\text{Efficiency} = \frac{\text{CausalDepth} \times \text{Creativity}}{\text{Energy} \times \text{Data}}$$

---

## 🛠️ Technology Stack

- **Python 3.12+**
- **SymPy** - Symbolic math representation
- **DEAP** - Genetic algorithms & Self-evolution engine
- **NetworkX** - Causal graph creation & analysis
- **Pydantic** - Data structures and compliance validation

---

## 💻 Quick Start & Demo

Ensure dependencies are installed:
```bash
pip install sympy deap networkx pydantic
```

Run the unit test suite:
```bash
python3 -m unittest discover tests
```

Execute the full pipeline simulation:
```bash
python3 demo.py
```
