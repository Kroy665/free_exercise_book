# Study Plan and Syllabus: WBSSC SLST Mathematics

The content plan and study plan for **WBSSC SLST (Assistant Teacher) Mathematics**: Class IX–X (GRAD, code 86) and Class XI–XII (PG, code 19). The official syllabus is transcribed in [syllabus/wbssc-slst-mathematics.md](syllabus/wbssc-slst-mathematics.md).

**80 topics, 1 written.** Status: ✅ written · 🔲 queued. **IX–XII** = in both syllabi; **XI–XII** = PG syllabus only. Topics are written to PG depth, so every topic serves both papers.

## The plan: 6 months at 1–2 hours a day

Planned for an M.Sc. graduate returning after about 6 years, working full time. The plan starts on 19 Nov 2026 and the exam is assumed to be about 6 months later.

| Phase | Weeks | Dates (approx.) | What |
|---|---|---|---|
| **Learn** | 1–18 | 19 Nov 2026 – 25 Mar 2027 | All 80 topics, in the block order below: about 4–5 topics a week |
| **Consolidate** | 19–22 | 26 Mar – 22 Apr 2027 | Weak topics (Progress page), the Revise queue, mixed custom tests per block |
| **Mock** | 23–26 | 23 Apr – 20 May 2027 | Two full 60-question mock tests a week (IX–X and XI–XII patterns) under exam timing, plus review of every wrong answer |

**A study day (1–2 h):**
1. **Revise first, 10–20 min.** Clear the cards that are due (spaced repetition brings back every wrong answer).
2. **Notes, 30–45 min.** Read today's topic and work the solved examples on paper.
3. **Practice, 30–45 min.** Answer the 30 MCQs with pen and paper, then read every worked solution, including for the ones you got right.

**Each week:** 5 topic days, 1 day for a custom test on the week's topics, and 1 day off or catch-up. On a busy day, do only step 1. The streak is kept and nothing piles up.

**Content keeps ahead of you.** One topic is written a day, while you study 4–5 a week, so each block is ready before you reach it.

## Why this order
- **Computation before abstraction.** After a long gap, algebra, matrices and calculus bring back fluency fast and support everything else.
- **The core first.** Blocks 1–5 are mostly in both syllabi and carry most of the paper. Modern algebra and Analysis II need the fluency regained by then.
- **Algorithmic topics late.** LPP, numerical methods and statistics follow fixed procedures and are quick to learn close to the exam.
- **Mechanics last.** It is the heaviest per topic. Its PG-only parts (statics, virtual work, rigid dynamics) are lowest priority if time runs short.

## How each topic is written
1. **Notes** (`notes.en.md`, English): definitions, theorem statements, standard results and formulas, solved examples, exam shortcuts and common traps. Proofs appear only where the idea is examinable. Graphs and tables are used where they help.
2. **30 MCQs**: mostly computational `single` questions, plus `statements`, `match` and `assertion-reason`, with a worked solution in every explanation. Difficulty mix: about 8 easy, 14 medium, 8 hard.
3. **An independent check**: every answer is recomputed separately (by hand and by script), there must be exactly one correct option, and the statements are compared with standard texts.
4. **Validation** (`tools/content-check/validate.py`, which also renders every formula and graph), then commit.

Subject `math`; folder `content/subjects/math/<unit>/<topic>/`; topic id `math.<unit>.<topic>`.

## Topic queue (study order)


### Block 1: Warm-up: Classical Algebra (Weeks 1–2)

