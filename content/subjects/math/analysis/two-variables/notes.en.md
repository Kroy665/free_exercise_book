# Functions of Two Variables

## Limits and continuity in the plane {#limits-continuity}

Let $f$ be defined in a deleted neighbourhood of $(a, b)$. The **simultaneous (double) limit**

$$\lim_{(x,y)\to(a,b)} f(x, y) = L$$

means: for every $\varepsilon > 0$ there is $\delta > 0$ such that $|f(x,y) - L| < \varepsilon$ whenever $0 < \sqrt{(x-a)^2 + (y-b)^2} < \delta$. The point may approach $(a,b)$ along **any** path, and the limit must be the same along all of them.

$f$ is **continuous** at $(a, b)$ if $\lim_{(x,y)\to(a,b)} f(x,y) = f(a,b)$. Sums, products, quotients (non-zero denominator) and compositions of continuous functions are continuous, so polynomials and rational functions are continuous wherever they are defined.

**Path test for non-existence.** If two paths give different limits, the double limit does not exist. Classic example, with $f(0,0) = 0$:

$$f(x,y) = \frac{xy}{x^2 + y^2}: \qquad \text{along } y = mx,\quad f = \frac{m}{1 + m^2}.$$

The value depends on $m$ (it is $0$ on the axes and $\tfrac12$ on $y = x$), so the limit does not exist and $f$ is discontinuous at the origin.

```plot
title: Limit of $\frac{xy}{x^2+y^2}$ along $y = mx$, as a function of the slope $m$
x: -5, 5
y: -0.7, 0.7
f: x/(1 + x^2) | $\frac{m}{1+m^2}$
point: 1, 0.5 | $y = x$
point: 0, 0 | axes
xlabel: m
ylabel: limit
```

**Straight lines are not enough.** For $f = \dfrac{x^2 y}{x^4 + y^2}$, every line $y = mx$ gives the limit $0$, but the parabola $y = x^2$ gives $\tfrac12$. No limit.

**Proving a limit exists.** Use polar coordinates or an inequality. For $\dfrac{x^2y^2}{x^2+y^2}$: with $x = r\cos\theta$, $y = r\sin\theta$, $|f| = r^2\cos^2\theta\sin^2\theta \le r^2 \to 0$, uniformly in $\theta$. So the limit is $0$.

**Repeated (iterated) limits** take one variable at a time:

$$\lim_{x\to a}\lim_{y\to b} f(x,y) \quad\text{and}\quad \lim_{y\to b}\lim_{x\to a} f(x,y).$$

- They may differ: for $\dfrac{x - y}{x + y}$ at $(0,0)$, the first is $\lim_{x\to0} \frac{x}{x} = 1$ and the second is $\lim_{y\to0} \frac{-y}{y} = -1$. Then the double limit cannot exist.
- They may agree while the double limit fails: for $\frac{xy}{x^2+y^2}$ both are $0$.
- The double limit may exist while a repeated limit fails: $x\sin\frac1y + y\sin\frac1x \to 0$, but $\lim_{y\to0}$ of $x\sin\frac1y$ does not exist for fixed $x \ne 0$.

:::keyfacts
- If the double limit is $L$ and, for each $x$ near $a$, $\lim_{y\to b} f(x,y)$ exists, then $\lim_{x\to a}\lim_{y\to b} f = L$.
- So if the double limit and both repeated limits exist, all three are equal. Unequal repeated limits prove the double limit does not exist.
:::

## Partial derivatives {#partial-derivatives}

The **partial derivatives** of $f$ at $(a, b)$ are the ordinary derivatives of the one-variable sections:

$$f_x(a,b) = \lim_{h\to0}\frac{f(a+h, b) - f(a,b)}{h}, \qquad f_y(a,b) = \lim_{k\to0}\frac{f(a, b+k) - f(a,b)}{k}.$$

In practice, differentiate with respect to one variable and hold the other constant. For $f = x^2 y + x\sin y$: $f_x = 2xy + \sin y$ and $f_y = x^2 + x\cos y$.

At an exceptional point (where the formula breaks down) use the **definition**. For the function $f = \frac{xy}{x^2+y^2}$, $f(0,0) = 0$:

$$f(h, 0) = 0 \text{ for all } h \;\Rightarrow\; f_x(0,0) = 0, \qquad f(0,k) = 0 \;\Rightarrow\; f_y(0,0) = 0.$$

