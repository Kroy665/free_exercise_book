import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.two-variables")

# q1
T.single(1, ["limits-continuity"],
    r"For $f(x,y) = \dfrac{xy}{x^2 + y^2}$, the limit of $f$ as $(x,y) \to (0,0)$ along the line $y = 2x$ is",
    [r"$\dfrac25$", r"$\dfrac12$", r"$0$", r"$\dfrac23$"],
    r"""Put $y = 2x$:
$$f(x, 2x) = \frac{2x^2}{x^2 + 4x^2} = \frac25.$$
In general the line $y = mx$ gives $\frac{m}{1+m^2}$; $\frac12$ is the value for $m = 1$. Because the value depends on $m$, the double limit does not exist.""")

# q2
T.single(2, ["limits-continuity"],
    r"For $f(x,y) = \dfrac{x - y}{x + y}$, the repeated limits $\lim\limits_{x\to0}\lim\limits_{y\to0} f(x,y)$ and $\lim\limits_{y\to0}\lim\limits_{x\to0} f(x,y)$ are, respectively,",
    [r"$1$ and $-1$", r"$-1$ and $1$", r"$0$ and $0$", r"$1$ and $1$"],
    r"""Inner limit first. For fixed $x \ne 0$: $\lim_{y\to0}\frac{x - y}{x + y} = \frac{x}{x} = 1$, so the first repeated limit is $1$.

For fixed $y \ne 0$: $\lim_{x\to0}\frac{x - y}{x + y} = \frac{-y}{y} = -1$, so the second is $-1$.

Swapping the order of the inner and outer limits gives the reversed option. Since the repeated limits differ, the double limit at $(0,0)$ does not exist.""")

# q3
T.single(2, ["limits-continuity", "exam-tips"],
    r"$\lim\limits_{(x,y)\to(0,0)} \dfrac{x^2 y}{x^4 + y^2}$",
    [r"does not exist", r"equals $0$", r"equals $\dfrac12$", r"equals $1$"],
    r"""Along every line $y = mx$ ($m \ne 0$):
$$\frac{mx^3}{x^4 + m^2x^2} = \frac{mx}{x^2 + m^2} \to 0,$$
and on the axes $f = 0$. But along the parabola $y = x^2$:
$$\frac{x^4}{x^4 + x^4} = \frac12.$$
Two paths give different values, so the limit does not exist. "$0$" is the trap of testing straight lines only.""")

# q4
T.single(1, ["limits-continuity"],
    r"$\lim\limits_{(x,y)\to(0,0)} \dfrac{x^2 y^2}{x^2 + y^2}$",
    [r"equals $0$", r"equals $1$", r"equals $\dfrac12$", r"does not exist"],
    r"""Use polar coordinates $x = r\cos\theta$, $y = r\sin\theta$:
$$\left|\frac{x^2y^2}{x^2+y^2}\right| = r^2\cos^2\theta\sin^2\theta \le r^2 \to 0,$$
and the bound does not depend on $\theta$. So the limit is $0$.

Paths cannot prove existence, but here the numerator has degree 4 against degree 2 in the denominator, so the value is squeezed to $0$.""")

# q5
T.single(2, ["partial-derivatives", "differentiability"],
    r"Let $f(x,y) = \dfrac{xy}{x^2 + y^2}$ for $(x,y) \ne (0,0)$ and $f(0,0) = 0$. At the origin,",
    [r"$f_x(0,0)$ and $f_y(0,0)$ both exist, but $f$ is not continuous",
     r"$f$ is continuous, but $f_x(0,0)$ does not exist",
     r"$f$ is differentiable",
     r"$f_x(0,0) = f_y(0,0) = \dfrac12$"],
    r"""On the axes $f = 0$, so
$$f_x(0,0) = \lim_{h\to0}\frac{f(h,0) - 0}{h} = 0, \qquad f_y(0,0) = 0.$$
Along $y = mx$, $f = \frac{m}{1+m^2}$, which depends on $m$, so $f$ has no limit at the origin and is not continuous. Hence it is not differentiable either.

$\frac12$ is the value along $y = x$, not a partial derivative.""")

# q6
T.single(3, ["differentiability"],
    r"For $f(x,y) = \sqrt{\lvert xy\rvert}$ at the origin, which statement is correct?",
    [r"$f$ is continuous and $f_x(0,0) = f_y(0,0) = 0$, but $f$ is not differentiable",
     r"$f$ is differentiable at $(0,0)$",
     r"$f$ is continuous, but $f_x(0,0)$ does not exist",
     r"$f$ is not continuous at $(0,0)$"],
    r"""Continuity: $\sqrt{|xy|} \le \frac{|x| + |y|}{2} \to 0$.

Partials: $f(h,0) = f(0,k) = 0$, so both partial derivatives are $0$.

Differentiability would need
$$\frac{f(h,k) - 0 - 0\cdot h - 0\cdot k}{\sqrt{h^2+k^2}} = \frac{\sqrt{|hk|}}{\sqrt{h^2+k^2}} \to 0.$$
Along $h = k$ this ratio is $\frac{|h|}{\sqrt2|h|} = \frac{1}{\sqrt2}$. So $f$ is not differentiable.

"Differentiable" is the tempting option: continuity and existing partials are not enough.""")

