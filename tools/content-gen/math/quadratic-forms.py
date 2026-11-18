import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.quadratic-forms")

# 1
T.single(1, ["matrix-of-form"],
    r"The symmetric matrix of the quadratic form $x^2 + 4xy + 3y^2$ is",
    [r"$\begin{pmatrix} 1 & 2\\ 2 & 3\end{pmatrix}$", r"$\begin{pmatrix} 1 & 4\\ 4 & 3\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 4\\ 0 & 3\end{pmatrix}$", r"$\begin{pmatrix} 3 & 2\\ 2 & 1\end{pmatrix}$"],
    r"""Squares go on the diagonal; the cross coefficient $4$ is **halved** between positions $(1,2)$ and $(2,1)$:
$$A = \begin{pmatrix} 1 & 2\\ 2 & 3\end{pmatrix}.$$

$\begin{pmatrix} 1 & 4\\ 4 & 3\end{pmatrix}$ forgets to halve and gives $x^2 + 8xy + 3y^2$. $\begin{pmatrix} 1 & 4\\ 0 & 3\end{pmatrix}$ gives the right form but is not symmetric. The last option swaps the diagonal entries.""")

# 2
T.single(1, ["matrix-of-form"],
    r"The matrix of the quadratic form $x^2 + 2y^2 - z^2 + 4xy - 6yz + 2zx$ is",
    [r"$\begin{pmatrix} 1 & 2 & 1\\ 2 & 2 & -3\\ 1 & -3 & -1\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 4 & 2\\ 4 & 2 & -6\\ 2 & -6 & -1\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 2 & -3\\ 2 & 2 & 1\\ -3 & 1 & -1\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 2 & 1\\ 2 & 2 & 3\\ 1 & 3 & -1\end{pmatrix}$"],
    r"""Halve each cross coefficient: $xy \to 2$ at $(1,2)$, $yz \to -3$ at $(2,3)$, $zx \to 1$ at $(1,3)$. The diagonal is $1, 2, -1$:
$$A = \begin{pmatrix} 1 & 2 & 1\\ 2 & 2 & -3\\ 1 & -3 & -1\end{pmatrix}.$$

The second option forgets to halve. The third puts the $yz$ and $zx$ entries in each other's places. The fourth drops the minus sign of $-6yz$.""")

# 3
T.single(1, ["matrix-of-form"],
    r"The quadratic form whose matrix is $\begin{pmatrix} 2 & -1 & 0\\ -1 & 3 & 2\\ 0 & 2 & 1\end{pmatrix}$ is",
    [r"$2x^2 + 3y^2 + z^2 - 2xy + 4yz$", r"$2x^2 + 3y^2 + z^2 - xy + 2yz$",
     r"$2x^2 + 3y^2 + z^2 - 2xy + 4zx$", r"$2x^2 + 3y^2 + z^2 + 2xy - 4yz$"],
    r"""Each off-diagonal entry appears twice in $x^TAx$, so the cross coefficient is **double** the entry:
$$Q = 2x^2 + 3y^2 + z^2 + 2(-1)xy + 2(2)yz = 2x^2 + 3y^2 + z^2 - 2xy + 4yz.$$

$-xy + 2yz$ forgets the doubling. The $(1,3)$ entry is $0$, so there is no $zx$ term.""")

# 4
T.single(1, ["congruence"],
    r"The substitution $x = u + v$, $y = u - v$ transforms the form $2xy$ into",
    [r"$2u^2 - 2v^2$", r"$2u^2 + 2v^2$", r"$u^2 - v^2$", r"$4uv$"],
    r"""$$2(u + v)(u - v) = 2u^2 - 2v^2.$$

In matrix terms, $P = \begin{pmatrix} 1 & 1\\ 1 & -1\end{pmatrix}$ and
$$P^T\begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix}P = \begin{pmatrix} 2 & 0\\ 0 & -2\end{pmatrix}.$$

$u^2 - v^2$ drops the factor $2$. A product of a sum and a difference gives a difference of squares, not $2u^2 + 2v^2$.""")

# 5
T.single(2, ["inertia", "orthogonal-reduction"],
    r"For the quadratic form $2xy + 2yz + 2zx$, the rank, index and signature ($p - q$) are respectively",
    [r"$3, 1, -1$", r"$3, 2, 1$", r"$3, 1, 1$", r"$2, 1, 0$"],
    r"""The matrix is $A = J - I$, where $J$ is the all-ones matrix. $J$ has eigenvalues $3, 0, 0$, so $A$ has
$$2, \ -1, \ -1.$$

So $r = 3$, $p = 1$, $q = 2$ and the signature is $p - q = -1$.

$3, 2, 1$ swaps $p$ and $q$. $3, 1, 1$ gives the index as the signature. Check: $\det A = 2 \ne 0$, so the rank is $3$, not $2$.""")

