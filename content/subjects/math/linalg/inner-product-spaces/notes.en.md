# Inner Product Spaces

## Inner products and examples {#inner-products}

Let $V$ be a vector space over $F = \R$ or $\C$. An **inner product** on $V$ is a map $\langle\cdot,\cdot\rangle : V \times V \to F$ such that, for all $u, v, w \in V$ and $\alpha \in F$:

1. **Linearity in the first argument:** $\langle \alpha u + w, v\rangle = \alpha\langle u, v\rangle + \langle w, v\rangle$.
2. **Conjugate symmetry:** $\langle u, v\rangle = \overline{\langle v, u\rangle}$ (over $\R$ this is just symmetry).
3. **Positive definiteness:** $\langle v, v\rangle \ge 0$, and $\langle v, v\rangle = 0 \iff v = 0$.

**Convention.** These notes take linearity in the **first** argument (Mapa, Hoffman–Kunze, Axler). Then 1 and 2 give **conjugate-linearity in the second**:

$$\langle u, \alpha v\rangle = \bar\alpha\,\langle u, v\rangle.$$

(Physics books use the opposite convention; questions that depend on it should state it.) By 2, $\langle v, v\rangle$ is always real, so axiom 3 makes sense. A real vector space with an inner product is a **Euclidean space**; a complex one is a **unitary space**.

| Space | Standard inner product |
|:---|:---|
| $\R^n$ | dot product $\langle x, y\rangle = \sum x_i y_i = y^T x$ |
| $\C^n$ | $\langle x, y\rangle = \sum x_i \overline{y_i}$ |
| $\R^n$, weights $w_i > 0$ | $\sum w_i x_i y_i$ |
| $\R^n$, $A$ real symmetric positive definite | $\langle x, y\rangle = y^T A x$ |
| $C[a, b]$ (real continuous functions) | $\int_a^b f(x)g(x)\,dx$ |
| $M_{m\times n}(\R)$ | $\operatorname{tr}(A^T B) = \sum_{i,j} a_{ij}b_{ij}$ |

**Verifying an inner product on $\R^2$.** A form $\langle x, y\rangle = a x_1y_1 + b x_1y_2 + c x_2y_1 + d x_2y_2$ equals $x^T M y$ with $M = \begin{pmatrix} a & b\\ c & d\end{pmatrix}$. It is an inner product **iff** $b = c$ (symmetry) and $M$ is positive definite: $a > 0$ and $ad - b^2 > 0$.

Example: $x_1y_1 - x_1y_2 - x_2y_1 + 3x_2y_2$ has $M = \begin{pmatrix} 1 & -1\\ -1 & 3\end{pmatrix}$, with $1 > 0$ and $\det M = 2 > 0$, so it is an inner product.

:::caution
On $C[a, b]$, positivity uses **continuity**: if $\int_a^b f^2 = 0$ with $f$ continuous, then $f \equiv 0$. For merely integrable functions, $\int f^2 = 0$ does not force $f = 0$. Similarly, $\langle p, q\rangle = p(0)q(0) + p(1)q(1)$ is an inner product on polynomials of degree $\le 1$, but **not** on degree $\le 2$: $p = x(x - 1) \ne 0$ has $\langle p, p\rangle = 0$.
:::

:::exam-tip
Complex dot product: conjugate the **second** vector. $\langle(1 + i, 2), (i, 1 - i)\rangle = (1 + i)(-i) + 2(1 + i) = 3 + i$.
:::

## Norm, Cauchy–Schwarz and the triangle inequality {#norm-inequalities}

The **induced norm** is $\|v\| = \sqrt{\langle v, v\rangle}$. It satisfies $\|v\| \ge 0$ with equality iff $v = 0$, and $\|\alpha v\| = |\alpha|\,\|v\|$. A vector with $\|v\| = 1$ is a **unit vector**; $v/\|v\|$ normalises $v \ne 0$.

:::keyfacts
- **Cauchy–Schwarz:** $|\langle u, v\rangle| \le \|u\|\,\|v\|$, with **equality iff $u, v$ are linearly dependent**.
- **Triangle inequality:** $\|u + v\| \le \|u\| + \|v\|$. In a real space with $u, v \ne 0$, equality holds **iff $v = cu$ with $c > 0$** (same direction).
- **Parallelogram law:** $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.
- **Polarisation (real):** $\langle u, v\rangle = \tfrac14\left(\|u + v\|^2 - \|u - v\|^2\right)$.
:::

