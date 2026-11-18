import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.linear-systems")

# ---------------------------------------------------------------- matrix form, consistency
T.single(1, ["matrix-form"],
    r"A system $AX = B$ of $m$ linear equations in $n$ unknowns is consistent if and only if",
    [r"$\rho(A) = \rho([A \mid B])$",
     r"$\rho(A) = n$",
     r"$\det A \ne 0$",
     r"$\rho([A \mid B]) = \rho(A) + 1$"],
    r"""By the Rouché–Capelli theorem, $AX = B$ has a solution exactly when $B$ lies in the column space of $A$, that is, when
$$\rho(A) = \rho([A \mid B]).$$

- $\rho(A) = n$ concerns **uniqueness**, not existence: $x + y = 1$, $x + y = 2$, $x - y = 0$ has $\rho(A) = 2 = n$ but no solution.
- $\det A \ne 0$ is sufficient (for square $A$) but not necessary: $x + y = 2$, $2x + 2y = 4$ is consistent with $\det A = 0$.
- $\rho([A\mid B]) = \rho(A) + 1$ is precisely the **inconsistent** case.""")

T.single(1, ["matrix-form"],
    r"The augmented matrix of the system $2x - y = 3,\ x + 4z = 1$ in the unknowns $x, y, z$ (in that order) is",
    [r"$\left(\begin{array}{ccc|c} 2 & -1 & 0 & 3 \\ 1 & 0 & 4 & 1 \end{array}\right)$",
     r"$\left(\begin{array}{cc|c} 2 & -1 & 3 \\ 1 & 4 & 1 \end{array}\right)$",
     r"$\left(\begin{array}{ccc|c} 2 & 1 & 0 & 3 \\ 1 & 0 & 4 & 1 \end{array}\right)$",
     r"$\left(\begin{array}{ccc|c} 2 & -1 & 3 & 0 \\ 1 & 4 & 1 & 0 \end{array}\right)$"],
    r"""Write each equation with all three unknowns, using $0$ for a missing one:
$$2x - 1y + 0z = 3, \qquad 1x + 0y + 4z = 1.$$
So $[A \mid B] = \left(\begin{array}{ccc|c} 2 & -1 & 0 & 3 \\ 1 & 0 & 4 & 1 \end{array}\right)$.

The $2 \times 3$ option drops the zero coefficients and puts $4$ under $y$; the third loses the sign of $-y$; the last one is not an augmented matrix of this system at all.""")

T.single(1, ["matrix-form", "elimination"],
    r"While reducing the augmented matrix of a system in $x, y, z$, one row becomes $(0\ \ 0\ \ 0 \mid 5)$. Then the system",
    [r"has no solution",
     r"has infinitely many solutions",
     r"has a unique solution with $z = 5$",
     r"has the unique solution $x = y = z = 0$"],
    r"""The row reads $0x + 0y + 0z = 5$, that is, $0 = 5$, which no $(x, y, z)$ satisfies. Equivalently, $\rho([A \mid B]) = \rho(A) + 1$, so the system is **inconsistent**.

A zero row $(0\ 0\ 0 \mid 0)$ would only signal a dependent equation; it is the non-zero last entry that makes the system impossible.""")

# ---------------------------------------------------------------- solution cases
T.single(1, ["solution-cases"],
    r"A consistent system in $6$ unknowns has $\rho(A) = \rho([A \mid B]) = 4$. The number of arbitrary parameters in its general solution is",
    [r"$2$", r"$4$", r"$6$", r"$0$"],
    r"""When $\rho(A) = \rho([A\mid B]) = r < n$, the solution has $n - r$ free parameters:
$$n - r = 6 - 4 = 2.$$
$4$ is the number of basic (pivot) unknowns, not free ones; $0$ would need $r = n$.""")

T.single(1, ["parameter-systems", "solution-cases"],
    r"The system $2x + 3y = 5,\ 4x + ky = 10$ has infinitely many solutions when $k$ equals",
    [r"$6$", r"$-6$", r"$3$", r"no real value of $k$"],
    r"""For infinitely many solutions the two equations must be the same line. The right-hand sides are in the ratio $10 : 5 = 2$, so we need
$$\frac{4}{2} = \frac{k}{3} = \frac{10}{5} = 2 \implies k = 6.$$
Then the second equation is twice the first, and $\rho(A) = \rho([A\mid B]) = 1 < 2$.

For $k \ne 6$, $\det A = 2k - 12 \ne 0$ and the solution is unique, so no other value works.""")

T.match(2, ["solution-cases"],
    r"A system $AX = B$ has $3$ unknowns. Match each rank condition in List I with the nature of its solution set in List II.",
    [r"$\rho(A) = \rho([A \mid B]) = 3$",
     r"$\rho(A) = \rho([A \mid B]) = 2$",
     r"$\rho(A) = 2,\ \rho([A \mid B]) = 3$",
     r"$\rho(A) = \rho([A \mid B]) = 1$"],
    [r"no solution",
     r"exactly one solution",
     r"a one-parameter family of solutions",
     r"a two-parameter family of solutions"],
    [r"A-2, B-3, C-1, D-4",
     r"A-2, B-4, C-1, D-3",
     r"A-3, B-2, C-1, D-4",
     r"A-2, B-3, C-4, D-1"],
    r"""Use $r = \rho(A)$, $r' = \rho([A\mid B])$ and $n = 3$:

- A: $r = r' = n$, so exactly one solution (2).
- B: $r = r' = 2$, so $3 - 2 = 1$ parameter (3).
- C: $r < r'$, so inconsistent (1).
- D: $r = r' = 1$, so $3 - 1 = 2$ parameters (4).

Hence A-2, B-3, C-1, D-4. Swapping B and D comes from counting parameters as $r$ instead of $n - r$.""")

