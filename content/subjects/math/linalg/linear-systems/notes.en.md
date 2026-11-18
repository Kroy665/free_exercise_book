# Systems of Linear Equations

## Matrix form and consistency {#matrix-form}

A system of $m$ linear equations in $n$ unknowns over a field $F$ (here $\R$ or $\C$)

$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i, \qquad i = 1, \dots, m,$$

is written $AX = B$, where:

- $A = (a_{ij})$ is the $m \times n$ **coefficient matrix**;
- $X = (x_1, \dots, x_n)^T$ is the column of unknowns;
- $B = (b_1, \dots, b_m)^T$ is the column of constants.

The **augmented matrix** is $[A \mid B]$, the $m \times (n + 1)$ matrix obtained by adjoining $B$ as an extra column. For example,

$$\begin{aligned} 2x - y &= 3 \\ x + 4z &= 1 \end{aligned} \quad\longrightarrow\quad [A \mid B] = \left(\begin{array}{ccc|c} 2 & -1 & 0 & 3 \\ 1 & 0 & 4 & 1 \end{array}\right).$$

Note the $0$ entries for missing unknowns, and keep the columns in a fixed order $x, y, z$.

- The system is **homogeneous** if $B = O$, and **non-homogeneous** otherwise.
- It is **consistent** if it has at least one solution, and **inconsistent** otherwise.

**Rank.** The rank $\rho(A)$ is the order of the largest non-vanishing minor of $A$. Equivalently, it is the number of non-zero rows in any row echelon form of $A$, or the number of linearly independent rows (or columns). All these definitions give the same number, so questions are convention-safe.

:::keyfacts
- **Rouché–Capelli theorem.** $AX = B$ is consistent $\iff \rho(A) = \rho([A \mid B])$.
- Always $\rho(A) \le \rho([A \mid B]) \le \rho(A) + 1$.
:::

**Proof idea.** $AX = x_1C_1 + \cdots + x_nC_n$, where $C_j$ are the columns of $A$. So a solution exists exactly when $B$ is a linear combination of the columns, that is, when adjoining $B$ does not enlarge the column space. That is the statement $\rho([A \mid B]) = \rho(A)$.

:::exam-tip
In an echelon form of $[A \mid B]$, inconsistency shows up as a row $(0\ 0\ \cdots\ 0 \mid c)$ with $c \ne 0$. That row says $0 = c$, and it is exactly the case $\rho([A\mid B]) = \rho(A) + 1$.
:::

## Unique, infinitely many or no solutions {#solution-cases}

Let $r = \rho(A)$ and $r' = \rho([A \mid B])$, with $n$ unknowns.

| Ranks | Conclusion |
|:---|:---|
| $r < r'$ | inconsistent: no solution |
| $r = r' = n$ | exactly one solution |
| $r = r' < n$ | infinitely many solutions, with $n - r$ free parameters |

In the last case, choose $r$ unknowns whose columns give a non-zero $r \times r$ minor (the **pivot** or basic variables). The other $n - r$ unknowns can take arbitrary values, and the basic ones are then determined. So the solution is an $(n - r)$-parameter family.

For a **square** system ($m = n$), $\det A \ne 0 \iff r = n$, and then the solution is unique for every $B$.

**Geometry in two unknowns.** Each equation is a line. Two lines meet in one point (unique solution), are parallel (none) or coincide (infinitely many):

```plot
title: $x + y = 2$ meets $x - y = 0$ once; $x + y = 4$ is parallel to $x + y = 2$
x: -1, 5
y: -1, 5
f: 2 - x | $x + y = 2$
f: x | $x - y = 0$
f: 4 - x | $x + y = 4$
point: 1, 1 | $(1, 1)$
```

**Geometry in three unknowns.** Each equation is a plane in $\R^3$.

| $r$ | $r'$ | Three planes |
|:---:|:---:|:---|
| 3 | 3 | meet in exactly one point |
| 2 | 2 | have a common line |
| 1 | 1 | all coincide (a common plane) |
| 2 | 3 | no common point (a triangular prism, or two parallel planes) |
| 1 | 2 | parallel, not all coincident |

