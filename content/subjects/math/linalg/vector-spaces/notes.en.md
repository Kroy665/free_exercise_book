# Vector Spaces

## Vector spaces: axioms and examples {#axioms}

Let $F$ be a field (here $\R$ or $\C$, sometimes $\Q$). A **vector space over $F$** is a set $V$ with an addition $V \times V \to V$ and a scalar multiplication $F \times V \to V$ such that, for all $u, v, w \in V$ and $a, b \in F$:

| Addition: $(V, +)$ is an abelian group | Scalar multiplication |
|:---|:---|
| $u + v = v + u$, $\;(u + v) + w = u + (v + w)$ | $a(u + v) = au + av$ |
| a zero vector $0$ with $v + 0 = v$ | $(a + b)v = av + bv$ |
| each $v$ has a negative $-v$ | $(ab)v = a(bv)$ |
| | $1\cdot v = v$ |

Consequences: $0\cdot v = 0$, $a\cdot 0 = 0$, $(-1)v = -v$, and $av = 0 \Rightarrow a = 0$ or $v = 0$.

**Standard examples.**

| Space | Elements | Dimension |
|:---|:---|:---|
| $\R^n$ over $\R$ | $n$-tuples, componentwise operations | $n$ |
| $\C^n$ over $\C$ | complex $n$-tuples | $n$ |
| $\C^n$ over $\R$ | the same set, only real scalars allowed | $2n$ |
| $P_n$ (or $\R_n[x]$) | real polynomials of degree $\le n$, with $0$ | $n + 1$ |
| $\R[x]$ | all real polynomials | infinite |
| $M_{m\times n}(\R)$ | real $m\times n$ matrices | $mn$ |
| $C[a, b]$ | continuous real functions on $[a, b]$ | infinite |
| $\R$ over $\Q$ | real numbers, rational scalars | infinite |

The **field matters**. $\C$ over $\C$ has basis $\{1\}$, but $\C$ over $\R$ needs $\{1, i\}$, because $i$ is not a real multiple of $1$. And $\R$ is **not** a vector space over $\C$: $i\cdot 1 = i \notin \R$, so scalar multiplication is not closed.

**Non-examples** (check closure and the zero vector first):

- $\{(x, y) : y = x + 1\}$: no zero vector.
- Polynomials of degree **exactly** $n$: $x^n + (-x^n + 1) = 1$ has degree $0$, and $0$ itself has no degree $n$.
- $\R^2$ with the usual addition but $a(x, y) = (ax, 0)$: then $1\cdot(1, 1) = (1, 0) \ne (1, 1)$, so the axiom $1\cdot v = v$ fails.

:::caution
When an exam gives a "strange" operation, test the axiom that is easiest to break: usually $1\cdot v = v$ or $(a + b)v = av + bv$. One failure is enough.
:::

## Subspaces: the one-step test {#subspaces}

A **subspace** of $V$ is a subset $W$ that is itself a vector space over $F$ under the same operations. The axioms of associativity, distributivity and so on are inherited, so only closure needs checking.

:::keyfacts
- **One-step test.** A subset $W \subseteq V$ is a subspace iff $W \ne \varnothing$ and $au + bv \in W$ for all $u, v \in W$ and $a, b \in F$.
- Equivalent form: $W \ne \varnothing$ and $au + v \in W$ for all $u, v \in W$, $a \in F$.
- Every subspace contains $0$. If $0 \notin W$, $W$ is not a subspace.
:::

**Subspaces of $\R^n$.** The solution set of a **homogeneous** linear system $AX = 0$ is a subspace (the null space of $A$). A non-homogeneous system $AX = b$, $b \ne 0$, never gives a subspace, since $0$ fails.

The subspaces of $\R^2$ are $\{0\}$, the lines through the origin and $\R^2$. The subspaces of $\R^3$ are $\{0\}$, lines and planes through the origin, and $\R^3$.

**Typical tests in $\R^3$:**

