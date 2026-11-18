import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.integral.area-length-volume")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["cartesian-area"], r"The area of the region bounded by $y = x$ and $y = x^2$ is",
         [r"$\tfrac16$", r"$\tfrac13$", r"$\tfrac12$", r"$\tfrac56$"],
         r"""The curves meet where $x = x^2$, i.e. at $x = 0$ and $x = 1$, and $x \ge x^2$ on $[0, 1]$. So
$$A = \int_0^1 (x - x^2)\,dx = \frac12 - \frac13 = \frac16.$$
$\frac13$ is only the area under $y = x^2$; $\frac56$ adds the two areas instead of subtracting.""")

T.single(1, ["polar-area"], r"The area enclosed by the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ is",
         [r"$6\pi$", r"$12\pi$", r"$3\pi$", r"$36\pi$"],
         r"""With $x = 3\cos t$, $y = 2\sin t$,
$$A = \int_0^{2\pi} x\,\dot y\,dt = \int_0^{2\pi} 6\cos^2 t\,dt = 6\pi = \pi ab, \quad a = 3,\ b = 2.$$
$36\pi$ uses $a^2 b^2$ in place of $ab$ (with $a = 3$, $b = 2$, $\pi a^2b^2 = 36\pi$); $12\pi$ doubles the true value.""")

T.single(1, ["polar-area"], r"The area enclosed by the cardioid $r = a(1 + \cos\theta)$ is",
         [r"$\dfrac{3\pi a^2}{2}$", r"$\dfrac{3\pi a^2}{4}$", r"$\pi a^2$", r"$3\pi a^2$"],
         r"""By symmetry about the initial line,
$$A = 2\cdot\frac12\int_0^\pi a^2(1 + \cos\theta)^2\,d\theta = a^2\left(\pi + 0 + \frac{\pi}{2}\right) = \frac{3\pi a^2}{2}.$$
$3\pi a^2$ forgets the factor $\frac12$ in $\frac12\int r^2\,d\theta$; $\frac{3\pi a^2}{4}$ integrates only over $[0, \pi]$ without doubling.""")

T.single(1, ["volume-revolution"], r"The region under $y = \sqrt{x}$, $0 \le x \le 4$, is revolved about the $x$-axis. The volume generated is",
         [r"$8\pi$", r"$16\pi$", r"$4\pi$", r"$\dfrac{16\pi}{3}$"],
         r"""Disc method:
$$V = \pi\int_0^4 y^2\,dx = \pi\int_0^4 x\,dx = \pi\cdot\frac{16}{2} = 8\pi.$$
$16\pi$ forgets the $\frac12$ from $\int x\,dx$; $\frac{16\pi}{3}$ is $\pi\int_0^4\sqrt x\,dx$, i.e. it uses $y$ instead of $y^2$.""")

T.single(1, ["arc-length"], r"The length of the arc of $y = \tfrac23 x^{3/2}$ from $x = 0$ to $x = 3$ is",
         [r"$\dfrac{14}{3}$", r"$\dfrac{16}{3}$", r"$2\sqrt3$", r"$\dfrac73$"],
         r"""$y' = x^{1/2}$, so $1 + y'^2 = 1 + x$ and
$$s = \int_0^3 \sqrt{1 + x}\,dx = \frac23\left[(1 + x)^{3/2}\right]_0^3 = \frac23(8 - 1) = \frac{14}{3}.$$
$\frac{16}{3}$ forgets to subtract the lower limit value $1$; $\frac73$ uses $\frac13$ in place of $\frac23$ when integrating $(1 + x)^{1/2}$.""")

T.single(1, ["arc-length"], r"The whole perimeter of the astroid $x^{2/3} + y^{2/3} = a^{2/3}$ is",
         [r"$6a$", r"$8a$", r"$4a$", r"$\dfrac{3\pi a}{2}$"],
         r"""With $x = a\cos^3 t$, $y = a\sin^3 t$: $\dot x^2 + \dot y^2 = 9a^2\sin^2 t\cos^2 t$, so in the first quadrant
$$s_1 = \int_0^{\pi/2} 3a\sin t\cos t\,dt = \frac{3a}{2},$$
and the perimeter is $4\cdot\frac{3a}{2} = 6a$.
$8a$ is the cardioid / cycloid-arch value. Integrating $3a\sin t\cos t$ over $[0, 2\pi]$ without absolute values gives $0$: the pieces cancel.""")

