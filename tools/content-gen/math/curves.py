import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.curves")

# ---------------------------------------------------------------- single (20)
# q1
T.single(1, ["tangents-normals"], r"The tangent to $y = x^3$ at the point $(1, 1)$ is",
         [r"$y = 3x - 2$", r"$y = 3x + 2$", r"$3y = x + 2$", r"$y = x$"],
         r"""The slope is $\frac{dy}{dx} = 3x^2 = 3$ at $x = 1$. So
$$y - 1 = 3(x - 1) \implies y = 3x - 2.$$
Check: $(1, 1)$ satisfies $1 = 3 - 2$. The option $3y = x + 2$ is the line through $(1,1)$ with slope $\frac13$, the reciprocal slope.""")

# q2
T.single(1, ["tangents-normals"], r"The normal to the parabola $y^2 = 4x$ at the point $(1, 2)$ is",
         [r"$x + y = 3$", r"$x - y + 1 = 0$", r"$x + y = 1$", r"$2x + y = 4$"],
         r"""Differentiate: $2yy' = 4$, so $y' = \frac{2}{y} = 1$ at $(1, 2)$. The normal has slope $-1$:
$$y - 2 = -(x - 1) \implies x + y = 3.$$
$x - y + 1 = 0$ is the **tangent** at $(1, 2)$, not the normal.""")

# q3
T.single(2, ["tangents-normals"],
         r"For the astroid $x^{2/3} + y^{2/3} = a^{2/3}$ $(a > 0)$, the length of the part of any tangent intercepted between the coordinate axes is",
         [r"$a$", r"$2a$", r"$\dfrac{a}{2}$", r"$a\lvert\sin 2t\rvert$ at the point $(a\cos^3t, a\sin^3t)$, so it varies"],
         r"""Use $x = a\cos^3t$, $y = a\sin^3t$. The slope is $\frac{\dot y}{\dot x} = \frac{3a\sin^2t\cos t}{-3a\cos^2t\sin t} = -\tan t$, and the tangent is
$$\frac{x}{a\cos t} + \frac{y}{a\sin t} = 1.$$
The intercepts are $a\cos t$ and $a\sin t$, so the length is $\sqrt{a^2\cos^2t + a^2\sin^2t} = a$, the same at every point.

$a\lvert\sin 2t\rvert$ looks like a product of the intercepts; the length is the hypotenuse, not a product.""")

# q4
T.single(2, ["polar-pedal"],
         r"For the cardioid $r = a(1 - \cos\theta)$, the angle $\phi$ between the radius vector and the tangent at the point $\theta$ $(0 < \theta < \pi)$ is",
         [r"$\dfrac{\theta}{2}$", r"$\dfrac{\pi}{2} + \dfrac{\theta}{2}$", r"$\theta$", r"$\dfrac{\pi}{2} - \theta$"],
         r"""$$\tan\phi = r\frac{d\theta}{dr} = \frac{a(1 - \cos\theta)}{a\sin\theta} = \frac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)} = \tan\frac{\theta}{2},$$
so $\phi = \frac{\theta}{2}$.

$\frac\pi2 + \frac\theta2$ is the answer for the **other** cardioid $r = a(1 + \cos\theta)$, where $\tan\phi = -\cot\frac\theta2$.""")

# q5
T.single(1, ["polar-pedal"],
         r"For the equiangular spiral $r = ae^{\theta\cot\alpha}$ $(0 < \alpha < \pi/2)$, the angle between the radius vector and the tangent at any point is",
         [r"$\alpha$", r"$\dfrac{\pi}{2} - \alpha$", r"$\theta + \alpha$", r"$\cot\alpha$"],
         r"""$\frac{dr}{d\theta} = r\cot\alpha$, so
$$\tan\phi = \frac{r}{dr/d\theta} = \frac{1}{\cot\alpha} = \tan\alpha,\qquad \phi = \alpha.$$
The angle is constant, which is why the curve is called equiangular. $\theta + \alpha$ is $\psi$, the angle the tangent makes with the initial line.""")

# q6
T.single(2, ["polar-pedal"],
         r"With the focus as pole, the pedal equation of the parabola $y^2 = 4ax$ is",
         [r"$p^2 = ar$", r"$p^2 = 2ar$", r"$p = ar^2$", r"$p^2 = \dfrac{r^3}{2a}$"],
         r"""With the focus as pole and a suitable initial line, the parabola is $\frac{2a}{r} = 1 - \cos\theta$. Put $u = \frac1r = \frac{1 - \cos\theta}{2a}$, $u_\theta = \frac{\sin\theta}{2a}$:
$$\frac{1}{p^2} = u^2 + u_\theta^2 = \frac{(1 - \cos\theta)^2 + \sin^2\theta}{4a^2} = \frac{2(1 - \cos\theta)}{4a^2} = \frac{1}{ar}.$$
So $p^2 = ar$.

Check at the vertex: $r = a$ and the tangent there is at distance $a$ from the focus, so $p^2 = a^2 = a\cdot a$. $p^2 = \frac{r^3}{2a}$ is the cardioid's pedal equation.""")

