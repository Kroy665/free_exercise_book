# Matrices, Inverse and Rank

## Matrix algebra {#matrix-algebra}

An $m\times n$ **matrix** over a field $F$ ($\R$ or $\C$) is a rectangular array $A = [a_{ij}]$ with $m$ rows and $n$ columns. Write $M_{m\times n}(F)$ for the set of all of them.

- **Equality:** $A = B$ iff they have the **same order** and $a_{ij} = b_{ij}$ for all $i, j$.
- **Sum:** $A + B = [a_{ij} + b_{ij}]$, defined only for the same order. Addition is commutative and associative, with zero $O$ and negative $-A$.
- **Scalar multiple:** $kA = [k\,a_{ij}]$.
- **Product:** if $A$ is $m\times n$ and $B$ is $n\times p$, then $AB$ is $m\times p$ with
  $$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj}.$$

The product is **associative** and **distributive** over addition, and $I_m A = A = A I_n$. But it is **not commutative**:

- $BA$ may be undefined ($A$ is $2\times 3$, $B$ is $3\times 4$), or of a different order ($A$ is $2\times3$, $B$ is $3\times 2$).
- Even for square matrices, $AB \ne BA$ in general.

**Zero divisors.** $AB = O$ does not force $A = O$ or $B = O$:

$$A = \begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix},\quad B = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix}:\qquad AB = O,\quad BA = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix} \ne O.$$

So $AB = AC$ does **not** give $B = C$ unless $A$ is non-singular. Also $(A + B)^2 = A^2 + AB + BA + B^2$, which equals $A^2 + 2AB + B^2$ only when $AB = BA$.

**Special square matrices** (order $n$):

| Name | Condition |
|:---|:---|
| diagonal | $a_{ij} = 0$ for $i \ne j$ |
| scalar | $A = kI$ (commutes with every $n\times n$ matrix) |
| upper / lower triangular | $a_{ij} = 0$ for $i > j$ / for $i < j$ |
| idempotent | $A^2 = A$ |
| nilpotent (index $k$) | $A^k = O$, $A^{k-1} \ne O$ |
| involutory | $A^2 = I$ |

Example: $\begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$ is nilpotent of index 2, and $\begin{pmatrix}1 & 1\\ 0 & 0\end{pmatrix}$ is idempotent.

**Trace:** $\operatorname{tr} A = \sum a_{ii}$. It is linear, and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ even when $AB \ne BA$.

:::caution
$\det(A + B) \ne \det A + \det B$ in general, but $\det(AB) = \det A\,\det B$ and $\det(kA) = k^n\det A$ for $n\times n$ matrices.
:::

## Transpose, symmetric and Hermitian matrices {#transpose-symmetric}

