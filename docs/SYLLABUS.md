# Roadmap and Syllabus: WBSSC SLST Mathematics

The content plan for Free Exercise Book: the **WBSSC SLST (Assistant Teacher) Mathematics** syllabus for Class IX–X (GRAD, code 86) and Class XI–XII (PG, code 19). The official syllabus, transcribed, is in [syllabus/wbssc-slst-mathematics.md](syllabus/wbssc-slst-mathematics.md).

**80 topics.** **Progress: 0 / 80 written.** Status: ✅ written · 🔲 queued.

Level: **IX–XII** means the topic is in both syllabi (written to PG depth, so it serves both). **XI–XII** means the topic is in the PG syllabus only.

## Who the content is for
Readers who studied mathematics to B.Sc./M.Sc. level and are **revising**, not learning from scratch. Notes are compact: definitions, theorem statements, standard results and formulas, solved examples and exam shortcuts. Proofs only where a proof idea is itself examined. Questions are exam-style MCQs (the written test is 60 MCQs, no negative marking) with a **worked solution** in every explanation.

## Roadmap
| Phase | What | Topics | Days (1 topic/day) |
|---|---|---|---|
| 0 | App: maths support (formula rendering with KaTeX, worked-solution layout) | n/a | before content |
| 1 | Core topics in both syllabi (IX–XII) | 53 | 53 |
| 2 | PG-only topics (XI–XII) | 27 | 27 |
| 3 | Full-length mock tests (60 Q) and topic-mixed revision sets | ongoing | n/a |

## How content is produced (one topic per day)
1. **Write** `topic.yaml`, `notes.en.md` (English only for now; formulas in LaTeX `$…$` / `$$…$$`) and `questions.yaml` (30 MCQs, mostly `single`, with some `statements`, `match` and `assertion-reason`; numerical answers worked out step by step in `explanation`).
2. **Verify** in a separate pass: every numerical answer recomputed independently (by hand and with a quick script where possible), exactly one correct option, theorem statements checked against standard texts.
3. **Validate** with `python3 -I tools/content-check/validate.py content`, add the topic to its `unit.yaml`, mark it ✅ here, open a pull request.

Subject id `math`; folder `content/subjects/math/<unit>/<topic>/`; topic id `math.<unit>.<topic>`.

## Daily queue


### Phase 1: core topics (IX–XII)

