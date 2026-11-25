import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.polar-equations")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["polar-coordinates"], r"The Cartesian coordinates of the point with polar coordinates $\left(2, \dfrac{2\pi}{3}\right)$ are",
         [r"$(-1, \sqrt3)$", r"$(1, -\sqrt3)$", r"$(-\sqrt3, 1)$", r"$(1, \sqrt3)$"],
         r"""$$x = 2\cos\frac{2\pi}{3} = -1,\qquad y = 2\sin\frac{2\pi}{3} = \sqrt3.$$
The point is in quadrant II, as $\frac{2\pi}{3}$ is. $(-\sqrt3, 1)$ swaps sine and cosine (that is the point at $\frac{5\pi}{6}$); $(1, \sqrt3)$ is the point at $\frac\pi3$.""")

# q2
T.single(1, ["polar-coordinates"], r"With $r > 0$ and $-\pi < \theta \le \pi$, the polar coordinates of the point $(-1, -1)$ are",
         [r"$\left(\sqrt2, -\dfrac{3\pi}{4}\right)$", r"$\left(\sqrt2, \dfrac{\pi}{4}\right)$", r"$\left(\sqrt2, \dfrac{3\pi}{4}\right)$", r"$\left(2, -\dfrac{3\pi}{4}\right)$"],
         r"""$r = \sqrt{1 + 1} = \sqrt2$. The point is in quadrant III, so
$$\theta = -\pi + \frac\pi4 = -\frac{3\pi}{4}.$$
$\frac\pi4$ is what $\tan^{-1}\frac{-1}{-1}$ gives; it is the point $(1, 1)$. $\frac{3\pi}{4}$ is in quadrant II; $r = 2$ forgets the square root.""")

# q3
T.single(1, ["polar-coordinates"], r"The distance between the points $\left(3, \dfrac\pi6\right)$ and $\left(4, \dfrac\pi2\right)$ is",
         [r"$\sqrt{13}$", r"$5$", r"$\sqrt{37}$", r"$1$"],
         r"""By the cosine rule,
$$d^2 = 3^2 + 4^2 - 2\cdot3\cdot4\cos\left(\frac\pi2 - \frac\pi6\right) = 25 - 24\cdot\frac12 = 13.$$
$5$ treats the angle at the pole as a right angle; $\sqrt{37}$ uses $+24\cos$; $1$ just subtracts the radii.""")

# q4
T.single(3, ["chord-tangent-normal"], r"The tangents to the conic $\dfrac2r = 1 + \cos\theta$ at the points $\theta = \dfrac\pi3$ and $\theta = -\dfrac\pi3$ meet at the point (Cartesian coordinates, pole as origin, initial line as $x$-axis)",
         [r"$\left(\dfrac43, 0\right)$", r"$(2, 0)$", r"$\left(\dfrac23, 0\right)$", r"$(4, 0)$"],
         r"""Tangents at $\alpha, \beta$ of $\frac lr = 1 + e\cos\theta$ meet at
$$\theta = \frac{\alpha + \beta}{2} = 0,\qquad \frac lr = e\cos\frac{\alpha + \beta}{2} + \cos\frac{\alpha - \beta}{2} = 1 + \frac12 = \frac32.$$
So $r = \frac{2}{3/2} = \frac43$, the point $\left(\frac43, 0\right)$.

Check in Cartesian form: the conic is $y^2 = 4 - 4x$, the point $\theta = \frac\pi3$ is $\left(\frac23, \frac{2}{\sqrt3}\right)$, and its tangent $\frac{2}{\sqrt3}y = -2x + \frac83$ meets $y = 0$ at $x = \frac43$. $(2, 0)$ is where the directrix meets the axis (tangents at the ends of a **focal** chord meet there, but $\pm\frac\pi3$ is not a focal chord).""")

# q5
T.single(1, ["straight-line"], r"The Cartesian equation of the line $r\cos\left(\theta - \dfrac\pi3\right) = 4$ is",
         [r"$x + \sqrt3 y = 8$", r"$\sqrt3 x + y = 8$", r"$x + \sqrt3 y = 4$", r"$x - \sqrt3 y = 8$"],
         r"""Expand: $r\cos\theta\cos\frac\pi3 + r\sin\theta\sin\frac\pi3 = 4$, i.e.
$$\frac12x + \frac{\sqrt3}{2}y = 4 \iff x + \sqrt3y = 8.$$
Check: the foot of the perpendicular $(4, \frac\pi3) = (2, 2\sqrt3)$ satisfies $2 + 6 = 8$. $\sqrt3x + y = 8$ is the line with $\alpha = \frac\pi6$; $x + \sqrt3y = 4$ forgets to clear the $\frac12$.""")

