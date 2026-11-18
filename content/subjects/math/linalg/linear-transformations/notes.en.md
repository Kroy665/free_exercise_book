# Linear Transformations

## Linear maps: definition and examples {#definition}

Let $V$ and $W$ be vector spaces over the same field $F$. A map $T : V \to W$ is a **linear transformation** (linear map, homomorphism) if

$$T(\alpha u + \beta v) = \alpha T(u) + \beta T(v) \qquad \text{for all } u, v \in V,\ \alpha, \beta \in F.$$

Equivalently, $T$ is **additive** ($T(u + v) = Tu + Tv$) and **homogeneous** ($T(\alpha v) = \alpha Tv$). A linear map from $V$ to itself is a **linear operator** on $V$. Immediate consequences:

- $T(0_V) = 0_W$ and $T(-v) = -T(v)$.
- $T\left(\sum \alpha_i v_i\right) = \sum \alpha_i T(v_i)$: linear combinations go to linear combinations.

| Map | Linear? | Reason |
|:---|:---|:---|
| $T_A(x) = Ax$, $A$ an $m\times n$ matrix, $\R^n \to \R^m$ | yes | matrix multiplication distributes |
| $D(p) = p'$ on polynomials | yes | derivative of a sum, of a scalar multiple |
| $f \mapsto \int_0^1 f(t)\,dt$ on $C[0,1]$ | yes | integral is linear |
| $A \mapsto \operatorname{tr}A$, $A \mapsto A^T$ on $M_n(F)$ | yes | entrywise linear |
| $p(x) \mapsto x\,p(x)$, $P_n \to P_{n+1}$ | yes | |
| $x \mapsto x + a$, $a \ne 0$ (translation) | **no** | $T(0) = a \ne 0$ |
| $x \mapsto x^2$ on $\R$ | **no** | $T(2) = 4 \ne 2T(1)$ |
| $(x, y) \mapsto (xy, x)$, or $x \mapsto \lvert x\rvert$ | **no** | not additive |
| $A \mapsto \det A$ on $M_n(F)$, $n \ge 2$ | **no** | $\det(2A) = 2^n\det A$ |

**A linear map is fixed by its values on a basis.** If $\{v_1, \dots, v_n\}$ is a basis of $V$ and $w_1, \dots, w_n \in W$ are **any** vectors, there is exactly one linear $T$ with $T(v_i) = w_i$, namely $T\left(\sum \alpha_i v_i\right) = \sum \alpha_i w_i$.

**Example.** $T : \R^2 \to \R^2$ is linear with $T(1, 1) = (0, 1)$ and $T(1, -1) = (2, 1)$. Write $(x, y) = \frac{x + y}{2}(1, 1) + \frac{x - y}{2}(1, -1)$. Then
$$T(x, y) = \tfrac{x + y}{2}(0, 1) + \tfrac{x - y}{2}(2, 1) = (x - y,\; x).$$

:::caution
$T(0) = 0$ is **necessary, not sufficient**: $x \mapsto x^2$ and $(x, y) \mapsto (xy, x)$ both fix $0$ and are still not linear. Also, linearity depends on the field: $z \mapsto \bar z$ is linear on $\C$ as a vector space over $\R$, but not over $\C$, since $\overline{iz} = -i\bar z$.
:::

## Kernel and range {#kernel-range}

For a linear $T : V \to W$:

- **Kernel (null space):** $\ker T = N(T) = \{v \in V : T(v) = 0\}$, a **subspace of $V$**.
- **Range (image):** $\operatorname{Im}T = R(T) = \{T(v) : v \in V\}$, a **subspace of $W$**.
- **Rank** $\rho(T) = \dim R(T)$; **nullity** $\nu(T) = \dim N(T)$ (when finite).

Both are subspaces: if $Tu = Tv = 0$ then $T(\alpha u + \beta v) = 0$; and $\alpha Tu + \beta Tv = T(\alpha u + \beta v)$ lies in the range.

**Range from a basis.** If $\{v_1, \dots, v_n\}$ spans $V$, then $R(T) = \operatorname{span}\{T v_1, \dots, T v_n\}$. So the rank is the number of independent vectors among the images of a basis.