# q7
T.single(1, ["asymptotes"], r"The asymptotes of the curve $y = \dfrac{2x + 3}{x - 1}$ are",
         [r"$x = 1$ and $y = 2$", r"$x = -\dfrac32$ and $y = 2$", r"$x = 1$ and $y = 3$", r"$x = 2$ and $y = 1$"],
         r"""Write the curve as $xy - y - 2x - 3 = 0$.
- The highest power of $x$ is $x^1$, with coefficient $y - 2$: asymptote $y = 2$.
- The highest power of $y$ is $y^1$, with coefficient $x - 1$: asymptote $x = 1$.

Directly: $y \to \pm\infty$ as $x \to 1$, and $y \to 2$ as $x \to \pm\infty$. $x = -\frac32$ is where the curve crosses the $x$-axis, not an asymptote.""")

# q8
T.single(2, ["asymptotes"], r"The oblique asymptote of $y = \dfrac{x^2 + 3x}{x - 1}$ is",
         [r"$y = x + 4$", r"$y = x + 3$", r"$y = x - 4$", r"$y = x + 1$"],
         r"""Divide: $x^2 + 3x = (x - 1)(x + 4) + 4$, so
$$y = x + 4 + \frac{4}{x - 1}.$$
The last term tends to $0$, so $y = x + 4$ is the asymptote. By limits: $m = \lim\frac yx = 1$ and $c = \lim(y - x) = \lim\frac{4x}{x - 1} = 4$.

$y = x + 3$ just drops the denominator's effect on the constant.""")

# q9
T.single(2, ["asymptotes", "curve-tracing"], r"The asymptote of the folium of Descartes $x^3 + y^3 = 3axy$ $(a > 0)$ is",
         [r"$x + y + a = 0$", r"$x + y = a$", r"$x - y + a = 0$", r"$x + y + 3a = 0$"],
         r"""Here $\phi_3(m) = 1 + m^3$ and $\phi_2(m) = -3am$. The only real root of $\phi_3(m) = 0$ is $m = -1$, and
$$c = -\frac{\phi_2(-1)}{\phi_3'(-1)} = -\frac{3a}{3} = -a.$$
So the asymptote is $y = -x - a$, i.e. $x + y + a = 0$.

Check: putting $y = -x - a$ into $x^3 + y^3 - 3axy$ makes the $x^3$ and $x^2$ terms vanish. $x + y = a$ has the right slope but the wrong sign of $c$.""")

# q10
T.single(3, ["asymptotes", "exam-tips"], r"The asymptotes of $x^3 - 6x^2y + 11xy^2 - 6y^3 + x + y + 1 = 0$ are",
         [r"$y = x$, $2y = x$, $3y = x$", r"$y = x$, $y = 2x$, $y = 3x$",
          r"$y = x + 1$, $2y = x + 1$, $3y = x + 1$", r"$y = -x$, $2y = -x$, $3y = -x$"],
         r"""$\phi_3(m) = 1 - 6m + 11m^2 - 6m^3 = -(m - 1)(2m - 1)(3m - 1)$, so $m = 1, \frac12, \frac13$.

There are no second-degree terms, so $\phi_2 \equiv 0$ and $c = -\frac{\phi_2(m)}{\phi_3'(m)} = 0$ for each simple root. The asymptotes are
$$y = x,\quad y = \tfrac12 x,\quad y = \tfrac13 x.$$
$y = 2x, 3x$ comes from factorising $x^3 - 6x^2y + 11xy^2 - 6y^3 = (x - y)(x - 2y)(x - 3y)$ and misreading the factors $x - 2y = 0$ as $y = 2x$.""")

# q11
T.single(3, ["asymptotes"], r"The asymptotes of the cubic $(x - y)^2(x + y) - 8x = 0$ are",
         [r"$y = x + 2$, $y = x - 2$ and $y = -x$", r"$y = x$ (counted twice) and $y = -x$",
          r"$y = x + 2$, $y = x - 2$ and $y = -x + 2$", r"$y = x + 4$, $y = x - 4$ and $y = -x$"],
         r"""$\phi_3(m) = (1 - m)^2(1 + m)$, $\phi_2 \equiv 0$, $\phi_1(m) = -8$.
- $m = -1$ (simple): $c = -\frac{\phi_2(-1)}{\phi_3'(-1)} = 0$, giving $y = -x$.
- $m = 1$ (double): $\phi_3'(1) = 0 = \phi_2(1)$, so use $\frac{c^2}{2}\phi_3''(1) + c\,\phi_2'(1) + \phi_1(1) = 0$. With $\phi_3''(1) = 4$: $2c^2 - 8 = 0$, $c = \pm2$.

So $y = x \pm 2$ and $y = -x$. Check: on $y = x + c$ the equation becomes $c^2(2x + c) - 8x = 0$; the $x$ term vanishes only for $c^2 = 4$. $y = x \pm 4$ forgets the factor $\frac12$ in $\frac{c^2}{2}\phi_3''$.""")

# q12
T.single(2, ["asymptotes"], r"The number of asymptotes of the curve $x^2y^2 - a^2(x^2 + y^2) = 0$ $(a > 0)$ is",
         [r"$4$", r"$2$", r"$0$", r"$3$"],
         r"""- Highest power of $x$: $x^2(y^2 - a^2)$, so $y = \pm a$.
- Highest power of $y$: $y^2(x^2 - a^2)$, so $x = \pm a$.
- Oblique: $\phi_4(m) = m^2$ gives only $m = 0$, already counted.

So there are $4$ asymptotes, the maximum allowed for a curve of degree $4$. Answering $2$ counts only one of the two families.""")

