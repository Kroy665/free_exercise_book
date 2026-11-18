# Real Quadratic Forms

## The matrix of a quadratic form {#matrix-of-form}

A **real quadratic form** in $x_1, \dots, x_n$ is a homogeneous polynomial of degree $2$ with real coefficients:

$$Q(x) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_{ij}x_ix_j = x^TAx, \qquad x = (x_1, \dots, x_n)^T.$$

Many matrices give the same form ($x^TAx = x^TA^Tx$), but exactly **one symmetric** matrix does, namely $\tfrac12(A + A^T)$. "The matrix of the form" always means this symmetric matrix.

**Rule.** The coefficient of $x_i^2$ goes on the diagonal. The coefficient of the cross term $x_ix_j$ ($i \ne j$) is **split in half** between positions $(i, j)$ and $(j, i)$.

In three variables:

$$ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy = \begin{pmatrix} x & y & z\end{pmatrix}\begin{pmatrix} a & h & g\\ h & b & f\\ g & f & c\end{pmatrix}\begin{pmatrix} x\\ y\\ z\end{pmatrix}.$$

**Worked example.** $Q = x^2 + 2y^2 - z^2 + 4xy - 6yz + 2zx$. Halve each cross coefficient: $xy \to 2$, $yz \to -3$, $zx \to 1$.

$$A = \begin{pmatrix} 1 & 2 & 1\\ 2 & 2 & -3\\ 1 & -3 & -1\end{pmatrix}.$$

**Reverse direction.** From $A = \begin{pmatrix} 2 & -1 & 0\\ -1 & 3 & 2\\ 0 & 2 & 1\end{pmatrix}$, read off $Q = 2x^2 + 3y^2 + z^2 - 2xy + 4yz$: each off-diagonal entry is **doubled** in $Q$.

**Value at a point.** $Q(x)$ is just $x^TAx$; substituting into the polynomial is usually quicker. For the form above, $Q(1, 1, 0) = 2 + 3 - 2 = 3$.

The **rank** of $Q$ is the rank of its symmetric matrix $A$. $Q$ is **non-singular** if $\det A \ne 0$.

:::caution
The most common slip is forgetting to halve: the matrix of $x^2 + 4xy + 3y^2$ is $\begin{pmatrix} 1 & 2\\ 2 & 3\end{pmatrix}$, **not** $\begin{pmatrix} 1 & 4\\ 4 & 3\end{pmatrix}$. The second matrix gives $x^2 + 8xy + 3y^2$. The non-symmetric $\begin{pmatrix} 1 & 4\\ 0 & 3\end{pmatrix}$ also gives the right form, but it is not *the* matrix of the form, and its eigenvalues and minors tell you nothing.
:::

:::exam-tip
Check a candidate matrix by expanding one cross term: the $(1,2)$ and $(2,1)$ entries together must add up to the coefficient of $x_1x_2$.
:::

## Linear change of variables and congruence {#congruence}

A **non-singular linear transformation** $x = Py$ ($P$ real, $\det P \ne 0$) turns $Q$ into a form in $y$:

$$Q = x^TAx = (Py)^TA(Py) = y^T\,(P^TAP)\,y.$$

So the new matrix is $B = P^TAP$. Two square matrices related this way are **congruent**. Congruence is an equivalence relation, and it preserves:

- **symmetry:** $(P^TAP)^T = P^TA^TP$;
- **rank:** $P$ and $P^T$ are invertible;
- **the sign of the determinant:** $\det B = (\det P)^2\det A$.

It does **not** preserve the determinant itself, the trace or the eigenvalues. Congruence is not similarity, since $P^T \ne P^{-1}$ in general. The two coincide when $P$ is **orthogonal** ($P^T = P^{-1}$).

**Worked example.** $Q = 2xy$, so $A = \begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix}$. Put $x = u + v$, $y = u - v$, that is $P = \begin{pmatrix} 1 & 1\\ 1 & -1\end{pmatrix}$:

$$P^TAP = \begin{pmatrix} 2 & 0\\ 0 & -2\end{pmatrix}, \qquad Q = 2u^2 - 2v^2.$$

