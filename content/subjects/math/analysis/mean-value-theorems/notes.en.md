# Derivatives and Mean Value Theorems

## The derivative and differentiability {#derivative}

Let $f$ be defined on an interval $I$ and $a \in I$. $f$ is **differentiable at $a$** if

$$f'(a) = \lim_{h \to 0}\frac{f(a + h) - f(a)}{h}$$

exists and is finite. The **right** and **left derivatives** $Rf'(a)$ and $Lf'(a)$ use $h \to 0^+$ and $h \to 0^-$. At an interior point, $f'(a)$ exists $\iff$ both exist and are equal. At an end point of a closed interval only the one-sided derivative is used.

- **Geometric meaning:** $f'(a)$ is the slope of the tangent to $y = f(x)$ at $(a, f(a))$, the limit of the slopes of the chords through that point. The tangent is $y - f(a) = f'(a)(x - a)$.
- **Physical meaning:** if $s(t)$ is the position at time $t$, then $s'(t)$ is the velocity and $s''(t)$ the acceleration. In general $f'(a)$ is the instantaneous **rate of change** of $f$ with respect to $x$.

**Differentiable $\Rightarrow$ continuous.** For $h \ne 0$,

$$f(a + h) - f(a) = \frac{f(a + h) - f(a)}{h}\cdot h \to f'(a)\cdot 0 = 0.$$

The **converse fails**:

| Function at $x = 0$ | Continuous? | Differentiable? |
|:---|:---:|:---:|
| $\lvert x\rvert$ | yes | no: $Lf'(0) = -1$, $Rf'(0) = 1$ (a corner) |
| $x\sin\frac1x$, $f(0) = 0$ | yes | no: $\frac{f(h)}{h} = \sin\frac1h$ oscillates |
| $x^{1/3}$ | yes | no: $\frac{f(h)}{h} = h^{-2/3} \to \infty$ (vertical tangent) |
| $x^2\sin\frac1x$, $f(0) = 0$ | yes | yes, $f'(0) = 0$; but $f'$ is **not continuous** at $0$ |

For the last one, $\frac{f(h)}{h} = h\sin\frac1h \to 0$, while for $x \ne 0$

$$f'(x) = 2x\sin\frac1x - \cos\frac1x,$$

which has no limit as $x \to 0$. So a derivative can exist everywhere and still be discontinuous.

:::exam-tip
For $f(x) = x^p\sin\frac1x$, $f(0) = 0$ (with $p > 0$): $f$ is continuous at $0$ for $p > 0$, differentiable at $0$ for $p > 1$, and $f'$ is continuous at $0$ for $p > 2$.
:::

:::caution
"Differentiable at $a$" needs a **finite** limit. $x^{1/3}$ has a vertical tangent at $0$, but it is not differentiable there.
:::

## Chain rule, successive derivatives and Leibniz's theorem {#successive-derivatives}

**Chain rule.** If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then $f \circ g$ is differentiable at $x$ and $(f \circ g)'(x) = f'(g(x))\,g'(x)$.

**Successive derivatives** $y_1 = y'$, $y_2 = y''$, …, $y_n = \dfrac{d^n y}{dx^n}$. The standard $n$th derivatives are:

| $y$ | $y_n$ |
|:---|:---|
| $e^{ax}$ | $a^n e^{ax}$ |
| $a^x$ ($a > 0$) | $(\ln a)^n a^x$ |
| $(ax + b)^m$ | $m(m - 1)\cdots(m - n + 1)\,a^n(ax + b)^{m - n}$ |
| $\dfrac{1}{ax + b}$ | $\dfrac{(-1)^n n!\,a^n}{(ax + b)^{n + 1}}$ |
| $\ln(ax + b)$ | $\dfrac{(-1)^{n - 1}(n - 1)!\,a^n}{(ax + b)^n}$ |
| $\sin(ax + b)$ | $a^n\sin\!\left(ax + b + \frac{n\pi}{2}\right)$ |
| $\cos(ax + b)$ | $a^n\cos\!\left(ax + b + \frac{n\pi}{2}\right)$ |
| $e^{ax}\sin(bx + c)$ | $r^n e^{ax}\sin(bx + c + n\phi)$, with $r = \sqrt{a^2 + b^2}$, $\cos\phi = \frac ar$, $\sin\phi = \frac br$ |

For a rational function, split it into partial fractions first: $\dfrac{1}{x^2 - 1} = \dfrac12\left(\dfrac{1}{x - 1} - \dfrac{1}{x + 1}\right)$.

**Leibniz's theorem.** If $u$ and $v$ have $n$th derivatives, then

