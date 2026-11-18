# Cubic and Biquadratic Equations

## Reducing the cubic {#reduced-cubic}

Throughout, coefficients are **real** unless stated otherwise. Two ways of writing a cubic are in use; this topic uses both, with fixed letters.

**Binomial form (Barnard–Child, Mapa).** Write the cubic with binomial coefficients:

$$a_0x^3 + 3a_1x^2 + 3a_2x + a_3 = 0, \qquad a_0 \ne 0.$$

The substitution $z = a_0x + a_1$, that is $x = \dfrac{z - a_1}{a_0}$, removes the $x^2$ term and gives the **reduced (depressed) cubic**

$$z^3 + 3Hz + G = 0, \qquad H = a_0a_2 - a_1^2, \qquad G = a_0^2a_3 - 3a_0a_1a_2 + 2a_1^3.$$

**Monic form.** For $x^3 + bx^2 + cx + d = 0$, put $x = y - \dfrac{b}{3}$. Then

$$y^3 + py + q = 0, \qquad p = c - \frac{b^2}{3}, \qquad q = \frac{2b^3}{27} - \frac{bc}{3} + d.$$

This is the binomial form with $a_0 = 1$, $a_1 = b/3$, so $3H = p$ and $G = q$. **In this topic the reduced cubic is always written $y^3 + 3Hy + G = 0$.** Read $H$ as one third of the coefficient of $y$ and $G$ as the constant term.

**Why $x = y - b/3$ works.** The roots shift by $b/3$, and the sum of the roots of the monic cubic is $-b$. The new roots therefore sum to $-b + 3\cdot\frac{b}{3} = 0$, so the $y^2$ coefficient is $0$. The same idea removes the $x^3$ term of a monic quartic: put $x = y - \frac{a}{4}$ in $x^4 + ax^3 + \cdots$.

**Example.** Reduce $x^3 - 9x^2 + 33x - 65 = 0$. Here $b = -9$, so put $x = y + 3$:

$$(y + 3)^3 - 9(y + 3)^2 + 33(y + 3) - 65 = y^3 + 6y - 20 = 0.$$

So $3H = 6$, $H = 2$, $G = -20$.

**Example (binomial form).** $x^3 + 3x^2 + 6x + 1 = 0$ has $a_0 = 1$, $a_1 = 1$, $a_2 = 2$, $a_3 = 1$. So $H = 2 - 1 = 1$ and $G = 1 - 6 + 2 = -3$. The reduced cubic is $z^3 + 3z - 3 = 0$, with $z = x + 1$.

:::caution
Keep the factor $3$ in mind. In $y^3 + 6y - 20 = 0$, $H$ is $2$, not $6$. Many wrong answers in Cardan problems come from using the coefficient of $y$ itself as $H$.
:::

:::exam-tip
To find the shift fast, divide the $x^2$ coefficient by $3a_0$ and change its sign: $x^3 - 6x^2 + \cdots$ needs $x = y + 2$. Check: the new $y^2$ coefficient is $3\cdot 2 - 6 = 0$.
:::

## Cardan's method {#cardan}

Solve $y^3 + 3Hy + G = 0$. Put $y = u + v$. Since $(u + v)^3 = u^3 + v^3 + 3uv(u + v)$,

$$u^3 + v^3 + (3uv + 3H)(u + v) + G = 0.$$

There are two unknowns and one equation, so impose a second condition: $uv = -H$. Then

$$u^3 + v^3 = -G, \qquad u^3v^3 = -H^3.$$

So $u^3$ and $v^3$ are the roots of the quadratic

$$t^2 + Gt - H^3 = 0, \qquad u^3, v^3 = \frac{-G \pm \sqrt{G^2 + 4H^3}}{2}.$$

This gives **Cardan's formula**

$$y = \sqrt[3]{\frac{-G + \sqrt{G^2 + 4H^3}}{2}} + \sqrt[3]{\frac{-G - \sqrt{G^2 + 4H^3}}{2}}.$$

**All three roots.** Each cube root has three values. Choose one value $u$ of the first, and take $v = -H/u$, so that $uv = -H$ holds. With $\omega = \frac{-1 + i\sqrt3}{2}$, the roots are

$$u + v, \qquad \omega u + \omega^2 v, \qquad \omega^2 u + \omega v.$$

The pairings $(\omega u, \omega^2 v)$ keep the product $uv$ unchanged. Pairing $\omega u$ with $\omega v$ does not, so it gives a wrong "root".

**Example 1.** $x^3 - 15x - 126 = 0$. Here $3H = -15$, so $H = -5$, and $G = -126$. Then $u^3 + v^3 = 126$ and $uv = 5$, so $u^3v^3 = 125$. The quadratic $t^2 - 126t + 125 = 0$ gives $t = 125, 1$. So $u = 5$, $v = 1$, and the roots are

