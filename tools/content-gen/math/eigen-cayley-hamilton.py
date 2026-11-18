import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.eigen-cayley-hamilton")

# 1
T.single(1, ["characteristic-polynomial"],
    r"The characteristic equation of $A = \begin{pmatrix} 1 & 2\\ 3 & 4\end{pmatrix}$ is",
    [r"$\lambda^2 - 5\lambda - 2 = 0$", r"$\lambda^2 + 5\lambda - 2 = 0$",
     r"$\lambda^2 - 5\lambda + 2 = 0$", r"$\lambda^2 - 5\lambda + 10 = 0$"],
    r"""For a $2 \times 2$ matrix, $\chi_A(\lambda) = \lambda^2 - (\operatorname{tr} A)\lambda + \det A$.

Here $\operatorname{tr} A = 5$ and $\det A = 4 - 6 = -2$, so
$$\lambda^2 - 5\lambda - 2 = 0.$$

$\lambda^2 - 5\lambda + 10$ comes from adding the cross product instead of subtracting it ($4 + 6$); $\lambda^2 + 5\lambda - 2$ has the wrong sign on the trace term.""")

# 2
T.single(1, ["characteristic-polynomial", "exam-tips"],
    r"The eigenvalues of $\begin{pmatrix} 2 & 1\\ 1 & 2\end{pmatrix}$ are",
    [r"$1$ and $3$", r"$0$ and $4$", r"$2$ and $2$", r"$-1$ and $3$"],
    r"""$\operatorname{tr} A = 4$ and $\det A = 3$, so $\lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3) = 0$, giving $\lambda = 1, 3$.

Check: $1 + 3 = 4$ (trace) and $1 \cdot 3 = 3$ (determinant). The pair $0, 4$ has the right sum but product $0 \ne 3$; the pair $-1, 3$ has the wrong sum.""")

# 3
T.single(1, ["properties"],
    r"The eigenvalues of $\begin{pmatrix} 2 & 5 & 7\\ 0 & -3 & 1\\ 0 & 0 & 4\end{pmatrix}$ are",
    [r"$2, -3, 4$", r"$2, 5, 7$", r"$7, 1, 4$", r"$-2, 3, -4$"],
    r"""The matrix is upper triangular, so $\det(\lambda I - A) = (\lambda - 2)(\lambda + 3)(\lambda - 4)$. The eigenvalues are the **diagonal entries** $2, -3, 4$.

The entries above the diagonal play no part. Check: their sum $3$ equals the trace.""")

# 4
T.single(1, ["properties"],
    r"A $3 \times 3$ matrix $A$ has eigenvalues $2, 3, -1$. Then $\det A$ equals",
    [r"$-6$", r"$6$", r"$4$", r"$-4$"],
    r"""The determinant is the **product** of the eigenvalues:
$$\det A = 2 \cdot 3 \cdot (-1) = -6.$$

$4$ is the sum of the eigenvalues, which is the trace, not the determinant. $6$ drops the sign of $-1$.""")

# 5
T.single(2, ["properties"],
    r"A $3 \times 3$ matrix $A$ has eigenvalues $1, 2, 3$. The eigenvalues of $\operatorname{adj} A$ are",
    [r"$6, 3, 2$", r"$1, \tfrac12, \tfrac13$", r"$1, 4, 9$", r"$6, 12, 18$"],
    r"""$\det A = 1 \cdot 2 \cdot 3 = 6 \ne 0$, so $A$ is invertible and $\operatorname{adj} A = (\det A)A^{-1}$.

The eigenvalues of $A^{-1}$ are $1/\lambda$, so those of $\operatorname{adj} A$ are $\det A/\lambda$:
$$\frac61, \frac62, \frac63 = 6, 3, 2.$$

$1, \frac12, \frac13$ are the eigenvalues of $A^{-1}$; it forgets the factor $\det A$. $6, 12, 18$ multiplies by $\lambda$ instead of dividing.""")

# 6
T.single(2, ["properties"],
    r"A $2 \times 2$ matrix $A$ has eigenvalues $2$ and $-1$. The eigenvalues of $A^2 - 3A + I$ are",
    [r"$-1$ and $5$", r"$11$ and $-1$", r"$1$ and $5$", r"$-1$ and $-5$"],
    r"""If $Ax = \lambda x$, then $p(A)x = p(\lambda)x$. With $p(\lambda) = \lambda^2 - 3\lambda + 1$:
$$p(2) = 4 - 6 + 1 = -1, \qquad p(-1) = 1 + 3 + 1 = 5.$$

The option $11, -1$ comes from using $\lambda^2 + 3\lambda + 1$ (a sign slip).""")

