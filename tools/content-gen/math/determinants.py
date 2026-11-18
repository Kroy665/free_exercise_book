import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.linalg.determinants")

V = lambda rows: r"\begin{vmatrix} " + r" \\ ".join(" & ".join(r) for r in rows) + r" \end{vmatrix}"

# q1
T.single(1, ["definition"],
    r"The value of $" + V([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "10"]]) + r"$ is",
    [r"$-3$", r"$3$", r"$0$", r"$-9$"],
    r"""Expand along the first row:
$$1(50 - 48) - 2(40 - 42) + 3(32 - 35) = 2 + 4 - 9 = -3.$$

The tempting $0$ comes from the familiar array with last entry $9$, whose rows are in arithmetic progression; changing $9$ to $10$ breaks that. The answer $3$ comes from a sign slip on the middle term, $-2(40-42) = +4$.""")

# q2
T.single(1, ["definition", "exam-tips"],
    r"The number of terms in the full expansion of a determinant of order $4$ is",
    [r"$24$", r"$16$", r"$12$", r"$4$"],
    r"""Each term picks one element from each row and each column, that is, one permutation $\sigma \in S_4$. So there are $4! = 24$ terms, $12$ with sign $+$ and $12$ with sign $-$.

$16 = 4^2$ counts the entries, not the terms, and $12$ counts only the terms of one sign.""")