$$(uv)_n = \sum_{k=0}^{n}\binom nk u_{n-k}\,v_k = u_n v + \binom n1 u_{n-1}v_1 + \binom n2 u_{n-2}v_2 + \cdots + u v_n.$$

Put the factor whose derivatives die out (a polynomial) as $v$. For $y = x^2e^x$, only three terms survive:

$$y_n = e^x x^2 + \binom n1 e^x(2x) + \binom n2 e^x(2) = e^x\left(x^2 + 2nx + n(n - 1)\right).$$

**The standard application** differentiates a relation $n$ times. For $y = \sin^{-1}x$: $\sqrt{1 - x^2}\,y_1 = 1$, so $(1 - x^2)y_1^2 = 1$. Differentiating gives $(1 - x^2)y_2 - xy_1 = 0$. Then Leibniz, applied $n$ times, gives

$$(1 - x^2)y_{n+2} - (2n + 1)x\,y_{n+1} - n^2 y_n = 0.$$

At $x = 0$: $y_{n+2}(0) = n^2 y_n(0)$. Since $y_1(0) = 1$ and $y_2(0) = 0$, we get $y_3(0) = 1$, $y_5(0) = 9$, $y_7(0) = 225$, and every even-order derivative vanishes at $0$.

Similar relations:

- $y = e^{m\sin^{-1}x}$: $(1 - x^2)y_{n+2} - (2n + 1)xy_{n+1} - (n^2 + m^2)y_n = 0$.
- $y = \tan^{-1}x$: $(1 + x^2)y_{n+1} + 2nx\,y_n + n(n - 1)y_{n-1} = 0$.

:::exam-tip
Check any $y_n$ formula at $n = 1$. For $x^2e^x$, $y_1 = e^x(x^2 + 2x)$ matches $n(n - 1) = 0$. A version with $n^2$ in place of $n(n - 1)$ fails at once.
:::

## Rolle's theorem {#rolle}

:::keyfacts
- **Rolle's theorem.** Let $f$ be (i) continuous on $[a, b]$, (ii) differentiable on $(a, b)$, with (iii) $f(a) = f(b)$. Then there is at least one $c \in (a, b)$ with $f'(c) = 0$.
- **Geometric meaning:** somewhere strictly between $a$ and $b$ the tangent is horizontal, parallel to the chord joining the end points.
:::

**Proof idea.** $f$ attains its maximum and minimum on $[a, b]$. If both occur at the end points, $f$ is constant and every $c$ works. Otherwise one occurs at an interior point $c$, and there $f'(c) = 0$, because $Rf'(c)$ and $Lf'(c)$ have opposite signs.

**Finding $c$.** Solve $f'(c) = 0$ and keep only the roots inside $(a, b)$.

- $f(x) = x^2 - 4x + 3$ on $[1, 3]$: $f(1) = f(3) = 0$, $f'(c) = 2c - 4 = 0$, so $c = 2$.
- $f(x) = x(x - 1)(x - 2)$ on $[0, 1]$: $f'(x) = 3x^2 - 6x + 2 = 0$ gives $x = 1 \pm \frac{1}{\sqrt3}$. Only $c = 1 - \frac{1}{\sqrt3}$ lies in $(0, 1)$.
- $f(x) = e^x\sin x$ on $[0, \pi]$: $f'(x) = e^x(\sin x + \cos x) = 0$ gives $\tan c = -1$, so $c = \frac{3\pi}{4}$.

**When a hypothesis fails**, the conclusion may fail:

| $f$ on $[a, b]$ | Failing hypothesis | Is there $c$ with $f'(c) = 0$? |
|:---|:---|:---|
| $\lvert x\rvert$ on $[-1, 1]$ | not differentiable at $0$ | no |
| $x^{2/3}$ on $[-1, 1]$ | not differentiable at $0$ | no |
| $f(x) = x$ on $[0, 1)$, $f(1) = 0$ | not continuous at $1$ | no |
| $x$ on $[0, 1]$ | $f(0) \ne f(1)$ | no |
| $\tan x$ on $[0, \pi]$ | not continuous at $\frac{\pi}{2}$ | no |

The hypotheses are **sufficient, not necessary**: $\cos x$ on $[0, 3\pi/2]$ has $f(a) \ne f(b)$, yet $f'(\pi) = 0$.

**Rolle and equations.** Between two consecutive real roots of a polynomial $p$ there is a root of $p'$. So if $p$ has $k$ distinct real roots, $p'$ has at least $k - 1$. Conversely, if $p'$ has no real root, $p$ has at most one. If $f$ is differentiable on $\R$ and $f'$ never vanishes, then $f$ is one-one.

