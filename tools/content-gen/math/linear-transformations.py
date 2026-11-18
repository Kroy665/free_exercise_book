import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.linear-transformations")

# ---------------------------------------------------------------- easy singles
T.single(1, ["definition"],
    r"Which of the following maps $T : \R^2 \to \R^2$ is linear?",
    [r"$T(x, y) = (x + y,\ x - y)$",
     r"$T(x, y) = (x + 1,\ y)$",
     r"$T(x, y) = (x^2,\ y)$",
     r"$T(x, y) = (xy,\ x)$"],
    r"""Each coordinate of $(x + y,\ x - y)$ is a linear form in $x, y$ with no constant term, so
$$T(\alpha u + \beta v) = \alpha T(u) + \beta T(v).$$
The others fail:
- $(x + 1, y)$ is a translation: $T(0, 0) = (1, 0) \ne 0$.
- $(x^2, y)$: $T(2, 0) = (4, 0) \ne 2T(1, 0) = (2, 0)$.
- $(xy, x)$: $T(1,1) + T(1,1) = (2, 2)$ but $T(2, 2) = (4, 2)$. It fixes $0$, yet is not linear.""")

T.single(1, ["rank-nullity"],
    r"$T : \R^5 \to \R^3$ is a linear map from $\R^5$ onto $\R^3$. The nullity of $T$ is",
    [r"$2$", r"$3$", r"$5$", r"$0$"],
    r"""Onto means $\rho(T) = \dim \R^3 = 3$. By rank–nullity (the sum is the dimension of the **domain**):
$$\nu(T) = 5 - 3 = 2.$$
$3$ confuses nullity with rank; $0$ would make $T$ one-one, impossible since $5 > 3$.""")

T.single(1, ["rank-nullity", "injective-surjective"],
    r"Which of the following is true for **every** linear map $T : \R^3 \to \R^2$?",
    [r"$T$ is not one-one",
     r"$T$ is not onto",
     r"$T$ is onto",
     r"$T$ is one-one"],
    r"""$\rho(T) \le 2$, so
$$\nu(T) = 3 - \rho(T) \ge 1,$$
and a non-zero kernel means $T$ is not one-one.

Onto-ness depends on $T$: the projection $(x, y, z) \mapsto (x, y)$ is onto, the zero map is not. So neither "onto" nor "not onto" holds for every $T$.""")

T.single(1, ["matrix-representation"],
    r"The matrix of $T(x, y) = (2x + 3y,\ x - y)$ relative to the standard basis of $\R^2$ (columns = coordinates of $T(e_1), T(e_2)$) is",
    [r"$\begin{pmatrix}2 & 3\\ 1 & -1\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 1\\ 3 & -1\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 3\\ -1 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}3 & 2\\ -1 & 1\end{pmatrix}$"],
    r"""$T(e_1) = T(1, 0) = (2, 1)$ and $T(e_2) = T(0, 1) = (3, -1)$. Writing them as columns:
$$[T] = \begin{pmatrix}2 & 3\\ 1 & -1\end{pmatrix},$$
which is just the coefficient matrix read row by row. $\begin{pmatrix}2 & 1\\ 3 & -1\end{pmatrix}$ is the transpose (images written as rows).""")

T.single(1, ["definition"],
    r"$T : \R^2 \to \R^2$ is linear with $T(1, 0) = (1, 2)$ and $T(0, 1) = (3, 4)$. Then $T(2, -1)$ is",
    [r"$(-1, 0)$", r"$(5, 8)$", r"$(0, 2)$", r"$(2, -1)$"],
    r"""$(2, -1) = 2e_1 - e_2$, so by linearity
$$T(2, -1) = 2(1, 2) - (3, 4) = (-1, 0).$$
$(5, 8)$ drops the minus sign; $(0, 2)$ uses the transposed matrix $\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}$.""")

T.single(1, ["definition"],
    r"Which of the following is **not** a linear map?",
    [r"$A \mapsto \det A$ on $M_2(\R)$",
     r"$A \mapsto \operatorname{tr}A$ on $M_2(\R)$",
     r"$p \mapsto p'$ on the space of real polynomials",
     r"$f \mapsto \int_0^1 f(t)\,dt$ on $C[0, 1]$"],
    r"""The determinant is not additive or homogeneous: for $2\times 2$ matrices
$$\det(2A) = 4\det A \ne 2\det A \quad (\det A \ne 0),$$
and $\det I + \det I = 2 \ne 4 = \det(2I)$. Trace, differentiation and the definite integral are all linear.""")