**For a matrix map** $T_A(x) = Ax$: $N(T_A)$ is the solution space of $AX = O$, and $R(T_A)$ is the **column space** of $A$. Hence $\rho(T_A) = \rho(A)$.

**Example.** $T(x, y, z) = (x + 2y - z,\ y + z,\ x + y - 2z)$ on $\R^3$. The matrix has rows $(1, 2, -1), (0, 1, 1), (1, 1, -2)$, and $R_3 = R_1 - R_2$, so the rank is $2$.

- **Kernel:** $y = -z$, $x = -2y + z = 3z$, so $N(T) = \operatorname{span}\{(3, -1, 1)\}$, nullity $1$.
- **Range:** spanned by the columns $(1, 0, 1)$ and $(2, 1, 1)$. It is the plane $\{(a, b, c) : c = a - b\}$, read off from $R_3 = R_1 - R_2$.

:::exam-tip
To find the range quickly, reduce the **rows** of the matrix: each dependence $\sum c_i R_i = 0$ among the rows gives an equation $\sum c_i y_i = 0$ satisfied by every image vector $(y_1, \dots, y_m)$.
:::

:::caution
The kernel lives in the **domain** and the range in the **codomain**. For $T : \R^4 \to \R^3$, $N(T) \subseteq \R^4$ and $R(T) \subseteq \R^3$, so the rank is at most $3$ even though the domain has dimension $4$.
:::

## The rank–nullity theorem {#rank-nullity}

:::keyfacts
- **Rank–nullity (dimension) theorem.** If $V$ is **finite-dimensional** and $T : V \to W$ is linear ($W$ any vector space over the same field), then $R(T)$ is finite-dimensional and
  $$\rho(T) + \nu(T) = \dim V.$$
- **Matrix form.** For an $m \times n$ matrix $A$: $\rho(A) + \dim N(A) = n$, the **number of columns**.
:::

**Proof idea (examinable).** Take a basis $\{u_1, \dots, u_k\}$ of $N(T)$ and extend it to a basis $\{u_1, \dots, u_k, v_1, \dots, v_r\}$ of $V$. Then $T v_1, \dots, T v_r$ span $R(T)$, because $T u_i = 0$. They are independent: if $\sum c_j T v_j = 0$, then $\sum c_j v_j \in N(T)$, which forces all $c_j = 0$. So $\rho = r = \dim V - k$.

**Consequences.**

- $\rho(T) \le \min(\dim V, \dim W)$.
- If $T : \R^5 \to \R^3$ is onto, $\nu(T) = 5 - 3 = 2$.
- If $\dim V > \dim W$, then $\nu(T) \ge \dim V - \dim W > 0$, so $T$ is **never one-one**.
- If $\dim V < \dim W$, then $\rho(T) \le \dim V < \dim W$, so $T$ is **never onto**.

**Standard examples.**

| Map | Rank | Nullity |
|:---|:---:|:---:|
| $D : P_n \to P_n$, $p \mapsto p'$ ($P_n$ = degree $\le n$, $\dim n + 1$) | $n$ | $1$ (constants) |
| $\operatorname{tr} : M_n(\R) \to \R$ | $1$ | $n^2 - 1$ |
| $A \mapsto A - A^T$ on $M_n(\R)$ | $\frac{n(n - 1)}{2}$ (skew-symmetric) | $\frac{n(n + 1)}{2}$ (symmetric) |
| projection $(x, y, z) \mapsto (x, y, 0)$ | $2$ | $1$ |
| zero map on $V$ | $0$ | $\dim V$ |

**Example.** $T(x, y, z, w) = (x + y + z + w,\ x + 2y + 3z + 4w,\ 2x + 3y + 4z + 5w)$. The third row is the sum of the first two, and the first two are independent, so $\rho = 2$ and $\nu = 4 - 2 = 2$.

:::caution
The theorem needs $V$ finite-dimensional, and the sum is $\dim V$ (the **domain**), not $\dim W$. A common slip is to write $\rho + \nu = \dim W$, or to use the number of **rows** of $A$.
:::

## One-one, onto, inverse and isomorphism {#injective-surjective}