# q7
T.single(2, ["differentiability"],
    r"Using the total differential, the approximate change in $z = x^2 y$ when $(x, y)$ changes from $(2, 3)$ to $(2.01, 2.98)$ is",
    [r"$0.04$", r"$0.20$", r"$-0.04$", r"$0.12$"],
    r"""$dz = 2xy\,dx + x^2\,dy$ with $x = 2$, $y = 3$, $dx = 0.01$, $dy = -0.02$:
$$dz = 12(0.01) + 4(-0.02) = 0.12 - 0.08 = 0.04.$$
$0.12$ forgets the $y$-term; $0.20$ ignores the negative sign of $dy$. The exact change is $2.01^2(2.98) - 12 \approx 0.0394$.""")

# q8
T.single(1, ["chain-rule"],
    r"If $z = xy$ with $x = e^{t}$ and $y = \cos t$, then $\dfrac{dz}{dt}$ equals",
    [r"$e^{t}(\cos t - \sin t)$", r"$e^{t}(\cos t + \sin t)$", r"$-e^{t}\sin t$", r"$e^{t}\cos t$"],
    r"""By the chain rule,
$$\frac{dz}{dt} = z_x\frac{dx}{dt} + z_y\frac{dy}{dt} = y e^{t} + x(-\sin t) = e^{t}(\cos t - \sin t).$$
**Check:** $z = e^t\cos t$ directly, and the product rule gives the same. Missing the sign of $\frac{d}{dt}\cos t$ gives $\cos t + \sin t$.""")

# q9
T.single(2, ["chain-rule"],
    r"If $x^3 + y^3 = 3axy$ defines $y$ as a differentiable function of $x$, then $\dfrac{dy}{dx}$ equals",
    [r"$\dfrac{ay - x^2}{y^2 - ax}$", r"$\dfrac{x^2 - ay}{y^2 - ax}$", r"$\dfrac{ay - x^2}{ax - y^2}$", r"$\dfrac{ax - y^2}{x^2 - ay}$"],
    r"""With $F = x^3 + y^3 - 3axy$: $F_x = 3x^2 - 3ay$, $F_y = 3y^2 - 3ax$. Then
$$\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{x^2 - ay}{y^2 - ax} = \frac{ay - x^2}{y^2 - ax}.$$
The second option drops the minus sign; the third has it twice. The last is the reciprocal, $-F_y/F_x$, which is $dx/dy$ up to sign.""")

# q10
T.single(2, ["chain-rule"],
    r"If $z = f(x,y)$ is differentiable and $x = r\cos\theta$, $y = r\sin\theta$, then $\left(\dfrac{\partial z}{\partial x}\right)^2 + \left(\dfrac{\partial z}{\partial y}\right)^2$ equals",
    [r"$z_r^2 + \dfrac{1}{r^2}z_\theta^2$", r"$z_r^2 + z_\theta^2$", r"$z_r^2 + r^2 z_\theta^2$", r"$z_r^2 - \dfrac{1}{r^2}z_\theta^2$"],
    r"""By the chain rule,
$$z_r = z_x\cos\theta + z_y\sin\theta, \qquad z_\theta = r(-z_x\sin\theta + z_y\cos\theta).$$
So $z_r^2 + \frac{z_\theta^2}{r^2} = z_x^2 + z_y^2$, since the cross terms cancel.

**Check:** $z = x$ gives $z_r = \cos\theta$, $z_\theta = -r\sin\theta$, and $\cos^2\theta + \sin^2\theta = 1$. Forgetting the factor $r$ in $z_\theta$ gives $z_r^2 + z_\theta^2$.""")

# q11
T.single(3, ["higher-derivatives"],
    r"Let $f(x,y) = \dfrac{xy(x^2 - y^2)}{x^2 + y^2}$ for $(x,y) \ne (0,0)$ and $f(0,0) = 0$. The value of $\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial x}\right)$ at $(0,0)$ is",
    [r"$-1$", r"$1$", r"$0$", r"does not exist"],
    r"""First find $f_x$ on the line $x = 0$ from the definition:
$$f_x(0,y) = \lim_{h\to0}\frac{f(h,y) - f(0,y)}{h} = \lim_{h\to0}\frac{y(h^2 - y^2)}{h^2 + y^2} = -y.$$
This holds for $y = 0$ too. Then
$$\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)(0,0) = \frac{d}{dy}(-y)\Big|_{y=0} = -1.$$
The other order gives $+1$, since $f_y(x,0) = x$. The answer $0$ comes from putting $x = y = 0$ in a formula that is $0/0$ there.""")