# q6
T.single(2, ["straight-line"], r"The line $r(\cos\theta + \sqrt3\sin\theta) = 3$ in the normal form $r\cos(\theta - \alpha) = p$ $(p > 0)$ is",
         [r"$r\cos\left(\theta - \dfrac\pi3\right) = \dfrac32$", r"$r\cos\left(\theta - \dfrac\pi6\right) = \dfrac32$", r"$r\cos\left(\theta - \dfrac\pi3\right) = 3$", r"$r\cos\left(\theta + \dfrac\pi3\right) = \dfrac32$"],
         r"""Divide by $\sqrt{1 + 3} = 2$:
$$r\left(\tfrac12\cos\theta + \tfrac{\sqrt3}{2}\sin\theta\right) = \tfrac32 \iff r\cos\left(\theta - \tfrac\pi3\right) = \tfrac32.$$
So $p = \frac32$ and $\alpha = \frac\pi3$ ($\cos\alpha = \frac12$, $\sin\alpha = \frac{\sqrt3}{2}$). Taking $\alpha = \frac\pi6$ swaps sine and cosine; $p = 3$ skips the division; $+\frac\pi3$ flips the sign of the $\sin\theta$ term.""")

# q7
T.single(2, ["circle"], r"The polar equation of the circle with centre $\left(2, \dfrac\pi3\right)$ and radius $3$ is",
         [r"$r^2 - 4r\cos\left(\theta - \dfrac\pi3\right) - 5 = 0$", r"$r^2 - 4r\cos\left(\theta - \dfrac\pi3\right) + 5 = 0$", r"$r^2 - 2r\cos\left(\theta - \dfrac\pi3\right) - 5 = 0$", r"$r^2 - 4r\cos\left(\theta + \dfrac\pi3\right) - 5 = 0$"],
         r"""For centre $(c, \alpha)$ and radius $a$: $r^2 - 2cr\cos(\theta - \alpha) + c^2 - a^2 = 0$. Here $c = 2$, $a = 3$:
$$r^2 - 4r\cos\left(\theta - \frac\pi3\right) + 4 - 9 = 0.$$
The constant is $c^2 - a^2 = -5$ (negative: the pole is inside the circle, since $2 < 3$). $+5$ uses $a^2 - c^2$; $2r$ forgets the factor $2$ of the cosine rule.""")

# q8
T.single(1, ["circle"], r"The curve $r = 6\sin\theta$ is a circle with",
         [r"centre $(0, 3)$ and radius $3$", r"centre $(0, 6)$ and radius $6$", r"centre $(3, 0)$ and radius $3$", r"centre $(0, -3)$ and radius $3$"],
         r"""Multiply by $r$: $x^2 + y^2 = 6y$, i.e.
$$x^2 + (y - 3)^2 = 9.$$
Centre $(0, 3)$, radius $3$; the circle passes through the pole. $r = 2a\sin\theta$ has radius $a$, not $2a$. Centre $(3, 0)$ belongs to $r = 6\cos\theta$.""")

# q9
T.single(2, ["circle"], r"A circle passes through the pole, has its centre on the initial line, and passes through the point $\left(4, \dfrac\pi3\right)$. Its equation is",
         [r"$r = 8\cos\theta$", r"$r = 4\cos\theta$", r"$r = 8\sin\theta$", r"$r = 16\cos\theta$"],
         r"""Such a circle is $r = 2a\cos\theta$. Put in the point:
$$4 = 2a\cos\frac\pi3 = a \implies r = 8\cos\theta.$$
Check: radius $4$, centre $(4, 0)$, and the distance from $(4, 0)$ to $(4, \frac\pi3) = (2, 2\sqrt3)$ is $\sqrt{4 + 12} = 4$. $r = 4\cos\theta$ takes $2a = 4$; $\sin\theta$ puts the centre on $\theta = \frac\pi2$.""")

# q10
T.single(1, ["conic-focus-pole"], r"The conic $\dfrac8r = 2 + 4\cos\theta$ is",
         [r"a hyperbola with eccentricity $2$", r"a hyperbola with eccentricity $4$", r"an ellipse with eccentricity $\dfrac12$", r"a parabola"],
         r"""Make the constant term $1$: divide by $2$,
$$\frac4r = 1 + 2\cos\theta.$$
Compare with $\frac lr = 1 + e\cos\theta$: $e = 2 > 1$, $l = 4$. A hyperbola. Reading $e = 4$ off the unnormalised equation is the trap; $\frac12$ inverts the ratio.""")

# q11
T.single(2, ["conic-focus-pole"], r"The length of the latus rectum of the conic $\dfrac{10}{r} = 3 - 2\cos\theta$ is",
         [r"$\dfrac{20}{3}$", r"$\dfrac{10}{3}$", r"$20$", r"$5$"],
         r"""Divide by $3$: $\frac{10/3}{r} = 1 - \frac23\cos\theta$. So $l = \frac{10}{3}$, $e = \frac23$ (an ellipse), and
$$\text{latus rectum} = 2l = \frac{20}{3}.$$
Check: at $\theta = \pm\frac\pi2$, $r = \frac{10}{3}$, the two half-chords. $\frac{10}{3}$ is the semi-latus rectum; $20$ forgets to normalise; $5$ uses $\frac{10}{3 - 1}$.""")