# ---------------------------------------------------------------- medium singles
T.single(2, ["injective-surjective"],
    r"The vector space $P_3$ of real polynomials of degree at most $3$ is isomorphic to",
    [r"$\R^4$", r"$\R^3$", r"$\R^5$", r"$\R^{16}$"],
    r"""$\{1, x, x^2, x^3\}$ is a basis, so $\dim P_3 = 4$. Finite-dimensional spaces over $\R$ are isomorphic iff their dimensions are equal, and the coordinate map
$$a_0 + a_1x + a_2x^2 + a_3x^3 \mapsto (a_0, a_1, a_2, a_3)$$
is an isomorphism onto $\R^4$. $\R^3$ is the off-by-one slip (degree $3$, but $4$ coefficients).""")

T.single(2, ["rank-nullity", "kernel-range"],
    r"For $T : \R^4 \to \R^3$, $T(x, y, z, w) = (x + y + z + w,\ x + 2y + 3z + 4w,\ 2x + 3y + 4z + 5w)$, the dimension of $\ker T$ is",
    [r"$2$", r"$1$", r"$3$", r"$0$"],
    r"""The matrix has rows $R_1 = (1,1,1,1)$, $R_2 = (1,2,3,4)$, $R_3 = (2,3,4,5) = R_1 + R_2$. $R_1, R_2$ are independent, so $\rho(T) = 2$ and
$$\nu(T) = 4 - 2 = 2.$$
$1$ assumes the rank is $3$ (the maximum for a map into $\R^3$) without spotting $R_3 = R_1 + R_2$.""")

T.single(2, ["kernel-range"],
    r"For $T : \R^3 \to \R^3$, $T(x, y, z) = (x + 2y - z,\ y + z,\ x + y - 2z)$, the kernel of $T$ is",
    [r"$\operatorname{span}\{(3, -1, 1)\}$",
     r"$\operatorname{span}\{(-3, 1, 1)\}$",
     r"$\operatorname{span}\{(1, 0, 1), (2, 1, 1)\}$",
     r"$\{(0, 0, 0)\}$"],
    r"""Solve $T(x, y, z) = 0$. From the second equation $y = -z$; then the first gives $x = -2y + z = 3z$. The third equation, $3z - z - 2z = 0$, holds automatically (it is $R_1 - R_2$). So
$$\ker T = \{(3z, -z, z)\} = \operatorname{span}\{(3, -1, 1)\}.$$
$\{(1,0,1),(2,1,1)\}$ spans the **range** (two independent columns), not the kernel. $(-3, 1, 1)$ is a sign slip: $T(-3,1,1) = (-2, 2, -4) \ne 0$.""")

T.single(2, ["matrix-representation"],
    r"$D(p) = p'$ on $P_2$ (real polynomials of degree $\le 2$). Relative to the ordered basis $(1, x, x^2)$, with columns the coordinates of $D(1), D(x), D(x^2)$, the matrix of $D$ is",
    [r"$\begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 2\\ 0 & 0 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}0 & 0 & 0\\ 1 & 0 & 0\\ 0 & 2 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0 & 0\\ 0 & 2 & 0\\ 0 & 0 & 0\end{pmatrix}$"],
    r"""$D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, with coordinates $(0,0,0)$, $(1,0,0)$, $(0,2,0)$. As columns:
$$[D] = \begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 2\\ 0 & 0 & 0\end{pmatrix}.$$
The lower-triangular option is the transpose (coordinates written as rows); the option with a $1$ in place of $2$ forgets $(x^2)' = 2x$. Check: rank $2$, nullity $1$ (the constants).""")