Both partial derivatives exist, yet $f$ is **not continuous** at the origin (see the path test). A partial derivative sees only the two axis directions, so it says nothing about other paths.

:::caution
In one variable, differentiable implies continuous. In two variables, **existence of $f_x$ and $f_y$ does not imply continuity**. The correct two-variable analogue of "differentiable" is the stronger notion in the next section.
:::

Conversely, a continuous function need not have partial derivatives: $f = |x| + |y|$ is continuous at the origin, but $f(h,0)/h = |h|/h$ has no limit, so $f_x(0,0)$ does not exist.

**Geometric meaning.** $f_x(a,b)$ is the slope of the curve cut from the surface $z = f(x,y)$ by the plane $y = b$, measured in the $x$-direction.

**Standard identities** to recognise quickly:

| Function | Identity |
|:---|:---|
| $u = \log(x^2 + y^2)$ | $u_{xx} + u_{yy} = 0$ (away from the origin) |
| $u = f(r)$, $r = \sqrt{x^2+y^2}$ | $u_{xx} + u_{yy} = f''(r) + \dfrac{f'(r)}{r}$ |
| $u = f(x + ct) + g(x - ct)$ | $u_{tt} = c^2 u_{xx}$ |
| $u = f(x - y,\, y - z,\, z - x)$ | $u_x + u_y + u_z = 0$ |

For $u = f(r)$: $r_x = x/r$, so $u_x = f'(r)\,x/r$ and $u_{xx} = f''\frac{x^2}{r^2} + f'\frac{r^2 - x^2}{r^3}$. Adding the $y$ version gives $f'' + f'/r$. In three variables the term becomes $2f'/r$; do not mix the two.

## Differentiability and the total differential {#differentiability}

$f$ is **differentiable** at $(a, b)$ if there are constants $A$, $B$ such that

$$f(a+h, b+k) - f(a,b) = Ah + Bk + \varepsilon\sqrt{h^2+k^2}, \qquad \varepsilon \to 0 \text{ as } (h,k)\to(0,0).$$

Equivalently, $\dfrac{f(a+h,b+k) - f(a,b) - Ah - Bk}{\sqrt{h^2+k^2}} \to 0$. If this holds, then necessarily $A = f_x(a,b)$ and $B = f_y(a,b)$. The linear part

$$df = f_x\,dx + f_y\,dy$$

is the **total differential**.

**Hierarchy of conditions** at a point:

| Condition | Implies |
|:---|:---|
| $f_x$, $f_y$ exist near $(a,b)$ and are continuous at $(a,b)$ | $f$ differentiable at $(a,b)$ |
| $f$ differentiable at $(a,b)$ | $f$ continuous, and $f_x$, $f_y$ exist, at $(a,b)$ |
| $f_x$, $f_y$ exist at $(a,b)$ | nothing about continuity |

A sharper sufficient condition: one partial derivative exists at $(a,b)$ and the other is continuous at $(a,b)$ (existing near it). None of the arrows reverses.

**Example (continuous, partials exist, not differentiable).** $f = \sqrt{|xy|}$ at the origin. It is continuous since $\sqrt{|xy|} \le \frac{|x| + |y|}{2}$. On the axes $f = 0$, so $f_x(0,0) = f_y(0,0) = 0$. Differentiability would need $\dfrac{\sqrt{|hk|}}{\sqrt{h^2+k^2}} \to 0$, but along $h = k$ this ratio is $\frac{1}{\sqrt2}$. So $f$ is **not** differentiable.

**Approximation and errors.** For small $dx$, $dy$: $\Delta f \approx f_x\,dx + f_y\,dy$. For $z = x^2y$ at $(2, 3)$ with $dx = 0.01$, $dy = -0.02$:

$$dz = 2xy\,dx + x^2\,dy = 12(0.01) + 4(-0.02) = 0.04.$$

For a product or power, use logarithmic differentiation for **percentage error**: if $V = \pi r^2 h$, then $\dfrac{dV}{V} = 2\dfrac{dr}{r} + \dfrac{dh}{h}$.

:::exam-tip
To test differentiability at the origin when $f(0,0) = 0$ and $f_x = f_y = 0$ there, just check whether $\dfrac{f(h,k)}{\sqrt{h^2+k^2}} \to 0$. One path with a non-zero limit settles "not differentiable".
:::

## Chain rule and implicit functions {#chain-rule}

**Chain rule.** Let $z = f(x, y)$ be **differentiable**, and $x = \phi(t)$, $y = \psi(t)$ be differentiable. Then

$$\frac{dz}{dt} = f_x\frac{dx}{dt} + f_y\frac{dy}{dt}.$$

If $x = x(u,v)$ and $y = y(u,v)$ have partial derivatives, then

$$z_u = f_x\,x_u + f_y\,y_u, \qquad z_v = f_x\,x_v + f_y\,y_v.$$

Example: $z = xy$, $x = e^t$, $y = \cos t$ gives $\dfrac{dz}{dt} = y e^t + x(-\sin t) = e^t(\cos t - \sin t)$.

**Polar coordinates.** With $x = r\cos\theta$, $y = r\sin\theta$: $z_r = z_x\cos\theta + z_y\sin\theta$ and $z_\theta = -z_x r\sin\theta + z_y r\cos\theta$. Squaring and adding:

$$z_x^2 + z_y^2 = z_r^2 + \frac{1}{r^2}z_\theta^2.$$

**Implicit functions.** Suppose $F(x, y) = 0$ defines $y$ as a differentiable function of $x$ near a point where $F_y \ne 0$ ($F$ with continuous partial derivatives; the implicit function theorem guarantees such a $y$ exists). Differentiating $F(x, y(x)) = 0$ by the chain rule gives $F_x + F_y\,y' = 0$, so

$$\frac{dy}{dx} = -\frac{F_x}{F_y}.$$

Example: $x^3 + y^3 - 3axy = 0$ has $F_x = 3x^2 - 3ay$ and $F_y = 3y^2 - 3ax$, so

$$\frac{dy}{dx} = -\frac{x^2 - ay}{y^2 - ax} = \frac{ay - x^2}{y^2 - ax}.$$

**Second derivative.** Differentiating again (with continuous second partials):

$$\frac{d^2y}{dx^2} = -\frac{F_{xx}F_y^2 - 2F_{xy}F_xF_y + F_{yy}F_x^2}{F_y^3}.$$

For $x^2 + y^2 = a^2$: $y' = -x/y$ and $y'' = -\dfrac{y - xy'}{y^2} = -\dfrac{x^2+y^2}{y^3} = -\dfrac{a^2}{y^3}$.