Concrete computation rebuilds speed and confidence after a long gap.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 1 | `math.algebra.complex-numbers` | Complex Numbers and De Moivre's Theorem | Ordered-pair definition, modulus, amplitude, Argand diagram, De Moivre, roots of unity | IX–XII | ✅ |
| 2 | `math.algebra.complex-functions` | Functions of a Complex Variable | exp, sin, cos, Log of z; a^z; inverse circular and hyperbolic functions | IX–XII | 🔲 |
| 3 | `math.algebra.polynomials` | Polynomials and Nature of Roots | Synthetic division, remainder theorem, fundamental theorem, conjugate roots, Descartes' rule, multiple roots, Rolle | IX–XII | 🔲 |
| 4 | `math.algebra.roots-coefficients` | Roots, Coefficients and Transformations | Relations between roots and coefficients, symmetric functions, transformation of equations, reciprocal equations | IX–XII | 🔲 |
| 5 | `math.algebra.cubic-biquadratic` | Cubic and Biquadratic Equations | Cardan's method, Ferrari's method | IX–XII | 🔲 |
| 6 | `math.algebra.inequalities` | Inequalities | AM ≥ GM ≥ HM, Cauchy–Schwarz inequality and applications | XI–XII | 🔲 |
| 7 | `math.algebra.number-theory` | Integers and Divisibility | Well-ordering, induction, division algorithm, GCD, primes, Euclid's theorems, unique factorisation | XI–XII | 🔲 |

### Block 2: Matrices and Linear Algebra (Weeks 3–4)

Mostly mechanical (determinants, rank, eigenvalues), then the vector-space theory.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 8 | `math.linalg.determinants` | Determinants | Properties, minors and cofactors, product, adjoint, symmetric/skew-symmetric, Cramer's rule | IX–XII | 🔲 |
| 9 | `math.linalg.matrices-rank` | Matrices, Inverse and Rank | Matrix algebra, adj A, inverse, elementary operations, rank, normal form, congruence | IX–XII | 🔲 |
| 10 | `math.linalg.linear-systems` | Systems of Linear Equations | Consistency, homogeneous systems, solution space, matrix method | IX–XII | 🔲 |
| 11 | `math.linalg.eigen-cayley-hamilton` | Eigenvalues and Cayley–Hamilton | Characteristic equation, eigenvalues/eigenvectors, Cayley–Hamilton, diagonalisation | IX–XII | 🔲 |
| 12 | `math.linalg.quadratic-forms` | Real Quadratic Forms | Matrix of a form, reduction to normal form, rank, signature, definiteness | IX–XII | 🔲 |
| 13 | `math.linalg.vector-spaces` | Vector Spaces | Subspaces, span, linear independence, basis, dimension, row/column space | IX–XII | 🔲 |
| 14 | `math.linalg.linear-transformations` | Linear Transformations | Null space, range, rank–nullity, Sylvester's law of nullity, matrix w.r.t. bases | XI–XII | 🔲 |
| 15 | `math.linalg.inner-product-spaces` | Inner Product Spaces | Norm, Cauchy–Schwarz, orthogonality, orthonormal basis, Gram–Schmidt | XI–XII | 🔲 |

### Block 3: Calculus and Real Analysis I (Weeks 5–8)