# ---------------------------------------------------------------- solution structure
T.single(2, ["solution-structure"],
    r"$X_1$ and $X_2$ are two distinct solutions of $AX = B$, where $B \ne O$. Which of the following is also a solution of $AX = B$?",
    [r"$\tfrac12(X_1 + X_2)$", r"$X_1 + X_2$", r"$X_1 - X_2$", r"$2X_1 + X_2$"],
    r"""Apply $A$ to each option:
$$A\left(\tfrac12(X_1 + X_2)\right) = \tfrac12(B + B) = B. \;\checkmark$$

- $A(X_1 + X_2) = 2B \ne B$, since $B \ne O$.
- $A(X_1 - X_2) = O$: this solves the **homogeneous** system instead.
- $A(2X_1 + X_2) = 3B \ne B$.

In general, $\lambda X_1 + \mu X_2$ solves $AX = B$ exactly when $\lambda + \mu = 1$.""")

T.single(2, ["solution-structure", "elimination"],
    r"The general solution of $x + y + z = 3,\ x + 2y + 3z = 4,\ 2x + 3y + 4z = 7$ is ($t$ arbitrary)",
    [r"$(x, y, z) = (2 + t,\ 1 - 2t,\ t)$",
     r"$(x, y, z) = (1 + t,\ 2 - 2t,\ t)$",
     r"$(x, y, z) = (2 - t,\ 1 + 2t,\ t)$",
     r"$(x, y, z) = (2,\ 1,\ 0)$ only"],
    r"""The third equation is the sum of the first two, so $\rho(A) = \rho([A\mid B]) = 2$, and there is $3 - 2 = 1$ parameter.

Subtracting the first equation from the second gives $y + 2z = 1$. Put $z = t$: then $y = 1 - 2t$ and $x = 3 - y - z = 2 + t$.
$$(x, y, z) = (2, 1, 0) + t(1, -2, 1).$$

**Check:** $(1 + t, 2 - 2t, t)$ satisfies the first equation but gives $5$, not $4$, in the second. $(2 - t, 1 + 2t, t)$ fails the first. $(2, 1, 0)$ is only one particular solution.""")

T.statements(2, ["solution-structure", "homogeneous"],
    r"$A$ is an $m \times n$ real matrix and $B \ne O$. Consider the following statements:",
    [r"The set of all solutions of $AX = B$ is a subspace of $\R^n$.",
     r"The difference of any two solutions of $AX = B$ is a solution of $AX = O$.",
     r"If $X_0$ is one solution of $AX = B$, every solution is $X_0 + Y$ for some $Y$ with $AY = O$."],
    [r"2 and 3 only", r"1, 2 and 3", r"2 only", r"1 and 3 only"],
    r"""- **1 is false.** A subspace contains $O$, but $AO = O \ne B$. The solution set is the translate $X_0 + N(A)$, not a subspace.
- **2 is true.** $A(X_1 - X_2) = B - B = O$.
- **3 is true.** For any solution $X$, put $Y = X - X_0$; by statement 2, $AY = O$.

So the answer is 2 and 3 only.""")

# ---------------------------------------------------------------- homogeneous
T.single(1, ["homogeneous"],
    r"A homogeneous system of $3$ linear equations in $5$ unknowns",
    [r"always has a non-trivial solution",
     r"has only the trivial solution",
     r"may be inconsistent",
     r"has a non-trivial solution only if its rank is $3$"],
    r"""$\rho(A) \le 3 < 5 = n$, so the solution space has dimension $5 - \rho(A) \ge 2$. A non-trivial solution always exists.

A homogeneous system is never inconsistent: $X = O$ always works. The rank can be $1$, $2$ or $3$; non-trivial solutions exist in every case.""")

T.single(1, ["homogeneous"],
    r"The dimension of the solution space of the single equation $x + y + z = 0$ in $\R^3$ is",
    [r"$2$", r"$1$", r"$3$", r"$0$"],
    r"""Here $A = (1\ 1\ 1)$ has rank $1$, so
$$\dim N(A) = n - \rho(A) = 3 - 1 = 2.$$
The solutions form a plane through the origin, with basis $(1, -1, 0)$ and $(1, 0, -1)$.

$1$ is the number of equations (the rank), not the dimension of the solution space.""")

T.single(2, ["homogeneous"],
    r"The solution space of $x - y + z = 0,\ 2x + y - z = 0$ is spanned by",
    [r"$(0, 1, 1)$", r"$(1, 1, 0)$", r"$(0, 1, -1)$", r"$(1, 0, -1)$"],
    r"""Add the equations: $3x = 0$, so $x = 0$. Then $-y + z = 0$, so $y = z$. With $z = t$:
$$(x, y, z) = t(0, 1, 1).$$
The rank is $2$, so the dimension is $3 - 2 = 1$, as found.

**Check the others:** $(1, 1, 0)$ and $(1, 0, -1)$ satisfy the first equation but give $3$ in the second; $(0, 1, -1)$ gives $-2$ in the first.""")

