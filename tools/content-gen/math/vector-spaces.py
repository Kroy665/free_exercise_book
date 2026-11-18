import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.vector-spaces")

# ---------------------------------------------------------------- easy singles
T.single(1, ["subspaces"],
    r"Which of the following subsets of $\R^3$ is a subspace?",
    [r"$\{(x,y,z) : x + 2y - z = 0\}$",
     r"$\{(x,y,z) : x + y + z = 1\}$",
     r"$\{(x,y,z) : xy = 0\}$",
     r"$\{(x,y,z) : x \ge 0\}$"],
    r"""$x + 2y - z = 0$ is a homogeneous linear condition: if $u, v$ satisfy it, so does $au + bv$. It is a plane through the origin, so it is a subspace.

- $x + y + z = 1$: $(0,0,0)$ is not in it.
- $xy = 0$: $(1,0,0) + (0,1,0) = (1,1,0)$ has $xy = 1$.
- $x \ge 0$: $(-1)(1,0,0) = (-1,0,0)$ is not in it.""")

T.single(1, ["axioms", "exam-tips"],
    r"The dimension of $\C^3$ as a vector space over $\R$ is",
    [r"$6$", r"$3$", r"$9$", r"infinite"],
    r"""Each complex coordinate $a + ib$ needs two real parameters. A real basis is
$$e_1, ie_1, e_2, ie_2, e_3, ie_3,$$
so $\dim_\R \C^3 = 2\cdot 3 = 6$. The answer $3$ is $\dim_\C \C^3$, over the field $\C$.""")

T.single(1, ["basis-dimension"],
    r"The dimension of the vector space of all real $3\times 3$ symmetric matrices is",
    [r"$6$", r"$3$", r"$9$", r"$5$"],
    r"""A symmetric matrix is fixed by its entries on and above the diagonal:
$$\frac{n(n+1)}{2} = \frac{3\cdot 4}{2} = 6.$$
$3$ is the dimension of the skew-symmetric (or diagonal) $3\times 3$ matrices; $9$ is all of $M_3(\R)$.""")

T.single(1, ["basis-dimension", "exam-tips"],
    r"The dimension of the real vector space $P_3$ of polynomials of degree at most $3$ (together with the zero polynomial) is",
    [r"$4$", r"$3$", r"$5$", r"infinite"],
    r"""The basis $1, x, x^2, x^3$ has $4$ elements, so $\dim P_3 = 3 + 1 = 4$.

$3$ is the off-by-one slip of counting only the degree.""")

T.single(1, ["span-independence"],
    r"The vectors $(1, 2)$ and $(3, k)$ in $\R^2$ are linearly dependent when $k$ equals",
    [r"$6$", r"$-6$", r"$\frac32$", r"$\frac23$"],
    r"""Two vectors are dependent iff they are proportional, iff
$$\begin{vmatrix}1 & 2\\ 3 & k\end{vmatrix} = k - 6 = 0 \iff k = 6.$$
Then $(3, 6) = 3(1, 2)$. $\frac32$ comes from setting $3/1 = k/2$ upside down.""")

T.single(1, ["span-independence"],
    r"Which of the following sets of vectors in $\R^3$ is linearly dependent?",
    [r"$\{(1,0,0),\,(0,1,0),\,(0,0,0)\}$",
     r"$\{(1,0,0),\,(0,1,0),\,(0,0,1)\}$",
     r"$\{(1,1,0),\,(0,1,1)\}$",
     r"$\{(1,2,3)\}$"],
    r"""Any set containing the zero vector is dependent:
$$0\cdot(1,0,0) + 0\cdot(0,1,0) + 1\cdot(0,0,0) = 0$$
is a non-trivial relation.

The standard basis is independent; $(1,1,0), (0,1,1)$ are not proportional; a single non-zero vector is independent.""")

# ---------------------------------------------------------------- medium singles
T.single(2, ["basis-dimension"],
    r"The dimension of the space of real $4\times 4$ skew-symmetric matrices is",
    [r"$6$", r"$10$", r"$16$", r"$4$"],
    r"""A skew-symmetric matrix has zero diagonal and $a_{ji} = -a_{ij}$, so only the entries strictly above the diagonal are free:
$$\frac{n(n-1)}{2} = \frac{4\cdot 3}{2} = 6.$$
$10 = \frac{4\cdot 5}{2}$ is the symmetric count; it wrongly lets the diagonal be free.""")