:::caution
The minus sign in $-F_x/F_y$ is the most common slip. Check on the circle: $F = x^2 + y^2 - 1$ must give $y' = -x/y$, which is negative in the first quadrant.
:::

:::exam-tip
For $u = f(x - y, y - z, z - x)$, write $p = x - y$, $q = y - z$, $w = z - x$. Then $u_x = f_p - f_w$, $u_y = -f_p + f_q$, $u_z = -f_q + f_w$, and the sum is $0$.
:::

## Higher derivatives: Schwarz's and Young's theorems {#higher-derivatives}

Second-order partial derivatives are $f_{xx}$, $f_{yy}$ and the two **mixed** derivatives. In these notes

$$f_{xy} = (f_x)_y = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right), \qquad f_{yx} = (f_y)_x = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).$$

Some textbooks use the opposite order of subscripts, so the questions write the derivative out in full.

For polynomials and all "nice" functions the mixed derivatives are equal, but not always.

:::keyfacts
- **Schwarz's theorem.** If $f_x$, $f_y$ and $f_{xy}$ exist in a neighbourhood of $(a,b)$ and $f_{xy}$ is continuous at $(a,b)$, then $f_{yx}(a,b)$ exists and $f_{yx}(a,b) = f_{xy}(a,b)$.
- **Young's theorem.** If $f_x$ and $f_y$ are both **differentiable** at $(a,b)$, then $f_{xy}(a,b) = f_{yx}(a,b)$.
- Neither condition is necessary; each is only sufficient. Existence of both mixed partials alone does **not** make them equal.
:::

**The classic counterexample.**

$$f(x,y) = \frac{xy(x^2 - y^2)}{x^2 + y^2}, \qquad f(0,0) = 0.$$

From the definition, for fixed $y$:

$$f_x(0, y) = \lim_{h\to0}\frac{f(h,y) - f(0,y)}{h} = \lim_{h\to0}\frac{y(h^2 - y^2)}{h^2 + y^2} = -y.$$

Similarly $f_y(x, 0) = \lim_{k\to0}\dfrac{x(x^2 - k^2)}{x^2+k^2} = x$. Therefore

