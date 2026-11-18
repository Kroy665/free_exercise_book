# Tangents, Normals, Asymptotes and Curvature

## Tangents and normals {#tangents-normals}

Let $P(x_1, y_1)$ be a point of the curve, and write $y_1' = \frac{dy}{dx}$ at $P$.

| Curve | Tangent at $P$ | Normal at $P$ |
|:---|:---|:---|
| $y = f(x)$ | $y - y_1 = f'(x_1)(x - x_1)$ | $(y - y_1)f'(x_1) + (x - x_1) = 0$ |
| $F(x, y) = 0$ | $(x - x_1)F_x + (y - y_1)F_y = 0$ | $\dfrac{x - x_1}{F_x} = \dfrac{y - y_1}{F_y}$ |
| $x = x(t),\ y = y(t)$ | $(x - x_1)\,\dot y - (y - y_1)\,\dot x = 0$ | $(x - x_1)\,\dot x + (y - y_1)\,\dot y = 0$ |

(In the implicit row, $F_x, F_y$ are evaluated at $P$ and not both zero.) A vertical tangent occurs where $\frac{dx}{dy} = 0$, that is $F_y = 0 \ne F_x$ or $\dot x = 0 \ne \dot y$.

**Lengths** at $P$ (with $\psi$ the angle the tangent makes with the $x$-axis, $\tan\psi = y_1'$):

- subtangent $= \left\lvert \dfrac{y}{y_1'}\right\rvert$, subnormal $= \lvert y\,y_1'\rvert$;
- tangent length $= \left\lvert \dfrac{y\sqrt{1 + y_1'^2}}{y_1'}\right\rvert$, normal length $= \left\lvert y\sqrt{1 + y_1'^2}\right\rvert$.

For the parabola $y^2 = 4ax$: $2yy' = 4a$, so the **subnormal is $2a$**, the same at every point, and the subtangent is $2x$ (twice the abscissa).

**Example (astroid).** On $x = a\cos^3 t$, $y = a\sin^3 t$: $\dot x = -3a\cos^2 t\sin t$, $\dot y = 3a\sin^2 t\cos t$, so the slope is $-\tan t$. The tangent is

$$\frac{x}{a\cos t} + \frac{y}{a\sin t} = 1.$$

Its intercepts are $a\cos t$ and $a\sin t$, so the part between the axes has length $a$ at every point.

**Angle between two curves** at a common point = the angle between their tangents there. The curves cut **orthogonally** when $m_1 m_2 = -1$.

:::exam-tip
For $y^n = k x^m$, take logs: $\frac{y'}{y} = \frac{m}{nx}$. The subtangent is then $\frac{n}{m}x$, a constant multiple of $x$. This one-liner covers the parabola ($n = 2, m = 1$: subtangent $2x$).
:::

## Polar curves and pedal equations {#polar-pedal}

For $r = f(\theta)$, let $\phi$ be the angle from the radius vector $OP$ to the tangent at $P$. (Some books call this angle $\psi$; here $\psi$ is the angle of the tangent with the initial line.) Then

$$\tan\phi = r\,\frac{d\theta}{dr}, \qquad \psi = \theta + \phi.$$

| Quantity | Formula |
|:---|:---|
| perpendicular from the pole to the tangent | $p = r\sin\phi$ |
| $p$ in terms of $r, \theta$ | $\dfrac{1}{p^2} = \dfrac{1}{r^2} + \dfrac{1}{r^4}\Big(\dfrac{dr}{d\theta}\Big)^2 = u^2 + \Big(\dfrac{du}{d\theta}\Big)^2,\ u = \dfrac1r$ |
| polar subtangent / subnormal | $r^2\dfrac{d\theta}{dr}$ and $\dfrac{dr}{d\theta}$ |
| angle between two polar curves | $\lvert\phi_1 - \phi_2\rvert$ |

**Standard angles.**
- Cardioid $r = a(1 - \cos\theta)$: $\tan\phi = \frac{1 - \cos\theta}{\sin\theta} = \tan\frac\theta2$, so $\phi = \frac\theta2$.
- Cardioid $r = a(1 + \cos\theta)$: $\tan\phi = -\cot\frac\theta2$, so $\phi = \frac\pi2 + \frac\theta2$.
- Equiangular spiral $r = ae^{\theta\cot\alpha}$: $\tan\phi = \tan\alpha$, so $\phi = \alpha$, a constant. This is the defining property.
- The cardioids $r = a(1 + \cos\theta)$ and $r = b(1 - \cos\theta)$ cut orthogonally: $\phi_1 - \phi_2 = \frac\pi2$.

**Pedal ($p$–$r$) equation.** Eliminate $\theta$ between $r = f(\theta)$ and the formula for $\frac{1}{p^2}$. For a Cartesian curve, the tangent at $(x, y)$ gives $p$, and $r^2 = x^2 + y^2$.

| Curve (pole) | Pedal equation |
|:---|:---|
| parabola $y^2 = 4ax$ (focus) | $p^2 = ar$ |
| ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (centre) | $\dfrac{a^2b^2}{p^2} = a^2 + b^2 - r^2$ |
| circle $r = 2a\cos\theta$ | $2ap = r^2$ |
| cardioid $r = a(1 + \cos\theta)$ | $p^2 = \dfrac{r^3}{2a}$ |
| lemniscate $r^2 = a^2\cos2\theta$ | $pa^2 = r^3$ |
| equiangular spiral | $p = r\sin\alpha$ |

The circle, cardioid and lemniscate rows are cases of one rule: for $r^n = a^n\cos n\theta$, $\tan\phi = -\cot n\theta$, so $\phi = \frac\pi2 + n\theta$ and $p = r\cos n\theta$. Hence

$$p\,a^n = r^{n+1}.$$

($n = 2$: lemniscate; $n = \frac12$: cardioid with $a$ replaced by $2a$; $n = -1$: the line $p = a$.)

**Worked example (cardioid).** $u = \frac{1}{a(1 + \cos\theta)}$, $\frac{du}{d\theta} = \frac{\sin\theta}{a(1 + \cos\theta)^2}$. Then

$$\frac{1}{p^2} = \frac{(1 + \cos\theta)^2 + \sin^2\theta}{a^2(1 + \cos\theta)^4} = \frac{2}{a^2(1 + \cos\theta)^3} = \frac{2a}{r^3}.$$

:::caution
A pedal equation depends on the **pole**. "$p^2 = ar$" for the parabola is about the focus; from the vertex the equation is different.
:::

## Asymptotes {#asymptotes}

A straight line is an **asymptote** of an infinite branch if the distance from a point $P$ of the branch to the line tends to $0$ as $P$ recedes to infinity along the branch.

**Non-vertical asymptote $y = mx + c$** of $y = f(x)$: $m = \lim \frac{y}{x}$, $c = \lim (y - mx)$ as $x \to \pm\infty$. The same limits, taken as $t \to t_1$ where $x(t) \to \pm\infty$, handle a **parametric** curve. A vertical asymptote $x = a$ needs $y \to \pm\infty$ as $x \to a$.

**Algebraic curves.** Write $F(x, y) = \phi_n(x, y) + \phi_{n-1}(x, y) + \cdots$, grouped by degree, and $\phi_k(m) = \phi_k(1, m)$.

- **Parallel to the axes.** Asymptotes parallel to the $x$-axis: equate to zero the coefficient of the **highest power of $x$** (if it is not a constant). Parallel to the $y$-axis: the coefficient of the highest power of $y$.
- **Oblique.** The slopes are the real roots of $\phi_n(m) = 0$. For each simple root,
  $$c = -\frac{\phi_{n-1}(m)}{\phi_n'(m)}.$$
- **Parallel asymptotes.** If $\phi_n'(m) = \phi_{n-1}(m) = 0$ (a double root), $c$ comes from
  $$\frac{c^2}{2}\,\phi_n''(m) + c\,\phi_{n-1}'(m) + \phi_{n-2}(m) = 0,$$
  giving two parallel asymptotes. If $\phi_n'(m) = 0 \ne \phi_{n-1}(m)$, there is no asymptote with slope $m$.

**Number.** A curve of degree $n$ has **at most $n$** asymptotes (real or imaginary, counted from both families).

**Examples.**
- $xy - y - 2x - 3 = 0$, i.e. $y = \frac{2x + 3}{x - 1}$: highest power of $x$ has coefficient $y - 2$, of $y$ has $x - 1$. Asymptotes $y = 2$, $x = 1$.
- Folium $x^3 + y^3 = 3axy$: $\phi_3(m) = 1 + m^3$ gives $m = -1$; $\phi_2(m) = -3am$, so $c = -\frac{3a}{3} = -a$. Asymptote $x + y + a = 0$.
- $x^3 - 6x^2y + 11xy^2 - 6y^3 + x + y + 1 = 0$: $\phi_3(m) = -(m - 1)(2m - 1)(3m - 1)$ and $\phi_2 = 0$, so the asymptotes are $y = x$, $2y = x$, $3y = x$.
- $(x - y)^2(x + y) - 8x = 0$: $m = 1$ is a double root with $\phi_2 = 0$, $\phi_3''(1) = 4$, $\phi_1(1) = -8$. So $2c^2 - 8 = 0$ gives $y = x \pm 2$; with $m = -1$, $c = 0$: $y = -x$.
- $x^2y^2 - a^2(x^2 + y^2) = 0$: $x^2(y^2 - a^2)$ and $y^2(x^2 - a^2)$ give $y = \pm a$, $x = \pm a$: four, the maximum for degree 4.

**Polar curves.** If $\frac1r = f(\theta)$ and $f(\theta_1) = 0$, then $r\sin(\theta - \theta_1) = \dfrac{1}{f'(\theta_1)}$ is an asymptote. For the hyperbolic spiral $r\theta = a$: $\theta_1 = 0$, giving $r\sin\theta = a$, i.e. $y = a$.

```plot
title: The folium $x^3 + y^3 = 3xy$ and its asymptote $x + y + 1 = 0$
x: -3, 3
y: -3, 3
equal: true
implicit: x^3 + y^3 = 3xy | $x^3 + y^3 = 3xy$
f: -x - 1 | $x + y + 1 = 0$
```

:::caution
A parabola has **no** asymptote. For $y^2 = 4ax$, $\frac{y}{x} \to 0$ but $y - 0\cdot x \to \infty$. Also, the coefficient of the highest power of $x$ in $y^2 - 4ax$ is the constant $-4a$, so there is no asymptote parallel to the $x$-axis.
:::

## Curvature and radius of curvature {#curvature}

**Curvature** at $P$ is $\kappa = \left\lvert\dfrac{d\psi}{ds}\right\rvert$: the rate of turning of the tangent per unit arc. The **radius of curvature** is $\rho = \dfrac{1}{\kappa} = \left\lvert\dfrac{ds}{d\psi}\right\rvert$. A line has $\kappa = 0$; a circle of radius $a$ has $\rho = a$ everywhere.

| Form | $\rho$ |
|:---|:---|
| $y = f(x)$ | $\dfrac{(1 + y_1^2)^{3/2}}{\lvert y_2\rvert}$ |
| $x = x(t),\ y = y(t)$ | $\dfrac{(\dot x^2 + \dot y^2)^{3/2}}{\lvert\dot x\ddot y - \dot y\ddot x\rvert}$ |
| $r = f(\theta)$ | $\dfrac{(r^2 + r_1^2)^{3/2}}{\lvert r^2 + 2r_1^2 - r r_2\rvert}$ |
| pedal $p = f(r)$ | $r\,\dfrac{dr}{dp}$ |
| $F(x, y) = 0$ | $\dfrac{(F_x^2 + F_y^2)^{3/2}}{\lvert F_{xx}F_y^2 - 2F_{xy}F_xF_y + F_{yy}F_x^2\rvert}$ |

Here $y_1 = \frac{dy}{dx}$, $y_2 = \frac{d^2y}{dx^2}$, $r_1 = \frac{dr}{d\theta}$, $r_2 = \frac{d^2r}{d\theta^2}$. If $y_2 = 0$ (a point of inflexion, as at the origin on $y = x^3$), the curvature is $0$ and $\rho$ is infinite.

**Standard values.**

| Curve | $\rho$ |
|:---|:---|
| $y^2 = 4ax$ at the vertex | $2a$ (the semi-latus rectum) |
| $y = x^2$ at the origin | $\frac12$ |
| ellipse at $(a, 0)$ / at $(0, b)$ | $\frac{b^2}{a}$ / $\frac{a^2}{b}$ |
| catenary $y = c\cosh\frac{x}{c}$ | $\frac{y^2}{c}$ |
| astroid $x = a\cos^3t,\ y = a\sin^3t$ | $3a\lvert\sin t\cos t\rvert$ |
| cardioid $r = a(1 + \cos\theta)$ | $\frac{4a}{3}\cos\frac\theta2 = \frac23\sqrt{2ar}$ |

**Cardioid by the pedal form.** From $p^2 = \frac{r^3}{2a}$: $2p\,dp = \frac{3r^2}{2a}dr$, so $\rho = r\frac{dr}{dp} = \frac{4ap}{3r}$. With $\frac{p}{r} = \sin\phi = \cos\frac\theta2$ this is $\frac{4a}{3}\cos\frac\theta2$.

**Catenary.** $y_1 = \sinh\frac xc$ and $y_2 = \frac1c\cosh\frac xc$, so $\rho = \dfrac{\cosh^3(x/c)}{\cosh(x/c)/c} = c\cosh^2\frac xc = \dfrac{y^2}{c}$.

:::exam-tip
$\rho$ does not depend on which variable is independent. If $y_1$ is infinite (vertical tangent), use $\rho = \dfrac{(1 + x_1^2)^{3/2}}{\lvert x_2\rvert}$ with $x$ as a function of $y$.
:::

:::caution
Curvature is $\frac{d\psi}{ds}$, **not** $\frac{ds}{d\psi}$; the latter is $\rho$. In the Cartesian formula the exponent is $\frac32$ on $1 + y_1^2$, not on $y_1$.
:::

## Curvature at the origin, centre and chord of curvature {#centre-of-curvature}

**Newton's formulae** (for a curve through the origin):

- if the curve **touches the $x$-axis** at $O$: $\rho = \lim\limits_{x \to 0}\dfrac{x^2}{2y}$;
- if it **touches the $y$-axis** at $O$: $\rho = \lim\limits_{x \to 0}\dfrac{y^2}{2x}$.

Reason: near $O$, $y \approx \frac12 y_2(0)x^2$ when $y_1(0) = 0$. For a polynomial curve the limit comes from the lowest-degree terms. For a general tangent, substitute $y = px + \frac{q}{2}x^2 + \cdots$, compare coefficients, and use $\rho = \frac{(1 + p^2)^{3/2}}{\lvert q\rvert}$.

**Example.** The folium $x^3 + y^3 = 3axy$ has two branches at $O$. On the branch touching the $x$-axis, $y \approx \frac{x^2}{3a}$, so $\rho = \lim \frac{x^2}{2y} = \frac{3a}{2}$. By symmetry the other branch also has $\rho = \frac{3a}{2}$.

**Centre of curvature** $(\bar x, \bar y)$ at $(x, y)$ on $y = f(x)$:

$$\bar x = x - \frac{y_1(1 + y_1^2)}{y_2}, \qquad \bar y = y + \frac{1 + y_1^2}{y_2}.$$

It lies on the normal, at distance $\rho$, on the concave side. The circle with this centre and radius $\rho$ is the **circle of curvature** (osculating circle). The locus of the centre is the **evolute**; it is also the envelope of the normals.

**Example.** $y = x^2$ at $(1, 1)$: $y_1 = 2$, $y_2 = 2$, so $\bar x = 1 - \frac{2\cdot5}{2} = -4$, $\bar y = 1 + \frac52 = \frac72$, and $\rho = \frac{5\sqrt5}{2}$.

```plot
title: $y = x^2$ and its circle of curvature at $(1, 1)$, centre $(-4, \frac72)$
x: -10, 4
y: -3, 10
equal: true
f: x^2 | $y = x^2$
implicit: (x + 4)^2 + (y - 3.5)^2 = 31.25 | circle of curvature
point: 1, 1 | $(1, 1)$
point: -4, 3.5 | centre
```

**Chord of curvature** (the chord of the circle of curvature through $P$):

| Direction of the chord | Length |
|:---|:---|
| parallel to the $x$-axis | $2\rho\sin\psi$ |
| parallel to the $y$-axis | $2\rho\cos\psi$ |
| through the pole (polar curve) | $2\rho\sin\phi = 2p\dfrac{dr}{dp}$ |

For the cardioid, the chord through the pole is $2\cdot\frac{4a}{3}\cos\frac\theta2\cdot\cos\frac\theta2 = \frac{4r}{3}$.

:::caution
Newton's formula needs the axis to be the **tangent** at $O$. Applied to a branch that does not touch the $x$-axis, $\lim\frac{x^2}{2y}$ is $0$ or meaningless.
:::

## Envelopes {#envelopes}

Let $f(x, y, \alpha) = 0$ be a one-parameter family of curves. The **envelope** is a curve that touches every member of the family, each at some point. To find it, **eliminate $\alpha$** from

$$f(x, y, \alpha) = 0, \qquad \frac{\partial f}{\partial\alpha}(x, y, \alpha) = 0.$$

**Quadratic shortcut.** If the family is $A\alpha^2 + B\alpha + C = 0$ ($A, B, C$ functions of $x, y$), the envelope is $B^2 = 4AC$: two members coincide.

**Standard envelopes.**

| Family | Envelope |
|:---|:---|
| $x\cos\alpha + y\sin\alpha = a$ | circle $x^2 + y^2 = a^2$ |
| $y = mx + \frac{a}{m}$ | parabola $y^2 = 4ax$ |
| $\frac{x}{a} + \frac{y}{b} = 1$, $a + b = c$ | $\sqrt x + \sqrt y = \sqrt c$ |
| $\frac{x}{a} + \frac{y}{b} = 1$, $ab = c^2$ | $4xy = c^2$ |
| $\frac{x}{a} + \frac{y}{b} = 1$, $a^2 + b^2 = c^2$ | astroid $x^{2/3} + y^{2/3} = c^{2/3}$ |
| $(x - \alpha)^2 + y^2 = r^2$ | the lines $y = \pm r$ |
| normals of a curve | its evolute |

**Worked examples.**
- $x\cos\alpha + y\sin\alpha = a$; $\partial_\alpha$: $-x\sin\alpha + y\cos\alpha = 0$. Squaring and adding gives $x^2 + y^2 = a^2$. Each line is at distance $a$ from $O$, so each touches this circle.
- $y = mx + \frac am$ is $xm^2 - ym + a = 0$. Then $B^2 = 4AC$ gives $y^2 = 4ax$.
- **The ladder.** With $a = c\cos\alpha$, $b = c\sin\alpha$, the family is $\frac{x}{\cos\alpha} + \frac{y}{\sin\alpha} = c$. Differentiating: $\frac{x\sin\alpha}{\cos^2\alpha} = \frac{y\cos\alpha}{\sin^2\alpha}$, so $x = c\cos^3\alpha$, $y = c\sin^3\alpha$: the astroid.

```plot
title: A ladder of length 1 sliding between the axes: its positions envelop the astroid
x: -0.1, 1.2
y: -0.1, 1.2
equal: true
param: cos(t)^3, sin(t)^3 | astroid $x^{2/3} + y^{2/3} = 1$
t: 0, pi/2
f: 0.2588 - 0.2679x
f: 0.5 - 0.5774x
f: 0.7071 - x
f: 0.866 - 1.732x
f: 0.9659 - 3.732x
```

:::caution
The eliminant from $f = 0$, $f_\alpha = 0$ can also contain a **locus of singular points** (nodes or cusps) of the members, which is not a true envelope. Check that the curve found actually touches the members.
:::

## Curve tracing {#curve-tracing}

**Steps for a Cartesian curve $F(x, y) = 0$.**

1. **Symmetry.** Only even powers of $y$: symmetric about the $x$-axis. Only even powers of $x$: about the $y$-axis. Unchanged when $(x, y) \to (-x, -y)$: about the origin. Unchanged when $x$ and $y$ are swapped: about the line $y = x$.
2. **Origin.** The curve passes through $O$ if there is no constant term. The **tangents at $O$** come from equating the lowest-degree terms to zero.
3. **Intercepts** and the tangents there.
4. **Asymptotes** (see above).
5. **Region.** Where $y$ is real; e.g. $y^2 = g(x)$ needs $g(x) \ge 0$.
6. **Monotonicity, extrema and points of inflexion** from $y_1$ and $y_2$.

**Double points.** At a double point, the two tangents are:

| Tangents | Name |
|:---|:---|
| real and distinct | **node** (two branches cross) |
| real and coincident | **cusp** (usually; it can also be a tacnode) |
| imaginary | **conjugate (isolated) point** |

For example, $y^2 = x^2(x - 1)$ has the lowest terms $y^2 + x^2$. The tangents are imaginary, so $O$ is an isolated point: near $O$, $x - 1 < 0$ forces $y = 0 = x$.

**For polar curves:** symmetry about the initial line if the equation is unchanged under $\theta \to -\theta$. The tangents at the pole are the lines $\theta = \theta_0$ with $f(\theta_0) = 0$. Tabulate $r$ against $\theta$.

**Familiar curves.**

| Curve | Key features |
|:---|:---|
| cissoid $y^2(2a - x) = x^3$ | symmetric about $Ox$; cusp at $O$ (tangent $y = 0$); asymptote $x = 2a$; lies in $0 \le x < 2a$ |
| folium $x^3 + y^3 = 3axy$ | symmetric about $y = x$; node at $O$ with tangents $x = 0,\ y = 0$; loop in the first quadrant reaching $(\frac{3a}{2}, \frac{3a}{2})$; asymptote $x + y + a = 0$ |
| astroid $x^{2/3} + y^{2/3} = a^{2/3}$ | symmetric about both axes; four cusps $(\pm a, 0), (0, \pm a)$; no asymptote |
| cardioid $r = a(1 + \cos\theta)$ | symmetric about the initial line; $r_{\max} = 2a$ at $\theta = 0$; cusp at the pole ($\theta = \pi$) |
| lemniscate $r^2 = a^2\cos2\theta$ | symmetric about both axes; node at the pole with tangents $\theta = \pm\frac\pi4$; real only where $\cos 2\theta \ge 0$; Cartesian form $(x^2 + y^2)^2 = a^2(x^2 - y^2)$ |

```plot
title: Cardioid $r = 1 + \cos\theta$ and lemniscate $(x^2 + y^2)^2 = x^2 - y^2$
x: -1.5, 2.5
y: -1.5, 1.5
equal: true
polar: 1 + cos(t) | cardioid
implicit: (x^2 + y^2)^2 = x^2 - y^2 | lemniscate
```

## Quick checks and traps {#exam-tips}

:::keyfacts
- $\tan\phi = r\frac{d\theta}{dr}$; $p = r\sin\phi$; $\frac{1}{p^2} = u^2 + u_\theta^2$ with $u = \frac1r$.
- Parabola (focus): $p^2 = ar$. Cardioid: $p^2 = \frac{r^3}{2a}$. Lemniscate: $pa^2 = r^3$. Spiral: $p = r\sin\alpha$.
- Oblique asymptote: $\phi_n(m) = 0$, $c = -\frac{\phi_{n-1}(m)}{\phi_n'(m)}$. At most $n$ asymptotes for degree $n$.
- $\rho = \frac{(1 + y_1^2)^{3/2}}{\lvert y_2\rvert}$; $\rho = r\frac{dr}{dp}$; Newton: $\rho = \lim\frac{x^2}{2y}$.
- Envelope: eliminate $\alpha$ from $f = 0$, $f_\alpha = 0$; for a quadratic in $\alpha$, $B^2 = 4AC$.
:::

**Fast checks.**
- **Pedal equation check:** test it at one convenient point. For the cardioid at $\theta = 0$: $r = 2a$, the tangent is vertical, so $p = 2a$, and $p^2 = 4a^2 = \frac{(2a)^3}{2a}$.
- **Asymptote check:** substitute $y = mx + c$ into $F$. The coefficients of $x^n$ and $x^{n-1}$ must vanish.
- **Radius of curvature check:** on a circle the answer must reduce to the radius; at the vertex of $y^2 = 4ax$ it is $2a$.

**Traps.**
- Mixing $\phi$ (radius vector to tangent) with $\psi$ (initial line to tangent): $\psi = \theta + \phi$.
- Writing the asymptotes of $x^3 - 6x^2y + 11xy^2 - 6y^3 + \cdots$ as $y = x, 2x, 3x$. The roots of $\phi_3(m) = 0$ are $m = 1, \frac12, \frac13$.
- The parabola has no asymptote; the hyperbola $xy = c^2$ has the two axes as asymptotes.
- $\rho$ at the vertex of $y^2 = 4ax$ is $2a$, not $a$.
- The envelope of $\frac xa + \frac yb = 1$ depends on the constraint: $a + b = c$ gives $\sqrt x + \sqrt y = \sqrt c$; $a^2 + b^2 = c^2$ gives the astroid.
- "Coincident tangents at a double point" does not by itself prove a cusp; check the branches.
