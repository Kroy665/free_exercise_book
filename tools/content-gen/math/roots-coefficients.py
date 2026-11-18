import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.roots-coefficients")

# ---------- Vieta ----------
# q1
T.single(1, ["vieta"],
    r"If $\alpha, \beta, \gamma, \delta$ are the roots of $2x^4 - 3x^3 + 5x^2 - 7x + 4 = 0$, then $\sum\alpha\beta\gamma$ equals",
    [r"$\dfrac72$", r"$-\dfrac72$", r"$\dfrac52$", r"$2$"],
    r"""For $ax^4 + bx^3 + cx^2 + dx + e = 0$, the sum of the products three at a time is $-\dfrac{d}{a}$:
$$\sum\alpha\beta\gamma = -\frac{-7}{2} = \frac72.$$

$-\frac72$ forgets the alternating sign; $\frac52 = \frac ca$ is $\sum\alpha\beta$; $2 = \frac ea$ is the product of all four roots.""")

# q2
T.single(1, ["symmetric-functions", "exam-tips"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 - 2x^2 + 3x - 4 = 0$, then $\alpha^2 + \beta^2 + \gamma^2$ equals",
    [r"$-2$", r"$10$", r"$4$", r"$2$"],
    r"""Here $e_1 = \sum\alpha = 2$ and $e_2 = \sum\alpha\beta = 3$. So
$$\sum\alpha^2 = e_1^2 - 2e_2 = 4 - 6 = -2.$$

The value $10$ comes from $e_1^2 + 2e_2$, a sign slip. A negative sum of squares is no contradiction: it shows that the roots are not all real.""")

# q3
T.single(2, ["symmetric-functions"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 - 3x + 1 = 0$, then $\alpha^3 + \beta^3 + \gamma^3$ equals",
    [r"$-3$", r"$3$", r"$-1$", r"$9$"],
    r"""Each root satisfies $\alpha^3 = 3\alpha - 1$. Summing over the three roots:
$$\sum\alpha^3 = 3\sum\alpha - 3 = 3(0) - 3 = -3.$$

Equivalently, $e_1^3 - 3e_1e_2 + 3e_3$ with $e_1 = 0$, $e_3 = -1$ gives $-3$. The tempting $-1$ adds the constant once instead of once per root.""")

# q4
T.single(2, ["symmetric-functions"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 - 2x + 1 = 0$, then $\alpha^4 + \beta^4 + \gamma^4$ equals",
    [r"$8$", r"$-8$", r"$4$", r"$16$"],
    r"""Use Newton's identities for $x^3 + px + q$ with $p = -2$, $q = 1$:
$$s_1 = 0, \quad s_2 = -2p = 4, \quad s_4 = -p\,s_2 - q\,s_1 = 2 \cdot 4 - 0 = 8.$$

In general $s_4 = 2p^2 = 8$. The value $4$ is $s_2$, and $16 = s_2^2$ wrongly treats $\sum\alpha^4$ as $(\sum\alpha^2)^2$.

**Check:** $x^3 - 2x + 1 = (x - 1)(x^2 + x - 1)$. The quadratic's roots have $\sum\alpha^2 = 1 + 2 = 3$ and $\sum\alpha^4 = 3^2 - 2 = 7$. Adding $1^4$ gives $8$.""")

# q5
T.single(2, ["symmetric-functions"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 + 2x^2 - 3x - 1 = 0$, then $\sum\alpha^2\beta$ (the sum of all six terms $\alpha^2\beta, \alpha^2\gamma, \ldots$) equals",
    [r"$3$", r"$6$", r"$9$", r"$5$"],
    r"""Here $e_1 = -2$, $e_2 = -3$, $e_3 = 1$. Expanding $e_1e_2$ gives every $\alpha^2\beta$ term once, plus $3\alpha\beta\gamma$:
$$\sum\alpha^2\beta = e_1e_2 - 3e_3 = 6 - 3 = 3.$$

$6$ forgets to subtract $3e_3$; $5 = e_1e_2 - e_3$ subtracts it only once; $9$ adds it.""")

# q6
T.single(2, ["symmetric-functions"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 - 4x^2 + x + 6 = 0$, then $(\alpha + \beta)(\beta + \gamma)(\gamma + \alpha)$ equals",
    [r"$10$", r"$-2$", r"$4$", r"$-10$"],
    r"""Use $(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha) = e_1e_2 - e_3$, with $e_1 = 4$, $e_2 = 1$, $e_3 = -6$:
$$4 \cdot 1 - (-6) = 10.$$

$-2$ comes from $e_1e_2 + e_3$, a sign slip with the product.

**Check:** the roots are $-1, 2, 3$, so the value is $(1)(5)(2) = 10$.""")

# ---------- root relations ----------
# q7
T.single(2, ["root-relations"],
    r"The roots of $x^3 - 12x^2 + 39x - 28 = 0$ are in arithmetic progression. The roots are",
    [r"$1, 4, 7$", r"$2, 4, 6$", r"$-1, 4, 9$", r"$1, 3, 5$"],
    r"""Take the roots as $a - d, a, a + d$. The sum is $3a = 12$, so $a = 4$. The product is
$$(4 - d)\cdot 4\cdot(4 + d) = 28 \implies 16 - d^2 = 7 \implies d = \pm 3.$$

So the roots are $1, 4, 7$. **Check:** $\sum\alpha\beta = 4 + 7 + 28 = 39$.

$2, 4, 6$ has the right sum but product $48$, not $28$.""")

# q8
T.single(2, ["root-relations"],
    r"The roots of $x^3 - 14x^2 + 56x - 64 = 0$ are in geometric progression. The roots are",
    [r"$2, 4, 8$", r"$1, 4, 16$", r"$1, 2, 4$", r"$4, 4, 4$"],
    r"""Take the roots as $\frac ar, a, ar$. The product is $a^3 = 64$, so $a = 4$. Then
$$4\left(\frac1r + 1 + r\right) = 14 \implies r + \frac1r = \frac52 \implies r = 2 \text{ or } \frac12.$$

Both give the roots $2, 4, 8$.

$1, 4, 16$ also has product $64$, but its sum is $21$, not $14$. A quick check is that the middle root is $-c/b = -56/(-14) = 4$.""")

# q9
T.single(3, ["root-relations"],
    r"The roots of $ax^3 + bx^2 + cx + d = 0$ ($a \ne 0$) are in arithmetic progression if and only if",
    [r"$2b^3 - 9abc + 27a^2d = 0$", r"$2b^3 - 9abc - 27a^2d = 0$", r"$ac^3 = b^3d$", r"$b^3 - 3abc + 27a^2d = 0$"],
    r"""In an AP the middle root is the mean of the roots, $-\frac{b}{3a}$. The roots are in AP exactly when this number is a root:
$$a\left(-\frac{b}{3a}\right)^3 + b\left(\frac{b^2}{9a^2}\right) - \frac{bc}{3a} + d = 0.$$

Multiplying by $27a^2$ gives $-b^3 + 3b^3 - 9abc + 27a^2d = 0$, that is, $2b^3 - 9abc + 27a^2d = 0$.

$ac^3 = b^3d$ is the condition for roots in **GP**.""")

# q10
T.single(3, ["root-relations"],
    r"The equation $x^4 - 2x^3 + 4x^2 + 6x - 21 = 0$ has two roots whose sum is zero. Its other two roots are",
    [r"$1 \pm i\sqrt6$", r"$-1 \pm i\sqrt6$", r"$1 \pm \sqrt6$", r"$1 \pm i\sqrt3$"],
    r"""Write the quartic as $(x^2 - k)(x^2 + ax + b)$ and compare coefficients:
- $x^3$: $a = -2$
- $x$: $-ak = 6$, so $k = 3$
- $x^2$: $b - k = 4$, so $b = 7$
- constant: $-bk = -21$, which checks.

The roots of $x^2 - 2x + 7 = 0$ are $1 \pm i\sqrt6$; the other two roots are $\pm\sqrt3$.

**Check:** all four roots must sum to $2$, and $\sqrt3 - \sqrt3 + 2 = 2$. The pair $-1 \pm i\sqrt6$ would make the sum $-2$.""")

# q11
T.single(1, ["root-relations"],
    r"The equation $x^3 + px^2 + qx + r = 0$ has two roots whose sum is zero. Then",
    [r"$r = pq$", r"$q = pr$", r"$p = qr$", r"$r = -pq$"],
    r"""If $\alpha + \beta = 0$, then $\gamma = (\alpha + \beta + \gamma) - (\alpha + \beta) = -p$. Also $\alpha\beta = \alpha\beta + \gamma(\alpha + \beta) = q$. So the cubic is
$$(x^2 + q)(x + p) = x^3 + px^2 + qx + pq,$$
and therefore $r = pq$.

**Check:** $x^3 - 2x^2 - 9x + 18 = 0$ has $pq = 18 = r$, and its roots are $2, \pm3$.""")

# ---------- basic transformations ----------
# q12
T.single(1, ["basic-transformations"],
    r"The equation whose roots are the reciprocals of the roots of $2x^3 - 3x^2 + 5x - 7 = 0$ is",
    [r"$7x^3 - 5x^2 + 3x - 2 = 0$", r"$7x^3 + 5x^2 + 3x + 2 = 0$", r"$2x^3 + 3x^2 + 5x + 7 = 0$", r"$7x^3 - 3x^2 + 5x - 2 = 0$"],
    r"""Replace $x$ by $\frac1x$ and multiply by $x^3$. This reverses the coefficients:
$$-7x^3 + 5x^2 - 3x + 2 = 0 \iff 7x^3 - 5x^2 + 3x - 2 = 0.$$

$2x^3 + 3x^2 + 5x + 7 = 0$ has the **negatives** of the roots (from $x \to -x$). $7x^3 - 3x^2 + 5x - 2$ swaps only the end coefficients.

**Check:** the new sum of roots should be $\sum\frac1\alpha = \frac{e_2}{e_3} = \frac{5/2}{7/2} = \frac57$, and $-\frac{-5}{7} = \frac57$.""")

# q13
T.single(1, ["basic-transformations"],
    r"The equation whose roots are three times the roots of $x^3 - x^2 + 2x - 1 = 0$ is",
    [r"$x^3 - 3x^2 + 18x - 27 = 0$", r"$x^3 - 3x^2 + 6x - 3 = 0$", r"$27x^3 - 9x^2 + 6x - 1 = 0$", r"$x^3 - 9x^2 + 18x - 27 = 0$"],
    r"""To multiply the roots by $k$, substitute $x \to \frac xk$ and multiply by $k^n$. This multiplies $a_r$ by $k^r$:
$$1,\ -1\cdot3,\ 2\cdot 9,\ -1\cdot 27 \;\to\; x^3 - 3x^2 + 18x - 27 = 0.$$

$27x^3 - 9x^2 + 6x - 1 = 0$ is $f(3x) = 0$, whose roots are the old roots **divided** by $3$.

**Check:** the new sum of roots is $3$, three times the old sum $1$.""")

# ---------- diminishing roots ----------
# q14
T.single(1, ["diminishing-roots"],
    r"To remove the second term (the $x^3$ term) of $x^4 - 8x^3 + x^2 - x + 3 = 0$, its roots should be diminished by",
    [r"$2$", r"$-2$", r"$8$", r"$4$"],
    r"""Diminish the roots by their mean:
$$h = -\frac{a_1}{n\,a_0} = -\frac{-8}{4 \cdot 1} = 2.$$

Then the new roots $\alpha_i - 2$ sum to $8 - 4\cdot2 = 0$, so the $y^3$ term vanishes. $8$ is the sum of the roots, not their mean; $-2$ is a sign slip.""")

# q15
T.single(2, ["diminishing-roots"],
    r"Diminishing each root of $x^3 - 6x^2 + 10x - 3 = 0$ by $2$ gives the equation",
    [r"$y^3 - 2y + 1 = 0$", r"$y^3 - 2y - 1 = 0$", r"$y^3 - 12y^2 + 46y - 55 = 0$", r"$y^3 + 2y + 1 = 0$"],
    r"""Divide by $x - 2$ repeatedly (synthetic division), recording the remainders:
- $1, -6, 10, -3 \to 1, -4, 2$, remainder $1$
- $1, -4, 2 \to 1, -2$, remainder $-2$
- $1, -2 \to 1$, remainder $0$

The remainders are the new coefficients from the constant term upwards:
$$y^3 + 0\,y^2 - 2y + 1 = 0.$$

$y^3 - 12y^2 + 46y - 55 = 0$ is $f(y - 2) = 0$, which **increases** the roots by $2$. **Check:** the new sum of roots is $6 - 3\cdot 2 = 0$.""")

# ---------- general transformation ----------
# q16
T.single(3, ["general-transformation"],
    r"The equation whose roots are the squares of the roots of $x^3 - 2x^2 + 3x - 1 = 0$ is",
    [r"$y^3 + 2y^2 + 5y - 1 = 0$", r"$y^3 - 2y^2 + 5y - 1 = 0$", r"$y^3 + 2y^2 + 5y + 1 = 0$", r"$y^3 + 2y^2 + 13y - 1 = 0$"],
    r"""Separate the odd and even powers: $x(x^2 + 3) = 2x^2 + 1$. Square both sides and put $y = x^2$:
$$y(y + 3)^2 = (2y + 1)^2 \implies y^3 + 6y^2 + 9y = 4y^2 + 4y + 1 \implies y^3 + 2y^2 + 5y - 1 = 0.$$

**Checks:**
- the new sum of roots is $-2 = \sum\alpha^2 = 2^2 - 2\cdot3$
- the new product is $1 = (\alpha\beta\gamma)^2$, so the constant term must be $-1$, not $+1$

$13$ comes from $q^2 + 2pr$ instead of $q^2 - 2pr$.""")

# q17
T.single(3, ["general-transformation"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 - x - 1 = 0$, then $\dfrac{1 + \alpha}{1 - \alpha} + \dfrac{1 + \beta}{1 - \beta} + \dfrac{1 + \gamma}{1 - \gamma}$ equals",
    [r"$-7$", r"$7$", r"$1$", r"$-1$"],
    r"""Put $y = \frac{1 + x}{1 - x}$, so $x = \frac{y - 1}{y + 1}$. Substitute and multiply by $(y + 1)^3$:
$$(y - 1)^3 - (y - 1)(y + 1)^2 - (y + 1)^3 = 0 \implies -y^3 - 7y^2 + y - 1 = 0.$$

So $y^3 + 7y^2 - y + 1 = 0$, and the required sum is $-7$.

$+7$ forgets the minus sign in "sum of roots $= -a_1/a_0$".""")

# q18
T.single(3, ["general-transformation"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 + px + q = 0$ ($q \ne 0$), the equation whose roots are $\beta\gamma, \gamma\alpha, \alpha\beta$ is",
    [r"$y^3 - py^2 - q^2 = 0$", r"$y^3 + py^2 - q^2 = 0$", r"$y^3 - py^2 + q^2 = 0$", r"$y^3 - py - q^2 = 0$"],
    r"""Since $\alpha\beta\gamma = -q$, we have $\beta\gamma = -\frac q\alpha$. So put $y = -\frac qx$, that is, $x = -\frac qy$:
$$-\frac{q^3}{y^3} - \frac{pq}{y} + q = 0 \implies y^3 - py^2 - q^2 = 0.$$

**Checks:**
- the new sum of roots is $\sum\alpha\beta = p$
- the new product is $(\alpha\beta\gamma)^2 = q^2$
- the middle coefficient is $\sum(\alpha\beta)(\beta\gamma) = \alpha\beta\gamma\sum\alpha = 0$

$y^3 + py^2 - q^2$ has the wrong sum of roots.""")

# ---------- reciprocal equations ----------
# q19
T.single(1, ["reciprocal-equations"],
    r"Which of the following is necessarily a root of $x^5 + 4x^4 + x^3 + x^2 + 4x + 1 = 0$?",
    [r"$-1$", r"$1$", r"$0$", r"$2$"],
    r"""The coefficients $1, 4, 1, 1, 4, 1$ read the same from either end. So this is a reciprocal equation of the first class, of odd degree, and $x = -1$ is a root:
$$-1 + 4 - 1 + 1 - 4 + 1 = 0.$$

$x = 1$ is forced only for the second class (coefficients equal and opposite). Here $f(1) = 12$.""")

# q20
T.single(2, ["reciprocal-equations"],
    r"With $z = x + \dfrac1x$, the equation $x^4 - 5x^3 + 8x^2 - 5x + 1 = 0$ reduces to",
    [r"$z^2 - 5z + 6 = 0$", r"$z^2 - 5z + 8 = 0$", r"$z^2 - 5z + 10 = 0$", r"$z^2 + 5z + 6 = 0$"],
    r"""Divide by $x^2$ and group:
$$\left(x^2 + \frac1{x^2}\right) - 5\left(x + \frac1x\right) + 8 = 0.$$

Since $x^2 + \frac1{x^2} = z^2 - 2$, this gives $z^2 - 2 - 5z + 8 = z^2 - 5z + 6 = 0$.

$z^2 - 5z + 10$ uses $z^2 + 2$ by mistake. **Result:** $z = 2, 3$, so $x = 1, 1, \frac{3 \pm \sqrt5}{2}$.""")

# q21
T.single(3, ["reciprocal-equations"],
    r"The sum of the real roots of $x^5 + 4x^4 + x^3 + x^2 + 4x + 1 = 0$ is",
    [r"$-5$", r"$-4$", r"$-1$", r"$-3$"],
    r"""This is first class, of odd degree, so $x + 1$ is a factor. The quotient is
$$x^4 + 3x^3 - 2x^2 + 3x + 1.$$

Dividing by $x^2$ and putting $z = x + \frac1x$ gives $z^2 + 3z - 4 = 0$, so $z = 1$ or $z = -4$.
- $z = 1$: $x^2 - x + 1 = 0$, non-real roots (since $|z| < 2$).
- $z = -4$: $x^2 + 4x + 1 = 0$, $x = -2 \pm\sqrt3$, both real.

The real roots are $-1, -2 \pm \sqrt3$, with sum $-5$.

$-4$ is the sum of **all five** roots, which includes the non-real pair (sum $1$).""")

# ---------- statements ----------
# q22
T.statements(2, ["symmetric-functions", "exam-tips"],
    r"Let $\alpha, \beta, \gamma$ be the roots of $x^3 + px + q = 0$, where $q \ne 0$. Consider the following statements:",
    [r"$\alpha^2 + \beta^2 + \gamma^2 = -2p$",
     r"$\alpha^3 + \beta^3 + \gamma^3 = 3q$",
     r"$\dfrac1\alpha + \dfrac1\beta + \dfrac1\gamma = -\dfrac pq$"],
    [r"1 and 3 only", r"1 and 2 only", r"1, 2 and 3", r"3 only"],
    r"""Here $e_1 = 0$, $e_2 = p$, $e_3 = -q$.
1. True: $\sum\alpha^2 = e_1^2 - 2e_2 = -2p$.
2. False: summing $\alpha^3 = -p\alpha - q$ over the roots gives $\sum\alpha^3 = -3q$, not $3q$.
3. True: $\sum\frac1\alpha = \frac{e_2}{e_3} = \frac{p}{-q}$.

**Check with $x^3 - 3x + 2 = (x - 1)^2(x + 2)$:** $\sum\alpha^3 = 1 + 1 - 8 = -6 = -3q$.""")

# q23
T.statements(2, ["basic-transformations", "diminishing-roots"],
    r"Let $f(x) = a_0x^n + a_1x^{n-1} + \cdots + a_n$ with $a_0a_n \ne 0$ and roots $\alpha_1, \ldots, \alpha_n$. Consider the following statements:",
    [r"The roots of $x^nf\!\left(\dfrac1x\right) = 0$ are $\dfrac1{\alpha_1}, \ldots, \dfrac1{\alpha_n}$.",
     r"The roots of $f(x + h) = 0$ are $\alpha_1 - h, \ldots, \alpha_n - h$.",
     r"Diminishing every root by $\dfrac{a_1}{na_0}$ removes the term in $x^{n-1}$."],
    [r"1 and 2 only", r"1 and 3 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. True: $x^nf(1/x) = a_nx^n + \cdots + a_0$, and it vanishes at $x = 1/\alpha_i$.
2. True: $f((\alpha_i - h) + h) = f(\alpha_i) = 0$.
3. False: the mean of the roots is $-\frac{a_1}{na_0}$, so the correct $h$ is $-\frac{a_1}{na_0}$. For $x^3 - 6x^2 + \cdots$, $h = 2$, while $\frac{a_1}{na_0} = -2$ gives new roots with sum $12$.""")

# q24
T.statements(3, ["reciprocal-equations"],
    r"Consider the following statements about reciprocal equations $a_0x^n + \cdots + a_n = 0$ ($a_0a_n \ne 0$):",
    [r"Every reciprocal equation of odd degree has $1$ or $-1$ as a root.",
     r"A reciprocal equation of the second class ($a_{n-r} = -a_r$) and of even degree has $x^2 - 1$ as a factor.",
     r"If $\alpha$ is a root of a reciprocal equation, then so is $\dfrac1\alpha$."],
    [r"1, 2 and 3", r"1 and 2 only", r"2 and 3 only", r"1 and 3 only"],
    r"""1. True. For the first class and odd $n$, the terms of $f(-1)$ cancel in pairs, so $-1$ is a root. For the second class and odd $n$, $f(1) = 0$.
2. True. The middle coefficient satisfies $a_m = -a_m$, so it is $0$, and the terms of both $f(1)$ and $f(-1)$ cancel in pairs.
3. True. This is the definition: $x^nf(1/x) = \pm f(x)$, and $\alpha \ne 0$ because $a_n \ne 0$.

Statement 1 does **not** extend to even degree: $x^2 + x + 1 = 0$ is reciprocal and has neither $1$ nor $-1$ as a root.""")

# ---------- match ----------
# q25
T.match(2, ["symmetric-functions"],
    r"$\alpha, \beta, \gamma$ are the roots of $x^3 - 6x^2 + 11x - 6 = 0$. Match each expression in List I with its value in List II.",
    [r"$\sum\alpha^2$", r"$\sum\dfrac1\alpha$", r"$\sum\alpha^2\beta$", r"$(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha)$"],
    [r"$60$", r"$14$", r"$\dfrac{11}{6}$", r"$48$"],
    [r"A-2, B-3, C-4, D-1", r"A-2, B-3, C-1, D-4", r"A-4, B-3, C-2, D-1", r"A-2, B-1, C-4, D-3"],
    r"""With $e_1 = 6$, $e_2 = 11$, $e_3 = 6$:
- A: $e_1^2 - 2e_2 = 36 - 22 = 14$
- B: $\frac{e_2}{e_3} = \frac{11}{6}$
- C: $e_1e_2 - 3e_3 = 66 - 18 = 48$
- D: $e_1e_2 - e_3 = 66 - 6 = 60$

So A-2, B-3, C-4, D-1. **Check:** the roots are $1, 2, 3$, and $(3)(5)(4) = 60$.""")

# q26
T.match(2, ["basic-transformations", "diminishing-roots"],
    r"Let $f(x) = x^3 + 2x^2 - x + 3$. Match each set of new roots (List I), formed from the roots of $f(x) = 0$, with its equation (List II).",
    [r"each root doubled", r"reciprocals of the roots", r"negatives of the roots", r"each root increased by $1$"],
    [r"$x^3 - x^2 - 2x + 5 = 0$", r"$x^3 - 2x^2 - x - 3 = 0$", r"$x^3 + 4x^2 - 4x + 24 = 0$", r"$3x^3 - x^2 + 2x + 1 = 0$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-4, C-1, D-2"],
    r"""- A (doubled): multiply $a_r$ by $2^r$: $1, 4, -4, 24$. That is 3.
- B (reciprocals): reverse the coefficients: $3x^3 - x^2 + 2x + 1$. That is 4.
- C (negatives): $-f(-x) = x^3 - 2x^2 - x - 3$. That is 2.
- D (increased by $1$): $f(x - 1) = x^3 - x^2 - 2x + 5$. That is 1.

So A-3, B-4, C-2, D-1. **Check D:** the new sum of roots is $-2 + 3 = 1$.""")

# ---------- assertion-reason ----------
# q27
T.assertion_reason(2, ["diminishing-roots"],
    r"Diminishing the roots of $x^3 - 6x^2 + 10x - 3 = 0$ by $2$ gives an equation with no $x^2$ term.",
    r"If the roots of $a_0x^n + a_1x^{n-1} + \cdots + a_n = 0$ are diminished by $h = -\dfrac{a_1}{na_0}$, the new roots have sum $0$.",
    0,
    r"""Both are true, and R explains A.

R: the new sum is $\sum(\alpha_i - h) = -\frac{a_1}{a_0} - nh = 0$, and the coefficient of $y^{n-1}$ is $-a_0$ times this sum.

A is the case $h = -\frac{-6}{3} = 2$. The transformed equation is $y^3 - 2y + 1 = 0$.""")

# q28
T.assertion_reason(2, ["reciprocal-equations"],
    r"$x = 1$ is a root of $x^5 - 3x^4 + 2x^3 - 2x^2 + 3x - 1 = 0$.",
    r"If $\alpha$ is a root of a reciprocal equation, then $\dfrac1\alpha$ is also a root.",
    1,
    r"""Both are true, but R does not explain A.

- A: the coefficients $1, -3, 2, -2, 3, -1$ are equal and opposite from the two ends (second class, odd degree). So the terms of $f(1)$ cancel in pairs: $1 - 3 + 2 - 2 + 3 - 1 = 0$.
- R: true, by the definition of a reciprocal equation.

R alone only pairs a root $\alpha$ with $\frac1\alpha$. It does not force $1$ to be a root: $x^2 + x + 1 = 0$ is reciprocal and $f(1) \ne 0$. The real reason for A is the second-class sign pattern combined with odd degree.""")

# q29
T.assertion_reason(3, ["symmetric-functions"],
    r"If $\alpha, \beta, \gamma$ are the roots of $x^3 + px^2 + qx + r = 0$, then $\alpha^2\beta^2 + \beta^2\gamma^2 + \gamma^2\alpha^2 = q^2 - 2pr$.",
    r"$\alpha^2\beta^2 + \beta^2\gamma^2 + \gamma^2\alpha^2 = (\alpha\beta + \beta\gamma + \gamma\alpha)^2 + 2\alpha\beta\gamma(\alpha + \beta + \gamma)$.",
    2,
    r"""A is true and R is false.

The correct identity has a minus sign:
$$(\alpha\beta + \beta\gamma + \gamma\alpha)^2 = \sum\alpha^2\beta^2 + 2\alpha\beta\gamma(\alpha + \beta + \gamma).$$

So $\sum\alpha^2\beta^2 = e_2^2 - 2e_1e_3 = q^2 - 2(-p)(-r) = q^2 - 2pr$.

**Check with $\alpha, \beta, \gamma = 1, 1, 1$:** the left side is $3$; R's right side gives $9 + 6 = 15$.""")

# q30
T.assertion_reason(1, ["vieta"],
    r"The three relations between the roots and coefficients of a cubic are enough to find its roots, with no further information.",
    r"For $x^3 + bx^2 + cx + d = 0$ with roots $\alpha, \beta, \gamma$, the coefficient $c$ equals $\alpha\beta + \beta\gamma + \gamma\alpha$.",
    3,
    r"""A is false and R is true.

R is Vieta's second relation: $c = \sum\alpha\beta$.

A is false. Eliminating two unknowns from the three relations just gives back the original cubic for the third root, so nothing is gained. The relations help only when an extra condition is known, such as roots in AP or GP, or two roots with sum zero.""")


def check():
    import sympy as sp
    x, y, z, p, q, r = sp.symbols("x y z p q r")

    def roots(f):
        return [rt for rt, m in sp.roots(sp.Poly(f, x)).items() for _ in range(m)] or sp.Poly(f, x).all_roots()

    def esym(f):
        P = sp.Poly(f, x); c = P.all_coeffs(); a0 = c[0]
        return [(-1) ** k * c[k] / a0 for k in range(1, len(c))]

    def psum(f, k):
        rs = sp.Poly(f, x).all_roots()
        return sp.nsimplify(sp.N(sum(rt ** k for rt in rs), 30), rational=True)

    def same_roots(f, g):
        # monic-normalised polynomials equal
        F, G = sp.Poly(f, x), sp.Poly(g, x)
        return sp.simplify(F.monic().as_expr() - G.monic().as_expr()) == 0

    # q1
    e = esym(2*x**4 - 3*x**3 + 5*x**2 - 7*x + 4); eq(e[2], sp.Rational(7, 2), "q1")
    # q2
    f = x**3 - 2*x**2 + 3*x - 4; eq(psum(f, 2), -2, "q2")
    # q3
    eq(psum(x**3 - 3*x + 1, 3), -3, "q3")
    # q4
    eq(psum(x**3 - 2*x + 1, 4), 8, "q4")
    # q5
    f = x**3 + 2*x**2 - 3*x - 1
    a, b, c = sp.Poly(f, x).all_roots()
    v = sp.N(a**2*b + a**2*c + b**2*a + b**2*c + c**2*a + c**2*b, 30)
    eq(sp.nsimplify(v, rational=True), 3, "q5")
    # q6
    a, b, c = roots(x**3 - 4*x**2 + x + 6)
    eq((a + b)*(b + c)*(c + a), 10, "q6")
    # q7
    assert sorted(roots(x**3 - 12*x**2 + 39*x - 28)) == [1, 4, 7], "q7"
    assert sp.expand((x-2)*(x-4)*(x-6)) != sp.expand(x**3 - 12*x**2 + 39*x - 28)
    # q8
    assert sorted(roots(x**3 - 14*x**2 + 56*x - 64)) == [2, 4, 8], "q8"
    # q9: AP condition — roots t-d, t, t+d
    t, d, A = sp.symbols("t d A")
    P = sp.Poly(sp.expand(A*(x-(t-d))*(x-t)*(x-(t+d))), x).all_coeffs()
    Aa, Bb, Cc, Dd = P
    eq(sp.expand(2*Bb**3 - 9*Aa*Bb*Cc + 27*Aa**2*Dd), 0, "q9 AP")
    # distractor GP condition fails on an AP cubic (1,4,7)
    Aa, Bb, Cc, Dd = sp.Poly(x**3 - 12*x**2 + 39*x - 28, x).all_coeffs()
    assert Aa*Cc**3 != Bb**3*Dd and 2*Bb**3 - 9*Aa*Bb*Cc - 27*Aa**2*Dd != 0
    assert Bb**3 - 3*Aa*Bb*Cc + 27*Aa**2*Dd != 0
    # and fails for a non-AP cubic (roots 1,2,4)
    Aa, Bb, Cc, Dd = sp.Poly(sp.expand((x-1)*(x-2)*(x-4)), x).all_coeffs()
    assert 2*Bb**3 - 9*Aa*Bb*Cc + 27*Aa**2*Dd != 0
    # q10
    rs = roots(x**4 - 2*x**3 + 4*x**2 + 6*x - 21)
    want = {sp.sqrt(3), -sp.sqrt(3), 1 + sp.I*sp.sqrt(6), 1 - sp.I*sp.sqrt(6)}
    assert set(sp.simplify(v) for v in rs) == want, ("q10", rs)
    # q11
    eq(sp.expand((x**2 + q)*(x + p)) - (x**3 + p*x**2 + q*x + p*q), 0, "q11")
    assert sorted(roots(x**3 - 2*x**2 - 9*x + 18)) == [-3, 2, 3]
    # q12
    f = 2*x**3 - 3*x**2 + 5*x - 7
    assert same_roots(sp.expand(x**3 * f.subs(x, 1/x)), 7*x**3 - 5*x**2 + 3*x - 2), "q12"
    # q13
    f = x**3 - x**2 + 2*x - 1
    assert same_roots(sp.expand(27 * f.subs(x, x/3)), x**3 - 3*x**2 + 18*x - 27), "q13"
    # q14
    g = sp.expand((x**4 - 8*x**3 + x**2 - x + 3).subs(x, y + 2))
    eq(sp.Poly(g, y).coeff_monomial(y**3), 0, "q14")
    # q15
    eq(sp.expand((x**3 - 6*x**2 + 10*x - 3).subs(x, y + 2)), y**3 - 2*y + 1, "q15")
    eq(sp.expand((x**3 - 6*x**2 + 10*x - 3).subs(x, y - 2)), y**3 - 12*y**2 + 46*y - 55, "q15 distractor")
    # q16
    f = x**3 - 2*x**2 + 3*x - 1
    res = sp.Poly(sp.resultant(f, y - x**2, x), y)
    eq(res.monic().as_expr(), y**3 + 2*y**2 + 5*y - 1, "q16")
    # q17
    rs = sp.Poly(x**3 - x - 1, x).all_roots()
    eq(sp.nsimplify(sp.N(sum((1 + a)/(1 - a) for a in rs), 30), rational=True), -7, "q17")
    eq(sp.expand(-((y-1)**3 - (y-1)*(y+1)**2 - (y+1)**3)), y**3 + 7*y**2 - y + 1, "q17 eqn")
    # q18: compare with symbolic product over roots
    fq = x**3 + p*x + q
    res = sp.expand(sp.resultant(fq, x*y + q, x))   # y = -q/x  <=> xy + q = 0
    eq(sp.expand(res / sp.Poly(res, y).LC()), y**3 - p*y**2 - q**2, "q18")
    # q19
    f = x**5 + 4*x**4 + x**3 + x**2 + 4*x + 1
    eq(f.subs(x, -1), 0, "q19"); assert f.subs(x, 1) == 12 and f.subs(x, 2) != 0
    # q20
    g = sp.expand((x**4 - 5*x**3 + 8*x**2 - 5*x + 1) / x**2)
    eq(g.subs(x, (z + sp.sqrt(z**2 - 4))/2), z**2 - 5*z + 6, "q20")
    # q21
    real = [rt for rt in sp.Poly(f, x).all_roots() if rt.is_real]
    assert len(real) == 3
    eq(sum(real), -5, "q21")
    eq(sp.quo(f, x + 1), x**4 + 3*x**3 - 2*x**2 + 3*x + 1, "q21 quotient")
    # q22
    a, b, c = sp.symbols("a b c")
    rs = roots(x**3 - 3*x + 2)   # p=-3, q=2
    eq(sum(v**2 for v in rs), 6, "q22 s1")              # -2p = 6  true
    eq(sum(v**3 for v in rs), -6, "q22 s2")             # -3q, so '3q' false
    rs = sp.Poly(x**3 - 3*x + 1, x).all_roots()        # q != 0 example for s3
    eq(sp.nsimplify(sp.N(sum(1/v for v in rs), 30), rational=True), 3, "q22 s3")  # -p/q = 3
    # q23
    f = x**3 - 6*x**2 + 10*x - 3
    rs = sp.Poly(f, x).all_roots()
    g = sp.expand(f.subs(x, x + 2))   # roots alpha - 2
    for v in rs:
        assert abs(sp.N(g.subs(x, v - 2))) < 1e-12
    assert abs(sp.N(sp.expand(x**3 * f.subs(x, 1/x)).subs(x, 1/rs[0]))) < 1e-12
    h_wrong = sp.Rational(-6, 3)     # a1/(n a0)
    eq(sp.Poly(sp.expand(f.subs(x, y + h_wrong)), y).coeff_monomial(y**2), -12, "q23 s3 false")
    # q24
    for f in [x**3 + 2*x**2 + 2*x + 1, x**5 - 3*x**4 + 2*x**3 - 2*x**2 + 3*x - 1]:
        assert f.subs(x, -1) == 0 or f.subs(x, 1) == 0
    f2 = x**4 + 3*x**3 - 3*x - 1
    eq(sp.rem(f2, x**2 - 1, x), 0, "q24 s2")
    assert (x**2 + x + 1).subs(x, 1) != 0 and (x**2 + x + 1).subs(x, -1) != 0
    # q25
    rs = [1, 2, 3]; a, b, c = rs
    vals = [sum(v**2 for v in rs), sum(sp.Rational(1, v) for v in rs),
            a**2*b + a**2*c + b**2*a + b**2*c + c**2*a + c**2*b, (a+b)*(b+c)*(c+a)]
    assert vals == [14, sp.Rational(11, 6), 48, 60], vals
    assert sorted(roots(x**3 - 6*x**2 + 11*x - 6)) == [1, 2, 3]
    # q26
    f = x**3 + 2*x**2 - x + 3
    assert same_roots(sp.expand(8*f.subs(x, x/2)), x**3 + 4*x**2 - 4*x + 24)
    assert same_roots(sp.expand(x**3*f.subs(x, 1/x)), 3*x**3 - x**2 + 2*x + 1)
    assert same_roots(sp.expand(-f.subs(x, -x)), x**3 - 2*x**2 - x - 3)
    assert same_roots(sp.expand(f.subs(x, x - 1)), x**3 - x**2 - 2*x + 5)
    # q27
    eq(sp.Poly(sp.expand((x**3 - 6*x**2 + 10*x - 3).subs(x, y + 2)), y).coeff_monomial(y**2), 0, "q27")
    # q28
    f = x**5 - 3*x**4 + 2*x**3 - 2*x**2 + 3*x - 1
    eq(f.subs(x, 1), 0, "q28 A")
    eq(sp.expand(x**5 * f.subs(x, 1/x)) + f, 0, "q28 reciprocal second class")
    # q29
    p_, q_, r_ = esym(x**3 + p*x**2 + q*x + r)
    e1, e2, e3 = p_, q_, r_
    al, be, ga = sp.symbols("al be ga")
    lhs = al**2*be**2 + be**2*ga**2 + ga**2*al**2
    E1, E2, E3 = al + be + ga, al*be + be*ga + ga*al, al*be*ga
    eq(sp.expand(lhs - (E2**2 - 2*E1*E3)), 0, "q29 identity")
    eq(e2**2 - 2*e1*e3, q**2 - 2*p*r, "q29 A")
    assert sp.expand(lhs - (E2**2 + 2*E1*E3)) != 0          # R false
    # q30: R true (Vieta e2 = c for monic)
    eq(esym(x**3 + p*x**2 + q*x + r)[1], q, "q30 R")


T.write(check)