# q12
T.single(2, ["euler-theorem"],
    r"If $u = \dfrac{x^{1/3} + y^{1/3}}{x^{1/2} + y^{1/2}}$ ($x, y > 0$), then $x\dfrac{\partial u}{\partial x} + y\dfrac{\partial u}{\partial y}$ equals",
    [r"$-\dfrac{u}{6}$", r"$\dfrac{u}{6}$", r"$\dfrac{5u}{6}$", r"$-\dfrac{u}{5}$"],
    r"""The numerator has degree $\frac13$ and the denominator degree $\frac12$, so $u$ is homogeneous of degree $\frac13 - \frac12 = -\frac16$. By Euler's theorem,
$$xu_x + yu_y = -\frac16\,u.$$
Subtracting the degrees the wrong way round gives $+\frac{u}{6}$; adding them gives $\frac{5u}{6}$.""")

# q13
T.single(2, ["euler-theorem"],
    r"If $u = \dfrac{x^4 + y^4}{x + y}$, then $x^2 u_{xx} + 2xy\,u_{xy} + y^2 u_{yy}$ equals",
    [r"$6u$", r"$3u$", r"$9u$", r"$12u$"],
    r"""$u$ is homogeneous of degree $n = 4 - 1 = 3$. The second-order form of Euler's theorem gives
$$x^2u_{xx} + 2xy\,u_{xy} + y^2u_{yy} = n(n-1)u = 3\cdot2\,u = 6u.$$
$3u$ is the first-order result $nu$; $9u$ uses $n^2$; $12u$ uses $n(n+1)$.""")

# q14
T.single(3, ["euler-theorem"],
    r"If $u = \tan^{-1}\dfrac{x^3 + y^3}{x - y}$ ($x \ne y$), then $x u_x + y u_y$ equals",
    [r"$\sin 2u$", r"$2\tan u$", r"$\tan u$", r"$2\sin u$"],
    r"""$u$ is not homogeneous, but $z = \tan u = \frac{x^3 + y^3}{x - y}$ is homogeneous of degree $2$. Euler for $z$:
$$x z_x + y z_y = 2z \;\Rightarrow\; \sec^2u\,(xu_x + yu_y) = 2\tan u.$$
So
$$xu_x + yu_y = \frac{2\tan u}{\sec^2 u} = 2\sin u\cos u = \sin 2u.$$
$2\tan u$ is Euler applied to $\tan u$, forgetting to divide by $\sec^2 u$.""")

# q15
T.single(3, ["euler-theorem"],
    r"If $u = \sin^{-1}\dfrac{x^2 + y^2}{x + y}$, then $x^2 u_{xx} + 2xy\,u_{xy} + y^2 u_{yy}$ equals",
    [r"$\tan^3 u$", r"$\tan u\sec^2 u$", r"$\tan u$", r"$0$"],
    r"""$\sin u = \frac{x^2+y^2}{x+y}$ is homogeneous of degree $1$, so
$$g(u) := xu_x + yu_y = \frac{1\cdot\sin u}{\cos u} = \tan u.$$
The second-order composite formula is $g(u)\big(g'(u) - 1\big)$:
$$\tan u\,(\sec^2 u - 1) = \tan^3 u.$$
$\tan u\sec^2 u$ is $g\,g'$, which forgets the $-1$ (that term comes from $xu_x + yu_y$ reappearing when the first-order identity is differentiated). $\tan u$ is the first-order answer.""")

# q16
T.single(1, ["extrema"],
    r"The stationary point of $f(x,y) = x^2 + xy + y^2 - 3x$ is",
    [r"$(2, -1)$", r"$(-1, 2)$", r"$(1, 1)$", r"$\left(\dfrac32, 0\right)$"],
    r"""Solve $f_x = 2x + y - 3 = 0$ and $f_y = x + 2y = 0$. The second gives $x = -2y$; then $-4y + y = 3$, so $y = -1$ and $x = 2$.

Here $r = 2$, $s = 1$, $t = 2$, and $rt - s^2 = 3 > 0$ with $r > 0$, so it is a minimum. $\left(\frac32, 0\right)$ solves $f_x = 0$ with $y = 0$ only.""")