# q12
T.single(2, ["conic-focus-pole"], r"The length of the major axis of the ellipse $\dfrac{15}{r} = 3 + 2\cos\theta$ is",
         [r"$18$", r"$15$", r"$9$", r"$6\sqrt5$"],
         r"""The vertices are on the axis: $\theta = 0$ gives $r = \frac{15}{5} = 3$ and $\theta = \pi$ gives $r = \frac{15}{1} = 15$. They lie on opposite sides of the focus, so
$$2a = 3 + 15 = 18.$$
Equivalently $l = 5$, $e = \frac23$ and $2a = \frac{2l}{1 - e^2} = \frac{10}{5/9} = 18$. $9$ is the semi-major axis; $6\sqrt5 = 2\cdot\frac{l}{\sqrt{1 - e^2}}$ is the **minor** axis.""")

# q13
T.single(2, ["conic-focus-pole"], r"The Cartesian equation of $\dfrac2r = 1 + \cos\theta$ (pole as origin, initial line as $x$-axis) is",
         [r"$y^2 = 4 - 4x$", r"$y^2 = 4 + 4x$", r"$y^2 = 4 - 2x$", r"$x^2 = 4 - 4y$"],
         r"""$2 = r + r\cos\theta = r + x$, so $r = 2 - x$ and
$$x^2 + y^2 = (2 - x)^2 \iff y^2 = 4 - 4x.$$
A parabola opening to the left with focus at the origin and directrix $x = 2$ (the initial line points from the focus towards the directrix). $y^2 = 4 + 4x$ belongs to $\frac2r = 1 - \cos\theta$.""")

# q14
T.single(2, ["conic-focus-pole"], r"For the hyperbola $\dfrac lr = 1 + 2\cos\theta$, $r \to \infty$ in the directions",
         [r"$\theta = \pm\dfrac{2\pi}{3}$", r"$\theta = \pm\dfrac{\pi}{3}$", r"$\theta = \pm\dfrac{\pi}{6}$", r"$\theta = \pm\dfrac{5\pi}{6}$"],
         r"""$r \to \infty$ when $1 + 2\cos\theta = 0$, i.e.
$$\cos\theta = -\frac12,\qquad \theta = \pm\frac{2\pi}{3}.$$
These are the directions of the asymptotes. $\pm\frac\pi3$ solves $\cos\theta = +\frac12$ (sign slip). In general the directions are $\cos\theta = -\frac1e$.""")

# q15
T.single(2, ["chord-tangent-normal"], r"The tangent to the conic $\dfrac2r = 1 + \cos\theta$ at the point $\theta = \dfrac\pi2$ is",
         [r"$\dfrac2r = \cos\theta + \sin\theta$", r"$\dfrac2r = 1 + \sin\theta$", r"$\dfrac2r = \cos\theta - \sin\theta$", r"$\dfrac2r = 1 + \cos\theta + \sin\theta$"],
         r"""The tangent at $\alpha$ to $\frac lr = 1 + e\cos\theta$ is $\frac lr = e\cos\theta + \cos(\theta - \alpha)$. With $e = 1$, $\alpha = \frac\pi2$:
$$\frac2r = \cos\theta + \sin\theta \iff x + y = 2.$$
Check: the point is $(0, 2)$; on $y^2 = 4 - 4x$ the slope there is $-\frac{2}{y} = -1$, giving $x + y = 2$. $1 + \sin\theta$ copies the constant $1$ from the conic; that curve is a parabola, not a line.""")

# q16
T.single(3, ["chord-tangent-normal"], r"The normal to the conic $\dfrac2r = 1 + \cos\theta$ at the point $\theta = \dfrac\pi2$ is",
         [r"$\dfrac2r = \sin\theta - \cos\theta$", r"$\dfrac2r = \cos\theta + \sin\theta$", r"$\dfrac2r = \cos\theta - \sin\theta$", r"$\dfrac1r = \sin\theta - \cos\theta$"],
         r"""The normal at $\alpha$ to $\frac lr = 1 + e\cos\theta$ is
$$\frac{le\sin\alpha}{1 + e\cos\alpha}\cdot\frac1r = e\sin\theta + \sin(\theta - \alpha).$$
With $l = 2$, $e = 1$, $\alpha = \frac\pi2$: $\frac2r = \sin\theta - \cos\theta$, i.e. $y - x = 2$.

Check: the tangent at $(0, 2)$ has slope $-1$, so the normal is $y = x + 2$. $\cos\theta + \sin\theta$ is the tangent; $\cos\theta - \sin\theta$ is $x - y = 2$, which misses $(0, 2)$.""")

# q17
T.single(2, ["chord-tangent-normal"], r"The chord of the conic $\dfrac2r = 1 + \cos\theta$ joining the points $\theta = 0$ and $\theta = \dfrac\pi2$ is",
         [r"$\dfrac2r = \cos\theta + \sqrt2\cos\left(\theta - \dfrac\pi4\right)$", r"$\dfrac2r = \cos\theta + \cos\left(\theta - \dfrac\pi4\right)$", r"$\dfrac2r = 1 + \sqrt2\cos\left(\theta - \dfrac\pi4\right)$", r"$\dfrac2r = \cos\theta + \dfrac{1}{\sqrt2}\cos\left(\theta - \dfrac\pi4\right)$"],
         r"""The chord joining $\alpha - \beta$ and $\alpha + \beta$ is $\frac lr = e\cos\theta + \sec\beta\cos(\theta - \alpha)$. Here $\alpha = \beta = \frac\pi4$, $\sec\beta = \sqrt2$:
$$\frac2r = \cos\theta + \sqrt2\cos\left(\theta - \frac\pi4\right) = 2\cos\theta + \sin\theta \iff 2x + y = 2.$$
Check: it passes through $(1, 0)$ ($\theta = 0$, $r = 1$) and $(0, 2)$ ($\theta = \frac\pi2$, $r = 2$). Without $\sec\beta$ you get the tangent at $\frac\pi4$; $\frac1{\sqrt2}$ uses $\cos\beta$.""")

