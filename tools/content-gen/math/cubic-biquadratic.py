import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.cubic-biquadratic")

# ---------------------------------------------------------------- reduction
T.single(1, ["reduced-cubic", "exam-tips"],
    r"To remove the $x^2$ term from $x^3 - 6x^2 + 11x - 6 = 0$, the substitution is",
    [r"$x = y + 2$", r"$x = y - 2$", r"$x = y + 6$", r"$x = y + 3$"],
    r"""For a monic cubic $x^3 + bx^2 + \cdots$, put $x = y - \frac{b}{3}$. Here $b = -6$, so $x = y + 2$.

Check: the $y^2$ coefficient of $(y + 2)^3 - 6(y + 2)^2$ is $3\cdot 2 - 6 = 0$.

$x = y - 2$ is the sign slip; $x = y + 6$ forgets to divide by $3$.""")

T.single(2, ["reduced-cubic"],
    r"The substitution $x = y + 3$ transforms $x^3 - 9x^2 + 33x - 65 = 0$ into",
    [r"$y^3 + 6y - 20 = 0$", r"$y^3 + 6y + 20 = 0$", r"$y^3 - 6y - 20 = 0$", r"$y^3 + 33y - 65 = 0$"],
    r"""Expand:
$$(y + 3)^3 - 9(y + 3)^2 + 33(y + 3) - 65.$$
- $y^2$: $9 - 9 = 0$.
- $y$: $27 - 54 + 33 = 6$.
- constant: $27 - 81 + 99 - 65 = -20$.

So $y^3 + 6y - 20 = 0$. Check: $x = 5$ is a root of the original, and $y = 2$ is a root of $y^3 + 6y - 20$.""")

T.single(2, ["reduced-cubic"],
    r"The substitution $z = a_0x + a_1$ reduces $a_0x^3 + 3a_1x^2 + 3a_2x + a_3 = 0$ to $z^3 + 3Hz + G = 0$. Then $H$ equals",
    [r"$a_0a_2 - a_1^2$", r"$a_1^2 - a_0a_2$", r"$a_0a_2 - 3a_1^2$", r"$a_0a_3 - a_1a_2$"],
    r"""Multiply the cubic by $a_0^2$ and write $a_0x = z - a_1$:
$$(z - a_1)^3 + 3a_1(z - a_1)^2 + 3a_0a_2(z - a_1) + a_0^2a_3 = 0.$$
The $z$-coefficient is $3a_1^2 - 6a_1^2 + 3a_0a_2 = 3(a_0a_2 - a_1^2)$, so
$$H = a_0a_2 - a_1^2.$$
$a_1^2 - a_0a_2$ is the sign slip.""")

T.single(2, ["reduced-cubic"],
    r"Write $x^3 + 3x^2 + 6x + 1 = 0$ as $a_0x^3 + 3a_1x^2 + 3a_2x + a_3 = 0$ and reduce it to $z^3 + 3Hz + G = 0$ with $z = a_0x + a_1$. Then $(H, G)$ is",
    [r"$(1, -3)$", r"$(1, 3)$", r"$(-1, -3)$", r"$(3, -3)$"],
    r"""Here $a_0 = 1$, $a_1 = 1$, $a_2 = 2$, $a_3 = 1$. So
$$H = a_0a_2 - a_1^2 = 1, \qquad G = a_0^2a_3 - 3a_0a_1a_2 + 2a_1^3 = 1 - 6 + 2 = -3.$$
Direct check: with $x = z - 1$ the cubic becomes $z^3 + 3z - 3 = 0$.

$(3, -3)$ uses the coefficient of $z$ itself as $H$.""")

# ---------------------------------------------------------------- Cardan
T.single(1, ["cardan"],
    r"In Cardan's method for $y^3 + 3Hy + G = 0$, put $y = u + v$ with $uv = -H$. Then $u^3$ and $v^3$ are the roots of",
    [r"$t^2 + Gt - H^3 = 0$", r"$t^2 - Gt - H^3 = 0$", r"$t^2 + Gt + H^3 = 0$", r"$t^2 + 3Ht + G = 0$"],
    r"""Since $(u + v)^3 = u^3 + v^3 + 3uv(u + v)$, the condition $uv = -H$ leaves
$$u^3 + v^3 = -G, \qquad u^3v^3 = -H^3.$$
A quadratic with this sum and product is $t^2 + Gt - H^3 = 0$.

$t^2 - Gt - H^3$ uses $+G$ as the sum; $t^2 + Gt + H^3$ uses $H^3$ as the product.""")

T.single(3, ["cardan"],
    r"The non-real roots of $x^3 - 15x - 126 = 0$ are",
    [r"$-3 \pm 2\sqrt3\,i$", r"$3 \pm 2\sqrt3\,i$", r"$-3 \pm \sqrt3\,i$", r"$-3 \pm 4\sqrt3\,i$"],
    r"""Here $H = -5$, $G = -126$. So $u^3 + v^3 = 126$ and $u^3v^3 = 125$, giving $t^2 - 126t + 125 = 0$, $t = 125, 1$. So $u = 5$, $v = 1$, and the real root is $6$.

The other roots are $5\omega + \omega^2$ and $5\omega^2 + \omega$:
$$5\omega + \omega^2 = \frac{-5 + 5\sqrt3\,i}{2} + \frac{-1 - \sqrt3\,i}{2} = -3 + 2\sqrt3\,i.$$
**Check:** the three roots must sum to $0$, so the complex pair sums to $-6$, which rules out $3 \pm 2\sqrt3\,i$. Their product must be $126/6 = 21 = 9 + 12$, which picks $-3 \pm 2\sqrt3\,i$.""")