# 7
T.single(1, ["special-matrices"],
    r"Which of the following can be an eigenvalue of a real orthogonal matrix?",
    [r"$-1$", r"$2$", r"$\tfrac12$", r"$0$"],
    r"""If $A^TA = I$ and $Ax = \lambda x$ with $x \neq 0$, then $\lVert Ax\rVert = \lVert x\rVert$, so $\lvert\lambda\rvert = 1$.

Among the options only $-1$ has modulus $1$. For example, $\begin{pmatrix}-1 & 0\\ 0 & 1\end{pmatrix}$ is orthogonal with eigenvalue $-1$. $0$ is impossible because an orthogonal matrix is invertible.""")

# 8
T.single(2, ["cayley-hamilton"],
    r"For $A = \begin{pmatrix} 3 & 1\\ 2 & 2\end{pmatrix}$, the Cayley–Hamilton theorem gives $A^{-1} =$",
    [r"$\dfrac{5I - A}{4}$", r"$\dfrac{A - 5I}{4}$", r"$\dfrac{A + 5I}{4}$", r"$\dfrac{4I - A}{5}$"],
    r"""$\operatorname{tr} A = 5$, $\det A = 6 - 2 = 4$, so $A^2 - 5A + 4I = O$.

Rearrange: $A(5I - A) = 4I$, hence
$$A^{-1} = \frac{5I - A}{4} = \frac14\begin{pmatrix} 2 & -1\\ -2 & 3\end{pmatrix}.$$

Check: this agrees with $\frac{1}{\det A}\operatorname{adj} A$. $\frac{A - 5I}{4}$ has the wrong sign; $\frac{4I - A}{5}$ swaps the roles of trace and determinant.""")

# 9
T.single(3, ["cayley-hamilton"],
    r"Let $A = \begin{pmatrix} 2 & -1\\ 1 & 0\end{pmatrix}$. Then $A^{50}$ equals",
    [r"$50A - 49I$", r"$49A - 50I$", r"$50A + 49I$", r"$I$"],
    r"""$\operatorname{tr} A = 2$, $\det A = 1$, so $\chi_A = \lambda^2 - 2\lambda + 1 = (\lambda - 1)^2$ and, by Cayley–Hamilton, $A^2 = 2A - I$.

Write $A^m = aA + bI$. Then $\lambda^m = a\lambda + b$ at $\lambda = 1$, and, because $1$ is a double root, also the derivative $m\lambda^{m-1} = a$ at $\lambda = 1$. So $a = m$ and $b = 1 - m$:
$$A^{50} = 50A - 49I.$$

Check with $m = 2$: $2A - I$. The tempting answer $I$ assumes that "all eigenvalues are $1$" forces $A^{50} = I$. That holds only for a diagonalisable $A$, which would then equal $I$; here $A \ne I$, so $A$ is not diagonalisable.""")

# 10
T.single(2, ["cayley-hamilton"],
    r"The characteristic polynomial of a $3 \times 3$ matrix $A$ is $\lambda^3 - 6\lambda^2 + 11\lambda - 6$. Then $A^{-1}$ equals",
    [r"$\dfrac{A^2 - 6A + 11I}{6}$", r"$-\dfrac{A^2 - 6A + 11I}{6}$",
     r"$\dfrac{A^2 - 6A + 11I}{11}$", r"$\dfrac{A^2 + 6A + 11I}{6}$"],
    r"""By Cayley–Hamilton, $A^3 - 6A^2 + 11A - 6I = O$, so
$$A\left(A^2 - 6A + 11I\right) = 6I \quad\Longrightarrow\quad A^{-1} = \frac{A^2 - 6A + 11I}{6}.$$

The constant term $-6$ moves to the right as $+6I$; the option with the minus sign misses this. $\det A = 6 \ne 0$, so the inverse exists.""")