The largest block and the core of both papers.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 16 | `math.analysis.real-numbers` | The Real Number System | Rationals and irrationals, completeness (LUB) axiom, Archimedean property, bounded sets | IX–XII | 🔲 |
| 17 | `math.analysis.sequences` | Sequences | Bounds, limits, monotone sequences, e, Cauchy sequences, Cauchy's limit theorems, subsequences | IX–XII | 🔲 |
| 18 | `math.analysis.series-positive` | Series of Positive Terms | Convergence, Cauchy criterion, comparison, ratio, root, Abel–Pringsheim tests | IX–XII | 🔲 |
| 19 | `math.analysis.series-arbitrary` | Alternating and Arbitrary Series | Leibniz test, absolute and conditional convergence, Abel's and Dirichlet's tests | IX–XII | 🔲 |
| 20 | `math.analysis.limits-continuity` | Limits and Continuity | Cauchy definition, algebra of limits, standard limits, continuity, discontinuities, properties on [a,b] | IX–XII | 🔲 |
| 21 | `math.analysis.mean-value-theorems` | Derivatives and Mean Value Theorems | Differentiability, Leibniz theorem, Rolle, Lagrange, Cauchy MVT, Darboux | IX–XII | 🔲 |
| 22 | `math.analysis.taylor-series` | Taylor's Theorem and Expansions | Taylor and Maclaurin theorems, expansions of eˣ, log(1+x), (1+x)ᵐ, sin x, cos x | XI–XII | 🔲 |
| 23 | `math.analysis.indeterminate-extrema` | Indeterminate Forms, Maxima and Minima | L'Hospital's rule, local extrema, applications | IX–XII | 🔲 |
| 24 | `math.analysis.two-variables` | Functions of Two Variables | Limits, partial derivatives, chain rule, implicit functions, Euler, Schwarz, extrema | IX–XII | 🔲 |
| 25 | `math.analysis.curves` | Tangents, Normals, Asymptotes and Curvature | Tangent/normal, pedal equations, asymptotes, curvature, envelopes, curve tracing | IX–XII | 🔲 |
| 26 | `math.integral.integration-methods` | Methods of Integration | Standard forms, ∫dx/(a+b cos x), (l sin x+m cos x)/(n sin x+p cos x), rational functions | IX–XII | 🔲 |
| 27 | `math.integral.reduction-formulae` | Reduction Formulae | sinᵐx cosⁿx, tanⁿx, secⁿx, 1/(x²+a²)ⁿ and related | IX–XII | 🔲 |
| 28 | `math.integral.definite-integrals` | Definite Integrals | Properties, limit of a sum, standard results | IX–XII | 🔲 |
| 29 | `math.integral.area-length-volume` | Areas, Lengths and Volumes | Quadrature, rectification, volume and surface of revolution, double integrals | IX–XII | 🔲 |

### Block 4: Differential Equations (Week 9)

Short, formula-driven, and high-scoring.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 30 | `math.ode.ode-first-order` | First-Order Equations | Formation, order and degree, separable, homogeneous, exact equations, integrating factors | IX–XII | 🔲 |
| 31 | `math.ode.ode-linear-clairaut` | Linear, Bernoulli and Clairaut Equations | Linear and Bernoulli equations, Clairaut's equation, singular solutions, orthogonal trajectories | IX–XII | 🔲 |
| 32 | `math.ode.ode-higher-order` | Higher-Order Linear Equations | Constant coefficients, CF and PI, D-operator, variation of parameters, Cauchy–Euler | IX–XII | 🔲 |

### Block 5: Analytical Geometry and Vectors (Weeks 10–11)

Standard results and quick computation.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 33 | `math.geometry.axes-conics` | Transformation of Axes and General Conics | Translation, rotation, invariants, general second-degree equation, classification | IX–XII | 🔲 |
| 34 | `math.geometry.pair-of-lines` | Pair of Straight Lines | Condition, angle, bisectors, lines joining origin to intersections with a conic | IX–XII | 🔲 |
| 35 | `math.geometry.tangents-polars` | Tangents, Poles and Polars | Pair of tangents, chord of contact, poles and polars, conjugate points (circle to hyperbola) | IX–XII | 🔲 |
| 36 | `math.geometry.polar-equations` | Polar Equations | Lines, circles, conic with focus as pole; tangent, normal, chord | IX–XII | 🔲 |
| 37 | `math.geometry.planes` | 3D Coordinates and Planes | Direction cosines, projection, plane forms, distance, angle, bisectors | IX–XII | 🔲 |
| 38 | `math.geometry.lines-3d` | Straight Lines in Space | Symmetric and parametric forms, coplanarity, shortest distance between skew lines | IX–XII | 🔲 |
| 39 | `math.geometry.sphere` | The Sphere | General equation, circle, radical plane, tangent plane | XI–XII | 🔲 |
| 40 | `math.geometry.quadrics` | Quadrics | General second-degree equation in three variables, classification | XI–XII | 🔲 |
| 41 | `math.vectors.vector-algebra` | Vector Algebra | Collinearity, coplanarity, scalar/vector/triple products, geometric applications | IX–XII | 🔲 |
| 42 | `math.vectors.vector-applications` | Vector Applications and Calculus | Work, moment, vector equations of lines and planes, tetrahedron volume, vector differentiation | XI–XII | 🔲 |