# q13
T.single(1, ["curvature"], r"The radius of curvature of $y = x^2$ at the origin is",
         [r"$\dfrac12$", r"$2$", r"$1$", r"$\dfrac14$"],
         r"""$y_1 = 2x = 0$ and $y_2 = 2$ at the origin, so
$$\rho = \frac{(1 + 0)^{3/2}}{2} = \frac12.$$
Newton's formula agrees: $\rho = \lim\frac{x^2}{2y} = \lim\frac{x^2}{2x^2} = \frac12$. The value $2$ is $y_2$ itself, the curvature, not its reciprocal.""")

# q14
T.single(2, ["curvature"], r"The radius of curvature at any point $(x, y)$ of the catenary $y = c\cosh\dfrac{x}{c}$ $(c > 0)$ is",
         [r"$\dfrac{y^2}{c}$", r"$c$", r"$\dfrac{c^2}{y}$", r"$\dfrac{y}{c}$"],
         r"""$y_1 = \sinh\frac xc$ and $y_2 = \frac1c\cosh\frac xc$. Since $1 + \sinh^2 = \cosh^2$,
$$\rho = \frac{\cosh^3(x/c)}{\frac1c\cosh(x/c)} = c\cosh^2\frac xc = \frac{y^2}{c}.$$
At the vertex $y = c$, so $\rho = c$ there; but $c$ is not the value at every point.""")

# q15
T.single(3, ["curvature", "polar-pedal"], r"The radius of curvature of the cardioid $r = a(1 + \cos\theta)$ at the point $\theta$ $(-\pi < \theta < \pi)$ is",
         [r"$\dfrac{4a}{3}\cos\dfrac{\theta}{2}$", r"$\dfrac{2a}{3}\cos\dfrac{\theta}{2}$",
          r"$\dfrac{4a}{3}\sin\dfrac{\theta}{2}$", r"$\dfrac{3a}{4}\cos\dfrac{\theta}{2}$"],
         r"""Pedal method: $p^2 = \frac{r^3}{2a}$ gives $2p\,dp = \frac{3r^2}{2a}\,dr$, so
$$\rho = r\frac{dr}{dp} = \frac{4ap}{3r}.$$
Here $\frac pr = \sin\phi$ and $\phi = \frac\pi2 + \frac\theta2$, so $\frac pr = \cos\frac\theta2$ and $\rho = \frac{4a}{3}\cos\frac\theta2$ $\left(= \frac23\sqrt{2ar}\right)$.

Check with the polar formula: $r^2 + r_1^2 = 4a^2\cos^2\frac\theta2$ and $r^2 + 2r_1^2 - rr_2 = 3a^2(1 + \cos\theta)$, which give the same value. At $\theta = 0$, $\rho = \frac{4a}{3}$.""")

# q16
T.single(3, ["centre-of-curvature"], r"The centre of curvature of $y = x^2$ at the point $(1, 1)$ is",
         [r"$\left(-4, \dfrac72\right)$", r"$\left(4, \dfrac72\right)$", r"$\left(-4, -\dfrac32\right)$", r"$\left(6, -\dfrac32\right)$"],
         r"""$y_1 = 2$, $y_2 = 2$, $1 + y_1^2 = 5$:
$$\bar x = x - \frac{y_1(1 + y_1^2)}{y_2} = 1 - \frac{2\cdot5}{2} = -4,\qquad \bar y = y + \frac{1 + y_1^2}{y_2} = 1 + \frac52 = \frac72.$$
The centre lies on the concave (upper) side, so $\bar y > 1$; options with $\bar y = -\frac32$ use the wrong sign. Check: the distance from $(1, 1)$ to $(-4, \frac72)$ is $\sqrt{25 + \frac{25}{4}} = \frac{5\sqrt5}{2} = \rho$.""")

# q17
T.single(2, ["envelopes"], r"The envelope of the family of lines $y = mx + \dfrac{a}{m}$ ($m$ the parameter, $a \neq 0$) is",
         [r"$y^2 = 4ax$", r"$y^2 = ax$", r"$x^2 = 4ay$", r"$xy = a$"],
         r"""Clear the denominator: $xm^2 - ym + a = 0$, a quadratic in $m$. The envelope is where the two roots coincide:
$$B^2 = 4AC \implies y^2 = 4ax.$$
This is the familiar fact that $y = mx + \frac am$ is a tangent to $y^2 = 4ax$ for every $m$. $y^2 = ax$ forgets the $4$ in the discriminant.""")

# q18
T.single(1, ["curve-tracing", "asymptotes"], r"The cissoid $y^2(2a - x) = x^3$ $(a > 0)$ has the asymptote",
         [r"$x = 2a$", r"$x = a$", r"$y = 2a$", r"$x = -2a$"],
         r"""The highest power of $y$ is $y^2$, with coefficient $2a - x$. Equating it to zero gives $x = 2a$. Indeed $y^2 = \frac{x^3}{2a - x} \to \infty$ as $x \to 2a^-$.

There is no asymptote parallel to the $x$-axis: the highest power of $x$ is $x^3$, with the constant coefficient $-1$.""")

