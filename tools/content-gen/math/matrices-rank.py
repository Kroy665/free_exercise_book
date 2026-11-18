import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.matrices-rank")

# ---------------------------------------------------------------- easy singles
T.single(1, ["matrix-algebra", "exam-tips"],
    r"If $A$ is a $3\times 2$ matrix and $B$ is a $2\times 3$ matrix, then the order of $AB$ is",
    [r"$3\times 3$", r"$2\times 2$", r"$3\times 2$", r"$AB$ is not defined"],
    r"""$(m\times n)(n\times p)$ is $m\times p$. Here $(3\times 2)(2\times 3)$ has matching inner size $2$, so
$$AB \text{ is } 3\times 3.$$
$2\times 2$ is the order of $BA$, not $AB$.""")

T.single(1, ["adjoint-inverse"],
    r"The inverse of $A = \begin{pmatrix}2 & 3\\ 1 & 2\end{pmatrix}$ is",
    [r"$\begin{pmatrix}2 & -3\\ -1 & 2\end{pmatrix}$",
     r"$\begin{pmatrix}2 & -1\\ -3 & 2\end{pmatrix}$",
     r"$\begin{pmatrix}-2 & 3\\ 1 & -2\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 3\\ 1 & 2\end{pmatrix}$"],
    r"""$\det A = 4 - 3 = 1$. For a $2\times 2$ matrix, swap the diagonal and negate the off-diagonal:
$$A^{-1} = \frac{1}{1}\begin{pmatrix}2 & -3\\ -1 & 2\end{pmatrix}.$$
Check: $A A^{-1} = \begin{pmatrix}4 - 3 & -6 + 6\\ 2 - 2 & -3 + 4\end{pmatrix} = I$. The option with $-1$ and $-3$ swapped is the transpose of the adjoint (the cofactor matrix), a common slip.""")

T.single(1, ["transpose-symmetric", "exam-tips"],
    r"For matrices $A$ ($m\times n$) and $B$ ($n\times p$), $(AB)^T$ equals",
    [r"$B^TA^T$", r"$A^TB^T$", r"$AB$", r"$BA$"],
    r"""The reversal law: $\big((AB)^T\big)_{ij} = (AB)_{ji} = \sum_k a_{jk}b_{ki} = \sum_k (B^T)_{ik}(A^T)_{kj}$, so
$$(AB)^T = B^TA^T.$$
$A^TB^T$ is not even defined here unless $p = m$ (it would be $(n\times m)(p\times n)$).""")

T.single(1, ["transpose-symmetric"],
    r"If $A = \begin{pmatrix}2 & 3 + i\\ x & 5\end{pmatrix}$ is Hermitian, then $x$ equals",
    [r"$3 - i$", r"$3 + i$", r"$-3 + i$", r"$-3 - i$"],
    r"""Hermitian means $A^* = A$, that is, $a_{21} = \overline{a_{12}}$. So
$$x = \overline{3 + i} = 3 - i.$$
$x = 3 + i$ would make $A$ symmetric, not Hermitian; $-3 + i$ is the skew-Hermitian condition $a_{21} = -\overline{a_{12}}$.""")

T.single(1, ["rank-properties", "rank"],
    r"The rank of $\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 3 & 6 & 9\end{pmatrix}$ is",
    [r"$1$", r"$2$", r"$3$", r"$0$"],
    r"""Rows 2 and 3 are $2\times$ and $3\times$ row 1. After $R_2 - 2R_1$ and $R_3 - 3R_1$ only one non-zero row remains:
$$\rho = 1.$$
The rank is not $0$ because the matrix is non-zero (any entry is a non-zero $1\times1$ minor). It is not $2$: every $2\times 2$ minor is $0$.""")

T.single(1, ["adjoint-inverse", "exam-tips"],
    r"If $A = \begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 0 & 0 & 2\end{pmatrix}$, then $A\,(\operatorname{adj}A)$ equals",
    [r"$2I$", r"$4I$", r"$I$", r"$8I$"],
    r"""Always $A\,(\operatorname{adj}A) = (\det A)\,I$. $A$ is upper triangular, so
$$\det A = 1\cdot 1\cdot 2 = 2, \qquad A\,(\operatorname{adj}A) = 2I.$$
$4I$ and $8I$ come from mixing this up with $\det(\operatorname{adj}A) = \lvert A\rvert^{2} = 4$ or with $\lvert A\rvert^3$.""")