T.single(2, ["homogeneous", "parameter-systems"],
    r"The system $kx + y + z = 0,\ x + ky + z = 0,\ x + y + kz = 0$ has a non-trivial solution if and only if",
    [r"$k = 1$ or $k = -2$",
     r"$k = -1$ or $k = 2$",
     r"$k = 1$ only",
     r"$k \ne 1$ and $k \ne -2$"],
    r"""A square homogeneous system has a non-trivial solution iff $\det A = 0$. Adding all columns to the first,
$$\det A = (k + 2)\begin{vmatrix} 1 & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{vmatrix} = (k + 2)(k - 1)^2.$$
So $k = 1$ or $k = -2$.

"$k = 1$ only" forgets the factor $k + 2$ from the column sum. "$k \ne 1, -2$" is the condition for **only** the trivial solution.""")

T.single(2, ["homogeneous", "parameter-systems"],
    r"The system $x + y + z = 0,\ x + 2y + 3z = 0,\ x + 3y + kz = 0$ has a non-trivial solution for",
    [r"$k = 5$", r"$k = 4$", r"$k = -5$", r"every $k \ne 5$"],
    r"""Set $\det A = 0$:
$$\begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 3 & k \end{vmatrix} = (2k - 9) - (k - 3) + (3 - 2) = k - 5.$$
So $k = 5$. Then the rows $(1,1,1), (1,2,3), (1,3,5)$ are in arithmetic progression ($R_1 + R_3 = 2R_2$), and the solution space is the line $t(1, -2, 1)$.

$k = 4$ comes from continuing the pattern $1, 2, 3$ instead of solving. For $k \ne 5$ only the trivial solution exists.""")

T.single(3, ["homogeneous"],
    r"The dimension of the solution space of $x + 2y - z + w = 0,\ 2x + 4y - 2z + 2w = 0,\ x + 2y + z + 3w = 0$ in $\R^4$ is",
    [r"$2$", r"$1$", r"$3$", r"$0$"],
    r"""The second equation is twice the first, so
$$A \sim \begin{pmatrix} 1 & 2 & -1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \qquad \rho(A) = 2.$$
Hence $\dim N(A) = 4 - 2 = 2$. A basis is $(-2, 1, 0, 0)$ and $(-2, 0, -1, 1)$.

The trap is $4 - 3 = 1$: it counts **equations** instead of the **rank**.""")

T.single(3, ["homogeneous", "parameter-systems"],
    r"For the system $kx + y + z = 0,\ x + ky + z = 0,\ x + y + kz = 0$, let $d_1$ and $d_{-2}$ be the dimensions of its solution space when $k = 1$ and $k = -2$. Then",
    [r"$d_1 = 2,\ d_{-2} = 1$",
     r"$d_1 = 1,\ d_{-2} = 2$",
     r"$d_1 = d_{-2} = 1$",
     r"$d_1 = d_{-2} = 2$"],
    r"""- $k = 1$: all three equations are $x + y + z = 0$, so $\rho(A) = 1$ and $d_1 = 3 - 1 = 2$ (a plane).
- $k = -2$: the rows $(-2, 1, 1)$, $(1, -2, 1)$, $(1, 1, -2)$ sum to zero, but any two are independent. So $\rho(A) = 2$ and $d_{-2} = 3 - 2 = 1$, the line $t(1, 1, 1)$.

The double root $(k - 1)^2$ of $\det A$ matches the larger solution space at $k = 1$, but the dimension must still be found from the rank.""")