# q17
T.single(1, ["extrema"],
    r"At a stationary point of $f(x,y)$, with continuous second partial derivatives, $f_{xx} = 2$, $f_{xy} = 3$ and $f_{yy} = 4$. Then $f$ has",
    [r"a saddle point there", r"a local minimum there", r"a local maximum there", r"a point where the test is inconclusive"],
    r"""$r = 2$, $s = 3$, $t = 4$:
$$rt - s^2 = 8 - 9 = -1 < 0,$$
so the point is a saddle point. The sign of $r$ matters only when $rt - s^2 > 0$; "local minimum" comes from looking at $r = 2 > 0$ alone.""")

# q18
T.single(3, ["extrema"],
    r"The minimum value of $f(x,y) = x^4 + y^4 - 2(x - y)^2$ is",
    [r"$-8$", r"$-4$", r"$0$", r"$-2$"],
    r"""$f_x = 4x^3 - 4(x - y) = 0$ and $f_y = 4y^3 + 4(x - y) = 0$. Adding: $x^3 + y^3 = 0$, so $y = -x$. Then $4x^3 - 8x = 0$, giving $x = 0, \pm\sqrt2$.

At $(\sqrt2, -\sqrt2)$: $r = 12x^2 - 4 = 20$, $s = 4$, $t = 20$, $rt - s^2 = 384 > 0$ with $r > 0$, a minimum, with
$$f = 4 + 4 - 2(2\sqrt2)^2 = 8 - 16 = -8.$$
The same holds at $(-\sqrt2, \sqrt2)$. At $(0,0)$, $rt - s^2 = 16 - 16 = 0$ (test fails; it is in fact not an extremum). Since $f \to \infty$ as $|(x,y)| \to \infty$, $-8$ is the least value. $0$ is the value at the doubtful point.""")

# q19
T.single(2, ["extrema"],
    r"Using Lagrange multipliers, the maximum value of $xy$ subject to $x^2 + 4y^2 = 8$ is",
    [r"$2$", r"$4$", r"$1$", r"$8$"],
    r"""With $L = xy + \lambda(x^2 + 4y^2 - 8)$: $y + 2\lambda x = 0$ and $x + 8\lambda y = 0$. Eliminating $\lambda$: $x^2 = 4y^2$. Then $8y^2 = 8$, so $y = \pm1$, $x = \pm2$, and the maximum of $xy$ is $2\cdot1 = 2$.

**Check (AM–GM):** $8 = x^2 + 4y^2 \ge 2\sqrt{4x^2y^2} = 4|xy|$, so $xy \le 2$. $4$ comes from dropping the factor 4 in the constraint.""")

# q20
T.single(2, ["chain-rule"],
    r"If $x^2 + y^2 = a^2$ ($y \ne 0$) defines $y$ as a function of $x$, then $\dfrac{d^2y}{dx^2}$ equals",
    [r"$-\dfrac{a^2}{y^3}$", r"$\dfrac{a^2}{y^3}$", r"$-\dfrac{a^2}{y^2}$", r"$-\dfrac{x}{y}$"],
    r"""First $y' = -\frac{x}{y}$. Then by the quotient rule
$$y'' = -\frac{y - xy'}{y^2} = -\frac{y + x^2/y}{y^2} = -\frac{x^2 + y^2}{y^3} = -\frac{a^2}{y^3}.$$
**Check:** on the upper semicircle ($y > 0$) the curve is concave down, so $y'' < 0$. $-\frac{x}{y}$ is the first derivative.""")

# q21
T.single(3, ["partial-derivatives", "chain-rule"],
    r"If $u = f(r)$ where $r = \sqrt{x^2 + y^2}$ and $f$ is twice differentiable, then $u_{xx} + u_{yy}$ equals",
    [r"$f''(r) + \dfrac{1}{r}f'(r)$", r"$f''(r) + \dfrac{2}{r}f'(r)$", r"$f''(r)$", r"$f''(r) + \dfrac{1}{r^2}f'(r)$"],
    r"""$r_x = \frac{x}{r}$, so $u_x = f'(r)\frac{x}{r}$ and
$$u_{xx} = f''(r)\frac{x^2}{r^2} + f'(r)\frac{r^2 - x^2}{r^3}.$$
Adding the corresponding $u_{yy}$ and using $x^2 + y^2 = r^2$:
$$u_{xx} + u_{yy} = f''(r) + f'(r)\frac{2r^2 - r^2}{r^3} = f''(r) + \frac{f'(r)}{r}.$$
$f'' + \frac{2}{r}f'$ is the three-variable result. **Check:** $f = \log r$ gives $-\frac{1}{r^2} + \frac{1}{r^2} = 0$, as $\log(x^2+y^2)$ is harmonic.""")