T.single(2, ["cardan", "exam-tips"],
    r"Cardan's formula for $y^3 + 6y - 20 = 0$ gives $y = \sqrt[3]{10 + 6\sqrt3} + \sqrt[3]{10 - 6\sqrt3}$. This number equals",
    [r"$2$", r"$1$", r"$2\sqrt3$", r"$\sqrt[3]{20}$"],
    r"""Note $(1 + \sqrt3)^3 = 1 + 3\sqrt3 + 9 + 3\sqrt3 = 10 + 6\sqrt3$, and similarly $(1 - \sqrt3)^3 = 10 - 6\sqrt3$. So
$$y = (1 + \sqrt3) + (1 - \sqrt3) = 2.$$
**Check:** $8 + 12 - 20 = 0$. The cube root of a sum is not the sum of cube roots, so $\sqrt[3]{20}$ is wrong.""")

# ---------------------------------------------------------------- nature
T.single(1, ["nature-of-roots"],
    r"The cubic $y^3 + 3Hy + G = 0$, with $H, G$ real, has one real root and two non-real roots if and only if",
    [r"$G^2 + 4H^3 > 0$", r"$G^2 + 4H^3 < 0$", r"$G^2 + 4H^3 = 0$", r"$G^2 - 4H^3 > 0$"],
    r"""The sign of $G^2 + 4H^3$, the discriminant of Cardan's quadratic $t^2 + Gt - H^3 = 0$, decides:
- $> 0$: one real root, two non-real conjugates;
- $= 0$: all real, at least two equal;
- $< 0$: three distinct real roots.

$G^2 + 4H^3 < 0$ is the irreducible case (three real roots), so it is the swapped condition.""")

T.single(1, ["nature-of-roots"],
    r"The equation $x^3 - 3x + 2 = 0$ has",
    [r"all roots real, two of them equal", r"three distinct real roots", r"one real root and two non-real roots", r"all three roots equal"],
    r"""Here $H = -1$, $G = 2$, so $G^2 + 4H^3 = 4 - 4 = 0$: all roots are real and at least two are equal. In fact
$$x^3 - 3x + 2 = (x - 1)^2(x + 2),$$
so the roots are $1, 1, -2$. All three are equal only when $G = H = 0$.""")

T.single(2, ["nature-of-roots"],
    r"The equation $x^3 - 12x + k = 0$ ($k$ real) has three distinct real roots if and only if",
    [r"$\lvert k\rvert < 16$", r"$\lvert k\rvert > 16$", r"$\lvert k\rvert \le 16$", r"$\lvert k\rvert < 4$"],
    r"""Here $3H = -12$, so $H = -4$, and $G = k$. Three distinct real roots need
$$G^2 + 4H^3 = k^2 - 256 < 0 \iff \lvert k\rvert < 16.$$
At $\lvert k\rvert = 16$ there is a double root (e.g. $x^3 - 12x + 16 = (x - 2)^2(x + 4)$), so $\le$ is wrong. $\lvert k\rvert < 4$ compares $k$ with $\lvert H\rvert$ instead of using $G^2 + 4H^3$.""")

T.single(2, ["nature-of-roots"],
    r"For $y^3 + py + q = 0$ write $p = 3H$, $q = G$. The discriminant $\Delta = -4p^3 - 27q^2$ equals",
    [r"$-27(G^2 + 4H^3)$", r"$27(G^2 + 4H^3)$", r"$-(G^2 + 4H^3)$", r"$-108(G^2 + 4H^3)$"],
    r"""Substitute:
$$\Delta = -4(3H)^3 - 27G^2 = -108H^3 - 27G^2 = -27(G^2 + 4H^3).$$
So $\Delta > 0$ (three distinct real roots) exactly when $G^2 + 4H^3 < 0$. The signs are opposite, which is why $27(G^2 + 4H^3)$ is the tempting slip.""")

# ---------------------------------------------------------------- trigonometric
T.single(3, ["trigonometric"],
    r"The roots of $y^3 - 3y + 1 = 0$ are",
    [r"$2\cos\frac{2\pi}{9},\ 2\cos\frac{4\pi}{9},\ 2\cos\frac{8\pi}{9}$",
     r"$2\cos\frac{\pi}{9},\ 2\cos\frac{5\pi}{9},\ 2\cos\frac{7\pi}{9}$",
     r"$\cos\frac{2\pi}{9},\ \cos\frac{4\pi}{9},\ \cos\frac{8\pi}{9}$",
     r"$2\sin\frac{2\pi}{9},\ 2\sin\frac{4\pi}{9},\ 2\sin\frac{8\pi}{9}$"],
    r"""$H = -1$, $G = 1$, and $G^2 + 4H^3 = -3 < 0$: the irreducible case. Put $y = 2\sqrt{-H}\cos\theta = 2\cos\theta$:
$$8\cos^3\theta - 6\cos\theta + 1 = 2\cos 3\theta + 1 = 0, \qquad \cos 3\theta = -\tfrac12.$$
So $\theta = \frac{2\pi}{9} + \frac{2k\pi}{3}$, giving $2\cos\frac{2\pi}{9}$, $2\cos\frac{8\pi}{9}$, $2\cos\frac{14\pi}{9} = 2\cos\frac{4\pi}{9}$.

The set with $\frac{\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}$ solves $\cos 3\theta = +\frac12$, i.e. $y^3 - 3y - 1 = 0$. The set without the factor $2$ has the wrong scale.""")