T.statements(2, ["homogeneous"],
    r"Consider the following statements about a homogeneous system $AX = O$ with $A$ an $m \times n$ real matrix:",
    [r"It is always consistent.",
     r"If $m < n$, it has a non-trivial solution.",
     r"If $m = n$ and $\det A \ne 0$, it has infinitely many solutions."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""- **1 is true:** $X = O$ is a solution.
- **2 is true:** $\rho(A) \le m < n$, so $\dim N(A) = n - \rho(A) \ge 1$.
- **3 is false:** $\det A \ne 0$ means $\rho(A) = n$, so $N(A) = \{O\}$: only the trivial solution.

So the answer is 1 and 2 only.""")

T.assertion_reason(2, ["homogeneous"],
    r"The system $x + 2y + 3z = 0,\ 4x + 5y + 6z = 0,\ 7x + 8y + 9z = 0$ has a non-trivial solution.",
    r"A homogeneous system of $n$ equations in $n$ unknowns has a non-trivial solution if and only if the determinant of its coefficient matrix is zero.",
    0,
    r"""**R is true:** a non-trivial solution exists iff $\rho(A) < n$, and for square $A$ that means $\det A = 0$.

**A is true, by R:** $R_3 - R_2 = R_2 - R_1 = (3, 3, 3)$, so the rows are dependent and $\det A = 0$. Indeed $(1, -2, 1)$ is a solution: $1 - 4 + 3 = 0$, $4 - 10 + 6 = 0$, $7 - 16 + 9 = 0$.

R is exactly the reason, so the answer is (0).""")

T.assertion_reason(2, ["homogeneous", "solution-cases"],
    r"Every system of $3$ linear equations in $4$ unknowns has infinitely many solutions.",
    r"A homogeneous system with fewer equations than unknowns has a non-trivial solution.",
    3,
    r"""**R is true:** $\rho(A) \le 3 < 4$, so the solution space has dimension at least $1$.

**A is false:** a non-homogeneous system can be inconsistent. For example,
$$x + y + z + w = 1,\quad x + y + z + w = 2,\quad x - y = 0$$
has $\rho(A) = 2$ but $\rho([A\mid B]) = 3$, so no solution. A consistent system of this size does have infinitely many solutions.

So A is false and R is true: (3).""")

T.assertion_reason(3, ["homogeneous", "solution-structure"],
    r"For an $m \times n$ real matrix $A$, the set of solutions of $AX = O$ is a subspace of $\R^n$.",
    r"For an $m \times n$ real matrix $A$, the set of solutions of $AX = B$ is a subspace of $\R^n$ for every $B \in \R^m$.",
    2,
    r"""**A is true:** $O$ is a solution, and if $AY_1 = AY_2 = O$ then $A(\alpha Y_1 + \beta Y_2) = O$.

**R is false:** for $B \ne O$ the zero vector is not a solution, since $AO = O \ne B$. The set is a translate $X_0 + N(A)$, or empty. For example, $x + y = 1$ has solutions $(1, 0)$ and $(0, 1)$, but their sum $(1, 1)$ is not a solution.

So (2).""")

# ---------------------------------------------------------------- elimination / matrix method
T.single(2, ["matrix-method"],
    r"Solving $x + y + z = 6,\ x - y + z = 2,\ 2x + y - z = 1$ by the matrix method gives $(x, y, z) =$",
    [r"$(1, 2, 3)$", r"$(3, 2, 1)$", r"$(1, 3, 2)$", r"$(2, 1, 3)$"],
    r"""$\det A = 1(1 - 1) - 1(-1 - 2) + 1(1 + 2) = 6 \ne 0$, so $X = A^{-1}B$ is unique. With
$$\operatorname{adj}A = \begin{pmatrix} 0 & 2 & 2 \\ 3 & -3 & 0 \\ 3 & 1 & -2 \end{pmatrix}, \qquad X = \frac16\begin{pmatrix} 0 & 2 & 2 \\ 3 & -3 & 0 \\ 3 & 1 & -2 \end{pmatrix}\begin{pmatrix} 6 \\ 2 \\ 1 \end{pmatrix} = \frac16\begin{pmatrix} 6 \\ 12 \\ 18 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}.$$

**Fast check:** subtracting the first two equations gives $2y = 4$, so $y = 2$; then $x + z = 4$ and $2x - z = -1$ give $x = 1$, $z = 3$. $(3, 2, 1)$ fails the third equation ($6 + 2 - 1 = 7$).""")

T.single(2, ["matrix-method"],
    r"For a square system $AX = B$, suppose $\det A = 0$ and $(\operatorname{adj}A)B \ne O$. Then the system",
    [r"is inconsistent",
     r"has a unique solution",
     r"has infinitely many solutions",
     r"may have infinitely many solutions or none"],
    r"""If $X$ were a solution, then multiplying $AX = B$ by $\operatorname{adj}A$ gives
$$(\operatorname{adj}A)B = (\operatorname{adj}A)AX = (\det A)X = O,$$
a contradiction. So there is **no** solution.

Example: $x + 2y = 1$, $2x + 4y = 3$ has $\det A = 0$ and $(\operatorname{adj}A)B = (-2, 1)^T \ne O$; it is inconsistent.

"Infinitely many or none" is the (inconclusive) verdict for $(\operatorname{adj}A)B = O$, not for $\ne O$.""")

T.single(3, ["matrix-method"],
    r"By Cramer's rule, the value of $y$ satisfying $x + 2y + 3z = 3,\ 2x - y + z = 6,\ 3x + y - 2z = 3$ is",
    [r"$-1$", r"$1$", r"$2$", r"$-2$"],
    r"""$$\Delta = \begin{vmatrix} 1 & 2 & 3 \\ 2 & -1 & 1 \\ 3 & 1 & -2 \end{vmatrix} = 30, \qquad \Delta_2 = \begin{vmatrix} 1 & 3 & 3 \\ 2 & 6 & 1 \\ 3 & 3 & -2 \end{vmatrix} = -30.$$
So $y = \Delta_2 / \Delta = -1$. The full solution is $(x, y, z) = (2, -1, 1)$, with $\Delta_1 = 60$ and $\Delta_3 = 30$.

$2$ is $x = \Delta_1/\Delta$, the value of the wrong unknown. **Check:** $2 - 2 + 3 = 3$, $4 + 1 + 1 = 6$, $6 - 1 - 2 = 3$.""")

T.statements(3, ["matrix-method", "solution-cases"],
    r"Consider the following statements about a non-homogeneous system $AX = B$ of $m$ equations in $n$ unknowns:",
    [r"If $m < n$, the system always has infinitely many solutions.",
     r"If $m = n$ and $\det A \ne 0$, the system has the unique solution $X = A^{-1}B$.",
     r"If $m = n$, $\det A = 0$ and $(\operatorname{adj}A)B = O$, the system has infinitely many solutions."],
    [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""- **1 is false:** $x + y + z = 1$, $x + y + z = 2$ ($m = 2 < 3 = n$) has no solution. Fewer equations only guarantee infinitely many solutions **if** the system is consistent.
- **2 is true:** $A^{-1}$ exists, and $AX = B \iff X = A^{-1}B$.
- **3 is false:** if every entry of $A$ is $1$ ($3 \times 3$), then $\operatorname{adj}A = O$, so $(\operatorname{adj}A)B = O$ for every $B$. Yet $x + y + z = 1, 2, 3$ is inconsistent.

So the answer is 2 only.""")