T.single(2, ["basis-dimension"],
    r"The dimension of the subspace $\{A \in M_3(\R) : \operatorname{tr}A = 0\}$ is",
    [r"$8$", r"$9$", r"$6$", r"$3$"],
    r"""$\operatorname{tr}A = a_{11} + a_{22} + a_{33} = 0$ is one non-trivial linear condition on the $9$ entries, so
$$\dim = 9 - 1 = 8.$$
Basis: the $6$ off-diagonal units $E_{ij}$ and $E_{11} - E_{33}$, $E_{22} - E_{33}$.""")

T.single(2, ["span-independence"],
    r"The vectors $(1,1,0)$, $(0,1,1)$, $(1,0,k)$ are linearly dependent if and only if",
    [r"$k = -1$", r"$k = 1$", r"$k = 0$", r"$k = 2$"],
    r"""Three vectors in $\R^3$ are dependent iff the determinant they form is $0$:
$$\begin{vmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & k\end{vmatrix} = 1\cdot k - 1\cdot(0 - 1) + 0 = k + 1.$$
So $k = -1$. Check: $(1,1,0) - (0,1,1) = (1, 0, -1)$. A sign slip in the second cofactor gives $k = 1$.""")

T.single(2, ["row-column-space", "span-independence"],
    r"The dimension of the subspace of $\R^3$ spanned by $(1,2,1)$, $(2,1,0)$, $(3,3,1)$, $(1,-1,-1)$ is",
    [r"$2$", r"$3$", r"$4$", r"$1$"],
    r"""The dimension of the span is the rank of the matrix with these rows. Here
$$(3,3,1) = (1,2,1) + (2,1,0), \qquad (1,-1,-1) = (2,1,0) - (1,2,1),$$
and $(1,2,1), (2,1,0)$ are not proportional. So the dimension is $2$.

$4$ is impossible: a subspace of $\R^3$ has dimension at most $3$.""")

T.single(2, ["sum-intersection"],
    r"$W_1$ and $W_2$ are subspaces of $\R^5$ with $\dim W_1 = 3$ and $\dim W_2 = 4$. The least possible value of $\dim(W_1 \cap W_2)$ is",
    [r"$2$", r"$1$", r"$3$", r"$0$"],
    r"""Since $W_1 + W_2 \subseteq \R^5$,
$$\dim(W_1 \cap W_2) = 3 + 4 - \dim(W_1 + W_2) \ge 7 - 5 = 2.$$
The value $2$ is attained: $W_1 = L\{e_1, e_2, e_3\}$, $W_2 = L\{e_1, e_2, e_4, e_5\}$. $0$ forgets that the subspaces live in a space of dimension only $5$.""")

T.single(2, ["coordinates"],
    r"The coordinate vector of $(3, 1)$ relative to the ordered basis $\big((1,1),\,(1,-1)\big)$ of $\R^2$ is",
    [r"$(2, 1)$", r"$(1, 2)$", r"$(3, 1)$", r"$(2, -1)$"],
    r"""Solve $a(1,1) + b(1,-1) = (3,1)$: $a + b = 3$, $a - b = 1$, so $a = 2$, $b = 1$.
$$[(3,1)]_B = (2, 1).$$
Check: $2(1,1) + (1,-1) = (3,1)$. $(1,2)$ is the answer for the basis in the reverse order; $(3,1)$ copies the standard coordinates.""")

T.single(2, ["coordinates"],
    r"The coordinate vector of $p(x) = 2 + 3x + x^2$ relative to the ordered basis $\big(1,\ 1 + x,\ (1 + x)^2\big)$ of $P_2$ is",
    [r"$(0, 1, 1)$", r"$(2, 3, 1)$", r"$(1, 1, 0)$", r"$(0, 1, 2)$"],
    r"""Put $t = 1 + x$, so $x = t - 1$:
$$p = 2 + 3(t - 1) + (t - 1)^2 = 2 + 3t - 3 + t^2 - 2t + 1 = 0 + t + t^2.$$
So $p = 0\cdot 1 + 1\cdot(1 + x) + 1\cdot(1 + x)^2$ and $[p]_B = (0, 1, 1)$.

Check: $(1 + x) + (1 + 2x + x^2) = 2 + 3x + x^2$. $(2, 3, 1)$ is the coordinate vector relative to the standard basis $1, x, x^2$.""")