Directly: $2(u + v)(u - v) = 2u^2 - 2v^2$. The determinant went from $-1$ to $-4 = (\det P)^2(-1)$.

**Congruence by operations.** Applying an elementary row operation and then the **same** column operation replaces $A$ by $E^TAE$. Repeating such pairs diagonalises any real symmetric matrix. Doing the same column operations on $I$ records $P$.

:::keyfacts
- Every real symmetric matrix is congruent to a diagonal matrix.
- In fact it is congruent to $\operatorname{diag}(I_p, -I_q, O)$ for a unique pair $(p, q)$ (Sylvester's law, below).
:::

:::caution
"Congruent" here means $B = P^TAP$, not congruence of integers mod $n$. Writing $PAP^T$ is also fine (replace $P$ by $P^T$); writing $P^{-1}AP$ is **similarity**, a different relation.
:::

## Reduction by completing squares (Lagrange) {#lagrange}

**Lagrange's method** reduces a form to a sum of squares using only rational arithmetic.

1. Pick a variable whose square appears, say $x_1$ with $a_{11} \ne 0$. Collect every term containing $x_1$ and complete the square:
   $$a_{11}x_1^2 + 2x_1(a_{12}x_2 + \dots + a_{1n}x_n) = a_{11}\Big(x_1 + \tfrac{a_{12}}{a_{11}}x_2 + \cdots\Big)^2 - (\text{terms without } x_1).$$
2. Repeat on the remaining form in $x_2, \dots, x_n$.
3. **No square terms left** (only products)? If $x_ix_j$ appears, put $x_i = u + v$, $x_j = u - v$. This creates $u^2 - v^2$, and you can continue.

The new variables are linear combinations of the old ones, given by a triangular (hence non-singular) substitution, as long as you keep a full set of $n$ new variables.

**Example 1.** $Q = x^2 + 2y^2 + 3z^2 + 2xy + 4yz$.

$$Q = (x + y)^2 + y^2 + 4yz + 3z^2 = (x + y)^2 + (y + 2z)^2 - z^2.$$

With $X = x + y$, $Y = y + 2z$, $Z = z$: $Q = X^2 + Y^2 - Z^2$. So $p = 2$, $q = 1$, and $Q$ is **indefinite**, even though every diagonal coefficient is positive.

**Example 2.** $Q = x^2 + 2y^2 + 2z^2 + 2xy + 2zx$.

$$Q = (x + y + z)^2 - 2yz + y^2 + z^2 = (x + y + z)^2 + (y - z)^2.$$

Only two squares: rank $2$. $Q \ge 0$ always, and $Q = 0$ at $(-2, 1, 1)$, so $Q$ is positive semi-definite but not positive definite.

**Example 3 (no squares).** $Q = 2xy + 2yz$. Put $x = u + v$, $y = u - v$, $z = w$:

$$Q = 2u^2 - 2v^2 + 2uw - 2vw = 2\big(u + \tfrac{w}{2}\big)^2 - 2\big(v + \tfrac{w}{2}\big)^2.$$

In the original variables, $Q = \tfrac12(x + y + z)^2 - \tfrac12(x - y + z)^2$. Rank $2$, $p = q = 1$.

:::exam-tip
Always expand your answer back once. Completing squares often produces a leftover such as $-z^2$ that is easy to drop, and dropping it changes the signature.
:::

## Orthogonal reduction via eigenvalues {#orthogonal-reduction}

A real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors. Put them as columns of an orthogonal $P$. Then $P^TAP = P^{-1}AP = D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, and $x = Py$ gives

$$Q = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2.$$

This is the **canonical form under an orthogonal transformation**. The coefficients are exactly the eigenvalues of $A$. Geometrically, the new axes are the **principal axes** of the conic or quadric $Q = c$.

**Example.** $Q = 3x^2 + 2xy + 3y^2$, so $A = \begin{pmatrix} 3 & 1\\ 1 & 3\end{pmatrix}$, with eigenvalues $2$ and $4$. The unit eigenvectors are $\tfrac{1}{\sqrt2}(1, -1)^T$ and $\tfrac{1}{\sqrt2}(1, 1)^T$. So

$$X = \frac{x - y}{\sqrt2},\quad Y = \frac{x + y}{\sqrt2}: \qquad Q = 2X^2 + 4Y^2.$$

The curve $Q = 4$ is an ellipse with semi-axes $\sqrt2$ along $y = -x$ and $1$ along $y = x$.

```plot
title: $3x^2 + 2xy + 3y^2 = 4$ and its principal axes $y = \pm x$
x: -2, 2
y: -2, 2
equal: true
implicit: 3x^2 + 2xy + 3y^2 = 4 | $Q = 4$
f: x | $y = x$ (eigenvalue 4)
f: -x | $y = -x$ (eigenvalue 2)
```

**Three variables.** $Q = 2x^2 + 2y^2 + 2z^2 + 2xy + 2yz + 2zx$ has $A = I + J$, where $J$ is the all-ones matrix. $J$ has eigenvalues $3, 0, 0$, so $A$ has $4, 1, 1$, and $Q = 4Y_1^2 + Y_2^2 + Y_3^2$. It is positive definite.

**Extreme values (Rayleigh).** For $x \ne 0$,

$$\lambda_{\min} \le \frac{x^TAx}{x^Tx} \le \lambda_{\max}.$$

So on the unit circle or sphere $x^Tx = 1$, the maximum of $Q$ is $\lambda_{\max}$ and the minimum is $\lambda_{\min}$, attained at the corresponding unit eigenvectors. For $5x^2 + 4xy + 2y^2$ the eigenvalues are $6$ and $1$, so the maximum on $x^2 + y^2 = 1$ is $6$.

:::caution
Lagrange's method and orthogonal reduction usually give **different coefficients**: $Q = (x + y)^2 + 2y^2$ is $X^2 + 2Y^2$ by completing squares, but its eigenvalues are $2 \pm \sqrt2$. Only the **signs** (hence $p$ and $q$) must agree. Do not treat Lagrange coefficients as eigenvalues.
:::

## Rank, index, signature and Sylvester's law {#inertia}

Reduce $Q$ (of rank $r$) to a diagonal form by any real non-singular transformation. Let $p$ = number of **positive** coefficients and $q$ = number of **negative** ones. Then $p + q = r$.

:::keyfacts
- **Sylvester's law of inertia.** The numbers $p$ and $q$ do not depend on the transformation used. Every real quadratic form of rank $r$ can be reduced to the **normal form**
  $$z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2,$$
  and $p$ is the same for every such reduction. In matrix terms, a real symmetric $A$ is congruent to exactly one $\operatorname{diag}(I_p, -I_q, O)$.
- **Classification.** Two real symmetric $n \times n$ matrices are congruent $\iff$ they have the same rank and the same index (equivalently, the same $p$ and $q$).
- Since eigenvalues give one diagonal form, $p$ and $q$ are the numbers of positive and negative eigenvalues, counted with multiplicity.
:::

**Terminology.**

| Term | Value | Notes |
|:---|:---|:---|
| rank $r$ | $p + q$ | rank of $A$ |
| index | $p$ | number of positive squares |
| signature | $s = p - q$ | most Indian texts and Mapa; some books call $p$ itself the signature, or the pair $(p, q)$ |
| nullity | $n - r$ | number of zero coefficients |

In this course, **signature means $p - q$**, and questions say so. From $r$ and $s$: $p = \frac{r + s}{2}$, $q = \frac{r - s}{2}$. So $s$ and $r$ have the **same parity**, and $\lvert s\rvert \le r$.

**Normal form from a diagonal form.** Scale each square: $2X^2 + 4Y^2 - 3Z^2$ becomes $z_1^2 + z_2^2 - z_3^2$ with $z_1 = \sqrt2X$, $z_2 = 2Y$, $z_3 = \sqrt3Z$. Here $r = 3$, $p = 2$, $s = 1$.

**Example.** $Q = 2xy + 2yz + 2zx$ has $A = J - I$, with eigenvalues $3 - 1 = 2$ and $0 - 1 = -1$ (twice). So $r = 3$, $p = 1$, $q = 2$, $s = -1$, and the normal form is $z_1^2 - z_2^2 - z_3^2$.

**Counting classes.** A congruence class of real symmetric $n \times n$ matrices is fixed by a pair $(p, q)$ with $p + q \le n$. There are $\frac{(n + 1)(n + 2)}{2}$ classes: $6$ for $n = 2$ and $10$ for $n = 3$.

:::caution
Over $\C$ only the rank survives, since $-1 = i^2$ is a square: every complex symmetric matrix of rank $r$ is congruent to $\operatorname{diag}(I_r, O)$. Sylvester's law of inertia is a statement about **real** forms.
:::

## Definiteness {#definiteness}

Let $Q = x^TAx$ with $A$ real symmetric of order $n$. The form is

| Name | Condition on $Q$ | Eigenvalues | $(p, q)$ |
|:---|:---|:---|:---|
| positive definite (PD) | $Q(x) > 0$ for all $x \ne 0$ | all $> 0$ | $p = n$ |
| negative definite (ND) | $Q(x) < 0$ for all $x \ne 0$ | all $< 0$ | $q = n$ |
| positive semi-definite | $Q(x) \ge 0$ for all $x$ | all $\ge 0$ | $q = 0$ |
| negative semi-definite | $Q(x) \le 0$ for all $x$ | all $\le 0$ | $p = 0$ |
| indefinite | takes both signs | some $> 0$, some $< 0$ | $p \ge 1,\ q \ge 1$ |

:::caution
Many Indian texts reserve "semi-definite" for forms that are $\ge 0$ **and** vanish at some $x \ne 0$ (so $\det A = 0$). Under that convention a PD form is not called semi-definite. To stay safe, questions here say "positive semi-definite but not positive definite" when they mean $q = 0$ and $r < n$.
:::

**Leading principal minors** are $D_1 = a_{11}$, $D_2 = \begin{vmatrix} a_{11} & a_{12}\\ a_{21} & a_{22}\end{vmatrix}$, …, $D_n = \det A$.

:::keyfacts
- **Sylvester's criterion.** $Q$ is PD $\iff$ $D_1 > 0, D_2 > 0, \dots, D_n > 0$.
- $Q$ is ND $\iff$ $-A$ is PD $\iff$ $(-1)^kD_k > 0$ for every $k$: $D_1 < 0$, $D_2 > 0$, $D_3 < 0$.
- **Two variables.** $ax^2 + 2hxy + by^2$ is PD $\iff$ $a > 0$ and $ab - h^2 > 0$; ND $\iff$ $a < 0$ and $ab - h^2 > 0$; indefinite if $ab - h^2 < 0$.
- **Jacobi's rule.** If every $D_k \ne 0$, then $Q = \sum_k \frac{D_k}{D_{k-1}}\,y_k^2$ ($D_0 = 1$), so $q$ = number of **sign changes** in $1, D_1, D_2, \dots, D_n$.
- PD $\iff$ $A = P^TP$ for some non-singular $P$ $\iff$ $A$ is congruent to $I$.
:::

**Example (PD).** $Q = 2x^2 + 2y^2 + 2z^2 - 2xy - 2yz$: $A = \begin{pmatrix} 2 & -1 & 0\\ -1 & 2 & -1\\ 0 & -1 & 2\end{pmatrix}$, with $D_1 = 2$, $D_2 = 3$, $D_3 = 4$. All positive, so PD.

**Example (parameter).** $x^2 + 2y^2 + z^2 + 2xy + 2ayz$: $A = \begin{pmatrix} 1 & 1 & 0\\ 1 & 2 & a\\ 0 & a & 1\end{pmatrix}$, with $D_1 = 1$, $D_2 = 1$, $D_3 = 1 - a^2$. PD $\iff -1 < a < 1$.

**Example (Jacobi).** $D_1 = 2$, $D_2 = -1$, $D_3 = 4$: the sequence $1, 2, -1, 4$ has two sign changes, so $q = 2$, $p = 1$, $s = -1$.

**Necessary conditions for PD** (quick eliminators): every diagonal entry $a_{ii} > 0$, $\det A > 0$, $\operatorname{tr} A > 0$, and $a_{ii}a_{jj} > a_{ij}^2$. None of them is sufficient on its own.

## Semi-definite forms and the minors caveat {#semidefinite}

Sylvester's criterion needs **strict** inequalities. Relaxing them to $D_k \ge 0$ does **not** test semi-definiteness.

**Counterexample 1.** $A = \begin{pmatrix} 0 & 0\\ 0 & -1\end{pmatrix}$, so $Q = -y^2$. Here $D_1 = 0$ and $D_2 = 0$, both $\ge 0$, yet $Q(0, 1) = -1 < 0$. The form is negative semi-definite.

**Counterexample 2.** $Q = x^2 + y^2 + 2xy + 2yz + 2zx = (x + y + z)^2 - z^2$, with
$$A = \begin{pmatrix} 1 & 1 & 1\\ 1 & 1 & 1\\ 1 & 1 & 0\end{pmatrix}, \qquad D_1 = 1,\ D_2 = 0,\ D_3 = 0.$$
All leading minors are $\ge 0$, but $Q = -1$ at $(1, 0, -1)$, so $Q$ is **indefinite**. The principal minor on rows and columns $\{2, 3\}$ is $1\cdot 0 - 1 = -1 < 0$, which exposes it.

:::keyfacts
- $Q$ is positive semi-definite $\iff$ **every principal minor** (all $2^n - 1$ of them, not only the leading ones) is $\ge 0$.
- $Q$ is negative semi-definite $\iff$ every principal minor of order $k$ has the sign of $(-1)^k$ or is $0$.
- Safest route: compute the eigenvalues, or reduce by completing squares and count signs.
:::

**Principal minors of a $3 \times 3$ matrix:** the three diagonal entries; the three $2 \times 2$ minors on rows and columns $\{1,2\}$, $\{1,3\}$, $\{2,3\}$; and $\det A$.

**Recognising semi-definite forms.**
- $\det A = 0$ means $r < n$, so the form is never definite.
- If additionally all eigenvalues are $\ge 0$ (or the completed squares all carry $+$), it is positive semi-definite but not PD.
- A perfect square $(\alpha x + \beta y + \gamma z)^2$ has rank $1$ and signature $1$.
- $x^2 + y^2 + z^2 - xy - yz - zx = \tfrac12\big[(x - y)^2 + (y - z)^2 + (z - x)^2\big]$ is positive semi-definite with rank $2$. It vanishes on the line $x = y = z$.

:::exam-tip
In a classification question, first look at $\det A$. If $\det A = 0$, "positive definite" and "negative definite" are out at once. Then a single test vector with $Q < 0$ (or $Q > 0$) decides between semi-definite and indefinite.
:::

## Quick checks and traps {#exam-tips}

- **Halve the cross terms.** The $(i, j)$ entry of $A$ is half the coefficient of $x_ix_j$. Going back, double it.
- **Congruence is not similarity.** $P^TAP$ keeps the rank, symmetry and the *sign* of $\det A$, but not the eigenvalues, trace or determinant.
- **Eigenvalues give the orthogonal canonical form.** Lagrange coefficients are not eigenvalues; only their signs agree with the eigenvalues' signs.
- **Signature convention.** Here $s = p - q$. Then $p = \frac{r + s}{2}$, and $r$ and $s$ have the same parity, so (rank $3$, signature $2$) is impossible.
- **Positive diagonal does not mean PD.** $x^2 + 6xy + 2y^2$ has $D_2 = 2 - 9 < 0$: indefinite.
- **Trace and determinant in two variables.** $\det A < 0$: indefinite. $\det A > 0$: definite, with the sign of $\operatorname{tr} A$ (or $a_{11}$). $\det A = 0$: semi-definite (or zero).
- **ND test.** The signs alternate starting with **negative**: $D_1 < 0$, $D_2 > 0$, $D_3 < 0$. A sequence $-, -, -$ is not ND.
- **Semi-definite trap.** Leading minors $\ge 0$ prove nothing; check all principal minors or the eigenvalues.
- **Two forms are congruent** exactly when they have the same rank and the same signature: $x^2 - y^2$ and $2xy$ are congruent, $x^2 + y^2$ and $x^2 - y^2$ are not.
- **Max on the unit sphere** of $x^TAx$ is $\lambda_{\max}$; the minimum is $\lambda_{\min}$.