T.single(2, ["change-of-basis", "matrix-representation"],
    r"$T(x, y) = (2x + y,\ x)$ on $\R^2$. Its matrix relative to the ordered basis $B' = ((1, 0), (1, 1))$ (columns = $B'$-coordinates of the images) is",
    [r"$\begin{pmatrix}1 & 2\\ 1 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 1\\ 2 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 1\\ 1 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}2 & 3\\ 1 & 1\end{pmatrix}$"],
    r"""Use $(a, b) = (a - b)(1, 0) + b(1, 1)$.
- $T(1, 0) = (2, 1) = 1\cdot(1,0) + 1\cdot(1,1)$: column $(1, 1)$.
- $T(1, 1) = (3, 1) = 2\cdot(1,0) + 1\cdot(1,1)$: column $(2, 1)$.
$$[T]_{B'} = \begin{pmatrix}1 & 2\\ 1 & 1\end{pmatrix} = P^{-1}AP,\quad A = \begin{pmatrix}2 & 1\\ 1 & 0\end{pmatrix},\ P = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}.$$
$\begin{pmatrix}2 & 3\\ 1 & 1\end{pmatrix}$ writes the images themselves instead of their coordinates; its trace $3$ differs from $\operatorname{tr}A = 2$, so it cannot be similar to $A$.""")

T.single(2, ["kernel-range", "rank-nullity"],
    r"$T : \R^3 \to \R^3$ is linear with $T(e_1) = e_1 - e_2$, $T(e_2) = e_2 - e_3$, $T(e_3) = e_3 - e_1$. The dimension of the range of $T$ is",
    [r"$2$", r"$3$", r"$1$", r"$0$"],
    r"""The range is spanned by the three images, and
$$(e_1 - e_2) + (e_2 - e_3) + (e_3 - e_1) = 0,$$
so they are dependent; any two of them are independent. Hence $\rho(T) = 2$ and $\nu(T) = 1$, with $\ker T = \operatorname{span}\{(1, 1, 1)\}$. $3$ assumes the images of a basis are always a basis, which holds only for invertible $T$.""")

T.single(2, ["matrix-representation"],
    r"$S(x, y) = (x + y,\ y)$ and $T(x, y) = (2x,\ x - y)$ on $\R^2$. The map $S \circ T$ is",
    [r"$(x, y) \mapsto (3x - y,\ x - y)$",
     r"$(x, y) \mapsto (2x + 2y,\ x)$",
     r"$(x, y) \mapsto (3x + y,\ x - y)$",
     r"$(x, y) \mapsto (2x + y,\ x - y)$"],
    r"""$S \circ T$ means "first $T$, then $S$":
$$S(T(x, y)) = S(2x,\ x - y) = (2x + x - y,\ x - y) = (3x - y,\ x - y).$$
In matrices, $[S][T] = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}\begin{pmatrix}2 & 0\\ 1 & -1\end{pmatrix} = \begin{pmatrix}3 & -1\\ 1 & -1\end{pmatrix}$. $(2x + 2y,\ x)$ is $T \circ S$, the wrong order.""")

T.single(2, ["injective-surjective"],
    r"$T(x, y) = (2x + y,\ 3x + 2y)$ on $\R^2$. Then $T^{-1}(x, y)$ is",
    [r"$(2x - y,\ -3x + 2y)$",
     r"$(2x - 3y,\ -x + 2y)$",
     r"$(-2x + y,\ 3x - 2y)$",
     r"$(2x + y,\ -3x - 2y)$"],
    r"""$A = \begin{pmatrix}2 & 1\\ 3 & 2\end{pmatrix}$, $\det A = 1 \ne 0$, so $T$ is invertible and
$$A^{-1} = \begin{pmatrix}2 & -1\\ -3 & 2\end{pmatrix},\qquad T^{-1}(x, y) = (2x - y,\ -3x + 2y).$$
Check: $T(2x - y, -3x + 2y) = (x, y)$. $(2x - 3y,\ -x + 2y)$ uses the transpose of $A^{-1}$; $(-2x + y, \dots)$ is $-T^{-1}$.""")

T.single(2, ["sylvester"],
    r"$A$ and $B$ are $5\times 5$ real matrices with nullities $N(A) = 2$ and $N(B) = 1$. The largest possible nullity of $AB$ is",
    [r"$3$", r"$2$", r"$1$", r"$5$"],
    r"""Sylvester's law of nullity:
$$\max\{N(A), N(B)\} \le N(AB) \le N(A) + N(B), \quad\text{so}\quad 2 \le N(AB) \le 3.$$
The bound $3$ is attained, for example by $A = \operatorname{diag}(0,0,1,1,1)$, $B = \operatorname{diag}(1,1,0,1,1)$, where $AB = \operatorname{diag}(0,0,0,1,1)$. $2$ is the smallest possible value, not the largest.""")