# 11
T.single(2, ["eigenvectors"],
    r"An eigenvector of $\begin{pmatrix} 4 & 1\\ 2 & 3\end{pmatrix}$ belonging to the eigenvalue $2$ is",
    [r"$(1, -2)^T$", r"$(1, 1)^T$", r"$(2, -1)^T$", r"$(1, 2)^T$"],
    r"""Solve $(A - 2I)x = 0$: $A - 2I = \begin{pmatrix} 2 & 1\\ 2 & 1\end{pmatrix}$, so $2x + y = 0$, i.e. $y = -2x$. Take $x = (1, -2)^T$.

Check: $A(1, -2)^T = (2, -4)^T = 2(1, -2)^T$. The vector $(1, 1)^T$ is the eigenvector for the other eigenvalue $5$; $(2, -1)^T$ gives $A x = (7, 1)^T$, not a multiple.""")

# 12
T.single(3, ["eigenvectors"],
    r"For $A = \begin{pmatrix} 3 & 1 & 1\\ 0 & 3 & 0\\ 0 & 0 & 3\end{pmatrix}$, the algebraic and geometric multiplicities of the eigenvalue $3$ are, respectively,",
    [r"$3$ and $2$", r"$3$ and $1$", r"$3$ and $3$", r"$2$ and $1$"],
    r"""$A$ is triangular with all diagonal entries $3$, so $\chi_A = (\lambda - 3)^3$: algebraic multiplicity $3$.

$$A - 3I = \begin{pmatrix} 0 & 1 & 1\\ 0 & 0 & 0\\ 0 & 0 & 0\end{pmatrix}$$
has rank $1$, so the geometric multiplicity is $3 - 1 = 2$ (eigenspace $y + z = 0$).

$3$ and $1$ would be right for a single Jordan block; here the two off-diagonal $1$s sit in the same row, so the rank is only $1$.""")

# 13
T.single(3, ["diagonalisation"],
    r"Let $A = \begin{pmatrix} 2 & 0 & 0\\ a & 2 & 0\\ b & c & 3\end{pmatrix}$ with real $a, b, c$. Then $A$ is diagonalisable if and only if",
    [r"$a = 0$", r"$c = 0$", r"$b = 0$", r"$a = b = c = 0$"],
    r"""The eigenvalues are $2, 2, 3$. The simple eigenvalue $3$ causes no trouble; $A$ is diagonalisable iff the geometric multiplicity of $2$ is $2$, i.e. $\operatorname{rank}(A - 2I) = 1$.

$$A - 2I = \begin{pmatrix} 0 & 0 & 0\\ a & 0 & 0\\ b & c & 1\end{pmatrix}.$$
The third row is non-zero. If $a \neq 0$, rows 2 and 3 are independent (rank $2$); if $a = 0$, the rank is $1$.

So the condition is $a = 0$, whatever $b$ and $c$ are. "$a = b = c = 0$" is sufficient but not necessary.""")

# 14
T.single(2, ["diagonalisation", "properties"],
    r"For $A = \begin{pmatrix} 1 & 2\\ 2 & 1\end{pmatrix}$, the trace of $A^5$ is",
    [r"$242$", r"$244$", r"$243$", r"$32$"],
    r"""$\operatorname{tr} A = 2$, $\det A = -3$, so $\lambda^2 - 2\lambda - 3 = 0$ and $\lambda = 3, -1$.

The eigenvalues of $A^5$ are $3^5$ and $(-1)^5$, so
$$\operatorname{tr}(A^5) = 243 - 1 = 242.$$

$244$ uses $(-1)^5 = +1$; $32 = (\operatorname{tr} A)^5$ wrongly treats the trace as multiplicative.""")

# 15
T.single(3, ["diagonalisation"],
    r"For $A = \begin{pmatrix} 4 & 1\\ 2 & 3\end{pmatrix}$ and every positive integer $n$, the $(1,1)$ entry of $A^n$ is",
    [r"$\dfrac{2\cdot 5^n + 2^n}{3}$", r"$\dfrac{5^n + 2\cdot 2^n}{3}$",
     r"$\dfrac{2\cdot 5^n - 2^n}{3}$", r"$5^n - 2^n$"],
    r"""Eigenvalues $5, 2$ with eigenvectors $(1, 1)^T$ and $(1, -2)^T$. Take
$$P = \begin{pmatrix} 1 & 1\\ 1 & -2\end{pmatrix},\quad P^{-1} = \frac13\begin{pmatrix} 2 & 1\\ 1 & -1\end{pmatrix}.$$

Then $A^n = P\operatorname{diag}(5^n, 2^n)P^{-1}$, whose $(1,1)$ entry is
$$\frac{2\cdot 5^n + 2^n}{3}.$$

Check at $n = 1$: $(10 + 2)/3 = 4$. The option $(5^n + 2\cdot 2^n)/3$ gives $3$ at $n = 1$, and $(2\cdot5^n - 2^n)/3$ gives $\frac83$.""")