T.single(2, ["row-column-space"],
    r"Which of the following vectors lies in the row space of $\begin{pmatrix}1 & 0 & 2\\ 0 & 1 & -1\end{pmatrix}$?",
    [r"$(2, 3, 1)$", r"$(1, 1, 2)$", r"$(2, 3, 2)$", r"$(0, 0, 1)$"],
    r"""The matrix is in reduced echelon form with pivots in columns 1 and 2. A row-space vector with first two coordinates $(a, b)$ must be
$$a(1,0,2) + b(0,1,-1) = (a,\ b,\ 2a - b).$$
- $(2,3,\cdot)$: third coordinate must be $4 - 3 = 1$. So $(2,3,1)$ is in it and $(2,3,2)$ is not.
- $(1,1,\cdot)$: needs $2 - 1 = 1$, not $2$.
- $(0,0,\cdot)$: needs $0$, not $1$.""")

T.single(2, ["sum-intersection"],
    r"Let $W_1, W_2$ be subspaces of a vector space $V$. Then $W_1 \cup W_2$ is a subspace of $V$ if and only if",
    [r"$W_1 \subseteq W_2$ or $W_2 \subseteq W_1$",
     r"$W_1 \cap W_2 = \{0\}$",
     r"$W_1 + W_2 = V$",
     r"$W_1 \cap W_2 \ne \{0\}$"],
    r"""If $u \in W_1 \setminus W_2$ and $v \in W_2 \setminus W_1$, then $u + v$ lies in neither: $u + v \in W_1$ would give $v = (u + v) - u \in W_1$, and similarly for $W_2$. So the union is closed under addition only when one subspace contains the other; conversely, then the union is just the larger subspace.

The $x$- and $y$-axes in $\R^2$ meet only in $\{0\}$ and their sum is $\R^2$, yet their union is not a subspace; so the other conditions are wrong.""")

T.single(2, ["basis-dimension"],
    r"The dimension of $W = \{p \in P_3 : p(1) = 0 \text{ and } p(-1) = 0\}$, where $P_3$ is the space of real polynomials of degree at most $3$, is",
    [r"$2$", r"$3$", r"$1$", r"$4$"],
    r"""$p(1) = p(-1) = 0$ means $(x - 1)(x + 1) \mid p$, so
$$W = \{(x^2 - 1)(a + bx) : a, b \in \R\},$$
with basis $x^2 - 1,\ x^3 - x$. Hence $\dim W = 2 = 4 - 2$ (two independent conditions on a 4-dimensional space). $3$ starts from $\dim P_3 = 3$, the off-by-one slip.""")

T.single(2, ["basis-dimension"],
    r"The dimension of the space of real $3\times 3$ upper triangular matrices with trace $0$ is",
    [r"$5$", r"$6$", r"$8$", r"$3$"],
    r"""Upper triangular $3\times 3$ matrices have $\frac{3\cdot 4}{2} = 6$ free entries. The trace condition $a_{11} + a_{22} + a_{33} = 0$ removes one:
$$\dim = 6 - 1 = 5.$$
$8$ is the dimension of all trace-zero $3\times 3$ matrices.""")

# ---------------------------------------------------------------- hard singles
T.single(3, ["sum-intersection"],
    r"In $\R^4$ let $W_1 = \{x : x_1 + x_2 + x_3 + x_4 = 0\}$ and $W_2 = \{x : x_1 = x_2,\ x_3 = x_4\}$. Then $\dim(W_1 + W_2)$ is",
    [r"$4$", r"$5$", r"$3$", r"$2$"],
    r"""$\dim W_1 = 3$ (one condition) and $\dim W_2 = 2$ (two conditions). On $W_2$, $x = (a, a, b, b)$, and $W_1$ adds $2a + 2b = 0$:
$$W_1 \cap W_2 = L\{(1, 1, -1, -1)\}, \quad \dim = 1.$$
$$\dim(W_1 + W_2) = 3 + 2 - 1 = 4.$$
$5$ forgets the intersection (and exceeds $\dim\R^4$); $3$ assumes $W_2 \subseteq W_1$.""")

