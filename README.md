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

## 🧠 Micro-AGI v3.0 (Atlas Edition)

Micro-AGI v3.0 introduces deep structural integrations directly derived from the **Universal Leverage Atlas**, refining self-proving guarantees, resilience, and noise-robust active discovery:

1. **Upgrade A (Zero-Knowledge Attestation - Entry 26):**
   When the engine discovers a physical law or promotes a model, it generates a lightweight cryptographic commitment of parameters using SHA-256 and provides verification proofs on independent datasets without revealing the internal model structure.

2. **Upgrade B (Model Zoo with N-1 Contingency - Entry 10):**
   The engine maintains an active ensemble of diverse models representing different mathematical structural families (Polynomial, Exponential, Trigonometric, Hybrid). If the best-performing model fails, the system triggers N-1 contingency, falling back onto secondary models in the zoo without stopping discovery.

3. **Upgrade C (Correlation Filter - Entry 30):**
   To prevent search space bloat and severe overfitting in highly collinear environments, candidate terms are filtered using Pearson correlation. Terms with $|\rho| > 0.995$ relative to existing terms are discarded.

4. **Diagnosis A (Weak Ties - Entry 5):**
   To avoid closed-loop echo chambers, the system injects periodic "weak ties" (external datasets/unrelated mathematical rules) every 5 generations to maintain network distance and global generalizability.

5. **Diagnosis B (Camouflaged Active Sampling - Entry 21):**
   Instead of raw BALD active query points, the system executes **Camouflaged BALD queries (The Kyle Model)**. True target inquiry points are blended with randomized "distractor" query points at a controlled ratio (1.5x) to prevent adversaries or external agents from reconstructing model weaknesses.

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