# q18
T.single(2, ["focal-chords"], r"A focal chord of a parabola is divided by the focus into segments of lengths $3$ and $6$. The length of the latus rectum is",
         [r"$8$", r"$4$", r"$9$", r"$\dfrac92$"],
         r"""The semi-latus rectum is the harmonic mean of the segments:
$$l = \frac{2\cdot3\cdot6}{3 + 6} = 4,\qquad \text{latus rectum} = 2l = 8.$$
$4$ is the **semi**-latus rectum; $9$ is the chord itself; $\frac92$ is the arithmetic mean.""")

# q19
T.single(3, ["focal-chords"], r"For the ellipse $\dfrac6r = 2 + \cos\theta$, the length of the focal chord inclined at $\dfrac\pi3$ to the major axis is",
         [r"$\dfrac{32}{5}$", r"$\dfrac{96}{13}$", r"$6$", r"$8$"],
         r"""Normalise: $\frac3r = 1 + \frac12\cos\theta$, so $l = 3$, $e = \frac12$. The focal chord at angle $\theta$ to the axis has length
$$\frac{2l}{1 - e^2\cos^2\theta} = \frac{6}{1 - \frac14\cdot\frac14} = \frac{6}{15/16} = \frac{32}{5}.$$
Directly: $r(\tfrac\pi3) = \frac{3}{5/4} = \frac{12}{5}$ and $r(\tfrac{4\pi}{3}) = \frac{3}{3/4} = 4$, sum $\frac{32}{5}$. $\frac{96}{13}$ uses $\sin^2\theta$; $6$ is the latus rectum; $8$ is the major axis.""")

# q20
T.single(3, ["focal-chords"], r"$PQ$ and $RT$ are perpendicular focal chords of the ellipse $\dfrac6r = 2 + \cos\theta$. Then $\dfrac1{PQ} + \dfrac1{RT}$ equals",
         [r"$\dfrac{7}{24}$", r"$\dfrac{1}{3}$", r"$\dfrac{3}{8}$", r"$\dfrac{7}{12}$"],
         r"""With $l = 3$, $e = \frac12$, a focal chord at angle $\theta$ has $\frac1{PQ} = \frac{1 - e^2\cos^2\theta}{2l}$. For the perpendicular chord replace $\cos^2\theta$ by $\sin^2\theta$ and add:
$$\frac1{PQ} + \frac1{RT} = \frac{2 - e^2}{2l} = \frac{2 - \frac14}{6} = \frac{7}{24}.$$
Check with the axis and the latus rectum: $\frac18 + \frac16 = \frac{7}{24}$. $\frac38$ comes from $2 + e^2$; $\frac{7}{12}$ forgets the $2$ in $2l$.""")

# q21
T.single(3, ["chord-tangent-normal"], r"The line $\dfrac3r = \cos\theta + k\sin\theta$ touches the conic $\dfrac3r = 1 + \dfrac12\cos\theta$ if and only if",
         [r"$k = \pm\dfrac{\sqrt3}{2}$", r"$k = \pm\dfrac12$", r"$k = \pm\sqrt3$", r"$k = \pm\dfrac{\sqrt5}{2}$"],
         r"""The line $\frac lr = A\cos\theta + B\sin\theta$ touches $\frac lr = 1 + e\cos\theta$ iff $(A - e)^2 + B^2 = 1$ (the tangent at $\alpha$ has $A = e + \cos\alpha$, $B = \sin\alpha$). Here $A = 1$, $e = \frac12$:
$$\frac14 + k^2 = 1 \implies k = \pm\frac{\sqrt3}{2}.$$
In fact $A - e = \frac12 = \cos\alpha$ gives $\alpha = \pm\frac\pi3$. $\pm\frac12$ comes from $A^2 + B^2 = 1 + e^2$; $\pm\frac{\sqrt5}{2}$ from $B^2 = 1 + e^2$.""")

# ---------------------------------------------------------------- statements (2)
T.statements(2, ["circle"], r"Consider the following statements:",
             [r"$r = 2a\cos\theta$ $(a > 0)$ is a circle through the pole with centre $(a, 0)$ and radius $a$.",
              r"$r = a$ $(a > 0)$ is a circle with centre at the pole and radius $a$.",
              r"$r^2 - 4r\cos\theta + 3 = 0$ is a circle with centre $(2, 0)$ and radius $\sqrt3$."],
             [r"1 and 2 only", r"1, 2 and 3", r"2 and 3 only", r"1 only"],
             r"""1. True: $x^2 + y^2 = 2ax$, i.e. $(x - a)^2 + y^2 = a^2$.
2. True: $x^2 + y^2 = a^2$.
3. False: in $r^2 - 2cr\cos(\theta - \alpha) + c^2 - a^2 = 0$, $c = 2$ and $c^2 - a^2 = 3$, so $a = 1$. In Cartesian form, $x^2 + y^2 - 4x + 3 = 0$, i.e. $(x - 2)^2 + y^2 = 1$. The value $\sqrt3$ treats the constant as the radius squared.""")