The **transpose** $A^T$ (also $A'$) of an $m\times n$ matrix is the $n\times m$ matrix with $(A^T)_{ij} = a_{ji}$.

$$(A^T)^T = A,\qquad (A + B)^T = A^T + B^T,\qquad (kA)^T = kA^T,\qquad (AB)^T = B^TA^T.$$

The **reversal law** extends: $(ABC)^T = C^TB^TA^T$.

A square matrix is **symmetric** if $A^T = A$ and **skew-symmetric** if $A^T = -A$.

- In a skew-symmetric matrix $a_{ii} = -a_{ii}$, so **every diagonal entry is $0$** (over $\R$ or $\C$).
- A skew-symmetric matrix of **odd order** has determinant $0$, since $\det A = \det(-A^T) = (-1)^n\det A$.
- For any $A$ (any order), $AA^T$ and $A^TA$ are symmetric.
- If $A, B$ are symmetric, $AB$ is symmetric iff $AB = BA$.
- If $A$ is skew-symmetric, $A^k$ is symmetric for even $k$ and skew-symmetric for odd $k$.

**Decomposition theorem.** Every square matrix is **uniquely** the sum of a symmetric and a skew-symmetric matrix:

$$A = \underbrace{\tfrac12(A + A^T)}_{P,\ \text{symmetric}} + \underbrace{\tfrac12(A - A^T)}_{Q,\ \text{skew-symmetric}}.$$

Uniqueness: if $A = P + Q$, then $A^T = P - Q$, which forces the formulas above.

Example: for $A = \begin{pmatrix}1 & 2\\ 4 & 3\end{pmatrix}$, $P = \begin{pmatrix}1 & 3\\ 3 & 3\end{pmatrix}$ and $Q = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$.

**Complex matrices.** $\bar A = [\bar a_{ij}]$, and the **conjugate transpose** is $A^* = \bar A^{\,T}$ (also written $A^\theta$). It obeys $(AB)^* = B^*A^*$.

| Type | Condition | Diagonal entries |
|:---|:---|:---|
| Hermitian | $A^* = A$ | real |
| skew-Hermitian | $A^* = -A$ | purely imaginary or $0$ |

A real Hermitian matrix is symmetric; a real skew-Hermitian matrix is skew-symmetric. $A$ is Hermitian iff $iA$ is skew-Hermitian. Every square complex matrix is uniquely $H + iK$ with $H = \frac12(A + A^*)$ and $K = \frac1{2i}(A - A^*)$ both Hermitian.

:::exam-tip
For "find $x$ so that $A$ is Hermitian", just set $a_{ji} = \overline{a_{ij}}$: in $\begin{pmatrix}2 & 3 + i\\ x & 5\end{pmatrix}$, $x = 3 - i$.
:::

## Adjoint and inverse {#adjoint-inverse}

Let $A$ be $n\times n$ and $C_{ij}$ the cofactor of $a_{ij}$. The **adjoint** (adjugate) is the **transpose** of the cofactor matrix: $\operatorname{adj} A = [C_{ji}]$.

**Fundamental identity.** By expansion along a row and the "alien cofactor" rule,

$$A\,(\operatorname{adj}A) = (\operatorname{adj}A)\,A = (\det A)\,I_n.$$

$A$ is **singular** if $\det A = 0$ and **non-singular** otherwise. A square $A$ has an inverse $B$ ($AB = BA = I$) **iff** $\det A \ne 0$, and then

$$A^{-1} = \frac{1}{\det A}\operatorname{adj}A, \qquad \begin{pmatrix}a & b\\ c & d\end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d & -b\\ -c & a\end{pmatrix}.$$

The inverse is unique. For square matrices, $AB = I$ alone already implies $BA = I$.

**Rules** (non-singular $A, B$ of order $n$, scalar $k \ne 0$):

| Inverse | Adjoint ($n \ge 2$) |
|:---|:---|
| $(AB)^{-1} = B^{-1}A^{-1}$ | $\operatorname{adj}(AB) = \operatorname{adj}B\,\operatorname{adj}A$ |
| $(A^T)^{-1} = (A^{-1})^T$ | $\operatorname{adj}(A^T) = (\operatorname{adj}A)^T$ |
| $(kA)^{-1} = k^{-1}A^{-1}$ | $\operatorname{adj}(kA) = k^{n-1}\operatorname{adj}A$ |
| $\det(A^{-1}) = 1/\det A$ | $\det(\operatorname{adj}A) = (\det A)^{n-1}$ |
| $(A^{-1})^{-1} = A$ | $\operatorname{adj}(\operatorname{adj}A) = (\det A)^{n-2}A$ |

The adjoint formulas in the right column hold for **all** $n\times n$ matrices, singular or not.

**Example.** $A = \begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}$ has $\det A = -24 + 40 - 15 = 1$. The cofactors give

$$A^{-1} = \operatorname{adj}A = \begin{pmatrix}-24 & 18 & 5\\ 20 & -15 & -4\\ -5 & 4 & 1\end{pmatrix}.$$

**Inverse from a polynomial identity.** If $A^2 - A + I = O$, then $A(I - A) = I$, so $A^{-1} = I - A$. (Cayley–Hamilton, a later topic, produces such identities.)

:::caution
The adjoint is the transpose of the cofactor matrix. Forgetting the transpose puts $C_{ij}$ in position $(i, j)$ and gives a wrong inverse for every non-symmetric $A$.
:::