### Block 6: Modern Algebra (Weeks 12–13)

Abstract, so it is easier once the computational parts are back.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 43 | `math.modalg.sets-relations` | Sets and Relations | Set algebra, De Morgan, Cartesian product, equivalence relations, partitions, partial order, congruence mod n | IX–XII | 🔲 |
| 44 | `math.modalg.mappings` | Mappings | Injective, surjective, bijective maps; composition; inverse and identity maps | IX–XII | 🔲 |
| 45 | `math.modalg.groups` | Groups | Groupoid, semigroup, monoid, group; examples; elementary properties; order of an element | IX–XII | 🔲 |
| 46 | `math.modalg.subgroups-lagrange` | Subgroups, Cosets and Lagrange's Theorem | Subgroup tests, intersection and union, cosets, Lagrange's theorem | IX–XII | 🔲 |
| 47 | `math.modalg.cyclic-permutation-groups` | Cyclic and Permutation Groups | Cyclic groups and generators, permutations, cycles, Sₙ, Aₙ, Klein 4-group | XI–XII | 🔲 |
| 48 | `math.modalg.normal-homomorphism` | Normal Subgroups and Homomorphisms | Normal subgroups, quotient groups, homomorphism, kernel, isomorphism theorem | XI–XII | 🔲 |
| 49 | `math.modalg.rings-fields` | Rings, Integral Domains and Fields | Rings, ℤₙ, integral domains, fields, sub-rings, sub-fields, characteristic | IX–XII | 🔲 |

### Block 7: Real Analysis II (Week 14)

PG-level analysis, built on block 3.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 50 | `math.analysis.point-sets` | Point Sets in ℝ and ℝ² | Countability, open/closed sets, limit points, Bolzano–Weierstrass, Heine–Borel | XI–XII | 🔲 |
| 51 | `math.analysis.uniform-continuity` | Uniform Continuity | Uniform continuity, piecewise continuity, inverse of monotone functions | XI–XII | 🔲 |
| 52 | `math.analysis.riemann-integration` | Riemann Integration | Upper/lower sums, Darboux, integrability conditions, fundamental theorem, mean value theorems | XI–XII | 🔲 |
| 53 | `math.analysis.improper-integrals` | Improper Integrals, Beta and Gamma | Convergence tests, absolute convergence, Beta and Gamma functions | XI–XII | 🔲 |
| 54 | `math.analysis.uniform-convergence` | Sequences and Series of Functions | Pointwise and uniform convergence, Weierstrass M-test, term-by-term operations | XI–XII | 🔲 |
| 55 | `math.analysis.power-series` | Power Series | Radius of convergence, Cauchy–Hadamard, Abel's limit theorem, functions by power series | XI–XII | 🔲 |

### Block 8: Linear Programming and Numerical Analysis (Weeks 15–16)

Algorithmic topics with predictable questions.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 56 | `math.lpp.lpp-graphical` | LPP Formulation and Convex Sets | Formulation, graphical solution, convex sets, extreme points, BFS | IX–XII | 🔲 |
| 57 | `math.lpp.simplex` | The Simplex Method | Standard form, simplex, Big-M, two-phase, degeneracy | IX–XII | 🔲 |
| 58 | `math.lpp.duality` | Duality | Dual problems, duality theorems, complementary slackness | IX–XII | 🔲 |
| 59 | `math.lpp.transportation-assignment` | Transportation and Assignment | Initial solutions, optimality, Hungarian method | IX–XII | 🔲 |
| 60 | `math.numerical.errors-operators` | Errors and Difference Operators | Significant figures, errors, Δ, ∇, E | IX–XII | 🔲 |
| 61 | `math.numerical.interpolation` | Interpolation | Newton forward/backward, Lagrange, divided differences, Stirling, Bessel | IX–XII | 🔲 |
| 62 | `math.numerical.numerical-integration` | Numerical Differentiation and Integration | Trapezoidal, Simpson's 1/3, Weddle; error terms | IX–XII | 🔲 |
| 63 | `math.numerical.roots-of-equations` | Roots of Equations | Bisection, fixed-point iteration, Newton–Raphson, regula falsi | IX–XII | 🔲 |
| 64 | `math.numerical.numerical-ode` | Numerical Solution of ODEs | Euler, RK4, Milne | XI–XII | 🔲 |