# ---------------------------------------------------------------- medium singles
T.single(2, ["transpose-symmetric"],
    r"$A = \begin{pmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{pmatrix}$ is written as $P + Q$ with $P$ symmetric and $Q$ skew-symmetric. The $(1,3)$ entry of $Q$ is",
    [r"$-2$", r"$2$", r"$5$", r"$-4$"],
    r"""$Q = \frac12(A - A^T)$, so
$$q_{13} = \frac{a_{13} - a_{31}}{2} = \frac{3 - 7}{2} = -2.$$
$5$ is $p_{13} = \frac{3 + 7}{2}$ (the symmetric part); $-4$ forgets the factor $\frac12$; $2$ is $q_{31}$.""")

T.single(2, ["adjoint-inverse", "exam-tips"],
    r"$A$ is a $3\times 3$ matrix with $\det A = 5$. Then $\det(\operatorname{adj}A)$ is",
    [r"$25$", r"$125$", r"$5$", r"$\dfrac15$"],
    r"""Take determinants in $A\,\operatorname{adj}A = (\det A)I_3$: $\det A\cdot\det(\operatorname{adj}A) = (\det A)^3$. So
$$\det(\operatorname{adj}A) = (\det A)^{n-1} = 5^2 = 25.$$
$125 = 5^3$ uses the exponent $n$ instead of $n - 1$; $\frac15$ is $\det(A^{-1})$.""")

T.single(2, ["adjoint-inverse"],
    r"If $A$ is a $3\times 3$ matrix with $\det A = 4$, then $\operatorname{adj}(\operatorname{adj}A)$ equals",
    [r"$4A$", r"$16A$", r"$A$", r"$64A$"],
    r"""For order $n$, $\operatorname{adj}(\operatorname{adj}A) = (\det A)^{n-2}A$. With $n = 3$:
$$\operatorname{adj}(\operatorname{adj}A) = 4^{1}A = 4A.$$
$16A$ uses $(\det A)^{n-1}$, which is the formula for $\det(\operatorname{adj}A)$. The answer $A$ is correct only for $n = 2$.""")

T.single(2, ["rank"],
    r"The rank of $\begin{pmatrix}1 & 2 & -1 & 3\\ 2 & 4 & 1 & -2\\ 3 & 6 & 3 & -7\end{pmatrix}$ is",
    [r"$2$", r"$3$", r"$1$", r"$4$"],
    r"""Sweep out the first column:
$$\xrightarrow[R_3 - 3R_1]{R_2 - 2R_1}\begin{pmatrix}1 & 2 & -1 & 3\\ 0 & 0 & 3 & -8\\ 0 & 0 & 6 & -16\end{pmatrix}\xrightarrow{R_3 - 2R_2}\begin{pmatrix}1 & 2 & -1 & 3\\ 0 & 0 & 3 & -8\\ 0 & 0 & 0 & 0\end{pmatrix}.$$
Two non-zero rows, so $\rho = 2$. The rank of a $3\times 4$ matrix is at most $3$, so $4$ is impossible; $3$ misses the dependence $R_3 = 2R_2 - R_1$.""")

T.single(2, ["rank"],
    r"The matrix $\begin{pmatrix}1 & 1 & 1\\ 1 & 2 & 3\\ 2 & 3 & k\end{pmatrix}$ has rank $2$ when $k$ equals",
    [r"$4$", r"$3$", r"$5$", r"$-4$"],
    r"""The first two rows are independent, so the rank is at least $2$. It is exactly $2$ iff the determinant is $0$:
$$\det = 1(2k - 9) - 1(k - 6) + 1(3 - 4) = k - 4 = 0 \iff k = 4.$$
Check: for $k = 4$, $R_3 = R_1 + R_2$. For every other $k$ the rank is $3$.""")