| Set | Subspace? | Why |
|:---|:---|:---|
| $x + 2y - z = 0$ | yes | homogeneous linear |
| $x + y + z = 1$ | no | $0 \notin W$ |
| $xy = 0$ (with any $z$) | no | $(1,0,0) + (0,1,0) = (1,1,0) \notin W$ |
| $x \ge 0$ | no | $(-1)(1,0,0) \notin W$ |
| $x = y = 2z$ | yes | a line through $0$ |
| $x^2 = y^2$ | no | contains $(1,1,0)$ and $(1,-1,0)$, not their sum |
| $x \in \Q$ | no (over $\R$) | $\sqrt2\,(1,0,0) \notin W$ |

**Subspaces of matrix and function spaces.** In $M_n(\R)$: symmetric, skew-symmetric, diagonal, upper triangular and trace-zero matrices form subspaces. Invertible matrices do not ($0$ is missing), and singular matrices do not either: $\operatorname{diag}(1, 0) + \operatorname{diag}(0, 1) = I$. In $P_n$: $\{p : p(1) = 0\}$ is a subspace, $\{p : p(1) = 1\}$ is not.

:::exam-tip
A condition gives a subspace when it is **linear and homogeneous** in the coordinates. Any constant term, product of coordinates, square, inequality or "or" usually kills it. To disprove, give one explicit failure of closure.
:::

## Span and linear independence {#span-independence}

A **linear combination** of $v_1, \dots, v_k$ is $a_1v_1 + \cdots + a_kv_k$ with $a_i \in F$. The **span** $L(S)$ of a set $S$ is the set of all finite linear combinations of its vectors; $L(\varnothing) = \{0\}$. It is the **smallest subspace containing $S$**.

$v_1, \dots, v_k$ are **linearly dependent** if $a_1v_1 + \cdots + a_kv_k = 0$ for some scalars not all zero; otherwise they are **independent** (only the trivial combination gives $0$).

Basic facts:

- Any set containing $0$ is dependent ($1\cdot 0 = 0$).
- A single vector $\{v\}$ is independent iff $v \ne 0$.
- Two vectors are dependent iff one is a scalar multiple of the other.
- A set is dependent iff some vector is a combination of the **others** (in an ordered list, of the preceding ones).
- A superset of a dependent set is dependent; a subset of an independent set is independent. The converses fail.

**Testing in $\R^n$.** Put the vectors as the rows (or columns) of a matrix $A$. Then

$$\{v_1, \dots, v_k\} \text{ independent} \iff \rho(A) = k, \qquad \dim L(v_1, \dots, v_k) = \rho(A).$$

For $n$ vectors in $\R^n$ the matrix is square: independent $\iff \det A \ne 0$. More than $n$ vectors in $\R^n$ are always dependent.

**Example (value of $k$).** For which $k$ are $(1,1,0), (0,1,1), (1,0,k)$ dependent?