T.single(2, ["sylvester"],
    r"$A$ and $B$ are $4\times 4$ real matrices with $\rho(A) = 3$ and $\rho(B) = 2$. The least possible value of $\rho(AB)$ is",
    [r"$1$", r"$2$", r"$0$", r"$5$"],
    r"""Sylvester's inequality, with $n = 4$:
$$\rho(AB) \ge \rho(A) + \rho(B) - n = 3 + 2 - 4 = 1.$$
It is attained: $A = \operatorname{diag}(1,1,1,0)$, $B = \operatorname{diag}(0,0,1,1)$ give $AB = \operatorname{diag}(0,0,1,0)$. So $AB$ can never be $O$, ruling out $0$; $2 = \min\{\rho(A), \rho(B)\}$ is the **upper** bound.""")

# ---------------------------------------------------------------- hard singles
T.single(3, ["definition", "exam-tips"],
    r"$T : \R^3 \to \R^3$ is linear with $T(1, 1, 0) = (1, 0, 0)$, $T(0, 1, 1) = (0, 1, 0)$ and $T(1, 0, 1) = (0, 0, 1)$. Then $T(1, 0, 0)$ is",
    [r"$\left(\tfrac12, -\tfrac12, \tfrac12\right)$",
     r"$(1, -1, 1)$",
     r"$\left(\tfrac12, \tfrac12, -\tfrac12\right)$",
     r"$(1, 0, 0)$"],
    r"""Write $(1, 0, 0)$ in the given basis: with $u = (1,1,0)$, $v = (0,1,1)$, $w = (1,0,1)$,
$$u - v + w = (2, 0, 0), \quad\text{so}\quad (1, 0, 0) = \tfrac12(u - v + w).$$
Hence $T(1, 0, 0) = \tfrac12\big((1,0,0) - (0,1,0) + (0,0,1)\big) = \left(\tfrac12, -\tfrac12, \tfrac12\right)$.
$(1, -1, 1)$ forgets the factor $\frac12$; $(1, 0, 0)$ wrongly assumes $T$ fixes $e_1$.""")

T.single(3, ["injective-surjective"],
    r"$T : \R^3 \to \R^3$, $T(x, y, z) = (x + y + z,\ x + 2y + kz,\ x + 4y + k^2z)$. $T$ fails to be invertible exactly when",
    [r"$k = 1$ or $k = 2$", r"$k = 1$ only", r"$k = 2$ only", r"$k = 4$"],
    r"""$T$ is invertible iff its matrix is non-singular. The columns are $(1,1,1)$, $(1,2,4)$, $(1,k,k^2)$: a Vandermonde matrix in $1, 2, k$, so
$$\det = (2 - 1)(k - 1)(k - 2).$$
It vanishes iff $k = 1$ (column 3 = column 1) or $k = 2$ (column 3 = column 2). Each single-value option misses one of the two repeated nodes.""")

T.single(3, ["sylvester", "rank-nullity"],
    r"$T$ is a linear operator on $\R^6$ with $T \circ T = 0$. The largest possible rank of $T$ is",
    [r"$3$", r"$2$", r"$5$", r"$6$"],
    r"""$T^2 = 0$ means $R(T) \subseteq N(T)$, so $\rho(T) \le \nu(T) = 6 - \rho(T)$. Equivalently, by Sylvester, $0 = \rho(T^2) \ge 2\rho(T) - 6$. Either way
$$\rho(T) \le 3.$$
$3$ is attained by $T(x_1, \dots, x_6) = (x_4, x_5, x_6, 0, 0, 0)$. $5$ is the rank of a single nilpotent Jordan block, for which $T^2 \ne 0$.""")

T.single(3, ["rank-nullity", "kernel-range"],
    r"$T : M_3(\R) \to M_3(\R)$ is defined by $T(A) = A - A^T$. The rank of $T$ is",
    [r"$3$", r"$6$", r"$9$", r"$0$"],
    r"""$\ker T = \{A : A = A^T\}$, the symmetric matrices, of dimension $\frac{3\cdot 4}{2} = 6$. By rank–nullity,
$$\rho(T) = 9 - 6 = 3.$$
Indeed the range is the space of skew-symmetric matrices: $A - A^T$ is skew, and every skew $S$ equals $T(S/2)$. $6$ is the nullity, not the rank.""")