T.single(2, ["elementary-operations"],
    r"The inverse of the elementary matrix $E = \begin{pmatrix}1 & 0 & 2\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$ is",
    [r"$\begin{pmatrix}1 & 0 & -2\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\\ 2 & 0 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0 & \frac12\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\\ -2 & 0 & 1\end{pmatrix}$"],
    r"""$E$ comes from $I_3$ by $R_1 \to R_1 + 2R_3$. The inverse operation is $R_1 \to R_1 - 2R_3$, so
$$E^{-1} = \begin{pmatrix}1 & 0 & -2\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}.$$
Check: $EE^{-1}$ has $(1,3)$ entry $-2 + 2 = 0$. The transpose $E^T$ is not the inverse (that holds only for orthogonal matrices), and $\frac12$ is the rule for the scaling type, not the adding type.""")

T.single(2, ["adjoint-inverse", "exam-tips"],
    r"If $A^{-1} = \begin{pmatrix}1 & 2\\ 0 & 1\end{pmatrix}$ and $B^{-1} = \begin{pmatrix}1 & 0\\ 3 & 1\end{pmatrix}$, then $(AB)^{-1}$ is",
    [r"$\begin{pmatrix}1 & 2\\ 3 & 7\end{pmatrix}$",
     r"$\begin{pmatrix}7 & 2\\ 3 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 2\\ 3 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 2\\ 3 & 2\end{pmatrix}$"],
    r"""By the reversal law $(AB)^{-1} = B^{-1}A^{-1}$:
$$\begin{pmatrix}1 & 0\\ 3 & 1\end{pmatrix}\begin{pmatrix}1 & 2\\ 0 & 1\end{pmatrix} = \begin{pmatrix}1 & 2\\ 3 & 7\end{pmatrix}.$$
$\begin{pmatrix}7 & 2\\ 3 & 1\end{pmatrix}$ is $A^{-1}B^{-1}$, the wrong order. Quick check: $\det = 7 - 6 = 1 = \det A^{-1}\det B^{-1}$.""")

T.single(2, ["normal-form", "rank"],
    r"The matrix $\begin{pmatrix}1 & 2 & 3 & 4\\ 2 & 4 & 6 & 8\\ 1 & 0 & 1 & 0\end{pmatrix}$ is equivalent to",
    [r"$\begin{bmatrix}I_2 & O\\ O & O\end{bmatrix}_{3\times 4}$",
     r"$\begin{bmatrix}I_3 & O\end{bmatrix}_{3\times 4}$",
     r"$\begin{bmatrix}I_1 & O\\ O & O\end{bmatrix}_{3\times 4}$",
     r"$I_3$"],
    r"""Equivalent matrices have the same order and the same rank. Here $R_2 = 2R_1$, and rows 1 and 3 are not proportional, so
$$\rho = 2,$$
and the normal form is $\begin{bmatrix}I_2 & O\\ O & O\end{bmatrix}$ of order $3\times 4$. $I_3$ has the wrong order, and $[I_3\ O]$ needs rank $3$.""")

T.single(2, ["normal-form"],
    r"$A = \dfrac13\begin{pmatrix}1 & 2 & 2\\ 2 & 1 & -2\\ x & 2 & -1\end{pmatrix}$ is orthogonal. Then $x$ equals",
    [r"$-2$", r"$2$", r"$1$", r"$-1$"],
    r"""The rows of an orthogonal matrix are orthonormal. Row 3 must be orthogonal to row 1:
$$x + 4 - 2 = 0 \implies x = -2.$$
Check with row 2: $2(-2) + 2 + 2 = 0$, and the length of row 3 is $\frac13\sqrt{4 + 4 + 1} = 1$. $x = 2$ makes the length right but breaks orthogonality.""")

T.single(2, ["adjoint-inverse"],
    r"A square matrix $A$ satisfies $A^2 - A + I = O$. Then $A^{-1}$",
    [r"exists and equals $I - A$", r"exists and equals $A - I$", r"exists and equals $A + I$", r"does not exist"],
    r"""Rewrite: $A - A^2 = I$, that is,
$$A(I - A) = (I - A)A = I.$$
So $A$ is invertible and $A^{-1} = I - A$. The sign slip gives $A - I$, which is $-A^{-1}$.""")