:::caution
Rolle needs **closed** $[a, b]$ for continuity but only **open** $(a, b)$ for differentiability. $\sqrt{1 - x^2}$ on $[-1, 1]$ satisfies Rolle even though it has no derivative at $\pm 1$.
:::

## Lagrange's mean value theorem {#lagrange-mvt}

:::keyfacts
- **Lagrange's MVT.** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then for some $c \in (a, b)$:
  $$\frac{f(b) - f(a)}{b - a} = f'(c).$$
- **$\theta$-form.** With $b = a + h$: $\;f(a + h) = f(a) + h f'(a + \theta h)$ for some $0 < \theta < 1$.
- **Geometric meaning:** at some interior point the tangent is **parallel to the chord** joining the end points.
:::

**Proof idea.** Apply Rolle to $\phi(x) = f(x) - f(a) - \dfrac{f(b) - f(a)}{b - a}(x - a)$, the vertical gap between the curve and the chord. Rolle is the special case $f(a) = f(b)$.

```plot
title: Lagrange's MVT for $y = \sqrt x$ on $[1, 4]$; the tangent at $c = \frac94$ is parallel to the chord
x: 0, 5
y: 0, 2.6
f: sqrt(x) | $y = \sqrt x$
f: x/3 + 2/3 | chord, slope $\frac13$
f: x/3 + 3/4 | tangent at $c = \frac94$
point: 1, 1 | $A$
point: 4, 2 | $B$
point: 9/4, 3/2 | $c$
vline: 9/4
```

**Finding $c$.** For $\sqrt x$ on $[1, 4]$: $\frac{2 - 1}{3} = \frac{1}{2\sqrt c}$, so $c = \frac94$. For $\ln x$ on $[1, e]$: $\frac{1}{e - 1} = \frac1c$, so $c = e - 1$. For any quadratic $px^2 + qx + r$, $c = \frac{a + b}{2}$, the midpoint.

**Finding $\theta$.**

- $f(x) = x^2$: $(a + h)^2 - a^2 = 2ah + h^2 = h\cdot 2(a + \theta h)$ gives $\theta = \frac12$ for every $a$ and $h$.
- $f(x) = x^3$, $a = 0$: $h^3 = h\cdot 3\theta^2h^2$, so $\theta = \frac{1}{\sqrt3}$.
- $f(x) = e^x$, $a = 0$: $e^h - 1 = h e^{\theta h}$, so $\theta = \frac1h\ln\frac{e^h - 1}{h} \to \frac12$ as $h \to 0$.

**General fact.** If $f''$ is continuous at $a$ and $f''(a) \ne 0$, then $\theta \to \frac12$ as $h \to 0$.

**Consequences.**

- If $f'(x) = 0$ on an interval, then $f$ is constant there.
- If $f' = g'$ on an interval, then $f - g$ is constant there.
- If $\lvert f'\rvert \le M$, then $\lvert f(x) - f(y)\rvert \le M\lvert x - y\rvert$. For example, $\lvert\sin x - \sin y\rvert \le \lvert x - y\rvert$.

**Inequalities via the MVT.** Bound $f'(c)$ between its values at the end points:

- $\ln(1 + x) = \dfrac{x}{1 + c}$ with $0 < c < x$, so $\dfrac{x}{1 + x} < \ln(1 + x) < x$ for $x > 0$.
- For $0 < a < b$: $\dfrac{b - a}{1 + b^2} < \tan^{-1}b - \tan^{-1}a < \dfrac{b - a}{1 + a^2}$, and $\dfrac{b - a}{b} < \ln\dfrac ba < \dfrac{b - a}{a}$.

Taylor's theorem, the next topic, extends the $\theta$-form to higher derivatives.

## Cauchy's mean value theorem {#cauchy-mvt}

:::keyfacts
- **Cauchy's MVT.** Let $f$ and $g$ be continuous on $[a, b]$ and differentiable on $(a, b)$, with $g'(x) \ne 0$ for every $x \in (a, b)$. Then for some $c \in (a, b)$:
  $$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}.$$
- Without the condition $g' \ne 0$, the conclusion reads $\big[f(b) - f(a)\big]g'(c) = \big[g(b) - g(a)\big]f'(c)$.
:::

**Why $g' \ne 0$?** It guarantees $g(b) \ne g(a)$: otherwise Rolle would give a zero of $g'$. It also keeps the right side defined.

**Proof idea.** Apply Rolle to $\phi(x) = f(x) - \dfrac{f(b) - f(a)}{g(b) - g(a)}\,g(x)$, which has $\phi(a) = \phi(b)$. Taking $g(x) = x$ gives back Lagrange.