T.single(3, ["basis-dimension"],
    r"The set of all $2\times 2$ complex Hermitian matrices is a vector space over $\R$. Its dimension is",
    [r"$4$", r"$3$", r"$8$", r"$2$"],
    r"""A Hermitian matrix is $\begin{pmatrix}a & c + id\\ c - id & b\end{pmatrix}$ with $a, b, c, d \in \R$: the diagonal must be real and $a_{21} = \overline{a_{12}}$. Four real parameters, basis
$$\begin{pmatrix}1&0\\0&0\end{pmatrix},\ \begin{pmatrix}0&0\\0&1\end{pmatrix},\ \begin{pmatrix}0&1\\1&0\end{pmatrix},\ \begin{pmatrix}0&i\\-i&0\end{pmatrix}.$$
In general the dimension is $n^2$. $3$ is the count for real symmetric $2\times 2$ matrices; $8$ is $\dim_\R M_2(\C)$.""")

T.single(3, ["basis-dimension"],
    r"The dimension of the subspace $\{X \in M_2(\R) : XA = AX\}$, where $A = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$, is",
    [r"$2$", r"$1$", r"$3$", r"$4$"],
    r"""Let $X = \begin{pmatrix}p & q\\ r & s\end{pmatrix}$. Then
$$AX = \begin{pmatrix}p + r & q + s\\ r & s\end{pmatrix}, \qquad XA = \begin{pmatrix}p & p + q\\ r & r + s\end{pmatrix}.$$
Equating: $r = 0$ and $s = p$. So $X = \begin{pmatrix}p & q\\ 0 & p\end{pmatrix} = pI + q\begin{pmatrix}0&1\\0&0\end{pmatrix}$, dimension $2$.

$1$ counts only the scalar matrices; $4$ would need $A$ to be scalar.""")