$$5 + 1 = 6, \qquad 5\omega + \omega^2 = -3 + 2\sqrt3\,i, \qquad 5\omega^2 + \omega = -3 - 2\sqrt3\,i.$$

Check: the roots sum to $0$ (no $x^2$ term) and multiply to $6\cdot(9 + 12) = 126$.

**Example 2.** $y^3 + 6y - 20 = 0$, from the reduction above. Here $H = 2$, $G = -20$, and $G^2 + 4H^3 = 432 = (12\sqrt3)^2$. So $u^3 = 10 + 6\sqrt3$ and $v^3 = 10 - 6\sqrt3$. Since $(1 + \sqrt3)^3 = 10 + 6\sqrt3$, we get $u = 1 + \sqrt3$, $v = 1 - \sqrt3$ (indeed $uv = -2 = -H$). So $y = 2$, and $x = y + 3 = 5$. Dividing, $x^3 - 9x^2 + 33x - 65 = (x - 5)(x^2 - 4x + 13)$, so the other roots are $2 \pm 3i$.

:::exam-tip
To simplify $s = \sqrt[3]{A + \sqrt B} + \sqrt[3]{A - \sqrt B}$, cube it: $s^3 = 2A + 3\sqrt[3]{A^2 - B}\;s$. Then guess a small integer root of this cubic. For example, $\sqrt[3]{2 + \sqrt5} + \sqrt[3]{2 - \sqrt5}$ satisfies $s^3 = 4 - 3s$, so $s = 1$.
:::

## Nature of the roots and the discriminant {#nature-of-roots}