T.assertion_reason(2, ["matrix-method", "solution-cases"],
    r"The system $x + y = 2,\ 2x + 2y = 4$ has infinitely many solutions.",
    r"The determinant of the coefficient matrix of this system is zero.",
    1,
    r"""**A is true:** the second equation is twice the first, so $\rho(A) = \rho([A\mid B]) = 1 < 2$, with solutions $(2 - t, t)$.

**R is true:** $\det\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix} = 0$.

But R does not explain A. A zero determinant only rules out a unique solution: $x + y = 2$, $2x + 2y = 5$ has the same $A$ and **no** solution. The real reason is the rank equality $\rho(A) = \rho([A\mid B]) < n$. So (1).""")

T.assertion_reason(1, ["matrix-form", "solution-cases"],
    r"The system $x + y + z = 1,\ x + y + z = 2$ has no solution.",
    r"Here $\rho(A) = 1$ and $\rho([A \mid B]) = 2$, and a linear system is consistent if and only if these two ranks are equal.",
    0,
    r"""$[A \mid B] = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \end{array}\right) \to \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{array}\right)$, so $\rho(A) = 1$ and $\rho([A\mid B]) = 2$.

R is true (it states the ranks and the Rouché–Capelli theorem), and it is exactly why A holds: the ranks differ, so there is no solution. Answer (0).""")

# ---------------------------------------------------------------- parameter systems
T.single(2, ["parameter-systems"],
    r"The system $x + y + z = 1,\ x + 2y + 4z = k,\ x + 4y + 10z = k^2$ is consistent if and only if",
    [r"$k = 1$ or $k = 2$",
     r"$k = -1$ or $k = -2$",
     r"$k = 1$ or $k = -2$",
     r"$k$ is any real number"],
    r"""$\det A = 0$, so check consistency by elimination:
$$R_2 - R_1:\ y + 3z = k - 1, \qquad R_3 - R_1:\ 3y + 9z = k^2 - 1.$$
The left side of the second is $3$ times the first, so we need
$$k^2 - 1 = 3(k - 1) \iff k^2 - 3k + 2 = 0 \iff k = 1 \text{ or } 2.$$
For these values $\rho(A) = \rho([A\mid B]) = 2$, with infinitely many solutions; otherwise $\rho([A\mid B]) = 3$.

"Any real $k$" ignores that $\det A = 0$.""")

T.single(3, ["parameter-systems"],
    r"The system $ax + y + z = 1,\ x + ay + z = 1,\ x + y + az = 1$ has no solution if and only if",
    [r"$a = -2$", r"$a = 1$", r"$a = 2$", r"$a = 1$ or $a = -2$"],
    r"""$\det A = (a + 2)(a - 1)^2$. For $a \ne 1, -2$ the solution is unique. Test each root separately:

- $a = 1$: all three equations are $x + y + z = 1$, so there are infinitely many solutions.
- $a = -2$: adding the three equations gives $0 = 3$, so $\rho(A) = 2 < 3 = \rho([A\mid B])$, and there is **no** solution.

So only $a = -2$. "$a = 1$ or $a = -2$" is the trap of treating every root of $\det A = 0$ as inconsistent.""")

T.single(3, ["parameter-systems"],
    r"For real $k$, the system $x + y + z = 1,\ 2x + 3y + kz = 3,\ x + ky + 3z = 2$ has",
    [r"no solution for $k = 0$ and for $k = 3$, and a unique solution otherwise",
     r"infinitely many solutions for $k = 0$ and for $k = 3$, and a unique solution otherwise",
     r"no solution for $k = 0$ and infinitely many for $k = 3$",
     r"a unique solution for every real $k$"],
    r"""$$\det A = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & k \\ 1 & k & 3 \end{vmatrix} = (9 - k^2) - (6 - k) + (2k - 3) = -k(k - 3).$$
For $k \ne 0, 3$ the solution is unique. Test the roots:

- $k = 0$: $R_2 - 2R_1$: $y - 2z = 1$; $R_3 - R_1$: $-y + 2z = 1$. Adding gives $0 = 2$: **no** solution.
- $k = 3$: $R_2 - 2R_1$: $y + z = 1$; $R_3 - R_1$: $2y + 2z = 1$, so $y + z = \tfrac12$. These contradict: **no** solution.

In both cases $\rho(A) = 2$ and $\rho([A\mid B]) = 3$. Assuming $\det A = 0$ means "infinitely many" is the trap.""")