$$\begin{vmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & k\end{vmatrix} = 1(k - 0) - 1(0 - 1) + 0 = k + 1 = 0 \iff k = -1.$$

**Example (membership in a span).** Is $(1, k, 5)$ in $L\{(1,-3,2), (2,-1,1)\}$? Solve $a + 2b = 1$, $2a + b = 5$ (first and third coordinates): $a = 3$, $b = -1$. The middle coordinate forces $k = -9 + 1 = -8$.

**Polynomials.** Compare coefficients. $\{1 + x,\ x + x^2,\ 1 - x^2\}$ is dependent because $(1 + x) - (x + x^2) = 1 - x^2$.

:::caution
Independence depends on the field. In $\C$ over $\C$, $1$ and $i$ are dependent ($i\cdot 1 - 1\cdot i = 0$). In $\C$ over $\R$ they are independent.
:::

## Basis and dimension {#basis-dimension}

A **basis** of $V$ is a linearly independent set that spans $V$ (a set of **generators** that is independent). Every vector is then a **unique** linear combination of the basis vectors.

:::keyfacts
- **Replacement (exchange) theorem.** If $V$ is spanned by $m$ vectors, then any independent set in $V$ has at most $m$ vectors.
- Hence any two bases of a finite-dimensional space have the same number of elements: the **dimension** $\dim V$. $\dim\{0\} = 0$.
- Every finite spanning set contains a basis (discard dependent vectors).
- **Extension theorem.** Every independent set in a finite-dimensional $V$ can be extended to a basis of $V$.
- If $\dim V = n$: any $n + 1$ vectors are dependent; any $n$ independent vectors form a basis; any $n$ vectors that span $V$ form a basis.
- If $W$ is a subspace of $V$, then $\dim W \le \dim V$, with equality iff $W = V$.
:::

**Standard bases.** $\R^n$: $e_1, \dots, e_n$. $P_n$: $1, x, \dots, x^n$. $M_{m\times n}$: the matrix units $E_{ij}$.

**Extending a set to a basis.** Extend $\{(1, 1, 0), (0, 1, 1)\}$ to a basis of $\R^3$: add a standard vector that keeps the determinant non-zero. With $e_1$: $\det\begin{pmatrix}1&1&0\\0&1&1\\1&0&0\end{pmatrix} = 1 \ne 0$, so $\{(1,1,0), (0,1,1), (1,0,0)\}$ is a basis.

**Dimensions of matrix subspaces** ($n\times n$ real matrices):

| Subspace | Free entries | Dimension |
|:---|:---|:---|
| all of $M_n$ | all | $n^2$ |
| diagonal | diagonal | $n$ |
| upper (or lower) triangular | on and above the diagonal | $\frac{n(n+1)}{2}$ |
| symmetric | on and above the diagonal | $\frac{n(n+1)}{2}$ |
| skew-symmetric | strictly above (diagonal is $0$) | $\frac{n(n-1)}{2}$ |
| trace zero | all but one diagonal entry | $n^2 - 1$ |
| upper triangular, trace zero | | $\frac{n(n+1)}{2} - 1$ |

Check: symmetric $+$ skew $= \frac{n(n+1)}{2} + \frac{n(n-1)}{2} = n^2$, matching $M_n = \text{Sym} \oplus \text{Skew}$.

**Hermitian matrices** ($A^* = A$) do not form a subspace over $\C$ ($iI$ is not Hermitian), but they do over $\R$, with dimension $n^2$: $n$ real diagonal entries and $\frac{n(n-1)}{2}$ complex entries above the diagonal, each worth 2 real parameters.

**Counting by constraints.** A subspace cut out by $r$ **independent** linear conditions in an $n$-dimensional space has dimension $n - r$. Example: $\{p \in P_3 : p(1) = p(-1) = 0\} = \{(x^2 - 1)(a + bx)\}$ has dimension $4 - 2 = 2$.

:::exam-tip
For "dimension of a space of matrices", count the entries you can choose freely after the conditions are imposed. For "matrices commuting with $A$", write a general matrix and solve the linear equations: for $A = \begin{pmatrix}1&1\\0&1\end{pmatrix}$ the answer is $\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}\right\}$, dimension $2$.
:::

## Intersection, union, sum and the dimension formula {#sum-intersection}

Let $W_1, W_2$ be subspaces of $V$.

- **Intersection.** $W_1 \cap W_2$ is always a subspace (any family of subspaces works).
- **Union.** $W_1 \cup W_2$ is a subspace **iff** $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$.
- **Sum.** $W_1 + W_2 = \{w_1 + w_2 : w_1 \in W_1, w_2 \in W_2\}$ is a subspace. It is the smallest subspace containing $W_1 \cup W_2$, so $W_1 + W_2 = L(W_1 \cup W_2)$.

**Why the union fails.** If neither contains the other, pick $u \in W_1 \setminus W_2$ and $v \in W_2 \setminus W_1$. If $u + v \in W_1$ then $v = (u + v) - u \in W_1$, a contradiction; similarly for $W_2$. So $u + v \notin W_1 \cup W_2$. In $\R^2$: the $x$-axis $\cup$ the $y$-axis $= \{xy = 0\}$, and $(1,0) + (0,1) \notin$ it.

:::keyfacts
**Dimension formula.** For finite-dimensional subspaces $W_1, W_2$:
$$\dim(W_1 + W_2) = \dim W_1 + \dim W_2 - \dim(W_1 \cap W_2).$$
:::