$$\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)(0,0) = \frac{d}{dy}(-y) = -1, \qquad \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)(0,0) = \frac{d}{dx}(x) = 1.$$

The mixed derivatives exist but differ. This $f$ is continuous and even differentiable at the origin (it is $O(r^2)$). The hypothesis of Schwarz fails because the mixed derivative is not continuous at $(0,0)$.

:::caution
Do not compute $f_x$ by the quotient rule and then put $x = y = 0$: the formula is $0/0$ there. At the exceptional point, always go back to the limit definition, one variable at a time.
:::

**Harmonic functions.** $u$ is harmonic if $u_{xx} + u_{yy} = 0$. Examples: $\log(x^2+y^2)$, $\tan^{-1}(y/x)$, $e^x\cos y$, $x^2 - y^2$, $x^3 - 3xy^2$.

## Homogeneous functions and Euler's theorem {#euler-theorem}

$f(x, y)$ is **homogeneous of degree $n$** if $f(tx, ty) = t^n f(x,y)$ for all $t > 0$ (and all $(x,y)$ in the domain). Equivalently $f = x^n\phi(y/x)$. The degree $n$ may be any real number.

| Function | Degree |
|:---|:---|
| $x^3 - 3xy^2$ | $3$ |
| $\dfrac{x^2+y^2}{x+y}$ | $1$ |
| $\dfrac{x}{y} + \dfrac{y}{x}$, $\;\sin^{-1}\dfrac{x}{y}$ | $0$ |
| $\dfrac{\sqrt x + \sqrt y}{x + y}$ | $-\tfrac12$ |
| $\dfrac{x^{1/3} + y^{1/3}}{x^{1/2} + y^{1/2}}$ | $\tfrac13 - \tfrac12 = -\tfrac16$ |

:::keyfacts
- **Euler's theorem.** If $f$ is homogeneous of degree $n$ and differentiable, then $x f_x + y f_y = n f$.
- **Second order.** If moreover $f$ has continuous second partial derivatives, then $x^2 f_{xx} + 2xy\,f_{xy} + y^2 f_{yy} = n(n-1) f$.
- The converse of the first-order form also holds: a differentiable $f$ with $xf_x + yf_y = nf$ (on a domain that is a cone) is homogeneous of degree $n$.
:::

**Proof idea.** Differentiate $f(tx, ty) = t^n f(x,y)$ with respect to $t$ and put $t = 1$. Differentiating the first-order identity once more by $x$ and by $y$, multiplying by $x$ and $y$ and adding, gives the second-order form.

**Composite form.** Often $u$ itself is not homogeneous but $F(u) = z$ is, of degree $n$. Then

$$x u_x + y u_y = \frac{n F(u)}{F'(u)} =: g(u), \qquad x^2u_{xx} + 2xy\,u_{xy} + y^2u_{yy} = g(u)\,\big(g'(u) - 1\big).$$

Examples:

- $u = \sin^{-1}\dfrac{x^2+y^2}{x+y}$: $\sin u$ has degree $1$, so $g = \dfrac{\sin u}{\cos u} = \tan u$, and the second-order expression is $\tan u(\sec^2u - 1) = \tan^3 u$.
- $u = \tan^{-1}\dfrac{x^3+y^3}{x-y}$: $\tan u$ has degree $2$, so $x u_x + y u_y = \dfrac{2\tan u}{\sec^2 u} = \sin 2u$.
- $u = \log\dfrac{x^4 + y^4}{x + y}$: $e^u$ has degree $3$, so $x u_x + y u_y = 3$.

:::caution
Find the degree of the **homogeneous** piece, not of $u$. And a sum like $x^2 + y$ is not homogeneous at all; Euler's theorem does not apply to it.
:::

## Maxima, minima and saddle points {#extrema}

$f$ has a **local maximum** at $(a,b)$ if $f(a+h, b+k) \le f(a,b)$ for all small $(h,k)$, and a **local minimum** if $\ge$. Extreme values are local maxima and minima.

**Necessary condition.** If $f$ has a local extremum at $(a,b)$ and $f_x$, $f_y$ exist there, then $f_x(a,b) = f_y(a,b) = 0$. Such points are **stationary points**. A stationary point that is not an extremum is a **saddle point**: $f - f(a,b)$ takes both signs arbitrarily close to it, as for $x^2 - y^2$ at the origin.