T.single(2, ["trigonometric"],
    r"In the irreducible case of $y^3 + 3Hy + G = 0$ (so $H < 0$), the substitution $y = 2\sqrt{-H}\cos\theta$ leads to",
    [r"$\cos 3\theta = -\dfrac{G}{2(-H)^{3/2}}$", r"$\cos 3\theta = \dfrac{G}{2(-H)^{3/2}}$",
     r"$\cos 3\theta = -\dfrac{G}{(-H)^{3/2}}$", r"$\cos 3\theta = -\dfrac{G}{4(-H)^{3/2}}$"],
    r"""Let $h = \sqrt{-H}$, so $H = -h^2$. Then
$$y^3 + 3Hy + G = 8h^3\cos^3\theta - 6h^3\cos\theta + G = 2h^3(4\cos^3\theta - 3\cos\theta) + G = 2h^3\cos 3\theta + G.$$
Setting this to $0$ gives $\cos 3\theta = -\dfrac{G}{2(-H)^{3/2}}$. Dropping the minus sign is the usual slip.""")

T.single(2, ["trigonometric"],
    r"The largest root of $x^3 - 3x - 1 = 0$ is",
    [r"$2\cos\frac{\pi}{9}$", r"$2\cos\frac{2\pi}{9}$", r"$2\cos\frac{\pi}{18}$", r"$\sqrt3$"],
    r"""$H = -1$, $G = -1$. Put $x = 2\cos\theta$: $2\cos 3\theta - 1 = 0$, so $\cos 3\theta = \frac12$ and $\theta = \frac{\pi}{9}, \frac{7\pi}{9}, \frac{13\pi}{9}$.

The largest of $2\cos\theta$ is $2\cos\frac{\pi}{9} \approx 1.879$.

$2\cos\frac{2\pi}{9} \approx 1.532$ is the largest root of $y^3 - 3y + 1 = 0$ (the sign slip $\cos 3\theta = -\frac12$). $\sqrt3$ is not a root: $3\sqrt3 - 3\sqrt3 - 1 = -1 \ne 0$.""")

# ---------------------------------------------------------------- Ferrari
T.single(2, ["ferrari"],
    r"Ferrari's method writes $x^4 + 2px^3 + qx^2 + 2rx + s = 0$ as $(x^2 + px + \lambda)^2 = (2\lambda + p^2 - q)x^2 + 2(p\lambda - r)x + (\lambda^2 - s)$. The resolvent cubic in $\lambda$ is",
    [r"$(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s)$",
     r"$(p\lambda + r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s)$",
     r"$(p\lambda - r)^2 = (2\lambda - p^2 + q)(\lambda^2 - s)$",
     r"$(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 + s)$"],
    r"""The right side $Ax^2 + 2Bx + C$, with $A = 2\lambda + p^2 - q$, $B = p\lambda - r$, $C = \lambda^2 - s$, is a perfect square iff $B^2 = AC$:
$$(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s).$$
The other options copy a coefficient with the wrong sign.""")

T.single(2, ["ferrari"],
    r"To solve $x^4 - 2x^3 - x^2 + 6x - 3 = 0$ by Ferrari's method, write it as $(x^2 - x + \lambda)^2 = (\text{a quadratic in } x)$. A rational value of $\lambda$ that makes the right side a perfect square is",
    [r"$\lambda = 1$", r"$\lambda = -1$", r"$\lambda = 3$", r"$\lambda = \frac12$"],
    r"""Here $p = -1$, $q = -1$, $r = 3$, $s = -3$. The right side is
$$(2\lambda + 2)x^2 - 2(\lambda + 3)x + (\lambda^2 + 3).$$
It is a square iff $(\lambda + 3)^2 = (2\lambda + 2)(\lambda^2 + 3)$, i.e.
$$2\lambda^3 + \lambda^2 - 3 = 0.$$
$\lambda = 1$ works: $2 + 1 - 3 = 0$. Then the right side is $4x^2 - 8x + 4 = (2x - 2)^2$. The other values do not satisfy the resolvent.""")

T.single(3, ["ferrari"],
    r"The roots of $x^4 - 2x^3 - x^2 + 6x - 3 = 0$ are",
    [r"$\frac{-1 \pm \sqrt5}{2},\ \frac{3 \pm i\sqrt3}{2}$", r"$\frac{1 \pm \sqrt5}{2},\ \frac{3 \pm i\sqrt3}{2}$",
     r"$\frac{-1 \pm \sqrt5}{2},\ \frac{-3 \pm i\sqrt3}{2}$", r"$\frac{-1 \pm \sqrt3}{2},\ \frac{3 \pm i\sqrt5}{2}$"],
    r"""With $\lambda = 1$ (a root of the resolvent $2\lambda^3 + \lambda^2 - 3 = 0$):
$$(x^2 - x + 1)^2 = (2x - 2)^2.$$
- $x^2 - x + 1 = 2x - 2$ gives $x^2 - 3x + 3 = 0$, so $x = \frac{3 \pm i\sqrt3}{2}$.
- $x^2 - x + 1 = -(2x - 2)$ gives $x^2 + x - 1 = 0$, so $x = \frac{-1 \pm \sqrt5}{2}$.

**Check:** the four roots must sum to $2$: $(-1) + 3 = 2$. The second and third options sum to $4$ and $-4$.""")