T.match(3, ["parameter-systems"],
    r"For the system $x + y + z = 6,\ x + 2y + 3z = 10,\ x + 2y + \lambda z = \mu$, match the values in List I with the outcome in List II.",
    [r"$\lambda = 3,\ \mu = 10$",
     r"$\lambda = 3,\ \mu = 11$",
     r"$\lambda = 4,\ \mu = 13$",
     r"$\lambda = 5,\ \mu = 12$"],
    [r"no solution",
     r"infinitely many solutions",
     r"a unique solution, with $z = 3$",
     r"a unique solution, with $z = 1$"],
    [r"A-2, B-1, C-3, D-4",
     r"A-1, B-2, C-3, D-4",
     r"A-2, B-1, C-4, D-3",
     r"A-2, B-3, C-1, D-4"],
    r"""Subtract the second equation from the third:
$$(\lambda - 3)z = \mu - 10.$$

- A: $0 \cdot z = 0$, so $\rho(A) = \rho([A\mid B]) = 2$: infinitely many (2).
- B: $0 \cdot z = 1$: no solution (1).
- C: $z = \frac{3}{1} = 3$, unique (3).
- D: $z = \frac{2}{2} = 1$, unique (4).

So A-2, B-1, C-3, D-4. Swapping A and B mixes up $\mu = 10$ (consistent) with $\mu \ne 10$.""")