# ---------------------------------------------------------------- hard singles
T.single(3, ["rank-properties"],
    r"$A$ is a $4\times 4$ matrix of rank $3$. The rank of $\operatorname{adj}A$ is",
    [r"$1$", r"$3$", r"$0$", r"$4$"],
    r"""For order $n$: $\rho(\operatorname{adj}A) = n, 1, 0$ according as $\rho(A) = n$, $n - 1$, or $\le n - 2$.

Here $\rho(A) = 3 = n - 1$. Some $3\times 3$ minor is non-zero, so $\operatorname{adj}A \ne O$. Also $A\operatorname{adj}A = (\det A)I = O$, which forces $\rho(\operatorname{adj}A) \le n - \rho(A) = 1$. Hence
$$\rho(\operatorname{adj}A) = 1.$$
$0$ is the answer only when $\rho(A) \le 2$.""")

T.single(3, ["rank-properties", "exam-tips"],
    r"If $A$ is a $3\times 2$ real matrix and $B$ is a $2\times 3$ real matrix, then $\det(AB)$",
    [r"is always $0$", r"equals $\det A\cdot\det B$", r"is always $1$", r"can be any real number"],
    r"""$AB$ is $3\times 3$, but
$$\rho(AB) \le \min\{\rho(A), \rho(B)\} \le 2 < 3,$$
so $AB$ is singular and $\det(AB) = 0$ always. $\det A$ and $\det B$ are not defined (the matrices are not square). By contrast, $BA$ is $2\times 2$ and can be non-singular.""")

T.single(3, ["rank"],
    r"The rank of $\begin{pmatrix}k & 1 & 1\\ 1 & k & 1\\ 1 & 1 & k\end{pmatrix}$ is exactly $2$ when $k$ equals",
    [r"$-2$", r"$1$", r"$2$", r"$-1$"],
    r"""Adding all rows to the first gives the factor $k + 2$, and
$$\det = (k + 2)(k - 1)^2.$$
The rank is $3$ unless $k = 1$ or $k = -2$.

- $k = 1$: all rows equal $(1,1,1)$, so the rank is $1$, not $2$.
- $k = -2$: the minor $\begin{vmatrix}-2 & 1\\ 1 & -2\end{vmatrix} = 3 \ne 0$, so the rank is $2$.""")

T.single(3, ["adjoint-inverse"],
    r"For $A = \begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}$, the $(1,2)$ entry of $A^{-1}$ is",
    [r"$18$", r"$20$", r"$-18$", r"$-20$"],
    r"""$\det A = 1(0 - 24) - 2(0 - 20) + 3(0 - 5) = 1$, so $A^{-1} = \operatorname{adj}A$.

The $(1,2)$ entry of $\operatorname{adj}A$ is the cofactor $C_{21}$ (transpose!):
$$C_{21} = -\begin{vmatrix}2 & 3\\ 6 & 0\end{vmatrix} = -(0 - 18) = 18.$$
$20$ is $C_{12}$, the answer you get if you forget to transpose; $-18$ forgets the sign $(-1)^{2+1}$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["rank-properties"],
    r"Consider the following statements about real matrices $A$ and $B$ for which the operations are defined:",
    [r"$\rho(A^T) = \rho(A)$",
     r"$\rho(AB) \le \min\{\rho(A), \rho(B)\}$",
     r"$\rho(A + B) = \rho(A) + \rho(B)$"],
    [r"1 and 2 only", r"1, 2 and 3", r"2 only", r"1 and 3 only"],
    r"""Statement 1 holds: the minors of $A^T$ are exactly the minors of $A$.

Statement 2 holds: the rows of $AB$ are combinations of the rows of $B$, and its columns are combinations of the columns of $A$.

Statement 3 fails. Only $\rho(A + B) \le \rho(A) + \rho(B)$ is true. With $A = I_2$, $B = -I_2$:
$$\rho(A + B) = \rho(O) = 0 \ne 2 + 2.$$""")

T.statements(3, ["matrix-algebra", "adjoint-inverse"],
    r"Consider the following statements about square matrices $A, B, C$ of order $n \ge 2$:",
    [r"If $AB = O$, then $A = O$ or $B = O$.",
     r"If $A$ is non-singular and $AB = AC$, then $B = C$.",
     r"$(A + B)^2 = A^2 + 2AB + B^2$."],
    [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""Statement 1 is false (zero divisors): $A = \begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$, $B = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix}$ give $AB = O$.

Statement 2 is true: multiply on the left by $A^{-1}$.

Statement 3 is false in general: $(A + B)^2 = A^2 + AB + BA + B^2$, and $AB \ne BA$. With the same $A, B$: $AB = O$ but $BA \ne O$, so the two sides differ by $BA - AB = BA \ne O$.""")