### Block 9: Probability and Statistics (Week 17)

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 65 | `math.probability.descriptive-statistics` | Descriptive Statistics | Frequency distributions, mean, median, mode, dispersion, moments | IX–XII | 🔲 |
| 66 | `math.probability.probability-basics` | Probability and Bayes' Theorem | Sample space, classical and axiomatic definitions, conditional probability, independence, Bayes | IX–XII | 🔲 |
| 67 | `math.probability.random-variables` | Random Variables and Expectation | Distribution functions, expectation, variance, MGF, characteristic function | XI–XII | 🔲 |
| 68 | `math.probability.distributions` | Standard Distributions | Binomial, Poisson, uniform, normal, gamma, beta, Cauchy | XI–XII | 🔲 |
| 69 | `math.probability.bivariate` | Bivariate Distributions, Correlation and Regression | Joint and conditional distributions, covariance, correlation, regression lines | XI–XII | 🔲 |
| 70 | `math.probability.limit-theorems` | Limit Theorems | Chebyshev, law of large numbers, normal and Poisson approximations, CLT | XI–XII | 🔲 |
| 71 | `math.probability.sampling-estimation` | Sampling and Estimation | Sampling distributions, χ², t, F, unbiasedness, consistency, MLE, confidence intervals | XI–XII | 🔲 |
| 72 | `math.probability.hypothesis-testing` | Testing of Hypotheses | Simple and composite hypotheses, Neyman–Pearson lemma, likelihood ratio tests | XI–XII | 🔲 |

### Block 10: Mechanics (Week 18)

Heaviest per topic; statics and rigid dynamics are PG-only.

| Q | ID | Topic | Covers | Level | Status |
|---|---|---|---|---|---|
| 73 | `math.mechanics.kinematics` | Kinematics in a Plane | Velocity and acceleration: Cartesian, polar, tangential and normal components | IX–XII | 🔲 |
| 74 | `math.mechanics.rectilinear-motion` | Rectilinear Motion and SHM | Newton's laws, work–energy, SHM, elastic strings, damped and forced oscillation, resisting media | IX–XII | 🔲 |
| 75 | `math.mechanics.projectiles-impact` | Projectiles and Impact | Projectiles in vacuo and resisting media, impulse, elastic impact | IX–XII | 🔲 |
| 76 | `math.mechanics.central-orbits` | Central Orbits | Central forces, inverse square law, Kepler's laws, escape velocity, satellites | IX–XII | 🔲 |
| 77 | `math.mechanics.statics` | Statics of Coplanar Forces | Resolution, moments, couples, reduction, equilibrium | XI–XII | 🔲 |
| 78 | `math.mechanics.friction-cg` | Friction and Centre of Gravity | Laws and cone of friction, rough curves and surfaces, centre of gravity | XI–XII | 🔲 |
| 79 | `math.mechanics.virtual-work` | Virtual Work and Forces in Space | Principle of virtual work, astatic equilibrium, central axis, wrench | XI–XII | 🔲 |
| 80 | `math.mechanics.rigid-dynamics` | Rigid Dynamics | Moments of inertia, D'Alembert, compound pendulum, rolling, Lagrangian | XI–XII | 🔲 |

## Rules
- IDs are permanent once written. New topics get the next free number in their block.
- The first topic of a unit also creates `content/subjects/math/subject.yaml` (if missing) and that unit's `unit.yaml`.
- **Past papers:** if WBSSC SLST maths question papers become available, add their topic weightage here and adjust the order.