| Q | ID | Unit | Topic | Covers | Level | Status |
|---|---|---|---|---|---|---|
| 1 | `math.algebra.complex-numbers` | Classical Algebra | Complex Numbers and De Moivre's Theorem | Ordered-pair definition, modulus, amplitude, Argand diagram, De Moivre, roots of unity | IX–XII | 🔲 |
| 2 | `math.algebra.complex-functions` | Classical Algebra | Functions of a Complex Variable | exp, sin, cos, Log of z; a^z; inverse circular and hyperbolic functions | IX–XII | 🔲 |
| 3 | `math.algebra.polynomials` | Classical Algebra | Polynomials and Nature of Roots | Synthetic division, remainder theorem, fundamental theorem, conjugate roots, Descartes' rule, multiple roots, Rolle | IX–XII | 🔲 |
| 4 | `math.algebra.roots-coefficients` | Classical Algebra | Roots, Coefficients and Transformations | Relations between roots and coefficients, symmetric functions, transformation of equations, reciprocal equations | IX–XII | 🔲 |
| 5 | `math.algebra.cubic-biquadratic` | Classical Algebra | Cubic and Biquadratic Equations | Cardan's method, Ferrari's method | IX–XII | 🔲 |
| 6 | `math.linalg.determinants` | Matrices and Linear Algebra | Determinants | Properties, minors and cofactors, product, adjoint, symmetric/skew-symmetric, Cramer's rule | IX–XII | 🔲 |
| 7 | `math.linalg.matrices-rank` | Matrices and Linear Algebra | Matrices, Inverse and Rank | Matrix algebra, adj A, inverse, elementary operations, rank, normal form, congruence | IX–XII | 🔲 |
| 8 | `math.linalg.linear-systems` | Matrices and Linear Algebra | Systems of Linear Equations | Consistency, homogeneous systems, solution space, matrix method | IX–XII | 🔲 |
| 9 | `math.linalg.vector-spaces` | Matrices and Linear Algebra | Vector Spaces | Subspaces, span, linear independence, basis, dimension, row/column space | IX–XII | 🔲 |
| 10 | `math.linalg.eigen-cayley-hamilton` | Matrices and Linear Algebra | Eigenvalues and Cayley–Hamilton | Characteristic equation, eigenvalues/eigenvectors, Cayley–Hamilton, diagonalisation | IX–XII | 🔲 |
| 11 | `math.linalg.quadratic-forms` | Matrices and Linear Algebra | Real Quadratic Forms | Matrix of a form, reduction to normal form, rank, signature, definiteness | IX–XII | 🔲 |
| 12 | `math.modalg.sets-relations` | Modern Algebra | Sets and Relations | Set algebra, De Morgan, Cartesian product, equivalence relations, partitions, partial order, congruence mod n | IX–XII | 🔲 |
| 13 | `math.modalg.mappings` | Modern Algebra | Mappings | Injective, surjective, bijective maps; composition; inverse and identity maps | IX–XII | 🔲 |
| 14 | `math.modalg.groups` | Modern Algebra | Groups | Groupoid, semigroup, monoid, group; examples; elementary properties; order of an element | IX–XII | 🔲 |
| 15 | `math.modalg.subgroups-lagrange` | Modern Algebra | Subgroups, Cosets and Lagrange's Theorem | Subgroup tests, intersection and union, cosets, Lagrange's theorem | IX–XII | 🔲 |
| 16 | `math.modalg.rings-fields` | Modern Algebra | Rings, Integral Domains and Fields | Rings, ℤₙ, integral domains, fields, sub-rings, sub-fields, characteristic | IX–XII | 🔲 |
| 17 | `math.analysis.real-numbers` | Real Analysis and Differential Calculus | The Real Number System | Rationals and irrationals, completeness (LUB) axiom, Archimedean property, bounded sets | IX–XII | 🔲 |
| 18 | `math.analysis.sequences` | Real Analysis and Differential Calculus | Sequences | Bounds, limits, monotone sequences, e, Cauchy sequences, Cauchy's limit theorems, subsequences | IX–XII | 🔲 |
| 19 | `math.analysis.series-positive` | Real Analysis and Differential Calculus | Series of Positive Terms | Convergence, Cauchy criterion, comparison, ratio, root, Abel–Pringsheim tests | IX–XII | 🔲 |
| 20 | `math.analysis.series-arbitrary` | Real Analysis and Differential Calculus | Alternating and Arbitrary Series | Leibniz test, absolute and conditional convergence, Abel's and Dirichlet's tests | IX–XII | 🔲 |
| 21 | `math.analysis.limits-continuity` | Real Analysis and Differential Calculus | Limits and Continuity | Cauchy definition, algebra of limits, standard limits, continuity, discontinuities, properties on [a,b] | IX–XII | 🔲 |
| 22 | `math.analysis.mean-value-theorems` | Real Analysis and Differential Calculus | Derivatives and Mean Value Theorems | Differentiability, Leibniz theorem, Rolle, Lagrange, Cauchy MVT, Darboux | IX–XII | 🔲 |
| 23 | `math.analysis.indeterminate-extrema` | Real Analysis and Differential Calculus | Indeterminate Forms, Maxima and Minima | L'Hospital's rule, local extrema, applications | IX–XII | 🔲 |
| 24 | `math.analysis.curves` | Real Analysis and Differential Calculus | Tangents, Normals, Asymptotes and Curvature | Tangent/normal, pedal equations, asymptotes, curvature, envelopes, curve tracing | IX–XII | 🔲 |
| 25 | `math.analysis.two-variables` | Real Analysis and Differential Calculus | Functions of Two Variables | Limits, partial derivatives, chain rule, implicit functions, Euler, Schwarz, extrema | IX–XII | 🔲 |
| 26 | `math.integral.integration-methods` | Integral Calculus | Methods of Integration | Standard forms, ∫dx/(a+b cos x), (l sin x+m cos x)/(n sin x+p cos x), rational functions | IX–XII | 🔲 |
| 27 | `math.integral.reduction-formulae` | Integral Calculus | Reduction Formulae | sinᵐx cosⁿx, tanⁿx, secⁿx, 1/(x²+a²)ⁿ and related | IX–XII | 🔲 |
| 28 | `math.integral.definite-integrals` | Integral Calculus | Definite Integrals | Properties, limit of a sum, standard results | IX–XII | 🔲 |
| 29 | `math.integral.area-length-volume` | Integral Calculus | Areas, Lengths and Volumes | Quadrature, rectification, volume and surface of revolution, double integrals | IX–XII | 🔲 |
| 30 | `math.ode.ode-first-order` | Differential Equations | First-Order Equations | Formation, order and degree, separable, homogeneous, exact equations, integrating factors | IX–XII | 🔲 |
| 31 | `math.ode.ode-linear-clairaut` | Differential Equations | Linear, Bernoulli and Clairaut Equations | Linear and Bernoulli equations, Clairaut's equation, singular solutions, orthogonal trajectories | IX–XII | 🔲 |
| 32 | `math.ode.ode-higher-order` | Differential Equations | Higher-Order Linear Equations | Constant coefficients, CF and PI, D-operator, variation of parameters, Cauchy–Euler | IX–XII | 🔲 |
| 33 | `math.geometry.axes-conics` | Analytical Geometry | Transformation of Axes and General Conics | Translation, rotation, invariants, general second-degree equation, classification | IX–XII | 🔲 |
| 34 | `math.geometry.pair-of-lines` | Analytical Geometry | Pair of Straight Lines | Condition, angle, bisectors, lines joining origin to intersections with a conic | IX–XII | 🔲 |
| 35 | `math.geometry.tangents-polars` | Analytical Geometry | Tangents, Poles and Polars | Pair of tangents, chord of contact, poles and polars, conjugate points (circle to hyperbola) | IX–XII | 🔲 |
| 36 | `math.geometry.polar-equations` | Analytical Geometry | Polar Equations | Lines, circles, conic with focus as pole; tangent, normal, chord | IX–XII | 🔲 |
| 37 | `math.geometry.planes` | Analytical Geometry | 3D Coordinates and Planes | Direction cosines, projection, plane forms, distance, angle, bisectors | IX–XII | 🔲 |
| 38 | `math.geometry.lines-3d` | Analytical Geometry | Straight Lines in Space | Symmetric and parametric forms, coplanarity, shortest distance between skew lines | IX–XII | 🔲 |
| 39 | `math.vectors.vector-algebra` | Vectors | Vector Algebra | Collinearity, coplanarity, scalar/vector/triple products, geometric applications | IX–XII | 🔲 |
| 40 | `math.mechanics.kinematics` | Mechanics | Kinematics in a Plane | Velocity and acceleration: Cartesian, polar, tangential and normal components | IX–XII | 🔲 |
| 41 | `math.mechanics.rectilinear-motion` | Mechanics | Rectilinear Motion and SHM | Newton's laws, work–energy, SHM, elastic strings, damped and forced oscillation, resisting media | IX–XII | 🔲 |
| 42 | `math.mechanics.projectiles-impact` | Mechanics | Projectiles and Impact | Projectiles in vacuo and resisting media, impulse, elastic impact | IX–XII | 🔲 |
| 43 | `math.mechanics.central-orbits` | Mechanics | Central Orbits | Central forces, inverse square law, Kepler's laws, escape velocity, satellites | IX–XII | 🔲 |
| 44 | `math.lpp.lpp-graphical` | Linear Programming | LPP Formulation and Convex Sets | Formulation, graphical solution, convex sets, extreme points, BFS | IX–XII | 🔲 |
| 45 | `math.lpp.simplex` | Linear Programming | The Simplex Method | Standard form, simplex, Big-M, two-phase, degeneracy | IX–XII | 🔲 |
| 46 | `math.lpp.duality` | Linear Programming | Duality | Dual problems, duality theorems, complementary slackness | IX–XII | 🔲 |
| 47 | `math.lpp.transportation-assignment` | Linear Programming | Transportation and Assignment | Initial solutions, optimality, Hungarian method | IX–XII | 🔲 |
| 48 | `math.numerical.errors-operators` | Numerical Analysis | Errors and Difference Operators | Significant figures, errors, Δ, ∇, E | IX–XII | 🔲 |
| 49 | `math.numerical.interpolation` | Numerical Analysis | Interpolation | Newton forward/backward, Lagrange, divided differences, Stirling, Bessel | IX–XII | 🔲 |
| 50 | `math.numerical.numerical-integration` | Numerical Analysis | Numerical Differentiation and Integration | Trapezoidal, Simpson's 1/3, Weddle; error terms | IX–XII | 🔲 |
| 51 | `math.numerical.roots-of-equations` | Numerical Analysis | Roots of Equations | Bisection, fixed-point iteration, Newton–Raphson, regula falsi | IX–XII | 🔲 |
| 52 | `math.probability.descriptive-statistics` | Probability and Statistics | Descriptive Statistics | Frequency distributions, mean, median, mode, dispersion, moments | IX–XII | 🔲 |
| 53 | `math.probability.probability-basics` | Probability and Statistics | Probability and Bayes' Theorem | Sample space, classical and axiomatic definitions, conditional probability, independence, Bayes | IX–XII | 🔲 |