T.statements(3, ["focal-chords"], r"Consider the following statements about the conic $\dfrac lr = 1 + e\cos\theta$ $(l > 0)$:",
             [r"For every focal chord $PSQ$, $\dfrac1{SP} + \dfrac1{SQ} = \dfrac2l$.",
              r"When $e = 1$ (parabola $y^2 = 4ax$, $l = 2a$), the focal chord inclined at $\theta$ to the axis has length $4a\operatorname{cosec}^2\theta$.",
              r"When $0 < e < 1$, the latus rectum is the shortest focal chord."],
             [r"1, 2 and 3", r"1 and 2 only", r"1 and 3 only", r"2 only"],
             r"""1. True: $\frac1{SP} + \frac1{SQ} = \frac{1 + e\cos\theta}{l} + \frac{1 - e\cos\theta}{l} = \frac2l$.
2. True: $PQ = \frac{2l}{1 - \cos^2\theta} = \frac{4a}{\sin^2\theta}$.
3. True: $PQ = \frac{2l}{1 - e^2\cos^2\theta}$ is least when $\cos\theta = 0$, giving $2l$, the latus rectum. (The longest is the major axis, $\frac{2l}{1 - e^2}$.)""")

# ---------------------------------------------------------------- match (2)
T.match(1, ["straight-line", "circle", "conic-focus-pole"], r"Match each polar equation in List I $(a, p > 0)$ with the curve in List II.",
        [r"$r\cos(\theta - \alpha) = p$", r"$r = 2a\cos\theta$", r"$\dfrac4r = 1 + \cos\theta$", r"$\dfrac4r = 2 + 3\cos\theta$"],
        [r"hyperbola", r"straight line", r"parabola", r"circle through the pole"],
        [r"A-2, B-4, C-3, D-1", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-2, B-3, C-4, D-1"],
        r"""- A: $x\cos\alpha + y\sin\alpha = p$, a straight line: 2.
- B: $x^2 + y^2 = 2ax$, a circle through the pole: 4.
- C: $e = 1$, a parabola: 3.
- D: $\frac2r = 1 + \frac32\cos\theta$, $e = \frac32 > 1$, a hyperbola: 1. Normalise before reading $e$.""")

T.match(2, ["conic-focus-pole"], r"For the conic $\dfrac6r = 2 + \cos\theta$, match each quantity in List I with its value in List II.",
        [r"eccentricity", r"semi-latus rectum", r"semi-major axis", r"distance from the pole to the corresponding directrix"],
        [r"$6$", r"$\dfrac12$", r"$4$", r"$3$"],
        [r"A-2, B-4, C-3, D-1", r"A-2, B-3, C-4, D-1", r"A-2, B-1, C-3, D-4", r"A-4, B-2, C-3, D-1"],
        r"""Normalise: $\frac3r = 1 + \frac12\cos\theta$.
- A: $e = \frac12$: 2.
- B: $l = 3$: 4.
- C: $a = \frac{l}{1 - e^2} = \frac{3}{3/4} = 4$ (vertex distances $2$ and $6$ add to $8$): 3.
- D: the directrix is $r\cos\theta = \frac le = 6$: 1.""")

# ---------------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["straight-line", "polar-coordinates"],
                   r"The curve $r\cos\theta = 3$ is a straight line perpendicular to the initial line.",
                   r"In polar coordinates $x = r\cos\theta$.",
                   0,
                   r"""R is the conversion formula. By R, $r\cos\theta = 3$ is $x = 3$, a line perpendicular to the $x$-axis (the initial line) at distance $3$ from the pole. It is the normal form $r\cos(\theta - \alpha) = p$ with $\alpha = 0$, $p = 3$. Both true, and R explains A.""")

T.assertion_reason(2, ["conic-focus-pole"],
                   r"The conic $\dfrac5r = 1 + 2\cos\theta$ is a hyperbola.",
                   r"The length of the latus rectum of the conic $\dfrac lr = 1 + e\cos\theta$ is $l$.",
                   2,
                   r"""A is true: $e = 2 > 1$.

R is false: at $\theta = \pm\frac\pi2$, $r = l$, so $l$ is the **semi**-latus rectum and the latus rectum is $2l$. For this hyperbola it is $10$.""")