T.single(3, ["ferrari"],
    r"$\alpha, \beta, \gamma, \delta$ are the roots of $x^4 + 2px^3 + qx^2 + 2rx + s = 0$. The roots of Ferrari's resolvent cubic $(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s)$ are",
    [r"$\frac12(\alpha\beta + \gamma\delta),\ \frac12(\alpha\gamma + \beta\delta),\ \frac12(\alpha\delta + \beta\gamma)$",
     r"$\alpha\beta + \gamma\delta,\ \alpha\gamma + \beta\delta,\ \alpha\delta + \beta\gamma$",
     r"$(\alpha + \beta)^2,\ (\alpha + \gamma)^2,\ (\alpha + \delta)^2$",
     r"$\frac12(\alpha + \beta)(\gamma + \delta),\ \frac12(\alpha + \gamma)(\beta + \delta),\ \frac12(\alpha + \delta)(\beta + \gamma)$"],
    r"""For a root $\lambda$, the quartic splits as $x^2 + px + \lambda \mp (mx + n)$. The two factors have constant terms $\lambda - n$ and $\lambda + n$, which are the products of the root pairs, say $\alpha\beta$ and $\gamma\delta$. Adding,
$$\lambda = \frac{\alpha\beta + \gamma\delta}{2}.$$
The other two pairings give the other two roots.

Example: $x^4 - 2x^3 - x^2 + 6x - 3$ has pair products $-1$ and $3$, and $\lambda = 1$ is a resolvent root. The squares $(\alpha + \beta)^2$ belong to Descartes's cubic for a reduced quartic, not to Ferrari's.""")

# ---------------------------------------------------------------- Descartes
T.single(1, ["descartes-method", "exam-tips"],
    r"Before applying Descartes's method to $x^4 - 8x^3 + 3x^2 + x - 5 = 0$, the cubic term is removed by putting",
    [r"$x = y + 2$", r"$x = y - 2$", r"$x = y + 8$", r"$x = y + 4$"],
    r"""For $x^4 + ax^3 + \cdots$, put $x = y - \frac{a}{4}$. Here $a = -8$, so $x = y + 2$.

Check: the $y^3$ coefficient of $(y + 2)^4 - 8(y + 2)^3$ is $4\cdot 2 - 8 = 0$. $x = y + 4$ divides by $2$ instead of $4$.""")

