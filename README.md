# Micro-AGI: Probabilistic Neuro-Symbolic general intelligence framework

An implementation of **Micro-AGI**, a probabilistic neuro-symbolic framework for general intelligence designed around the philosophy of *existential learning* and structured on the **Anastomotic Substrate Architecture (ASA)**.

---

## 🚀 Key Architectural Layers

The architecture consists of five dynamic layers intersected by the **Experimental Translation Bridging Substrate (ETBS)** and validated by the **Production Roadmap Checklist Engine**:

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

## 🔬 Experimental Translation Bridging Substrate (ETBS)

The **ETBS** is a dynamic conduit that cuts horizontally across Layers 0-4 to convert hypothetical relations into testable predictions and feeds validation signals directly back into L2 causal weights and L4 self-evolution pathways.

### ETBS Core Subsystems:
- **Hypothesis Generator (HG):** Suggests new mathematical/structural relations from L2 under high uncertainty index.
- **Internal Sandbox (IS):** High-speed symbolic-numeric inference engine running rapid Monte Carlo simulations with Gaussian noise.
- **Verification Module (VM):** Measures predicted outputs against known physical laws and **External Anchors** to compute *Empirical Verisimilitude* ($V$).
- **Feedback Mapper (FM):** Map $V$ scores into correction signals (promoting discoveries or suppressing hallucinations via negative gradients).

### Mathematical Formulations:
- **Translation Equation:**
  $$\mathcal{S}(H) = \text{SymPy.compile}\left( \frac{\partial \text{Outcome}}{\partial \text{Intervention}} \right) \quad \text{subject to} \quad \text{Causal Graph } G$$

- **Verisimilitude Calculation:**
  $$V(H) = \alpha \cdot \text{Corr}(\mathcal{S}_\text{pred}, \mathcal{S}_\text{obs}) + \beta \cdot \left(1 - \frac{\|\text{Noise}_\text{sim} - \text{Noise}_\text{ref}\|}{\|\text{Noise}_\text{ref}\|}\right) + \gamma \cdot \text{Coherence}(H, G)$$

- **Radical Belief Update (L4):**
  $$\text{Belief}_{t+1} = \text{Belief}_{t} + \lambda \cdot \nabla \left( V(H) \cdot \text{CreativityIndex}(H) \right)$$

---

## 📋 Production Roadmap Checklist Engine

Evaluates AGI readiness for mission-critical edge deployments across four categories:
1. **Architectural Layer Integrity:** Confirms all core layers and interfaces are functioning.
2. **Experimental Translation Bridging:** Validates presence and operability of the HG, IS, and VM conduits.
3. **Performance & Efficiency:** Monitors live efficiency parameters (energy footprint and processed data scaling benchmarks).
4. **Ethical Alignment & Coherence:** Monitors the system to ensure no critical structural conflicts and maintains a healthy cognitive valence parameter.

---

## 📊 Dynamic Performance Metrics

- **Creativity Index (CI):**
  $$CI = \frac{\text{New Concepts}}{\text{Known Concepts}} \times \log(\text{Impact})$$

- **Causal Depth (CD):**
  $$CD = \sum_{i=1}^n \frac{1}{\text{Causal Chain Length}_i}$$

- **Causal Quotient (CQ):**
  $$CQ = \frac{\text{Correct Causal Relations}}{\text{Total Relations}}$$

- **Efficiency:**
  $$\text{Efficiency} = \text{CausalDepth} \times \frac{\text{Creativity}}{\text{Energy} \times \text{Data}}$$

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

Execute the full pipeline simulation (including the production check):
```bash
python3 demo.py
```