**Proof idea of Cauchy–Schwarz (real case).** For $v \neq 0$ the quadratic $t \mapsto \|u - tv\|^2 = \|u\|^2 - 2t\langle u, v\rangle + t^2\|v\|^2$ is never negative, so its discriminant is $\le 0$: $\langle u, v\rangle^2 \le \|u\|^2\|v\|^2$. Equality means $u - tv = 0$ for some $t$.

**The triangle inequality** follows: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2 \le (\|u\| + \|v\|)^2$.

**Angle.** In a Euclidean space, Cauchy–Schwarz gives $-1 \le \frac{\langle u, v\rangle}{\|u\|\|v\|} \le 1$. So for $u, v \ne 0$ the angle $\theta \in [0, \pi]$ is defined by

$$\cos\theta = \frac{\langle u, v\rangle}{\|u\|\,\|v\|}.$$

Example in $C[0, 1]$: $\langle 1, x\rangle = \frac12$, $\|1\| = 1$, $\|x\| = \frac{1}{\sqrt3}$, so $\cos\theta = \frac{\sqrt3}{2}$ and $\theta = \frac{\pi}{6}$.

**Expanding norms.** In a real space, $\|au + bv\|^2 = a^2\|u\|^2 + 2ab\langle u, v\rangle + b^2\|v\|^2$.

:::caution
Equality in the triangle inequality needs **positive** dependence. $u = (1, 0)$ and $v = (-1, 0)$ are dependent, yet $\|u + v\| = 0 < 2 = \|u\| + \|v\|$. Equality in Cauchy–Schwarz needs only dependence.
:::

:::exam-tip
A norm comes from an inner product **iff** it satisfies the parallelogram law (Jordan–von Neumann). The norm $|x| + |y|$ on $\R^2$ fails it: with $u = (1, 0)$, $v = (0, 1)$, the left side is $4 + 4 = 8$ but the right side is $4$.

Cauchy–Schwarz also gives maxima: on $x^2 + y^2 + z^2 = 1$, the maximum of $2x + 3y + 6z$ is $\sqrt{4 + 9 + 36} = 7$.
:::

## Orthogonality and orthonormal bases {#orthogonality}

$u$ and $v$ are **orthogonal**, $u \perp v$, if $\langle u, v\rangle = 0$. Then $0$ is orthogonal to everything, and it is the only vector orthogonal to itself.

**Pythagoras.** If $u \perp v$, then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$. The converse holds in a **real** space, but fails in a complex one: in $\C$, $\|1 + i\|^2 = 2 = 1 + 1$, yet $\langle 1, i\rangle = \bar i = -i \ne 0$ (the identity only forces $\operatorname{Re}\langle u, v\rangle = 0$).

A set $S$ is **orthogonal** if its vectors are pairwise orthogonal, and **orthonormal** if, in addition, each has norm $1$: $\langle e_i, e_j\rangle = \delta_{ij}$.

:::keyfacts
- An orthogonal set of **non-zero** vectors is linearly independent. (Take $\langle \sum c_j v_j, v_i\rangle = c_i\|v_i\|^2 = 0$.)
- So $n$ mutually orthogonal non-zero vectors in an $n$-dimensional space form a basis.
- Every finite-dimensional inner product space has an orthonormal basis, and every orthonormal set extends to one.
:::

**Fourier coefficients.** If $\{e_1, \dots, e_n\}$ is an orthonormal basis, then every $v$ satisfies

$$v = \sum_{i=1}^n \langle v, e_i\rangle\, e_i, \qquad \|v\|^2 = \sum_{i=1}^n |\langle v, e_i\rangle|^2 \ \text{(Parseval)}.$$

The scalars $\langle v, e_i\rangle$ are the **Fourier coefficients** of $v$. For an orthonormal set that is not a basis, **Bessel's inequality** $\sum|\langle v, e_i\rangle|^2 \le \|v\|^2$ holds. For an **orthogonal** (not normalised) basis $\{u_i\}$, the coefficient is $\dfrac{\langle v, u_i\rangle}{\|u_i\|^2}$.