# 6
T.single(2, ["orthogonal-reduction"],
    r"By an orthogonal transformation, the quadratic form $3x^2 + 2xy + 3y^2$ reduces to",
    [r"$2X^2 + 4Y^2$", r"$X^2 + 5Y^2$", r"$3X^2 + 3Y^2$", r"$4X^2 - 2Y^2$"],
    r"""$A = \begin{pmatrix} 3 & 1\\ 1 & 3\end{pmatrix}$: trace $6$, determinant $8$, so $\lambda^2 - 6\lambda + 8 = 0$ and $\lambda = 2, 4$. The orthogonal canonical form has the eigenvalues as coefficients:
$$Q = 2X^2 + 4Y^2, \qquad X = \tfrac{x - y}{\sqrt2},\ Y = \tfrac{x + y}{\sqrt2}.$$

$X^2 + 5Y^2$ uses the unhalved matrix $\begin{pmatrix} 3 & 2\\ 2 & 3\end{pmatrix}$. $3X^2 + 3Y^2$ just deletes the cross term. Check: the coefficients must add to the trace $6$ and multiply to $\det A = 8$.""")

# 7
T.single(2, ["orthogonal-reduction"],
    r"The canonical form, under an orthogonal transformation, of $2x^2 + 2y^2 + 2z^2 + 2xy + 2yz + 2zx$ is",
    [r"$X^2 + Y^2 + 4Z^2$", r"$X^2 + 2Y^2 + 3Z^2$", r"$6Z^2$", r"$2X^2 + 2Y^2 + 2Z^2$"],
    r"""$A = \begin{pmatrix} 2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2\end{pmatrix} = I + J$. The all-ones $J$ has eigenvalues $3, 0, 0$, so $A$ has $4, 1, 1$:
$$Q = X^2 + Y^2 + 4Z^2.$$

$X^2 + 2Y^2 + 3Z^2$ has the right trace $6$ but the wrong determinant ($6$, not $\det A = 4$). $6Z^2$ comes from the unhalved matrix (all entries $2$). The last option ignores the cross terms.""")

# 8
T.single(1, ["inertia"],
    r"The symmetric matrix of a real quadratic form in three variables has eigenvalues $3, -2, 0$. The normal form of the quadratic form is",
    [r"$z_1^2 - z_2^2$", r"$3z_1^2 - 2z_2^2$", r"$z_1^2 - z_2^2 + z_3^2$", r"$z_1^2 + z_2^2$"],
    r"""One positive, one negative and one zero eigenvalue: $p = 1$, $q = 1$, $r = 2$. Scaling each square to coefficient $\pm1$ gives the normal form
$$z_1^2 - z_2^2.$$

$3z_1^2 - 2z_2^2$ is the orthogonal canonical form, not the normal form (the coefficients are not $\pm 1$). The zero eigenvalue contributes no square, so $z_1^2 - z_2^2 + z_3^2$ is wrong.""")

# 9
T.single(2, ["definiteness"],
    r"The quadratic form $2x^2 + 2y^2 + 2z^2 - 2xy - 2yz$ is",
    [r"positive definite", r"positive semi-definite but not positive definite", r"indefinite", r"negative definite"],
    r"""$A = \begin{pmatrix} 2 & -1 & 0\\ -1 & 2 & -1\\ 0 & -1 & 2\end{pmatrix}$, with leading principal minors
$$D_1 = 2,\quad D_2 = 4 - 1 = 3,\quad D_3 = 2(3) + 1(-2) = 4.$$

All are positive, so the form is positive definite by Sylvester's criterion. Since $\det A = 4 \ne 0$, it cannot be semi-definite without being definite. The negative cross terms do not make it indefinite.""")

# 10
T.single(2, ["definiteness"],
    r"The quadratic form $x^2 + 2kxy + 4y^2$ is positive definite if and only if",
    [r"$-2 < k < 2$", r"$-1 < k < 1$", r"$-4 < k < 4$", r"$k > -2$"],
    r"""$A = \begin{pmatrix} 1 & k\\ k & 4\end{pmatrix}$: $D_1 = 1 > 0$ and
$$D_2 = 4 - k^2 > 0 \iff -2 < k < 2.$$

$-1 < k < 1$ comes from the unhalved matrix $\begin{pmatrix} 1 & 2k\\ 2k & 4\end{pmatrix}$ ($4 - 4k^2 > 0$). Positive definiteness needs $k^2 < 4$, which bounds $k$ on both sides, so $k > -2$ is not enough.""")

