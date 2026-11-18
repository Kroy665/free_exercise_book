# Determinants

## Definition and expansion {#definition}

A **determinant** is a scalar attached to a square array of numbers. For orders 2 and 3:

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc,$$

$$\begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix} = a_1(b_2c_3 - b_3c_2) - b_1(a_2c_3 - a_3c_2) + c_1(a_2b_3 - a_3b_2).$$

**Sarrus' rule** (order 3 only): copy the first two columns to the right. Add the three "down-right" diagonal products and subtract the three "up-right" ones. It does **not** work for order 4 or more.

**General definition (Leibniz).** For an $n \times n$ array $A = (a_{ij})$,

$$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{1\sigma(1)}a_{2\sigma(2)}\cdots a_{n\sigma(n)}.$$

- Each term takes **exactly one element from each row and each column**.
- There are $n!$ terms. A term gets the sign $+$ if the column permutation $\sigma$ is even and $-$ if it is odd.
- Example: in a 4th-order determinant, the term $a_{12}a_{21}a_{34}a_{43}$ has $\sigma = (1\,2)(3\,4)$, a product of two transpositions, so its sign is $+$.

**Laplace expansion.** The value equals the sum of the products of the elements of **any one row (or column)** with their cofactors (see [minors and cofactors](#minors-cofactors)). The order-3 formula above is the expansion along the first row. Each cofactor is a determinant of order $n-1$, so a determinant of order $n$ reduces step by step to order 2.

**Worked example.**

$$\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{vmatrix} = 1(50 - 48) - 2(40 - 42) + 3(32 - 35) = 2 + 4 - 9 = -3.$$

:::exam-tip
A **triangular** determinant (all entries above, or all below, the diagonal are zero) equals the product of its diagonal entries. Most hand calculations aim to reach this form using row operations, or to create two zeros in one row before expanding.
:::

## Properties {#properties}

Let $\Delta = \det A$, with $A$ of order $n$.

| Operation | Effect on $\Delta$ |
|:---|:---|
| Transpose (rows $\leftrightarrow$ columns) | unchanged: $\det A^{T} = \det A$ |
| Interchange two rows (or two columns) | changes sign |
| Two rows (or columns) identical or proportional | $\Delta = 0$ |
| Multiply one row by $k$ | $\Delta$ is multiplied by $k$ |
| Multiply the whole array by $k$ | $\det(kA) = k^{n}\det A$ |
| $R_i \to R_i + kR_j$ ($i \ne j$) | unchanged |
| A row of zeros | $\Delta = 0$ |
| One row is a sum: $R_i = R_i' + R_i''$ | $\Delta$ splits as a sum of two determinants |

Since $\det A^T = \det A$, every row property is also a column property.

**Linearity in one row.** A determinant is linear in each row separately, **not** in the whole array. In general $\det(A + B) \ne \det A + \det B$: for $A = B = I_2$, $\det(2I_2) = 4$ but $\det I_2 + \det I_2 = 2$.

**Zero conditions.** $\Delta = 0$ when a row (or column) is zero, when two rows are proportional, or more generally when one row is a linear combination of the others. Example: in
$$\begin{vmatrix} a-b & b-c & c-a \\ b-c & c-a & a-b \\ c-a & a-b & b-c \end{vmatrix}$$
every row sums to $0$. So $C_1 \to C_1 + C_2 + C_3$ gives a zero column and $\Delta = 0$.

**Factor theorem.** If $\Delta$ is a polynomial in $a$ and putting $a = b$ makes $\Delta$ vanish identically, then $(a - b)$ is a factor. This finds factors without expanding. Compare degrees to find the remaining factor, then fix the constant by comparing one term, for example the diagonal product.

:::caution
$\det(kA) = k^{n}\det A$, not $k\det A$. For a $3\times3$ matrix with $\det A = 5$: $\det(2A) = 8 \cdot 5 = 40$. Also, a combined operation like $R_1 \to 2R_1 + R_2$ multiplies $\Delta$ by $2$; only $R_i \to R_i + kR_j$ leaves it unchanged.
:::

## Minors and cofactors {#minors-cofactors}

For the element $a_{ij}$ of a determinant of order $n$:

- the **minor** $M_{ij}$ is the determinant of order $n - 1$ left after deleting row $i$ and column $j$;
- the **cofactor** is $C_{ij} = (-1)^{i+j} M_{ij}$.

The sign pattern $(-1)^{i+j}$ is a chessboard that starts with $+$ in the top-left corner:

$$\begin{matrix} + & - & + \\ - & + & - \\ + & - & + \end{matrix}$$

**Expansion theorem.** For any fixed row $i$ and any fixed column $j$:

$$\sum_{k=1}^{n} a_{ik}C_{ik} = \Delta, \qquad \sum_{k=1}^{n} a_{kj}C_{kj} = \Delta.$$

**Alien cofactors.** Elements of one row multiplied by the cofactors of a **different** row always sum to zero:

$$\sum_{k=1}^{n} a_{ik}C_{jk} = 0 \quad (i \ne j).$$

The reason: this sum is the expansion of a determinant whose row $j$ has been replaced by a copy of row $i$, and that determinant has two equal rows. In one line, $\sum_k a_{ik}C_{jk} = \delta_{ij}\Delta$.

**Worked example.** In
$$\Delta = \begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix},$$
the minor of $a_{23} = 6$ is $\begin{vmatrix} 1 & 2 \\ 7 & 8 \end{vmatrix} = -6$. Its cofactor is $(-1)^{5}(-6) = 6$.

:::exam-tip
Expand along the row or column with the **most zeros**. Before expanding, use $R_i \to R_i + kR_j$ to create zeros: it changes no value and saves most of the arithmetic.
:::

:::caution
Minor and cofactor differ only in sign, so a sign slip is the standard wrong option. Check $(-1)^{i+j}$: it is $-$ exactly when $i + j$ is odd.
:::

## Product of determinants and the adjoint {#product-adjoint}

**Product theorem.** For square arrays $A, B$ of the same order,

$$\det(AB) = \det A \cdot \det B.$$

**Row-by-column rule.** The $(i, j)$ entry of the product determinant is (row $i$ of the first) $\cdot$ (column $j$ of the second). Because a determinant equals that of its transpose, you may also multiply **row by row**, column by column or column by row. The value is the same; only the product array looks different.

Consequences: $\det(AB) = \det(BA)$ even when $AB \ne BA$; $\det(A^m) = (\det A)^m$; $\det(AA^{T}) = (\det A)^2$.

**Worked example.** Let $\Delta$ be the circulant with rows $(a,b,c), (b,c,a), (c,a,b)$. Swap columns 2 and 3, then multiply column 1 by $-1$. Two sign changes cancel, so the array with rows $(-a,c,b), (-b,a,c), (-c,b,a)$ also has value $\Delta$. Multiply the two arrays row by row. For instance, entry $(1,1)$ is $-a^2 + bc + cb$. This gives
$$\begin{vmatrix} 2bc - a^2 & c^2 & b^2 \\ c^2 & 2ca - b^2 & a^2 \\ b^2 & a^2 & 2ab - c^2 \end{vmatrix} = \begin{vmatrix} a & b & c \\ b & c & a \\ c & a & b \end{vmatrix}^2 = (a^3 + b^3 + c^3 - 3abc)^2.$$

**Adjoint (adjugate).** The adjoint of $A$ is the **transpose** of the matrix of cofactors: $(\operatorname{adj} A)_{ij} = C_{ji}$. The expansion theorem and the alien-cofactor rule give

$$A\,(\operatorname{adj} A) = (\operatorname{adj} A)\,A = (\det A)\,I_n.$$

Taking determinants, $\det A \cdot \det(\operatorname{adj} A) = (\det A)^{n}$. This yields the **adjoint determinant** (Jacobi / Cauchy):

:::keyfacts
- $\det(\operatorname{adj} A) = (\det A)^{\,n-1}$ for $n \ge 2$. It holds even when $\det A = 0$.
- The determinant of the cofactors (the **adjugate determinant** $\Delta'$) equals $\Delta^{n-1}$; for order 3, $\Delta' = \Delta^{2}$.
- $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2}A$, so $\det(\operatorname{adj}\operatorname{adj} A) = (\det A)^{(n-1)^2}$.
- $\operatorname{adj}(kA) = k^{n-1}\operatorname{adj} A$.
:::

For a $3\times3$ matrix with $\det A = 4$: $\det(\operatorname{adj} A) = 16$. For a $4\times4$ matrix with $\det A = -2$: $\det(\operatorname{adj} A) = (-2)^3 = -8$.

:::caution
$\det A = 0$ does **not** make $\operatorname{adj} A$ zero. For $A = \operatorname{diag}(1, 1, 0)$, $\operatorname{adj} A = \operatorname{diag}(0, 0, 1)$. It is only $\det(\operatorname{adj} A)$ that vanishes. Inverses, $A^{-1} = \operatorname{adj} A/\det A$, belong to the next topic.
:::

## Symmetric and skew-symmetric determinants {#symmetric-skew}

A determinant is **symmetric** if $a_{ij} = a_{ji}$ for all $i, j$, and **skew-symmetric** if $a_{ij} = -a_{ji}$ for all $i, j$. Over the reals (or any field where $2 \ne 0$), skew-symmetry forces $a_{ii} = -a_{ii}$, so every diagonal entry is $0$.

**Symmetric of order 3.**

$$\begin{vmatrix} a & h & g \\ h & b & f \\ g & f & c \end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2.$$

This is the discriminant of the general second-degree equation in two variables.

**Skew-symmetric of odd order is zero.** Let $A^{T} = -A$, of order $n$. Then

$$\det A = \det A^{T} = \det(-A) = (-1)^{n}\det A.$$

If $n$ is odd, $\det A = -\det A$, so $\det A = 0$. For example,
$$\begin{vmatrix} 0 & a & -b \\ -a & 0 & c \\ b & -c & 0 \end{vmatrix} = 0 \quad \text{for all } a, b, c.$$

The proof uses $\det A^T = \det A$ and $\det(-A) = (-1)^n \det A$. It does not use the zero diagonal.

**Skew-symmetric of even order is a perfect square.** For order 2, $\begin{vmatrix} 0 & a \\ -a & 0 \end{vmatrix} = a^2$. For order 4,

$$\begin{vmatrix} 0 & a & b & c \\ -a & 0 & d & e \\ -b & -d & 0 & f \\ -c & -e & -f & 0 \end{vmatrix} = (af - be + cd)^{2}.$$

In general it is the square of a polynomial in the entries, the **Pfaffian**.

:::caution
A symmetric determinant with zero diagonal need **not** vanish:
$$\begin{vmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{vmatrix} = 2.$$
The vanishing result is for **skew**-symmetric determinants of **odd** order only. Symmetric determinants are also not perfect squares in general.
:::

## Standard determinants {#standard-determinants}

These appear again and again. Know their values and how the factor theorem gives them.

| Determinant (rows listed) | Value |
|:---|:---|
| $(1, 1, 1),\ (a, b, c),\ (a^2, b^2, c^2)$ (Vandermonde) | $(a-b)(b-c)(c-a)$ |
| $(1, 1, 1),\ (a, b, c),\ (a^3, b^3, c^3)$ | $(a-b)(b-c)(c-a)(a+b+c)$ |
| $(1, a, bc),\ (1, b, ca),\ (1, c, ab)$ | $(a-b)(b-c)(c-a)$ |
| $(a, b, c),\ (b, c, a),\ (c, a, b)$ (circulant) | $-(a^3 + b^3 + c^3 - 3abc)$ |
| $(1+a, 1, 1),\ (1, 1+b, 1),\ (1, 1, 1+c)$ | $abc + ab + bc + ca$ |
| $(x, a, a),\ (a, x, a),\ (a, a, x)$ | $(x + 2a)(x - a)^2$ |
| $(b+c, a, a),\ (b, c+a, b),\ (c, c, a+b)$ | $4abc$ |
| $((b+c)^2, a^2, a^2),\ (b^2, (c+a)^2, b^2),\ (c^2, c^2, (a+b)^2)$ | $2abc(a+b+c)^3$ |

**Vandermonde by the factor theorem.** The determinant vanishes when $a = b$, $b = c$ or $c = a$ (two equal columns). So it is $k(a-b)(b-c)(c-a)$. Both sides have degree 3. Comparing the diagonal term $bc^2$ gives $k = 1$. In general, the $n$th-order Vandermonde equals $\prod_{i<j}(x_j - x_i)$.

**Circulant.** Apply $C_1 \to C_1 + C_2 + C_3$ to take out $(a + b + c)$:

$$\begin{vmatrix} a & b & c \\ b & c & a \\ c & a & b \end{vmatrix} = -(a+b+c)(a^2 + b^2 + c^2 - ab - bc - ca) = -(a^3 + b^3 + c^3 - 3abc).$$

So the circulant vanishes when $a + b + c = 0$. For example, with $1, \omega, \omega^2$, the cube roots of unity, it is $0$.

**Worked example.** $\begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & 5 \\ 4 & 9 & 25 \end{vmatrix} = (2-3)(3-5)(5-2) = (-1)(-2)(3) = 6.$

:::exam-tip
Check any claimed value with small numbers. Put $a = 0, b = 1, c = 2$ (or $a = b$ to test a factor) and compare. For the circulant with $a = 1, b = c = 0$, the array is $(1,0,0),(0,0,1),(0,1,0)$, with value $-1$. This fixes the overall minus sign.
:::

## Cramer's rule {#cramers-rule}

For the system
$$a_1x + b_1y + c_1z = d_1,\quad a_2x + b_2y + c_2z = d_2,\quad a_3x + b_3y + c_3z = d_3,$$
let $D$ be the coefficient determinant. Let $D_x$, $D_y$, $D_z$ be $D$ with the $x$-, $y$- or $z$-column replaced by the constants $(d_1, d_2, d_3)$.

:::keyfacts
- **If $D \ne 0$:** there is a **unique** solution $x = \dfrac{D_x}{D}$, $y = \dfrac{D_y}{D}$, $z = \dfrac{D_z}{D}$.
- **If $D = 0$ and at least one of $D_x, D_y, D_z$ is nonzero:** the system is **inconsistent** (no solution).
- **If $D = 0$ and $D_x = D_y = D_z = 0$:** Cramer's rule decides nothing. The system has **either infinitely many solutions or none**.
- **Homogeneous system** (all $d_i = 0$): $x = y = z = 0$ is always a solution. A **non-trivial** solution exists **if and only if** $D = 0$.
:::

The same holds for 2 variables with $2\times2$ determinants.

**Worked example.** $x + y + z = 6$, $x - y + z = 2$, $2x + y - z = 1$:

$$D = \begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 2 & 1 & -1 \end{vmatrix} = 6,\quad D_x = 6,\quad D_y = 12,\quad D_z = 18,$$

so $(x, y, z) = (1, 2, 3)$.

**Parameter questions.** For $kx + y + z = 0$, $x + ky + z = 0$, $x + y + kz = 0$:
$$D = (k + 2)(k - 1)^2,$$
so a non-trivial solution exists exactly when $k = 1$ or $k = -2$.

For $x + y + z = 6$, $x + 2y + 3z = 10$, $x + 2y + \lambda z = \mu$, we get $D = \lambda - 3$. So the solution is unique iff $\lambda \ne 3$. If $\lambda = 3$, subtracting the second equation from the third gives $0 = \mu - 10$. So there is no solution if $\mu \ne 10$, and infinitely many if $\mu = 10$.

:::caution
"$D = 0$ and all $D_i = 0$" does **not** guarantee infinitely many solutions. The system $x + y + z = 1$, $x + y + z = 2$, $x + y + z = 3$ has $D = D_x = D_y = D_z = 0$ (every determinant has two equal columns), yet it is inconsistent. For full consistency tests, use rank (next topics).
:::

## Quick checks and traps {#exam-tips}

- **Scaling:** $\det(kA) = k^{n}\det A$. One row times $k$ gives $k\Delta$.
- **Row swaps:** each interchange flips the sign. A cyclic shift of 3 rows is two swaps, so the value does not change.
- **Number of terms:** an $n$th-order determinant has $n!$ terms, half with each sign (for $n \ge 2$).
- **Cofactor sign:** $C_{ij} = (-1)^{i+j}M_{ij}$. Alien cofactors sum to $0$.
- **Adjoint:** $\det(\operatorname{adj} A) = (\det A)^{n-1}$, so it is $\Delta^2$ for order 3 and $\Delta^3$ for order 4. Also $\det(\operatorname{adj}\operatorname{adj} A) = (\det A)^{(n-1)^2}$.
- **Products:** $\det(AB) = \det(BA) = \det A\det B$ and $\det(AA^T) = (\det A)^2$. There is no rule for $\det(A + B)$.
- **Skew-symmetric:** of odd order, $0$; of even order, a perfect square.
- **Circulant:** $-(a^3 + b^3 + c^3 - 3abc)$. It is $0$ when $a + b + c = 0$ and when $a = b = c$.
- **Cramer:** $D \ne 0$ means a unique solution. $D = 0$ with some $D_i \ne 0$ means none. $D = 0$ with all $D_i = 0$ is undecided. A homogeneous system has a non-trivial solution iff $D = 0$.
- **Fast numeric check:** put small numbers into a symbolic determinant and compare with each option.