Example: $e_1 = \frac{1}{\sqrt2}(1, 1)$, $e_2 = \frac{1}{\sqrt2}(1, -1)$ is an orthonormal basis of $\R^2$. For $v = (3, 1)$:

$$\langle v, e_1\rangle = \frac{4}{\sqrt2} = 2\sqrt2, \qquad \langle v, e_2\rangle = \frac{2}{\sqrt2} = \sqrt2,$$

and indeed $2\sqrt2\, e_1 + \sqrt2\, e_2 = (2, 2) + (1, -1) = (3, 1)$, with $8 + 2 = 10 = \|v\|^2$.

:::exam-tip
To test a basis quickly, check orthogonality: $(1, 1, 0)$, $(1, -1, 0)$, $(0, 0, 2)$ are pairwise orthogonal and non-zero, so they form a basis of $\R^3$ with no determinant needed.
:::

## The Gram–Schmidt process {#gram-schmidt}

**Theorem.** Let $v_1, \dots, v_n$ be linearly independent. Define

$$u_1 = v_1, \qquad u_k = v_k - \sum_{j=1}^{k-1}\frac{\langle v_k, u_j\rangle}{\|u_j\|^2}\,u_j \quad (k = 2, \dots, n).$$

Then $u_1, \dots, u_n$ are orthogonal and non-zero, and $\operatorname{span}\{u_1, \dots, u_k\} = \operatorname{span}\{v_1, \dots, v_k\}$ for every $k$. Normalising, $e_k = u_k/\|u_k\|$ gives an **orthonormal** set with the same nested spans.

Each step subtracts from $v_k$ its projections onto the earlier $u_j$. If the $v_k$ are dependent, some $u_k$ comes out $0$: that is a quick dependence test.

### Worked example in $\R^3$

Orthonormalise $v_1 = (1, 1, 0)$, $v_2 = (1, 0, 1)$, $v_3 = (0, 1, 1)$ (dot product).

- $u_1 = (1, 1, 0)$, $\|u_1\|^2 = 2$.
- $\langle v_2, u_1\rangle = 1$, so $u_2 = (1, 0, 1) - \frac12(1, 1, 0) = \left(\frac12, -\frac12, 1\right)$. Scaling does not affect orthogonality, so use $u_2 = (1, -1, 2)$, $\|u_2\|^2 = 6$.
- $\langle v_3, u_1\rangle = 1$ and $\langle v_3, u_2\rangle = -1 + 2 = 1$, so
$$u_3 = (0, 1, 1) - \tfrac12(1, 1, 0) - \tfrac16(1, -1, 2) = \left(-\tfrac23, \tfrac23, \tfrac23\right) \sim (-1, 1, 1).$$

The orthonormal basis is

$$e_1 = \tfrac{1}{\sqrt2}(1, 1, 0), \quad e_2 = \tfrac{1}{\sqrt6}(1, -1, 2), \quad e_3 = \tfrac{1}{\sqrt3}(-1, 1, 1).$$

Check: each pair has dot product $0$. In $\R^3$, $u_3$ must be parallel to $u_1 \times u_2 = (2, -2, -2)$, which it is.

:::caution
The divisor is $\|u_j\|^2$, **not** $\|u_j\|$ and not $1$. Forgetting it in the step above gives $(1, 0, 1) - (1, 1, 0) = (0, -1, 1)$, which is not orthogonal to $(1, 1, 0)$. Also, project onto the **new** $u_j$, not onto the old $v_j$.
:::

:::exam-tip
The output depends on the **order** of the input vectors, but $e_1$ is always $v_1/\|v_1\|$. In an MCQ, eliminate options whose first vector is not parallel to $v_1$, then test orthogonality.
:::

## Gram–Schmidt on polynomials {#gram-schmidt-polynomials}

Take the space of real polynomials of degree $\le 2$ with

$$\langle p, q\rangle = \int_{-1}^{1} p(x)q(x)\,dx,$$

and apply Gram–Schmidt to $1, x, x^2$. Use $\int_{-1}^{1} x^k\,dx = \frac{2}{k + 1}$ for even $k$ and $0$ for odd $k$.