# 11
T.single(3, ["definiteness"],
    r"The quadratic form $x^2 + 2y^2 + z^2 + 2xy + 2ayz$ is positive definite if and only if",
    [r"$-1 < a < 1$", r"$-\sqrt2 < a < \sqrt2$", r"$-\tfrac12 < a < \tfrac12$", r"$a < 1$"],
    r"""$A = \begin{pmatrix} 1 & 1 & 0\\ 1 & 2 & a\\ 0 & a & 1\end{pmatrix}$. The leading minors are $D_1 = 1$, $D_2 = 2 - 1 = 1$ and
$$D_3 = 1(2 - a^2) - 1(1 - 0) = 1 - a^2.$$

PD $\iff 1 - a^2 > 0 \iff -1 < a < 1$.

$-\sqrt2 < a < \sqrt2$ only asks the $\{2,3\}$ minor $2 - a^2$ to be positive, ignoring the $xy$ coupling. $-\frac12 < a < \frac12$ comes from not halving $2a$.""")

# 12
T.single(3, ["definiteness", "inertia"],
    r"A real symmetric $3 \times 3$ matrix has leading principal minors $D_1 = 2$, $D_2 = -1$, $D_3 = 4$. The signature ($p - q$) of its quadratic form is",
    [r"$-1$", r"$1$", r"$3$", r"$-3$"],
    r"""All $D_k \ne 0$, so Jacobi's rule applies: $q$ is the number of sign changes in
$$1,\ 2,\ -1,\ 4 \quad (+,\ +,\ -,\ +).$$

There are $2$ changes, so $q = 2$, $p = 1$ and $p - q = -1$. Equivalently, the diagonal form is $\sum \frac{D_k}{D_{k-1}}y_k^2 = 2y_1^2 - \tfrac12 y_2^2 - 4y_3^2$.

The answer $1$ swaps $p$ and $q$. All minors being non-zero gives full rank, not definiteness.""")

# 13
T.single(3, ["inertia"],
    r"The number of congruence classes of real symmetric $3 \times 3$ matrices is",
    [r"$10$", r"$4$", r"$7$", r"$16$"],
    r"""By Sylvester's law, a class is fixed by $(p, q)$ with $p, q \ge 0$ and $p + q \le 3$. For rank $r = 0, 1, 2, 3$ there are $r + 1$ choices of $p$:
$$1 + 2 + 3 + 4 = 10 = \frac{(3 + 1)(3 + 2)}{2}.$$

$4$ counts only the ranks (that is the count over $\C$). $7$ counts only the signatures $-3, \dots, 3$, but the same signature occurs at different ranks.""")

# 14
T.single(2, ["inertia"],
    r"Which pair (rank, signature $p - q$) is impossible for a real quadratic form in three variables?",
    [r"$(3, 2)$", r"$(3, 1)$", r"$(2, 0)$", r"$(2, -2)$"],
    r"""$p = \frac{r + s}{2}$ must be an integer, so $r$ and $s$ have the same parity. For $(3, 2)$, $p = \frac52$: impossible.

The others: $(3, 1)$ is $p = 2, q = 1$; $(2, 0)$ is $p = q = 1$ (e.g. $2xy$); $(2, -2)$ is $p = 0, q = 2$ (e.g. $-x^2 - y^2$).""")

# 15
T.single(3, ["lagrange", "inertia"],
    r"The rank and signature ($p - q$) of the quadratic form $2xy + 2yz$ are",
    [r"rank $2$, signature $0$", r"rank $3$, signature $1$", r"rank $2$, signature $2$", r"rank $3$, signature $-1$"],
    r"""There are no square terms, so put $x = u + v$, $y = u - v$, $z = w$ and complete squares:
$$Q = 2u^2 - 2v^2 + 2uw - 2vw = 2\big(u + \tfrac{w}{2}\big)^2 - 2\big(v + \tfrac{w}{2}\big)^2.$$

So $p = q = 1$: rank $2$, signature $0$.

Check by eigenvalues: $A = \begin{pmatrix} 0 & 1 & 0\\ 1 & 0 & 1\\ 0 & 1 & 0\end{pmatrix}$ has $\det A = 0$ (so rank $3$ is wrong) and eigenvalues $0, \pm\sqrt2$.""")

# 16
T.single(2, ["definiteness", "exam-tips"],
    r"The quadratic form $x^2 + y^2 + z^2 - 2xy - 2yz - 2zx$ is",
    [r"indefinite", r"positive definite", r"positive semi-definite but not positive definite", r"negative definite"],
    r"""$A = \begin{pmatrix} 1 & -1 & -1\\ -1 & 1 & -1\\ -1 & -1 & 1\end{pmatrix} = 2I - J$. Since $J$ has eigenvalues $3, 0, 0$, $A$ has
$$-1,\ 2,\ 2.$$

Eigenvalues of both signs: indefinite. Quick test: $Q(1, 1, 1) = 3 - 6 = -3 < 0$ while $Q(1, 0, 0) = 1 > 0$.

The positive diagonal suggests "positive definite", but $D_2 = 1 - 1 = 0$ already rules that out.""")