T.statements(3, ["normal-form"],
    r"Let $B = P^TAP$, where $A$ is a real $n\times n$ matrix and $P$ is a real non-singular $n\times n$ matrix. Consider:",
    [r"$\rho(B) = \rho(A)$.",
     r"$\det B = \det A$.",
     r"If $A$ is symmetric, then $B$ is symmetric."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""$B$ is **congruent** to $A$.

1. True: multiplying by non-singular $P^T$ and $P$ does not change rank.
2. False: $\det B = (\det P)^2\det A$. With $A = I_2$ and $P = 2I_2$, $\det B = 16 \ne 1$.
3. True: $B^T = P^TA^TP = P^TAP = B$.

So congruence preserves rank and symmetry, but not the determinant (over $\R$, only its sign).""")

# ---------------------------------------------------------------- match
T.match(2, ["adjoint-inverse", "exam-tips"],
    r"$A$ is a $3\times 3$ matrix with $\det A = 2$. Match each quantity in List I with its value in List II.",
    [r"$\det(A^T)$", r"$\det(\operatorname{adj}A)$", r"$\det(2A)$", r"$\det(A^{-1})$"],
    [r"$\frac12$", r"$2$", r"$4$", r"$16$"],
    [r"A-2, B-3, C-4, D-1", r"A-2, B-4, C-3, D-1", r"A-1, B-3, C-4, D-2", r"A-2, B-3, C-1, D-4"],
    r"""- $\det A^T = \det A = 2$.
- $\det(\operatorname{adj}A) = (\det A)^{n-1} = 2^2 = 4$.
- $\det(2A) = 2^3\det A = 16$ (each of the 3 rows is doubled, not just one).
- $\det(A^{-1}) = \frac{1}{\det A} = \frac12$.

So A-2, B-3, C-4, D-1. The trap is $\det(2A) = 4$, which treats $2A$ as if one row were scaled.""")

T.match(3, ["transpose-symmetric", "matrix-algebra", "normal-form"],
    r"Match each matrix in List I with the property in List II that it has.",
    [r"$\begin{pmatrix}2 & 1 + i\\ 1 - i & 3\end{pmatrix}$",
     r"$\begin{pmatrix}0 & 2\\ -2 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}\frac35 & -\frac45\\ \frac45 & \frac35\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 1\\ 0 & 0\end{pmatrix}$"],
    [r"idempotent", r"orthogonal", r"Hermitian", r"skew-symmetric"],
    [r"A-3, B-4, C-2, D-1", r"A-4, B-3, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-3, B-4, C-1, D-2"],
    r"""- A: $a_{21} = 1 - i = \overline{a_{12}}$ and the diagonal is real, so $A^* = A$: **Hermitian** (3).
- B: $B^T = -B$: **skew-symmetric** (4). It is not orthogonal, since $BB^T = 4I$.
- C: the columns are orthonormal ($\frac{9}{25} + \frac{16}{25} = 1$, and $-\frac{12}{25} + \frac{12}{25} = 0$): **orthogonal** (2), a rotation.
- D: $D^2 = \begin{pmatrix}1 & 1\\ 0 & 0\end{pmatrix} = D$: **idempotent** (1).

So A-3, B-4, C-2, D-1. Each matrix has only its own property from List II.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["adjoint-inverse"],
    r"The matrix $\begin{pmatrix}1 & 2\\ 2 & 4\end{pmatrix}$ has no inverse.",
    r"A square matrix $A$ is invertible if and only if $\det A \ne 0$.",
    0,
    r"""$\det\begin{pmatrix}1 & 2\\ 2 & 4\end{pmatrix} = 4 - 4 = 0$, so by R the matrix is not invertible. Both are true and R is exactly the reason for A.

(R holds because $A\,\operatorname{adj}A = (\det A)I$ gives the inverse when $\det A \ne 0$, and $\det A\det A^{-1} = 1$ rules out an inverse when $\det A = 0$.)""")

T.assertion_reason(1, ["rank", "rank-properties"],
    r"The rank of $\begin{pmatrix}1 & 2\\ 3 & 6\end{pmatrix}$ is $1$.",
    r"For every matrix $A$, $\rho(A^T) = \rho(A)$.",
    1,
    r"""A is true: the second row is $3\times$ the first, so $\det = 0$, while the matrix is non-zero. Hence $\rho = 1$.

R is true: minors of $A^T$ are minors of $A$.

But R does not explain A. The rank in A comes from the vanishing determinant and the proportional rows, not from comparing with the transpose.""")

T.assertion_reason(2, ["matrix-algebra"],
    r"There exist non-zero $2\times 2$ real matrices $A$ and $B$ with $AB = O$.",
    r"For square matrices $A$ and $B$ of the same order, $AB = O$ implies $BA = O$.",
    2,
    r"""A is true: $A = \begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$, $B = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix}$ give $AB = O$.

R is false for the same pair:
$$BA = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix} \ne O.$$
Matrix multiplication is not commutative, so nothing about $BA$ follows from $AB$.""")

T.assertion_reason(2, ["transpose-symmetric"],
    r"Every real skew-symmetric matrix of order $3$ is non-singular.",
    r"Every diagonal entry of a real skew-symmetric matrix is $0$.",
    3,
    r"""A is false. For skew-symmetric $A$ of odd order $n$,
$$\det A = \det(A^T) = \det(-A) = (-1)^n\det A = -\det A,$$
so $\det A = 0$: every such matrix is **singular**.

R is true: $a_{ii} = -a_{ii}$ gives $a_{ii} = 0$.""")

T.assertion_reason(3, ["normal-form"],
    r"Any two $3\times 4$ real matrices of rank $2$ are equivalent.",
    r"Every $m\times n$ matrix of rank $r \ge 1$ can be reduced by elementary row and column operations to the normal form $\begin{bmatrix}I_r & O\\ O & O\end{bmatrix}$.",
    0,
    r"""R is the normal-form theorem: there are non-singular $P, Q$ with $PAQ = N_r$.

A follows from R: if $P_1AQ_1 = N_2 = P_2BQ_2$, then
$$B = (P_2^{-1}P_1)\,A\,(Q_1Q_2^{-1}),$$
so $B$ is equivalent to $A$. Both are true and R explains A.""")


def check():
    import sympy as sp
    M = sp.Matrix
    I2, I3 = sp.eye(2), sp.eye(3)

    # q1: order of AB
    A = sp.ones(3, 2); B = sp.ones(2, 3)
    eq((A * B).shape[0] * 10 + (A * B).shape[1], 33, "q1")

    # q2: inverse 2x2
    A = M([[2, 3], [1, 2]])
    assert A.inv() == M([[2, -3], [-1, 2]]), "q2"
    assert A.inv() != M([[2, -1], [-3, 2]]), "q2 distractor"

    # q3: (AB)^T = B^T A^T on random non-square matrices
    A = M(2, 3, [1, 2, 3, 4, 5, 6]); B = M(3, 4, list(range(1, 13)))
    assert (A * B).T == B.T * A.T, "q3"

    # q4: Hermitian
    x = 3 - sp.I
    H = M([[2, 3 + sp.I], [x, 5]])
    assert H.H == H, "q4"
    assert M([[2, 3 + sp.I], [3 + sp.I, 5]]).H != M([[2, 3 + sp.I], [3 + sp.I, 5]]), "q4 distractor"

    # q5: rank 1
    eq(M([[1, 2, 3], [2, 4, 6], [3, 6, 9]]).rank(), 1, "q5")

    # q6: A adj A
    A = M([[1, 2, 3], [0, 1, 4], [0, 0, 2]])
    assert A * A.adjugate() == 2 * I3, "q6"

    # q7: skew part (1,3)
    A = M([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Q = (A - A.T) / 2; P = (A + A.T) / 2
    eq(Q[0, 2], -2, "q7"); eq(P[0, 2], 5, "q7 sym part")
    assert Q.T == -Q and P.T == P and P + Q == A

    # q8, q9: adjoint determinants
    a = sp.symbols("a:9")
    A = M(3, 3, a)
    eq(A.adjugate().det() - A.det() ** 2, 0, "q8 identity")
    eq(5 ** 2, 25, "q8")
    assert (A.adjugate().adjugate() - A.det() * A).applyfunc(sp.expand) == sp.zeros(3, 3), "q9"
    A4 = M([[2, 1, 0], [0, 1, 0], [1, 0, 2]])  # det 4
    eq(A4.det(), 4, "q9 sample det")
    assert A4.adjugate().adjugate() == 4 * A4, "q9 numeric"

    # q10: rank of 3x4
    eq(M([[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]]).rank(), 2, "q10")

    # q11: k for rank 2
    k = sp.symbols("k")
    Ak = M([[1, 1, 1], [1, 2, 3], [2, 3, k]])
    assert sp.solve(Ak.det(), k) == [4], "q11"
    eq(Ak.subs(k, 4).rank(), 2, "q11 rank")
    for kk in (3, 5, -4):
        eq(Ak.subs(k, kk).rank(), 3, "q11 distractor")

    # q12: inverse of elementary matrix
    E = M([[1, 0, 2], [0, 1, 0], [0, 0, 1]])
    assert E.inv() == M([[1, 0, -2], [0, 1, 0], [0, 0, 1]]), "q12"
    assert E.T != E.inv()

    # q13: (AB)^{-1}
    Ai = M([[1, 2], [0, 1]]); Bi = M([[1, 0], [3, 1]])
    A = Ai.inv(); B = Bi.inv()
    assert (A * B).inv() == M([[1, 2], [3, 7]]), "q13"
    assert Ai * Bi == M([[7, 2], [3, 1]]), "q13 distractor"

    # q14: normal form, rank 2
    eq(M([[1, 2, 3, 4], [2, 4, 6, 8], [1, 0, 1, 0]]).rank(), 2, "q14")

    # q15: orthogonal x
    x = sp.symbols("x")
    A = M([[1, 2, 2], [2, 1, -2], [x, 2, -1]]) / 3
    G = (A * A.T - I3)
    sol = sp.solve(list(G), x, dict=True)
    assert sol == [{x: -2}], f"q15 {sol}"
    for xx in (2, 1, -1):
        assert (A * A.T).subs(x, xx) != I3

    # q16: A^2 - A + I = 0 => A^{-1} = I - A ; use a concrete A
    A = M([[0, -1], [1, 1]])  # char poly t^2 - t + 1
    assert A ** 2 - A + I2 == sp.zeros(2, 2)
    assert A.inv() == I2 - A, "q16"

    # q17: rank of adj, 4x4 rank 3 -> 1 ; rank 2 -> 0
    A = sp.diag(1, 2, 3, 0)
    eq(A.rank(), 3, "q17a"); eq(A.adjugate().rank(), 1, "q17")
    A = M([[1, 2, 0, 1], [0, 1, 1, 0], [1, 3, 1, 1], [2, 1, 0, 3]])
    eq(A.rank(), 3, "q17 b"); eq(A.adjugate().rank(), 1, "q17 b")
    eq(sp.diag(1, 2, 0, 0).adjugate().rank(), 0, "q17 rank2")

    # q18: det(AB) = 0 for 3x2 * 2x3 (symbolic)
    p = sp.symbols("p:6"); q = sp.symbols("q:6")
    A = M(3, 2, p); B = M(2, 3, q)
    eq(sp.expand((A * B).det()), 0, "q18")
    assert (B * A).subs({**{p[i]: [1, 0, 0, 1, 0, 0][i] for i in range(6)},
                         **{q[i]: [1, 0, 0, 0, 1, 0][i] for i in range(6)}}).det() != 0

    # q19: rank 2 iff k = -2
    Ak = M([[k, 1, 1], [1, k, 1], [1, 1, k]])
    eq(sp.factor(Ak.det()) - (k + 2) * (k - 1) ** 2, 0, "q19 det")
    eq(Ak.subs(k, -2).rank(), 2, "q19")
    eq(Ak.subs(k, 1).rank(), 1, "q19 k=1")
    eq(Ak.subs(k, 2).rank(), 3); eq(Ak.subs(k, -1).rank(), 3)

    # q20: (1,2) entry of inverse
    A = M([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    eq(A.det(), 1)
    eq(A.inv()[0, 1], 18, "q20")
    eq(A.cofactor(0, 1), 20, "q20 distractor C12")
    assert A.inv() == M([[-24, 18, 5], [20, -15, -4], [-5, 4, 1]])

    # q21 statements: rank properties
    a = sp.symbols("a:6")
    for Am, Bm in [(M([[1, 2], [2, 4], [0, 1]]), M([[1, 0, 1], [0, 0, 0]])),
                   (M([[1, 1], [1, 1]]), M([[1, -1], [-1, 1]]))]:
        assert Am.T.rank() == Am.rank()
        assert (Am * Bm).rank() <= min(Am.rank(), Bm.rank())
    assert (I2 + (-I2)).rank() != I2.rank() + (-I2).rank(), "q21 s3 false"

    # q22 statements: zero divisors
    A = M([[1, 0], [0, 0]]); B = M([[0, 0], [1, 0]])
    assert A * B == sp.zeros(2, 2) and A != sp.zeros(2, 2) and B != sp.zeros(2, 2), "q22 s1 false"
    assert (A + B) ** 2 != A ** 2 + 2 * A * B + B ** 2, "q22 s3 false"

    # q23 statements: congruence
    P = M([[1, 2, 0], [0, 1, 3], [1, 0, 1]]); assert P.det() != 0
    S = M([[1, 2, 3], [2, 0, 1], [3, 1, 1]]); C = P.T * S * P
    assert C.T == C and C.rank() == S.rank(), "q23 s1 s3"
    assert (2 * I2).T * I2 * (2 * I2) != I2 and ((2 * I2).T * I2 * (2 * I2)).det() == 16, "q23 s2 false"
    Sing = M([[1, 2, 3], [2, 4, 6], [1, 0, 1]])
    eq((P.T * Sing * P).rank(), Sing.rank())

    # q24 match: det A = 2, n = 3
    A = M([[2, 0, 0], [0, 1, 0], [0, 0, 1]])
    vals = [A.T.det(), A.adjugate().det(), (2 * A).det(), A.inv().det()]
    right = [sp.Rational(1, 2), 2, 4, 16]
    assert [right.index(v) + 1 for v in vals] == [2, 3, 4, 1], "q24"

    # q25 match: each matrix has exactly its own property
    mats = [M([[2, 1 + sp.I], [1 - sp.I, 3]]), M([[0, 2], [-2, 0]]),
            M([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]]),
            M([[1, 1], [0, 0]])]
    props = [lambda X: X ** 2 == X,               # 1 idempotent
             lambda X: X * X.T == I2,             # 2 orthogonal
             lambda X: X.H == X,                  # 3 Hermitian
             lambda X: X.T == -X]                 # 4 skew-symmetric
    table = [[j + 1 for j, f in enumerate(props) if f(X)] for X in mats]
    assert table == [[3], [4], [2], [1]], f"q25 {table}"

    # q26 AR: det 0 -> no inverse
    eq(M([[1, 2], [2, 4]]).det(), 0, "q26")

    # q27 AR: rank 1
    eq(M([[1, 2], [3, 6]]).rank(), 1, "q27")

    # q28 AR: AB = O but BA != O
    A = M([[1, 0], [0, 0]]); B = M([[0, 0], [1, 0]])
    assert A * B == sp.zeros(2, 2) and B * A != sp.zeros(2, 2), "q28"

    # q29 AR: skew-symmetric order 3 is singular
    b = sp.symbols("b:3")
    K = M([[0, b[0], b[1]], [-b[0], 0, b[2]], [-b[1], -b[2], 0]])
    eq(sp.expand(K.det()), 0, "q29")

    # q30 AR: two 3x4 rank-2 matrices are equivalent (both reduce to N_2)
    X = M([[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]])
    Y = M([[1, 2, 3, 4], [2, 4, 6, 8], [1, 0, 1, 0]])
    eq(X.rank(), 2); eq(Y.rank(), 2)


T.write(check)