T.assertion_reason(2, ["focal-chords"],
                   r"Every focal chord of the parabola $\dfrac4r = 1 + \cos\theta$ has length $8$.",
                   r"For every focal chord $PSQ$ of $\dfrac lr = 1 + e\cos\theta$, $\dfrac1{SP} + \dfrac1{SQ} = \dfrac2l$.",
                   3,
                   r"""R is true: $\frac{1 + e\cos\theta}{l} + \frac{1 - e\cos\theta}{l} = \frac2l$.

A is false: the focal chord at $\theta$ has length $\frac{2l}{\sin^2\theta} = \frac{8}{\sin^2\theta}$. Only the latus rectum has length $8$; at $\theta = \frac\pi4$ the length is $16$. A fixed harmonic mean does not fix the sum $SP + SQ$.""")

T.assertion_reason(3, ["focal-chords", "chord-tangent-normal"],
                   r"The tangents at the ends of any focal chord of the parabola $\dfrac lr = 1 + \cos\theta$ meet on its directrix.",
                   r"The semi-latus rectum of a conic is the harmonic mean of the segments of any focal chord.",
                   1,
                   r"""A is true: the ends are $\alpha$ and $\alpha + \pi$, with tangents
$$\frac lr = \cos\theta + \cos(\theta - \alpha),\qquad \frac lr = \cos\theta - \cos(\theta - \alpha).$$
Adding, the intersection satisfies $\frac lr = \cos\theta$, which is the directrix $r\cos\theta = l$.

R is also true ($\frac1{SP} + \frac1{SQ} = \frac2l$), but it is about lengths along the chord and plays no part in locating the tangents' intersection. So R does not explain A.""")

T.assertion_reason(3, ["chord-tangent-normal"],
                   r"The tangent at the point $\alpha$ of the conic $\dfrac lr = 1 + e\cos\theta$ is $\dfrac lr = e\cos\theta + \cos(\theta - \alpha)$.",
                   r"The chord joining the points $\alpha - \beta$ and $\alpha + \beta$ of the conic $\dfrac lr = 1 + e\cos\theta$ is $\dfrac lr = e\cos\theta + \sec\beta\cos(\theta - \alpha)$.",
                   0,
                   r"""R is true: the right side is linear in $\cos\theta, \sin\theta$, so it is a line; at $\theta = \alpha \pm \beta$ it equals $e\cos\theta + 1$, which is the conic's value of $\frac lr$.

A is true and follows from R: the tangent is the limit of the chord as the two points coincide, $\beta \to 0$, and $\sec\beta \to 1$. Both true, and R explains A.""")