# q22 statements
T.statements(1, ["differentiability", "partial-derivatives"],
    r"For a real function $f(x,y)$ and a point $(a,b)$, consider the following statements:",
    [r"If $f$ is differentiable at $(a,b)$, then $f$ is continuous at $(a,b)$.",
     r"If $f_x(a,b)$ and $f_y(a,b)$ both exist, then $f$ is continuous at $(a,b)$.",
     r"If $f_x$ and $f_y$ exist in a neighbourhood of $(a,b)$ and are continuous at $(a,b)$, then $f$ is differentiable at $(a,b)$."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 and 2 only", r"3 only"],
    r"""1 is true: in $f(a+h,b+k) - f(a,b) = Ah + Bk + \varepsilon\sqrt{h^2+k^2}$, the right side tends to $0$.

2 is false: $\frac{xy}{x^2+y^2}$ (with $f(0,0) = 0$) has $f_x(0,0) = f_y(0,0) = 0$ but no limit at the origin.

3 is true: it is the standard sufficient condition for differentiability (proved with the mean value theorem in each variable).""")

# q23 statements
T.statements(3, ["higher-derivatives"],
    r"Consider the following statements about the mixed partial derivatives of $f(x,y)$ at a point $(a,b)$:",
    [r"If $f_x$, $f_y$ and $\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial x}\right)$ exist in a neighbourhood of $(a,b)$ and the last is continuous at $(a,b)$, then $\dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial y}\right)(a,b)$ exists and the two mixed derivatives are equal at $(a,b)$.",
     r"If $f_x$ and $f_y$ are both differentiable at $(a,b)$, then the two mixed derivatives at $(a,b)$ are equal.",
     r"If both mixed derivatives exist at $(a,b)$, then they are equal."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1 is Schwarz's theorem and 2 is Young's theorem; both are true.

3 is false. For $f = \frac{xy(x^2-y^2)}{x^2+y^2}$, $f(0,0) = 0$, we have $f_x(0,y) = -y$ and $f_y(x,0) = x$, so at the origin
$$\frac{\partial}{\partial y}\frac{\partial f}{\partial x} = -1, \qquad \frac{\partial}{\partial x}\frac{\partial f}{\partial y} = 1.$$
Both exist and differ.""")

# q24 match
T.match(2, ["euler-theorem"],
    r"Match each homogeneous function in List I with its degree in List II ($x, y > 0$).",
    [r"$\dfrac{x^2 + y^2}{x + y}$", r"$x^3 - 3xy^2$", r"$\dfrac{\sqrt x + \sqrt y}{x + y}$", r"$\dfrac{x}{y} + \dfrac{y}{x}$"],
    [r"$0$", r"$1$", r"$-\dfrac12$", r"$3$"],
    [r"A-2, B-4, C-3, D-1", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-2, B-3, C-4, D-1"],
    r"""Replace $(x,y)$ by $(tx,ty)$ and read off the power of $t$:
- A: $\frac{t^2}{t} = t^1$, degree $1$ (2).
- B: every term has degree $3$ (4).
- C: $\frac{t^{1/2}}{t} = t^{-1/2}$, degree $-\frac12$ (3).
- D: $\frac{tx}{ty} = \frac{x}{y}$, degree $0$ (1).

So A-2, B-4, C-3, D-1.""")

# q25 match
T.match(2, ["extrema"],
    r"Match each function in List I with the nature of its stationary point at the origin, as given by the $rt - s^2$ test (List II).",
    [r"$x^2 + xy + y^2$", r"$2xy - x^2 - 2y^2$", r"$x^2 - 3xy + y^2$", r"$x^4 + y^4$"],
    [r"$rt - s^2 = 0$; the test fails", r"local maximum", r"saddle point", r"local minimum"],
    [r"A-4, B-2, C-3, D-1", r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-3, D-1", r"A-4, B-3, C-2, D-1"],
    r"""At $(0,0)$:
- A: $r = 2$, $s = 1$, $t = 2$; $rt - s^2 = 3 > 0$, $r > 0$: minimum (4).
- B: $r = -2$, $s = 2$, $t = -4$; $rt - s^2 = 8 - 4 = 4 > 0$, $r < 0$: maximum (2).
- C: $r = 2$, $s = -3$, $t = 2$; $rt - s^2 = -5 < 0$: saddle (3).
- D: $r = s = t = 0$: the test fails (1), though $x^4 + y^4$ clearly has a minimum.

So A-4, B-2, C-3, D-1.""")

# q26 AR
T.assertion_reason(2, ["extrema"],
    r"$f(x,y) = x^3 + y^3 - 3xy$ has a local minimum at $(1,1)$.",
    r"At a stationary point where $rt - s^2 > 0$, a function with continuous second partial derivatives always has a local minimum.",
    2,
    r"""A is true: $f_x = 3x^2 - 3y$ and $f_y = 3y^2 - 3x$ vanish at $(1,1)$; $r = 6$, $s = -3$, $t = 6$, so $rt - s^2 = 27 > 0$ with $r > 0$. The minimum value is $-1$.

R is false: $rt - s^2 > 0$ gives an extremum, a minimum if $r > 0$ and a maximum if $r < 0$. For $-x^2 - y^2$ at the origin, $rt - s^2 = 4 > 0$ but the point is a maximum.""")

# q27 AR
T.assertion_reason(2, ["limits-continuity"],
    r"$\lim\limits_{(x,y)\to(0,0)} \dfrac{xy}{x^2 + y^2}$ does not exist.",
    r"Both repeated limits of $\dfrac{xy}{x^2 + y^2}$ at $(0,0)$ are equal to $0$.",
    1,
    r"""A is true: along $y = mx$ the value is $\frac{m}{1+m^2}$, which depends on $m$.

R is true: for fixed $x \ne 0$, $\lim_{y\to0}\frac{xy}{x^2+y^2} = 0$, so $\lim_x\lim_y = 0$; similarly in the other order.

But R does not explain A. Equal repeated limits are consistent with a double limit; they never prove that one fails to exist. A is shown by the path test.""")

# q28 AR
T.assertion_reason(1, ["chain-rule"],
    r"On the circle $x^2 + y^2 = 1$, near any point with $y \ne 0$, $\dfrac{dy}{dx} = -\dfrac{x}{y}$.",
    r"If $F(x,y) = 0$ defines $y$ as a differentiable function of $x$, where $F$ has continuous partial derivatives and $F_y \ne 0$, then $\dfrac{dy}{dx} = -\dfrac{F_x}{F_y}$.",
    0,
    r"""Both are true, and R explains A.

R follows from differentiating $F(x, y(x)) = 0$ by the chain rule: $F_x + F_y y' = 0$.

With $F = x^2 + y^2 - 1$: $F_x = 2x$, $F_y = 2y \ne 0$, so $y' = -\frac{2x}{2y} = -\frac{x}{y}$.""")

# q29 AR
T.assertion_reason(1, ["differentiability", "partial-derivatives"],
    r"Every function $f(x,y)$ whose partial derivatives $f_x$ and $f_y$ exist at $(a,b)$ is differentiable at $(a,b)$.",
    r"Every function $f(x,y)$ that is differentiable at $(a,b)$ is continuous at $(a,b)$.",
    3,
    r"""A is false: $\frac{xy}{x^2+y^2}$ ($0$ at the origin) has both partial derivatives $0$ at the origin but is not even continuous there; $\sqrt{|xy|}$ is continuous with zero partials but still not differentiable.

R is true: from $f(a+h,b+k) - f(a,b) = Ah + Bk + \varepsilon\sqrt{h^2+k^2}$ with $\varepsilon \to 0$, the right side tends to $0$.""")

# q30 AR
T.assertion_reason(3, ["euler-theorem"],
    r"If $u = \sin^{-1}\dfrac{x^2 + y^2}{x + y}$, then $x\dfrac{\partial u}{\partial x} + y\dfrac{\partial u}{\partial y} = \tan u$.",
    r"$\sin u$ is a homogeneous function of $x$ and $y$ of degree $1$.",
    0,
    r"""Both are true, and R explains A.

R: $\frac{(tx)^2 + (ty)^2}{tx + ty} = t\cdot\frac{x^2+y^2}{x+y}$.

Apply Euler's theorem to $z = \sin u$: $xz_x + yz_y = z$, that is,
$$\cos u\,(xu_x + yu_y) = \sin u \;\Rightarrow\; xu_x + yu_y = \tan u.$$
Note that $u$ itself is not homogeneous, so Euler cannot be applied to $u$ directly.""")


def check():
    import sympy as sp
    x, y, t, h, k, m, a, r, th, lam = sp.symbols("x y t h k m a r theta lambda", real=True)
    X, Y, T_ = sp.symbols("X Y T_", positive=True)

    # q1
    eq(sp.simplify((x*y/(x**2+y**2)).subs(y, 2*x)), sp.Rational(2, 5), "q1")
    # q2
    f2 = (x - y)/(x + y)
    eq(sp.limit(sp.limit(f2, y, 0), x, 0), 1, "q2a")
    eq(sp.limit(sp.limit(f2, x, 0), y, 0), -1, "q2b")
    # q3
    f3 = x**2*y/(x**4 + y**2)
    eq(sp.limit(f3.subs(y, m*x), x, 0), 0, "q3 lines")
    eq(sp.limit(f3.subs(y, x**2), x, 0), sp.Rational(1, 2), "q3 parabola")
    # q4: polar bound r^2 cos^2 sin^2 <= r^2 -> 0
    f4 = (x**2*y**2/(x**2+y**2)).subs({x: r*sp.cos(th), y: r*sp.sin(th)})
    eq(sp.simplify(f4), r**2*sp.cos(th)**2*sp.sin(th)**2, "q4 polar")
    eq(sp.limit(r**2, r, 0), 0, "q4")
    # q5
    f5 = x*y/(x**2+y**2)
    eq(sp.limit(f5.subs(y, 0)/x, x, 0), 0, "q5 fx")  # f(h,0)=0
    eq(sp.limit(f5.subs(y, m*x), x, 0), m/(1+m**2), "q5 path")
    assert sp.limit(f5.subs(y, x), x, 0) != sp.limit(f5.subs(y, 0), x, 0)
    # q6
    g6 = sp.sqrt(sp.Abs(h*k))/sp.sqrt(h**2+k**2)
    hp = sp.symbols("hp", positive=True)
    eq(sp.simplify(g6.subs({h: hp, k: hp})), 1/sp.sqrt(2), "q6 ratio along h=k")
    eq(sp.sqrt(sp.Abs(h*0)), 0, "q6 axis")
    # q7
    z7 = x**2*y
    dz = (sp.diff(z7, x)*sp.Rational(1, 100) + sp.diff(z7, y)*sp.Rational(-2, 100)).subs({x: 2, y: 3})
    eq(dz, sp.Rational(4, 100), "q7")
    assert abs(sp.N(z7.subs({x: sp.Rational(201, 100), y: sp.Rational(298, 100)}) - 12) - 0.04) < 0.001
    # q8
    eq(sp.diff(sp.exp(t)*sp.cos(t), t), sp.exp(t)*(sp.cos(t) - sp.sin(t)), "q8")
    # q9
    eq(sp.idiff(x**3 + y**3 - 3*a*x*y, y, x), (a*y - x**2)/(y**2 - a*x), "q9")
    # q10 with a concrete function
    F10 = x**3*y + sp.sin(x)*y**2
    zx, zy = sp.diff(F10, x), sp.diff(F10, y)
    P = F10.subs({x: r*sp.cos(th), y: r*sp.sin(th)})
    lhs = (zx**2 + zy**2).subs({x: r*sp.cos(th), y: r*sp.sin(th)})
    rhs = sp.diff(P, r)**2 + sp.diff(P, th)**2/r**2
    for vals in [(1.3, 0.4), (0.7, 2.1), (2.2, -1.0)]:
        assert abs(sp.N((lhs - rhs).subs({r: vals[0], th: vals[1]}))) < 1e-9, "q10"
    # q11
    f11 = x*y*(x**2 - y**2)/(x**2 + y**2)
    fx0y = sp.limit((f11.subs(x, h))/h, h, 0)   # f(0,y)=0
    eq(fx0y, -y, "q11 fx(0,y)")
    fyx0 = sp.limit((f11.subs(y, k))/k, k, 0)
    eq(fyx0, x, "q11 fy(x,0)")
    eq(sp.diff(fx0y, y), -1, "q11")
    eq(sp.diff(fyx0, x), 1, "q11 other order")
    # q12
    u12 = (X**sp.Rational(1, 3) + Y**sp.Rational(1, 3))/(sp.sqrt(X) + sp.sqrt(Y))
    eq(sp.simplify(X*sp.diff(u12, X) + Y*sp.diff(u12, Y) + u12/6), 0, "q12")
    # q13
    u13 = (x**4 + y**4)/(x + y)
    eq(sp.simplify(x**2*sp.diff(u13, x, 2) + 2*x*y*sp.diff(u13, x, y) + y**2*sp.diff(u13, y, 2) - 6*u13), 0, "q13")
    # q14 numeric at several points
    u14 = sp.atan((x**3 + y**3)/(x - y))
    e14 = x*sp.diff(u14, x) + y*sp.diff(u14, y) - sp.sin(2*u14)
    eq(sp.simplify(e14), 0, "q14")
    # q15
    u15 = sp.asin((x**2 + y**2)/(x + y))
    e15 = x**2*sp.diff(u15, x, 2) + 2*x*y*sp.diff(u15, x, y) + y**2*sp.diff(u15, y, 2) - sp.tan(u15)**3
    for p in [(0.3, 0.4), (0.2, 0.5), (0.6, 0.1)]:
        assert abs(sp.N(e15.subs({x: p[0], y: p[1]}))) < 1e-9, "q15"
        # distractor tan u sec^2 u is different
        assert abs(sp.N((e15 + sp.tan(u15)**3 - sp.tan(u15)/sp.cos(u15)**2).subs({x: p[0], y: p[1]}))) > 1e-3
    # q16
    f16 = x**2 + x*y + y**2 - 3*x
    assert sp.solve([sp.diff(f16, x), sp.diff(f16, y)], [x, y]) == {x: 2, y: -1}, "q16"
    # q17
    eq(2*4 - 3**2, -1, "q17")
    # q18
    f18 = x**4 + y**4 - 2*(x - y)**2
    sols = sp.solve([sp.diff(f18, x), sp.diff(f18, y)], [x, y], dict=True)
    vals = [f18.subs(s) for s in sols if all(v.is_real for v in s.values())]
    eq(min(vals, key=lambda v: sp.N(v)), -8, "q18")
    H = sp.hessian(f18, (x, y)).subs({x: sp.sqrt(2), y: -sp.sqrt(2)})
    assert H.det() > 0 and H[0, 0] > 0
    eq(sp.hessian(f18, (x, y)).subs({x: 0, y: 0}).det(), 0, "q18 doubtful")
    # q19
    L = x*y + lam*(x**2 + 4*y**2 - 8)
    sols = sp.solve([sp.diff(L, x), sp.diff(L, y), sp.diff(L, lam)], [x, y, lam], dict=True)
    eq(max((x*y).subs(s) for s in sols), 2, "q19")
    # q20
    yp = sp.idiff(x**2 + y**2 - a**2, y, x, 2)
    eq(sp.simplify(yp.subs(x**2, a**2 - y**2) + a**2/y**3), 0, "q20")
    # q21: concrete f = r^5 and exp(r)
    rr = sp.sqrt(x**2 + y**2)
    for fr in [lambda s: s**5, lambda s: sp.exp(s), lambda s: sp.log(s)]:
        u = fr(rr)
        R = sp.symbols("R", positive=True)
        expect = (sp.diff(fr(R), R, 2) + sp.diff(fr(R), R)/R).subs(R, rr)
        eq(sp.simplify(sp.diff(u, x, 2) + sp.diff(u, y, 2) - expect), 0, "q21")
    # q22: statement 2 counterexample (q5 above); statement 1, 3 standard
    # q23: counterexample computed in q11; check Schwarz holds for a smooth function
    g = sp.exp(x*y)*sp.sin(x + y**2)
    eq(sp.diff(g, x, y) - sp.diff(g, y, x), 0, "q23 smooth")
    # q24 degrees
    def deg(expr):
        s = sp.simplify(expr.subs({X: T_*X, Y: T_*Y}, simultaneous=True)/expr)
        return sp.simplify(sp.log(s)/sp.log(T_))
    eq(deg((X**2 + Y**2)/(X + Y)), 1, "q24A")
    eq(deg(X**3 - 3*X*Y**2), 3, "q24B")
    eq(deg((sp.sqrt(X) + sp.sqrt(Y))/(X + Y)), -sp.Rational(1, 2), "q24C")
    eq(deg(X/Y + Y/X), 0, "q24D")
    # q25
    def rts(f):
        H = sp.hessian(f, (x, y)).subs({x: 0, y: 0})
        return H[0, 0], H.det()
    assert rts(x**2 + x*y + y**2) == (2, 3)
    rB, dB = rts(2*x*y - x**2 - 2*y**2); assert rB < 0 and dB > 0
    assert rts(x**2 - 3*x*y + y**2)[1] < 0
    assert rts(x**4 + y**4)[1] == 0
    # q26
    f26 = x**3 + y**3 - 3*x*y
    H = sp.hessian(f26, (x, y)).subs({x: 1, y: 1})
    assert H.det() == 27 and H[0, 0] == 6
    eq(f26.subs({x: 1, y: 1}), -1, "q26")
    Hm = sp.hessian(-x**2 - y**2, (x, y))
    assert Hm.det() > 0 and Hm[0, 0] < 0  # R false
    # q27
    eq(sp.limit(sp.limit(f5, y, 0), x, 0), 0, "q27a")
    eq(sp.limit(sp.limit(f5, x, 0), y, 0), 0, "q27b")
    # q28
    eq(sp.idiff(x**2 + y**2 - 1, y, x), -x/y, "q28")
    # q29: A false via q5/q6 counterexamples; R standard
    # q30
    e30 = x*sp.diff(u15, x) + y*sp.diff(u15, y) - sp.tan(u15)
    for p in [(0.3, 0.4), (0.2, 0.5)]:
        assert abs(sp.N(e30.subs({x: p[0], y: p[1]}))) < 1e-9, "q30"
    eq(deg((X**2 + Y**2)/(X + Y)), 1, "q30 R")


T.write(check)