## Elementary operations and elementary matrices {#elementary-operations}

The three **elementary row operations** are:

1. $R_i \leftrightarrow R_j$: interchange two rows;
2. $R_i \to kR_i$, with $k \ne 0$: multiply a row by a non-zero scalar;
3. $R_i \to R_i + kR_j$ ($i \ne j$): add a multiple of another row.

Column operations $C_i \leftrightarrow C_j$, $C_i \to kC_i$, $C_i \to C_i + kC_j$ are defined the same way.

An **elementary matrix** is obtained from $I_n$ by **one** elementary operation. The key facts:

- A row operation on $A$ equals **pre-multiplication** $EA$, where $E$ is the result of the same operation on $I_m$.
- A column operation equals **post-multiplication** $AE$, with $E$ from $I_n$.
- Every elementary matrix is non-singular, and its inverse is elementary of the same type:

| $E$ from | $\det E$ | $E^{-1}$ from |
|:---|:---:|:---|
| $R_i \leftrightarrow R_j$ | $-1$ | $R_i \leftrightarrow R_j$ |
| $R_i \to kR_i$ | $k$ | $R_i \to \frac1k R_i$ |
| $R_i \to R_i + kR_j$ | $1$ | $R_i \to R_i - kR_j$ |

For example, $E = \begin{pmatrix}1 & 0 & 2\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$ (from $R_1 \to R_1 + 2R_3$) has $E^{-1} = \begin{pmatrix}1 & 0 & -2\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$.

**Theorem.** A square matrix is non-singular iff it is a product of elementary matrices, iff it can be reduced to $I$ by row operations alone.

**Inverse by Gauss–Jordan.** Row-reduce $[A \mid I]$. If $A$ reaches $I$, the right block is $A^{-1}$; if a zero row appears on the left, $A$ is singular. Reason: if $E_k\cdots E_1A = I$, then $E_k\cdots E_1 = A^{-1}$ and the same product turns $I$ into $A^{-1}$.

$$\left[\begin{array}{cc|cc}2 & 1 & 1 & 0\\ 5 & 3 & 0 & 1\end{array}\right] \to \left[\begin{array}{cc|cc}1 & 0 & 3 & -1\\ 0 & 1 & -5 & 2\end{array}\right],\quad\text{so}\quad \begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}^{-1} = \begin{pmatrix}3 & -1\\ -5 & 2\end{pmatrix}.$$

:::caution
For Gauss–Jordan use **only row operations** (or only column operations on $\begin{bmatrix}A\\ I\end{bmatrix}$). Mixing rows and columns breaks the argument.
:::

## Rank: minors and echelon form {#rank}

**By minors.** The **rank** $\rho(A)$ of a non-zero matrix is the largest $r$ such that $A$ has a non-zero minor of order $r$; $\rho(O) = 0$. Equivalently, $\rho(A) = r$ iff

- some $r\times r$ minor is non-zero, and
- every $(r+1)\times(r+1)$ minor is zero (then all larger minors vanish too).

For an $m\times n$ matrix, $\rho(A) \le \min(m, n)$. A square $A$ of order $n$ is non-singular iff $\rho(A) = n$.

**By echelon form (sweep-out).** A matrix is in **row echelon form** when the zero rows are at the bottom and the leading (first non-zero) entry of each row lies to the right of the leading entry of the row above. Elementary operations do not change rank, so

$$\rho(A) = \text{number of non-zero rows in any row echelon form of } A.$$

The **sweep-out process** uses a pivot to clear the column below it (and above it, for the reduced form), then moves to the next row and column.

**Example.**
$$\begin{pmatrix}1 & 2 & -1 & 3\\ 2 & 4 & 1 & -2\\ 3 & 6 & 3 & -7\end{pmatrix} \xrightarrow[R_3 - 3R_1]{R_2 - 2R_1} \begin{pmatrix}1 & 2 & -1 & 3\\ 0 & 0 & 3 & -8\\ 0 & 0 & 6 & -16\end{pmatrix} \xrightarrow{R_3 - 2R_2} \begin{pmatrix}1 & 2 & -1 & 3\\ 0 & 0 & 3 & -8\\ 0 & 0 & 0 & 0\end{pmatrix}.$$
Two non-zero rows, so the rank is $2$.

