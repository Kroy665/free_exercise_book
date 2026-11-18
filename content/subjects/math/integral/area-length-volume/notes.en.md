# Areas, Lengths and Volumes

## Area in Cartesian coordinates {#cartesian-area}

**Quadrature** means finding the area of a plane region by integration.

- If $f$ is continuous on $[a, b]$, the area between $y = f(x)$, the $x$-axis and the lines $x = a$, $x = b$ is
  $$A = \int_a^b \lvert f(x)\rvert\,dx.$$
  Where $f$ changes sign, split the interval at its zeros. The plain integral $\int_a^b f\,dx$ is a **signed** area.
- **Between two curves.** If $f$ and $g$ are continuous and $f(x) \ge g(x)$ on $[a, b]$, the area between them is
  $$A = \int_a^b \big(f(x) - g(x)\big)\,dx = \int_a^b (\text{upper} - \text{lower})\,dx.$$
- Strips can also be horizontal: $A = \int_c^d (x_{\text{right}} - x_{\text{left}})\,dy$. Choose the direction that needs one integral instead of two.

**Method.** Sketch the curves, solve for the intersection points (these give the limits), decide which curve is on top, then integrate.

```plot
title: Area between $y = x$ and $y = x^2$
x: -0.3, 1.4
y: -0.3, 1.4
f: x | $y = x$
f: x^2 | $y = x^2$
shade: x, 0, 1, x^2
point: 1, 1 | $(1, 1)$
equal: true
```

**Example 1.** $y = x$ and $y = x^2$ meet at $x = 0, 1$, and $x \ge x^2$ there:
$$A = \int_0^1 (x - x^2)\,dx = \frac12 - \frac13 = \frac16.$$

**Example 2.** The parabolas $y^2 = 4ax$ and $x^2 = 4ay$ ($a > 0$) meet at $(0, 0)$ and $(4a, 4a)$. The upper curve is $y = 2\sqrt{ax}$:
$$A = \int_0^{4a}\left(2\sqrt{a}\,x^{1/2} - \frac{x^2}{4a}\right)dx = \frac{4\sqrt a}{3}(4a)^{3/2} - \frac{(4a)^3}{12a} = \frac{32a^2}{3} - \frac{16a^2}{3} = \frac{16a^2}{3}.$$

**Example 3 (a loop).** The curve $ay^2 = x^2(a - x)$ is symmetric about the $x$-axis and has a loop for $0 \le x \le a$. Its area is
$$A = 2\int_0^a x\sqrt{1 - \frac{x}{a}}\,dx = \frac{8a^2}{15}$$
(substitute $x = a\sin^2\theta$, or $u = a - x$).

:::caution
"Area" is never negative. $\int_0^{2\pi}\sin x\,dx = 0$, but the area between $y = \sin x$ and the $x$-axis over $[0, 2\pi]$ is $\int_0^{2\pi}\lvert\sin x\rvert\,dx = 4$.
:::

:::exam-tip
Use symmetry first. For a curve symmetric about both axes, find the area in the first quadrant and multiply by 4.
:::

## Parametric and polar areas {#polar-area}

**Parametric.** For a closed curve $x = x(t)$, $y = y(t)$, $t \in [\alpha, \beta]$, traced once anticlockwise with $x, y$ continuously differentiable,
$$A = \frac12\int_\alpha^\beta (x\dot y - y\dot x)\,dt = \int_\alpha^\beta x\,\dot y\,dt = -\int_\alpha^\beta y\,\dot x\,dt.$$
For an arc above the $x$-axis, the area under it is $\int y\,dx = \int y(t)\,\dot x(t)\,dt$, with the limits in the order that makes $x$ increase.

**Polar.** If $r = f(\theta)$ is continuous and non-negative on $[\alpha, \beta]$, with $\beta - \alpha \le 2\pi$, the area swept by the radius vector from $\theta = \alpha$ to $\theta = \beta$ is
$$A = \frac12\int_\alpha^\beta r^2\,d\theta.$$
(An elementary sector has area $\tfrac12 r^2\,d\theta$.)

**Standard results** ($a, b > 0$):