:::caution
"More unknowns than equations" does **not** guarantee infinitely many solutions for a non-homogeneous system. $x + y + z = 1,\ x + y + z = 2$ has 3 unknowns, 2 equations and no solution ($r = 1$, $r' = 2$). What is true: **if** such a system is consistent, it has infinitely many solutions, because $r \le m < n$.
:::

## Structure of the solution set {#solution-structure}

Suppose $X_0$ is one solution of $AX = B$ (a **particular solution**). Then

$$\{X : AX = B\} = \{X_0 + Y : AY = O\}.$$

In words: **general solution = particular solution + general solution of the associated homogeneous system.**

**Why.** If $AX = B$, then $A(X - X_0) = B - B = O$. Conversely, if $AY = O$, then $A(X_0 + Y) = B$.

Consequences:

- The difference of two solutions of $AX = B$ solves $AX = O$.
- If $X_1, X_2$ solve $AX = B$, then so does $\lambda X_1 + (1 - \lambda)X_2$ for every scalar $\lambda$, since $A(\lambda X_1 + (1-\lambda)X_2) = \lambda B + (1-\lambda)B = B$. In particular $\tfrac12(X_1 + X_2)$ is a solution, but $X_1 + X_2$ is not (it gives $2B$) unless $B = O$.
- Over $\R$ or $\C$, a linear system has **0, 1 or infinitely many** solutions. It can never have exactly two: two distinct solutions give the whole line $X_1 + t(X_2 - X_1)$.
- The solution set of $AX = B$ is a subspace **only when $B = O$**. For $B \ne O$ it does not contain $O$. It is a translate (coset) $X_0 + N(A)$ of the null space $N(A)$, sometimes called an affine subspace.

**Example.** For $x + y + z = 3$, $x + 2y + 3z = 4$, $2x + 3y + 4z = 7$, the third equation is the sum of the first two, so $r = r' = 2$ and there is $3 - 2 = 1$ free parameter. Subtracting the first equation from the second gives $y + 2z = 1$. Putting $z = t$:

$$(x, y, z) = (2 + t,\ 1 - 2t,\ t) = \underbrace{(2, 1, 0)}_{X_0} + t\underbrace{(1, -2, 1)}_{\text{spans } N(A)}.$$

:::exam-tip
To test an option for a general solution, substitute it into **every** equation. Checking the first equation alone is a classic trap: a wrong family can satisfy it and still fail the second.
:::

## Homogeneous systems and the solution space {#homogeneous}

The homogeneous system $AX = O$, with $A$ an $m \times n$ matrix, has these properties.

:::keyfacts
- It is **always consistent**: $X = O$ (the trivial solution) works, and $\rho(A) = \rho([A \mid O])$ automatically.
- Its solution set $N(A) = \{X \in F^n : AX = O\}$ is a **subspace** of $F^n$ (the null space or solution space).
- $\dim N(A) = n - \rho(A)$. This is the rank–nullity relation for $A$.
- A **non-trivial solution exists** $\iff \rho(A) < n$.
- For **square** $A$: a non-trivial solution exists $\iff \det A = 0$.
- If $m < n$ (fewer equations than unknowns), a non-trivial solution always exists, since $\rho(A) \le m < n$.
:::

Closure is immediate: if $AY_1 = AY_2 = O$, then $A(\alpha Y_1 + \beta Y_2) = O$.

A **basis** of the solution space comes from the free variables. Set one free variable equal to 1 and the others to 0, solve for the basic variables, and repeat. This gives $n - r$ independent solutions, called a **fundamental set**.

**Example.** $x + 2y - z = 0$, $2x + y + z = 0$. Subtracting twice the first from the second gives $-3y + 3z = 0$, so $y = z$ and $x = -2y + z = -z$. With $z = t$, the solutions are $t(-1, 1, 1)$. The rank is 2, so the dimension is $3 - 2 = 1$, a line through the origin.

**Example.** $x + 2y - z + w = 0$, $2x + 4y - 2z + 2w = 0$, $x + 2y + z + 3w = 0$. The second row is twice the first, so $\rho(A) = 2$, not 3. The dimension is $4 - 2 = 2$.

:::caution
$\dim N(A) = n - \rho(A)$, **not** $n - m$. When some equations are dependent, the number of equations overstates the rank. Always find the rank first.
:::

:::exam-tip
For a square homogeneous system with a parameter, set $\det A = 0$ and solve; those are the values giving non-trivial solutions. For $kx + y + z = 0$, $x + ky + z = 0$, $x + y + kz = 0$: $\det A = (k - 1)^2(k + 2)$, so $k = 1$ or $k = -2$. At $k = 1$ the rank is 1 (a plane of solutions); at $k = -2$ the rank is 2 (a line).
:::

## Gauss and Gauss–Jordan elimination {#elimination}

**Elementary row operations** on $[A \mid B]$:

1. interchange two rows, $R_i \leftrightarrow R_j$;
2. multiply a row by a non-zero scalar, $R_i \to cR_i$ with $c \ne 0$;
3. add a multiple of one row to another, $R_i \to R_i + cR_j$.

Each operation is invertible, so it gives an **equivalent** system with the same solution set. It also preserves both ranks. Column operations on $A$ are not allowed while solving, because they mix up the unknowns.

- **Gaussian elimination:** reduce $[A \mid B]$ to row echelon form, then use back substitution.
- **Gauss–Jordan:** continue to the **reduced** row echelon form, where each pivot is 1 and is the only non-zero entry in its column. The solution can then be read off directly.

**Example (unique solution).** $x + y + 2z = 9$, $2x + 4y - 3z = 1$, $3x + 6y - 5z = 0$.

$$\left(\begin{array}{ccc|c} 1 & 1 & 2 & 9 \\ 2 & 4 & -3 & 1 \\ 3 & 6 & -5 & 0 \end{array}\right) \xrightarrow[R_3 - 3R_1]{R_2 - 2R_1} \left(\begin{array}{ccc|c} 1 & 1 & 2 & 9 \\ 0 & 2 & -7 & -17 \\ 0 & 3 & -11 & -27 \end{array}\right) \xrightarrow{R_3 - \frac32 R_2} \left(\begin{array}{ccc|c} 1 & 1 & 2 & 9 \\ 0 & 2 & -7 & -17 \\ 0 & 0 & -\frac12 & -\frac32 \end{array}\right).$$

Back substitution gives $z = 3$, then $2y = -17 + 21$ so $y = 2$, then $x = 9 - 2 - 6 = 1$.

**Reading the echelon form of $[A \mid B]$:**

| Echelon form shows | Conclusion |
|:---|:---|
| a row $(0 \cdots 0 \mid c)$ with $c \ne 0$ | inconsistent |
| no such row, and a pivot in every column of $A$ | unique solution |
| no such row, and some column of $A$ without a pivot | infinitely many; the non-pivot columns are the free variables |

**Example (inconsistent).** $x + y = 1$, $2x + 2y = 3$: $R_2 - 2R_1$ gives $(0\ 0 \mid 1)$, which says $0 = 1$.

:::exam-tip
The rank by the sweep-out process is just the number of non-zero rows after elimination. One elimination of $[A \mid B]$ gives both $\rho(A)$ and $\rho([A\mid B])$: ignore the last column for the first.
:::

## The matrix method and Cramer's rule {#matrix-method}

If $A$ is **square** and $\det A \ne 0$, then $A^{-1}$ exists, and $AX = B$ has the unique solution

$$X = A^{-1}B = \frac{1}{\det A}\,(\operatorname{adj} A)\,B.$$

**Example.** $x + y + z = 3$, $2x - y + z = 2$, $x + 2y - z = 2$. Here $\det A = 7$ and

$$\operatorname{adj}A = \begin{pmatrix} -1 & 3 & 2 \\ 3 & -2 & 1 \\ 5 & -1 & -3 \end{pmatrix}, \qquad (\operatorname{adj}A)B = \begin{pmatrix} 7 \\ 7 \\ 7 \end{pmatrix}, \qquad X = \frac17\begin{pmatrix} 7 \\ 7 \\ 7 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.$$

**When $\det A = 0$.** Multiplying $AX = B$ by $\operatorname{adj}A$ and using $(\operatorname{adj}A)A = (\det A)I = O$ gives $(\operatorname{adj}A)B = O$ for any solution $X$. Hence:

- $\det A = 0$ and $(\operatorname{adj}A)B \ne O$ $\Rightarrow$ **inconsistent**.
- $\det A = 0$ and $(\operatorname{adj}A)B = O$ $\Rightarrow$ **no conclusion yet**: the system may have infinitely many solutions or none. Use ranks or elimination.

:::caution
Some school texts state that "$\det A = 0$ and $(\operatorname{adj}A)B = O$" means infinitely many solutions. This is **false** in general. For $A$ with every entry 1, $\operatorname{adj}A = O$, so $(\operatorname{adj}A)B = O$ for every $B$. Yet $x + y + z = 1$, $x + y + z = 2$, $x + y + z = 3$ is inconsistent.
:::

**Cramer's rule** (from the Determinants topic): if $\Delta = \det A \ne 0$, then $x_j = \Delta_j / \Delta$, where $\Delta_j$ is $\det A$ with column $j$ replaced by $B$. It is the matrix method written out entry by entry.

:::exam-tip
The matrix method and Cramer's rule apply only to square systems with $\det A \ne 0$. For $\det A = 0$, or for non-square systems, use ranks or elimination. To check an answer, substitute it into all the equations. This takes seconds and catches $\Delta_j/\Delta$ inversions and sign slips.
:::

## Systems with a parameter {#parameter-systems}

The standard question is: "find the values of $k$ (or $\lambda, \mu$) for which the system has no solution, a unique solution or infinitely many solutions."

**Recipe for a square system.**

1. Compute $\det A$ as a function of the parameter.
2. Where $\det A \ne 0$: **unique** solution, whatever the right-hand side.
3. At each root of $\det A = 0$: substitute and reduce $[A \mid B]$. If $\rho(A) < \rho([A\mid B])$ there is **no** solution; if they are equal there are **infinitely many**.

Step 3 must be done separately for **each** root. The roots often behave differently.

**Example.** $x + y + z = 6$, $x + 2y + 3z = 10$, $x + 2y + \lambda z = \mu$. Subtracting the second equation from the third gives

$$(\lambda - 3)z = \mu - 10.$$

| Condition | $\rho(A)$, $\rho([A\mid B])$ | Solutions |
|:---|:---:|:---|
| $\lambda \ne 3$ (any $\mu$) | 3, 3 | unique, $z = \frac{\mu - 10}{\lambda - 3}$ |
| $\lambda = 3$, $\mu \ne 10$ | 2, 3 | none |
| $\lambda = 3$, $\mu = 10$ | 2, 2 | infinitely many (one parameter) |

**Example (homogeneous).** $x - ky + z = 0$, $kx + 3y - kz = 0$, $3x + y - z = 0$. Here $\det A = 2(k - 2)(k + 3)$, so non-trivial solutions exist exactly for $k = 2$ and $k = -3$.

**Non-square or right-hand-side parameters.** Reduce $[A \mid B]$ and impose the condition that the last entry of each zero row of $A$ vanishes. For example, $x + y + z = 1$, $x + 2y + 4z = k$, $x + 4y + 10z = k^2$ reduces to $y + 3z = k - 1$ and $3y + 9z = k^2 - 1$. It is consistent iff $k^2 - 1 = 3(k - 1)$, that is, $k = 1$ or $k = 2$.

:::caution
A root of $\det A = 0$ does **not** automatically give infinitely many solutions. For $ax + y + z = 1$, $x + ay + z = 1$, $x + y + az = 1$, we have $\det A = (a - 1)^2(a + 2)$. At $a = 1$ all three equations coincide (infinitely many solutions). At $a = -2$, adding the three equations gives $0 = 3$ (no solution).
:::

## Quick checks and traps {#exam-tips}

- **Consistency** is a rank test: $\rho(A) = \rho([A\mid B])$. A determinant only tells you about uniqueness, and only for square systems.
- **Count parameters** as $n - \rho(A)$: unknowns minus rank, never unknowns minus equations.
- **Homogeneous** systems are never inconsistent. "Non-trivial solution" means $\rho(A) < n$, or $\det A = 0$ when $A$ is square.
- **Fewer equations than unknowns:** a homogeneous system has a non-trivial solution; a non-homogeneous one has either none or infinitely many.
- **Two distinct solutions** imply infinitely many (over $\R$ or $\C$).
- **$\tfrac12(X_1 + X_2)$** of two solutions is again a solution; $X_1 + X_2$ is not when $B \ne O$; $X_1 - X_2$ solves the homogeneous system.
- **$(\operatorname{adj}A)B \ne O$ with $\det A = 0$** means inconsistent; $(\operatorname{adj}A)B = O$ decides nothing.
- **Parameter questions:** test every root of $\det A = 0$ separately.
- **Verify by substitution.** Put a candidate solution into all the equations; it is faster than re-solving.