T.single(3, ["matrix-representation"],
    r"$T : \R^3 \to \R^2$, $T(x, y, z) = (x + y,\ y + z)$. With ordered bases $B = ((1,0,0), (1,1,0), (1,1,1))$ of $\R^3$ and $C = ((1, 0), (1, 1))$ of $\R^2$, the matrix of $T$ (columns = $C$-coordinates of the images) is",
    [r"$\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 2\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 2 & 2\\ 0 & 1 & 2\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0\\ 1 & 1\\ 0 & 2\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 1\end{pmatrix}$"],
    r"""Images: $T(1,0,0) = (1, 0)$, $T(1,1,0) = (2, 1)$, $T(1,1,1) = (2, 2)$. Since $(a, b) = (a - b)(1, 0) + b(1, 1)$, the $C$-coordinates are $(1, 0)$, $(1, 1)$, $(0, 2)$. So
$$[T]_B^C = \begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 2\end{pmatrix}.$$
$\begin{pmatrix}1 & 2 & 2\\ 0 & 1 & 2\end{pmatrix}$ lists the images without converting to $C$-coordinates; the $3\times 2$ option is the transpose (a map $\R^3 \to \R^2$ needs a $2\times 3$ matrix); the last one is the standard matrix of $T$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["kernel-range", "injective-surjective", "rank-nullity"],
    r"$T : V \to W$ is a linear map between finite-dimensional real vector spaces. Consider the following statements:",
    [r"$\ker T$ is a subspace of $V$.",
     r"$T$ is one-one if and only if $\ker T = \{0\}$.",
     r"If $\dim V < \dim W$, then $T$ can be onto."],
    [r"1 and 2 only", r"1, 2 and 3", r"2 and 3 only", r"1 only"],
    r"""- **1 is true:** if $Tu = Tv = 0$ then $T(\alpha u + \beta v) = 0$, and $0 \in \ker T$.
- **2 is true:** $Tu = Tv \iff T(u - v) = 0$.
- **3 is false:** $\rho(T) \le \dim V < \dim W$, so $R(T) \ne W$. For example, no linear map $\R^2 \to \R^3$ is onto.""")

T.statements(3, ["sylvester"],
    r"$A$ and $B$ are $n\times n$ real matrices, and $N(\cdot)$ denotes nullity. Consider the following statements:",
    [r"$N(AB) \ge N(B)$.",
     r"$\rho(AB) = \rho(BA)$.",
     r"$N(AB) \le N(A) + N(B)$."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 and 2 only", r"3 only"],
    r"""- **1 is true:** $BX = 0 \Rightarrow ABX = 0$, so $N(B) \subseteq N(AB)$.
- **2 is false:** with $A = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$, $B = \begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$,
$$AB = O \ (\rho = 0), \qquad BA = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}\ (\rho = 1).$$
- **3 is true:** this is the upper half of Sylvester's law of nullity.""")