**Second-derivative test** (Lagrange's conditions). Let $f$ have continuous second partial derivatives near a stationary point $(a,b)$, and write

$$r = f_{xx}(a,b), \qquad s = f_{xy}(a,b), \qquad t = f_{yy}(a,b).$$

| Condition | Conclusion |
|:---|:---|
| $rt - s^2 > 0$, $r > 0$ | local minimum |
| $rt - s^2 > 0$, $r < 0$ | local maximum |
| $rt - s^2 < 0$ | saddle point (no extremum) |
| $rt - s^2 = 0$ | test fails; examine further |

When $rt - s^2 > 0$, $r$ and $t$ have the same sign, so either may be used.

**Worked example.** $f = x^3 + y^3 - 3xy$. Then $f_x = 3x^2 - 3y$ and $f_y = 3y^2 - 3x$. Setting both to $0$: $y = x^2$, $x = y^2$, so $x^4 = x$, giving $(0,0)$ and $(1,1)$. With $r = 6x$, $s = -3$, $t = 6y$:

- At $(0,0)$: $rt - s^2 = -9 < 0$, a saddle.
- At $(1,1)$: $rt - s^2 = 36 - 9 = 27 > 0$ and $r = 6 > 0$, a local minimum, with value $-1$.

**Doubtful case.** For $x^4 + y^4$ and for $x^4 - y^4$ at the origin, $r = s = t = 0$. The first has a minimum and the second a saddle. Decide by looking at $f$ itself, for example along lines or by sign.

```plot
title: Level curves of $x^2 - y^2$ near the saddle point at the origin
x: -3, 3
y: -3, 3
equal: true
implicit: x^2 - y^2 = 1 | $f = 1$
implicit: x^2 - y^2 = -1 | $f = -1$
f: x | $f = 0$
f: -x
point: 0, 0 | saddle
```

**Lagrange multipliers (brief).** To find extrema of $f(x,y)$ subject to $\phi(x,y) = 0$, form $L = f + \lambda\phi$ and solve

$$f_x + \lambda\phi_x = 0, \qquad f_y + \lambda\phi_y = 0, \qquad \phi = 0.$$

Geometrically, at a constrained extremum the level curve of $f$ touches the constraint curve ($\nabla f \parallel \nabla\phi$, with $\nabla\phi \ne 0$). Example: maximise $xy$ on $x^2 + 4y^2 = 8$. The equations $y = -2\lambda x$, $x = -8\lambda y$ give $x^2 = 4y^2$, so $x^2 = 4$, $y^2 = 1$, and the maximum is $xy = 2$ (also clear from AM–GM: $x^2 + 4y^2 \ge 4|xy|$).

:::exam-tip
Before using $rt - s^2$, find **all** stationary points; options often list a saddle as if it were an extremum. For "least value" questions on a closed constraint, the Lagrange points plus a quick AM–GM check are usually fastest.
:::

## Quick checks and traps {#exam-tips}

- **Path test:** substitute $y = mx$; if the answer depends on $m$, the limit does not exist. If every line gives the same value, also try $y = mx^2$ (or the curve that balances the degrees).
- **Polar test for existence:** if $|f(r\cos\theta, r\sin\theta) - L| \le g(r) \to 0$ with $g$ independent of $\theta$, the limit is $L$.
- **Unequal repeated limits** prove that the double limit does not exist; equal repeated limits prove nothing.
- **Implications:** continuous partials $\Rightarrow$ differentiable $\Rightarrow$ continuous and partials exist. Partials existing gives nothing more.
- **Exceptional points** (defined separately at the origin): compute partials and mixed partials from the **definition**.
- **Mixed partials:** for $\frac{xy(x^2-y^2)}{x^2+y^2}$, $\frac{\partial}{\partial y}\frac{\partial f}{\partial x} = -1$ and $\frac{\partial}{\partial x}\frac{\partial f}{\partial y} = +1$ at the origin. Remember $f_x(0,y) = -y$ and $f_y(x,0) = x$.
- **Euler:** degree of $\frac{\text{degree } p}{\text{degree } q}$ is $p - q$; for $u = F^{-1}(\text{homogeneous})$, $xu_x + yu_y = nF(u)/F'(u)$.
- **$rt - s^2$:** negative means saddle whatever the sign of $r$; zero means the test fails, not "saddle".
- **$dy/dx = -F_x/F_y$:** keep the minus sign and require $F_y \ne 0$.