T.single(1, ["double-integrals"], r"$\displaystyle\int_0^1\!\int_0^2 xy\,dy\,dx$ equals",
         [r"$1$", r"$2$", r"$\tfrac12$", r"$4$"],
         r"""The integrand is a product and the region a rectangle, so it splits:
$$\int_0^1 x\,dx\cdot\int_0^2 y\,dy = \frac12\cdot 2 = 1.$$
$2$ forgets the $\frac12$ in $\int_0^1 x\,dx$; $4$ forgets both halves.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["cartesian-area"], r"The area enclosed between the parabolas $y^2 = 4ax$ and $x^2 = 4ay$ ($a > 0$) is",
         [r"$\dfrac{16a^2}{3}$", r"$\dfrac{8a^2}{3}$", r"$\dfrac{32a^2}{3}$", r"$\dfrac{4a^2}{3}$"],
         r"""They meet at $(0, 0)$ and $(4a, 4a)$; the upper curve is $y = 2\sqrt{ax}$:
$$A = \int_0^{4a}\left(2\sqrt a\,x^{1/2} - \frac{x^2}{4a}\right)dx = \frac{32a^2}{3} - \frac{16a^2}{3} = \frac{16a^2}{3}.$$
$\frac{32a^2}{3}$ is only the area under the upper parabola. Check: for $a = \frac14$ this is the standard $\frac13$ between $y^2 = x$ and $x^2 = y$, and $\frac{16}{3}\cdot\frac{1}{16} = \frac13$.""")

T.single(2, ["polar-area"], r"The area of one loop of $r = a\cos 2\theta$ is",
         [r"$\dfrac{\pi a^2}{8}$", r"$\dfrac{\pi a^2}{4}$", r"$\dfrac{\pi a^2}{2}$", r"$\dfrac{\pi a^2}{16}$"],
         r"""The loop on the initial line runs between the zeros $\theta = \pm\frac{\pi}{4}$:
$$A = \frac12\int_{-\pi/4}^{\pi/4} a^2\cos^2 2\theta\,d\theta = \frac{a^2}{2}\cdot\frac{\pi}{4} = \frac{\pi a^2}{8}.$$
$\frac{\pi a^2}{2}$ is the total of all **four** loops; $\frac{\pi a^2}{4}$ forgets the factor $\frac12$.""")

T.single(2, ["polar-area"], r"The area enclosed by the astroid $x = a\cos^3 t$, $y = a\sin^3 t$ is",
         [r"$\dfrac{3\pi a^2}{8}$", r"$\dfrac{3\pi a^2}{4}$", r"$\dfrac{3\pi a^2}{16}$", r"$\dfrac{\pi a^2}{8}$"],
         r"""Four times the first-quadrant area:
$$A = 4\int_0^a y\,dx = 4\int_{\pi/2}^{0} a\sin^3 t\cdot(-3a\cos^2 t\sin t)\,dt = 12a^2\int_0^{\pi/2}\sin^4 t\cos^2 t\,dt = 12a^2\cdot\frac{\pi}{32} = \frac{3\pi a^2}{8}.$$
$\frac{3\pi a^2}{16}$ uses a wrong Wallis value ($\frac{\pi}{64}$); $\frac{3\pi a^2}{4}$ doubles the answer.""")

T.single(2, ["polar-area"], r"The area between one arch of the cycloid $x = a(t - \sin t)$, $y = a(1 - \cos t)$ and its base is",
         [r"$3\pi a^2$", r"$2\pi a^2$", r"$4\pi a^2$", r"$\pi a^2$"],
         r"""$$A = \int_0^{2\pi} y\,\dot x\,dt = a^2\int_0^{2\pi}(1 - \cos t)^2\,dt = a^2(2\pi + \pi) = 3\pi a^2.$$
This is three times the area of the rolling circle. $2\pi a^2$ drops the $\int\cos^2 t\,dt = \pi$ term.""")

T.single(2, ["arc-length"], r"The length of one arch of the cycloid $x = a(t - \sin t)$, $y = a(1 - \cos t)$, $0 \le t \le 2\pi$, is",
         [r"$8a$", r"$4a$", r"$6a$", r"$2\pi a$"],
         r"""$\dot x^2 + \dot y^2 = a^2\left[(1 - \cos t)^2 + \sin^2 t\right] = 2a^2(1 - \cos t) = 4a^2\sin^2\frac t2$. On $[0, 2\pi]$, $\sin\frac t2 \ge 0$, so
$$s = \int_0^{2\pi} 2a\sin\frac t2\,dt = \left[-4a\cos\frac t2\right]_0^{2\pi} = 8a.$$
$4a$ is half an arch; $2\pi a$ is the base length, not the arc.""")

T.single(2, ["arc-length"], r"The whole length of the cardioid $r = a(1 + \cos\theta)$ is",
         [r"$8a$", r"$4a$", r"$16a$", r"$2\pi a$"],
         r"""$r^2 + r'^2 = a^2(1 + \cos\theta)^2 + a^2\sin^2\theta = 2a^2(1 + \cos\theta) = 4a^2\cos^2\frac\theta2$. Use the upper half and double:
$$s = 2\int_0^\pi 2a\cos\frac\theta2\,d\theta = 2\cdot 4a = 8a.$$
$4a$ is only the upper half. Integrating $2a\cos\frac\theta2$ over $[0, 2\pi]$ without $\lvert\cdot\rvert$ gives $0$.""")

T.single(2, ["arc-length"], r"For the catenary $y = c\cosh\dfrac{x}{c}$, the length of the arc from the vertex $(0, c)$ to the point with abscissa $x > 0$ is",
         [r"$c\sinh\dfrac xc$", r"$c\cosh\dfrac xc$", r"$c\left(\cosh\dfrac xc - 1\right)$", r"$\sinh\dfrac xc$"],
         r"""$y' = \sinh\frac xc$, so $1 + y'^2 = \cosh^2\frac xc$ and
$$s = \int_0^x \cosh\frac uc\,du = c\sinh\frac xc.$$
Hence $y^2 - s^2 = c^2$. $c\cosh\frac xc$ is the ordinate $y$, and $c(\cosh\frac xc - 1)$ is the rise $y - c$; $\sinh\frac xc$ drops the factor $c$ (wrong dimension).""")

T.single(2, ["volume-revolution"], r"The ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ is revolved about the $x$-axis. The volume of the ellipsoid generated is",
         [r"$\tfrac43\pi ab^2$", r"$\tfrac43\pi a^2 b$", r"$\tfrac23\pi ab^2$", r"$\tfrac43\pi a^3$"],
         r"""$$V = \pi\int_{-a}^{a} y^2\,dx = \pi b^2\int_{-a}^{a}\left(1 - \frac{x^2}{a^2}\right)dx = \pi b^2\cdot\frac{4a}{3} = \frac43\pi ab^2.$$
$\frac43\pi a^2 b$ is the volume about the $y$-axis. Check: $a = b$ gives the sphere $\frac43\pi a^3$.""")

T.single(2, ["volume-revolution"], r"The region bounded by $y = x$ and $y = x^2$ is revolved about the $x$-axis. The volume generated is",
         [r"$\dfrac{2\pi}{15}$", r"$\dfrac{\pi}{30}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{3}$"],
         r"""Washers with outer radius $x$ and inner radius $x^2$ on $[0, 1]$:
$$V = \pi\int_0^1 (x^2 - x^4)\,dx = \pi\left(\frac13 - \frac15\right) = \frac{2\pi}{15}.$$
$\frac{\pi}{30} = \pi\int_0^1 (x - x^2)^2\,dx$ squares the difference instead of taking the difference of squares; $\frac{\pi}{6}$ is $\pi\times$ the plane area.""")

T.single(2, ["surface-revolution"], r"The arc of $x^2 + y^2 = 25$, $y \ge 0$, from $x = 0$ to $x = 3$ is revolved about the $x$-axis. The area of the surface generated is",
         [r"$30\pi$", r"$15\pi$", r"$50\pi$", r"$60\pi$"],
         r"""For $y = \sqrt{25 - x^2}$, $y\sqrt{1 + y'^2} = \sqrt{25 - x^2}\cdot\frac{5}{\sqrt{25 - x^2}} = 5$, so
$$S = 2\pi\int_0^3 5\,dx = 30\pi = 2\pi a h, \quad a = 5,\ h = 3.$$
$50\pi$ is the hemisphere ($h = 5$); $15\pi$ forgets the $2$ in $2\pi\int y\,ds$.""")

T.single(2, ["double-integrals"], r"$\displaystyle\int_0^1\!\int_x^1 e^{y^2}\,dy\,dx$ equals",
         [r"$\dfrac{e - 1}{2}$", r"$e - 1$", r"$\dfrac{e + 1}{2}$", r"$\dfrac{e}{2}$"],
         r"""$\int e^{y^2}dy$ is not elementary, so reverse the order. The region $0 \le x \le 1$, $x \le y \le 1$ is $0 \le y \le 1$, $0 \le x \le y$:
$$\int_0^1\!\int_0^y e^{y^2}\,dx\,dy = \int_0^1 y\,e^{y^2}\,dy = \left[\frac{e^{y^2}}{2}\right]_0^1 = \frac{e - 1}{2}.$$
$e - 1$ forgets the $\frac12$; $\frac e2$ forgets the lower limit term $\frac12$.""")

T.single(3, ["double-integrals"], r"If $D$ is the disc $x^2 + y^2 \le a^2$, then $\displaystyle\iint_D e^{-(x^2 + y^2)}\,dx\,dy$ equals",
         [r"$\pi\left(1 - e^{-a^2}\right)$", r"$2\pi\left(1 - e^{-a^2}\right)$", r"$\pi\left(1 - e^{-a}\right)$", r"$\pi a^2 e^{-a^2}$"],
         r"""Polar substitution, $dx\,dy = r\,dr\,d\theta$:
$$\int_0^{2\pi}\!\int_0^a e^{-r^2}\,r\,dr\,d\theta = 2\pi\left[-\frac{e^{-r^2}}{2}\right]_0^a = \pi\left(1 - e^{-a^2}\right).$$
$2\pi(1 - e^{-a^2})$ forgets the $\frac12$ from $\int r e^{-r^2}dr$. As $a \to \infty$ the value tends to $\pi$, the square of the Gaussian integral.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["surface-revolution"], r"The cardioid $r = a(1 + \cos\theta)$ is revolved about its axis (the initial line). The area of the surface generated is",
         [r"$\dfrac{32\pi a^2}{5}$", r"$\dfrac{16\pi a^2}{5}$", r"$\dfrac{64\pi a^2}{5}$", r"$\dfrac{32\pi a^2}{3}$"],
         r"""Use the upper half, $0 \le \theta \le \pi$. With $r = 2a\cos^2\frac\theta2$: $ds = 2a\cos\frac\theta2\,d\theta$ and $y = r\sin\theta = 4a\cos^3\frac\theta2\sin\frac\theta2$. So
$$S = 2\pi\int_0^\pi 8a^2\cos^4\frac\theta2\sin\frac\theta2\,d\theta = 2\pi\cdot 16a^2\int_0^1 u^4\,du = \frac{32\pi a^2}{5} \quad \left(u = \cos\tfrac\theta2\right).$$
$\frac{64\pi a^2}{5}$ integrates over the whole curve, $[0, 2\pi]$, counting the surface twice; $\frac{16\pi a^2}{5}$ uses $\pi$ in place of $2\pi$.""")

T.single(3, ["cartesian-area"], r"The area of the loop of the curve $ay^2 = x^2(a - x)$, $a > 0$, is",
         [r"$\dfrac{8a^2}{15}$", r"$\dfrac{4a^2}{15}$", r"$\dfrac{16a^2}{15}$", r"$\dfrac{8a^2}{5}$"],
         r"""The loop is $0 \le x \le a$, symmetric about the $x$-axis, with $y = \pm x\sqrt{1 - x/a}$. With $u = a - x$:
$$A = 2\int_0^a x\sqrt{1 - \frac xa}\,dx = \frac{2}{\sqrt a}\int_0^a (a - u)\,u^{1/2}\,du = \frac{2}{\sqrt a}\left(\frac{2a^{5/2}}{3} - \frac{2a^{5/2}}{5}\right) = \frac{8a^2}{15}.$$
$\frac{4a^2}{15}$ is only the half above the $x$-axis.""")

# ---------------------------------------------------------------- statements
T.statements(3, ["polar-area"],
             r"Consider the following statements about areas of polar curves ($a > 0$):",
             [r"The area of one loop of $r = a\cos 2\theta$ is $\dfrac{\pi a^2}{8}$.",
              r"The total area enclosed by all the loops of $r = a\sin 3\theta$ is $\dfrac{\pi a^2}{2}$.",
              r"The total area enclosed by both loops of the lemniscate $r^2 = a^2\cos 2\theta$ is $a^2$."],
             [r"1 and 3 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** $\frac12\int_{-\pi/4}^{\pi/4} a^2\cos^2 2\theta\,d\theta = \frac{\pi a^2}{8}$.
- **2 is false:** one loop ($0 \le \theta \le \frac\pi3$) has area $\frac{\pi a^2}{12}$, and there are 3 loops, so the total is $\frac{\pi a^2}{4}$. The value $\frac{\pi a^2}{2} = \frac12\int_0^{2\pi} a^2\sin^2 3\theta\,d\theta$ traces every loop twice (odd $n$).
- **3 is true:** one loop is $\frac12\int_{-\pi/4}^{\pi/4} a^2\cos 2\theta\,d\theta = \frac{a^2}{2}$, so both loops give $a^2$.""")

T.statements(3, ["double-integrals"],
             r"Consider the following statements about double integrals:",
             [r"For continuous $f$, $\displaystyle\int_0^1\!\int_0^x f(x, y)\,dy\,dx = \int_0^1\!\int_y^1 f(x, y)\,dx\,dy$.",
              r"Under $x = r\cos\theta$, $y = r\sin\theta$, the area element $dx\,dy$ becomes $r\,dr\,d\theta$.",
              r"For $f(x, y) = \dfrac{x - y}{(x + y)^3}$, $\displaystyle\int_0^1\!\int_0^1 f\,dy\,dx = \int_0^1\!\int_0^1 f\,dx\,dy$."],
             [r"1 and 2 only", r"1 and 3 only", r"2 only", r"1, 2 and 3"],
             r"""- **1 is true:** the region $0 \le y \le x \le 1$ is the triangle described either way, and $f$ is continuous, so Fubini applies.
- **2 is true:** $\dfrac{\partial(x, y)}{\partial(r, \theta)} = \begin{vmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{vmatrix} = r$.
- **3 is false:** $\int_0^1 f\,dy = \frac{1}{(1 + x)^2}$, so the first order gives $\frac12$; by antisymmetry the other order gives $-\frac12$. $f$ is unbounded near $(0, 0)$ and $\iint\lvert f\rvert = \infty$, so Fubini does not apply.""")

# ---------------------------------------------------------------- match
T.match(2, ["polar-area"], r"Match each region in List I with its area in List II ($a, b > 0$).",
        [r"Interior of $x = a\cos t$, $y = b\sin t$", r"Interior of $r = a(1 + \cos\theta)$",
         r"Interior of $x = a\cos^3 t$, $y = a\sin^3 t$", r"Under one arch of $x = a(t - \sin t)$, $y = a(1 - \cos t)$"],
        [r"$3\pi a^2$", r"$\pi ab$", r"$\dfrac{3\pi a^2}{8}$", r"$\dfrac{3\pi a^2}{2}$"],
        [r"A-2, B-4, C-3, D-1", r"A-2, B-1, C-3, D-4", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1"],
        r"""- A: ellipse, $\pi ab$: **2**.
- B: cardioid, $\frac12\int_0^{2\pi}a^2(1 + \cos\theta)^2\,d\theta = \frac{3\pi a^2}{2}$: **4**.
- C: astroid, $\frac{3\pi a^2}{8}$: **3**.
- D: cycloid arch, $a^2\int_0^{2\pi}(1 - \cos t)^2\,dt = 3\pi a^2$: **1**.

So A-2, B-4, C-3, D-1. The cardioid ($\frac32\pi a^2$) and cycloid ($3\pi a^2$) are the pair most often swapped.""")

T.match(3, ["arc-length"], r"Match each arc in List I with its length in List II ($a, c > 0$).",
        [r"The whole astroid $x^{2/3} + y^{2/3} = a^{2/3}$", r"The whole cardioid $r = a(1 + \cos\theta)$",
         r"The whole circle $r = 2a\cos\theta$", r"The catenary $y = c\cosh\frac xc$ from $x = -c$ to $x = c$"],
        [r"$2c\sinh 1$", r"$2\pi a$", r"$6a$", r"$8a$"],
        [r"A-3, B-4, C-2, D-1", r"A-4, B-3, C-2, D-1", r"A-3, B-4, C-1, D-2", r"A-3, B-2, C-4, D-1"],
        r"""- A: astroid, $4\cdot\frac{3a}{2} = 6a$: **3**.
- B: cardioid, $2\int_0^\pi 2a\cos\frac\theta2\,d\theta = 8a$: **4**.
- C: $r = 2a\cos\theta$ is a circle of radius $a$; $\sqrt{r^2 + r'^2} = 2a$ over $-\frac\pi2 \le \theta \le \frac\pi2$ gives $2\pi a$: **2**.
- D: $s = \int_{-c}^{c}\cosh\frac xc\,dx = 2c\sinh 1$: **1**.

So A-3, B-4, C-2, D-1. Swapping $6a$ and $8a$ is the usual slip.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["surface-revolution"],
                   r"The volume of the torus generated by revolving the disc $(x - 2)^2 + y^2 \le 1$ about the $y$-axis is $4\pi^2$.",
                   r"The volume of a solid of revolution equals the area of the revolving region times the distance travelled by its centroid, provided the region lies on one side of the axis.",
                   0,
                   r"""**R is true:** it is Pappus's theorem for volumes.

**A is true, and R explains it:** the disc has area $\pi$ and centroid $(2, 0)$, at distance $2$ from the axis, and it lies in $x \ge 1 > 0$. So
$$V = \pi\cdot 2\pi\cdot 2 = 4\pi^2 \;(= 2\pi^2 a^2 b,\ a = 1,\ b = 2).$$""")

T.assertion_reason(3, ["polar-area"],
                   r"The area of one loop of $r = a\sin 3\theta$ is $\dfrac{\pi a^2}{12}$.",
                   r"The curve $r = a\sin 3\theta$ is symmetric about the line $\theta = \dfrac{\pi}{2}$.",
                   1,
                   r"""**A is true:** the loop $0 \le \theta \le \frac\pi3$ gives
$$\frac12\int_0^{\pi/3} a^2\sin^2 3\theta\,d\theta = \frac{a^2}{2}\cdot\frac{\pi}{6} = \frac{\pi a^2}{12}.$$

**R is true:** $a\sin 3(\pi - \theta) = a\sin(3\pi - 3\theta) = a\sin 3\theta$, so $(r, \theta) \mapsto (r, \pi - \theta)$ maps the curve to itself.

**But R does not explain A.** The area comes from integrating $\frac12 r^2$ between consecutive zeros of $r$; the symmetry plays no part.""")

T.assertion_reason(2, ["arc-length"],
                   r"The length of the arc of $y = \cosh x$ from $x = 0$ to $x = 1$ is $\sinh 1$.",
                   r"For a continuously differentiable $y = f(x)$, the arc length from $x = a$ to $x = b$ is $\displaystyle\int_a^b \big(1 + f'(x)\big)\,dx$.",
                   2,
                   r"""**A is true:** $\sqrt{1 + \sinh^2 x} = \cosh x$, so $s = \int_0^1\cosh x\,dx = \sinh 1$.

**R is false:** the correct integrand is $\sqrt{1 + f'(x)^2}$. Here R would give $\int_0^1 (1 + \sinh x)\,dx = \cosh 1 \ne \sinh 1$.""")

T.assertion_reason(1, ["cartesian-area", "exam-tips"],
                   r"The area of the region between $y = \sin x$ and the $x$-axis for $0 \le x \le 2\pi$ is $0$.",
                   r"$\displaystyle\int_0^{2\pi}\sin x\,dx = 0$.",
                   3,
                   r"""**A is false:** area is never negative. Split at the zero $x = \pi$:
$$A = \int_0^{\pi}\sin x\,dx + \left\lvert\int_\pi^{2\pi}\sin x\,dx\right\rvert = 2 + 2 = 4.$$

**R is true:** $[-\cos x]_0^{2\pi} = 0$. It is a signed area; the parts above and below the axis cancel.""")

T.assertion_reason(3, ["volume-revolution"],
                   r"The volume of the solid generated by revolving the cardioid $r = a(1 + \cos\theta)$ about the initial line is $\dfrac{8\pi a^3}{3}$.",
                   r"The volume generated by revolving the polar region $0 \le r \le f(\theta)$, $\alpha \le \theta \le \beta$ (with $0 \le \alpha < \beta \le \pi$), about the initial line is $\dfrac{2\pi}{3}\displaystyle\int_\alpha^\beta r^3\sin\theta\,d\theta$.",
                   0,
                   r"""**R is true:** it is the standard polar volume formula (an elementary sector of radius $r$ generates a volume $\frac{2\pi}{3}r^3\sin\theta\,d\theta$).

**A is true, and R explains it:** the upper half $0 \le \theta \le \pi$ generates the whole solid. With $u = 1 + \cos\theta$:
$$V = \frac{2\pi a^3}{3}\int_0^\pi (1 + \cos\theta)^3\sin\theta\,d\theta = \frac{2\pi a^3}{3}\int_0^2 u^3\,du = \frac{2\pi a^3}{3}\cdot 4 = \frac{8\pi a^3}{3}.$$""")


def check():
    import sympy as sp
    x, y, t, th, u, r = sp.symbols("x y t theta u r", real=True)
    a, b, c = sp.symbols("a b c", positive=True)
    pi, I_ = sp.pi, sp.integrate

    def num(label, got, want):
        eq(got, want, label)
        assert abs(float(sp.N(got.subs({a: 1.3, b: 0.7, c: 0.9}) if hasattr(got, "subs") else got)) -
                   float(sp.N(want.subs({a: 1.3, b: 0.7, c: 0.9}) if hasattr(want, "subs") else want))) < 1e-9, label

    def ne(label, got, *wrong):
        for w in wrong:
            assert sp.simplify(sp.sympify(got) - sp.sympify(w)) != 0, f"DISTRACTOR EQUALS KEY {label}: {w}"

    def polar_area(rr, lo, hi):
        return I_(sp.Rational(1, 2) * rr**2, (th, lo, hi))

    # q1
    num("q1", I_(x - x**2, (x, 0, 1)), sp.Rational(1, 6))
    # q2
    num("q2", I_(3 * sp.cos(t) * sp.diff(2 * sp.sin(t), t), (t, 0, 2 * pi)), 6 * pi)
    # q3
    k3 = polar_area(a * (1 + sp.cos(th)), 0, 2 * pi)
    num("q3", k3, 3 * pi * a**2 / 2)
    # q4
    num("q4", pi * I_(x, (x, 0, 4)), 8 * pi); ne("q4", 8 * pi, pi * I_(sp.sqrt(x), (x, 0, 4)))
    # q5
    num("q5", I_(sp.sqrt(1 + sp.diff(sp.Rational(2, 3) * x**sp.Rational(3, 2), x)**2), (x, 0, 3)), sp.Rational(14, 3))
    # q6 astroid perimeter (with abs via quadrant symmetry) + numeric full abs integral
    X, Y = a * sp.cos(t)**3, a * sp.sin(t)**3
    sp_ = sp.sqrt(sp.diff(X, t)**2 + sp.diff(Y, t)**2)
    num("q6", 4 * I_(3 * a * sp.sin(t) * sp.cos(t), (t, 0, pi / 2)), 6 * a)
    assert abs(sp.Integral(sp_.subs(a, 1), (t, 0, 2 * pi)).evalf() - 6) < 1e-8, "q6 numeric"
    # q7
    num("q7", I_(I_(x * y, (y, 0, 2)), (x, 0, 1)), 1)
    # q8
    num("q8", I_(2 * sp.sqrt(a * x) - x**2 / (4 * a), (x, 0, 4 * a)), 16 * a**2 / 3)
    # q9
    num("q9", polar_area(a * sp.cos(2 * th), -pi / 4, pi / 4), pi * a**2 / 8)
    num("q9 total", polar_area(a * sp.cos(2 * th), 0, 2 * pi), pi * a**2 / 2)
    # q10 astroid area
    num("q10", 4 * I_(Y * (-sp.diff(X, t)), (t, 0, pi / 2)), 3 * pi * a**2 / 8)
    # q11 cycloid area
    Xc, Yc = a * (t - sp.sin(t)), a * (1 - sp.cos(t))
    num("q11", I_(Yc * sp.diff(Xc, t), (t, 0, 2 * pi)), 3 * pi * a**2)
    # q12 cycloid length
    num("q12", I_(2 * a * sp.sin(t / 2), (t, 0, 2 * pi)), 8 * a)
    eq(sp.simplify(sp.diff(Xc, t)**2 + sp.diff(Yc, t)**2 - 4 * a**2 * sp.sin(t / 2)**2), 0, "q12 ds")
    assert abs(sp.Integral(sp.sqrt(sp.diff(Xc, t)**2 + sp.diff(Yc, t)**2).subs(a, 1), (t, 0, 2 * pi)).evalf() - 8) < 1e-8
    # q13 cardioid length
    rc = a * (1 + sp.cos(th))
    eq(sp.simplify(rc**2 + sp.diff(rc, th)**2 - 4 * a**2 * sp.cos(th / 2)**2), 0, "q13 ds")
    num("q13", 2 * I_(2 * a * sp.cos(th / 2), (th, 0, pi)), 8 * a)
    assert abs(sp.Integral(sp.sqrt(rc**2 + sp.diff(rc, th)**2).subs(a, 1), (th, 0, 2 * pi)).evalf() - 8) < 1e-8
    # q14 catenary
    xs = sp.symbols("xs", positive=True)
    s14 = I_(sp.sqrt(1 + sp.diff(c * sp.cosh(x / c), x)**2).rewrite(sp.exp), (x, 0, xs))
    assert abs(sp.N((s14 - c * sp.sinh(xs / c)).subs({c: 0.9, xs: 1.7}))) < 1e-9, "q14"
    # q15 ellipsoid
    num("q15", pi * I_(b**2 * (1 - x**2 / a**2), (x, -a, a)), sp.Rational(4, 3) * pi * a * b**2)
    ne("q15", sp.Rational(4, 3) * pi * a * b**2, sp.Rational(4, 3) * pi * a**2 * b)
    # q16 washer
    num("q16", pi * I_(x**2 - x**4, (x, 0, 1)), 2 * pi / 15)
    eq(pi * I_((x - x**2)**2, (x, 0, 1)), pi / 30, "q16 distractor")
    # q17 spherical zone
    ys = sp.sqrt(25 - x**2)
    num("q17", 2 * pi * I_(sp.simplify(ys * sp.sqrt(1 + sp.diff(ys, x)**2)), (x, 0, 3)), 30 * pi)
    # q18 reversed order
    num("q18", I_(I_(sp.exp(y**2), (x, 0, y)), (y, 0, 1)), (sp.E - 1) / 2)
    import mpmath as mp
    assert abs(mp.quad(lambda X: mp.quad(lambda Y: mp.e**(Y**2), [X, 1]), [0, 1]) - (mp.e - 1) / 2) < 1e-9, "q18 numeric"
    # q19 polar Gaussian
    num("q19", I_(I_(sp.exp(-r**2) * r, (r, 0, a)), (th, 0, 2 * pi)), pi * (1 - sp.exp(-a**2)))
    assert abs(mp.quad(lambda X: mp.quad(lambda Y: mp.e**(-(X**2 + Y**2)), [-mp.sqrt(1 - X**2), mp.sqrt(1 - X**2)]), [-1, 1])
               - mp.pi * (1 - mp.e**-1)) < 1e-8, "q19 numeric"
    # q20 cardioid surface
    yy = rc * sp.sin(th)
    S20 = 2 * pi * sp.Integral((yy * sp.sqrt(rc**2 + sp.diff(rc, th)**2)).subs(a, 1), (th, 0, pi)).evalf()
    assert abs(S20 - sp.N(32 * pi / 5)) < 1e-8, "q20 numeric"
    num("q20", 2 * pi * I_(8 * a**2 * sp.cos(th / 2)**4 * sp.sin(th / 2), (th, 0, pi)), 32 * pi * a**2 / 5)
    # q21 loop
    num("q21", 2 * I_(x * sp.sqrt(1 - x / a), (x, 0, a)), 8 * a**2 / 15)
    # q22 statements: 1 T, 2 F, 3 T
    eq(polar_area(a * sp.sin(3 * th), 0, pi / 3), pi * a**2 / 12, "q22 loop")
    eq(3 * polar_area(a * sp.sin(3 * th), 0, pi / 3), pi * a**2 / 4, "q22 total")
    ne("q22 stmt2", pi * a**2 / 4, pi * a**2 / 2)
    eq(polar_area(a * sp.cos(2 * th), -pi / 4, pi / 4), pi * a**2 / 8, "q22 stmt1")
    eq(2 * I_(sp.Rational(1, 2) * a**2 * sp.cos(2 * th), (th, -pi / 4, pi / 4)), a**2, "q22 stmt3")
    # q23 statements: 1 T, 2 T, 3 F
    f = sp.exp(x) * y**2 + x * y
    eq(I_(I_(f, (y, 0, x)), (x, 0, 1)), I_(I_(f, (x, y, 1)), (y, 0, 1)), "q23 stmt1")
    eq(sp.simplify(sp.Matrix([r * sp.cos(th), r * sp.sin(th)]).jacobian([r, th]).det()), r, "q23 stmt2")
    g = (x - y) / (x + y)**3
    o1 = I_(I_(g, (y, 0, 1)), (x, 0, 1)); o2 = I_(I_(g, (x, 0, 1)), (y, 0, 1))
    eq(o1, sp.Rational(1, 2), "q23 o1"); eq(o2, -sp.Rational(1, 2), "q23 o2")
    # q24 match areas
    eq(polar_area(a * (1 + sp.cos(th)), 0, 2 * pi), 3 * pi * a**2 / 2, "q24 B")
    eq(I_(a * sp.cos(t) * sp.diff(b * sp.sin(t), t), (t, 0, 2 * pi)), pi * a * b, "q24 A")
    # q25 match lengths
    rr = 2 * a * sp.cos(th)
    eq(I_(sp.sqrt(sp.simplify(rr**2 + sp.diff(rr, th)**2)), (th, -pi / 2, pi / 2)), 2 * pi * a, "q25 C")
    eq(I_(sp.cosh(x / c), (x, -c, c)), 2 * c * sp.sinh(1), "q25 D")
    # q26 Pappus torus vs direct shell
    eq(pi * 1 * 2 * pi * 2, 4 * pi**2, "q26")
    eq(2 * pi * I_(x * 2 * sp.sqrt(1 - (x - 2)**2), (x, 1, 3)), 4 * pi**2, "q26 shell")
    # q27 symmetry and loop
    eq(sp.simplify(sp.sin(3 * (pi - th)) - sp.sin(3 * th)), 0, "q27 R")
    # q28
    eq(I_(sp.sqrt(1 + sp.sinh(x)**2).rewrite(sp.exp), (x, 0, 1)), sp.sinh(1), "q28 A")
    ne("q28 R", I_(1 + sp.sinh(x), (x, 0, 1)), sp.sinh(1))
    # q29
    eq(I_(sp.sin(x), (x, 0, 2 * pi)), 0, "q29 R")
    eq(I_(sp.Abs(sp.sin(x)), (x, 0, 2 * pi)), 4, "q29 A")
    # q30 cardioid volume, plus cross-check by discs in Cartesian (numeric)
    eq(sp.Rational(2, 3) * pi * I_(rc**3 * sp.sin(th), (th, 0, pi)), 8 * pi * a**3 / 3, "q30")
    # disc method parametrically: V = pi * |∫ y^2 dx| over upper half
    xp, yp = (rc * sp.cos(th)).subs(a, 1), (rc * sp.sin(th)).subs(a, 1)
    Vd = sp.Integral(pi * yp**2 * sp.diff(xp, th), (th, 0, pi)).evalf()
    assert abs(abs(Vd) - sp.N(8 * pi / 3)) < 1e-8, f"q30 disc {Vd}"

    # extra facts stated in notes
    eq(pi * I_(Yc**2 * sp.diff(Xc, t), (t, 0, 2 * pi)), 5 * pi**2 * a**3, "notes cycloid volume")
    eq(2 * pi * I_(Yc * 2 * a * sp.sin(t / 2), (t, 0, 2 * pi)), sp.Rational(64, 3) * pi * a**2, "notes cycloid surface")
    pl = sp.Integral(sp.sqrt(1 + 1 / x), (x, 0, 1)).evalf()  # y^2 = 4x, a = 1
    assert abs(pl - sp.N(sp.sqrt(2) + sp.log(1 + sp.sqrt(2)))) < 1e-8, "notes parabola"
    eq(2 * pi * a * 2 * pi * b, 4 * pi**2 * a * b, "notes torus S")
    eq(polar_area(2 * a * sp.cos(th), -pi / 2, pi / 2), pi * a**2, "notes circle")


T.write(check)