def check():
    import sympy as sp
    x, y, z, w, k, a, lam, mu = sp.symbols("x y z w k a lam mu")
    X3 = (x, y, z)

    def ok(cond, label):
        if not cond:
            sys.exit(f"CHECK FAILED {label}")

    def nsol(A, B, syms):
        """'none', 'unique' or the number of free parameters (as 'inf<d>')."""
        A, B = sp.Matrix(A), sp.Matrix(B)
        r, r2 = A.rank(), A.row_join(B).rank()
        if r < r2:
            ok(sp.linsolve((A, B), *syms) == sp.EmptySet, "linsolve-none")
            return "none"
        if r == len(syms):
            return "unique"
        return f"inf{len(syms) - r}"

    # q1: rank criterion; counterexamples for the distractors
    ok(nsol([[1, 1], [1, 1], [1, -1]], [1, 2, 0], (x, y)) == "none", "q1 rank n but inconsistent")
    ok(sp.Matrix([[1, 1], [1, 1], [1, -1]]).rank() == 2, "q1 rank")
    ok(nsol([[1, 1], [2, 2]], [2, 4], (x, y)) == "inf1", "q1 det0 consistent")

    # q2: augmented matrix
    Am, Bm = sp.linear_eq_to_matrix([2 * x - y - 3, x + 4 * z - 1], X3)
    ok(Am.row_join(Bm) == sp.Matrix([[2, -1, 0, 3], [1, 0, 4, 1]]), "q2")

    # q3: zero row with nonzero last entry
    ok(sp.linsolve((sp.Matrix([[1, 0, 0], [0, 0, 0]]), sp.Matrix([1, 5])), *X3) == sp.EmptySet, "q3")

    # q4: 6 unknowns, rank 4 -> 2 parameters
    A = sp.Matrix(4, 6, lambda i, j: 1 if j in (i, i + 1, i + 2) else 0)
    ok(A.rank() == 4, "q4 rank")
    s6 = sp.symbols("u1:7")
    S = sp.linsolve((A, sp.Matrix([1, 2, 3, 4])), *s6)
    eq(len(set().union(*[e.free_symbols for e in list(S)[0]])), 2, "q4")

    # q5: k = 6
    for kv in [6, -6, 3]:
        r = nsol([[2, 3], [4, kv]], [5, 10], (x, y))
        ok((r == "inf1") == (kv == 6), f"q5 k={kv}")
    eq(sp.solve(sp.Matrix([[2, 3], [4, k]]).det(), k)[0], 6, "q5 det")

    # q6 match: rank conditions -> outcomes (examples)
    ok(nsol(sp.eye(3), [1, 2, 3], X3) == "unique", "q6 A")
    ok(nsol([[1, 0, 0], [0, 1, 0], [1, 1, 0]], [1, 1, 2], X3) == "inf1", "q6 B")
    ok(nsol([[1, 0, 0], [0, 1, 0], [1, 1, 0]], [1, 1, 3], X3) == "none", "q6 C")
    ok(nsol([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [1, 2, 3], X3) == "inf2", "q6 D")

    # q7: affine combinations
    A = sp.Matrix([[1, 1, 1], [1, 2, 3]]); B = sp.Matrix([3, 4])
    X1 = sp.Matrix([2, 1, 0]); X2 = sp.Matrix([3, -1, 1])
    ok(A * X1 == B and A * X2 == B, "q7 setup")
    ok(A * (X1 + X2) / 2 == B, "q7 key")
    ok(A * (X1 + X2) != B and A * (X1 - X2) != B and A * (2 * X1 + X2) != B, "q7 distractors")

    # q8: general solution
    A = sp.Matrix([[1, 1, 1], [1, 2, 3], [2, 3, 4]]); B = sp.Matrix([3, 4, 7])
    t = sp.symbols("t")
    good = lambda v: sp.simplify(A * sp.Matrix(v) - B) == sp.zeros(3, 1)
    ok(good([2 + t, 1 - 2 * t, t]), "q8 key")
    ok(not good([1 + t, 2 - 2 * t, t]) and not good([2 - t, 1 + 2 * t, t]), "q8 distractors")
    ok(nsol(A, B, X3) == "inf1", "q8 one parameter")
    S = list(sp.linsolve((A, B), *X3))[0]
    ok(sp.simplify(sp.Matrix(S).subs(z, t) - sp.Matrix([2 + t, 1 - 2 * t, t])) == sp.zeros(3, 1), "q8 linsolve")

    # q9 statements: 1 false (x+y=1 example), 2 & 3 true (structure)
    A = sp.Matrix([[1, 1]]); B = sp.Matrix([1])
    ok(A * sp.Matrix([1, 0]) == B and A * sp.Matrix([0, 1]) == B and A * sp.Matrix([1, 1]) != B, "q9 stmt1 false")
    ok(A * (sp.Matrix([1, 0]) - sp.Matrix([0, 1])) == sp.zeros(1, 1), "q9 stmt2")

    # q10: 3 x 5 homogeneous always nontrivial
    A = sp.Matrix([[1, 2, 0, 1, 3], [0, 1, 1, 0, 2], [1, 0, 2, 1, 0]])
    ok(len(A.nullspace()) == 5 - A.rank() and len(A.nullspace()) >= 2, "q10")

    # q11: x + y + z = 0 has a 2-dim solution space
    eq(len(sp.Matrix([[1, 1, 1]]).nullspace()), 2, "q11")

    # q12: spanned by (0,1,1)
    N = sp.Matrix([[1, -1, 1], [2, 1, -1]]).nullspace()
    ok(len(N) == 1 and N[0].cross(sp.Matrix([0, 1, 1])) == sp.zeros(3, 1), "q12")
    for v in ([1, 1, 0], [0, 1, -1], [1, 0, -1]):
        ok(sp.Matrix([[1, -1, 1], [2, 1, -1]]) * sp.Matrix(v) != sp.zeros(2, 1), f"q12 {v}")

    # q13: det = (k-1)^2 (k+2)
    Ak = sp.Matrix([[k, 1, 1], [1, k, 1], [1, 1, k]])
    eq(sp.factor(Ak.det()), (k - 1) ** 2 * (k + 2), "q13 det")
    ok(set(sp.solve(Ak.det(), k)) == {1, -2}, "q13 roots")

    # q14: det = k - 5
    A = sp.Matrix([[1, 1, 1], [1, 2, 3], [1, 3, k]])
    eq(A.det(), k - 5, "q14 det")
    N = A.subs(k, 5).nullspace()
    ok(len(N) == 1 and N[0].cross(sp.Matrix([1, -2, 1])) == sp.zeros(3, 1), "q14 nullspace")
    eq(len(A.subs(k, 4).nullspace()), 0, "q14 k=4 trivial")

    # q15: dimension 2
    A = sp.Matrix([[1, 2, -1, 1], [2, 4, -2, 2], [1, 2, 1, 3]])
    eq(A.rank(), 2, "q15 rank"); eq(len(A.nullspace()), 2, "q15")
    for v in ([-2, 1, 0, 0], [-2, 0, -1, 1]):
        ok(A * sp.Matrix(v) == sp.zeros(3, 1), "q15 basis")

    # q16: dims at k = 1 and k = -2
    eq(len(Ak.subs(k, 1).nullspace()), 2, "q16 k=1")
    N = Ak.subs(k, -2).nullspace()
    eq(len(N), 1, "q16 k=-2")
    ok(N[0].cross(sp.Matrix([1, 1, 1])) == sp.zeros(3, 1), "q16 line")

    # q17 statements: 1 true, 2 true (m<n example), 3 false (det != 0 -> trivial only)
    A = sp.Matrix([[1, 2, 3], [4, 5, 7]])
    ok(len(A.nullspace()) >= 1, "q17 stmt2")
    ok(len(sp.Matrix([[1, 2], [3, 4]]).nullspace()) == 0, "q17 stmt3 false")

    # q18 AR: det = 0 and (1,-2,1) is a solution
    A = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    eq(A.det(), 0, "q18 det"); ok(A * sp.Matrix([1, -2, 1]) == sp.zeros(3, 1), "q18 sol")

    # q19 AR: inconsistent 3x4 example
    X4 = (x, y, z, w)
    A = sp.Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, -1, 0, 0]])
    eq(A.rank(), 2, "q19 rank")
    ok(nsol(A, [1, 2, 0], X4) == "none", "q19 A false")
    ok(len(A.nullspace()) >= 1, "q19 R true")

    # q20 AR: R false (x + y = 1 example done in q9), A true (closure)
    A = sp.Matrix([[1, 2, 3], [2, 4, 6]])
    N = A.nullspace()
    ok(A * (2 * N[0] - 3 * N[1]) == sp.zeros(2, 1), "q20 closure")

    # q21: matrix method
    A = sp.Matrix([[1, 1, 1], [1, -1, 1], [2, 1, -1]]); B = sp.Matrix([6, 2, 1])
    eq(A.det(), 6, "q21 det")
    ok(A.adjugate() == sp.Matrix([[0, 2, 2], [3, -3, 0], [3, 1, -2]]), "q21 adj")
    ok(A.inv() * B == sp.Matrix([1, 2, 3]), "q21")
    ok(sp.linsolve((A, B), *X3) == sp.FiniteSet((1, 2, 3)), "q21 linsolve")
    for v in ([3, 2, 1], [1, 3, 2], [2, 1, 3]):
        ok(A * sp.Matrix(v) != B, f"q21 {v}")

    # q22: det 0 and adj(A)B != 0 -> inconsistent
    A = sp.Matrix([[1, 2], [2, 4]]); B = sp.Matrix([1, 3])
    eq(A.det(), 0, "q22 det")
    ok(A.adjugate() * B == sp.Matrix([-2, 1]), "q22 adjB")
    ok(nsol(A, B, (x, y)) == "none", "q22")

    # q23: Cramer
    A = sp.Matrix([[1, 2, 3], [2, -1, 1], [3, 1, -2]]); B = sp.Matrix([3, 6, 3])
    D = A.det(); eq(D, 30, "q23 D")
    Ds = []
    for i in range(3):
        Ai = A.copy(); Ai[:, i] = B; Ds.append(Ai.det())
    ok(Ds == [60, -30, 30], "q23 Dj")
    eq(Ds[1] / D, -1, "q23")
    ok(sp.linsolve((A, B), *X3) == sp.FiniteSet((2, -1, 1)), "q23 linsolve")

    # q24 statements: 1 false, 2 true, 3 false (all-ones counterexample)
    ok(nsol([[1, 1, 1], [1, 1, 1]], [1, 2], X3) == "none", "q24 stmt1")
    J = sp.ones(3, 3)
    ok(J.adjugate() == sp.zeros(3, 3), "q24 adj J = 0")
    ok(nsol(J, [1, 2, 3], X3) == "none", "q24 stmt3 false")

    # q25 AR: det 0 for both; one consistent, one not
    ok(nsol([[1, 1], [2, 2]], [2, 4], (x, y)) == "inf1", "q25 A")
    ok(nsol([[1, 1], [2, 2]], [2, 5], (x, y)) == "none", "q25 R not sufficient")

    # q26 AR: ranks 1 and 2
    A = sp.Matrix([[1, 1, 1], [1, 1, 1]]); B = sp.Matrix([1, 2])
    ok(A.rank() == 1 and A.row_join(B).rank() == 2, "q26 ranks")
    ok(sp.linsolve((A, B), *X3) == sp.EmptySet, "q26")

    # q27: consistent iff k = 1 or 2
    A = sp.Matrix([[1, 1, 1], [1, 2, 4], [1, 4, 10]])
    eq(A.det(), 0, "q27 det")
    good = [kv for kv in range(-5, 6) if nsol(A, [1, kv, kv ** 2], X3) != "none"]
    ok(good == [1, 2], f"q27 {good}")

    # q28: a = -2 none, a = 1 infinite
    Aa = sp.Matrix([[a, 1, 1], [1, a, 1], [1, 1, a]])
    eq(sp.factor(Aa.det()), (a + 2) * (a - 1) ** 2, "q28 det")
    ok(nsol(Aa.subs(a, -2), [1, 1, 1], X3) == "none", "q28 a=-2")
    ok(nsol(Aa.subs(a, 1), [1, 1, 1], X3) == "inf2", "q28 a=1")
    ok(nsol(Aa.subs(a, 2), [1, 1, 1], X3) == "unique", "q28 a=2")

    # q29: k = 0 and k = 3 both inconsistent
    Ak2 = sp.Matrix([[1, 1, 1], [2, 3, k], [1, k, 3]]); B = sp.Matrix([1, 3, 2])
    eq(sp.factor(Ak2.det()), -k * (k - 3), "q29 det")
    ok(nsol(Ak2.subs(k, 0), B, X3) == "none" and nsol(Ak2.subs(k, 3), B, X3) == "none", "q29")
    ok(nsol(Ak2.subs(k, 1), B, X3) == "unique", "q29 k=1")

    # q30 match: lambda, mu
    def sys30(l, m):
        return sp.Matrix([[1, 1, 1], [1, 2, 3], [1, 2, l]]), sp.Matrix([6, 10, m])
    ok(nsol(*sys30(3, 10), X3) == "inf1", "q30 A")
    ok(nsol(*sys30(3, 11), X3) == "none", "q30 B")
    ok(list(sp.linsolve(sys30(4, 13), *X3))[0][2] == 3, "q30 C")
    ok(list(sp.linsolve(sys30(5, 12), *X3))[0][2] == 1, "q30 D")

    # notes examples
    A = sp.Matrix([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    ok(sp.linsolve((A, sp.Matrix([9, 1, 0])), *X3) == sp.FiniteSet((1, 2, 3)), "notes GJ")
    A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
    ok(A.det() == 7 and A.adjugate() == sp.Matrix([[-1, 3, 2], [3, -2, 1], [5, -1, -3]]), "notes adj")
    ok(A.adjugate() * sp.Matrix([3, 2, 2]) == sp.Matrix([7, 7, 7]), "notes adjB")
    M = sp.Matrix([[1, -k, 1], [k, 3, -k], [3, 1, -1]])
    eq(sp.factor(M.det()), 2 * (k - 2) * (k + 3), "notes homog")
    N = sp.Matrix([[1, 2, -1], [2, 1, 1]]).nullspace()
    ok(len(N) == 1 and N[0].cross(sp.Matrix([-1, 1, 1])) == sp.zeros(3, 1), "notes homog ex")


T.write(check)