**Proof idea.** Take a basis of $W_1 \cap W_2$, extend it to bases of $W_1$ and of $W_2$; the union of the two extended bases is a basis of $W_1 + W_2$.

**Direct sum.** $V = W_1 \oplus W_2$ means $V = W_1 + W_2$ and $W_1 \cap W_2 = \{0\}$. Equivalently, every $v$ is **uniquely** $w_1 + w_2$. Then $\dim V = \dim W_1 + \dim W_2$. Example: $M_n = \text{Sym} \oplus \text{Skew}$, with $A = \frac{A + A^T}{2} + \frac{A - A^T}{2}$.

**Consequences in $\R^n$.** Since $W_1 + W_2 \subseteq \R^n$,

$$\dim(W_1 \cap W_2) \ge \dim W_1 + \dim W_2 - n.$$

- Two planes through the origin in $\R^3$: $\dim(W_1 \cap W_2) \ge 2 + 2 - 3 = 1$. They always share a line.
- A 3-dimensional and a 4-dimensional subspace of $\R^5$ meet in dimension at least $2$.

**Worked example.** In $\R^4$ let $W_1 = \{x : x_1 + x_2 + x_3 + x_4 = 0\}$ ($\dim 3$) and $W_2 = \{x : x_1 = x_2,\ x_3 = x_4\}$ ($\dim 2$). On $W_2$, $x = (a, a, b, b)$, and the condition of $W_1$ gives $2a + 2b = 0$. So $W_1 \cap W_2 = L\{(1, 1, -1, -1)\}$ has dimension $1$, and

$$\dim(W_1 + W_2) = 3 + 2 - 1 = 4, \quad\text{so } W_1 + W_2 = \R^4.$$

:::caution
$W_1 + W_2$ is not the union, and "$W_1 \cap W_2 = \{0\}$" alone does not give $V = W_1 \oplus W_2$: the sum must also be all of $V$.
:::

## Row space, column space and rank {#row-column-space}

For an $m\times n$ matrix $A$ over $F$:

- the **row space** $R(A)$ is the span of its rows, a subspace of $F^n$;
- the **column space** $C(A)$ is the span of its columns, a subspace of $F^m$. It equals $\{AX : X \in F^n\}$, so $AX = b$ is consistent iff $b \in C(A)$.

The **row rank** is $\dim R(A)$ and the **column rank** is $\dim C(A)$.

:::keyfacts
**Theorem.** For every matrix, row rank $=$ column rank $=$ rank $\rho(A)$ (the order of the largest non-vanishing minor). Equivalently $\dim R(A) = \dim R(A^T)$.
:::

**How row operations act.**

- Elementary **row** operations do **not change the row space** (each new row is a combination of old rows, and the operation is reversible). So the non-zero rows of an echelon form of $A$ are a **basis** of $R(A)$.
- Row operations **change the column space** in general, but they **preserve linear relations among the columns**. So the pivot columns of the echelon form tell you which **original** columns form a basis of $C(A)$.

Example: $A = \begin{pmatrix}1 & 2\\ 2 & 4\end{pmatrix} \to \begin{pmatrix}1 & 2\\ 0 & 0\end{pmatrix}$. The column space changes from $L\{(1, 2)\}$ to $L\{(1, 0)\}$; the row space stays $L\{(1, 2)\}$.

**Testing membership.** Is $(2, 3, 1)$ in the row space of $\begin{pmatrix}1 & 0 & 2\\ 0 & 1 & -1\end{pmatrix}$? The rows are already in reduced form, so the only candidate is $2r_1 + 3r_2 = (2, 3, 4 - 3) = (2, 3, 1)$. Yes. In reduced echelon form the pivot coordinates read off the coefficients directly.

**Dimension of a span in $\R^n$.** $\dim L(v_1, \dots, v_k) = \rho\begin{pmatrix}v_1\\ \vdots\\ v_k\end{pmatrix}$. For $(1,2,1), (2,1,0), (3,3,1), (1,-1,-1)$: the third is the sum of the first two and the fourth is the second minus the first, so the dimension is $2$.