# q3
T.single(1, ["minors-cofactors"],
    r"In $" + V([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) + r"$, the cofactor of the element $6$ (row 2, column 3) is",
    [r"$6$", r"$-6$", r"$3$", r"$-3$"],
    r"""Delete row 2 and column 3. The minor is
$$M_{23} = \begin{vmatrix} 1 & 2 \\ 7 & 8 \end{vmatrix} = 8 - 14 = -6.$$
The cofactor is $C_{23} = (-1)^{2+3}M_{23} = -(-6) = 6$.

$-6$ is the minor, not the cofactor: the sign $(-1)^{i+j}$ is $-$ here because $i + j = 5$ is odd.""")

# q4
T.statements(1, ["properties"],
    r"Let $A$ and $B$ be real square matrices of order $n \ge 2$. Consider the following statements:",
    [r"$\det A^{T} = \det A$",
     r"$\det(A + B) = \det A + \det B$",
     r"If every element of one row of $A$ is multiplied by $k$, the determinant is multiplied by $k$."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""Statements 1 and 3 are basic properties: transposing does not change a determinant, and a determinant is linear in each row.

Statement 2 is false. With $A = B = I_2$:
$$\det(A + B) = \det(2I_2) = 4, \qquad \det A + \det B = 2.$$
A determinant is linear in **each row separately**, not in the whole matrix.""")

# q5
T.single(2, ["definition"],
    r"In the expansion of the determinant $\lvert a_{ij}\rvert$ of order $4$, the term $a_{12}a_{21}a_{34}a_{43}$ occurs with",
    [r"sign $+$", r"sign $-$", r"sign $+$ or $-$ depending on the entries", r"no sign: it is not a term of the expansion"],
    r"""The row indices are $1, 2, 3, 4$ and the column indices are $\sigma = (2, 1, 4, 3)$. Each row and each column appears once, so this is a genuine term.

$\sigma = (1\,2)(3\,4)$ is a product of **two** transpositions, so it is even, and the sign is $\operatorname{sgn}\sigma = +1$.

A common slip is to see "swaps" and choose $-$; count them: an even number of transpositions gives $+$.""")

# q6
T.single(1, ["standard-determinants"],
    r"The value of $" + V([["1", "1", "1"], ["2", "3", "5"], ["4", "9", "25"]]) + r"$ is",
    [r"$6$", r"$-6$", r"$30$", r"$0$"],
    r"""This is the Vandermonde determinant with $a, b, c = 2, 3, 5$:
$$(a - b)(b - c)(c - a) = (2 - 3)(3 - 5)(5 - 2) = (-1)(-2)(3) = 6.$$

$-6$ is what you get with the factors in the wrong cyclic order, for example $(b-a)(c-b)(c-a)$ with one sign flipped. Check by direct expansion: $1(75 - 45) - 1(50 - 20) + 1(18 - 12) = 30 - 30 + 6 = 6$.""")

# q7
T.single(1, ["standard-determinants"],
    r"The value of the circulant $" + V([["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]) + r"$ is",
    [r"$-(a^3 + b^3 + c^3 - 3abc)$", r"$a^3 + b^3 + c^3 - 3abc$", r"$(a + b + c)(a^2 + b^2 + c^2)$", r"$3abc - (a + b + c)^3$"],
    r"""$C_1 \to C_1 + C_2 + C_3$ makes the first column $(a+b+c)(1, 1, 1)^T$. Taking this factor out and expanding,
$$\Delta = -(a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) = -(a^3 + b^3 + c^3 - 3abc).$$

**Check:** with $a = 1$, $b = c = 0$, the rows are $(1,0,0), (0,0,1), (0,1,0)$, and the value is $-1$. The formula without the minus sign gives $+1$, so it is wrong.""")

# q8
T.single(1, ["product-adjoint"],
    r"If $A$ is a $3 \times 3$ matrix with $\det A = 4$, then $\det(\operatorname{adj} A)$ equals",
    [r"$16$", r"$4$", r"$64$", r"$12$"],
    r"""From $A\,\operatorname{adj} A = (\det A) I_n$ we get $\det(\operatorname{adj} A) = (\det A)^{n-1}$. Here $n = 3$:
$$\det(\operatorname{adj} A) = 4^{2} = 16.$$

$64 = 4^3$ uses the exponent $n$ instead of $n - 1$.""")

# q9
T.assertion_reason(1, ["properties", "standard-determinants"],
    r"$(a - b)$ is a factor of $" + V([["1", "a", "a^2"], ["1", "b", "b^2"], ["1", "c", "c^2"]]) + r"$.",
    r"If a determinant whose entries are polynomials in $a$ vanishes identically when $a$ is replaced by $b$, then $(a - b)$ is a factor of it.",
    0,
    r"""Both are true, and R explains A.

Putting $a = b$ makes rows 1 and 2 identical, so the determinant becomes $0$. By the factor theorem (R), $(a - b)$ divides it. In fact the value is $(a - b)(b - c)(c - a)$.""")

# q10
T.single(2, ["cramers-rule"],
    r"For the system $x + y + z = 6$, $x - y + z = 2$, $2x + y - z = 1$, Cramer's rule gives",
    [r"$D = 6$ and $y = 2$", r"$D = -6$ and $y = 2$", r"$D = 6$ and $y = 3$", r"$D = 6$ and $y = 12$"],
    r"""$$D = \begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 2 & 1 & -1 \end{vmatrix} = 1(1 - 1) - 1(-1 - 2) + 1(1 + 2) = 6.$$
Replace the $y$-column by $(6, 2, 1)$:
$$D_y = \begin{vmatrix} 1 & 6 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & -1 \end{vmatrix} = 12, \qquad y = \frac{D_y}{D} = 2.$$

$y = 12$ forgets to divide by $D$. **Check:** $(x, y, z) = (1, 2, 3)$ satisfies all three equations.""")

# q11
T.single(2, ["cramers-rule"],
    r"The system $kx + y + z = 0$, $x + ky + z = 0$, $x + y + kz = 0$ has a non-trivial solution if and only if",
    [r"$k = 1$ or $k = -2$", r"$k = -1$ or $k = 2$", r"$k = 1$ only", r"$k \ne 1$ and $k \ne -2$"],
    r"""A homogeneous system has a non-trivial solution iff $D = 0$. Adding all columns to $C_1$ gives a factor $(k + 2)$:
$$D = \begin{vmatrix} k & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{vmatrix} = (k + 2)(k - 1)^2.$$
So $D = 0 \iff k = 1$ or $k = -2$.

"$k = 1$ only" misses the factor $(k + 2)$. The last option describes when the **only** solution is the trivial one.""")

# q12
T.single(2, ["standard-determinants", "properties"],
    r"$" + V([["1", "1", "1"], ["a", "b", "c"], ["a^3", "b^3", "c^3"]]) + r"$ equals",
    [r"$(a - b)(b - c)(c - a)(a + b + c)$", r"$(a - b)(b - c)(c - a)(ab + bc + ca)$", r"$(a - b)(b - c)(c - a)(a^2 + b^2 + c^2)$", r"$-(a - b)(b - c)(c - a)(a + b + c)$"],
    r"""The determinant vanishes when $a = b$, $b = c$ or $c = a$, so $(a - b)(b - c)(c - a)$ is a factor. The determinant has degree $1 + 3 = 4$, so the other factor is linear and symmetric: $k(a + b + c)$.

Compare the diagonal term $bc^3$: the product $(a-b)(b-c)(c-a)(a+b+c)$ contains $bc^3$ with coefficient $+1$, so $k = 1$.

**Check:** $a, b, c = 0, 1, 2$ gives $\begin{vmatrix} 1&1&1\\0&1&2\\0&1&8\end{vmatrix} = 6$, and the formula gives $(-1)(-1)(2)(3) = 6$. The option with $ab + bc + ca$ has the wrong degree (5).""")

# q13
T.single(2, ["standard-determinants"],
    r"$" + V([["1+a", "1", "1"], ["1", "1+b", "1"], ["1", "1", "1+c"]]) + r"$ equals",
    [r"$abc + ab + bc + ca$", r"$abc + a + b + c$", r"$abc$", r"$1 + a + b + c$"],
    r"""Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
$$\begin{vmatrix} 1 + a & 1 & 1 \\ -a & b & 0 \\ -a & 0 & c \end{vmatrix} = (1 + a)bc - 1(-ac) + 1(ab) = abc + bc + ca + ab.$$

**Check:** $a, b, c = 1, 2, 3$ gives $\begin{vmatrix} 2&1&1\\1&3&1\\1&1&4\end{vmatrix} = 22 - 3 - 2 = 17$, and $abc + ab + bc + ca = 6 + 2 + 6 + 3 = 17$. The option $abc + a + b + c$ gives $12$.""")

# q14
T.single(2, ["product-adjoint", "properties"],
    r"$A$ and $B$ are $3 \times 3$ matrices with $\det A = 2$ and $\det B = -3$. Then $\det(2AB^{T})$ equals",
    [r"$-48$", r"$-12$", r"$48$", r"$-6$"],
    r"""Use $\det(kM) = k^{n}\det M$, $\det(AB^T) = \det A\det B^T$ and $\det B^T = \det B$:
$$\det(2AB^T) = 2^{3}\cdot 2\cdot(-3) = -48.$$

$-12$ uses $\det(2M) = 2\det M$, which is the classic slip. The transpose changes nothing, so the sign stays negative.""")

# q15
T.assertion_reason(2, ["symmetric-skew"],
    r"Every skew-symmetric determinant of order $3$ with real entries has the value $0$.",
    r"Every diagonal element of a real skew-symmetric matrix is $0$.",
    1,
    r"""Both are true, but R does not explain A.

A: if $A^T = -A$ and $n = 3$, then $\det A = \det A^T = \det(-A) = (-1)^3\det A$, so $\det A = 0$.

R: $a_{ii} = -a_{ii}$ gives $a_{ii} = 0$.

The proof of A uses only $\det A^T = \det A$ and the odd order. A zero diagonal by itself does not force a zero determinant: $\begin{vmatrix} 0&1\\1&0\end{vmatrix} = -1$.""")

# q16
T.single(3, ["standard-determinants", "properties"],
    r"$" + V([["b+c", "a", "a"], ["b", "c+a", "b"], ["c", "c", "a+b"]]) + r"$ equals",
    [r"$4abc$", r"$2abc$", r"$abc$", r"$(a + b + c)^3$"],
    r"""Put $a = 0$: the first row becomes $(b + c, 0, 0)$, and
$$\Delta = (b + c)\begin{vmatrix} c & b \\ c & b \end{vmatrix} = 0.$$
So $a$ is a factor, and by symmetry so are $b$ and $c$. The degree is 3, so $\Delta = k\,abc$.

$a = b = c = 1$ gives $\begin{vmatrix} 2&1&1\\1&2&1\\1&1&2\end{vmatrix} = 4$, so $k = 4$ and $\Delta = 4abc$.

$(a + b + c)^3$ fails this check: it gives $27$.""")

# q17
T.single(2, ["standard-determinants"],
    r"$" + V([["1", "a", "bc"], ["1", "b", "ca"], ["1", "c", "ab"]]) + r"$ equals",
    [r"$(a - b)(b - c)(c - a)$", r"$-(a - b)(b - c)(c - a)$", r"$0$", r"$(a - b)(b - c)(c - a)(a + b + c)$"],
    r"""$R_2 \to R_2 - R_1$, $R_3 \to R_3 - R_1$:
$$\begin{vmatrix} 1 & a & bc \\ 0 & b - a & c(a - b) \\ 0 & c - a & b(a - c) \end{vmatrix} = (a - b)(c - a)\begin{vmatrix} -1 & c \\ 1 & -b \end{vmatrix} = (a - b)(c - a)(b - c).$$

**Check:** $a, b, c = 0, 1, 2$: $\begin{vmatrix} 1&0&2\\1&1&0\\1&2&0\end{vmatrix} = 2(2 - 1) = 2$, and $(a-b)(b-c)(c-a) = (-1)(-1)(2) = 2$. The option with an extra $(a + b + c)$ has degree 4, but every term of the determinant has degree 3.""")

# q18
T.single(3, ["standard-determinants", "properties"],
    r"$" + V([["(b+c)^2", "a^2", "a^2"], ["b^2", "(c+a)^2", "b^2"], ["c^2", "c^2", "(a+b)^2"]]) + r"$ equals",
    [r"$2abc(a + b + c)^3$", r"$abc(a + b + c)^3$", r"$2abc(a + b + c)^2$", r"$2(a + b + c)^6$"],
    r"""Put $a + b + c = 0$. Then $(b + c)^2 = a^2$, $(c + a)^2 = b^2$, $(a + b)^2 = c^2$, so $C_1 = C_2 = C_3 = (a^2, b^2, c^2)^T$ and $\Delta = 0$. More precisely, $C_1 \to C_1 - C_3$ and $C_2 \to C_2 - C_3$ each take out a factor $(a + b + c)$, and the remaining determinant still vanishes at $a + b + c = 0$. So $(a + b + c)^3$ divides $\Delta$.

Put $a = 0$: row 1 becomes $((b + c)^2, 0, 0)$ and its minor $\begin{vmatrix} c^2 & b^2 \\ c^2 & b^2 \end{vmatrix} = 0$. So $a$, and by symmetry $b$ and $c$, are factors. The degree is 6, so $\Delta = k\,abc(a + b + c)^3$.

$a = b = c = 1$: $\begin{vmatrix} 4&1&1\\1&4&1\\1&1&4\end{vmatrix} = 54$, and $abc(a+b+c)^3 = 27$, so $k = 2$.

The option without the $2$ is the usual slip from not fixing the constant.""")

# q19
T.single(1, ["cramers-rule"],
    r"The system $x + 2y = 3$, $2x + 4y = k$ has infinitely many solutions when",
    [r"$k = 6$", r"$k = 3$", r"$k \ne 6$", r"no value of $k$"],
    r"""$D = \begin{vmatrix} 1 & 2 \\ 2 & 4 \end{vmatrix} = 0$, so there is no unique solution.
$$D_x = \begin{vmatrix} 3 & 2 \\ k & 4 \end{vmatrix} = 12 - 2k.$$
If $k \ne 6$, then $D_x \ne 0$ and the system is inconsistent. If $k = 6$, the second equation is twice the first, so every point of the line $x + 2y = 3$ is a solution.""")

# q20
T.single(3, ["cramers-rule"],
    r"The system $x + y + z = 6$, $x + 2y + 3z = 10$, $x + 2y + \lambda z = \mu$ has **no** solution when",
    [r"$\lambda = 3,\ \mu \ne 10$", r"$\lambda = 3,\ \mu = 10$", r"$\lambda \ne 3,\ \mu = 10$", r"$\lambda \ne 3,\ \mu \ne 10$"],
    r"""$$D = \begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 2 & \lambda \end{vmatrix} = \lambda - 3.$$
If $\lambda \ne 3$, then $D \ne 0$ and the solution is unique, whatever $\mu$ is.

If $\lambda = 3$, subtract the second equation from the third: $0 = \mu - 10$. So there is no solution when $\mu \ne 10$, and infinitely many when $\mu = 10$.

The option $\lambda = 3, \mu = 10$ is the infinitely-many case.""")

# q21
T.single(3, ["symmetric-skew"],
    r"The value of $" + V([["0", "1", "2", "3"], ["-1", "0", "4", "5"], ["-2", "-4", "0", "6"], ["-3", "-5", "-6", "0"]]) + r"$ is",
    [r"$64$", r"$0$", r"$-64$", r"$784$"],
    r"""This is skew-symmetric of **even** order, so it is a perfect square. With the entries $a, b, c, d, e, f = 1, 2, 3, 4, 5, 6$ above the diagonal,
$$\Delta = (af - be + cd)^2 = (6 - 10 + 12)^2 = 8^2 = 64.$$

$0$ is the trap: only **odd**-order skew-symmetric determinants vanish. $784 = 28^2$ uses $af + be + cd$, with the wrong sign on $be$. $-64$ is impossible, because the value is a square.""")

# q22
T.single(3, ["product-adjoint", "standard-determinants"],
    r"$" + V([["2bc-a^2", "c^2", "b^2"], ["c^2", "2ca-b^2", "a^2"], ["b^2", "a^2", "2ab-c^2"]]) + r"$ equals",
    [r"$(a^3 + b^3 + c^3 - 3abc)^2$", r"$-(a^3 + b^3 + c^3 - 3abc)^2$", r"$(a^2 + b^2 + c^2 - ab - bc - ca)^2$", r"$a^3 + b^3 + c^3 - 3abc$"],
    r"""Let $\Delta$ be the circulant with rows $(a, b, c), (b, c, a), (c, a, b)$, so $\Delta = -(a^3 + b^3 + c^3 - 3abc)$. Swapping $C_2, C_3$ and then changing the sign of $C_1$ gives rows $(-a, c, b), (-b, a, c), (-c, b, a)$, also with value $\Delta$.

Multiply the two row by row. Entry $(1,1)$ is $-a^2 + bc + cb = 2bc - a^2$, entry $(1,2)$ is $-ab + ab + c^2 = c^2$, and so on. This gives exactly the given array, so its value is
$$\Delta \cdot \Delta = (a^3 + b^3 + c^3 - 3abc)^2.$$

**Check:** put $a = b = 1$, $c = 0$. The array is $\begin{vmatrix} -1&0&1\\0&-1&1\\1&1&2\end{vmatrix} = 4$. The key gives $2^2 = 4$; the other options give $-4$, $1$ and $2$.""")

# q23
T.single(2, ["minors-cofactors"],
    r"For $\Delta = " + V([["1", "2", "3"], ["0", "1", "4"], ["5", "6", "0"]]) + r"$ with cofactors $C_{ij}$, the value of $a_{11}C_{21} + a_{12}C_{22} + a_{13}C_{23}$ is",
    [r"$0$", r"$1$", r"$-1$", r"$5$"],
    r"""This multiplies the elements of row 1 by the cofactors of row 2: **alien cofactors**. The sum is the expansion of a determinant whose second row has been replaced by a copy of the first row. That determinant has two equal rows, so the sum is $0$.

$1$ is $\Delta$ itself, which you get only with the cofactors of the **same** row: $a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13} = -24 + 40 - 15 = 1$.""")

# q24
T.statements(3, ["symmetric-skew"],
    r"Consider the following statements about real determinants:",
    [r"Every skew-symmetric determinant of odd order is $0$.",
     r"Every skew-symmetric determinant of even order is the square of a polynomial in its entries.",
     r"Every symmetric determinant of order $3$ whose diagonal entries are all $0$ is $0$."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"1 and 3 only"],
    r"""1 is true: $\det A = \det A^T = (-1)^n\det A$ forces $\det A = 0$ for odd $n$.

2 is true: the value is the square of the Pfaffian. For order 2 it is $a^2$; for order 4 it is $(af - be + cd)^2$.

3 is false:
$$\begin{vmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{vmatrix} = 2 \ne 0.$$
The vanishing result needs **skew**-symmetry, not just a zero diagonal.""")

# q25
T.statements(2, ["cramers-rule"],
    r"For a system of three linear equations in $x, y, z$ with coefficient determinant $D$ and Cramer determinants $D_x, D_y, D_z$, consider the following statements:",
    [r"If $D \ne 0$, the system has a unique solution.",
     r"If $D = 0$ and at least one of $D_x, D_y, D_z$ is non-zero, the system has no solution.",
     r"If $D = 0$ and $D_x = D_y = D_z = 0$, the system has infinitely many solutions."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1 is true: $x = D_x/D$ and so on is the unique solution.

2 is true: from $A\,\operatorname{adj}A = DI$, any solution would satisfy $D\,x = D_x$, that is, $0 = D_x \ne 0$.

3 is false. The system $x + y + z = 1$, $x + y + z = 2$, $x + y + z = 3$ has $D = D_x = D_y = D_z = 0$ (each determinant has two equal columns), but it is inconsistent. When everything vanishes, Cramer's rule decides nothing.""")

# q26
T.match(2, ["standard-determinants", "symmetric-skew"],
    r"Match each determinant in List I (rows listed) with its value in List II.",
    [r"$(a, b, c),\ (b, c, a),\ (c, a, b)$",
     r"$(1, 1, 1),\ (a, b, c),\ (a^2, b^2, c^2)$",
     r"$(1+a, 1, 1),\ (1, 1+b, 1),\ (1, 1, 1+c)$",
     r"$(0, a, b),\ (-a, 0, c),\ (-b, -c, 0)$"],
    [r"$abc + ab + bc + ca$",
     r"$0$",
     r"$-(a^3 + b^3 + c^3 - 3abc)$",
     r"$(a - b)(b - c)(c - a)$"],
    [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-2, D-1", r"A-2, B-4, C-1, D-3"],
    r"""- A: the circulant, $-(a^3 + b^3 + c^3 - 3abc)$ (3).
- B: Vandermonde, $(a - b)(b - c)(c - a)$ (4).
- C: $abc + ab + bc + ca$ (1).
- D: skew-symmetric of odd order, so $0$ (2).

So A-3, B-4, C-1, D-2.""")

# q27
T.match(3, ["product-adjoint", "properties"],
    r"$A$ is a $3 \times 3$ matrix with $\det A = 2$. Match each expression in List I with its value in List II.",
    [r"$\det(3A)$", r"$\det(\operatorname{adj} A)$", r"$\det(-A)$", r"$\det(\operatorname{adj}(\operatorname{adj} A))$"],
    [r"$-2$", r"$16$", r"$54$", r"$4$"],
    [r"A-3, B-4, C-1, D-2", r"A-3, B-2, C-1, D-4", r"A-2, B-4, C-1, D-3", r"A-3, B-4, C-2, D-1"],
    r"""With $n = 3$:
- A: $\det(3A) = 3^3 \cdot 2 = 54$ (3).
- B: $\det(\operatorname{adj} A) = 2^{2} = 4$ (4).
- C: $\det(-A) = (-1)^3 \cdot 2 = -2$ (1).
- D: $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2}A = 2A$, so $\det = 2^3 \cdot 2 = 16 = 2^{(n-1)^2}$ (2).

So A-3, B-4, C-1, D-2. Swapping B and D confuses $(\det A)^{n-1}$ with $(\det A)^{(n-1)^2}$.""")

# q28
T.assertion_reason(3, ["product-adjoint"],
    r"If $A$ is a $3 \times 3$ matrix with $\det A = 0$, then $\det(\operatorname{adj} A) = 0$.",
    r"If $\det A = 0$, then $\operatorname{adj} A$ is the zero matrix.",
    2,
    r"""A is true: $\det(\operatorname{adj} A) = (\det A)^{2} = 0$.

R is false. For $A = \operatorname{diag}(1, 1, 0)$, $\det A = 0$ but
$$\operatorname{adj} A = \operatorname{diag}(0, 0, 1) \ne O.$$
$\operatorname{adj} A = O$ needs every $2 \times 2$ minor to vanish, which is much stronger than $\det A = 0$.""")

# q29
T.assertion_reason(2, ["symmetric-skew"],
    r"Every real symmetric determinant of order $2$ is a perfect square.",
    r"Every real skew-symmetric determinant of even order is a perfect square.",
    3,
    r"""A is false: $\begin{vmatrix} a & h \\ h & b \end{vmatrix} = ab - h^2$, which is $-1$ for $a = b = 0$, $h = 1$. A negative real number is not a square.

R is true: $\begin{vmatrix} 0 & a \\ -a & 0 \end{vmatrix} = a^2$, and in general an even-order skew-symmetric determinant is the square of its Pfaffian.""")

# q30
T.assertion_reason(2, ["product-adjoint"],
    r"For any two square matrices $A$ and $B$ of the same order, $\det(AB) = \det(BA)$.",
    r"$\det(AB) = \det A \cdot \det B$, and multiplication of real numbers is commutative.",
    0,
    r"""Both are true, and R explains A:
$$\det(AB) = \det A\det B = \det B\det A = \det(BA).$$
This holds even when $AB \ne BA$. For example, $A = \begin{pmatrix} 1&1\\0&1\end{pmatrix}$, $B = \begin{pmatrix} 1&0\\1&1\end{pmatrix}$ do not commute, but both products have determinant $1$.""")


def check():
    import sympy as sp
    M = sp.Matrix
    a, b, c, d, e, f, k, x, h, lam, mu = sp.symbols("a b c d e f k x h lambda mu")
    yv, zv = sp.symbols("y z")
    I = sp.Rational
    # q1
    eq(M([[1, 2, 3], [4, 5, 6], [7, 8, 10]]).det(), -3, "q1")
    # q2
    eq(sp.factorial(4), 24, "q2")
    # q3: cofactor C23
    A3 = M([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    eq(A3.cofactor(1, 2), 6, "q3")
    eq(A3.minor(1, 2), -6, "q3 minor distractor")
    # q4: statements 1,3 true; 2 false
    G = M(3, 3, sp.symbols("g0:9"))
    eq(G.T.det() - G.det(), 0, "q4 s1")
    eq((2 * sp.eye(2)).det(), 4, "q4 s2 lhs"); eq(sp.eye(2).det() * 2, 2, "q4 s2 rhs")
    G2 = G.copy(); G2[0, :] = k * G[0, :]
    eq(G2.det() - k * G.det(), 0, "q4 s3")
    # q5: sign of permutation (2,1,4,3)
    from sympy.combinatorics import Permutation
    eq(Permutation([1, 0, 3, 2]).signature(), 1, "q5")
    # q6
    eq(M([[1, 1, 1], [2, 3, 5], [4, 9, 25]]).det(), 6, "q6")
    # q7
    Circ = M([[a, b, c], [b, c, a], [c, a, b]])
    eq(Circ.det(), -(a**3 + b**3 + c**3 - 3 * a * b * c), "q7")
    # q8: det adj = det^(n-1), random 3x3 scaled to det 4
    R = M([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
    eq(R.det(), 4, "q8 setup"); eq(R.adjugate().det(), 16, "q8")
    R2 = M([[1, 2, 0], [3, 1, 1], [0, 2, 5]])
    eq(R2.adjugate().det(), R2.det()**2, "q8 general")
    # q9: factor (a-b)
    Vd = M([[1, a, a**2], [1, b, b**2], [1, c, c**2]])
    eq(Vd.det().subs(a, b), 0, "q9"); eq(Vd.det(), (a - b) * (b - c) * (c - a), "q9 value")
    # q10
    D = M([[1, 1, 1], [1, -1, 1], [2, 1, -1]]); rhs = M([6, 2, 1])
    Dy = D.copy(); Dy[:, 1] = rhs
    eq(D.det(), 6, "q10 D"); eq(Dy.det() / D.det(), 2, "q10 y")
    eq(D.solve(rhs)[1], 2, "q10 solve")
    # q11
    Dk = M([[k, 1, 1], [1, k, 1], [1, 1, k]]).det()
    eq(Dk, (k + 2) * (k - 1)**2, "q11")
    assert set(sp.solve(Dk, k)) == {1, -2}, "q11 roots"
    # q12
    eq(M([[1, 1, 1], [a, b, c], [a**3, b**3, c**3]]).det(), (a - b) * (b - c) * (c - a) * (a + b + c), "q12")
    # q13
    eq(M([[1 + a, 1, 1], [1, 1 + b, 1], [1, 1, 1 + c]]).det(), a * b * c + a * b + b * c + c * a, "q13")
    # q14
    Am = M([[2, 0, 0], [0, 1, 0], [0, 0, 1]]); Bm = M([[-3, 1, 0], [0, 1, 2], [0, 0, 1]])
    eq(Am.det(), 2, "q14 A"); eq(Bm.det(), -3, "q14 B")
    eq((2 * Am * Bm.T).det(), -48, "q14")
    # q15: skew 3x3 zero; R true; R alone not sufficient
    Sk = M([[0, a, b], [-a, 0, c], [-b, -c, 0]])
    eq(Sk.det(), 0, "q15 A"); eq(M([[0, 1], [1, 0]]).det(), -1, "q15 zero-diagonal counterexample")
    # q16
    eq(M([[b + c, a, a], [b, c + a, b], [c, c, a + b]]).det(), 4 * a * b * c, "q16")
    # q17
    eq(M([[1, a, b * c], [1, b, c * a], [1, c, a * b]]).det(), (a - b) * (b - c) * (c - a), "q17")
    # q18
    eq(M([[(b + c)**2, a**2, a**2], [b**2, (c + a)**2, b**2], [c**2, c**2, (a + b)**2]]).det(),
       2 * a * b * c * (a + b + c)**3, "q18")
    eq(M([[4, 1, 1], [1, 4, 1], [1, 1, 4]]).det(), 54, "q18 check")
    # q19
    eq(M([[1, 2], [2, 4]]).det(), 0, "q19 D")
    eq(M([[3, 2], [k, 4]]).det(), 12 - 2 * k, "q19 Dx")
    xs, ys = sp.symbols("xs ys")
    assert sp.linsolve([xs + 2 * ys - 3, 2 * xs + 4 * ys - 6], xs, ys) != sp.EmptySet, "q19 k=6 consistent"
    assert sp.linsolve([xs + 2 * ys - 3, 2 * xs + 4 * ys - 5], xs, ys) == sp.EmptySet, "q19 k!=6"
    # q20
    eq(M([[1, 1, 1], [1, 2, 3], [1, 2, lam]]).det(), lam - 3, "q20 D")
    assert sp.linsolve([x + yv + zv - 6, x + 2 * yv + 3 * zv - 10, x + 2 * yv + 3 * zv - 11], x, yv, zv) == sp.EmptySet, "q20 none"
    sol = sp.linsolve([x + yv + zv - 6, x + 2 * yv + 3 * zv - 10, x + 2 * yv + 3 * zv - 10], x, yv, zv)
    assert list(sol)[0].free_symbols, "q20 lambda=3, mu=10 infinite"
    # q21
    Sk4 = M([[0, 1, 2, 3], [-1, 0, 4, 5], [-2, -4, 0, 6], [-3, -5, -6, 0]])
    eq(Sk4.det(), 64, "q21")
    Sk4s = M([[0, a, b, c], [-a, 0, d, e], [-b, -d, 0, f], [-c, -e, -f, 0]])
    eq(Sk4s.det(), (a * f - b * e + c * d)**2, "q21 Pfaffian")
    # q22
    eq(M([[-1, 0, 1], [0, -1, 1], [1, 1, 2]]).det(), 4, "q22 check")
    P = M([[2 * b * c - a**2, c**2, b**2], [c**2, 2 * c * a - b**2, a**2], [b**2, a**2, 2 * a * b - c**2]])
    eq(P.det(), (a**3 + b**3 + c**3 - 3 * a * b * c)**2, "q22")
    Q = M([[-a, c, b], [-b, a, c], [-c, b, a]])
    eq(Q.det() - Circ.det(), 0, "q22 second factor")
    assert sp.expand(Circ * Q.T - P) == sp.zeros(3, 3), "q22 product"
    # q23
    A23 = M([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    eq(sum(A23[0, j] * A23.cofactor(1, j) for j in range(3)), 0, "q23")
    eq(A23.det(), 1, "q23 det")
    # q24
    eq(M([[0, 1, 1], [1, 0, 1], [1, 1, 0]]).det(), 2, "q24 s3 counterexample")
    Sk5 = M(5, 5, lambda i, j: 0)
    syms = iter(sp.symbols("s0:10"))
    for i in range(5):
        for j in range(i + 1, 5):
            s = next(syms); Sk5[i, j] = s; Sk5[j, i] = -s
    eq(Sk5.det(), 0, "q24 s1 order 5")
    # q25: counterexample to statement 3
    C3 = M([[1, 1, 1], [1, 1, 1], [1, 1, 1]]); r3 = M([1, 2, 3])
    eq(C3.det(), 0, "q25 D")
    for i in range(3):
        Ci = C3.copy(); Ci[:, i] = r3; eq(Ci.det(), 0, f"q25 D{i}")
    assert sp.linsolve([x + yv + zv - 1, x + yv + zv - 2, x + yv + zv - 3], x, yv, zv) == sp.EmptySet, "q25 inconsistent"
    # q26
    eq(Circ.det(), -(a**3 + b**3 + c**3 - 3 * a * b * c), "q26 A")
    eq(M([[1, 1, 1], [a, b, c], [a**2, b**2, c**2]]).det(), (a - b) * (b - c) * (c - a), "q26 B")
    eq(M([[1 + a, 1, 1], [1, 1 + b, 1], [1, 1, 1 + c]]).det(), a * b * c + a * b + b * c + c * a, "q26 C")
    eq(M([[0, a, b], [-a, 0, c], [-b, -c, 0]]).det(), 0, "q26 D")
    # q27: concrete A with det 2
    A27 = M([[2, 1, 0], [0, 1, 3], [0, 0, 1]])
    eq(A27.det(), 2, "q27 setup")
    eq((3 * A27).det(), 54, "q27 A"); eq(A27.adjugate().det(), 4, "q27 B")
    eq((-A27).det(), -2, "q27 C"); eq(A27.adjugate().adjugate().det(), 16, "q27 D")
    # q28
    A28 = sp.diag(1, 1, 0)
    eq(A28.det(), 0, "q28"); eq(A28.adjugate().det(), 0, "q28 A")
    assert A28.adjugate() == sp.diag(0, 0, 1), "q28 R false"
    # q29
    eq(M([[0, 1], [1, 0]]).det(), -1, "q29 A false"); eq(M([[0, a], [-a, 0]]).det(), a**2, "q29 R")
    # q30
    A30 = M([[1, 1], [0, 1]]); B30 = M([[1, 0], [1, 1]])
    assert A30 * B30 != B30 * A30, "q30 noncommuting"
    eq((A30 * B30).det() - (B30 * A30).det(), 0, "q30")
    G3 = M(3, 3, sp.symbols("u0:9"))
    eq((G * G3).det() - (G3 * G).det(), 0, "q30 general")


T.write(check)