- $u_0 = 1$, $\|u_0\|^2 = 2$.
- $\langle x, 1\rangle = 0$, so $u_1 = x$, $\|u_1\|^2 = \frac23$.
- $\langle x^2, 1\rangle = \frac23$ and $\langle x^2, x\rangle = 0$, so
$$u_2 = x^2 - \frac{2/3}{2}\cdot 1 = x^2 - \frac13, \qquad \|u_2\|^2 = \int_{-1}^1\left(x^4 - \tfrac23 x^2 + \tfrac19\right)dx = \tfrac25 - \tfrac49 + \tfrac29 = \tfrac{8}{45}.$$

Normalising gives the orthonormal basis

$$\frac{1}{\sqrt2}, \qquad \sqrt{\frac32}\,x, \qquad \sqrt{\frac58}\,(3x^2 - 1).$$

These are multiples of the **Legendre polynomials** $P_0 = 1$, $P_1 = x$, $P_2 = \frac12(3x^2 - 1)$, which satisfy $\int_{-1}^1 P_n^2 = \frac{2}{2n + 1}$. They are orthogonal but **not** normalised; the orthonormal versions are $\sqrt{\frac{2n + 1}{2}}\,P_n$.

```plot
title: The orthogonal polynomials $1$, $x$ and $x^2 - \tfrac13$ on $[-1, 1]$
x: -1, 1
y: -1, 1.2
f: 1 | $u_0 = 1$
f: x | $u_1 = x$
f: x^2 - 1/3 | $u_2 = x^2 - \tfrac13$
```

**Symmetry shortcut.** On a symmetric interval $[-a, a]$, every even function is orthogonal to every odd function. So $x$ is automatically orthogonal to $1$ and $x^2$, and only the constant needs subtracting from $x^2$.

:::caution
The interval matters. On $[0, 1]$, Gram–Schmidt on $1, x, x^2$ gives $1$, $x - \frac12$, $x^2 - x + \frac16$: there $x$ is **not** orthogonal to $1$, because $\int_0^1 x\,dx = \frac12$.
:::

## Orthogonal complements and projections {#complement-projection}

For a subset $S$ of $V$, the **orthogonal complement** is

$$S^\perp = \{v \in V : \langle v, s\rangle = 0 \text{ for all } s \in S\}.$$

It is always a subspace (even if $S$ is not), and $S^\perp = (\operatorname{span} S)^\perp$.

:::keyfacts
For a subspace $W$ of a **finite-dimensional** inner product space $V$:
- $V = W \oplus W^\perp$, so $\dim W^\perp = \dim V - \dim W$.
- $(W^\perp)^\perp = W$.
- $\{0\}^\perp = V$ and $V^\perp = \{0\}$.
- For a real $m \times n$ matrix $A$: $(\text{row space of } A)^\perp = \text{null space of } A$ in $\R^n$.
:::

**Computing $W^\perp$.** If $W = \operatorname{span}\{w_1, \dots, w_k\}$, then $W^\perp$ is the solution space of the homogeneous system $\langle x, w_i\rangle = 0$, $i = 1, \dots, k$. First find $\dim W$ (the rank), because the spanning set may be dependent.

Example: in $\R^4$, $W = \operatorname{span}\{(1, 2, 0, 1), (2, 1, 1, 0), (3, 3, 1, 1)\}$. The third vector is the sum of the first two, so $\dim W = 2$ and $\dim W^\perp = 4 - 2 = 2$.

**Orthogonal projection.** If $\{u_1, \dots, u_k\}$ is an **orthogonal** basis of $W$, the projection of $v$ onto $W$ is

$$P_W v = \sum_{j=1}^k \frac{\langle v, u_j\rangle}{\|u_j\|^2}\,u_j,$$

and $v - P_W v \in W^\perp$. **Best approximation:** $P_W v$ is the unique vector of $W$ nearest to $v$, so the distance from $v$ to $W$ is $\|v - P_W v\|$.

Example: $v = (1, 2, 3)$, $W = \operatorname{span}\{(1, 1, 0), (1, -1, 2)\}$ (already orthogonal). Then