# 16
T.single(1, ["characteristic-polynomial", "properties"],
    r"A $2 \times 2$ matrix has trace $7$ and determinant $10$. Its eigenvalues are",
    [r"$2$ and $5$", r"$-2$ and $-5$", r"$3$ and $4$", r"$1$ and $10$"],
    r"""The characteristic equation is $\lambda^2 - 7\lambda + 10 = 0$, i.e. $(\lambda - 2)(\lambda - 5) = 0$.

The eigenvalues must add to $7$ and multiply to $10$: only $2, 5$ does both. $3, 4$ has the right sum but product $12$; $1, 10$ has the right product but sum $11$.""")

# 17
T.single(2, ["characteristic-polynomial"],
    r"The characteristic equation of $A = \begin{pmatrix} 1 & 2 & 0\\ 0 & 3 & 1\\ 1 & 0 & 2\end{pmatrix}$ is",
    [r"$\lambda^3 - 6\lambda^2 + 11\lambda - 8 = 0$", r"$\lambda^3 + 6\lambda^2 + 11\lambda + 8 = 0$",
     r"$\lambda^3 - 6\lambda^2 + 11\lambda - 6 = 0$", r"$\lambda^3 - 6\lambda^2 + 9\lambda - 8 = 0$"],
    r"""Use $\lambda^3 - (\operatorname{tr} A)\lambda^2 + S_2\lambda - \det A = 0$.

- $\operatorname{tr} A = 1 + 3 + 2 = 6$.
- Principal minors of order 2: $\begin{vmatrix} 1 & 2\\ 0 & 3\end{vmatrix} = 3$, $\begin{vmatrix} 1 & 0\\ 1 & 2\end{vmatrix} = 2$, $\begin{vmatrix} 3 & 1\\ 0 & 2\end{vmatrix} = 6$, so $S_2 = 11$.
- $\det A = 1(6 - 0) - 2(0 - 1) + 0 = 8$.

$$\lambda^3 - 6\lambda^2 + 11\lambda - 8 = 0.$$

The option ending in $-6$ takes the product of the diagonal entries instead of the determinant; that works only for triangular matrices.""")

# 18
T.single(2, ["special-matrices"],
    r"Which of the following can be the complete list of eigenvalues of a real $3 \times 3$ skew-symmetric matrix?",
    [r"$0, 2i, -2i$", r"$0, 1, -1$", r"$1, i, -i$", r"$0, 2i, 2i$"],
    r"""Eigenvalues of a real skew-symmetric matrix are $0$ or purely imaginary, and, since the matrix is real, non-real ones come in conjugate pairs. So $0, 2i, -2i$ is possible: for example, $\begin{pmatrix} 0 & -2 & 0\\ 2 & 0 & 0\\ 0 & 0 & 0\end{pmatrix}$.

$0, \pm1$ and $1, \pm i$ contain non-zero real eigenvalues. $0, 2i, 2i$ is not closed under conjugation (and its sum $4i$ cannot be the real trace $0$).""")

# 19
T.single(2, ["special-matrices"],
    r"A real symmetric $2 \times 2$ matrix has eigenvalues $3$ and $-1$, and $(1, 2)^T$ is an eigenvector for $3$. An eigenvector for $-1$ is",
    [r"$(2, -1)^T$", r"$(1, -2)^T$", r"$(2, 1)^T$", r"$(-1, 2)^T$"],
    r"""For a real symmetric matrix, eigenvectors belonging to distinct eigenvalues are **orthogonal**. In $\R^2$ the vectors orthogonal to $(1, 2)^T$ are multiples of $(2, -1)^T$.

Check dot products with $(1, 2)$: $(2, -1) \to 0$; $(1, -2) \to -3$; $(2, 1) \to 4$; $(-1, 2) \to 3$. Only the first is orthogonal.""")

# 20
T.single(3, ["minimal-polynomial"],
    r"The minimal polynomial of $\begin{pmatrix} 2 & 1 & 0\\ 0 & 2 & 0\\ 0 & 0 & 2\end{pmatrix}$ is",
    [r"$(x - 2)^2$", r"$(x - 2)^3$", r"$x - 2$", r"$(x - 2)(x + 2)$"],
    r"""$\chi_A = (x - 2)^3$, so $m_A$ is $(x - 2)^k$ for some $k \le 3$.

- $A - 2I = \begin{pmatrix} 0 & 1 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0\end{pmatrix} \ne O$, so $k \ne 1$.
- $(A - 2I)^2 = O$, so $k = 2$.

$$m_A(x) = (x - 2)^2.$$

$(x - 2)^3$ is the characteristic polynomial, not the least-degree one. $(x - 2)(x + 2)$ has the root $-2$, which is not an eigenvalue.""")

