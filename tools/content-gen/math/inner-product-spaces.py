import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.inner-product-spaces")

# 1
T.single(1, ["norm-inequalities"],
    r"With the standard inner product on $\R^3$, the norm of $(1, -2, 2)$ is",
    [r"$3$", r"$9$", r"$1$", r"$5$"],
    r"""$$\|(1, -2, 2)\| = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt9 = 3.$$

$9$ is $\|v\|^2$ (the square root was forgotten); $1$ adds the entries instead of their squares.""")

# 2
T.single(1, ["norm-inequalities"],
    r"The angle between $(1, 0, 1)$ and $(0, 1, 1)$ in $\R^3$ (standard inner product) is",
    [r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{2\pi}{3}$"],
    r"""$$\cos\theta = \frac{\langle u, v\rangle}{\|u\|\|v\|} = \frac{0 + 0 + 1}{\sqrt2\cdot\sqrt2} = \frac12,$$
so $\theta = \frac{\pi}{3}$.

$\frac{\pi}{6}$ reads $\frac12$ as a sine; $\frac{2\pi}{3}$ would need $\cos\theta = -\frac12$.""")

# 3
T.single(1, ["orthogonality"],
    r"The vectors $(1, k, 2)$ and $(3, -1, k)$ in $\R^3$ are orthogonal (standard inner product) when $k$ equals",
    [r"$-3$", r"$3$", r"$1$", r"$-1$"],
    r"""$$\langle u, v\rangle = 3 - k + 2k = 3 + k = 0 \implies k = -3.$$

$k = 3$ is the sign slip in solving $3 + k = 0$.""")

# 4
T.single(1, ["inner-products", "norm-inequalities"],
    r"On $C[0, 1]$ with $\langle f, g\rangle = \int_0^1 f(x)g(x)\,dx$, the norm of $f(x) = x$ is",
    [r"$\dfrac{1}{\sqrt3}$", r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac{1}{\sqrt2}$"],
    r"""$$\|x\|^2 = \int_0^1 x^2\,dx = \frac13, \qquad \|x\| = \frac{1}{\sqrt3}.$$

$\frac13$ is $\|x\|^2$; $\frac12 = \int_0^1 x\,dx$ integrates $f$ instead of $f^2$.""")

# 5
T.single(1, ["norm-inequalities"],
    r"In an inner product space, equality holds in the Cauchy–Schwarz inequality $|\langle u, v\rangle| \le \|u\|\,\|v\|$ if and only if",
    [r"$u$ and $v$ are linearly dependent", r"$u$ and $v$ are orthogonal",
     r"$\|u\| = \|v\|$", r"$v = cu$ for some $c > 0$"],
    r"""Equality holds **iff** $u, v$ are linearly dependent (one is a scalar multiple of the other, or one is $0$).

Orthogonal non-zero vectors give $0 < \|u\|\|v\|$, the opposite extreme. "$v = cu$, $c > 0$" is the equality case of the **triangle** inequality; for Cauchy–Schwarz a negative $c$ also gives equality, e.g. $u = (1, 0)$, $v = (-2, 0)$: $|\langle u, v\rangle| = 2 = \|u\|\|v\|$.""")

# 6
T.single(1, ["orthogonality"],
    r"$e_1 = \tfrac{1}{\sqrt2}(1, 1)$ and $e_2 = \tfrac{1}{\sqrt2}(1, -1)$ form an orthonormal basis of $\R^2$. The Fourier coefficients $\big(\langle v, e_1\rangle, \langle v, e_2\rangle\big)$ of $v = (3, 1)$ are",
    [r"$(2\sqrt2, \sqrt2)$", r"$(4, 2)$", r"$(2, 1)$", r"$(\sqrt2, 2\sqrt2)$"],
    r"""$$\langle v, e_1\rangle = \frac{3 + 1}{\sqrt2} = 2\sqrt2, \qquad \langle v, e_2\rangle = \frac{3 - 1}{\sqrt2} = \sqrt2.$$

Check: $2\sqrt2\,e_1 + \sqrt2\,e_2 = (2, 2) + (1, -1) = (3, 1)$, and $8 + 2 = 10 = \|v\|^2$ (Parseval).

$(4, 2)$ uses the unnormalised vectors $(1, 1)$, $(1, -1)$; $(2, 1)$ divides by $\|u\|^2 = 2$, which gives coordinates with respect to $(1, 1), (1, -1)$, not Fourier coefficients for $e_1, e_2$.""")

# 7
T.single(1, ["norm-inequalities"],
    r"In a real inner product space, $\|u\| = 3$, $\|v\| = 4$ and $\|u + v\| = 6$. Then $\|u - v\|$ equals",
    [r"$\sqrt{14}$", r"$14$", r"$1$", r"$\sqrt{86}$"],
    r"""By the parallelogram law,
$$\|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2 - \|u + v\|^2 = 18 + 32 - 36 = 14,$$
so $\|u - v\| = \sqrt{14}$.

$14$ forgets the square root; $\sqrt{86}$ adds $36$ instead of subtracting it; $1 = \big|\|u\| - \|v\|\big|$ is only a lower bound.""")

# 8
T.single(2, ["inner-products", "exam-tips"],
    r"With the standard inner product $\langle x, y\rangle = \sum x_k\overline{y_k}$ on $\C^2$, $\langle (1 + i, 2), (i, 1 - i)\rangle$ equals",
    [r"$3 + i$", r"$1 - i$", r"$3 - i$", r"$1 + i$"],
    r"""Conjugate the **second** vector: $\overline{i} = -i$, $\overline{1 - i} = 1 + i$.
$$(1 + i)(-i) + 2(1 + i) = (1 - i) + (2 + 2i) = 3 + i.$$

$1 - i$ forgets the conjugation: $(1 + i)i + 2(1 - i)$. $3 - i$ conjugates the first vector instead, which gives $\overline{3 + i}$, i.e. $\langle y, x\rangle$.""")

# 9
T.single(2, ["inner-products"],
    r"For $x = (x_1, x_2)$, $y = (y_1, y_2)$ in $\R^2$, which of the following defines an inner product?",
    [r"$x_1y_1 - x_1y_2 - x_2y_1 + 3x_2y_2$", r"$x_1y_1 - x_2y_2$",
     r"$x_1y_2 + x_2y_1$", r"$x_1y_1 + 2x_1y_2 + x_2y_1 + x_2y_2$"],
    r"""Write each form as $x^T M y$; it is an inner product iff $M$ is symmetric and positive definite.

- $M = \begin{pmatrix} 1 & -1\\ -1 & 3\end{pmatrix}$: symmetric, $1 > 0$, $\det M = 2 > 0$. **Inner product.**
- $x_1y_1 - x_2y_2$: $\langle (0, 1), (0, 1)\rangle = -1 < 0$.
- $x_1y_2 + x_2y_1$: $\langle (1, 0), (1, 0)\rangle = 0$ for a non-zero vector.
- $x_1y_1 + 2x_1y_2 + x_2y_1 + x_2y_2$: not symmetric, e.g. $\langle e_1, e_2\rangle = 2 \ne 1 = \langle e_2, e_1\rangle$.""")

# 10
T.single(2, ["inner-products", "exam-tips"],
    r"$\langle x, y\rangle = x_1y_1 + k(x_1y_2 + x_2y_1) + 4x_2y_2$ is an inner product on $\R^2$ if and only if",
    [r"$-2 < k < 2$", r"$-2 \le k \le 2$", r"$-4 < k < 4$", r"$0 < k < 2$"],
    r"""The matrix is $M = \begin{pmatrix} 1 & k\\ k & 4\end{pmatrix}$, symmetric for every $k$. Positive definite iff $1 > 0$ and $\det M = 4 - k^2 > 0$, i.e. $-2 < k < 2$.

At $k = 2$, the non-zero vector $x = (2, -1)$ gives $\langle x, x\rangle = 4 - 8 + 4 = 0$ (similarly $(2, 1)$ at $k = -2$), so positivity fails: the endpoints must be excluded. $-4 < k < 4$ compares $k$ with $4$ instead of $k^2$.""")

# 11
T.single(2, ["gram-schmidt"],
    r"Gram–Schmidt (standard inner product) is applied to $v_1 = (1, 1, 0)$, $v_2 = (1, 0, 1)$. The second orthogonal vector $u_2$ is",
    [r"$\left(\tfrac12, -\tfrac12, 1\right)$", r"$(0, -1, 1)$", r"$\left(\tfrac12, \tfrac12, 1\right)$", r"$(1, -1, 1)$"],
    r"""$$u_2 = v_2 - \frac{\langle v_2, u_1\rangle}{\|u_1\|^2}u_1 = (1, 0, 1) - \frac12(1, 1, 0) = \left(\tfrac12, -\tfrac12, 1\right).$$

Check: $\langle u_2, u_1\rangle = \frac12 - \frac12 = 0$.

$(0, -1, 1)$ forgets to divide by $\|u_1\|^2 = 2$; it has dot product $-1$ with $u_1$, so it is not orthogonal.""")

# 12
T.single(2, ["complement-projection", "exam-tips"],
    r"The orthogonal projection of $v = (1, 2, 3)$ onto the line spanned by $u = (1, 1, 1)$ in $\R^3$ is",
    [r"$(2, 2, 2)$", r"$(6, 6, 6)$", r"$(2\sqrt3, 2\sqrt3, 2\sqrt3)$", r"$(-1, 0, 1)$"],
    r"""$$\operatorname{proj}_u v = \frac{\langle v, u\rangle}{\langle u, u\rangle}u = \frac63(1, 1, 1) = (2, 2, 2).$$

$(6, 6, 6)$ forgets the division by $\|u\|^2$; $(2\sqrt3, \ldots)$ divides by $\|u\|$ only. $(-1, 0, 1) = v - \operatorname{proj}_u v$ is the component **orthogonal** to $u$.""")

# 13
T.single(2, ["norm-inequalities"],
    r"On $C[0, 1]$ with $\langle f, g\rangle = \int_0^1 fg\,dx$, the angle between $f(x) = 1$ and $g(x) = x$ is",
    [r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{2}$"],
    r"""$\langle 1, x\rangle = \int_0^1 x\,dx = \frac12$, $\|1\| = 1$, $\|x\| = \frac{1}{\sqrt3}$. So
$$\cos\theta = \frac{1/2}{1/\sqrt3} = \frac{\sqrt3}{2}, \qquad \theta = \frac{\pi}{6}.$$

$\frac{\pi}{3}$ comes from forgetting the square root in $\|x\|$ ($\cos\theta = \frac{1/2}{1}$ would also give it). $\frac{\pi}{2}$ would hold on $[-1, 1]$, where $1 \perp x$, not on $[0, 1]$.""")

# 14
T.single(2, ["inner-products", "exam-tips"],
    r"On the space of real $2 \times 2$ matrices with $\langle A, B\rangle = \operatorname{tr}(A^TB)$, the norm of $A = \begin{pmatrix} 1 & 2\\ 0 & 3\end{pmatrix}$ is",
    [r"$\sqrt{14}$", r"$\sqrt{10}$", r"$14$", r"$4$"],
    r"""$\operatorname{tr}(A^TA) = \sum a_{ij}^2 = 1 + 4 + 0 + 9 = 14$, so $\|A\| = \sqrt{14}$.

$\sqrt{10}$ uses $\operatorname{tr}(A^2) = 1 + 9$, forgetting the transpose; $4 = \operatorname{tr}A$.""")

# 15
T.single(2, ["gram-schmidt-polynomials"],
    r"Gram–Schmidt is applied to $1, x, x^2$ with $\langle p, q\rangle = \int_{-1}^{1}p(x)q(x)\,dx$. The third (unnormalised) output is",
    [r"$x^2 - \dfrac13$", r"$x^2 - \dfrac12$", r"$x^2 - x + \dfrac16$", r"$x^2 - \dfrac23$"],
    r"""$x^2$ is even and $x$ is odd, so $\langle x^2, x\rangle = 0$. Only the constant is subtracted:
$$u_2 = x^2 - \frac{\langle x^2, 1\rangle}{\langle 1, 1\rangle}\cdot 1 = x^2 - \frac{2/3}{2} = x^2 - \frac13.$$

$x^2 - \frac23$ forgets to divide by $\|1\|^2 = 2$. $x^2 - x + \frac16$ is the answer on $[0, 1]$, not $[-1, 1]$.""")

# 16
T.single(3, ["complement-projection", "exam-tips"],
    r"$W = \operatorname{span}\{(1, 2, 0, 1),\ (2, 1, 1, 0),\ (3, 3, 1, 1)\} \subseteq \R^4$ (standard inner product). Then $\dim W^\perp$ equals",
    [r"$2$", r"$1$", r"$3$", r"$0$"],
    r"""$(3, 3, 1, 1) = (1, 2, 0, 1) + (2, 1, 1, 0)$, and the first two are independent, so $\dim W = 2$. Since $\R^4 = W \oplus W^\perp$,
$$\dim W^\perp = 4 - 2 = 2.$$

$1$ comes from counting three spanning vectors as if independent.""")

# 17
T.single(2, ["orthogonal-matrices"],
    r"The matrix $\dfrac13\begin{pmatrix} 2 & -2 & 1\\ 1 & 2 & 2\\ 2 & 1 & x\end{pmatrix}$ is orthogonal when $x$ equals",
    [r"$-2$", r"$2$", r"$-1$", r"$1$"],
    r"""The rows must be orthonormal. Row 3 $\perp$ row 1:
$$2\cdot 2 + (-2)\cdot 1 + 1\cdot x = 2 + x = 0 \implies x = -2.$$

Check: row 3 $\cdot$ row 2 $= 2 + 2 - 4 = 0$, and $\|(2, 1, -2)\| = 3$, so the scaled row is a unit vector.

$x = 2$ makes row 3 a unit vector too, but $(2, 1, 2)\cdot(2, -2, 1) = 4 \ne 0$.""")

# 18
T.single(2, ["norm-inequalities", "exam-tips"],
    r"The maximum value of $2x + 3y + 6z$ subject to $x^2 + y^2 + z^2 = 1$ is",
    [r"$7$", r"$11$", r"$49$", r"$\sqrt{11}$"],
    r"""By Cauchy–Schwarz in $\R^3$,
$$|2x + 3y + 6z| \le \sqrt{2^2 + 3^2 + 6^2}\,\sqrt{x^2 + y^2 + z^2} = \sqrt{49} = 7,$$
with equality at $(x, y, z) = \frac17(2, 3, 6)$.

$11 = 2 + 3 + 6$ adds the coefficients; $49$ forgets the square root.""")

# 19
T.single(3, ["gram-schmidt-polynomials"],
    r"With $\langle p, q\rangle = \int_{-1}^{1}pq\,dx$, the unit vector obtained by normalising $x^2 - \frac13$ is",
    [r"$\sqrt{\dfrac58}\,(3x^2 - 1)$", r"$\dfrac12(3x^2 - 1)$", r"$\sqrt{\dfrac52}\,(3x^2 - 1)$", r"$\sqrt{\dfrac38}\,(3x^2 - 1)$"],
    r"""$$\|3x^2 - 1\|^2 = \int_{-1}^{1}(9x^4 - 6x^2 + 1)\,dx = \frac{18}{5} - 4 + 2 = \frac85,$$
so the unit vector is $\sqrt{\frac58}\,(3x^2 - 1)$.

$\frac12(3x^2 - 1)$ is the Legendre polynomial $P_2$; it is orthogonal to $1$ and $x$ but has $\|P_2\|^2 = \frac25$, not $1$.""")

# 20
T.single(3, ["complement-projection"],
    r"In $\R^3$ (standard inner product), the distance from $v = (1, 2, 3)$ to the plane $W = \operatorname{span}\{(1, 1, 0), (1, -1, 2)\}$ is",
    [r"$\dfrac{4}{\sqrt3}$", r"$\dfrac{16}{3}$", r"$\dfrac43$", r"$\dfrac{2}{\sqrt3}$"],
    r"""The spanning vectors are orthogonal ($1 - 1 + 0 = 0$), so
$$P_W v = \frac32(1, 1, 0) + \frac56(1, -1, 2) = \left(\tfrac73, \tfrac23, \tfrac53\right), \qquad v - P_W v = \tfrac43(-1, 1, 1).$$
The distance is $\frac43\sqrt3 = \frac{4}{\sqrt3}$.

Quick check: the normal is $n = (1, 1, 0)\times(1, -1, 2) \sim (-1, 1, 1)$ and $\frac{|\langle v, n\rangle|}{\|n\|} = \frac{4}{\sqrt3}$. $\frac{16}{3}$ is the squared distance; $\frac43$ drops the $\sqrt3$.""")

# 21
T.single(3, ["gram-schmidt"],
    r"Gram–Schmidt (standard inner product) is applied to $(1, 1, 0)$, $(1, 0, 1)$, $(0, 1, 1)$ in that order. The third vector of the resulting orthonormal basis is",
    [r"$\tfrac{1}{\sqrt3}(-1, 1, 1)$", r"$\tfrac{1}{\sqrt3}(1, 1, 1)$", r"$\tfrac{1}{\sqrt3}(1, -1, 1)$", r"$\tfrac{1}{\sqrt2}(0, 1, 1)$"],
    r"""$u_1 = (1, 1, 0)$, $u_2 \sim (1, -1, 2)$ with $\|u_2\|^2 = 6$. Then
$$u_3 = (0, 1, 1) - \tfrac12(1, 1, 0) - \tfrac16(1, -1, 2) = \left(-\tfrac23, \tfrac23, \tfrac23\right),$$
and normalising gives $\frac{1}{\sqrt3}(-1, 1, 1)$.

Fast check: $e_3$ must be orthogonal to $(1, 1, 0)$ and $(1, -1, 2)$. Only $(-1, 1, 1)$ is; $(1, 1, 1)$ has dot product $2$ with $(1, 1, 0)$, and $\frac{1}{\sqrt2}(0, 1, 1)$ is just $v_3$ normalised.""")

# 22 statements
T.statements(3, ["orthogonality", "inner-products"],
    r"Let $V$ be a complex inner product space, with $\langle\cdot,\cdot\rangle$ linear in the first argument. Consider the following statements:",
    [r"$\langle u, \alpha v\rangle = \bar\alpha\langle u, v\rangle$ for all $u, v \in V$, $\alpha \in \C$.",
     r"If $\|u + v\|^2 = \|u\|^2 + \|v\|^2$, then $u \perp v$.",
     r"Every orthogonal set of non-zero vectors in $V$ is linearly independent."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 and 2 only", r"3 only"],
    r"""1. True: $\langle u, \alpha v\rangle = \overline{\langle \alpha v, u\rangle} = \overline{\alpha\langle v, u\rangle} = \bar\alpha\langle u, v\rangle$.
2. False: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$ forces only $\operatorname{Re}\langle u, v\rangle = 0$. In $\C$: $u = 1$, $v = i$ give $\|1 + i\|^2 = 2 = 1 + 1$, but $\langle 1, i\rangle = \bar i = -i \ne 0$.
3. True: if $\sum c_j v_j = 0$, take the inner product with $v_i$: $c_i\|v_i\|^2 = 0$, so $c_i = 0$.

Statement 2 is true in a **real** space, which is the trap.""")

# 23 statements
T.statements(3, ["inner-products"],
    r"Consider the following statements:",
    [r"$\langle f, g\rangle = \int_0^1 f(x)g(x)\,dx$ is an inner product on $C[0, 1]$.",
     r"$\langle p, q\rangle = p(0)q(0) + p(1)q(1)$ is an inner product on the space of real polynomials of degree $\le 1$.",
     r"$\langle A, B\rangle = \operatorname{tr}(A^TB)$ is an inner product on the space of real $n \times n$ matrices."],
    [r"1, 2 and 3", r"1 and 3 only", r"1 and 2 only", r"2 and 3 only"],
    r"""1. True: bilinear, symmetric, and $\int_0^1 f^2 = 0$ forces $f \equiv 0$ because $f$ is **continuous**.
2. True: bilinear and symmetric; $\langle p, p\rangle = p(0)^2 + p(1)^2 = 0$ means $p$ has two roots $0$ and $1$, and a polynomial of degree $\le 1$ with two roots is $0$.
3. True: $\operatorname{tr}(A^TB) = \sum_{i,j}a_{ij}b_{ij}$ is the dot product of the entries.

The tempting "1 and 3 only" treats 2 as on degree $\le 2$, where $p = x(x - 1)$ would break positivity.""")

# 24 match
T.match(1, ["norm-inequalities"],
    r"Let $u = (1, 2, 2)$ and $v = (3, 0, 4)$ in $\R^3$ (standard inner product). Match List I with List II.",
    [r"$\langle u, v\rangle$", r"$\|u\|$", r"$\|u - v\|$", r"$\cos\theta$, $\theta$ the angle between $u$ and $v$"],
    [r"$\tfrac{11}{15}$", r"$2\sqrt3$", r"$11$", r"$3$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-4, C-1, D-2"],
    r"""- A: $3 + 0 + 8 = 11$ (3).
- B: $\sqrt{1 + 4 + 4} = 3$ (4).
- C: $u - v = (-2, 2, -2)$, norm $\sqrt{12} = 2\sqrt3$ (2).
- D: $\|v\| = 5$, so $\cos\theta = \frac{11}{3\cdot 5} = \frac{11}{15}$ (1).

So A-3, B-4, C-2, D-1.""")

# 25 match
T.match(2, ["norm-inequalities"],
    r"In a real inner product space, match each result in List I with its statement in List II.",
    [r"Cauchy–Schwarz inequality", r"Triangle inequality", r"Parallelogram law", r"Polarisation identity"],
    [r"$\|u + v\| \le \|u\| + \|v\|$",
     r"$\langle u, v\rangle = \tfrac14\left(\|u + v\|^2 - \|u - v\|^2\right)$",
     r"$|\langle u, v\rangle| \le \|u\|\,\|v\|$",
     r"$\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$"],
    [r"A-3, B-1, C-4, D-2", r"A-1, B-3, C-4, D-2", r"A-3, B-1, C-2, D-4", r"A-3, B-4, C-1, D-2"],
    r"""- Cauchy–Schwarz bounds the inner product: (3).
- Triangle inequality bounds the norm of a sum: (1).
- Parallelogram law: sum of squares of the diagonals equals sum of squares of the sides: (4).
- Polarisation recovers $\langle u, v\rangle$ from norms: (2).

So A-3, B-1, C-4, D-2. Swapping C and D is the usual slip: both identities involve $\|u \pm v\|^2$, but only polarisation has the inner product on one side.""")

# 26 AR 0
T.assertion_reason(2, ["orthogonality"],
    r"The vectors $(1, 1, 0)$, $(1, -1, 0)$, $(0, 0, 2)$ form a basis of $\R^3$.",
    r"An orthogonal set of non-zero vectors in an inner product space is linearly independent.",
    0,
    r"""The three vectors are non-zero and pairwise orthogonal: $1 - 1 + 0 = 0$, and the third is orthogonal to both. By the reason they are independent, and three independent vectors in $\R^3$ form a basis.

Both are true, and the reason explains the assertion.""")

# 27 AR 1
T.assertion_reason(2, ["norm-inequalities"],
    r"For $u = (1, 2)$ and $v = (2, 4)$ in $\R^2$, $|\langle u, v\rangle| = \|u\|\,\|v\|$.",
    r"In every inner product space, $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.",
    1,
    r"""Assertion: $\langle u, v\rangle = 2 + 8 = 10$ and $\|u\|\|v\| = \sqrt5\cdot\sqrt{20} = 10$. True, because $v = 2u$ (equality in Cauchy–Schwarz for dependent vectors).

Reason: the parallelogram law, true in every inner product space. But it says nothing about when Cauchy–Schwarz is an equality, so it does not explain the assertion.""")

# 28 AR 2
T.assertion_reason(3, ["norm-inequalities"],
    r"In a real inner product space, if $u, v \ne 0$ and $\|u + v\| = \|u\| + \|v\|$, then $v = cu$ for some $c > 0$.",
    r"Equality holds in the triangle inequality whenever $u$ and $v$ are linearly dependent.",
    2,
    r"""Assertion: true. Squaring, $\|u + v\|^2 = (\|u\| + \|v\|)^2$ gives $\langle u, v\rangle = \|u\|\|v\|$; this is Cauchy–Schwarz equality, so $v = cu$, and $\langle u, cu\rangle = c\|u\|^2 > 0$ forces $c > 0$.

Reason: false. $u = (1, 0)$, $v = (-1, 0)$ are dependent, yet $\|u + v\| = 0 < 2 = \|u\| + \|v\|$. Dependence is the equality case of Cauchy–Schwarz, not of the triangle inequality.""")

# 29 AR 3
T.assertion_reason(3, ["norm-inequalities"],
    r"The norm $\|(x, y)\| = |x| + |y|$ on $\R^2$ is induced by some inner product.",
    r"A norm on a real vector space is induced by an inner product if and only if it satisfies the parallelogram law.",
    3,
    r"""Reason: true (Jordan–von Neumann theorem); the inner product is then given by polarisation.

Assertion: false. With $u = (1, 0)$, $v = (0, 1)$:
$$\|u + v\|^2 + \|u - v\|^2 = 4 + 4 = 8 \ne 4 = 2\|u\|^2 + 2\|v\|^2,$$
so the parallelogram law fails and, by the reason, no inner product induces this norm.""")

# 30 AR 0
T.assertion_reason(2, ["orthogonal-matrices"],
    r"If $Q$ is a real orthogonal $n \times n$ matrix, then $\|Qx\| = \|x\|$ for every $x \in \R^n$.",
    r"For a real orthogonal matrix $Q$, $Q^TQ = I$, so $\langle Qx, Qy\rangle = y^TQ^TQx = \langle x, y\rangle$.",
    0,
    r"""Reason: true; it is the definition $Q^TQ = I$ applied to the dot product.

Taking $y = x$ gives $\|Qx\|^2 = \|x\|^2$, which is the assertion. Both are true, and the reason explains the assertion.""")


def check():
    import sympy as sp
    M, x, t = sp.Matrix, sp.symbols("x"), sp.symbols("t", real=True)
    I = sp.I
    dot = lambda a, b: (M(a).T*M(b))[0]
    nrm = lambda a: sp.sqrt(dot(a, a))
    cdot = lambda a, b: sum(p*sp.conjugate(q) for p, q in zip(a, b))
    ip = lambda f, g, a=-1, b=1: sp.integrate(f*g, (x, a, b))

    eq(nrm([1, -2, 2]), 3, "q1")
    eq(sp.acos(dot([1, 0, 1], [0, 1, 1])/(nrm([1, 0, 1])*nrm([0, 1, 1]))), sp.pi/3, "q2")
    k = sp.symbols("k")
    assert sp.solve(dot([1, k, 2], [3, -1, k]), k) == [-3], "q3"
    eq(sp.sqrt(ip(x, x, 0, 1)), 1/sp.sqrt(3), "q4")
    # q5: dependent with negative scalar gives CS equality; orthogonal gives strict
    eq(abs(dot([1, 0], [-2, 0])), nrm([1, 0])*nrm([-2, 0]), "q5")
    e1, e2 = M([1, 1])/sp.sqrt(2), M([1, -1])/sp.sqrt(2)
    v = M([3, 1])
    eq(v.dot(e1), 2*sp.sqrt(2), "q6a"); eq(v.dot(e2), sp.sqrt(2), "q6b")
    assert v.dot(e1)*e1 + v.dot(e2)*e2 == v
    eq(sp.sqrt(2*9 + 2*16 - 36), sp.sqrt(14), "q7")
    eq(sp.expand(cdot([1 + I, 2], [I, 1 - I])), 3 + I, "q8")
    eq(sp.expand(sum(p*q for p, q in zip([1 + I, 2], [I, 1 - I]))), 1 - I, "q8 distractor")
    # q9
    assert M([[1, -1], [-1, 3]]).is_positive_definite
    assert not M([[1, 0], [0, -1]]).is_positive_definite
    assert not M([[0, 1], [1, 0]]).is_positive_definite
    A9 = M([[1, 2], [1, 1]]); assert A9 != A9.T
    # q10
    Mk = M([[1, k], [k, 4]])
    assert sp.solve_univariate_inequality(Mk.det() > 0, k, relational=False) == sp.Interval.open(-2, 2), "q10"
    eq((M([2, -1]).T*M([[1, 2], [2, 4]])*M([2, -1]))[0], 0, "q10 endpoint")
    # q11
    v1, v2, v3 = M([1, 1, 0]), M([1, 0, 1]), M([0, 1, 1])
    u2 = v2 - v2.dot(v1)/v1.dot(v1)*v1
    assert u2 == M([sp.Rational(1, 2), -sp.Rational(1, 2), 1]), "q11"
    assert (v2 - v1).dot(v1) != 0
    # q12
    vv, uu = M([1, 2, 3]), M([1, 1, 1])
    assert vv.dot(uu)/uu.dot(uu)*uu == M([2, 2, 2]), "q12"
    # q13
    eq(sp.acos(ip(1, x, 0, 1)/sp.sqrt(ip(1, 1, 0, 1)*ip(x, x, 0, 1))), sp.pi/6, "q13")
    # q14
    A = M([[1, 2], [0, 3]])
    eq(sp.sqrt((A.T*A).trace()), sp.sqrt(14), "q14")
    eq((A**2).trace(), 10, "q14 distractor")
    # q15 and q19 (Gram-Schmidt on polynomials)
    p0 = sp.Integer(1); p1 = x - ip(x, p0)/ip(p0, p0)*p0
    p2 = x**2 - ip(x**2, p0)/ip(p0, p0)*p0 - ip(x**2, p1)/ip(p1, p1)*p1
    eq(p2, x**2 - sp.Rational(1, 3), "q15")
    q0 = sp.Integer(1); q1 = x - ip(x, q0, 0, 1)/ip(q0, q0, 0, 1)*q0
    q2 = x**2 - ip(x**2, q0, 0, 1)/ip(q0, q0, 0, 1)*q0 - ip(x**2, q1, 0, 1)/ip(q1, q1, 0, 1)*q1
    eq(q2, x**2 - x + sp.Rational(1, 6), "q15 distractor [0,1]")
    unit = p2/sp.sqrt(ip(p2, p2))
    eq(unit, sp.sqrt(sp.Rational(5, 8))*(3*x**2 - 1), "q19")
    eq(ip(sp.sqrt(sp.Rational(5, 8))*(3*x**2 - 1), sp.sqrt(sp.Rational(5, 8))*(3*x**2 - 1)), 1, "q19 norm")
    eq(ip((3*x**2 - 1)/2, (3*x**2 - 1)/2), sp.Rational(2, 5), "q19 P2")
    # q16
    W = M([[1, 2, 0, 1], [2, 1, 1, 0], [3, 3, 1, 1]])
    eq(4 - W.rank(), 2, "q16"); eq(len(W.nullspace()), 2, "q16 nullspace")
    # q17
    xs = sp.symbols("xs")
    Q = M([[2, -2, 1], [1, 2, 2], [2, 1, xs]])/3
    assert sp.solve((Q[2, :]*Q[0, :].T)[0], xs) == [-2], "q17"
    Q2 = Q.subs(xs, -2); assert sp.simplify(Q2*Q2.T) == sp.eye(3), "q17 orth"
    # q18
    y, z, lam = sp.symbols("y z lam", real=True)
    sols = sp.solve([2 - 2*lam*x, 3 - 2*lam*y, 6 - 2*lam*z, x**2 + y**2 + z**2 - 1], [x, y, z, lam], dict=True)
    eq(max(2*s[x] + 3*s[y] + 6*s[z] for s in sols), 7, "q18")
    # q20
    w1, w2 = M([1, 1, 0]), M([1, -1, 2]); assert w1.dot(w2) == 0
    P = vv.dot(w1)/w1.dot(w1)*w1 + vv.dot(w2)/w2.dot(w2)*w2
    assert P == M([sp.Rational(7, 3), sp.Rational(2, 3), sp.Rational(5, 3)])
    eq((vv - P).norm(), 4/sp.sqrt(3), "q20")
    # q21: full Gram-Schmidt via sympy
    G = sp.GramSchmidt([v1, v2, v3], True)
    assert sp.simplify(G[2] - M([-1, 1, 1])/sp.sqrt(3)) == sp.zeros(3, 1), "q21"
    assert sp.simplify(G[1] - M([1, -1, 2])/sp.sqrt(6)) == sp.zeros(3, 1)
    # q22
    a, b = sp.symbols("a b", complex=True)
    eq(cdot([a], [b*a]), sp.conjugate(b)*cdot([a], [a]), "q22 s1")
    eq(cdot([1 + I], [1 + I]), cdot([1], [1]) + cdot([I], [I]), "q22 s2 Pythag holds")
    assert cdot([1], [I]) == -I, "q22 s2 false"
    # q23: s2 Gram matrix of 1, x under p(0)q(0)+p(1)q(1) is positive definite
    form = lambda p, q: p.subs(x, 0)*q.subs(x, 0) + p.subs(x, 1)*q.subs(x, 1)
    basis = [sp.Integer(1), x]
    assert M(2, 2, lambda i, j: form(basis[i], basis[j])).is_positive_definite, "q23 s2"
    eq(form(x*(x - 1), x*(x - 1)), 0, "q23 degree-2 counterexample")
    # q24
    u, w = M([1, 2, 2]), M([3, 0, 4])
    eq(u.dot(w), 11, "q24A"); eq(u.norm(), 3, "q24B"); eq((u - w).norm(), 2*sp.sqrt(3), "q24C")
    eq(u.dot(w)/(u.norm()*w.norm()), sp.Rational(11, 15), "q24D")
    # q25: identities symbolically in R^3
    U, V = M(sp.symbols("u1:4", real=True)), M(sp.symbols("v1:4", real=True))
    eq((U + V).dot(U + V) + (U - V).dot(U - V), 2*U.dot(U) + 2*V.dot(V), "q25 parallelogram")
    eq(((U + V).dot(U + V) - (U - V).dot(U - V))/4, U.dot(V), "q25 polarisation")
    # q26
    B = M([[1, 1, 0], [1, -1, 0], [0, 0, 2]])
    assert B*B.T == sp.diag(2, 2, 4) and B.rank() == 3, "q26"
    # q27
    eq(abs(dot([1, 2], [2, 4])), nrm([1, 2])*nrm([2, 4]), "q27")
    # q28: reason false
    assert nrm([0, 0]) != nrm([1, 0]) + nrm([-1, 0]), "q28 R"
    # q29: l1 norm fails parallelogram law
    l1 = lambda p: abs(p[0]) + abs(p[1])
    assert l1([1, 1])**2 + l1([1, -1])**2 == 8 and 2*l1([1, 0])**2 + 2*l1([0, 1])**2 == 4, "q29"
    # q30: rotation preserves norm
    R = M([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])
    X = M(sp.symbols("x1:3", real=True))
    eq(sp.simplify((R*X).dot(R*X)), X.dot(X), "q30")
    # notes examples
    eq(sp.expand(cdot([1 + I, 2], [I, 1 - I])), 3 + I, "notes complex")
    assert M([[1, 1], [0, 1]]).det() == 1 and M([[1, 1], [0, 1]])*M([[1, 1], [0, 1]]).T != sp.eye(2)
    eq(ip(p2, p2), sp.Rational(8, 45), "notes ||u2||^2")
    eq(sp.sqrt(sp.Rational(3, 2))**2*ip(x, x), 1, "notes e1 poly")
    assert v1.cross(M([1, -1, 2])) == M([2, -2, -2])


T.write(check)