:::caution
You cannot prove Cauchy's MVT by applying Lagrange to $f$ and $g$ separately and dividing. That gives $\frac{f'(c_1)}{g'(c_2)}$ with two possibly **different** points.
:::

**Geometric meaning.** On the parametric curve $x = g(t)$, $y = f(t)$, some tangent is parallel to the chord joining the end points.

**Classic $c$ values** on $[a, b]$ with $0 < a < b$:

| $f,\ g$ | $c$ |
|:---|:---|
| $e^x,\ e^{-x}$ | $\dfrac{a + b}{2}$ (AM) |
| $\sqrt x,\ \dfrac{1}{\sqrt x}$ | $\sqrt{ab}$ (GM) |
| $\dfrac{1}{x^2},\ \dfrac1x$ | $\dfrac{2ab}{a + b}$ (HM) |
| $x^2,\ x^3$ | $\dfrac{2(a^2 + ab + b^2)}{3(a + b)}$ |

**Worked example.** For $e^x$ and $e^{-x}$:

$$\frac{e^b - e^a}{e^{-b} - e^{-a}} = \frac{e^b - e^a}{(e^a - e^b)/e^{a+b}} = -e^{a+b} \quad\text{and}\quad \frac{f'(c)}{g'(c)} = \frac{e^c}{-e^{-c}} = -e^{2c}.$$

Hence $2c = a + b$.

For $x^2$ and $x^3$ on $[1, 2]$: $\frac{3}{7} = \frac{2c}{3c^2} = \frac{2}{3c}$, so $c = \frac{14}{9}$, which lies in $(1, 2)$.

Cauchy's MVT is the key step in the proof of L'Hospital's rule, which belongs to the topic on indeterminate forms.

## Monotonicity and Darboux's theorem {#monotonicity-darboux}

**Sign of the derivative.** Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$.

- If $f'(x) \ge 0$ on $(a, b)$, then $f$ is non-decreasing on $[a, b]$. If $f'(x) > 0$, it is strictly increasing.
- If $f'(x) \le 0$, $f$ is non-increasing; if $f'(x) < 0$, strictly decreasing.
- **Proof:** for $x_1 < x_2$, the MVT gives $f(x_2) - f(x_1) = (x_2 - x_1)f'(c)$, which has the sign of $f'(c)$.
- $f' \ge 0$ with $f' = 0$ only at isolated points still gives strict increase.

Example: $f(x) = x^3 - 3x$ has $f'(x) = 3(x - 1)(x + 1)$. So $f$ is strictly increasing on $(-\infty, -1]$ and on $[1, \infty)$, and strictly decreasing on $[-1, 1]$.

:::caution
- **Strictly increasing does not force $f' > 0$.** $x^3$ is strictly increasing on $\R$, but $f'(0) = 0$.
- **$f'(a) > 0$ at a single point does not make $f$ increasing near $a$.** Take $f(x) = x + 2x^2\sin\frac1x$, $f(0) = 0$. Then $f'(0) = 1$, but $f'(x) = 1 + 4x\sin\frac1x - 2\cos\frac1x$ takes the value $-1$ at every $x = \frac{1}{2k\pi}$, arbitrarily close to $0$. It only gives $f(a - h) < f(a) < f(a + h)$ for small $h > 0$.
:::

:::keyfacts
- **Darboux's theorem.** If $f$ is differentiable on $[a, b]$ (one-sided at the ends) and $k$ lies strictly between $f'(a)$ and $f'(b)$, then $f'(c) = k$ for some $c \in (a, b)$.
- So a derivative has the **intermediate value property**, even when it is not continuous.
:::

**Proof idea.** Say $f'(a) < k < f'(b)$. Let $\phi(x) = f(x) - kx$, so $\phi'(a) < 0 < \phi'(b)$. Then $\phi$ dips below $\phi(a)$ just right of $a$, and below $\phi(b)$ just left of $b$. So its minimum on $[a, b]$ is at an interior point $c$, and there $\phi'(c) = 0$.

**Consequences.**

- A derivative **cannot have a jump** (or removable) discontinuity. Its discontinuities, if any, are of the second kind, like $2x\sin\frac1x - \cos\frac1x$ at $0$.
- So $\operatorname{sgn}x$, $\lfloor x\rfloor$ and the unit step are **not derivatives** of any function on an interval containing their jump.
- If $f'$ never vanishes on an interval, then $f'$ keeps one sign there, so $f$ is strictly monotone.

:::exam-tip
Darboux's theorem does **not** say that $f'$ is continuous. $x^2\sin\frac1x$ has a discontinuous derivative, which still has the intermediate value property.
:::

## Differentials and approximation {#differentials}

Let $y = f(x)$ be differentiable at $x$. For an increment $\Delta x = dx$:

- The **differential** is $dy = f'(x)\,dx$. It is the rise along the tangent.
- The **actual change** is $\Delta y = f(x + dx) - f(x)$.
- Differentiability means $\Delta y = f'(x)\,dx + \varepsilon\,dx$ with $\varepsilon \to 0$ as $dx \to 0$. So $\Delta y \approx dy$ for small $dx$, and the error is small compared with $dx$.

**Linear approximation:**

$$f(a + h) \approx f(a) + h f'(a).$$

This is the MVT with $\theta$ replaced by $0$.

- $\sqrt{26} \approx \sqrt{25} + \dfrac{1}{2\sqrt{25}} = 5 + \dfrac{1}{10} = 5.1$. (True value $5.0990\ldots$.)
- $\sqrt[3]{26} \approx 3 - \dfrac{1}{3\cdot 27^{2/3}} = 3 - \dfrac{1}{27} \approx 2.963$.
- $\sin 31^\circ \approx \sin 30^\circ + \cos 30^\circ\cdot\dfrac{\pi}{180} \approx 0.5 + 0.866 \times 0.01745 \approx 0.5151$.

**Errors.** Let $\delta x$ be the error in $x$.

- The **absolute error** in $y$ is $\delta y \approx f'(x)\,\delta x$.
- The **relative error** is $\dfrac{\delta y}{y}$, and the **percentage error** is $100\,\dfrac{\delta y}{y}$.
- For $y = kx^n$: $\dfrac{\delta y}{y} \approx n\,\dfrac{\delta x}{x}$. So the percentage error is multiplied by the power.

| Quantity | Formula | Error from a 1% error in $r$ (or side $x$) |
|:---|:---|:---|
| Area of a circle | $\pi r^2$ | 2% |
| Volume of a sphere | $\frac43\pi r^3$ | 3% |
| Surface of a sphere | $4\pi r^2$ | 2% |
| Volume of a cube | $x^3$ | 3% |

For a product or quotient, take logarithms first. If $y = \dfrac{uv}{w}$, then $\dfrac{\delta y}{y} \approx \dfrac{\delta u}{u} + \dfrac{\delta v}{v} - \dfrac{\delta w}{w}$.

:::caution
The approximation uses $f'$ at the **known** point $a$, not at $a + h$. For $\sqrt{26}$ use $f'(25) = \frac{1}{10}$, not $f'(26)$. The answer $5.01$ comes from moving the decimal point wrongly in $\frac{1}{10}$.
:::

:::exam-tip
Angles must be in **radians**: $1^\circ = \frac{\pi}{180} \approx 0.01745$.
:::

## Quick checks and traps {#exam-tips}

- **Hypotheses of Rolle and Lagrange:** continuous on the **closed** interval, differentiable on the **open** one. Cauchy also needs $g' \ne 0$ on $(a, b)$.
- **Which hypothesis fails?** Look for a corner ($\lvert x\rvert$, $\lvert x - 1\rvert$), a cusp ($x^{2/3}$), a vertical tangent ($x^{1/3}$), a jump, or an asymptote inside the interval ($\tan x$, $\frac1x$).
- **$c$ for a quadratic** in Lagrange's MVT is always the midpoint. **$\theta$ for $x^2$** is always $\frac12$.
- **Cauchy $c$ values:** $e^{\pm x}$ give the AM, $\sqrt x$ and $\frac{1}{\sqrt x}$ the GM, $\frac{1}{x^2}$ and $\frac1x$ the HM.
- **Check $c$** by confirming that it lies strictly inside $(a, b)$. Discard roots outside.
- **$n$th derivatives:** check at $n = 1$ or $n = 0$. Remember the factor $a^n$ from the chain rule, and $(n - 1)!$ (not $n!$) for $\ln$.
- **Leibniz at $x = 0$:** for $\sin^{-1}x$, $y_{n+2}(0) = n^2y_n(0)$; for $\tan^{-1}x$, $y_{n+1}(0) = -n(n - 1)y_{n-1}(0)$.
- **Darboux:** a function with a jump is never a derivative on an interval containing the jump.
- **Inequalities:** pick $f$ so that the middle quantity is $f(b) - f(a)$, then bound $f'(c)$ using monotonicity of $f'$.
- **Percentage error** of $kx^n$ is $n$ times that of $x$.