# 21
T.single(3, ["cayley-hamilton"],
    r"For $A = \begin{pmatrix} 1 & 2\\ 3 & 4\end{pmatrix}$, Cayley–Hamilton gives $A^3 =$",
    [r"$27A + 10I$", r"$25A + 10I$", r"$27A + 2I$", r"$23A - 10I$"],
    r"""$\chi_A = \lambda^2 - 5\lambda - 2$, so $A^2 = 5A + 2I$. Then
$$A^3 = 5A^2 + 2A = 5(5A + 2I) + 2A = 27A + 10I.$$

$25A + 10I$ forgets the $2A$ from the second step. Check one entry: $A^3$ has $(1,1)$ entry $37 = 27 + 10$.""")

# 22 statements
T.statements(2, ["properties"],
    r"Consider the following statements about an $n \times n$ real matrix $A$:",
    [r"$A$ and $A^T$ have the same eigenvalues.",
     r"$A$ and $A^T$ have the same eigenvectors.",
     r"If $A$ is invertible, then $0$ is not an eigenvalue of $A$."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1. True: $\det(\lambda I - A^T) = \det\big((\lambda I - A)^T\big) = \det(\lambda I - A)$.
2. False: for $A = \begin{pmatrix} 1 & 1\\ 0 & 2\end{pmatrix}$, $(1, 0)^T$ is an eigenvector of $A$, but $A^T(1, 0)^T = (1, 1)^T$ is not a multiple of it.
3. True: $\det A = \prod\lambda_i \ne 0$, so no eigenvalue is $0$.""")

# 23 statements
T.statements(3, ["diagonalisation", "eigenvectors"],
    r"Consider the following statements about $n \times n$ real matrices:",
    [r"A matrix with $n$ distinct real eigenvalues is diagonalisable over $\R$.",
     r"A matrix that is diagonalisable must have $n$ distinct eigenvalues.",
     r"If the characteristic polynomial of a matrix splits into real linear factors, the matrix is diagonalisable over $\R$."],
    [r"1 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"],
    r"""1. True: eigenvectors for distinct eigenvalues are linearly independent, so there are $n$ independent eigenvectors.
2. False: $I_n$ is diagonal (hence diagonalisable) but has the single eigenvalue $1$.
3. False: $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ has $\chi = (\lambda - 1)^2$, which splits, but the geometric multiplicity of $1$ is only $1$.

Splitting is necessary, but one also needs geometric multiplicity = algebraic multiplicity for every eigenvalue.""")

# 24 match
T.match(1, ["properties"],
    r"A $2 \times 2$ matrix $A$ has eigenvalues $2$ and $3$. Match each matrix in List I with its eigenvalues in List II.",
    [r"$A^{-1}$", r"$A^2$", r"$A - 2I$", r"$3A$"],
    [r"$4, 9$", r"$6, 9$", r"$\tfrac12, \tfrac13$", r"$0, 1$"],
    [r"A-3, B-1, C-4, D-2", r"A-3, B-2, C-4, D-1", r"A-4, B-1, C-3, D-2", r"A-3, B-1, C-2, D-4"],
    r"""Apply $\lambda \mapsto f(\lambda)$ to $2$ and $3$:
- $A^{-1}$: $\frac12, \frac13$ (3)
- $A^2$: $4, 9$ (1)
- $A - 2I$: $0, 1$ (4)
- $3A$: $6, 9$ (2)

So A-3, B-1, C-4, D-2.""")

# 25 match
T.match(2, ["special-matrices", "characteristic-polynomial"],
    r"Match each matrix in List I with its eigenvalues in List II.",
    [r"$\begin{pmatrix} 0 & 1\\ -1 & 0\end{pmatrix}$", r"$\begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 1\\ 1 & 1\end{pmatrix}$", r"$\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$"],
    [r"$0, 2$", r"$i, -i$", r"$1, 1$", r"$1, -1$"],
    [r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-3, D-1", r"A-2, B-1, C-4, D-3"],
    r"""Use $\lambda^2 - (\operatorname{tr})\lambda + \det = 0$:
- A: trace $0$, det $1$: $\lambda^2 + 1 = 0$, so $\pm i$ (2). (Skew-symmetric, also orthogonal.)
- B: trace $0$, det $-1$: $\lambda^2 - 1 = 0$, so $\pm 1$ (4).
- C: trace $2$, det $0$: $\lambda(\lambda - 2) = 0$, so $0, 2$ (1).
- D: triangular, diagonal $1, 1$ (3).

So A-2, B-4, C-1, D-3. Swapping A and B is the usual slip: the symmetric one has real eigenvalues.""")

# 26 AR: 0
T.assertion_reason(1, ["special-matrices"],
    r"The eigenvalues of $\begin{pmatrix} 1 & 2\\ 2 & -2\end{pmatrix}$ are real.",
    r"Every eigenvalue of a real symmetric matrix is real.",
    0,
    r"""The matrix is real symmetric, so by the reason its eigenvalues are real. Directly: $\lambda^2 + \lambda - 6 = 0$, so $\lambda = 2, -3$.

Both statements are true, and the reason explains the assertion.""")

# 27 AR: 1
T.assertion_reason(2, ["properties"],
    r"The sum of the eigenvalues of $\begin{pmatrix} 1 & 2\\ 3 & 4\end{pmatrix}$ is $5$.",
    r"The product of the eigenvalues of a square matrix equals its determinant.",
    1,
    r"""Assertion: true, because the sum of the eigenvalues is the trace, $1 + 4 = 5$.

Reason: true ($\prod\lambda_i = \det A$; here $-2$). But it is about the **product**, so it does not explain a statement about the **sum**. The explanation is $\sum\lambda_i = \operatorname{tr} A$.""")

# 28 AR: 2
T.assertion_reason(2, ["diagonalisation", "eigenvectors"],
    r"The matrix $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ is not diagonalisable.",
    r"A square matrix with a repeated eigenvalue is never diagonalisable.",
    2,
    r"""Assertion: true. The eigenvalue $1$ has algebraic multiplicity $2$, but $A - I = \begin{pmatrix} 0 & 1\\ 0 & 0\end{pmatrix}$ has rank $1$, so the geometric multiplicity is $1$.

Reason: false. $I_2$ has the repeated eigenvalue $1$ and is diagonal. A repeated eigenvalue only makes failure *possible*; what matters is whether the geometric multiplicity equals the algebraic one.""")

# 29 AR: 3
T.assertion_reason(3, ["minimal-polynomial"],
    r"The minimal polynomial of $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ is $x - 1$.",
    r"The minimal polynomial of a square matrix divides its characteristic polynomial.",
    3,
    r"""Assertion: false. If $m_A = x - 1$ then $A - I = O$, but $A - I = \begin{pmatrix} 0 & 1\\ 0 & 0\end{pmatrix} \ne O$. In fact $(A - I)^2 = O$, so $m_A = (x - 1)^2 = \chi_A$.

Reason: true, because $\chi_A(A) = O$ by Cayley–Hamilton and $m_A$ divides every polynomial that annihilates $A$.""")

# 30 AR: 0
T.assertion_reason(2, ["cayley-hamilton"],
    r"If the characteristic polynomial of a $3 \times 3$ matrix $A$ is $\lambda^3 - 2\lambda^2 + \lambda - 5$, then $A^3 - 2A^2 + A = 5I$.",
    r"Every square matrix satisfies its own characteristic equation.",
    0,
    r"""The reason is the Cayley–Hamilton theorem. Applied here it gives $A^3 - 2A^2 + A - 5I = O$, which is exactly the assertion.

Both are true, and the reason explains the assertion.""")


def check():
    import sympy as sp
    lam, x = sp.symbols("lambda x")
    M = sp.Matrix
    I2, I3 = sp.eye(2), sp.eye(3)

    def cp(A):
        return A.charpoly(lam).as_expr()

    def ev(A):  # sorted list of eigenvalues with multiplicity
        return sorted(sum(([k] * v for k, v in A.eigenvals().items()), []), key=sp.default_sort_key)

    def same(a, b, label):
        if sorted(a, key=sp.default_sort_key) != sorted(b, key=sp.default_sort_key):
            sys.exit(f"CHECK FAILED {label}: {a} vs {b}")

    # q1
    eq(cp(M([[1, 2], [3, 4]])), lam**2 - 5*lam - 2, "q1")
    # q2
    same(ev(M([[2, 1], [1, 2]])), [1, 3], "q2")
    # q3
    same(ev(M([[2, 5, 7], [0, -3, 1], [0, 0, 4]])), [2, -3, 4], "q3")
    # q4: realise eigenvalues with a non-diagonal matrix
    A4 = M([[2, 1, 0], [0, 3, 1], [0, 0, -1]])
    same(ev(A4), [2, 3, -1], "q4 ev"); eq(A4.det(), -6, "q4")
    # q5: adj eigenvalues
    A5 = M([[1, 1, 0], [0, 2, 1], [0, 0, 3]])
    same(ev(A5.adjugate()), [6, 3, 2], "q5")
    # q6
    A6 = M([[2, 1], [0, -1]])
    same(ev(A6**2 - 3*A6 + I2), [-1, 5], "q6")
    # q7: orthogonal with eigenvalue -1, and |lambda| = 1 for a rotation
    R = M([[-1, 0], [0, 1]]); assert R.T*R == I2 and -1 in R.eigenvals()
    th = sp.symbols("theta", real=True)
    Rot = M([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
    for e in Rot.eigenvals():
        eq(sp.simplify(e * sp.conjugate(e)), 1, "q7 |lambda|")
    # q8
    A8 = M([[3, 1], [2, 2]])
    assert A8.inv() == (5*I2 - A8)/4, "q8"
    assert A8.inv() != (A8 - 5*I2)/4 and A8.inv() != (A8 + 5*I2)/4 and A8.inv() != (4*I2 - A8)/5
    # q9
    A9 = M([[2, -1], [1, 0]])
    assert A9**50 == 50*A9 - 49*I2, "q9"
    assert A9**50 != I2 and A9**50 != 49*A9 - 50*I2 and A9**50 != 50*A9 + 49*I2
    # q10: companion matrix of the given polynomial (non-diagonal)
    A10 = M([[0, 0, 6], [1, 0, -11], [0, 1, 6]])
    eq(cp(A10), lam**3 - 6*lam**2 + 11*lam - 6, "q10 cp")
    assert A10.inv() == (A10**2 - 6*A10 + 11*I3)/6, "q10"
    # q11
    A11 = M([[4, 1], [2, 3]])
    assert A11*M([1, -2]) == 2*M([1, -2]), "q11"
    for w in ([1, 1], [2, -1], [1, 2]):
        assert A11*M(w) != 2*M(w)
    # q12
    A12 = M([[3, 1, 1], [0, 3, 0], [0, 0, 3]])
    eq(A12.eigenvals()[3], 3, "q12 am"); eq(3 - (A12 - 3*I3).rank(), 2, "q12 gm")
    # q13
    a, b, c = sp.symbols("a b c")
    def diag13(av, bv, cv):
        return M([[2, 0, 0], [av, 2, 0], [bv, cv, 3]]).is_diagonalizable()
    assert diag13(0, 5, 7) and diag13(0, -1, 2) and not diag13(1, 0, 0) and not diag13(2, 3, 0), "q13"
    assert not diag13(1, 0, 0)  # c = 0, b = 0 but a != 0: not diagonalisable, so b=0 / c=0 are wrong
    # q14
    eq((M([[1, 2], [2, 1]])**5).trace(), 242, "q14")
    # q15
    n = sp.symbols("n", positive=True, integer=True)
    for k in range(1, 7):
        eq((A11**k)[0, 0], (2*5**k + 2**k)/sp.Integer(3), f"q15 n={k}")
    eq((A11**2)[0, 0] - (5**2 + 2*2**2)/sp.Integer(3), 18 - 11, "q15 distractor differs")
    # q16
    same(ev(M([[2, 1], [0, 5]])), [2, 5], "q16"); eq(sp.Integer(2 + 5), 7, "q16 tr"); eq(sp.Integer(2*5), 10, "q16 det")
    # q17
    eq(cp(M([[1, 2, 0], [0, 3, 1], [1, 0, 2]])), lam**3 - 6*lam**2 + 11*lam - 8, "q17")
    # q18
    S = M([[0, -2, 0], [2, 0, 0], [0, 0, 0]]); assert S.T == -S
    same(ev(S), [0, 2*sp.I, -2*sp.I], "q18")
    # q19
    u, v = M([1, 2]), M([2, -1])
    A19 = (3*u*u.T - v*v.T)/5
    assert A19 == A19.T and A19*u == 3*u and A19*v == -v, "q19"
    for w in ([1, -2], [2, 1], [-1, 2]):
        assert (u.T*M(w))[0] != 0
    # q20
    A20 = M([[2, 1, 0], [0, 2, 0], [0, 0, 2]])
    assert A20 - 2*I3 != sp.zeros(3) and (A20 - 2*I3)**2 == sp.zeros(3), "q20"
    # q21
    A21 = M([[1, 2], [3, 4]])
    assert A21**3 == 27*A21 + 10*I2, "q21"
    assert A21**3 != 25*A21 + 10*I2
    # q22 statements: 1 true, 2 false, 3 true
    B = M([[1, 1], [0, 2]])
    same(ev(B), ev(B.T), "q22 s1")
    e = M([1, 0]); assert B*e == 1*e and (B.T*e) != (B.T*e)[0]*e, "q22 s2 counterexample"
    assert 0 not in A21.eigenvals() and A21.det() != 0, "q22 s3"
    # q23 statements: 1 true, 2 false, 3 false
    assert A11.is_diagonalizable() and len(A11.eigenvals()) == 2, "q23 s1"
    assert I3.is_diagonalizable() and len(I3.eigenvals()) == 1, "q23 s2 counterexample"
    J = M([[1, 1], [0, 1]])
    assert sp.factor(cp(J)) == (lam - 1)**2 and not J.is_diagonalizable(), "q23 s3 counterexample"
    # q24 match: A-3, B-1, C-4, D-2
    A24 = M([[2, 1], [0, 3]])
    same(ev(A24.inv()), [sp.Rational(1, 2), sp.Rational(1, 3)], "q24 A")
    same(ev(A24**2), [4, 9], "q24 B")
    same(ev(A24 - 2*I2), [0, 1], "q24 C")
    same(ev(3*A24), [6, 9], "q24 D")
    # q25 match: A-2, B-4, C-1, D-3
    same(ev(M([[0, 1], [-1, 0]])), [sp.I, -sp.I], "q25 A")
    same(ev(M([[0, 1], [1, 0]])), [1, -1], "q25 B")
    same(ev(M([[1, 1], [1, 1]])), [0, 2], "q25 C")
    same(ev(J), [1, 1], "q25 D")
    # q26 AR 0
    A26 = M([[1, 2], [2, -2]]); assert A26 == A26.T
    same(ev(A26), [2, -3], "q26")
    # q27 AR 1
    eq(sum(ev(A21)), 5, "q27 A"); eq(sp.prod(ev(A21)), A21.det(), "q27 R")
    # q28 AR 2
    assert not J.is_diagonalizable(), "q28 A"
    assert I2.is_diagonalizable() and len(I2.eigenvals()) == 1, "q28 R is false"
    # q29 AR 3
    assert J - I2 != sp.zeros(2) and (J - I2)**2 == sp.zeros(2), "q29 A false"
    assert sp.rem(cp(J), (lam - 1)**2, lam) == 0 and sp.rem(cp(A20), (lam - 2)**2, lam) == 0, "q29 R"
    # q30 AR 0: companion matrix of lambda^3 - 2 lambda^2 + lambda - 5
    C = M([[0, 0, 5], [1, 0, -1], [0, 1, 2]])
    eq(cp(C), lam**3 - 2*lam**2 + lam - 5, "q30 cp")
    assert C**3 - 2*C**2 + C == 5*I3, "q30"
    # notes examples
    N1 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    eq(cp(N1), (lam - 1)**2*(lam - 4), "notes cp"); eq(3 - (N1 - I3).rank(), 2, "notes gm")
    N2 = M([[5, 4], [1, 2]]); m = sp.symbols("m")
    P = M([[4, 1], [1, -1]])
    assert P.inv()*N2*P == sp.diag(6, 1)
    for k in range(1, 5):
        assert N2**k == M([[4*6**k + 1, 4*6**k - 4], [6**k - 1, 6**k + 4]])/5
    N3 = M([[1, 1], [-2, 4]])
    for k in range(1, 6):
        assert N3**k == (3**k - 2**k)*N3 + (3*2**k - 2*3**k)*I2
    N4 = M([[2, 1], [1, 3]])
    assert N4**2 - 5*N4 + 5*I2 == sp.zeros(2) and N4.inv() == (5*I2 - N4)/5
    assert N4**3 == 20*N4 - 25*I2


T.write(check)