# 17
T.single(1, ["lagrange"],
    r"Which substitution reduces $x^2 + 4xy + 5y^2$ to $X^2 + Y^2$?",
    [r"$X = x + 2y,\ Y = y$", r"$X = x + 4y,\ Y = y$", r"$X = x + 2y,\ Y = \sqrt5\,y$", r"$X = x - 2y,\ Y = y$"],
    r"""Complete the square in $x$:
$$x^2 + 4xy + 5y^2 = (x + 2y)^2 - 4y^2 + 5y^2 = (x + 2y)^2 + y^2.$$

So $X = x + 2y$, $Y = y$. $X = x + 4y$ uses the whole cross coefficient instead of half of it. $Y = \sqrt5\,y$ forgets that $4y^2$ was used up by the square.""")

# 18
T.single(3, ["lagrange", "inertia"],
    r"Completing squares in $Q = x^2 + 2y^2 + 3z^2 + 2xy + 4yz$ gives",
    [r"$(x + y)^2 + (y + 2z)^2 - z^2$", r"$(x + y)^2 + (y + 2z)^2 + z^2$",
     r"$(x + y)^2 + (y + z)^2 + 2z^2$", r"$(x + 2y)^2 + (y + 2z)^2 - z^2$"],
    r"""Collect the $x$ terms: $x^2 + 2xy = (x + y)^2 - y^2$. Then
$$Q = (x + y)^2 + y^2 + 4yz + 3z^2 = (x + y)^2 + (y + 2z)^2 - 4z^2 + 3z^2 = (x + y)^2 + (y + 2z)^2 - z^2.$$

So $p = 2$, $q = 1$: the form is indefinite although its diagonal is positive (indeed $\det A = -1$).

$+z^2$ gets the sign of $3 - 4$ wrong. $(x + 2y)^2$ forgets to halve the $2xy$ coefficient.""")

# 19
T.single(2, ["orthogonal-reduction"],
    r"The maximum value of $5x^2 + 4xy + 2y^2$ subject to $x^2 + y^2 = 1$ is",
    [r"$6$", r"$1$", r"$7$", r"$5$"],
    r"""On the unit circle, $x^TAx$ ranges over $[\lambda_{\min}, \lambda_{\max}]$. Here $A = \begin{pmatrix} 5 & 2\\ 2 & 2\end{pmatrix}$, with $\lambda^2 - 7\lambda + 6 = 0$, so $\lambda = 1, 6$.

The maximum is $6$, attained at $\pm\frac{1}{\sqrt5}(2, 1)$: $\frac{5\cdot4 + 4\cdot2 + 2}{5} = 6$.

$1$ is the minimum, $7$ is the trace, and $5$ is only the value at $(1, 0)$.""")

# 20
T.single(3, ["semidefinite"],
    r"The quadratic form $x^2 + y^2 + 2xy + 2yz + 2zx$ is",
    [r"indefinite", r"positive semi-definite but not positive definite", r"positive definite", r"negative semi-definite"],
    r"""The leading minors of $A = \begin{pmatrix} 1 & 1 & 1\\ 1 & 1 & 1\\ 1 & 1 & 0\end{pmatrix}$ are $1, 0, 0$, all $\ge 0$. That proves **nothing** about semi-definiteness. Complete the square instead:
$$Q = (x + y + z)^2 - z^2.$$

So $p = q = 1$ and $Q$ is indefinite: $Q(1, 0, -1) = -1 < 0$ while $Q(1, 0, 0) = 1 > 0$. The principal minor on $\{2, 3\}$ is $1\cdot 0 - 1 = -1 < 0$, which also rules out positive semi-definiteness.""")

# 21 statements: 1 only
T.statements(2, ["congruence"],
    r"Let $A$ be a real symmetric matrix and $B = P^TAP$ with $P$ real and non-singular. Consider the following statements:",
    [r"$\operatorname{rank} B = \operatorname{rank} A$.",
     r"$B$ has the same eigenvalues as $A$.",
     r"$\det B = \det A$."],
    [r"1 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"],
    r"""1. True: multiplying by invertible matrices does not change the rank.
2. False: congruence is not similarity. With $A = I_2$ and $P = 2I$, $B = 4I$ has eigenvalue $4$, not $1$.
3. False: $\det B = (\det P)^2\det A$; only the **sign** is kept. In the same example, $\det B = 16 \ne 1$.

Statements 2 and 3 hold when $P$ is orthogonal, but not in general.""")