For real $H$ and $G$, the sign of $G^2 + 4H^3$ (the discriminant of Cardan's quadratic) decides the nature of the roots of $y^3 + 3Hy + G = 0$:

| $G^2 + 4H^3$ | Roots |
|:---|:---|
| $> 0$ | one real root and two non-real conjugate roots |
| $= 0$ | all real, at least two equal (all three equal iff $G = H = 0$) |
| $< 0$ | three distinct real roots (the **irreducible case**) |

The usual **discriminant** of $y^3 + py + q$ is $\Delta = -4p^3 - 27q^2$. With $p = 3H$ and $q = G$,

$$\Delta = -27\,(G^2 + 4H^3).$$

So $\Delta > 0$ means three distinct real roots, and $\Delta < 0$ means one real root. The two criteria agree; only the sign convention differs. For the binomial form, $G^2 + 4H^3 = a_0^2\,\Delta_1$, where $\Delta_1$ depends only on the coefficients, so the sign of $G^2 + 4H^3$ already decides the nature.

**Why.** If the roots are $\alpha, \beta, \gamma$, then $(\alpha - \beta)^2(\beta - \gamma)^2(\gamma - \alpha)^2 = -27(G^2 + 4H^3)$. If all roots are real and distinct, the left side is positive. If $\beta, \gamma = m \pm in$ with $n \ne 0$, the left side is $-4n^2\big((\alpha - m)^2 + n^2\big)^2 < 0$.

**Two quick consequences.**

- If $H > 0$, then $G^2 + 4H^3 > 0$, so there is exactly one real root. (Also, $y^3 + 3Hy$ is then strictly increasing.)
- Three real roots need $H < 0$. But $H < 0$ alone is not enough: $y^3 - 3y + 3 = 0$ has $H = -1$, $G = 3$ and $G^2 + 4H^3 = 5 > 0$.

**Examples.**

- $x^3 - 3x + 2 = 0$: $H = -1$, $G = 2$, $G^2 + 4H^3 = 0$. The roots are $1, 1, -2$.
- $x^3 - 12x + k = 0$: $H = -4$, so three distinct real roots iff $k^2 < 256$, that is $\lvert k\rvert < 16$.

```plot
title: $y = x^3 - 3x + c$ for $c = 1, 2, 3$ ($G^2 + 4H^3 = c^2 - 4$)
x: -2.6, 2.2
y: -3, 7
f: x^3 - 3x + 1 | $c = 1$: three real roots
f: x^3 - 3x + 2 | $c = 2$: a double root at $x = 1$
f: x^3 - 3x + 3 | $c = 3$: one real root
hline: 0
```

:::caution
"$G^2 + 4H^3 = 0$" does **not** mean all three roots are equal. That needs $G = H = 0$ as well, as in $(x - 1)^3 = 0$.
:::

## The irreducible case: trigonometric solution {#trigonometric}

When $G^2 + 4H^3 < 0$, the cubic has three distinct real roots, yet $\sqrt{G^2 + 4H^3}$ is imaginary. Cardan's formula then needs **cube roots of non-real complex numbers**: $u$ and $v$ are complex conjugates, and $u + v$ is real. This is the *casus irreducibilis*. It happens even when the roots are integers: $x^3 - 7x + 6 = 0$ has roots $1, 2, -3$, but $G^2 + 4H^3 = 36 - \frac{1372}{27} < 0$.

**Trigonometric method.** Here $H < 0$. Put $y = 2\sqrt{-H}\cos\theta$. Using $4\cos^3\theta - 3\cos\theta = \cos 3\theta$:

$$y^3 + 3Hy + G = 2(-H)^{3/2}\cos 3\theta + G = 0, \qquad \cos 3\theta = \frac{-G}{2(-H)^{3/2}}.$$

The right side lies in $(-1, 1)$ exactly when $G^2 < -4H^3$, that is in the irreducible case. If $\theta_0$ is one solution, the three roots are

$$y_k = 2\sqrt{-H}\,\cos\!\left(\theta_0 + \frac{2k\pi}{3}\right), \qquad k = 0, 1, 2.$$

**Example 1.** $y^3 - 3y + 1 = 0$. Here $H = -1$ and $G = 1$, so $y = 2\cos\theta$ and $\cos 3\theta = -\frac12$. Take $3\theta_0 = \frac{2\pi}{3}$, so $\theta_0 = \frac{2\pi}{9}$. The roots are

$$2\cos\frac{2\pi}{9}, \qquad 2\cos\frac{8\pi}{9}, \qquad 2\cos\frac{14\pi}{9} = 2\cos\frac{4\pi}{9}.$$

**Example 2.** $x^3 - 3x - 1 = 0$. Here $\cos 3\theta = \frac12$, so $\theta_0 = \frac{\pi}{9}$. The roots are $2\cos\frac{\pi}{9}$, $2\cos\frac{7\pi}{9}$ and $2\cos\frac{13\pi}{9} = 2\cos\frac{5\pi}{9}$. The largest is $2\cos\frac{\pi}{9} \approx 1.879$.

:::exam-tip
Check the scale first. For $y^3 - 3y \pm 1 = 0$ the roots are $2\cos(\cdot)$, not $\cos(\cdot)$, because $\lvert y\rvert$ can exceed $1$. A root list whose sum is not $0$ is wrong at once: the reduced cubic has no $y^2$ term.
:::

## Ferrari's method for the biquadratic {#ferrari}

A **biquadratic** is a quartic (degree-4) equation. Ferrari's method writes it as a **difference of two squares**. Write the quartic as

$$x^4 + 2px^3 + qx^2 + 2rx + s = 0.$$

Add terms to complete the square on the left, with a free parameter $\lambda$:

$$(x^2 + px + \lambda)^2 = (2\lambda + p^2 - q)\,x^2 + 2(p\lambda - r)\,x + (\lambda^2 - s).$$

The right side is a quadratic in $x$. It is a perfect square $(mx + n)^2$ exactly when its discriminant vanishes:

$$(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s).$$

This cubic in $\lambda$ is **Ferrari's resolvent cubic**. Take **any one** root $\lambda$ of it (a rational one if you can find it). Then

$$(x^2 + px + \lambda)^2 - (mx + n)^2 = 0 \;\Longrightarrow\; x^2 + px + \lambda = \pm(mx + n),$$

which gives two quadratics.

**Roots of the resolvent.** If the quartic has roots $\alpha, \beta, \gamma, \delta$, the three roots of the resolvent are

$$\frac{\alpha\beta + \gamma\delta}{2}, \qquad \frac{\alpha\gamma + \beta\delta}{2}, \qquad \frac{\alpha\delta + \beta\gamma}{2}.$$

Each root corresponds to one way of splitting the four roots into two pairs.

**Example.** Solve $x^4 - 2x^3 - x^2 + 6x - 3 = 0$. Here $p = -1$, $q = -1$, $r = 3$, $s = -3$. The resolvent is

$$(-\lambda - 3)^2 = (2\lambda + 2)(\lambda^2 + 3) \iff 2\lambda^3 + \lambda^2 - 3 = 0,$$

which has the root $\lambda = 1$. Then

$$(x^2 - x + 1)^2 = 4x^2 - 8x + 4 = (2x - 2)^2.$$

So $x^2 - x + 1 = 2x - 2$, giving $x^2 - 3x + 3 = 0$; or $x^2 - x + 1 = -(2x - 2)$, giving $x^2 + x - 1 = 0$. The roots are

$$\frac{3 \pm i\sqrt3}{2}, \qquad \frac{-1 \pm \sqrt5}{2}.$$

Check with the resolvent: the products of the two pairs are $3$ and $-1$, and $\frac{3 + (-1)}{2} = 1 = \lambda$.

:::caution
Watch the signs. The $x$-coefficient on the right is $2(p\lambda - r)$, and the constant is $\lambda^2 - s$, not $\lambda^2 + s$. Also, when the quartic is written $x^4 + ax^3 + bx^2 + cx + d$, then $p = a/2$ and $r = c/2$.
:::

## Descartes's method {#descartes-method}

Descartes's method also reduces a quartic to a cubic, but it factorises directly.

**Step 1: remove the cubic term.** For $x^4 + ax^3 + bx^2 + cx + d = 0$, put $x = y - \frac{a}{4}$. This gives

$$y^4 + qy^2 + ry + s = 0.$$

**Step 2: factorise.** Look for

$$y^4 + qy^2 + ry + s = (y^2 + ky + l)(y^2 - ky + m).$$

The $y$-coefficients are $k$ and $-k$ because the quartic has no $y^3$ term. Comparing coefficients:

$$l + m - k^2 = q, \qquad k(m - l) = r, \qquad lm = s.$$

**Step 3: eliminate $l$ and $m$.** Use $4lm = (l + m)^2 - (m - l)^2$:

$$4s = (q + k^2)^2 - \frac{r^2}{k^2}.$$

With $t = k^2$, this gives the cubic

$$t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0.$$

When $r \ne 0$, this cubic is negative at $t = 0$ and tends to $+\infty$, so it has a **positive** root $t = k^2$. That root gives a real $k$, then $l$ and $m$ from $l + m = q + k^2$ and $m - l = r/k$. Each quadratic factor then gives two roots. (If $r = 0$, the equation is already a quadratic in $y^2$.)

**Relation to the roots.** The roots of $y^2 + ky + l$ sum to $-k$. So, for the reduced quartic with roots $\alpha, \beta, \gamma, \delta$, the cubic in $t$ has roots $(\alpha + \beta)^2$, $(\alpha + \gamma)^2$ and $(\alpha + \delta)^2$.

**Example.** $y^4 - 2y^2 + 8y - 3 = 0$ has $q = -2$, $r = 8$, $s = -3$. The cubic is $t^3 - 4t^2 + 16t - 64 = 0$, that is $(t - 4)(t^2 + 16) = 0$. So $t = 4$ and $k = 2$. Then $l + m = 2$ and $m - l = 4$, so $l = -1$, $m = 3$:

$$y^4 - 2y^2 + 8y - 3 = (y^2 + 2y - 1)(y^2 - 2y + 3).$$

The roots are $-1 \pm \sqrt2$ and $1 \pm i\sqrt2$.

:::exam-tip
Ferrari and Descartes both lead to a cubic, and both need only one root of it. Descartes's cubic needs the cubic term removed first; Ferrari's does not.
:::

## Quick checks and traps {#exam-tips}

- **Reduction shift.** $x = y - \frac{b}{3}$ for a monic cubic, $x = y - \frac{a}{4}$ for a monic quartic. In binomial form, $z = a_0x + a_1$.
- **$H$ is one third** of the coefficient of $y$: $y^3 - 15y - 126$ has $H = -5$, $G = -126$.
- **Cardan's quadratic** is $t^2 + Gt - H^3 = 0$, from $u^3 + v^3 = -G$ and $uv = -H$.
- **Nature:** $G^2 + 4H^3 > 0$ gives one real root, $= 0$ a repeated real root, $< 0$ three distinct real roots. $\Delta = -27(G^2 + 4H^3)$ has the opposite sign.
- **$H > 0$** always gives exactly one real root; $H < 0$ alone proves nothing.
- **Irreducible case:** Cardan's formula still works but needs complex cube roots, even for integer roots ($x^3 - 7x + 6 = 0$). Use $y = 2\sqrt{-H}\cos\theta$ and $\cos 3\theta = -G/\big(2(-H)^{3/2}\big)$.
- **Sum test:** the roots of a reduced cubic (or reduced quartic) sum to $0$. This rules out many options.
- **Simplifying nested radicals:** $\sqrt[3]{A + \sqrt B} + \sqrt[3]{A - \sqrt B} = s$ satisfies $s^3 = 2A + 3\sqrt[3]{A^2 - B}\,s$.
- **Ferrari's resolvent:** $(p\lambda - r)^2 = (2\lambda + p^2 - q)(\lambda^2 - s)$ for $x^4 + 2px^3 + qx^2 + 2rx + s$. Its roots are $\frac12(\alpha\beta + \gamma\delta)$ and the two similar pair sums.
- **Descartes's cubic:** $t^3 + 2qt^2 + (q^2 - 4s)t - r^2 = 0$ in $t = k^2$, for the reduced quartic $y^4 + qy^2 + ry + s$.