The null space $\{X : AX = 0\}$ has dimension $n - \rho(A)$; this is treated with linear systems and, as rank–nullity, with linear maps.

:::exam-tip
$\dim R(A) = \dim C(A)$, but $R(A) \ne C(A)$ in general; they need not even lie in the same space when $m \ne n$.
:::

## Coordinates relative to a basis {#coordinates}

Let $B = (v_1, \dots, v_n)$ be an **ordered** basis of $V$. Each $v \in V$ has a unique expression $v = a_1v_1 + \cdots + a_nv_n$. The **coordinate vector** of $v$ relative to $B$ is

$$[v]_B = (a_1, \dots, a_n)^T.$$

The map $v \mapsto [v]_B$ respects sums and scalar multiples, so every $n$-dimensional space over $F$ behaves exactly like $F^n$. This is why problems in $P_n$ or $M_{m\times n}$ reduce to problems in $\R^n$: write the coefficient vectors and compute a rank or a determinant.

**Finding coordinates in $\R^n$.** If $P$ is the matrix whose **columns** are $v_1, \dots, v_n$, then $v = P[v]_B$, so $[v]_B = P^{-1}v$.

Example: $B = ((1, 1), (1, -1))$, $v = (3, 1)$. Solve $a + b = 3$, $a - b = 1$:

$$[v]_B = (2, 1)^T, \qquad\text{check: } 2(1,1) + 1(1,-1) = (3, 1).$$

**Polynomials.** Coordinates of $p(x) = 2 + 3x + x^2$ relative to $B = (1,\ 1 + x,\ (1 + x)^2)$. Put $t = 1 + x$, so $x = t - 1$:

$$p = 2 + 3(t - 1) + (t - 1)^2 = 0 + 1\cdot t + 1\cdot t^2, \qquad [p]_B = (0, 1, 1)^T.$$

The substitution trick works for any basis $1, (x - c), (x - c)^2, \dots$: the coordinates are the Taylor coefficients $\frac{p^{(k)}(c)}{k!}$.

**Order matters.** The same set in a different order gives the coordinates in a different order: relative to $((1, -1), (1, 1))$, the vector $(3, 1)$ has coordinates $(1, 2)$.

:::caution
The standard coordinates of $v$ are its own entries **only** for the standard basis. Do not copy the entries of $v$ as the answer for a non-standard basis.
:::

## Quick checks and traps {#exam-tips}

- **Subspace test:** $0 \in W$, then closure under $au + bv$. Linear homogeneous conditions pass; constants, products, squares, inequalities and "or" fail.
- **Union** of two subspaces is a subspace only when one contains the other. **Intersection** always is. **Sum** $W_1 + W_2 = L(W_1 \cup W_2)$.
- **Dimension formula:** $\dim(W_1 + W_2) = \dim W_1 + \dim W_2 - \dim(W_1 \cap W_2)$; in $\R^n$, $\dim(W_1 \cap W_2) \ge \dim W_1 + \dim W_2 - n$.
- **Field matters:** $\dim_\C \C^n = n$, $\dim_\R \C^n = 2n$; $\R$ over $\Q$ is infinite-dimensional; $\R$ is not a vector space over $\C$.
- **Polynomials of degree $\le n$:** dimension $n + 1$, not $n$. "Degree exactly $n$" is not a subspace.
- **Matrix dimensions** ($n\times n$): symmetric and upper triangular $\frac{n(n+1)}{2}$; skew $\frac{n(n-1)}{2}$; diagonal $n$; trace zero $n^2 - 1$; Hermitian over $\R$: $n^2$.
- **$n$ vectors in $\R^n$:** basis $\iff$ independent $\iff$ spanning $\iff$ $\det \ne 0$. For "the value of $k$ for dependence", set the determinant to $0$.
- **More than $n$ vectors in $\R^n$** are always dependent; **fewer than $n$** never span.
- **Dependent sets:** anything containing $0$; two vectors that are proportional. A subset of a dependent set may be independent.
- **Row operations** keep the row space but not the column space; the dimension of both equals the rank.
- **Coordinates** depend on the basis and its order; check by recombining.