# q19
T.single(2, ["curve-tracing", "polar-pedal"], r"The tangents to the lemniscate $r^2 = a^2\cos2\theta$ at the pole are",
         [r"$\theta = \pm\dfrac{\pi}{4}$", r"$\theta = 0$ and $\theta = \dfrac{\pi}{2}$", r"$\theta = \pm\dfrac{\pi}{3}$", r"$\theta = \pm\dfrac{\pi}{2}$"],
         r"""The tangents at the pole are the lines $\theta = \theta_0$ with $r(\theta_0) = 0$: $\cos2\theta_0 = 0$, so $\theta_0 = \pm\frac\pi4$ (the same lines as $\pm\frac{3\pi}{4}$).

In Cartesian form, $(x^2 + y^2)^2 = a^2(x^2 - y^2)$; the lowest-degree terms give $x^2 - y^2 = 0$, i.e. $y = \pm x$. The pole is a node.""")

# q20
T.single(3, ["asymptotes"], r"The asymptote of the hyperbolic spiral $r\theta = a$ $(a > 0)$ is",
         [r"$y = a$", r"$x = a$", r"$y = \dfrac{1}{a}$", r"$r = a$"],
         r"""Write $\frac1r = f(\theta) = \frac{\theta}{a}$. Then $f(\theta_1) = 0$ at $\theta_1 = 0$, and $f'(0) = \frac1a$. The asymptote is
$$r\sin(\theta - 0) = \frac{1}{f'(0)} = a, \quad\text{i.e. } y = a.$$
Directly: $y = r\sin\theta = a\frac{\sin\theta}{\theta} \to a$ while $x = a\frac{\cos\theta}{\theta} \to \infty$ as $\theta \to 0^+$.

$r = a$ is a circle (where $\theta = 1$), not an asymptote.""")

# ---------------------------------------------------------- statements (3)
T.statements(2, ["asymptotes"], r"Consider the following statements:",
             [r"An algebraic curve of degree $n$ has at most $n$ asymptotes.",
              r"The line $y = 0$ is an asymptote of $y = e^x$.",
              r"The asymptotes of the rectangular hyperbola $xy = c^2$ $(c \ne 0)$ are the coordinate axes."],
             [r"1, 2 and 3", r"1 and 2 only", r"1 and 3 only", r"2 and 3 only"],
             r"""1. True: the slopes are roots of $\phi_n(m) = 0$ (degree $\le n$), and together with the asymptotes parallel to the axes there are at most $n$.
2. True: $e^x \to 0$ as $x \to -\infty$, so the distance from the curve to $y = 0$ tends to $0$. An asymptote need only be approached along one branch.
3. True: the coefficient of the highest power of $x$ is $y$, and of $y$ is $x$, giving $y = 0$ and $x = 0$.

So all three are correct.""")

T.statements(2, ["curvature", "exam-tips"], r"Consider the following statements:",
             [r"The curvature of a straight line is zero at every point.",
              r"The radius of curvature of the parabola $y^2 = 4ax$ $(a > 0)$ at its vertex is $a$.",
              r"The curvature of $y = x^3$ at the origin is zero."],
             [r"1 and 3 only", r"1 only", r"1, 2 and 3", r"2 and 3 only"],
             r"""1. True: $\psi$ is constant on a line, so $\frac{d\psi}{ds} = 0$.
2. False: at the vertex the tangent is the $y$-axis. Newton's formula gives $\rho = \lim\frac{y^2}{2x} = \lim\frac{4ax}{2x} = 2a$, the semi-latus rectum.
3. True: $y_2 = 6x = 0$ at $x = 0$, so $\kappa = \frac{\lvert y_2\rvert}{(1 + y_1^2)^{3/2}} = 0$. The origin is a point of inflexion.

So 1 and 3 only.""")