T.single(3, ["span-independence"],
    r"The vector $(1, k, 5)$ lies in the span of $(1, -3, 2)$ and $(2, -1, 1)$ for",
    [r"$k = -8$", r"$k = 8$", r"$k = -10$", r"$k = 2$"],
    r"""Write $(1, k, 5) = a(1, -3, 2) + b(2, -1, 1)$:
$$a + 2b = 1, \qquad 2a + b = 5, \qquad -3a - b = k.$$
The first two give $a = 3$, $b = -1$; then $k = -9 + 1 = -8$.

Check by determinant: $\begin{vmatrix}1 & -3 & 2\\ 2 & -1 & 1\\ 1 & -8 & 5\end{vmatrix} = 0$. $k = -10$ comes from taking $b = +1$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["span-independence", "basis-dimension"],
    r"Consider the following statements about vectors in $\R^3$:",
    [r"Any four vectors in $\R^3$ are linearly dependent.",
     r"Any three vectors that span $\R^3$ form a basis of $\R^3$.",
     r"Every subset of a linearly dependent set is linearly dependent."],
    [r"1 and 2 only", r"1, 2 and 3", r"2 and 3 only", r"1 only"],
    r"""1. True: $\dim\R^3 = 3$, so more than $3$ vectors are dependent (replacement theorem).
2. True: a spanning set contains a basis, which must have exactly $3$ vectors, so the set is itself the basis.
3. False: $\{(1,0,0), (2,0,0)\}$ is dependent but its subset $\{(1,0,0)\}$ is independent. It is the **superset** of a dependent set that is always dependent.""")

T.statements(3, ["sum-intersection"],
    r"Let $W_1$ and $W_2$ be subspaces of a finite-dimensional vector space $V$. Consider:",
    [r"$W_1 \cap W_2$ is a subspace of $V$.",
     r"$W_1 + W_2$ is the smallest subspace of $V$ containing $W_1 \cup W_2$.",
     r"If $V = \R^3$ and $\dim W_1 = \dim W_2 = 2$, then $W_1 \cap W_2 \ne \{0\}$."],
    [r"1, 2 and 3", r"1 and 2 only", r"1 only", r"2 and 3 only"],
    r"""1. True: if $u, v \in W_1 \cap W_2$, then $au + bv$ lies in both.
2. True: $W_1 + W_2$ contains $W_1$ and $W_2$, and any subspace containing both contains all sums $w_1 + w_2$. So $W_1 + W_2 = L(W_1 \cup W_2)$.
3. True: by the dimension formula,
$$\dim(W_1 \cap W_2) = 2 + 2 - \dim(W_1 + W_2) \ge 4 - 3 = 1.$$
Two planes through the origin in $\R^3$ always share at least a line.""")

# ---------------------------------------------------------------- match
T.match(2, ["basis-dimension"],
    r"Match each subspace of $M_4(\R)$ (real $4\times 4$ matrices) in List I with its dimension in List II.",
    [r"symmetric matrices", r"skew-symmetric matrices", r"matrices of trace zero", r"diagonal matrices"],
    [r"$4$", r"$6$", r"$10$", r"$15$"],
    [r"A-3, B-2, C-4, D-1", r"A-2, B-3, C-4, D-1", r"A-3, B-2, C-1, D-4", r"A-4, B-2, C-3, D-1"],
    r"""With $n = 4$:
- symmetric: $\frac{n(n+1)}{2} = 10$;
- skew-symmetric: $\frac{n(n-1)}{2} = 6$;
- trace zero: $n^2 - 1 = 15$;
- diagonal: $n = 4$.

So A-3, B-2, C-4, D-1. Swapping the symmetric and skew counts (A-2, B-3) is the usual slip: the skew diagonal is forced to be $0$.""")

T.match(3, ["axioms", "basis-dimension", "row-column-space", "subspaces"],
    r"Match each real vector space in List I with its dimension in List II.",
    [r"$\C^3$ over $\R$",
     r"real polynomials of degree at most $4$",
     r"$\{x \in \R^4 : x_1 + x_2 + x_3 + x_4 = 0\}$",
     r"the row space of $\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 1 & 0 & 1\end{pmatrix}$"],
    [r"$2$", r"$3$", r"$5$", r"$6$"],
    [r"A-4, B-3, C-2, D-1", r"A-2, B-3, C-4, D-1", r"A-4, B-2, C-3, D-1", r"A-4, B-3, C-1, D-2"],
    r"""- A: $\dim_\R\C^3 = 2\cdot 3 = 6$.
- B: basis $1, x, x^2, x^3, x^4$, so $5$.
- C: one non-trivial homogeneous condition in $\R^4$: $4 - 1 = 3$.
- D: row 2 $= 2\times$ row 1, and row 3 is not a multiple of row 1, so the rank is $2$.

So A-4, B-3, C-2, D-1. Taking $\dim P_4 = 4$ or $\dim_\R\C^3 = 3$ are the off-by-one and wrong-field traps.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["span-independence"],
    r"The vectors $(1, 2)$ and $(2, 4)$ in $\R^2$ are linearly dependent.",
    r"Every set of vectors containing the zero vector is linearly dependent.",
    1,
    r"""A is true: $(2, 4) = 2(1, 2)$, so $2(1,2) - (2,4) = 0$.

R is true: $1\cdot 0 = 0$ is a non-trivial relation. But the set in A does not contain the zero vector, so R does not explain A. The correct reason is that two vectors are dependent iff they are proportional.""")

T.assertion_reason(1, ["subspaces", "sum-intersection"],
    r"$\{(x, y) \in \R^2 : xy = 0\}$ is not a subspace of $\R^2$.",
    r"The union of two subspaces is a subspace only if one of them contains the other.",
    0,
    r"""The set $xy = 0$ is the union of the $x$-axis and the $y$-axis, two subspaces neither of which contains the other. By R it is not a subspace; explicitly, $(1, 0) + (0, 1) = (1, 1)$ has $xy = 1$.

Both are true and R explains A.""")

T.assertion_reason(2, ["subspaces"],
    r"$\{(x, y, z) \in \R^3 : x + y + z = 1\}$ is a subspace of $\R^3$.",
    r"Every subspace of a vector space contains the zero vector.",
    3,
    r"""R is true: if $W$ is a subspace and $w \in W$, then $0 = 0\cdot w \in W$.

A is false: $0 + 0 + 0 = 0 \ne 1$, so $(0,0,0)$ is not in the set. (R is exactly the tool that disproves A.) The set is a plane **not** through the origin.""")