**A parameter example.** $\det\begin{pmatrix}k & 1 & 1\\ 1 & k & 1\\ 1 & 1 & k\end{pmatrix} = (k + 2)(k - 1)^2$. The rank is $3$ for $k \ne 1, -2$; $1$ for $k = 1$ (all rows equal); $2$ for $k = -2$ (a $2\times 2$ minor such as $k^2 - 1 = 3$ is non-zero).

:::exam-tip
Rank is also the maximum number of linearly independent rows (or columns). Row rank = column rank is proved in the vector-space topic; here it shows up as $\rho(A^T) = \rho(A)$, since minors of $A^T$ are the minors of $A$.
:::

## Properties of rank {#rank-properties}

Let $A$ be $m\times n$.

1. $\rho(A^T) = \rho(A)$, and $\rho(\bar A) = \rho(A^*) = \rho(A)$.
2. $\rho(kA) = \rho(A)$ for $k \ne 0$.
3. $\rho(AB) \le \min\{\rho(A), \rho(B)\}$, whenever $AB$ is defined.
4. If $P$ ($m\times m$) and $Q$ ($n\times n$) are non-singular, then $\rho(PA) = \rho(AQ) = \rho(PAQ) = \rho(A)$.
5. $\rho(A + B) \le \rho(A) + \rho(B)$ for matrices of the same order.
6. For a real matrix, $\rho(A^TA) = \rho(AA^T) = \rho(A)$.

Property 3 has a quick consequence. If $A$ is $3\times 2$ and $B$ is $2\times 3$, then $AB$ is $3\times 3$ with $\rho(AB) \le 2$, so $\det(AB) = 0$ **always**.

**Rank of the adjoint** ($A$ of order $n \ge 2$):

$$\rho(\operatorname{adj}A) = \begin{cases} n, & \rho(A) = n,\\ 1, & \rho(A) = n - 1,\\ 0, & \rho(A) \le n - 2.\end{cases}$$

Reason: if $\rho(A) = n - 1$, then $A\operatorname{adj}A = O$ forces $\rho(\operatorname{adj}A) \le 1$ (via the lower bound $\rho(A) + \rho(\operatorname{adj}A) - n \le \rho(A\operatorname{adj}A)$, Sylvester's inequality from the linear-transformations topic), and some $(n-1)$-minor is non-zero, so $\operatorname{adj}A \ne O$. If $\rho(A) \le n - 2$, every cofactor is $0$.

**Rank one.** $\rho(A) = 1$ iff $A = uv^T$ for non-zero column vectors $u, v$, that is, iff all rows are multiples of one non-zero row. For example, $\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 3 & 6 & 9\end{pmatrix}$ has rank $1$.

:::caution
Rank is **not** additive: $\rho(A + B)$ can be smaller than $\rho(A) + \rho(B)$. With $B = -A \ne O$, $\rho(A + B) = 0$. Also $\rho(AB)$ and $\rho(BA)$ may differ: in the zero-divisor example of the first section, $\rho(AB) = 0$ but $\rho(BA) = 1$.
:::

:::exam-tip
Rank checks in one line: a zero row or column, two proportional rows, or a row equal to the sum of two others all lower the rank. Look for these before computing any determinant.
:::

## Normal form, equivalence, congruence and orthogonal matrices {#normal-form}

**Normal form.** Every non-zero $m\times n$ matrix $A$ of rank $r$ can be reduced, by elementary row **and** column operations, to

$$N = \begin{bmatrix} I_r & O\\ O & O\end{bmatrix}_{m\times n}$$

(also $[I_r\ \ O]$, $\begin{bmatrix}I_r\\ O\end{bmatrix}$ or $I_r$ when there are no zero blocks). In matrix form: there exist non-singular $P$ ($m\times m$) and $Q$ ($n\times n$), products of elementary matrices, with $PAQ = N$. The number $r$ is unique and equals $\rho(A)$.

**Equivalence.** $B$ is **equivalent** to $A$ ($A \sim B$) if $B = PAQ$ for some non-singular $P, Q$, that is, if $B$ comes from $A$ by elementary operations. This is an equivalence relation, and

$$A \sim B \iff A, B \text{ have the same order and the same rank}.$$

So the normal forms $N_r$, $r = 0, 1, \dots, \min(m, n)$, list one representative of each class.

**Congruence** (brief). Square $B$ is **congruent** to $A$ if $B = P^TAP$ for some non-singular $P$. In practice, apply an elementary row operation and then the **same** column operation. Congruence implies equivalence, so congruent matrices have the **same rank**. It also preserves symmetry and skew-symmetry: $(P^TAP)^T = P^TA^TP$. The determinant is **not** preserved: $\det(P^TAP) = (\det P)^2\det A$, which keeps only its sign over $\R$. Every real symmetric matrix is congruent to a diagonal matrix; the reduction to $\operatorname{diag}(I_p, -I_q, O)$ is the quadratic-forms topic.

**Orthogonal matrices** (brief). A real square $A$ is **orthogonal** if $AA^T = A^TA = I$, that is, $A^{-1} = A^T$.

- The rows (and the columns) form an orthonormal set.
- $\det A = \pm 1$ (from $\det A^T\det A = 1$).
- Products, inverses and transposes of orthogonal matrices are orthogonal.
- In $2\times 2$: $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ (rotation, $\det = 1$) or $\begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix}$ (reflection, $\det = -1$).