For linear $T : V \to W$:

- **$T$ is one-one (injective) $\iff N(T) = \{0\}$.** If $Tu = Tv$ then $T(u - v) = 0$; conversely a non-zero kernel vector and $0$ have the same image.
- $T$ is one-one $\iff$ $T$ maps every linearly independent set to a linearly independent set.
- **$T$ is onto (surjective) $\iff R(T) = W$**; in finite dimensions, $\iff \rho(T) = \dim W$.

:::keyfacts
- If $\dim V = \dim W = n < \infty$, then for linear $T : V \to W$
  $$T \text{ one-one} \iff T \text{ onto} \iff T \text{ bijective} \iff \rho(T) = n \iff \nu(T) = 0.$$
- For an operator $T$ on $F^n$ with matrix $A$, each of these is equivalent to $\det A \ne 0$.
:::

This follows at once from rank–nullity: $\nu = 0 \iff \rho = n$.

**Infinite dimensions break this.** On the space $P$ of all real polynomials, $D(p) = p'$ is onto but not one-one, and $M(p) = x\,p(x)$ is one-one but not onto.

**Inverse.** A linear $T$ that is bijective is called **invertible** (non-singular). Its inverse map $T^{-1} : W \to V$ is **automatically linear**. Some books call $T$ non-singular when $N(T) = \{0\}$; for operators on a finite-dimensional space the two meanings agree. If $T$ has matrix $A$ in some bases, $T^{-1}$ has matrix $A^{-1}$ in the reversed bases.

**Example.** $T(x, y) = (2x + y,\ 3x + 2y)$ has matrix $A = \begin{pmatrix}2 & 1\\ 3 & 2\end{pmatrix}$, $\det A = 1$, so
$$A^{-1} = \begin{pmatrix}2 & -1\\ -3 & 2\end{pmatrix}, \qquad T^{-1}(x, y) = (2x - y,\ -3x + 2y).$$
Check: $T(2x - y, -3x + 2y) = (4x - 2y - 3x + 2y,\ 6x - 3y - 6x + 4y) = (x, y)$.

**Isomorphism.** A bijective linear map is an **isomorphism**; then $V \cong W$.

- Two finite-dimensional spaces over the same field are isomorphic **iff they have the same dimension**.
- If $B = (v_1, \dots, v_n)$ is an ordered basis of $V$, the **coordinate map** $v = \sum \alpha_i v_i \mapsto (\alpha_1, \dots, \alpha_n)$ is an isomorphism $V \to F^n$. So every $n$-dimensional space is a copy of $F^n$.
- Examples: $P_3 \cong \R^4$; $M_{2}(\R) \cong \R^4$; $M_{m\times n}(F) \cong F^{mn}$; $\C \cong \R^2$ over $\R$.
- An isomorphism carries bases to bases and subspaces to subspaces of the same dimension.

:::caution
"Injective $\iff$ surjective" needs **equal finite dimensions**. For $T : \R^2 \to \R^3$, $T(x, y) = (x, y, 0)$ is one-one but not onto.
:::

## The matrix of a linear transformation {#matrix-representation}

Let $B = (v_1, \dots, v_n)$ be an ordered basis of $V$ and $C = (w_1, \dots, w_m)$ an ordered basis of $W$. Write the image of each basis vector of $V$ in terms of $C$:

$$T(v_j) = \sum_{i=1}^{m} a_{ij}\, w_i, \qquad j = 1, \dots, n.$$

The $m \times n$ matrix $[T]_{B}^{C} = (a_{ij})$ is the **matrix of $T$ relative to $B$ and $C$**.

**Convention used here:** the **$j$th column** holds the $C$-coordinates of $T(v_j)$. Then
$$[T(v)]_C = [T]_B^C\,[v]_B.$$
A few books write these coordinates as **rows** and get the transpose; always check which convention a question uses.

**Order matters.** Reordering a basis permutes the columns (or rows) of the matrix.

**Examples.**