T.statements(2, ["curve-tracing"], r"Consider the following statements about double points at the origin:",
             [r"The folium $x^3 + y^3 = 3axy$ $(a > 0)$ has a node at the origin, with tangents $x = 0$ and $y = 0$.",
              r"The cissoid $y^2(2a - x) = x^3$ $(a > 0)$ has a cusp at the origin.",
              r"The curve $y^2 = x^2(x - 1)$ has a node at the origin."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""Tangents at the origin come from the lowest-degree terms.
1. True: the lowest terms are $3axy$, giving $x = 0$ and $y = 0$: real and distinct, so a node.
2. True: the lowest terms are $2ay^2$, giving $y^2 = 0$: coincident tangents, and the two branches $y = \pm\sqrt{x^3/(2a - x)}$ start at $O$ in the same direction and stop there. So $O$ is a cusp.
3. False: the lowest terms are $y^2 + x^2$ (from $y^2 - x^3 + x^2 = 0$), giving imaginary tangents. Near $O$, $x - 1 < 0$ forces $y = x = 0$: the origin is an isolated (conjugate) point.

So 1 and 2 only.""")

# --------------------------------------------------------------- match (2)
T.match(2, ["envelopes"], r"Match each family of lines in List I ($\alpha$, $a$, $b$ the parameters; $c > 0$ fixed) with its envelope in List II.",
        [r"$x\cos\alpha + y\sin\alpha = c$", r"$\dfrac xa + \dfrac yb = 1$, where $a + b = c$",
         r"$\dfrac xa + \dfrac yb = 1$, where $ab = c^2$", r"$\dfrac xa + \dfrac yb = 1$, where $a^2 + b^2 = c^2$"],
        [r"$x^{2/3} + y^{2/3} = c^{2/3}$", r"$4xy = c^2$", r"$\sqrt x + \sqrt y = \sqrt c$", r"$x^2 + y^2 = c^2$"],
        [r"A-4, B-3, C-2, D-1", r"A-4, B-1, C-2, D-3", r"A-4, B-3, C-1, D-2", r"A-2, B-3, C-4, D-1"],
        r"""- A: every line is at distance $c$ from $O$; the envelope is the circle $x^2 + y^2 = c^2$.
- B: put $b = c - a$; then $\partial_a$: $\frac{x}{a^2} = \frac{y}{(c - a)^2}$, so $a = \frac{c\sqrt x}{\sqrt x + \sqrt y}$, and the line gives $(\sqrt x + \sqrt y)^2 = c$.
- C: $\frac xa + \frac{ay}{c^2} = 1$ is $ya^2 - c^2a + c^2x = 0$; $B^2 = 4AC$ gives $c^4 = 4c^2xy$, i.e. $4xy = c^2$.
- D: with $a = c\cos\alpha$, $b = c\sin\alpha$, the envelope is $x = c\cos^3\alpha$, $y = c\sin^3\alpha$: the astroid.

So A-4, B-3, C-2, D-1. Swapping B and D is the usual slip.""")

T.match(3, ["polar-pedal"], r"Match each curve in List I (pole at the origin, $a > 0$) with its pedal equation in List II.",
        [r"circle $r = 2a\cos\theta$", r"cardioid $r = a(1 + \cos\theta)$",
         r"lemniscate $r^2 = a^2\cos2\theta$", r"equiangular spiral $r = ae^{\theta\cot\alpha}$"],
        [r"$p = r\sin\alpha$", r"$pa^2 = r^3$", r"$2ap = r^2$", r"$p^2 = \dfrac{r^3}{2a}$"],
        [r"A-3, B-4, C-2, D-1", r"A-4, B-3, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-2, B-4, C-3, D-1"],
        r"""Use $p = r\sin\phi$.
- A: $r = 2a\cos\theta$ is $r^n = (2a)^n\cos n\theta$ with $n = 1$, so $p\cdot 2a = r^2$.
- B: $\phi = \frac\pi2 + \frac\theta2$, so $p = r\cos\frac\theta2$ and $p^2 = r^2\cdot\frac{r}{2a} = \frac{r^3}{2a}$.
- C: $n = 2$ in $pa^n = r^{n+1}$: $pa^2 = r^3$.
- D: $\phi = \alpha$, so $p = r\sin\alpha$.

So A-3, B-4, C-2, D-1. Check B at $\theta = 0$: $r = 2a$, $p = 2a$, and $\frac{(2a)^3}{2a} = 4a^2 = p^2$.""")

# ------------------------------------------------------ assertion-reason (5)
T.assertion_reason(1, ["envelopes"],
                   r"The envelope of the family of lines $x\cos\alpha + y\sin\alpha = a$ $(a > 0$ fixed, $\alpha$ the parameter$)$ is the circle $x^2 + y^2 = a^2$.",
                   r"Every line of the family is at distance $a$ from the origin.",
                   0,
                   r"""Both are true. The distance from $O$ to $x\cos\alpha + y\sin\alpha = a$ is $\frac{a}{\sqrt{\cos^2\alpha + \sin^2\alpha}} = a$, so every line touches the circle $x^2 + y^2 = a^2$; that circle is the envelope. Formally, $f_\alpha = -x\sin\alpha + y\cos\alpha = 0$, and squaring and adding with $f = 0$ gives $x^2 + y^2 = a^2$. R explains A.""")

T.assertion_reason(2, ["asymptotes"],
                   r"The parabola $y^2 = 4ax$ $(a > 0)$ has an asymptote parallel to the $x$-axis.",
                   r"An algebraic curve of degree $n$ has at most $n$ asymptotes.",
                   3,
                   r"""A is false. Asymptotes parallel to the $x$-axis come from the coefficient of the highest power of $x$; in $y^2 - 4ax$ that coefficient is the constant $-4a$, so there are none. Also $\frac yx \to 0$ but $y \to \infty$, so no line $y = c$ works: a parabola has no asymptotes at all.

R is a true standard result, but it only bounds the number from above. So A is false and R is true.""")

T.assertion_reason(1, ["curvature"],
                   r"The radius of curvature of the circle $x^2 + y^2 = a^2$ $(a > 0)$ is $a$ at every point.",
                   r"The curvature of a curve at a point is $\dfrac{ds}{d\psi}$.",
                   2,
                   r"""A is true: on a circle, $s = a\psi$ (up to a constant), so $\rho = \frac{ds}{d\psi} = a$.

R is false: curvature is $\kappa = \frac{d\psi}{ds}$, the rate of turning per unit arc. $\frac{ds}{d\psi}$ is the radius of curvature $\rho = \frac1\kappa$. For this circle $\kappa = \frac1a$, not $a$.""")

T.assertion_reason(3, ["polar-pedal"],
                   r"For the cardioid $r = a(1 + \cos\theta)$, the angle between the radius vector and the tangent is $\phi = \dfrac{\pi}{2} + \dfrac{\theta}{2}$.",
                   r"For the equiangular spiral $r = ae^{\theta\cot\alpha}$, the angle between the radius vector and the tangent is constant.",
                   1,
                   r"""A is true: $\tan\phi = \frac{r}{dr/d\theta} = \frac{1 + \cos\theta}{-\sin\theta} = -\cot\frac\theta2 = \tan\left(\frac\pi2 + \frac\theta2\right)$.

R is true: there $\tan\phi = \tan\alpha$. But R is about a different curve and says nothing about the cardioid; for the cardioid $\phi$ varies with $\theta$. Both true, R does not explain A.""")

T.assertion_reason(3, ["centre-of-curvature", "curve-tracing"],
                   r"For the folium $x^3 + y^3 = 3axy$ $(a > 0)$, the radius of curvature at the origin of the branch that touches the $x$-axis is $\dfrac{3a}{2}$.",
                   r"If a curve passes through the origin and touches the $x$-axis there, its radius of curvature at the origin is $\lim\limits_{x \to 0}\dfrac{x^2}{2y}$.",
                   0,
                   r"""R is Newton's formula, true. On the branch touching the $x$-axis, $y$ is small compared with $x$, so the dominant terms near $O$ are $x^3 = 3axy$, i.e. $y \approx \frac{x^2}{3a}$. Then
$$\rho = \lim\frac{x^2}{2y} = \lim\frac{x^2}{2x^2/(3a)} = \frac{3a}{2}.$$
So A is true, and it follows from R. (Check with the parametrisation $x = \frac{3at}{1 + t^3}$, $y = \frac{3at^2}{1 + t^3}$ at $t = 0$.)""")


def check():
    import sympy as sp
    x, y, t, th, m, c, al = sp.symbols("x y t theta m c alpha", real=True)
    a, b, k = sp.symbols("a b k", positive=True)

    def slope(F, pt):
        return (-sp.diff(F, x) / sp.diff(F, y)).subs({x: pt[0], y: pt[1]})

    # q1 tangent to y = x^3 at (1, 1)
    s = sp.diff(x**3, x).subs(x, 1)
    eq(1 + s * (x - 1), 3 * x - 2, "q1")
    # q2 normal to y^2 = 4x at (1, 2): x + y = 3
    s = slope(y**2 - 4 * x, (1, 2)); eq(s, 1, "q2 slope")
    eq(2 - (x - 1) / s, 3 - x, "q2")
    # q3 astroid intercept length
    X, Y = a * sp.cos(t)**3, a * sp.sin(t)**3
    sl = sp.diff(Y, t) / sp.diff(X, t)
    xi = sp.simplify(X - Y / sl); yi = sp.simplify(Y - sl * X)
    eq(xi, a * sp.cos(t), "q3 xi"); eq(yi, a * sp.sin(t), "q3 yi")
    eq(sp.simplify(xi**2 + yi**2), a**2, "q3")

    def tanphi(r):
        return r / sp.diff(r, th)

    def pedal_p2(r):
        return sp.simplify(1 / (1 / r**2 + sp.diff(r, th)**2 / r**4))

    # q4 cardioid 1 - cos: phi = theta/2
    for v in (0.3, 1.1, 2.5):
        eq(sp.N((tanphi(a * (1 - sp.cos(th))) - sp.tan(th / 2)).subs({th: v, a: 2})), 0, "q4")
    # q5 spiral
    eq(tanphi(a * sp.exp(th * sp.cot(al))), sp.tan(al), "q5")
    # q6 parabola with focus pole: r = 2a/(1 - cos), p^2 = a r
    r = 2 * a / (1 - sp.cos(th))
    eq(pedal_p2(r) - a * r, 0, "q6")
    # cartesian cross-check: tangent at (a t^2, 2 a t) is x - t y + a t^2 = 0; focus (a, 0)
    pp = (a + a * t**2) / sp.sqrt(1 + t**2); rr = a * t**2 + a  # focal distance x + a
    eq(pp**2 - a * rr, 0, "q6 cart")
    # q7 asymptotes of (2x+3)/(x-1)
    f = (2 * x + 3) / (x - 1)
    eq(sp.limit(f, x, sp.oo), 2, "q7 h"); assert sp.limit(f, x, 1, "+") == sp.oo
    # q8
    f = (x**2 + 3 * x) / (x - 1)
    eq(sp.limit(f / x, x, sp.oo), 1, "q8 m"); eq(sp.limit(f - x, x, sp.oo), 4, "q8")

    def oblique(F, n):
        """simple-root oblique asymptotes (m, c) of F(x, y) of degree n."""
        P = sp.Poly(sp.expand(F), x, y)
        phi = {d: sp.S(0) + sum(cf * m**j for (i, j), cf in P.terms() if i + j == d) for d in range(n + 1)}
        out = []
        for mm in sp.solve(phi[n], m):
            if mm.is_real and sp.diff(phi[n], m).subs(m, mm) != 0:
                out.append((mm, sp.simplify(-phi[n - 1].subs(m, mm) / sp.diff(phi[n], m).subs(m, mm))))
        return phi, out

    def is_asym(F, n, mm, cc):
        """coefficients of x^n and x^(n-1) vanish after y = m x + c."""
        p = sp.Poly(sp.expand(F.subs(y, mm * x + cc)), x)
        return p.degree() <= n - 2

    # q9 folium
    Ff = x**3 + y**3 - 3 * a * x * y
    _, o = oblique(Ff, 3)
    assert o == [(-1, -a)], o
    assert is_asym(Ff, 3, -1, -a) and not is_asym(Ff, 3, -1, a)
    # q10
    F = x**3 - 6 * x**2 * y + 11 * x * y**2 - 6 * y**3 + x + y + 1
    _, o = oblique(F, 3)
    assert sorted(o) == sorted([(1, 0), (sp.Rational(1, 2), 0), (sp.Rational(1, 3), 0)]), o
    assert not is_asym(F, 3, 2, 0)
    # q11 parallel asymptotes
    F = (x - y)**2 * (x + y) - 8 * x
    phi, o = oblique(F, 3)
    assert o == [(-1, 0)], o
    cs = sp.solve(c**2 / 2 * sp.diff(phi[3], m, 2).subs(m, 1) + c * sp.diff(phi[2], m).subs(m, 1) + phi[1].subs(m, 1), c)
    assert sorted(cs) == [-2, 2], cs
    for cc in (2, -2):  # numeric: branch near y = x + cc at large x
        X0 = 10**4
        yy = sp.nsolve(F.subs(x, X0), y, X0 + cc)
        assert abs(yy - X0 - cc) < 1e-3
    # q12: x^2y^2 - a^2(x^2+y^2): coefficient of x^2 is y^2 - a^2, of y^2 is x^2 - a^2
    F = x**2 * y**2 - a**2 * (x**2 + y**2)
    assert sp.factor(sp.Poly(F, x).coeff_monomial(x**2)) == sp.factor(y**2 - a**2)
    assert sp.factor(sp.Poly(F, y).coeff_monomial(y**2)) == sp.factor(x**2 - a**2)
    assert sp.solve(sp.Poly(F, x, y).as_expr().subs({x: 1, y: m}).coeff(a, 0), m) == [0]
    # vertical asymptote check numerically: y^2 = a^2 x^2/(x^2 - a^2) -> inf as x -> a+
    assert sp.limit(x**2 / (x**2 - 1), x, 1, "+") == sp.oo

    def rho_cart(f, pt):
        y1, y2 = sp.diff(f, x), sp.diff(f, x, 2)
        return sp.simplify(((1 + y1**2)**sp.Rational(3, 2) / sp.Abs(y2)).subs(x, pt))

    # q13
    eq(rho_cart(x**2, 0), sp.Rational(1, 2), "q13")
    # q14 catenary
    y1 = sp.sinh(x / k); y2 = sp.cosh(x / k) / k
    eq(sp.simplify((sp.cosh(x / k)**3) / y2 - (k * sp.cosh(x / k))**2 / k), 0, "q14 identity")
    eq(sp.simplify(1 + y1**2 - sp.cosh(x / k)**2), 0, "q14 1+y1^2")
    eq(rho_cart(k * sp.cosh(x / k), sp.Rational(7, 5)), (k * sp.cosh(sp.Rational(7, 5) / k))**2 / k, "q14")

    # q15 cardioid polar formula
    r = a * (1 + sp.cos(th)); r1 = sp.diff(r, th); r2 = sp.diff(r, th, 2)
    rho = (r**2 + r1**2)**sp.Rational(3, 2) / (r**2 + 2 * r1**2 - r * r2)
    for v in (0, sp.Rational(1, 3), -1, 2.5):
        eq(sp.N(rho.subs({th: v, a: 1})), sp.N(sp.Rational(4, 3) * sp.cos(sp.S(v) / 2)), "q15")
    # and pedal cross-check p^2 = r^3/(2a)
    eq(pedal_p2(r) - r**3 / (2 * a), 0, "q15 pedal")
    # q16 centre of curvature
    f = x**2; Y1 = sp.diff(f, x).subs(x, 1); Y2 = sp.diff(f, x, 2).subs(x, 1)
    eq(1 - Y1 * (1 + Y1**2) / Y2, -4, "q16 x"); eq(1 + (1 + Y1**2) / Y2, sp.Rational(7, 2), "q16 y")
    eq(sp.sqrt(25 + sp.Rational(25, 4)), rho_cart(f, 1), "q16 rho")

    def envelope_quad(Fam, p):
        P = sp.Poly(sp.expand(Fam), p)
        A, B, C = [P.coeff_monomial(p**i) for i in (2, 1, 0)]
        return sp.expand(B**2 - 4 * A * C)

    # q17
    eq(envelope_quad(sp.expand(x * m**2 - y * m + a), m), y**2 - 4 * a * x, "q17")
    # q18 cissoid: coefficient of y^2 is 2a - x; limit
    F = y**2 * (2 * a - x) - x**3
    eq(sp.Poly(F, y).coeff_monomial(y**2), 2 * a - x, "q18")
    assert sp.limit(x**3 / (2 - x), x, 2, "-") == sp.oo
    # q19 lemniscate tangents
    sols = sp.solve(sp.cos(2 * th), th)
    assert sp.pi / 4 in sols
    Fl = sp.expand((x**2 + y**2)**2 - a**2 * (x**2 - y**2))
    low = sum(cf * x**i * y**j for (i, j), cf in sp.Poly(Fl, x, y).terms() if i + j == 2)
    eq(sp.factor(low), -a**2 * (x - y) * (x + y), "q19")
    # q20 hyperbolic spiral
    eq(sp.limit(a * sp.sin(th) / th, th, 0, "+"), a, "q20")
    assert sp.limit(a * sp.cos(th) / th, th, 0, "+") == sp.oo

    # S1 statements
    assert sp.limit(sp.exp(x), x, -sp.oo) == 0
    eq(sp.Poly(x * y - c**2, x).coeff_monomial(x), y, "S1 xy")
    # S2: line curvature 0; parabola vertex rho = 2a; y = x^3 curvature 0 at 0
    eq(sp.diff(3 * x + 1, x, 2), 0, "S2 line")
    eq(sp.limit((4 * a * x) / (2 * x), x, 0), 2 * a, "S2 parabola")
    Xp, Yp = a * t**2, 2 * a * t   # parametric cross-check at t = 0
    num = (sp.diff(Xp, t)**2 + sp.diff(Yp, t)**2)**sp.Rational(3, 2)
    den = sp.Abs(sp.diff(Xp, t) * sp.diff(Yp, t, 2) - sp.diff(Yp, t) * sp.diff(Xp, t, 2))
    eq(sp.simplify((num / den).subs(t, 0)), 2 * a, "S2 parabola param")
    eq(sp.diff(x**3, x, 2).subs(x, 0), 0, "S2 cubic")
    # S3: lowest-degree terms
    def lowest(F):
        P = sp.Poly(sp.expand(F), x, y); d = min(i + j for (i, j), _ in P.terms())
        return sp.factor(sum(cf * x**i * y**j for (i, j), cf in P.terms() if i + j == d))
    eq(lowest(Ff), -3 * a * x * y, "S3 folium")
    eq(lowest(y**2 * (2 * a - x) - x**3), 2 * a * y**2, "S3 cissoid")
    eq(lowest(y**2 - x**2 * (x - 1)), x**2 + y**2, "S3 isolated")
    assert sp.solve(x**2 + 1, x) == [] or all(not s.is_real for s in sp.solve(x**2 + 1, x))

    # M1 envelopes
    # A
    sol = sp.solve([x * sp.cos(al) + y * sp.sin(al) - k, -x * sp.sin(al) + y * sp.cos(al)], [x, y], dict=True)[0]
    eq(sp.simplify(sol[x]**2 + sol[y]**2), k**2, "M1 A")
    # B: a + b = c
    xp, yp, A_ = sp.symbols("xp yp A_", positive=True)
    Fb = xp / A_ + yp / (k - A_) - 1
    Asol = k * sp.sqrt(xp) / (sp.sqrt(xp) + sp.sqrt(yp))
    eq(sp.simplify(sp.diff(Fb, A_).subs(A_, Asol)), 0, "M1 B da")
    eq(sp.simplify(Fb.subs(A_, Asol).subs(k, (sp.sqrt(xp) + sp.sqrt(yp))**2)), 0, "M1 B")
    # C: ab = c^2 -> y a^2 - c^2 a + c^2 x = 0
    eq(envelope_quad(y * A_**2 - k**2 * A_ + k**2 * x, A_), k**4 - 4 * k**2 * x * y, "M1 C")
    # D: astroid
    Fd = x / sp.cos(al) + y / sp.sin(al) - k
    sol = sp.solve([Fd, sp.diff(Fd, al)], [x, y], dict=True)[0]
    eq(sp.simplify(sol[x] - k * sp.cos(al)**3), 0, "M1 D x"); eq(sp.simplify(sol[y] - k * sp.sin(al)**3), 0, "M1 D y")
    # M2 pedal equations
    r = 2 * a * sp.cos(th); eq(sp.simplify(pedal_p2(r) - (r**2 / (2 * a))**2), 0, "M2 A")
    r = a * (1 + sp.cos(th)); eq(pedal_p2(r) - r**3 / (2 * a), 0, "M2 B")
    r = a * sp.sqrt(sp.cos(2 * th))
    for v in (sp.Rational(1, 5), sp.Rational(1, 2)):
        eq(sp.N(pedal_p2(r).subs({th: v, a: 1})), sp.N((r**3 / a**2).subs({th: v, a: 1})**2), "M2 C")
    r = a * sp.exp(th * sp.cot(al))
    eq(sp.simplify(pedal_p2(r) - r**2 * sp.sin(al)**2), 0, "M2 D")

    # AR1: distance from origin = k
    eq(k / sp.sqrt(sp.cos(al)**2 + sp.sin(al)**2), k, "AR1")
    # AR2: parabola has no asymptote: y/x -> 0 but y -> oo
    yb = 2 * sp.sqrt(a * x)
    assert sp.limit(yb / x, x, sp.oo) == 0 and sp.limit(yb, x, sp.oo) == sp.oo
    # AR3: circle rho = a
    eq(sp.simplify(rho_cart(sp.sqrt(a**2 - x**2), a / 2)), a, "AR3")
    # AR4: cardioid phi = pi/2 + theta/2
    eq(sp.N((tanphi(1 + sp.cos(th)) - sp.tan(sp.pi / 2 + th / 2)).subs(th, 0.7)), 0, "AR4")
    # AR5: folium curvature at origin via parametrisation
    Xf, Yf = 3 * a * t / (1 + t**3), 3 * a * t**2 / (1 + t**3)
    num = (sp.diff(Xf, t)**2 + sp.diff(Yf, t)**2)**sp.Rational(3, 2)
    den = sp.diff(Xf, t) * sp.diff(Yf, t, 2) - sp.diff(Yf, t) * sp.diff(Xf, t, 2)
    eq(sp.simplify((num / den).subs(t, 0)), 3 * a / 2, "AR5")
    eq(sp.limit(x**2 / (2 * x**2 / (3 * a)), x, 0), 3 * a / 2, "AR5 newton")


T.write(check)