T.single(3, ["descartes-method"],
    r"In Descartes's method, $y^4 + qy^2 + ry + s = (y^2 + ky + l)(y^2 - ky + m)$. Then $t = k^2$ satisfies",
    [r"$t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0$", r"$t^3 + 2qt^2 + (q^2 + 4s)t - r^2 = 0$",
     r"$t^3 - 2qt^2 + (q^2 - 4s)t - r^2 = 0$", r"$t^3 + 2qt^2 + (q^2 - 4s)t + r^2 = 0$"],
    r"""Comparing coefficients: $l + m = q + k^2$, $m - l = r/k$, $lm = s$. Since $4lm = (l + m)^2 - (m - l)^2$,
$$4s = (q + k^2)^2 - \frac{r^2}{k^2}.$$
Multiply by $k^2$ and put $t = k^2$:
$$t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0.$$
**Check:** the constant term is $-r^2 \le 0$, which is why this cubic has a positive root when $r \ne 0$; the option with $+r^2$ fails this.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["nature-of-roots", "trigonometric"],
    r"Consider the equation $x^3 - 7x + 6 = 0$, written as $x^3 + 3Hx + G = 0$:",
    [r"It has three distinct real roots.",
     r"Cardan's formula expresses its roots using cube roots of non-real complex numbers.",
     r"Because its roots are integers, $G^2 + 4H^3 \ge 0$."],
    [r"1 and 2 only", r"1 only", r"1 and 3 only", r"1, 2 and 3"],
    r"""$x^3 - 7x + 6 = (x - 1)(x - 2)(x + 3)$, so statement 1 is true.

$H = -\frac73$, $G = 6$, and
$$G^2 + 4H^3 = 36 - \frac{1372}{27} = -\frac{400}{27} < 0.$$
So $\sqrt{G^2 + 4H^3}$ is imaginary, and Cardan's $u^3, v^3$ are non-real: statement 2 is true and statement 3 is false.

This is the irreducible case: the roots being rational does not help Cardan's formula.""")

T.statements(2, ["ferrari", "descartes-method"],
    r"Consider the following statements about solving a real quartic:",
    [r"Ferrari's resolvent of a quartic is a cubic equation.",
     r"In Ferrari's method, any one root of the resolvent is enough to split the quartic into two quadratics.",
     r"For $y^4 + qy^2 + ry + s$ with $r \ne 0$, Descartes's cubic $t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0$ has a positive root."],
    [r"1, 2 and 3", r"1 and 2 only", r"1 and 3 only", r"2 and 3 only"],
    r"""1. True: $(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s)$ has degree $3$ in $\lambda$.
2. True: one $\lambda$ makes the right side $(mx + n)^2$, and then $x^2 + px + \lambda = \pm(mx + n)$.
3. True: the cubic is $-r^2 < 0$ at $t = 0$ and tends to $+\infty$, so it crosses zero at some $t > 0$.

So all three are correct.""")

T.statements(3, ["nature-of-roots"],
    r"For the cubic $y^3 + 3Hy + G = 0$ with real $H, G$, consider:",
    [r"If $H > 0$, the equation has exactly one real root.",
     r"If $G^2 + 4H^3 = 0$, all three roots are equal.",
     r"If $H < 0$, the equation has three real roots."],
    [r"1 only", r"1 and 2 only", r"1 and 3 only", r"2 and 3 only"],
    r"""1. True: $H > 0$ makes $G^2 + 4H^3 > 0$ (also $y^3 + 3Hy$ is strictly increasing).
2. False: $y^3 - 3y + 2 = (y - 1)^2(y + 2)$ has $G^2 + 4H^3 = 0$ but roots $1, 1, -2$. All three are equal only if $G = H = 0$.
3. False: $y^3 - 3y + 3 = 0$ has $H = -1$ but $G^2 + 4H^3 = 9 - 4 = 5 > 0$, so only one real root.""")

# ---------------------------------------------------------------- match
T.match(1, ["nature-of-roots"],
    r"Match each cubic in List I with the nature of its roots in List II.",
    [r"$x^3 - 3x + 1 = 0$", r"$x^3 - 3x + 2 = 0$", r"$x^3 - 3x + 3 = 0$", r"$x^3 - 3x^2 + 3x - 1 = 0$"],
    [r"all three roots equal", r"one real and two non-real roots", r"three distinct real roots", r"all real, exactly two equal"],
    [r"A-3, B-4, C-2, D-1", r"A-2, B-4, C-3, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-3, C-2, D-1"],
    r"""For $x^3 - 3x + c$: $H = -1$, $G = c$, so $G^2 + 4H^3 = c^2 - 4$.
- A ($c = 1$): $-3 < 0$, three distinct real roots (3).
- B ($c = 2$): $0$, roots $1, 1, -2$ (4).
- C ($c = 3$): $5 > 0$, one real root (2).
- D: $(x - 1)^3 = 0$, all three equal (1).

So A-3, B-4, C-2, D-1.""")

T.match(3, ["cardan", "exam-tips"],
    r"Each expression in List I is a real root given by Cardan's formula (real cube roots throughout). Match it with its value in List II.",
    [r"$\sqrt[3]{2 + \sqrt5} + \sqrt[3]{2 - \sqrt5}$", r"$\sqrt[3]{10 + 6\sqrt3} + \sqrt[3]{10 - 6\sqrt3}$",
     r"$\sqrt[3]{9 + 4\sqrt5} + \sqrt[3]{9 - 4\sqrt5}$", r"$\sqrt[3]{20 + 14\sqrt2} + \sqrt[3]{20 - 14\sqrt2}$"],
    [r"$3$", r"$1$", r"$4$", r"$2$"],
    [r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-3, D-1", r"A-2, B-1, C-4, D-3"],
    r"""For $s = \sqrt[3]{A + \sqrt B} + \sqrt[3]{A - \sqrt B}$, cubing gives $s^3 = 2A + 3\sqrt[3]{A^2 - B}\,s$.
- A: $A^2 - B = -1$, so $s^3 + 3s - 4 = 0$, $s = 1$ (2).
- B: $100 - 108 = -8$, so $s^3 + 6s - 20 = 0$, $s = 2$ (4).
- C: $81 - 80 = 1$, so $s^3 - 3s - 18 = 0$, $s = 3$ (1).
- D: $400 - 392 = 8$, so $s^3 - 6s - 40 = 0$, $s = 4$ (3).

Each cubic has $G^2 + 4H^3 > 0$, so $s$ is its only real root. Equivalently, $\left(\frac{1 + \sqrt5}{2}\right)^3 = 2 + \sqrt5$, $(1 + \sqrt3)^3 = 10 + 6\sqrt3$, $\left(\frac{3 + \sqrt5}{2}\right)^3 = 9 + 4\sqrt5$, $(2 + \sqrt2)^3 = 20 + 14\sqrt2$.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["cardan", "nature-of-roots"],
    r"$x^3 - 15x - 126 = 0$ has exactly one real root.",
    r"If $G^2 + 4H^3 > 0$, the real cubic $y^3 + 3Hy + G = 0$ has one real root and two non-real roots.",
    0,
    r"""Both are true. For this cubic $H = -5$, $G = -126$, and
$$G^2 + 4H^3 = 15876 - 500 = 15376 > 0.$$
So R applies and explains A. (The roots are $6$ and $-3 \pm 2\sqrt3\,i$.)""")

T.assertion_reason(2, ["trigonometric", "nature-of-roots"],
    r"$x^3 - 7x + 6 = 0$ has three distinct real roots.",
    r"Cardan's formula gives every root of $x^3 - 7x + 6 = 0$ without using complex numbers.",
    2,
    r"""A is true: $x^3 - 7x + 6 = (x - 1)(x - 2)(x + 3)$.

R is false: $G^2 + 4H^3 = 36 - \frac{1372}{27} < 0$, so $\sqrt{G^2 + 4H^3}$ is imaginary and $u^3, v^3$ are non-real. This is the irreducible case.""")

T.assertion_reason(1, ["trigonometric"],
    r"The roots of $y^3 - 3y + 1 = 0$ are of the form $2\cos\theta$ for real $\theta$.",
    r"Every cubic equation with real coefficients has at least one real root.",
    1,
    r"""A is true: $G^2 + 4H^3 = 1 - 4 < 0$, so the substitution $y = 2\cos\theta$ gives $\cos 3\theta = -\frac12$ and three real roots $2\cos\frac{2\pi}{9}, 2\cos\frac{4\pi}{9}, 2\cos\frac{8\pi}{9}$.

R is true (non-real roots of a real polynomial occur in conjugate pairs, and the degree is odd). But R gives only one real root; it does not say that all three roots are real or lie in $[-2, 2]$. So R does not explain A.""")

T.assertion_reason(2, ["nature-of-roots"],
    r"All three roots of $x^3 - 3x + 2 = 0$ are equal.",
    r"If $G^2 + 4H^3 = 0$, the real cubic $y^3 + 3Hy + G = 0$ has all its roots real, with at least two equal.",
    3,
    r"""A is false: $x^3 - 3x + 2 = (x - 1)^2(x + 2)$, with roots $1, 1, -2$.

R is true. Here $G^2 + 4H^3 = 4 - 4 = 0$, which gives a repeated root. All three are equal only when $G = H = 0$.""")

T.assertion_reason(3, ["descartes-method"],
    r"For $y^4 + qy^2 + ry + s = 0$ with real coefficients and $r \ne 0$, Descartes's method always gives a factorisation into two quadratics with real coefficients.",
    r"A real cubic with positive leading coefficient and negative constant term has a positive real root.",
    0,
    r"""Both are true, and R explains A.

Descartes's cubic $t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0$ has constant term $-r^2 < 0$. By R (the cubic is negative at $0$ and tends to $+\infty$) it has a root $t = k^2 > 0$. So $k$ is real, and $l, m$ come from $l + m = q + k^2$ and $m - l = r/k$, both real.""")


def check():
    import sympy as sp
    x, y, z, t, lam, k = sp.symbols("x y z t lambda k")
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2

    def coeffs(e, v):
        return sp.Poly(sp.expand(e), v).all_coeffs()

    def nat(c3):  # (H, G) and G^2+4H^3 for monic reduced y^3+3Hy+G
        p = sp.Poly(c3, y).all_coeffs()
        H, G = p[2] / 3, p[3]
        return H, G, G**2 + 4 * H**3

    # q1 shift
    eq(coeffs((y + 2)**3 - 6 * (y + 2)**2 + 11 * (y + 2) - 6, y)[1], 0, "q1")
    for s in (-2, 6, 3):
        assert coeffs((y + s)**3 - 6 * (y + s)**2, y)[1] != 0
    # q2
    eq(sp.expand((y + 3)**3 - 9 * (y + 3)**2 + 33 * (y + 3) - 65), y**3 + 6 * y - 20, "q2")
    # q3, q4: H and G in binomial form; also G^2+4H^3 = a0^2 * (expr in coefficients)
    a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
    red = sp.expand(a0**2 * (a0 * x**3 + 3 * a1 * x**2 + 3 * a2 * x + a3)).subs(x, (z - a1) / a0)
    pc = sp.Poly(sp.expand(red), z).all_coeffs()
    eq(pc[0], 1, "q3 monic"); eq(pc[1], 0, "q3 no z^2")
    H, G = sp.simplify(pc[2] / 3), sp.simplify(pc[3])
    eq(H, a0 * a2 - a1**2, "q3")
    eq(G, a0**2 * a3 - 3 * a0 * a1 * a2 + 2 * a1**3, "notes G")
    q_, r_ = sp.div(sp.expand(G**2 + 4 * H**3), a0**2, a0)
    eq(r_, 0, "notes G^2+4H^3 divisible by a0^2")
    sub = {a0: 1, a1: 1, a2: 2, a3: 1}
    eq(H.subs(sub), 1, "q4 H"); eq(G.subs(sub), -3, "q4 G")
    eq(sp.expand((z - 1)**3 + 3 * (z - 1)**2 + 6 * (z - 1) + 1), z**3 + 3 * z - 3, "q4 direct")
    # monic reduction formulas in notes
    b, c, d = sp.symbols("b c d")
    mon = sp.Poly(sp.expand((y - b / 3)**3 + b * (y - b / 3)**2 + c * (y - b / 3) + d), y).all_coeffs()
    eq(mon[2], c - b**2 / 3, "notes p"); eq(mon[3], 2 * b**3 / 27 - b * c / 3 + d, "notes q")
    # q5 Cardan quadratic
    Hs, Gs, u, v = sp.symbols("H G u v")
    # u^3+v^3=-G, u^3 v^3 = -H^3 -> t^2 - (sum) t + prod
    eq(t**2 - (-Gs) * t + (-Hs**3), t**2 + Gs * t - Hs**3, "q5")
    eq(sp.expand((u + v)**3 + 3 * Hs * (u + v) + Gs).subs(v, -Hs / u), sp.expand(u**3 - Hs**3 / u**3 + Gs), "q5 derivation")
    # q6 roots of x^3-15x-126
    f6 = x**3 - 15 * x - 126
    eq(sp.expand((x - 6) * (x**2 + 6 * x + 21)), f6, "q6 factor")
    eq(sp.expand(5 * w + w**2), -3 + 2 * sp.sqrt(3) * sp.I, "q6 5w+w^2")
    eq(f6.subs(x, -3 + 2 * sp.sqrt(3) * sp.I), 0, "q6")
    for bad in (3 + 2 * sp.sqrt(3) * sp.I, -3 + sp.sqrt(3) * sp.I, -3 + 4 * sp.sqrt(3) * sp.I):
        assert sp.simplify(sp.expand(f6.subs(x, bad))) != 0
    # q7 nested radical = 2
    s7 = sp.real_root(10 + 6 * sp.sqrt(3), 3) + sp.real_root(10 - 6 * sp.sqrt(3), 3)
    eq(sp.N(s7, 30), 2, "q7")
    eq(sp.expand((1 + sp.sqrt(3))**3), 10 + 6 * sp.sqrt(3), "q7 cube")
    # q8 nature: examples for each sign
    for poly, want_real in ((y**3 - 3 * y + 3, 1), (y**3 - 3 * y + 1, 3)):
        Hn, Gn, D = nat(poly)
        nreal = len(sp.Poly(poly, y).real_roots())
        assert nreal == want_real and ((D > 0) == (want_real == 1)), "q8"
    # q9 x^3-3x+2
    eq(nat(y**3 - 3 * y + 2)[2], 0, "q9 disc")
    eq(sp.factor(x**3 - 3 * x + 2) - (x - 1)**2 * (x + 2), 0, "q9")
    # q10 |k|<16
    kk = sp.symbols("kk", real=True)
    eq(nat(y**3 - 12 * y + kk)[2], kk**2 - 256, "q10")
    eq(sp.expand((x - 2)**2 * (x + 4)), x**3 - 12 * x + 16, "q10 boundary")
    assert len(set(sp.Poly(x**3 - 12 * x + 10, x).real_roots())) == 3  # |k|<16 but >4
    assert len(set(sp.Poly(x**3 - 12 * x + 20, x).real_roots())) == 1
    # q11 discriminant
    p_, q_s = sp.symbols("p q")
    eq(sp.discriminant(y**3 + p_ * y + q_s, y), -4 * p_**3 - 27 * q_s**2, "q11 disc")
    eq((-4 * p_**3 - 27 * q_s**2).subs({p_: 3 * Hs, q_s: Gs}), -27 * (Gs**2 + 4 * Hs**3), "q11")
    # notes: product of squared differences = -27(G^2+4H^3)
    al, be = sp.symbols("alpha beta")
    ga = -al - be
    mono = sp.expand((y - al) * (y - be) * (y - ga))
    Hm, Gm = sp.Poly(mono, y).all_coeffs()[2] / 3, sp.Poly(mono, y).all_coeffs()[3]
    eq(sp.expand(((al - be) * (be - ga) * (ga - al))**2), sp.expand(-27 * (Gm**2 + 4 * Hm**3)), "notes disc")
    # q12 roots of y^3-3y+1
    f12 = y**3 - 3 * y + 1
    for ang in (2, 4, 8):
        eq(sp.N(f12.subs(y, 2 * sp.cos(ang * sp.pi / 9)), 30), 0, f"q12 {ang}")
    for wrong in (2 * sp.cos(sp.pi / 9), sp.cos(2 * sp.pi / 9), 2 * sp.sin(2 * sp.pi / 9)):
        assert abs(sp.N(f12.subs(y, wrong))) > 1e-6
    # q13 cos 3theta
    h, th = sp.symbols("h theta", positive=True)
    e13 = sp.expand_trig(((2 * h * sp.cos(th))**3 + 3 * (-h**2) * (2 * h * sp.cos(th)) + Gs))
    eq(sp.simplify(e13 - (2 * h**3 * sp.expand_trig(sp.cos(3 * th)) + Gs)), 0, "q13")
    # q14 largest root of x^3-3x-1
    rts = sp.Poly(x**3 - 3 * x - 1, x).real_roots()
    eq(sp.N(max(rts), 30), sp.N(2 * sp.cos(sp.pi / 9), 30), "q14")
    # q15 resolvent = discriminant condition
    P, Q, R, S = sp.symbols("p q r s")
    lhs = sp.expand((x**2 + P * x + lam)**2 - (x**4 + 2 * P * x**3 + Q * x**2 + 2 * R * x + S))
    A_, B2, C_ = sp.Poly(lhs, x).all_coeffs()
    eq(A_, 2 * lam + P**2 - Q, "q15 A"); eq(B2, 2 * (P * lam - R), "q15 B"); eq(C_, lam**2 - S, "q15 C")
    eq(sp.expand(B2**2 / 4 - A_ * C_), sp.expand((P * lam - R)**2 - (2 * lam + P**2 - Q) * (lam**2 - S)), "q15")
    # q16 resolvent root of example
    sub16 = {P: -1, Q: -1, R: 3, S: -3}
    res16 = sp.expand(((P * lam - R)**2 - (2 * lam + P**2 - Q) * (lam**2 - S)).subs(sub16))
    eq(res16, -(2 * lam**3 + lam**2 - 3), "q16 resolvent")
    eq(res16.subs(lam, 1), 0, "q16")
    for bad in (-1, 3, sp.Rational(1, 2)):
        assert res16.subs(lam, bad) != 0
    eq(sp.expand(lhs.subs(sub16).subs(lam, 1)), sp.expand((2 * x - 2)**2), "q16 square")
    # q17 roots
    f17 = x**4 - 2 * x**3 - x**2 + 6 * x - 3
    eq(sp.expand((x**2 + x - 1) * (x**2 - 3 * x + 3)), f17, "q17")
    for r0 in ((-1 + sp.sqrt(5)) / 2, (3 + sp.I * sp.sqrt(3)) / 2):
        eq(sp.expand(f17.subs(x, r0)), 0, "q17 root")
    for r0 in ((1 + sp.sqrt(5)) / 2, (-3 + sp.I * sp.sqrt(3)) / 2, (-1 + sp.sqrt(3)) / 2):
        assert sp.simplify(sp.expand(f17.subs(x, r0))) != 0
    # q18 resolvent roots = (ab+cd)/2 etc; test on roots 1,2,3,5 and on example
    for rr in ((1, 2, 3, 5), (1, -2, 4, 7)):
        a_, b_, c_, d_ = rr
        quart = sp.Poly(sp.expand((x - a_) * (x - b_) * (x - c_) * (x - d_)), x).all_coeffs()
        sb = {P: sp.Rational(quart[1], 2), Q: quart[2], R: sp.Rational(quart[3], 2), S: quart[4]}
        res = sp.expand(((P * lam - R)**2 - (2 * lam + P**2 - Q) * (lam**2 - S)).subs(sb))
        want = {sp.Rational(a_ * b_ + c_ * d_, 2), sp.Rational(a_ * c_ + b_ * d_, 2), sp.Rational(a_ * d_ + b_ * c_, 2)}
        assert set(sp.roots(res, lam).keys()) == want, "q18"
        assert not {a_ * b_ + c_ * d_}.issubset(set(sp.roots(res, lam).keys())), "q18 distractor"
    # q19 shift for quartic
    eq(sp.Poly(sp.expand((y + 2)**4 - 8 * (y + 2)**3 + 3 * (y + 2)**2 + (y + 2) - 5), y).all_coeffs()[1], 0, "q19")
    # q20 Descartes cubic; and roots (alpha+beta)^2
    l, m = sp.symbols("l m")
    prod = sp.Poly(sp.expand((y**2 + k * y + l) * (y**2 - k * y + m)), y).all_coeffs()
    ls, ms = (Q + k**2 - R / k) / 2, (Q + k**2 + R / k) / 2  # from l+m, m-l
    eq(prod[2].subs({l: ls, m: ms}), Q, "q20 y^2"); eq(prod[3].subs({l: ls, m: ms}), R, "q20 y")
    cub = sp.expand(4 * k**2 * (ls * ms - S))
    eq(cub.subs(k, sp.sqrt(t)), t**3 + 2 * Q * t**2 + (Q**2 - 4 * S) * t - R**2, "q20")
    # Descartes example in notes
    eq(sp.expand((y**2 + 2 * y - 1) * (y**2 - 2 * y + 3)), y**4 - 2 * y**2 + 8 * y - 3, "notes descartes")
    eq(sp.expand((t**3 + 2 * Q * t**2 + (Q**2 - 4 * S) * t - R**2).subs({Q: -2, R: 8, S: -3})), sp.expand((t - 4) * (t**2 + 16)), "notes descartes cubic")
    # Descartes cubic roots = (alpha+beta)^2 for a reduced quartic with roots 1,2,-1,-2? use 1,3,-2,-2
    rr = (1, 3, -2, -2)
    qc = sp.Poly(sp.expand(sp.prod([y - r0 for r0 in rr])), y).all_coeffs()
    assert qc[1] == 0
    dc = sp.Poly(t**3 + 2 * qc[2] * t**2 + (qc[2]**2 - 4 * qc[4]) * t - qc[3]**2, t)
    want = sorted([(rr[0] + rr[1])**2, (rr[0] + rr[2])**2, (rr[0] + rr[3])**2])
    got = sorted(sum([[r0] * mlt for r0, mlt in sp.roots(dc).items()], []))
    assert got == want, ("notes (a+b)^2", got, want)
    # statements 1: x^3-7x+6
    Hn, Gn, D = nat(y**3 - 7 * y + 6)
    eq(D, sp.Rational(-400, 27), "st1 disc")
    eq(sp.expand((x - 1) * (x - 2) * (x + 3)), x**3 - 7 * x + 6, "st1 roots")
    # statements 2: one lambda suffices (shown in q16); Descartes cubic at 0 is -r^2
    eq((t**3 + 2 * Q * t**2 + (Q**2 - 4 * S) * t - R**2).subs(t, 0), -R**2, "st2.3")
    # statements 3
    Hn, Gn, D = nat(y**3 + 3 * 2 * y + 5); assert D > 0
    assert len(sp.Poly(y**3 - 3 * y + 2, y).real_roots()) == 3 and len(set(sp.Poly(y**3 - 3 * y + 2, y).real_roots())) == 2
    eq(nat(y**3 - 3 * y + 3)[2], 5, "st3.3"); assert len(sp.Poly(y**3 - 3 * y + 3, y).real_roots()) == 1
    # match 1
    for poly, kind in ((x**3 - 3 * x + 1, (3, 3)), (x**3 - 3 * x + 2, (3, 2)), (x**3 - 3 * x + 3, (1, 1)), (x**3 - 3 * x**2 + 3 * x - 1, (3, 1))):
        rt = sp.Poly(poly, x).real_roots()
        assert (len(rt), len(set(rt))) == kind, ("m1", poly)
    # match 2
    vals = []
    for A, B in ((2, 5), (10, 108), (9, 80), (20, 392)):
        s_ = sp.real_root(A + sp.sqrt(B), 3) + sp.real_root(A - sp.sqrt(B), 3)
        vals.append(int(round(float(sp.N(s_, 30)))))
        eq(sp.N(s_, 30), vals[-1], "m2")
        cubic_s = t**3 - 3 * sp.real_root(A**2 - B, 3) * t - 2 * A
        eq(cubic_s.subs(t, vals[-1]), 0, "m2 cubic")
        Hn, Gn, D = nat(cubic_s.subs(t, y)); assert D > 0
    right = [3, 1, 4, 2]
    assert "A-2, B-4, C-1, D-3" == ", ".join(f"{L}-{right.index(vv) + 1}" for L, vv in zip("ABCD", vals))
    # AR1
    eq(nat(y**3 - 15 * y - 126)[2], 15376, "ar1")
    # AR3: roots in [-2,2] since 2cos
    assert all(abs(float(r0)) <= 2 for r0 in sp.Poly(y**3 - 3 * y + 1, y).real_roots())
    # AR5 example: q=0, r=1, s=1 -> cubic t^3 - 4t - 1 has positive root
    assert any(r0 > 0 for r0 in sp.Poly(t**3 - 4 * t - 1, t).real_roots())


T.write(check)