1. $T(x, y) = (2x + 3y,\ x - y)$ in the standard basis: $T(e_1) = (2, 1)$, $T(e_2) = (3, -1)$, so $[T] = \begin{pmatrix}2 & 3\\ 1 & -1\end{pmatrix}$, the coefficient matrix read row by row.
2. $D$ on $P_2$ with basis $(1, x, x^2)$: $D1 = 0$, $Dx = 1$, $Dx^2 = 2x$, so
$$[D] = \begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 2\\ 0 & 0 & 0\end{pmatrix}.$$
3. $T : \R^3 \to \R^2$, $T(x, y, z) = (x + y,\ y + z)$, with $B = ((1,0,0), (1,1,0), (1,1,1))$ and $C = ((1, 0), (1, 1))$. The images are $(1, 0), (2, 1), (2, 2)$. Since $(a, b) = (a - b)(1, 0) + b(1, 1)$, their $C$-coordinates are $(1, 0), (1, 1), (0, 2)$. So
$$[T]_B^C = \begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 2\end{pmatrix}.$$

**Algebra of matrices.** With bases fixed:

- $[S + T] = [S] + [T]$ and $[\alpha T] = \alpha[T]$.
- **Composition ↔ product:** for $T : U \to V$ and $S : V \to W$, $[S \circ T]_{B}^{D} = [S]_{C}^{D}\,[T]_{B}^{C}$. Note the order: $S$ is applied second but written first.
- $T$ is invertible $\iff$ $[T]$ is square and non-singular, and then $[T^{-1}] = [T]^{-1}$.
- $\rho(T) = \rho([T])$ for **any** choice of bases.
- $T \mapsto [T]$ is an isomorphism $L(V, W) \cong M_{m\times n}(F)$, so $\dim L(V, W) = mn$.

:::exam-tip
When the bases are not standard, two slips are common: writing the images themselves as columns instead of their **coordinates**, and writing the coordinates as rows. Check one column by reconstructing $T(v_j)$ from it.
:::

## Change of basis and similar matrices {#change-of-basis}