# 22 statements: 1 and 3 only
T.statements(3, ["definiteness", "semidefinite"],
    r"Consider the following statements about real symmetric $n \times n$ matrices:",
    [r"If $A$ is positive definite, then every diagonal entry of $A$ is positive.",
     r"If every leading principal minor of $A$ is non-negative, then $x^TAx \ge 0$ for all $x$.",
     r"If $A$ and $B$ are positive definite, then $A + B$ is positive definite."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 and 2 only", r"3 only"],
    r"""1. True: $a_{ii} = e_i^TAe_i > 0$.
2. False: $A = \begin{pmatrix} 0 & 0\\ 0 & -1\end{pmatrix}$ has $D_1 = D_2 = 0$, but $x^TAx = -1$ at $(0, 1)$. For semi-definiteness **all** principal minors must be $\ge 0$.
3. True: $x^T(A + B)x = x^TAx + x^TBx > 0$ for $x \ne 0$.""")

# 23 statements: 1 and 2 only
T.statements(2, ["inertia"],
    r"Consider the following statements about real quadratic forms in $n$ variables:",
    [r"The number of positive coefficients in any diagonal form obtained by a real non-singular linear transformation is the same.",
     r"Two real quadratic forms are congruent if and only if they have the same rank and the same signature.",
     r"The coefficients themselves in a diagonal form obtained by a real non-singular linear transformation are uniquely determined."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1. True: this is Sylvester's law of inertia.
2. True: rank and signature fix $p$ and $q$, hence the normal form $\operatorname{diag}(I_p, -I_q, O)$.
3. False: $x^2 + y^2$ becomes $4X^2 + 9Y^2$ under $x = 2X$, $y = 3Y$. Only the signs are invariant; even under orthogonal maps the order can change.""")

# 24 match: A-3, B-4, C-2, D-1
T.match(2, ["definiteness", "semidefinite"],
    r"Match each quadratic form in List I with its nature in List II.",
    [r"$x^2 + 2xy + y^2$", r"$x^2 + 2xy - y^2$", r"$-x^2 + 2xy - 2y^2$", r"$2x^2 + 2xy + y^2$"],
    [r"positive definite", r"negative definite", r"positive semi-definite but not positive definite", r"indefinite"],
    [r"A-3, B-4, C-2, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-2, C-4, D-1", r"A-3, B-4, C-1, D-2"],
    r"""Use $a$ and $D_2 = ab - h^2$ for $ax^2 + 2hxy + by^2$:
- A: $D_2 = 1 - 1 = 0$; $Q = (x + y)^2 \ge 0$ and vanishes at $(1, -1)$: positive semi-definite, not PD (3).
- B: $D_2 = -1 - 1 = -2 < 0$: indefinite (4).
- C: $a = -1 < 0$, $D_2 = 2 - 1 = 1 > 0$: negative definite (2).
- D: $a = 2 > 0$, $D_2 = 2 - 1 = 1 > 0$: positive definite (1).

Answer: A-3, B-4, C-2, D-1.""")

# 25 match: A-3, B-2, C-1, D-4
T.match(3, ["inertia", "lagrange"],
    r"Match each quadratic form in $x, y, z$ (List I) with its (rank, signature $p - q$) in List II.",
    [r"$x^2 + y^2 - z^2$", r"$2xy$", r"$x^2 + y^2 + z^2 + 2xy + 2yz + 2zx$", r"$-x^2 - y^2$"],
    [r"$(1, 1)$", r"$(2, 0)$", r"$(3, 1)$", r"$(2, -2)$"],
    [r"A-3, B-2, C-1, D-4", r"A-3, B-1, C-2, D-4", r"A-1, B-2, C-3, D-4", r"A-3, B-4, C-1, D-2"],
    r"""- A: already diagonal, $p = 2$, $q = 1$: $(3, 1)$ (3).
- B: $2xy = \tfrac12(x + y)^2 - \tfrac12(x - y)^2$, $p = q = 1$: $(2, 0)$ (2).
- C: $(x + y + z)^2$, a single square: $(1, 1)$ (1). Its matrix is the all-ones $J$, of rank $1$.
- D: $p = 0$, $q = 2$: $(2, -2)$ (4).

Answer: A-3, B-2, C-1, D-4.""")

# 26 AR: 0
T.assertion_reason(1, ["definiteness", "orthogonal-reduction"],
    r"The quadratic form $2x^2 + 2xy + 2y^2$ is positive definite.",
    r"A real quadratic form is positive definite if and only if every eigenvalue of its symmetric matrix is positive.",
    0,
    r"""$A = \begin{pmatrix} 2 & 1\\ 1 & 2\end{pmatrix}$ has eigenvalues $1$ and $3$, both positive, so the form is PD. The reason is the standard eigenvalue test (orthogonal reduction gives $Q = X^2 + 3Y^2$).

Both statements are true, and the reason explains the assertion.""")

# 27 AR: 1
T.assertion_reason(2, ["inertia", "matrix-of-form"],
    r"The signature ($p - q$) of the quadratic form $x^2 - y^2 + 2z^2$ is $1$.",
    r"The rank of a quadratic form equals the rank of its symmetric matrix.",
    1,
    r"""Assertion: true. The form is already diagonal with coefficients $1, -1, 2$: $p = 2$, $q = 1$, signature $1$.

Reason: true; it is the definition of the rank of a form (here $3$). But it says nothing about the split into positive and negative squares, so it does not explain the signature.""")

# 28 AR: 2
T.assertion_reason(1, ["definiteness", "exam-tips"],
    r"The quadratic form $x^2 + 6xy + 2y^2$ is indefinite.",
    r"A real quadratic form whose diagonal coefficients are all positive is positive definite.",
    2,
    r"""Assertion: true. $A = \begin{pmatrix} 1 & 3\\ 3 & 2\end{pmatrix}$ has $\det A = 2 - 9 = -7 < 0$, so the eigenvalues have opposite signs. For instance $Q(1, -1) = 1 - 6 + 2 = -3$ and $Q(1, 0) = 1$.

Reason: false, and this very form is a counterexample. Positive diagonal entries are necessary for PD, not sufficient.""")

# 29 AR: 3
T.assertion_reason(2, ["inertia", "congruence"],
    r"The matrices $\begin{pmatrix} 1 & 0\\ 0 & 1\end{pmatrix}$ and $\begin{pmatrix} 1 & 0\\ 0 & -1\end{pmatrix}$ are congruent over $\R$.",
    r"The number of positive squares in any diagonal form of a real quadratic form, obtained by a real non-singular transformation, is the same.",
    3,
    r"""Assertion: false. Both have rank $2$, but the indices differ ($p = 2$ and $p = 1$). Directly: $P^TIP = P^TP$ is positive definite, so it can never equal $\operatorname{diag}(1, -1)$. Note the determinants $1$ and $-1$ have opposite signs, which congruence cannot produce.

Reason: true; it is Sylvester's law of inertia, and it is exactly why the assertion fails.""")

# 30 AR: 0
T.assertion_reason(3, ["definiteness"],
    r"The quadratic form $x^2 + 4xy + y^2 + z^2$ is not positive definite.",
    r"A real symmetric matrix is positive definite if and only if all its leading principal minors are positive.",
    0,
    r"""$A = \begin{pmatrix} 1 & 2 & 0\\ 2 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$ has $D_1 = 1$, $D_2 = 1 - 4 = -3 < 0$, $D_3 = -3$. Since $D_2 < 0$, Sylvester's criterion (the reason) shows $A$ is not PD. Indeed $Q(1, -1, 0) = 1 - 4 + 1 = -2$.

Both statements are true, and the reason explains the assertion.""")


def check():
    import sympy as sp
    M = sp.Matrix
    x, y, z, u, v, w, k, a = sp.symbols("x y z u v w k a", real=True)
    X3 = M([x, y, z])

    def form(A, vec):
        return sp.expand((vec.T * A * vec)[0])

    def inertia(A):
        """(rank, p, q) from eigenvalues."""
        ev = [sp.re(sp.N(e, 30)) for e in A.eigenvals(multiple=True)]
        p = sum(1 for e in ev if sp.N(e) > 1e-12)
        q = sum(1 for e in ev if sp.N(e) < -1e-12)
        return p + q, p, q

    def lead(A):
        return [A[:i, :i].det() for i in range(1, A.shape[0] + 1)]

    def sorted_ev(A):
        return sorted(A.eigenvals(multiple=True), key=sp.default_sort_key)

    X2 = M([x, y])
    # q1
    A1 = M([[1, 2], [2, 3]])
    eq(form(A1, X2), x**2 + 4*x*y + 3*y**2, "q1")
    assert form(M([[1, 4], [4, 3]]), X2) != x**2 + 4*x*y + 3*y**2
    assert form(M([[3, 2], [2, 1]]), X2) != x**2 + 4*x*y + 3*y**2
    # q2
    Q2 = x**2 + 2*y**2 - z**2 + 4*x*y - 6*y*z + 2*z*x
    eq(form(M([[1, 2, 1], [2, 2, -3], [1, -3, -1]]), X3), Q2, "q2")
    for B in ([[1, 4, 2], [4, 2, -6], [2, -6, -1]], [[1, 2, -3], [2, 2, 1], [-3, 1, -1]], [[1, 2, 1], [2, 2, 3], [1, 3, -1]]):
        assert form(M(B), X3) != Q2
    # q3
    A3 = M([[2, -1, 0], [-1, 3, 2], [0, 2, 1]])
    eq(form(A3, X3), 2*x**2 + 3*y**2 + z**2 - 2*x*y + 4*y*z, "q3")
    eq(form(A3, M([1, 1, 0])), 3, "notes value")
    # q4
    eq(sp.expand(2*(u + v)*(u - v)), 2*u**2 - 2*v**2, "q4")
    P4 = M([[1, 1], [1, -1]])
    assert P4.T * M([[0, 1], [1, 0]]) * P4 == sp.diag(2, -2)
    # q5
    A5 = M([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    r, p, q = inertia(A5); assert (r, p, p - q) == (3, 1, -1), "q5"
    # q6
    assert sorted_ev(M([[3, 1], [1, 3]])) == [2, 4], "q6"
    assert sorted_ev(M([[3, 2], [2, 3]])) == [1, 5]
    # q7
    A7 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    assert sorted_ev(A7) == [1, 1, 4], "q7"
    eq(A7.det(), 4, "q7 det"); assert sorted_ev(2*sp.ones(3, 3)) == [0, 0, 6]
    # q8: realise eigenvalues 3, -2, 0 with a non-diagonal symmetric matrix
    O = M([[1, 1, 0], [1, -1, 0], [0, 0, sp.sqrt(2)]]) / sp.sqrt(2)
    assert sp.simplify(O.T * O) == sp.eye(3)
    A8 = sp.simplify(O * sp.diag(3, -2, 0) * O.T)
    assert inertia(A8) == (2, 1, 1), "q8"
    # q9
    A9 = M([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    assert lead(A9) == [2, 3, 4] and A9.is_positive_definite, "q9"
    eq(form(A9, X3), 2*x**2 + 2*y**2 + 2*z**2 - 2*x*y - 2*y*z, "q9 form")
    # q10
    A10 = M([[1, k], [k, 4]])
    sol = sp.solve_univariate_inequality(lead(A10)[1] > 0, k, relational=False)
    assert sol == sp.Interval.open(-2, 2), "q10"
    assert sp.solve_univariate_inequality(M([[1, 2*k], [2*k, 4]]).det() > 0, k, relational=False) == sp.Interval.open(-1, 1)
    # q11
    A11 = M([[1, 1, 0], [1, 2, a], [0, a, 1]])
    eq(form(A11, X3), x**2 + 2*y**2 + z**2 + 2*x*y + 2*a*y*z, "q11 form")
    eq(lead(A11)[2], 1 - a**2, "q11 D3")
    assert sp.solve_univariate_inequality(lead(A11)[2] > 0, a, relational=False) == sp.Interval.open(-1, 1)
    assert M([[1, 1, 0], [1, 2, sp.Rational(6, 5)], [0, sp.Rational(6, 5), 1]]).is_positive_definite is False  # a=1.2 in sqrt2 range, not PD
    # q12: non-diagonal realisation of D = 2, -1, 4
    A12 = M([[2, 1, 0], [1, 0, 1], [0, 1, -6]])
    assert lead(A12) == [2, -1, 4], "q12 minors"
    r, p, q = inertia(A12); eq(p - q, -1, "q12")
    # q13
    eq(sum(1 for P in range(4) for Q in range(4) if P + Q <= 3), 10, "q13")
    # q14: parity
    poss = {(P + Q, P - Q) for P in range(4) for Q in range(4) if P + Q <= 3}
    assert (3, 2) not in poss and {(3, 1), (2, 0), (2, -2)} <= poss, "q14"
    # q15
    A15 = M([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    eq(form(A15, X3), 2*x*y + 2*y*z, "q15 form")
    r, p, q = inertia(A15); assert (r, p - q) == (2, 0), "q15"
    eq(sp.expand(sp.Rational(1, 2)*(x + y + z)**2 - sp.Rational(1, 2)*(x - y + z)**2), 2*x*y + 2*y*z, "q15 notes")
    eq(sp.expand((2*u**2 - 2*v**2 + 2*u*w - 2*v*w) - (2*(u + w/2)**2 - 2*(v + w/2)**2)), 0, "q15 lagrange")
    # q16
    A16 = M([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
    assert inertia(A16) == (3, 2, 1), "q16"
    eq(form(A16, M([1, 1, 1])), -3, "q16 test")
    # q17
    eq(sp.expand((x + 2*y)**2 + y**2), x**2 + 4*x*y + 5*y**2, "q17")
    assert sp.expand((x + 4*y)**2 + y**2) != x**2 + 4*x*y + 5*y**2
    assert sp.expand((x + 2*y)**2 + 5*y**2) != x**2 + 4*x*y + 5*y**2
    # q18
    Q18 = x**2 + 2*y**2 + 3*z**2 + 2*x*y + 4*y*z
    eq(sp.expand((x + y)**2 + (y + 2*z)**2 - z**2), Q18, "q18")
    for d in ((x + y)**2 + (y + 2*z)**2 + z**2, (x + y)**2 + (y + z)**2 + 2*z**2, (x + 2*y)**2 + (y + 2*z)**2 - z**2):
        assert sp.expand(d) != Q18
    eq(M([[1, 1, 0], [1, 2, 2], [0, 2, 3]]).det(), -1, "q18 det")
    # q19
    A19 = M([[5, 2], [2, 2]])
    assert sorted_ev(A19) == [1, 6], "q19"
    eq(form(A19, M([2, 1]) / sp.sqrt(5)), 6, "q19 attained")
    # q20
    A20 = M([[1, 1, 1], [1, 1, 1], [1, 1, 0]])
    assert lead(A20) == [1, 0, 0]
    eq(form(A20, X3), sp.expand((x + y + z)**2 - z**2), "q20 form")
    assert inertia(A20) == (2, 1, 1), "q20"
    eq(form(A20, M([1, 0, -1])), -1, "q20 test"); eq(A20[1:, 1:].det(), -1, "q20 minor")
    # q21: 1 true, 2 and 3 false
    A21, P21 = sp.eye(2), 2*sp.eye(2)
    B21 = P21.T * A21 * P21
    assert B21.rank() == A21.rank() and sorted_ev(B21) != sorted_ev(A21) and B21.det() != A21.det(), "q21"
    Ar = M([[1, 2], [2, -1]]); Pr = M([[1, 3], [0, 2]])
    assert (Pr.T * Ar * Pr).rank() == Ar.rank() and sp.sign((Pr.T*Ar*Pr).det()) == sp.sign(Ar.det())
    # q22: 1 true, 2 false, 3 true
    Apd = M([[2, 1], [1, 3]]); Bpd = M([[1, -1], [-1, 2]])
    assert Apd.is_positive_definite and Bpd.is_positive_definite and (Apd + Bpd).is_positive_definite
    assert all(Apd[i, i] > 0 for i in range(2))
    C22 = M([[0, 0], [0, -1]])
    assert all(m >= 0 for m in lead(C22)) and form(C22, M([0, 1])) < 0, "q22 s2"
    # q23
    eq(sp.expand(((2*u)**2 + (3*v)**2)), 4*u**2 + 9*v**2, "q23 s3")
    assert inertia(M([[0, 1], [1, 0]])) == inertia(sp.diag(1, -1))
    # q24
    natures = {}
    for key, B in {"A": [[1, 1], [1, 1]], "B": [[1, 1], [1, -1]], "C": [[-1, 1], [1, -2]], "D": [[2, 1], [1, 1]]}.items():
        r, p, q = inertia(M(B)); natures[key] = (r, p, q)
    assert natures == {"A": (1, 1, 0), "B": (2, 1, 1), "C": (2, 0, 2), "D": (2, 2, 0)}, "q24"
    eq(form(M([[-1, 1], [1, -2]]), X2), -x**2 + 2*x*y - 2*y**2, "q24 C form")
    eq(form(M([[2, 1], [1, 1]]), X2), 2*x**2 + 2*x*y + y**2, "q24 D form")
    # q25
    got = {}
    for key, B in {"A": sp.diag(1, 1, -1), "B": M([[0, 1, 0], [1, 0, 0], [0, 0, 0]]), "C": sp.ones(3, 3), "D": sp.diag(-1, -1, 0)}.items():
        r, p, q = inertia(B); got[key] = (r, p - q)
    assert got == {"A": (3, 1), "B": (2, 0), "C": (1, 1), "D": (2, -2)}, "q25"
    eq(form(sp.ones(3, 3), X3), sp.expand((x + y + z)**2), "q25 C")
    # q26
    assert sorted_ev(M([[2, 1], [1, 2]])) == [1, 3], "q26"
    # q27
    r, p, q = inertia(sp.diag(1, -1, 2)); assert (r, p - q) == (3, 1), "q27"
    # q28
    A28 = M([[1, 3], [3, 2]])
    eq(A28.det(), -7, "q28"); eq(form(A28, M([1, -1])), -3, "q28 test")
    assert inertia(A28) == (2, 1, 1)
    # q29: identity and diag(1,-1) differ in index
    assert inertia(sp.eye(2))[1] != inertia(sp.diag(1, -1))[1], "q29"
    # q30
    A30 = M([[1, 2, 0], [2, 1, 0], [0, 0, 1]])
    assert lead(A30) == [1, -3, -3] and not A30.is_positive_definite, "q30"
    eq(form(A30, M([1, -1, 0])), -2, "q30 test")
    # notes checks
    eq(sp.expand((x + y + z)**2 + (y - z)**2), x**2 + 2*y**2 + 2*z**2 + 2*x*y + 2*z*x, "notes lagrange 2")
    assert sorted_ev(M([[1, 1], [1, 3]])) == sorted([2 - sp.sqrt(2), 2 + sp.sqrt(2)], key=sp.default_sort_key), "notes caution"
    eq(sp.expand(sp.Rational(1, 2)*((x - y)**2 + (y - z)**2 + (z - x)**2)), x**2 + y**2 + z**2 - x*y - y*z - z*x, "notes psd")


T.write(check)