T.assertion_reason(3, ["row-column-space"],
    r"A matrix and its row echelon form have the same row space.",
    r"Elementary row operations do not change the column space of a matrix.",
    2,
    r"""A is true: each new row is a linear combination of the old rows, and each row operation can be reversed, so the row spans are equal.

R is false. For $\begin{pmatrix}1 & 2\\ 2 & 4\end{pmatrix} \to \begin{pmatrix}1 & 2\\ 0 & 0\end{pmatrix}$, the column space changes from $L\{(1, 2)\}$ to $L\{(1, 0)\}$. Row operations preserve only the **dimension** of the column space and the linear relations among the columns.""")

T.assertion_reason(3, ["subspaces"],
    r"The set of singular real $2\times 2$ matrices is not a subspace of $M_2(\R)$.",
    r"If $A$ is a singular matrix and $c$ is a real number, then $cA$ is singular.",
    1,
    r"""A is true: $\begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$ and $\begin{pmatrix}0 & 0\\ 0 & 1\end{pmatrix}$ are singular, but their sum $I$ is not. Closure under addition fails.

R is true: $\det(cA) = c^2\det A = 0$. But R is about scalar multiplication, which does hold; it cannot explain why the set fails to be a subspace. So both are true and R does not explain A.""")


def check():
    import sympy as sp
    M = sp.Matrix
    a, b, c, d, k = sp.symbols("a b c d k")

    # q1: plane is a subspace; distractors fail
    u, v = M([1, 0, 1]), M([0, 1, 2])
    f = lambda w: w[0] + 2 * w[1] - w[2]
    eq(f(u), 0); eq(f(v), 0); eq(sp.expand(f(a * u + b * v)), 0, "q1")
    eq(sum(M([0, 0, 0])), 0, "q1 d1: zero not on x+y+z=1")
    w = M([1, 0, 0]) + M([0, 1, 0]); eq(w[0] * w[1], 1, "q1 d2")

    # q2: dim_R C^3 = 6 (real 6x6 matrix of real/imag parts of basis has full rank)
    basis = []
    for i in range(3):
        for s in (1, sp.I):
            e = [0] * 3; e[i] = s
            basis.append([x for z in e for x in (sp.re(z), sp.im(z))])
    eq(M(basis).rank(), 6, "q2")

    # matrix-space dimensions via linear conditions on n^2 entries
    def dim_sub(n, conds):
        X = M(n, n, sp.symbols(f"x0:{n*n}"))
        eqs = [e for e in conds(X) if e != 0]
        if not eqs:
            return n * n
        A, _ = sp.linear_eq_to_matrix(eqs, list(X))
        return n * n - A.rank()
    sym = lambda X: list(X - X.T)
    skew = lambda X: list(X + X.T)
    tr0 = lambda X: [X.trace()]
    diag = lambda X: [X[i, j] for i in range(X.rows) for j in range(X.cols) if i != j]
    upper = lambda X: [X[i, j] for i in range(X.rows) for j in range(X.cols) if i > j]
    eq(dim_sub(3, sym), 6, "q3")
    eq(len(sp.Poly(1 + sp.Symbol("x") ** 3).all_coeffs()), 4, "q4: P3 basis size")
    eq(sp.solve(M([[1, 2], [3, k]]).det(), k)[0], 6, "q5")
    eq(M([[1, 0, 0], [0, 1, 0], [0, 0, 0]]).rank(), 2, "q6 dependent")
    eq(M([[1, 1, 0], [0, 1, 1]]).rank(), 2, "q6 d")
    eq(dim_sub(4, skew), 6, "q7")
    eq(dim_sub(3, tr0), 8, "q8")
    eq(sp.solve(M([[1, 1, 0], [0, 1, 1], [1, 0, k]]).det(), k)[0], -1, "q9")
    eq(M([[1, 2, 1], [2, 1, 0], [3, 3, 1], [1, -1, -1]]).rank(), 2, "q10")
    # q11: example attaining 2
    W1 = M([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
    W2 = M([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
    eq(3 + 4 - W1.col_join(W2).rank(), 2, "q11")
    eq(3 + 4 - 5, 2, "q11 bound")
    # q12
    assert M([[1, 1], [1, -1]]).inv() * M([3, 1]) == M([2, 1]), "q12"
    assert M([[1, 1], [-1, 1]]).inv() * M([3, 1]) == M([1, 2]), "q12 reversed order"
    # q13
    x = sp.Symbol("x")
    eq(sp.expand(0 + 1 * (1 + x) + 1 * (1 + x) ** 2 - (2 + 3 * x + x ** 2)), 0, "q13")
    # q14: row space membership
    R = M([[1, 0, 2], [0, 1, -1]])
    for vec, ans in [((2, 3, 1), 2), ((1, 1, 2), 3), ((2, 3, 2), 3), ((0, 0, 1), 3)]:
        eq(R.col_join(M([vec])).rank(), ans, f"q14 {vec}")
    # q15: union counterexample
    s = M([1, 0]) + M([0, 1]); eq(s[0] * s[1], 1, "q15")
    # q16: dim {p in P3: p(1)=p(-1)=0}
    cs = sp.symbols("c0:4"); p = sum(cs[i] * x ** i for i in range(4))
    A, _ = sp.linear_eq_to_matrix([p.subs(x, 1), p.subs(x, -1)], cs)
    eq(4 - A.rank(), 2, "q16")
    # q17: upper triangular trace 0, n=3
    eq(dim_sub(3, lambda X: upper(X) + tr0(X)), 5, "q17")
    # q18
    Ab1 = M([[1, 1, 1, 1]]); Ab2 = M([[1, -1, 0, 0], [0, 0, 1, -1]])
    dW1 = 4 - Ab1.rank(); dW2 = 4 - Ab2.rank(); dcap = 4 - Ab1.col_join(Ab2).rank()
    eq(dW1, 3); eq(dW2, 2); eq(dcap, 1, "q18 cap"); eq(dW1 + dW2 - dcap, 4, "q18")
    # q19: Hermitian 2x2 over R: real-linear conditions on 8 real params
    re = sp.symbols("r0:4", real=True); im = sp.symbols("i0:4", real=True)
    H = M(2, 2, [re[j] + sp.I * im[j] for j in range(4)])
    D = H - H.H
    conds = [sp.re(z) for z in D] + [sp.im(z) for z in D]
    conds = [sp.expand(sp.simplify(z)) for z in conds]
    conds = [z for z in conds if z != 0]
    A, _ = sp.linear_eq_to_matrix(conds, list(re) + list(im))
    eq(8 - A.rank(), 4, "q19")
    # q20: commutant
    A0 = M([[1, 1], [0, 1]])
    eq(dim_sub(2, lambda X: list(X * A0 - A0 * X)), 2, "q20")
    # q21
    sol = sp.solve([a + 2 * b - 1, 2 * a + b - 5, -3 * a - b - k], [a, b, k])
    eq(sol[k], -8, "q21")
    eq(M([[1, -3, 2], [2, -1, 1], [1, -8, 5]]).det(), 0, "q21 det")
    # q22 statements: 4 vectors in R^3 dependent; 3 spanning -> independent; subset counterexample
    assert M([[1, 2, 3], [4, 5, 6], [7, 8, 10], [1, 1, 1]]).rank() <= 3, "q22 s1"
    eq(M([[1, 0, 0], [2, 0, 0]]).rank(), 1, "q22 s3 dependent"); eq(M([[1, 0, 0]]).rank(), 1, "q22 s3 subset indep")
    # q23 s3: two planes in R^3 meet in a line (example)
    P1 = M([[1, 0, 0], [0, 1, 0]]); P2 = M([[0, 1, 0], [0, 0, 1]])
    eq(2 + 2 - P1.col_join(P2).rank(), 1, "q23 s3")
    # q24 match: n = 4
    eq(dim_sub(4, sym), 10); eq(dim_sub(4, skew), 6); eq(dim_sub(4, tr0), 15); eq(dim_sub(4, diag), 4, "q24")
    # q25 match
    eq(M([[1, 2, 3], [2, 4, 6], [1, 0, 1]]).rank(), 2, "q25 D")
    eq(4 - M([[1, 1, 1, 1]]).rank(), 3, "q25 C")
    # AR checks
    eq(M([[1, 2], [2, 4]]).det(), 0, "ar1")
    E = M([[1, 2], [2, 4]]); Ech = M([[1, 2], [0, 0]])
    eq(E.col_join(Ech).rank(), 1, "ar4 same row space")
    eq(E.row_join(Ech).rank(), 2, "ar4 column space changed")
    eq((M([[1, 0], [0, 0]]) + M([[0, 0], [0, 1]])).det(), 1, "ar5")
    eq((c * M([[a, b], [2 * a, 2 * b]])).det(), 0, "ar5 R")


T.write(check)