Let $B = (v_1, \dots, v_n)$ and $B' = (v'_1, \dots, v'_n)$ be ordered bases of $V$. The **transition matrix** $P$ has as its $j$th column the $B$-coordinates of $v'_j$. It is non-singular, and
$$[v]_B = P\,[v]_{B'}.$$

:::keyfacts
- For an operator $T$ on $V$: $\;[T]_{B'} = P^{-1}\,[T]_B\,P$.
- For $T : V \to W$, with transition matrices $P$ on $V$ and $Q$ on $W$: $\;[T]_{B'}^{C'} = Q^{-1}\,[T]_B^C\,P$. Matrices related this way are **equivalent**: they have the same rank.
- Square matrices $A$ and $A'$ are **similar** if $A' = P^{-1}AP$ for some non-singular $P$. **Two matrices represent the same operator in two bases iff they are similar.**
:::

**Similarity invariants** (they belong to the operator, not to the basis): determinant, trace, rank, nullity, characteristic polynomial, eigenvalues, minimal polynomial. So $\det T$ and $\operatorname{tr} T$ are well defined.

**Not invariant:** the individual entries, symmetry, the diagonal entries themselves, the first column.

**Example.** $T(x, y) = (2x + y,\ x)$, $B'= ((1, 0), (1, 1))$. In the standard basis $A = \begin{pmatrix}2 & 1\\ 1 & 0\end{pmatrix}$, and $P = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$.

Directly: $T(1, 0) = (2, 1) = 1\cdot(1, 0) + 1\cdot(1, 1)$ and $T(1, 1) = (3, 1) = 2\cdot(1, 0) + 1\cdot(1, 1)$. So
$$[T]_{B'} = \begin{pmatrix}1 & 2\\ 1 & 1\end{pmatrix} = P^{-1}AP.$$
Check: both matrices have trace $2$ and determinant $-1$.

:::caution
Same trace, determinant and rank do **not** make two matrices similar. $I_2$ and $\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ agree in all three, but the only matrix similar to $I$ is $I$ itself, since $P^{-1}IP = I$.
:::

:::exam-tip
Use the invariants as a quick filter on options: an option for $[T]_{B'}$ with the wrong trace or determinant can be crossed out without computing $P^{-1}$.
:::

## Sylvester's law of nullity {#sylvester}

:::keyfacts
- **Sylvester's law of nullity.** For $n \times n$ matrices $A$ and $B$ (nullity $N(\cdot) = n - \rho(\cdot)$):
  $$\max\{N(A), N(B)\} \;\le\; N(AB) \;\le\; N(A) + N(B).$$
- **Rank form (Sylvester's inequality).** If $A$ is $m \times n$ and $B$ is $n \times p$:
  $$\rho(A) + \rho(B) - n \;\le\; \rho(AB) \;\le\; \min\{\rho(A), \rho(B)\}.$$
- **For maps.** If $T : U \to V$ and $S : V \to W$ are linear with $U, V$ finite-dimensional, then $\nu(S \circ T) \le \nu(S) + \nu(T)$.
:::

**Proof idea.** $N(T) \subseteq N(ST)$, and $T$ maps $N(ST)$ into $N(S)$. Apply rank–nullity to the restriction $T : N(ST) \to N(S)$, whose kernel is $N(T)$:
$$\nu(ST) = \nu(T) + \dim T\big(N(ST)\big) \le \nu(T) + \nu(S).$$

The upper bound $\rho(AB) \le \min$ holds because $R(AB) \subseteq R(A)$ and $AB$ is "$B$ followed by $A$".

**Consequences.**

- If $A$ (or $B$) is non-singular, $\rho(AB) = \rho(B)$ (or $\rho(A)$): multiplying by an invertible matrix keeps the rank.
- If $A$ is $n \times n$ and $A^2 = O$, then $0 \ge 2\rho(A) - n$, so $\rho(A) \le n/2$. For example, a nilpotent $3 \times 3$ matrix with $A^2 = O$ has rank at most $1$.
- For $4 \times 4$ matrices of ranks $3$ and $2$, $\rho(AB) \ge 3 + 2 - 4 = 1$, so $AB \ne O$.
- If $AB = O$ ($n \times n$), then $\rho(A) + \rho(B) \le n$.

**Example.** $A$, $B$ are $5 \times 5$ with $N(A) = 2$, $N(B) = 1$. Then $2 \le N(AB) \le 3$, so $\rho(AB) = 5 - N(AB)$ is $2$ or $3$. In rank form: $\rho(A) = 3$, $\rho(B) = 4$, and $3 + 4 - 5 = 2 \le \rho(AB) \le 3$.

:::caution
$\rho(AB)$ and $\rho(BA)$ can differ. With $A = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$, $B = \begin{pmatrix}1 & 0\\ 0 & 0\end{pmatrix}$: $AB = O$ but $BA = A \ne O$. Also, there is **no** law $N(A + B) \le N(A) + N(B)$: take $B = -A$ with $A$ non-singular.
:::

## Quick checks and traps {#exam-tips}

- **Linearity test:** first check $T(0) = 0$. If it fails (translation), the map is not linear. If it holds, look for squares, products of coordinates, $\lvert\cdot\rvert$, constants or $\det$.
- **Rank–nullity:** $\rho + \nu = \dim(\text{domain})$. For a matrix, that is the number of **columns**.
- **Dimension filter:** if $\dim V > \dim W$, $T$ is never one-one; if $\dim V < \dim W$, $T$ is never onto.
- **Square case:** for an operator on a finite-dimensional space, one-one $\iff$ onto $\iff$ $\det[T] \ne 0$.
- **Basis-defined maps:** to find $T(v)$, write $v$ in the given basis first. To test invertibility, check whether the images of the basis are independent.
- **Matrix of $T$:** the $j$th column is the coordinate vector of $T(v_j)$, in the codomain basis. $[S\circ T] = [S][T]$.
- **Similar matrices** share trace, determinant, rank and eigenvalues. Equal invariants do not prove similarity.
- **Sylvester:** $\rho(A) + \rho(B) - n \le \rho(AB) \le \min\{\rho(A), \rho(B)\}$; $A^2 = O \Rightarrow \rho(A) \le n/2$.
- **Isomorphism:** $V \cong W \iff \dim V = \dim W$ (finite-dimensional, same field). $\dim L(V, W) = \dim V\cdot\dim W$.