$$P_W v = \tfrac32(1, 1, 0) + \tfrac56(1, -1, 2) = \left(\tfrac73, \tfrac23, \tfrac53\right), \qquad v - P_W v = \tfrac43(-1, 1, 1),$$

so the distance is $\frac43\sqrt3 = \frac{4}{\sqrt3}$.

:::caution
The projection formula needs an **orthogonal** basis of $W$. With a non-orthogonal spanning set, run Gram–Schmidt first, or for a plane in $\R^3$ project onto its normal $n$ instead: $v - P_W v = \frac{\langle v, n\rangle}{\|n\|^2}n$.
:::

## Orthogonal matrices {#orthogonal-matrices}

A real $n \times n$ matrix $Q$ is **orthogonal** if $Q^TQ = QQ^T = I$, that is, $Q^{-1} = Q^T$. Equivalent conditions:

- the columns of $Q$ form an orthonormal basis of $\R^n$ (equally, the rows do);
- $\langle Qx, Qy\rangle = \langle x, y\rangle$ for all $x, y$ (it preserves dot products, hence lengths and angles);
- $\|Qx\| = \|x\|$ for all $x$ (preserves lengths; equivalent by polarisation).

**Properties.** $\det Q = \pm 1$, since $(\det Q)^2 = \det(Q^TQ) = 1$. Products and inverses of orthogonal matrices are orthogonal. Every real eigenvalue is $\pm 1$, and every complex eigenvalue has modulus $1$. The matrix that changes one orthonormal basis to another is orthogonal.

In $\R^2$ the orthogonal matrices are rotations $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ ($\det = 1$) and reflections $\begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix}$ ($\det = -1$). The complex analogue is a **unitary** matrix: $U^*U = I$, where $U^* = \bar U^T$.

Example: for $\frac13\begin{pmatrix} 2 & -2 & 1\\ 1 & 2 & 2\\ 2 & 1 & x\end{pmatrix}$ to be orthogonal, row 3 must be orthogonal to row 1: $4 - 2 + x = 0$, so $x = -2$. Then row 3 is $\frac13(2, 1, -2)$, a unit vector orthogonal to row 2 as well.

:::caution
$\det Q = \pm 1$ is necessary, **not** sufficient: $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ has determinant $1$ but is not orthogonal. Also, orthogonal columns are not enough; they must be **unit** vectors.
:::

## Quick checks and traps {#exam-tips}

- **Conjugate the second slot** (with these notes' convention): $\langle u, \alpha v\rangle = \bar\alpha\langle u, v\rangle$, so $\langle u, (1 + i)v\rangle = (1 - i)\langle u, v\rangle$.
- **Is it an inner product?** Write the matrix of the form: it must be symmetric and positive definite. For $\begin{pmatrix} 1 & k\\ k & 4\end{pmatrix}$ this needs $4 - k^2 > 0$, i.e. $-2 < k < 2$ (strict).
- **Angles:** compute $\cos\theta$ and keep $\theta \in [0, \pi]$.
- **Equality cases:** Cauchy–Schwarz $\iff$ dependent; triangle (real) $\iff$ one is a non-negative multiple of the other.
- **Projection onto a line:** $\frac{\langle v, u\rangle}{\langle u, u\rangle}u$; projecting $(1, 2, 3)$ onto $(1, 1, 1)$ gives $(2, 2, 2)$.
- **Gram–Schmidt sanity checks:** the first vector is parallel to $v_1$; all outputs are pairwise orthogonal; a zero output means the inputs were dependent.
- **On $[-1, 1]$:** even $\perp$ odd. The third Gram–Schmidt polynomial from $1, x, x^2$ is $x^2 - \frac13$.
- **$\dim W^\perp = \dim V - \dim W$:** find $\dim W$ by rank, not by counting the spanning vectors.
- **$\operatorname{tr}(A^TB)$ norm** is the sum of squares of all entries: $\left\lVert\begin{pmatrix} 1 & 2\\ 0 & 3\end{pmatrix}\right\rVert = \sqrt{14}$.
- **Orthogonal matrix:** rows orthonormal; $Q^{-1} = Q^T$; $\det Q = \pm1$ (necessary only).