| Curve | Area |
|:---|:---|
| Ellipse $x = a\cos t,\ y = b\sin t$ | $\pi ab$ |
| Astroid $x = a\cos^3 t,\ y = a\sin^3 t$ | $\dfrac{3\pi a^2}{8}$ |
| One arch of the cycloid $x = a(t - \sin t),\ y = a(1 - \cos t)$ | $3\pi a^2$ |
| Circle $r = 2a\cos\theta$ | $\pi a^2$ |
| Cardioid $r = a(1 + \cos\theta)$ | $\dfrac{3\pi a^2}{2}$ |
| One loop of $r = a\cos 2\theta$ (4 loops) | $\dfrac{\pi a^2}{8}$ |
| One loop of $r = a\sin 3\theta$ (3 loops) | $\dfrac{\pi a^2}{12}$ |
| Lemniscate $r^2 = a^2\cos 2\theta$ (both loops) | $a^2$ |

**Cardioid.** $\displaystyle A = 2\cdot\frac12\int_0^\pi a^2(1 + \cos\theta)^2\,d\theta = a^2\left(\pi + 0 + \frac{\pi}{2}\right) = \frac{3\pi a^2}{2}.$

**One loop of $r = a\cos 2\theta$.** The loop on the initial line lies between $\theta = -\pi/4$ and $\pi/4$ (where $r = 0$):
$$A = \frac12\int_{-\pi/4}^{\pi/4} a^2\cos^2 2\theta\,d\theta = \frac{a^2}{2}\cdot\frac{\pi}{4} = \frac{\pi a^2}{8}.$$
Similarly one loop of $r = a\sin 3\theta$ is $0 \le \theta \le \pi/3$, with area $\frac{a^2}{2}\cdot\frac{\pi}{6} = \frac{\pi a^2}{12}$.

```plot
title: Cardioid $r = 1 + \cos\theta$ and the four-leaved rose $r = \cos 2\theta$
polar: 1 + cos(t) | $r = 1 + \cos\theta$
polar: cos(2t) | $r = \cos 2\theta$
t: 0, 2pi
x: -1.2, 2.3
y: -1.6, 1.6
equal: true
```

:::caution
**Rose petals.** $r = a\cos n\theta$ has $n$ loops if $n$ is odd and $2n$ loops if $n$ is even. Integrating $\frac12 r^2$ over $[0, 2\pi]$ gives the right total for even $n$ ($\pi a^2/2$), but for odd $n$ it traces every loop **twice**: the total area of $r = a\sin 3\theta$ is $\pi a^2/4$, not $\pi a^2/2$.
:::

## Rectification: arc length {#arc-length}

**Rectification** means finding the length of an arc. If the function(s) below are continuously differentiable on the interval, the arc length $s$ is:

| Form | $ds$ | Length |
|:---|:---|:---|
| $y = f(x)$, $a \le x \le b$ | $\sqrt{1 + y'^2}\,dx$ | $\displaystyle\int_a^b \sqrt{1 + \left(\tfrac{dy}{dx}\right)^2}\,dx$ |
| $x = x(t),\ y = y(t)$ | $\sqrt{\dot x^2 + \dot y^2}\,dt$ | $\displaystyle\int_\alpha^\beta \sqrt{\dot x^2 + \dot y^2}\,dt$ |
| $r = f(\theta)$ | $\sqrt{r^2 + r'^2}\,d\theta$ | $\displaystyle\int_\alpha^\beta \sqrt{r^2 + \left(\tfrac{dr}{d\theta}\right)^2}\,d\theta$ |

All three come from $ds^2 = dx^2 + dy^2$ (in polar form, $ds^2 = dr^2 + r^2\,d\theta^2$).

**Standard results:**

- **Cycloid**, one arch: $\dot x^2 + \dot y^2 = 2a^2(1 - \cos t) = 4a^2\sin^2\frac t2$, so
  $$s = \int_0^{2\pi} 2a\sin\frac t2\,dt = 8a.$$
- **Astroid**, whole perimeter: $ds = 3a\lvert\sin t\cos t\rvert\,dt$, so $s = 4\int_0^{\pi/2} 3a\sin t\cos t\,dt = 4\cdot\frac{3a}{2} = 6a$.
- **Cardioid** $r = a(1 + \cos\theta)$: $r^2 + r'^2 = 2a^2(1 + \cos\theta) = 4a^2\cos^2\frac\theta2$, so
  $$s = 2\int_0^{\pi} 2a\cos\frac\theta2\,d\theta = 8a.$$
- **Catenary** $y = c\cosh\frac xc$: $1 + y'^2 = \cosh^2\frac xc$, so the arc from the vertex $(0, c)$ to the point with abscissa $x$ is
  $$s = c\sinh\frac xc, \qquad\text{and hence}\qquad y^2 = c^2 + s^2.$$
- **Semicubical parabola** $y = \frac23 x^{3/2}$ from $x = 0$ to $x = 3$: $s = \int_0^3\sqrt{1 + x}\,dx = \frac23(8 - 1) = \frac{14}{3}$.
- **Parabola** $y^2 = 4ax$ from the vertex to an end of the latus rectum $(a, 2a)$: $s = a\left[\sqrt2 + \ln(1 + \sqrt2)\right]$.

:::caution
The integrand is $\sqrt{1 + y'^2}$, **not** $1 + y'$ or $\sqrt{1 + y'}$. For a parametric curve, take $\sqrt{\dot x^2 + \dot y^2}$ as a non-negative quantity: where $\sin t\cos t$ or $\sin\frac t2$ changes sign, split the range or use symmetry, or the pieces cancel.
:::

:::exam-tip
Remember the "8a" family: the whole cardioid and one cycloid arch are both $8a$. The astroid is $6a$.
:::

## Volumes of solids of revolution {#volume-revolution}

Let $f$ be continuous on $[a, b]$.

- **Disc method.** Revolving the region under $y = f(x)$, $a \le x \le b$, about the $x$-axis gives
  $$V = \pi\int_a^b y^2\,dx.$$
  About the $y$-axis, a region bounded by $x = g(y)$, $c \le y \le d$: $V = \pi\int_c^d x^2\,dy$.
- **Washer method.** Revolving the region between $y = f(x) \ge y = g(x) \ge 0$ about the $x$-axis gives
  $$V = \pi\int_a^b \left(f^2 - g^2\right)dx.$$
- **Shell method.** Revolving the region under $y = f(x) \ge 0$, $0 \le a \le x \le b$, about the $y$-axis gives $V = 2\pi\int_a^b x\,f(x)\,dx$.
- **Parametric:** $V = \pi\int y^2\,\dfrac{dx}{dt}\,dt$ about the $x$-axis.
- **Polar region** $0 \le r \le f(\theta)$, $\alpha \le \theta \le \beta$ (within $[0, \pi]$), about the initial line:
  $$V = \frac{2\pi}{3}\int_\alpha^\beta r^3\sin\theta\,d\theta.$$

**Standard results:**

| Solid | Volume |
|:---|:---|
| Sphere: $x^2 + y^2 = a^2$ about the $x$-axis | $\frac43\pi a^3$ |
| Ellipsoid: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ about the $x$-axis | $\frac43\pi ab^2$ |
| Same ellipse about the $y$-axis | $\frac43\pi a^2 b$ |
| Cone: $y = \frac rh x$, $0 \le x \le h$, about the $x$-axis | $\frac13\pi r^2 h$ |
| Cardioid $r = a(1 + \cos\theta)$ about the initial line | $\frac83\pi a^3$ |
| One arch of the cycloid about its base | $5\pi^2 a^3$ |

**Ellipsoid.** $V = \pi\int_{-a}^{a} b^2\left(1 - \frac{x^2}{a^2}\right)dx = \pi b^2\left(2a - \frac{2a}{3}\right) = \frac43\pi ab^2$. The axis of revolution is $2a$; the square goes on the **other** semi-axis.

**Washer example.** The region between $y = x$ and $y = x^2$, about the $x$-axis:
$$V = \pi\int_0^1 (x^2 - x^4)\,dx = \pi\left(\frac13 - \frac15\right) = \frac{2\pi}{15}.$$

:::caution
For a washer, square **each** radius and subtract: $\pi(f^2 - g^2)$. The slip $\pi(f - g)^2$ gives $\pi\int_0^1 (x - x^2)^2\,dx = \frac{\pi}{30}$ above, which is wrong.
:::

## Surface area of revolution and Pappus's theorems {#surface-revolution}

If $y \ge 0$ and the arc is continuously differentiable, revolving it about the $x$-axis gives the surface area
$$S = 2\pi\int y\,ds,$$
with $ds$ from the table in the rectification section. For $y = f(x)$: $S = 2\pi\int_a^b y\sqrt{1 + y'^2}\,dx$. For a polar arc about the initial line, $y = r\sin\theta$:
$$S = 2\pi\int_\alpha^\beta r\sin\theta\,\sqrt{r^2 + r'^2}\,d\theta.$$

**Sphere.** For $y = \sqrt{a^2 - x^2}$, $y\sqrt{1 + y'^2} = a$, so the surface between $x = h_1$ and $x = h_2$ is
$$S = 2\pi\int_{h_1}^{h_2} a\,dx = 2\pi a(h_2 - h_1).$$
A **zone** of a sphere has area $2\pi a h$, depending only on its height $h$. With $h = 2a$, the whole sphere has $S = 4\pi a^2$.

**Cardioid about its axis.** With $r = 2a\cos^2\frac\theta2$, $ds = 2a\cos\frac\theta2\,d\theta$ and $y = r\sin\theta = 4a\cos^3\frac\theta2\sin\frac\theta2$:
$$S = 2\pi\int_0^\pi 8a^2\cos^4\frac\theta2\sin\frac\theta2\,d\theta = 2\pi\cdot 16a^2\int_0^1 u^4\,du = \frac{32\pi a^2}{5}.$$
(Only $0 \le \theta \le \pi$: the lower half generates the same surface.)

Also: one cycloid arch about its base gives $S = \frac{64}{3}\pi a^2$.

### Pappus's theorems (Pappus–Guldin)

Let a plane region (or arc) lie on one side of an axis in its plane.

1. **Volume** of the solid of revolution $=$ (area of the region) $\times$ (distance travelled by its centroid) $= A\cdot 2\pi\bar y$.
2. **Surface area** $=$ (length of the arc) $\times$ (distance travelled by the arc's centroid) $= L\cdot 2\pi\bar y$.

**Torus.** The circle $(x - b)^2 + y^2 = a^2$ with $b > a$, about the $y$-axis: the centroid travels $2\pi b$, so
$$V = \pi a^2\cdot 2\pi b = 2\pi^2 a^2 b, \qquad S = 2\pi a\cdot 2\pi b = 4\pi^2 ab.$$

:::exam-tip
Pappus in reverse finds centroids: a semicircular disc of radius $a$ about its diameter gives a sphere, so $\frac12\pi a^2\cdot 2\pi\bar y = \frac43\pi a^3$ and $\bar y = \frac{4a}{3\pi}$.
:::

## Double integrals: a working knowledge {#double-integrals}

For $f$ continuous on a closed bounded region $R$, the double integral $\iint_R f\,dA$ is evaluated as an **iterated** integral (Fubini's theorem):

- **Type I** region $a \le x \le b$, $\phi_1(x) \le y \le \phi_2(x)$:
  $$\iint_R f\,dA = \int_a^b\left(\int_{\phi_1(x)}^{\phi_2(x)} f(x, y)\,dy\right)dx.$$
- **Type II** region $c \le y \le d$, $\psi_1(y) \le x \le \psi_2(y)$: integrate in $x$ first.
- On a rectangle with $f(x, y) = g(x)h(y)$, the integral splits: $\int_a^b g\,dx\cdot\int_c^d h\,dy$. For example $\int_0^1\int_0^2 xy\,dy\,dx = \frac12\cdot 2 = 1$.
- **Area:** $A(R) = \iint_R dx\,dy$.

**Reversing the order.** Sketch the region from the given limits, then describe it the other way. The triangle $0 \le x \le 1$, $x \le y \le 1$ is also $0 \le y \le 1$, $0 \le x \le y$, so
$$\int_0^1\!\int_x^1 e^{y^2}\,dy\,dx = \int_0^1\!\int_0^y e^{y^2}\,dx\,dy = \int_0^1 y\,e^{y^2}\,dy = \frac{e - 1}{2}.$$
The inner integral $\int e^{y^2}dy$ is not elementary, so reversing is the only route.

**Polar substitution.** With $x = r\cos\theta$, $y = r\sin\theta$, the Jacobian is $\dfrac{\partial(x, y)}{\partial(r, \theta)} = r$, so
$$dx\,dy = r\,dr\,d\theta.$$
Over the disc $x^2 + y^2 \le a^2$:
$$\iint e^{-(x^2 + y^2)}\,dx\,dy = \int_0^{2\pi}\!\int_0^a e^{-r^2}\,r\,dr\,d\theta = \pi\left(1 - e^{-a^2}\right).$$
Letting $a \to \infty$ gives $\left(\int_{-\infty}^{\infty} e^{-x^2}dx\right)^2 = \pi$, the Gaussian integral.

**Area of a polar region** as a double integral: $\iint r\,dr\,d\theta = \int_\alpha^\beta \frac12 f(\theta)^2\,d\theta$, which is the polar area formula again.

:::caution
The order can be swapped freely only under hypotheses: $f$ continuous on a closed bounded region, or more generally $\iint\lvert f\rvert < \infty$. Without them it can fail. For $f = \frac{x - y}{(x + y)^3}$ on $[0, 1]^2$,
$$\int_0^1\!\int_0^1 f\,dy\,dx = \frac12, \qquad \int_0^1\!\int_0^1 f\,dx\,dy = -\frac12.$$
:::

:::caution
Do not forget the factor $r$ in $dx\,dy = r\,dr\,d\theta$. Without it the disc example gives a different, wrong value.
:::

## Quick checks and traps {#exam-tips}

**Formula sheet.**

| Quantity | Cartesian | Parametric | Polar |
|:---|:---|:---|:---|
| Area | $\int y\,dx$ | $\int y\,\dot x\,dt$ | $\frac12\int r^2\,d\theta$ |
| Arc length | $\int\sqrt{1 + y'^2}\,dx$ | $\int\sqrt{\dot x^2 + \dot y^2}\,dt$ | $\int\sqrt{r^2 + r'^2}\,d\theta$ |
| Volume (about $x$-axis) | $\pi\int y^2\,dx$ | $\pi\int y^2\,\dot x\,dt$ | $\frac{2\pi}{3}\int r^3\sin\theta\,d\theta$ |
| Surface (about $x$-axis) | $2\pi\int y\,ds$ | $2\pi\int y\,ds$ | $2\pi\int r\sin\theta\,ds$ |

**Numbers to know** ($a, b, c > 0$):

- Areas: ellipse $\pi ab$; astroid $\frac38\pi a^2$; cycloid arch $3\pi a^2$; cardioid $\frac32\pi a^2$; loop of $r = a\cos 2\theta$: $\frac{\pi a^2}{8}$; loop of $r = a\sin 3\theta$: $\frac{\pi a^2}{12}$; lemniscate $a^2$.
- Lengths: cardioid $8a$; cycloid arch $8a$; astroid $6a$; catenary $s = c\sinh\frac xc$.
- Volumes: sphere $\frac43\pi a^3$; ellipsoid of revolution $\frac43\pi ab^2$ (about the axis of length $2a$); cardioid $\frac83\pi a^3$; torus $2\pi^2a^2b$.
- Surfaces: sphere $4\pi a^2$; spherical zone $2\pi ah$; cardioid $\frac{32}{5}\pi a^2$; torus $4\pi^2 ab$.

**Dimension check.** Areas carry $a^2$, lengths $a$, volumes $a^3$. An option like "$\frac83\pi a^2$" for a volume is wrong on sight.

**Traps.**

1. Signed integral vs area: split at the zeros of $f$.
2. Rose curves with odd $n$: integrating over $[0, 2\pi]$ counts every loop twice.
3. Washers: $\pi(f^2 - g^2)$, not $\pi(f - g)^2$.
4. Ellipsoid: about the $x$-axis it is $\frac43\pi a b^2$, not $\frac43\pi a^2 b$.
5. Polar surface: use $y = r\sin\theta$ and $ds = \sqrt{r^2 + r'^2}\,d\theta$, over half the curve only.
6. Jacobian $r$ in polar double integrals.
7. Reversing limits: always redraw the region; never just swap the limits.

:::exam-tip
For a quick check on a cardioid or cycloid answer, rewrite with half-angles: $1 + \cos\theta = 2\cos^2\frac\theta2$ and $1 - \cos t = 2\sin^2\frac t2$. The square roots then come out cleanly.
:::