T.statements(1, ["definition"],
    r"Consider the following maps:",
    [r"$T(x, y) = (x + 1,\ y)$ on $\R^2$ is linear.",
     r"$T(x) = x^2$ on $\R$ is linear.",
     r"$T(p)(x) = x\,p(x)$ from $P_n$ to $P_{n+1}$ is linear."],
    [r"3 only", r"1 and 3 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""- **1 is false:** $T(0, 0) = (1, 0) \ne 0$; a translation is never linear.
- **2 is false:** $T(1 + 1) = 4 \ne T(1) + T(1) = 2$.
- **3 is true:** $x(\alpha p + \beta q) = \alpha\,xp + \beta\,xq$, and $\deg(xp) \le n + 1$.""")

# ---------------------------------------------------------------- match
T.match(3, ["rank-nullity", "kernel-range"],
    r"Match each linear map in List I with its rank in List II.",
    [r"$A \mapsto \operatorname{tr}A$, from $M_2(\R)$ to $\R$",
     r"$(x, y, z) \mapsto (x, y, 0)$ on $\R^3$",
     r"$p \mapsto p'$ on $P_3$ (degree $\le 3$)",
     r"the identity map on $M_2(\R)$"],
    [r"$3$", r"$1$", r"$4$", r"$2$"],
    [r"A-2, B-4, C-1, D-3", r"A-2, B-4, C-3, D-1", r"A-4, B-2, C-1, D-3", r"A-2, B-1, C-4, D-3"],
    r"""- **A:** the trace is a non-zero map onto $\R$: rank $1$ (nullity $3$). A-2.
- **B:** the range is the $xy$-plane: rank $2$. B-4.
- **C:** $\dim P_3 = 4$ and the kernel is the constants, so rank $= 4 - 1 = 3$; the range is $P_2$. C-1.
- **D:** the identity is onto $M_2(\R)$, of dimension $4$. D-3.

The tempting slip in C is rank $4$ (forgetting that constants die).""")

T.match(2, ["matrix-representation"],
    r"Match each operator on $\R^2$ in List I with its matrix (standard basis, columns = images of $e_1, e_2$) in List II.",
    [r"reflection in the line $y = x$",
     r"projection onto the $x$-axis",
     r"rotation through $90^\circ$ anticlockwise",
     r"$(x, y) \mapsto (x + y,\ y)$"],
    [r"$\begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$",
     r"$\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$",
     r"$\begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$"],
    [r"A-3, B-4, C-1, D-2", r"A-1, B-4, C-3, D-2", r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-1, D-4"],
    r"""- **A:** $(x, y) \mapsto (y, x)$: $e_1 \mapsto e_2$, $e_2 \mapsto e_1$, matrix $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$. A-3.
- **B:** $(x, y) \mapsto (x, 0)$. B-4.
- **C:** $e_1 \mapsto e_2$, $e_2 \mapsto -e_1$, so the columns are $(0, 1)$, $(-1, 0)$. C-1. (Its transpose is the **clockwise** rotation.)
- **D:** $e_1 \mapsto (1, 0)$, $e_2 \mapsto (1, 1)$: a shear. D-2.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["definition"],
    r"The map $T(x, y) = (x + 1,\ y - 1)$ is a linear operator on $\R^2$.",
    r"Every linear map sends the zero vector to the zero vector.",
    3,
    r"""**R is true:** $T(0) = T(0 + 0) = T(0) + T(0)$, so $T(0) = 0$.

**A is false:** $T(0, 0) = (1, -1) \ne (0, 0)$, so by R the map is not linear. It is a translation. So (3).""")

T.assertion_reason(2, ["injective-surjective"],
    r"Every one-one linear operator on $\R^4$ is onto.",
    r"For any linear map $T : V \to W$ between finite-dimensional spaces, if $T$ is one-one then $T$ is onto.",
    2,
    r"""**A is true:** one-one means $\nu(T) = 0$, so $\rho(T) = 4 - 0 = 4 = \dim\R^4$.

**R is false:** it needs $\dim V = \dim W$. The inclusion $T(x, y) = (x, y, 0)$ from $\R^2$ to $\R^3$ is one-one but not onto. So (2).""")

T.assertion_reason(2, ["change-of-basis"],
    r"Two matrices representing the same linear operator on $\R^3$ relative to two different ordered bases have the same rank.",
    r"Similar matrices have the same trace.",
    1,
    r"""**A is true:** the two matrices are similar, $A' = P^{-1}AP$, and multiplying by non-singular matrices does not change rank. Also, both ranks equal $\rho(T) = \dim R(T)$, which does not depend on a basis.

**R is true:** $\operatorname{tr}(P^{-1}AP) = \operatorname{tr}(APP^{-1}) = \operatorname{tr}A$.

But equal traces say nothing about rank: $\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$ and $O$ both have trace $0$ but ranks $2$ and $0$. R does not explain A, so (1).""")

T.assertion_reason(3, ["sylvester"],
    r"If $A$ is a $3\times 3$ real matrix with $A^2 = O$, then $\rho(A) \le 1$.",
    r"For $n\times n$ matrices $A$ and $B$, $\rho(AB) \ge \rho(A) + \rho(B) - n$.",
    0,
    r"""**R is true:** it is Sylvester's inequality (the rank form of the law of nullity).

**A is true, by R:** take $B = A$, $n = 3$:
$$0 = \rho(A^2) \ge 2\rho(A) - 3 \;\Rightarrow\; \rho(A) \le \tfrac32 \;\Rightarrow\; \rho(A) \le 1.$$
The bound is attained by $A = \begin{pmatrix}0 & 0 & 1\\ 0 & 0 & 0\\ 0 & 0 & 0\end{pmatrix}$. So (0).""")


# ---------------------------------------------------------------- checks
def check():
    import sympy as sp
    x, y, z, w, a, b, k = sp.symbols("x y z w a b k")
    u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2")
    M = sp.Matrix

    def is_linear(f):
        lhs = f(a*u1 + b*v1, a*u2 + b*v2)
        rhs = [a*p + b*q for p, q in zip(f(u1, u2), f(v1, v2))]
        return all(sp.expand(l - r) == 0 for l, r in zip(lhs, rhs))

    # q1
    assert is_linear(lambda x, y: (x + y, x - y))
    assert not is_linear(lambda x, y: (x + 1, y))
    assert not is_linear(lambda x, y: (x**2, y))
    assert not is_linear(lambda x, y: (x*y, x))
    # q2, q3: rank-nullity
    eq(5 - 3, 2, "q2")
    P = M([[1, 0, 0], [0, 1, 0]])          # onto R^3 -> R^2
    assert P.rank() == 2 and len(P.nullspace()) == 1
    assert M.zeros(2, 3).rank() == 0       # not onto
    # q4
    A4 = M([[2, 3], [1, -1]])
    assert A4 * M([x, y]) == M([2*x + 3*y, x - y])
    # q5
    A5 = M([[1, 3], [2, 4]])
    assert A5 * M([2, -1]) == M([-1, 0])
    assert A5.T * M([2, -1]) == M([0, 2])
    # q6
    X = M(2, 2, sp.symbols("m0:4")); Y = M(2, 2, sp.symbols("n0:4"))
    assert sp.expand((X + Y).trace() - X.trace() - Y.trace()) == 0
    eq((2*sp.eye(2)).det(), 4, "q6"); assert (2*sp.eye(2)).det() != 2*sp.eye(2).det()
    # q7
    eq(len([1, x, x**2, x**3]), 4, "q7")
    # q8
    A8 = M([[1, 1, 1, 1], [1, 2, 3, 4], [2, 3, 4, 5]])
    eq(A8.rank(), 2, "q8"); eq(len(A8.nullspace()), 2, "q8")
    # q9
    A9 = M([[1, 2, -1], [0, 1, 1], [1, 1, -2]])
    ns = A9.nullspace(); assert len(ns) == 1
    assert M([3, -1, 1]).cross(ns[0]) == M([0, 0, 0]) and A9 * M([3, -1, 1]) == M([0, 0, 0])
    assert A9 * M([-3, 1, 1]) != M([0, 0, 0])
    # q10
    basis = [sp.Integer(1), x, x**2]
    cols = [[sp.Poly(sp.diff(p, x), x).coeff_monomial(m) for m in basis] for p in basis]
    D = M(cols).T
    assert D == M([[0, 1, 0], [0, 0, 2], [0, 0, 0]])
    # q11
    A11 = M([[2, 1], [1, 0]]); P11 = M([[1, 1], [0, 1]])
    assert P11.inv() * A11 * P11 == M([[1, 2], [1, 1]])
    # q12
    A12 = M([[1, 0, -1], [-1, 1, 0], [0, -1, 1]])
    eq(A12.rank(), 2, "q12")
    # q13
    S = M([[1, 1], [0, 1]]); T2 = M([[2, 0], [1, -1]])
    assert S * T2 * M([x, y]) == M([3*x - y, x - y])
    assert T2 * S * M([x, y]) == M([2*x + 2*y, x])
    # q14
    A14 = M([[2, 1], [3, 2]])
    assert A14.inv() * M([x, y]) == M([2*x - y, -3*x + 2*y])
    # q15
    A15 = sp.diag(0, 0, 1, 1, 1); B15 = sp.diag(1, 1, 0, 1, 1)
    eq(5 - (A15 * B15).rank(), 3, "q15")
    # q16
    A16 = sp.diag(1, 1, 1, 0); B16 = sp.diag(0, 0, 1, 1)
    assert A16.rank() == 3 and B16.rank() == 2
    eq((A16 * B16).rank(), 1, "q16"); eq(3 + 2 - 4, 1, "q16")
    # q17
    Bm = M([[1, 0, 1], [1, 1, 0], [0, 1, 1]])       # columns u, v, w
    Tm = sp.eye(3) * Bm.inv()                        # T(u)=e1, T(v)=e2, T(w)=e3
    assert Tm * M([1, 0, 0]) == M([sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)])
    # q18
    A18 = M([[1, 1, 1], [1, 2, k], [1, 4, k**2]])
    assert set(sp.solve(A18.det(), k)) == {1, 2}
    # q19
    N19 = M.zeros(6, 6)
    for i in range(3):
        N19[i, i + 3] = 1
    assert N19**2 == M.zeros(6, 6) and N19.rank() == 3
    # q20: matrix of A -> A - A^T on M_3 as a 9x9 matrix
    cols = []
    for i in range(3):
        for j in range(3):
            E = M.zeros(3, 3); E[i, j] = 1
            cols.append(list(E - E.T))
    L = M(cols).T
    eq(L.rank(), 3, "q20")
    # q21
    C = M([[1, 1], [0, 1]])
    Tstd = M([[1, 1, 0], [0, 1, 1]])
    B3 = M([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    assert C.inv() * Tstd * B3 == M([[1, 1, 0], [0, 1, 2]])
    # statements 1: no onto map R^2 -> R^3 (rank <= 2)
    assert M(3, 2, sp.symbols("r0:6")).rank() <= 2
    # statements 2
    A = M([[0, 1], [0, 0]]); B = M([[1, 0], [0, 0]])
    assert (A * B).rank() == 0 and (B * A).rank() == 1
    import random
    rng = random.Random(1)
    for _ in range(200):
        n = 4
        A = M(n, n, lambda i, j: rng.choice([0, 0, 1, -1, 2]))
        B = M(n, n, lambda i, j: rng.choice([0, 0, 1, -1, 2]))
        NA, NB, NAB = n - A.rank(), n - B.rank(), n - (A * B).rank()
        assert max(NA, NB) <= NAB <= NA + NB
    # statements 3
    assert not is_linear(lambda x, y: (x + 1, y))
    p, q = sp.symbols("p q", cls=sp.Function)
    assert sp.expand(x * (a * p(x) + b * q(x)) - a * x * p(x) - b * x * q(x)) == 0
    # match 1: ranks
    trace_map = M([[1, 0, 0, 1]])
    proj = M([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    D3 = M([[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]])
    ranks = [trace_map.rank(), proj.rank(), D3.rank(), sp.eye(4).rank()]
    right = [3, 1, 4, 2]
    eq(sum(abs(right.index(r) + 1 - want) for r, want in zip(ranks, [2, 4, 1, 3])), 0, "match1")
    # match 2
    th = sp.pi / 2
    rot = M([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
    assert rot == M([[0, -1], [1, 0]])
    assert M([[0, 1], [1, 0]]) * M([x, y]) == M([y, x])
    assert M([[1, 0], [0, 0]]) * M([x, y]) == M([x, 0])
    assert M([[1, 1], [0, 1]]) * M([x, y]) == M([x + y, y])
    # AR1
    assert not is_linear(lambda x, y: (x + 1, y - 1))
    # AR2: inclusion R^2 -> R^3 is one-one, not onto
    inc = M([[1, 0], [0, 1], [0, 0]])
    assert len(inc.nullspace()) == 0 and inc.rank() < 3
    # AR3
    Pn = M([[1, 2, 0], [0, 1, 1], [1, 0, 1]]); An = M([[1, 2, 3], [2, 4, 6], [0, 1, 1]])
    assert (Pn.inv() * An * Pn).rank() == An.rank()
    eq((Pn.inv() * An * Pn).trace(), An.trace(), "AR3")
    assert M([[1, 0], [0, -1]]).trace() == 0 and M([[1, 0], [0, -1]]).rank() == 2
    # AR4
    N = M([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
    assert N**2 == M.zeros(3, 3) and N.rank() == 1
    for _ in range(300):
        A = M(3, 3, lambda i, j: rng.choice([0, 0, 0, 1, -1]))
        if A**2 == M.zeros(3, 3):
            assert A.rank() <= 1


T.write(check)