### Phase 2: PG-only topics (XI–XII)

| Q | ID | Unit | Topic | Covers | Level | Status |
|---|---|---|---|---|---|---|
| 54 | `math.algebra.number-theory` | Classical Algebra | Integers and Divisibility | Well-ordering, induction, division algorithm, GCD, primes, Euclid's theorems, unique factorisation | XI–XII | 🔲 |
| 55 | `math.algebra.inequalities` | Classical Algebra | Inequalities | AM ≥ GM ≥ HM, Cauchy–Schwarz inequality and applications | XI–XII | 🔲 |
| 56 | `math.linalg.linear-transformations` | Matrices and Linear Algebra | Linear Transformations | Null space, range, rank–nullity, Sylvester's law of nullity, matrix w.r.t. bases | XI–XII | 🔲 |
| 57 | `math.linalg.inner-product-spaces` | Matrices and Linear Algebra | Inner Product Spaces | Norm, Cauchy–Schwarz, orthogonality, orthonormal basis, Gram–Schmidt | XI–XII | 🔲 |
| 58 | `math.modalg.cyclic-permutation-groups` | Modern Algebra | Cyclic and Permutation Groups | Cyclic groups and generators, permutations, cycles, Sₙ, Aₙ, Klein 4-group | XI–XII | 🔲 |
| 59 | `math.modalg.normal-homomorphism` | Modern Algebra | Normal Subgroups and Homomorphisms | Normal subgroups, quotient groups, homomorphism, kernel, isomorphism theorem | XI–XII | 🔲 |
| 60 | `math.analysis.point-sets` | Real Analysis and Differential Calculus | Point Sets in ℝ and ℝ² | Countability, open/closed sets, limit points, Bolzano–Weierstrass, Heine–Borel | XI–XII | 🔲 |
| 61 | `math.analysis.taylor-series` | Real Analysis and Differential Calculus | Taylor's Theorem and Expansions | Taylor and Maclaurin theorems, expansions of eˣ, log(1+x), (1+x)ᵐ, sin x, cos x | XI–XII | 🔲 |
| 62 | `math.analysis.uniform-continuity` | Real Analysis and Differential Calculus | Uniform Continuity | Uniform continuity, piecewise continuity, inverse of monotone functions | XI–XII | 🔲 |
| 63 | `math.analysis.riemann-integration` | Real Analysis and Differential Calculus | Riemann Integration | Upper/lower sums, Darboux, integrability conditions, fundamental theorem, mean value theorems | XI–XII | 🔲 |
| 64 | `math.analysis.improper-integrals` | Real Analysis and Differential Calculus | Improper Integrals, Beta and Gamma | Convergence tests, absolute convergence, Beta and Gamma functions | XI–XII | 🔲 |
| 65 | `math.analysis.uniform-convergence` | Real Analysis and Differential Calculus | Sequences and Series of Functions | Pointwise and uniform convergence, Weierstrass M-test, term-by-term operations | XI–XII | 🔲 |
| 66 | `math.analysis.power-series` | Real Analysis and Differential Calculus | Power Series | Radius of convergence, Cauchy–Hadamard, Abel's limit theorem, functions by power series | XI–XII | 🔲 |
| 67 | `math.geometry.sphere` | Analytical Geometry | The Sphere | General equation, circle, radical plane, tangent plane | XI–XII | 🔲 |
| 68 | `math.geometry.quadrics` | Analytical Geometry | Quadrics | General second-degree equation in three variables, classification | XI–XII | 🔲 |
| 69 | `math.vectors.vector-applications` | Vectors | Vector Applications and Calculus | Work, moment, vector equations of lines and planes, tetrahedron volume, vector differentiation | XI–XII | 🔲 |
| 70 | `math.mechanics.statics` | Mechanics | Statics of Coplanar Forces | Resolution, moments, couples, reduction, equilibrium | XI–XII | 🔲 |
| 71 | `math.mechanics.friction-cg` | Mechanics | Friction and Centre of Gravity | Laws and cone of friction, rough curves and surfaces, centre of gravity | XI–XII | 🔲 |
| 72 | `math.mechanics.virtual-work` | Mechanics | Virtual Work and Forces in Space | Principle of virtual work, astatic equilibrium, central axis, wrench | XI–XII | 🔲 |
| 73 | `math.mechanics.rigid-dynamics` | Mechanics | Rigid Dynamics | Moments of inertia, D'Alembert, compound pendulum, rolling, Lagrangian | XI–XII | 🔲 |
| 74 | `math.numerical.numerical-ode` | Numerical Analysis | Numerical Solution of ODEs | Euler, RK4, Milne | XI–XII | 🔲 |
| 75 | `math.probability.random-variables` | Probability and Statistics | Random Variables and Expectation | Distribution functions, expectation, variance, MGF, characteristic function | XI–XII | 🔲 |
| 76 | `math.probability.distributions` | Probability and Statistics | Standard Distributions | Binomial, Poisson, uniform, normal, gamma, beta, Cauchy | XI–XII | 🔲 |
| 77 | `math.probability.bivariate` | Probability and Statistics | Bivariate Distributions, Correlation and Regression | Joint and conditional distributions, covariance, correlation, regression lines | XI–XII | 🔲 |
| 78 | `math.probability.limit-theorems` | Probability and Statistics | Limit Theorems | Chebyshev, law of large numbers, normal and Poisson approximations, CLT | XI–XII | 🔲 |
| 79 | `math.probability.sampling-estimation` | Probability and Statistics | Sampling and Estimation | Sampling distributions, χ², t, F, unbiasedness, consistency, MLE, confidence intervals | XI–XII | 🔲 |
| 80 | `math.probability.hypothesis-testing` | Probability and Statistics | Testing of Hypotheses | Simple and composite hypotheses, Neyman–Pearson lemma, likelihood ratio tests | XI–XII | 🔲 |

## Rules
- IDs and queue numbers are permanent once written; new topics get the next free number.
- The first topic of a unit also creates `content/subjects/math/subject.yaml` (if missing) and the unit's `unit.yaml`.