The complex analogue is a **unitary** matrix: $AA^* = I$.

**Example.** $A = \frac13\begin{pmatrix}1 & 2 & 2\\ 2 & 1 & -2\\ x & 2 & -1\end{pmatrix}$ is orthogonal only if row 3 is orthogonal to rows 1 and 2: $x + 4 - 2 = 0$ and $2x + 2 + 2 = 0$, so $x = -2$. Then row 3 has length $\frac13\sqrt{4 + 4 + 1} = 1$.

:::caution
$\det A = \pm1$ does **not** make $A$ orthogonal: $\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ has determinant $1$ but is not orthogonal.
:::

## Quick checks and traps {#exam-tips}

- **Order check first:** $(m\times n)(n\times p) = m\times p$. If the inner sizes differ, the product is undefined.
- **Reversal laws:** $(AB)^T = B^TA^T$, $(AB)^{-1} = B^{-1}A^{-1}$, $\operatorname{adj}(AB) = \operatorname{adj}B\,\operatorname{adj}A$. The option with the original order is the standard trap.
- **Adjoint numbers** for order $n$: $\det(\operatorname{adj}A) = \lvert A\rvert^{n-1}$, $\operatorname{adj}\operatorname{adj}A = \lvert A\rvert^{n-2}A$, $\det(\operatorname{adj}\operatorname{adj}A) = \lvert A\rvert^{(n-1)^2}$. For $n = 3$ and $\lvert A\rvert = 5$: $25$, $5A$, $625$.
- **$A\,\operatorname{adj}A$** is always $(\det A)I$; for a triangular $A$, $\det A$ is the product of the diagonal.
- **Determinant scaling:** $\det(kA) = k^n\det A$, not $k\det A$.
- **Rank traps:** the rank is at most the smaller dimension; $\rho(AB) \le \min$; a product $(n\times k)(k\times n)$ with $k < n$ is singular.
- **Rank of a symmetric pattern** like $\begin{pmatrix}k & 1 & 1\\ 1 & k & 1\\ 1 & 1 & k\end{pmatrix}$: factor the determinant, then test each root separately.
- **Elementary matrices:** row operation ↔ pre-multiply; column operation ↔ post-multiply.
- **Equivalent** = same order and same rank. **Congruent** ⇒ same rank, but not the same determinant.
- **Skew-symmetric:** zero diagonal; odd order ⇒ singular. **Hermitian:** real diagonal.
- **Orthogonal:** $A^{-1} = A^T$, $\det = \pm1$; to find a missing entry, use row orthogonality.