def check():
    import sympy as sp
    x, y, th, r, k = sp.symbols("x y theta r k", real=True)
    pi = sp.pi

    def cart(rr, t):
        return (sp.simplify(rr * sp.cos(t)), sp.simplify(rr * sp.sin(t)))

    def line_AB(l, A, B):
        # l/r = A cos θ + B sin θ  <=>  A x + B y = l
        return A * x + B * y - l

    def conic_cart(l, e):
        # sqrt(x^2+y^2) = l - e x  ->  squared
        return sp.expand(x**2 + y**2 - (l - e * x)**2)

    def on(expr, P):
        return sp.simplify(expr.subs({x: P[0], y: P[1]}))

    def polar_lr(l, e, t):
        return l / (1 + e * sp.cos(t))

    # q1
    P = cart(2, 2 * pi / 3); eq(P[0], -1, "q1x"); eq(P[1], sp.sqrt(3), "q1y")
    # q2
    eq(sp.sqrt(2), sp.Abs(-1 - sp.I), "q2r"); eq(sp.arg(-1 - sp.I), -3 * pi / 4, "q2t")
    # q3
    d2 = 9 + 16 - 24 * sp.cos(pi / 2 - pi / 6)
    P1, P2 = cart(3, pi / 6), cart(4, pi / 2)
    eq(d2, 13, "q3"); eq((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2, 13, "q3 cart")
    # q4: tangents at ±π/3 of 2/r = 1 + cos θ
    C = conic_cart(2, 1)
    eq(C - (y**2 - 4 + 4 * x), 0, "q13 cart")
    def tangent_line(l, e, al):
        return line_AB(l, e + sp.cos(al), sp.sin(al))
    sol = sp.solve([tangent_line(2, 1, pi / 3), tangent_line(2, 1, -pi / 3)], [x, y])
    eq(sol[x], sp.Rational(4, 3), "q4x"); eq(sol[y], 0, "q4y")
    # cross-check tangent with gradient of Cartesian conic
    def grad_tangent(Cc, Pt):
        gx, gy = [sp.diff(Cc, v).subs({x: Pt[0], y: Pt[1]}) for v in (x, y)]
        return gx * (x - Pt[0]) + gy * (y - Pt[1])
    Pt = cart(polar_lr(2, 1, pi / 3), pi / 3)
    eq(on(C, Pt), 0, "q4 pt on conic")
    tg = grad_tangent(C, Pt)
    eq(sp.solve(tg.subs(y, 0), x)[0], sp.Rational(4, 3), "q4 grad")
    # q5
    q5 = sp.expand(sp.expand_trig(sp.cos(th - pi / 3)))  # = cos/2 + sqrt3 sin/2
    eq(2 * (q5.coeff(sp.cos(th)) * x + q5.coeff(sp.sin(th)) * y) - (x + sp.sqrt(3) * y), 0, "q5")
    eq(2 * 4, 8, "q5 rhs")
    # q6
    eq(sp.expand(sp.expand_trig(2 * sp.cos(th - pi / 3)) - (sp.cos(th) + sp.sqrt(3) * sp.sin(th)) * 1), 0, "q6 form")
    eq(3 / sp.sqrt(1 + 3), sp.Rational(3, 2), "q6 p")
    # q7: circle centre (2, π/3) radius 3: check a point at distance 3
    cx, cy = cart(2, pi / 3)
    circ7 = r**2 - 4 * r * sp.cos(th - pi / 3) - 5
    cart7 = sp.expand((x - cx)**2 + (y - cy)**2 - 9)
    eq(sp.expand(sp.expand_trig(cart7.subs({x: r * sp.cos(th), y: r * sp.sin(th)})) - circ7), 0, "q7")
    # q8
    eq(sp.expand(x**2 + y**2 - 6 * y - (x**2 + (y - 3)**2 - 9)), 0, "q8")
    # q9
    a = sp.solve(sp.Eq(4, 2 * k * sp.cos(pi / 3)), k)[0]; eq(2 * a, 8, "q9")
    P9 = cart(4, pi / 3); eq((P9[0] - 4)**2 + P9[1]**2, 16, "q9 check")
    # q10
    eq(sp.Rational(4, 2), 2, "q10 e")
    eq(sp.expand(conic_cart(4, 2) - (-3 * x**2 + y**2 + 16 * x - 16)), 0, "q10 cart")
    q10c = sp.Poly(conic_cart(4, 2), x, y)
    assert q10c.coeff_monomial(x**2) * q10c.coeff_monomial(y**2) < 0  # hyperbola
    # q11
    eq(2 * (sp.Rational(10, 3)), sp.Rational(20, 3), "q11")
    eq(10 / (3 - 2 * sp.cos(pi / 2)), sp.Rational(10, 3), "q11 half")
    # q12
    eq(15 / (3 + 2 * sp.cos(0)) + 15 / (3 + 2 * sp.cos(pi)), 18, "q12")
    l12, e12 = 5, sp.Rational(2, 3)
    eq(2 * l12 / (1 - e12**2), 18, "q12 formula")
    eq(2 * l12 / sp.sqrt(1 - e12**2), 6 * sp.sqrt(5), "q12 minor")
    # q13 done above; also distractor y^2=4+4x is 2/r = 1 - cos
    eq(sp.expand(conic_cart(2, -1) - (y**2 - 4 - 4 * x)), 0, "q13 distractor")
    # q14
    assert set(sp.solve(sp.Eq(1 + 2 * sp.cos(th), 0), th)) == {2 * pi / 3, 4 * pi / 3}
    # q15
    T15 = tangent_line(2, 1, pi / 2); eq(T15 - (x + y - 2), 0, "q15")
    P15 = cart(polar_lr(2, 1, pi / 2), pi / 2)
    g = grad_tangent(C, P15)
    eq(sp.simplify(g / g.coeff(x) - (x + y - 2)), 0, "q15 grad")
    # q16: normal via gradient and via formula
    gx, gy = [sp.diff(C, v).subs({x: P15[0], y: P15[1]}) for v in (x, y)]
    N = gy * (x - P15[0]) - gx * (y - P15[1])
    eq(sp.simplify(N / N.coeff(y) - (y - x - 2)), 0, "q16 grad")
    # general normal formula: le sinα/(1+e cosα) /r = e sinθ + sin(θ-α)
    l, e, al = sp.symbols("l e alpha", positive=True)
    lhs = l * e * sp.sin(al) / (1 + e * sp.cos(al))
    Ngen = lhs - (e * y + (y * sp.cos(al) - x * sp.sin(al)))  # times r
    r1 = l / (1 + e * sp.cos(al)); X1, Y1 = r1 * sp.cos(al), r1 * sp.sin(al)
    eq(Ngen.subs({x: X1, y: Y1}), 0, "normal passes through point")
    Cg = conic_cart(l, e)
    gxg, gyg = [sp.diff(Cg, v).subs({x: X1, y: Y1}) for v in (x, y)]
    # normal direction (gx, gy) must be parallel to the line's direction (-coef_y, coef_x)
    cxn, cyn = Ngen.coeff(x), Ngen.coeff(y)
    eq(sp.simplify(gxg * cxn + gyg * cyn), 0, "normal perpendicular to tangent")
    lhs16 = lhs.subs({l: 2, e: 1, al: pi / 2})
    eq(lhs16, 2, "q16 formula")
    # general tangent formula through the point and with right slope
    Tg = line_AB(l, e + sp.cos(al), sp.sin(al))
    eq(Tg.subs({x: X1, y: Y1}), 0, "tangent through point")
    eq(sp.simplify(gxg * Tg.coeff(y) - gyg * Tg.coeff(x)), 0, "tangent parallel to gradient normal")
    # q17 chord
    Ch = line_AB(2, 1 + sp.sqrt(2) * sp.cos(pi / 4), sp.sqrt(2) * sp.sin(pi / 4))
    eq(Ch - (2 * x + y - 2), 0, "q17")
    for t in (0, pi / 2):
        eq(on(Ch, cart(polar_lr(2, 1, t), t)), 0, "q17 ends")
    # general chord formula
    be = sp.symbols("beta", positive=True)
    Chg = line_AB(l, e + sp.cos(al) / sp.cos(be), sp.sin(al) / sp.cos(be))
    for t in (al - be, al + be):
        eq(sp.simplify(Chg.subs({x: polar_lr(l, e, t) * sp.cos(t), y: polar_lr(l, e, t) * sp.sin(t)})), 0, "chord ends")
    # q18
    eq(2 * 3 * 6 / sp.Integer(9) * 2, 8, "q18")
    # q19
    l19, e19 = 3, sp.Rational(1, 2)
    eq(2 * l19 / (1 - e19**2 * sp.cos(pi / 3)**2), sp.Rational(32, 5), "q19")
    eq(polar_lr(l19, e19, pi / 3) + polar_lr(l19, e19, 4 * pi / 3), sp.Rational(32, 5), "q19 direct")
    eq(2 * l19 / (1 - e19**2 * sp.sin(pi / 3)**2), sp.Rational(96, 13), "q19 distractor")
    # q20
    tt = sp.symbols("t")
    PQ = lambda t: polar_lr(l19, e19, t) + polar_lr(l19, e19, t + pi)
    eq(sp.simplify(1 / PQ(tt) + 1 / PQ(tt + pi / 2)), sp.Rational(7, 24), "q20")
    # q21: tangency of 3x + ... : line x + k y = 3 with conic 3/r = 1 + cos/2
    C21 = conic_cart(3, sp.Rational(1, 2))
    disc = sp.discriminant(sp.expand(C21.subs(x, 3 - k * y)), y)
    assert set(sp.solve(disc, k)) == {sp.sqrt(3) / 2, -sp.sqrt(3) / 2}, sp.solve(disc, k)
    # S1
    eq(sp.expand((x - k)**2 + y**2 - k**2 - (x**2 + y**2 - 2 * k * x)), 0, "S1-1")
    eq(sp.expand(x**2 + y**2 - 4 * x + 3 - ((x - 2)**2 + y**2 - 1)), 0, "S1-3 radius 1")
    # S2
    c = sp.symbols("c")
    eq(sp.simplify(1 / (l / (1 + e * c)) + 1 / (l / (1 - e * c)) - 2 / l), 0, "S2-1")
    aa = sp.symbols("a", positive=True)
    eq(sp.simplify(2 * (2 * aa) / (1 - sp.cos(th)**2) - 4 * aa / sp.sin(th)**2), 0, "S2-2")
    f = 2 * l / (1 - e**2 * c**2)  # length as function of c = cos θ
    assert sp.solve(sp.diff(f, c), c) == [0]
    eq(f.subs({l: 3, e: sp.Rational(1, 2), c: 0}), 6, "S2-3 min")
    assert f.subs({l: 3, e: sp.Rational(1, 2), c: 1}) > 6
    # M1
    eq(sp.expand(conic_cart(4, 1) - (y**2 + 8 * x - 16)), 0, "M1 C parabola")
    m1d = sp.Poly(conic_cart(2, sp.Rational(3, 2)), x, y)
    assert m1d.coeff_monomial(x**2) * m1d.coeff_monomial(y**2) < 0  # D hyperbola
    m1b = sp.expand(sp.expand_trig((r**2 - 2 * k * r * sp.cos(th))).subs({r**2: x**2 + y**2}).subs(r * sp.cos(th), x))
    eq(m1b - (x**2 + y**2 - 2 * k * x), 0, "M1 B")
    # M2
    eq(polar_lr(3, sp.Rational(1, 2), 0) + polar_lr(3, sp.Rational(1, 2), pi), 8, "M2 C 2a")
    eq(sp.Rational(3) / sp.Rational(1, 2), 6, "M2 D")
    # check directrix: point θ=0 at r=2, distance to x=6 is 4, ratio 1/2
    eq(sp.Rational(2, 4), sp.Rational(1, 2), "M2 D ratio")
    # AR1
    eq((r * sp.cos(th)).subs(r, 3 / sp.cos(th)), 3, "AR1")
    # AR2
    eq(2 * polar_lr(5, 2, pi / 2), 10, "AR2")
    # AR3
    PQ3 = sp.simplify(polar_lr(4, 1, pi / 4) + polar_lr(4, 1, pi / 4 + pi))
    eq(PQ3, 16, "AR3 chord at pi/4")
    # AR4: tangents at α, α+π of l/r = 1 + cos θ meet on directrix x = l
    s = sp.solve([line_AB(l, 1 + sp.cos(al), sp.sin(al)), line_AB(l, 1 + sp.cos(al + pi), sp.sin(al + pi))], [x, y])
    eq(s[x], l, "AR4 directrix")
    # perpendicular too (for parabola)
    eq(sp.simplify((1 + sp.cos(al)) * (1 - sp.cos(al)) + sp.sin(al) * (-sp.sin(al))), 0, "AR4 perp")
    # AR5: chord -> tangent as β -> 0
    eq(sp.limit(1 / sp.cos(be), be, 0), 1, "AR5")


T.write(check)
