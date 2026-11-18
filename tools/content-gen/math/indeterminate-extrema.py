import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.indeterminate-extrema")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["standard-limits", "lhospital"], r"$\displaystyle\lim_{x\to0}\frac{1 - \cos x}{x^2}$ equals",
         [r"$\dfrac12$", r"$1$", r"$0$", r"$2$"],
         r"""The form is $0/0$. By L'Hospital's rule twice:
$$\lim_{x\to0}\frac{1 - \cos x}{x^2} = \lim\frac{\sin x}{2x} = \frac12.$$
Check: $1 - \cos x = 2\sin^2\frac x2 \approx \frac{x^2}{2}$.

The value $1$ forgets the factor $2$ from differentiating $x^2$.""")

# q2
T.single(1, ["other-forms", "standard-limits"], r"$\displaystyle\lim_{x\to0^+} x^x$ equals",
         [r"$1$", r"$0$", r"$e$", r"$\dfrac1e$"],
         r"""The form is $0^0$. Put $y = x^x$, so $\ln y = x\ln x = \dfrac{\ln x}{1/x}$ ($\infty/\infty$):
$$\lim_{x\to0^+}\frac{\ln x}{1/x} = \lim\frac{1/x}{-1/x^2} = \lim(-x) = 0.$$
So $y \to e^0 = 1$.

$0$ treats the base alone; $\frac1e$ is the **least value** of $x^x$ (at $x = \frac1e$), not the limit at $0$.""")

# q3
T.single(1, ["other-forms", "standard-limits"], r"For a real constant $a$, $\displaystyle\lim_{x\to\infty}\left(1 + \frac ax\right)^x$ equals",
         [r"$e^a$", r"$1$", r"$ae$", r"$e^{1/a}$"],
         r"""The form is $1^\infty$. Using $\lim f^g = e^{\lim g(f - 1)}$:
$$\lim_{x\to\infty} x\cdot\frac ax = a, \quad\text{so the limit is } e^a.$$
(Or: $\ln y = x\ln(1 + a/x) = \dfrac{\ln(1 + a/x)}{1/x} \to a$ by L'Hospital.)

$1$ is the classic mistake "$1^\infty = 1$".""")

# q4
T.single(1, ["local-extrema"], r"The local maximum value of $f(x) = x^3 - 6x^2 + 9x + 1$ is",
         [r"$5$", r"$1$", r"$3$", r"$21$"],
         r"""$f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$. The sign of $f'$ is $+, -, +$ across $1$ and $3$, so $x = 1$ gives a local maximum:
$$f(1) = 1 - 6 + 9 + 1 = 5.$$

$1 = f(3)$ is the local **minimum**; $3 = f(2)$ is the value at the point of inflexion.""")

# q5
T.single(1, ["global-extrema"], r"The greatest area of a rectangle inscribed in a circle of radius $r$ is",
         [r"$2r^2$", r"$r^2$", r"$4r^2$", r"$\dfrac{\pi r^2}{2}$"],
         r"""The diagonal of the rectangle is a diameter. With vertices $(\pm r\cos\theta, \pm r\sin\theta)$:
$$A = 4r^2\sin\theta\cos\theta = 2r^2\sin 2\theta \le 2r^2,$$
with equality at $\theta = \frac\pi4$: the square of side $r\sqrt2$.

$4r^2$ is the area of the **circumscribed** square.""")

# q6
T.single(1, ["higher-derivative-test"], r"For $f(x) = x^4$, the point $x = 0$ is",
         [r"a point of local minimum", r"a point of local maximum", r"a point of inflexion", r"neither an extremum nor a point of inflexion"],
         r"""$f'(0) = f''(0) = f'''(0) = 0$ and $f^{(4)}(0) = 24 > 0$. The first non-vanishing derivative has **even** order $4$ and is positive, so $0$ is a local minimum (indeed $x^4 \ge 0 = f(0)$).

$f''(0) = 0$ tempts "inflexion", but $f'' = 12x^2 \ge 0$ does not change sign.""")

# q7
T.single(2, ["standard-limits", "other-forms"], r"$\displaystyle\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{1/x^2}$ equals",
         [r"$e^{-1/6}$", r"$e^{1/6}$", r"$1$", r"$e^{-1/3}$"],
         r"""The form is $1^\infty$:
$$\frac1{x^2}\left(\frac{\sin x}{x} - 1\right) = \frac{\sin x - x}{x^3} \to -\frac16,$$
since $\sin x = x - \frac{x^3}{6} + \cdots$. So the limit is $e^{-1/6}$.

Sign check: $\frac{\sin x}{x} < 1$ near $0$, so the answer must be below $1$; this kills $e^{1/6}$.""")

# q8
T.single(2, ["standard-limits", "other-forms"], r"$\displaystyle\lim_{x\to0}\left(\frac{\tan x}{x}\right)^{1/x^2}$ equals",
         [r"$e^{1/3}$", r"$e^{-1/3}$", r"$e^{1/6}$", r"$e^{2/3}$"],
         r"""The form is $1^\infty$. Since $\tan x = x + \frac{x^3}{3} + \cdots$,
$$\frac1{x^2}\left(\frac{\tan x}{x} - 1\right) = \frac{\tan x - x}{x^3} \to \frac13,$$
so the limit is $e^{1/3}$.

$\frac{\tan x}{x} > 1$ near $0$, so the answer exceeds $1$; $e^{1/6}$ uses the $\sin x$ coefficient.""")

# q9
T.single(2, ["other-forms"], r"$\displaystyle\lim_{x\to0}\left(\frac1x - \frac1{e^x - 1}\right)$ equals",
         [r"$\dfrac12$", r"$0$", r"$1$", r"$-\dfrac12$"],
         r"""The form is $\infty - \infty$. Take the LCM:
$$\frac{e^x - 1 - x}{x(e^x - 1)}.$$
Since $e^x - 1 \sim x$, this behaves like $\dfrac{e^x - 1 - x}{x^2} \to \dfrac12$ (two applications of L'Hospital, or $e^x = 1 + x + \frac{x^2}{2} + \cdots$).

$0$ comes from cancelling "$\frac1x - \frac1x$" after replacing $e^x - 1$ by $x$ too early: that replacement is valid only for factors, not inside a difference.""")

# q10
T.single(2, ["standard-limits", "exam-tips"], r"$\displaystyle\lim_{x\to0}\frac{\tan x - x}{x - \sin x}$ equals",
         [r"$2$", r"$\dfrac12$", r"$1$", r"$-2$"],
         r"""Use the series:
$$\tan x - x = \frac{x^3}{3} + \cdots, \qquad x - \sin x = \frac{x^3}{6} + \cdots,$$
so the ratio tends to $\dfrac{1/3}{1/6} = 2$.

(By L'Hospital: $\dfrac{\sec^2 x - 1}{1 - \cos x} = \dfrac{\tan^2 x}{1 - \cos x} \to \dfrac{x^2}{x^2/2} = 2$.) $\frac12$ is the reciprocal.""")

# q11
T.single(2, ["other-forms"], r"$\displaystyle\lim_{x\to0^+}(\cot x)^{\sin x}$ equals",
         [r"$1$", r"$0$", r"$e$", r"$\infty$"],
         r"""The form is $\infty^0$. Take logarithms:
$$\ln y = \sin x\,\ln\cot x = -\sin x\,\ln\tan x.$$
As $x \to 0^+$, $\sin x \sim x$ and $\ln\tan x \sim \ln x$ (their difference $\ln\frac{\tan x}{x} \to 0$), so $\ln y \sim -x\ln x \to 0$. Hence $y \to e^0 = 1$.

$\infty$ treats the base alone; $\infty^0$ is indeterminate, not infinite.""")

# q12
T.single(2, ["higher-derivative-test"], r"For $f(x) = x^5 - 5x^4 + 5x^3 - 1$, at $x = 0$ the function $f$ has",
         [r"neither a maximum nor a minimum", r"a local maximum", r"a local minimum", r"a local maximum, since $f''(0) = 0$ and $f'''(0) > 0$"],
         r"""$f'(x) = 5x^4 - 20x^3 + 15x^2 = 5x^2(x - 1)(x - 3)$, so $f'(0) = 0$.

$f''(x) = 20x^3 - 60x^2 + 30x$, $f''(0) = 0$; $f'''(x) = 60x^2 - 120x + 30$, $f'''(0) = 30 \ne 0$.

The first non-vanishing derivative has **odd** order $3$, so there is no extremum (a stationary point of inflexion). Check: $f' = 5x^2(x - 1)(x - 3) > 0$ on both sides of $0$.

The extrema are at $x = 1$ (maximum, $f = 0$) and $x = 3$ (minimum, $f = -28$).""")

# q13
T.single(2, ["global-extrema"], r"The height of the right circular cylinder of greatest volume that can be inscribed in a sphere of radius $R$ is",
         [r"$\dfrac{2R}{\sqrt3}$", r"$\dfrac{4R}{3}$", r"$R\sqrt2$", r"$R$"],
         r"""With height $h$, the radius satisfies $r^2 = R^2 - \frac{h^2}{4}$, so
$$V = \pi r^2 h = \pi\left(R^2 h - \frac{h^3}{4}\right), \qquad V' = \pi\left(R^2 - \frac{3h^2}{4}\right) = 0 \implies h = \frac{2R}{\sqrt3}.$$
$V'' = -\frac{3\pi h}{2} < 0$, so this is the maximum, with $V = \dfrac{4\pi R^3}{3\sqrt3}$.

$\frac{4R}{3}$ is the height of the inscribed **cone** of greatest volume.""")

# q14
T.single(1, ["global-extrema"], r"A closed right circular cylinder has a given volume. Its total surface area is least when the height $h$ and radius $r$ satisfy",
         [r"$h = 2r$", r"$h = r$", r"$h = \dfrac r2$", r"$h = 4r$"],
         r"""With $V = \pi r^2 h$ fixed, $h = \frac{V}{\pi r^2}$ and
$$S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{2V}{r}, \qquad S' = 4\pi r - \frac{2V}{r^2} = 0 \implies V = 2\pi r^3.$$
Then $h = \frac{V}{\pi r^2} = 2r$: the height equals the diameter. $S'' > 0$, so it is a minimum.

$h = r$ is the answer for an **open-top** cylinder.""")

# q15
T.single(2, ["global-extrema"], r"The least distance of the point $(0, 2)$ from the parabola $y = x^2$ is",
         [r"$\dfrac{\sqrt7}{2}$", r"$2$", r"$\sqrt{\dfrac32}$", r"$\dfrac{\sqrt3}{2}$"],
         r"""Minimise the squared distance $D = x^2 + (x^2 - 2)^2$. Put $u = x^2 \ge 0$:
$$D = u + (u - 2)^2, \qquad D'(u) = 2u - 3 = 0 \implies u = \frac32,$$
and $D = \frac32 + \frac14 = \frac74$. The least distance is $\frac{\sqrt7}{2} \approx 1.32$.

$2$ is the distance to the vertex, which is a local **maximum** of $D$ along the curve; $\sqrt{3/2}$ is the $\lvert x\rvert$-coordinate of the nearest points.""")

# q16
T.single(2, ["global-extrema"], r"The least value of $f(x) = 2x^3 - 3x^2 - 12x$ on $[-2, 3]$ is",
         [r"$-20$", r"$-4$", r"$-9$", r"$7$"],
         r"""$f'(x) = 6(x^2 - x - 2) = 6(x - 2)(x + 1)$; critical points $-1$ and $2$, both in $[-2, 3]$.
$$f(-2) = -4,\quad f(-1) = 7,\quad f(2) = -20,\quad f(3) = -9.$$
The global minimum is $-20$ (at $x = 2$) and the global maximum is $7$.

$-4$ and $-9$ are endpoint values only; the closed-interval method compares all four.""")

# q17
T.single(3, ["exam-tips", "local-extrema"], r"For $x > 0$, the greatest value of $x^{1/x}$ is",
         [r"$e^{1/e}$", r"$e$", r"$1$", r"$\left(\dfrac1e\right)^{e}$"],
         r"""Let $y = x^{1/x}$, so $\ln y = \dfrac{\ln x}{x}$ and
$$\frac{d}{dx}\frac{\ln x}{x} = \frac{1 - \ln x}{x^2},$$
which is $> 0$ for $x < e$ and $< 0$ for $x > e$. So the maximum is at $x = e$, with value $e^{1/e} \approx 1.445$.

$e$ is the maximiser, not the maximum value. A consequence: $\pi^{1/\pi} < e^{1/e}$, so $\pi^e < e^\pi$.""")

# q18
T.single(3, ["standard-limits", "other-forms"], r"$\displaystyle\lim_{x\to0}\left(\frac1{x^2} - \cot^2 x\right)$ equals",
         [r"$\dfrac23$", r"$\dfrac13$", r"$-\dfrac23$", r"$0$"],
         r"""Write $\cot^2 x = \csc^2 x - 1$, so the expression is
$$\left(\frac1{x^2} - \frac1{\sin^2 x}\right) + 1.$$
Since $\sin^2 x = x^2 - \frac{x^4}{3} + \cdots$, we get $\dfrac{\sin^2 x - x^2}{x^2\sin^2 x} \to -\dfrac13$. So the limit is $-\frac13 + 1 = \frac23$.

$-\frac13$ (the limit of $\frac1{x^2} - \frac1{\sin^2 x}$) forgets the $+1$; $\frac13$ also changes the sign.""")

# q19
T.single(3, ["standard-limits", "other-forms"], r"For $a, b > 0$, $\displaystyle\lim_{x\to0}\left(\frac{a^x + b^x}{2}\right)^{1/x}$ equals",
         [r"$\sqrt{ab}$", r"$ab$", r"$\dfrac{a + b}{2}$", r"$1$"],
         r"""The form is $1^\infty$. Using $\lim f^g = e^{\lim g(f - 1)}$:
$$\frac1x\left(\frac{a^x + b^x}{2} - 1\right) = \frac12\left(\frac{a^x - 1}{x} + \frac{b^x - 1}{x}\right) \to \frac{\ln a + \ln b}{2}.$$
So the limit is $e^{\frac12\ln(ab)} = \sqrt{ab}$: the geometric mean.

$ab$ forgets the $\frac12$; $\frac{a + b}{2}$ is the value of the base at $x = 1$.""")

# q20
T.single(3, ["standard-limits"], r"$\displaystyle\lim_{x\to0}\frac{(1 + x)^{1/x} - e}{x}$ equals",
         [r"$-\dfrac e2$", r"$\dfrac e2$", r"$-e$", r"$0$"],
         r"""Write $(1 + x)^{1/x} = e^{\ln(1 + x)/x}$ and
$$\frac{\ln(1 + x)}{x} = 1 - \frac x2 + \frac{x^2}{3} - \cdots.$$
So $(1 + x)^{1/x} = e\cdot e^{-x/2 + \cdots} = e\left(1 - \frac x2 + \cdots\right)$, and
$$\frac{(1 + x)^{1/x} - e}{x} \to -\frac e2.$$
The sign is negative because $(1 + x)^{1/x}$ **increases** to $e$ as $x \to 0^+$.""")

# q21
T.single(3, ["standard-limits", "lhospital"],
         r"If $\displaystyle\lim_{x\to0}\frac{a\sin x - \sin 2x}{\tan^3 x}$ is finite, then the value of $a$ and of the limit are",
         [r"$a = 2$, limit $1$", r"$a = 2$, limit $-1$", r"$a = 2$, limit $\dfrac12$", r"$a = 1$, limit $1$"],
         r"""Since $\tan^3 x \sim x^3$, expand the numerator:
$$a\sin x - \sin 2x = (a - 2)x - \frac{a - 8}{6}x^3 + \cdots.$$
For a finite limit the $x$-term must vanish: $a = 2$. Then the numerator is $-\frac{2 - 8}{6}x^3 = x^3 + \cdots$, so the limit is $1$.

(Or: $2\sin x - \sin 2x = 2\sin x(1 - \cos x) \sim 2x\cdot\frac{x^2}{2} = x^3$.) The sign slip $-1$ comes from $-\frac{a - 8}{6}$ with the minus dropped.""")

# ------------------------------------------------------------ statements (3)
T.statements(2, ["lhospital"],
             r"Let $f, g$ be differentiable on a deleted neighbourhood of $a$. Consider the following statements:",
             [r"If $g'(x) \ne 0$ near $a$, $f(x) \to 0$, $g(x) \to 0$ and $\dfrac{f'(x)}{g'(x)} \to L$ as $x \to a$, then $\dfrac{f(x)}{g(x)} \to L$.",
              r"If $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}$ exists, then $\displaystyle\lim_{x\to a}\frac{f'(x)}{g'(x)}$ exists.",
              r"$\displaystyle\lim_{x\to0}\frac{x^2\sin(1/x)}{\sin x}$ exists, although the corresponding $\displaystyle\lim_{x\to0}\frac{f'(x)}{g'(x)}$ does not."],
             [r"1 and 3 only", r"1 only", r"1 and 2 only", r"1, 2 and 3"],
             r"""1. True: this is L'Hospital's rule for $0/0$, with its exact hypotheses.
2. False: the rule is one-way. Statement 3 is a counterexample.
3. True: $\dfrac{x^2\sin(1/x)}{\sin x} = \dfrac{x}{\sin x}\cdot x\sin\frac1x \to 1\cdot 0 = 0$. But
$$\frac{f'(x)}{g'(x)} = \frac{2x\sin(1/x) - \cos(1/x)}{\cos x},$$
and $\cos(1/x)$ oscillates between $-1$ and $1$, so this has no limit.

So 1 and 3 only.""")

T.statements(3, ["local-extrema", "higher-derivative-test"],
             r"Consider the following statements about a real function $f$ and an interior point $c$ of its domain:",
             [r"If $f'(c) = 0$ and $f''(c) = 0$, then $f$ has no local extremum at $c$.",
              r"If $f'(c) = \cdots = f^{(n-1)}(c) = 0$ and $f^{(n)}(c) > 0$ with $n$ even, then $f$ has a local minimum at $c$.",
              r"$f$ can have a local extremum at a point where it is not differentiable."],
             [r"2 and 3 only", r"1 and 2 only", r"2 only", r"1, 2 and 3"],
             r"""1. False: $f(x) = x^4$ has $f'(0) = f''(0) = 0$ and a minimum at $0$. When $f''(c) = 0$ the second-derivative test is silent.
2. True: this is the higher-derivative test. By Taylor, $f(c + h) - f(c) \approx \dfrac{h^n}{n!}f^{(n)}(c) > 0$ for small $h \ne 0$ when $n$ is even.
3. True: $f(x) = \lvert x\rvert$ has a minimum at $0$, where $f'(0)$ does not exist.

So 2 and 3 only.""")

T.statements(2, ["inflexion"],
             r"Consider the following statements:",
             [r"If $f''(c) = 0$, then $(c, f(c))$ is a point of inflexion of $y = f(x)$.",
              r"The origin is a point of inflexion of $y = x^3$.",
              r"The curve $y = x^4 - 4x^3$ has exactly one point of inflexion."],
             [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. False: $y = x^4$ has $y''(0) = 0$, but $y'' = 12x^2 \ge 0$ on both sides, so the concavity does not change.
2. True: $y'' = 6x$ changes sign at $0$ (and $y''' = 6 \ne 0$).
3. False: $y'' = 12x^2 - 24x = 12x(x - 2)$ changes sign at both $0$ and $2$, so there are **two** points of inflexion, $(0, 0)$ and $(2, -16)$.

So 2 only.""")

# ----------------------------------------------------------------- match (2)
T.match(2, ["other-forms", "standard-limits"], r"Match each limit in List I with its value in List II.",
        [r"$\displaystyle\lim_{x\to0}(\cos x)^{1/x^2}$", r"$\displaystyle\lim_{x\to0^+}x\ln x$",
         r"$\displaystyle\lim_{x\to0}(1 + 3x)^{1/x}$", r"$\displaystyle\lim_{x\to0}\frac{e^x - 1 - x}{x^2}$"],
        [r"$\dfrac12$", r"$e^{-1/2}$", r"$0$", r"$e^3$"],
        [r"A-2, B-3, C-4, D-1", r"A-1, B-3, C-4, D-2", r"A-2, B-4, C-3, D-1", r"A-3, B-2, C-4, D-1"],
        r"""- A ($1^\infty$): $\frac{\cos x - 1}{x^2} \to -\frac12$, so the limit is $e^{-1/2}$.
- B ($0\cdot\infty$): $\frac{\ln x}{1/x} \to \lim(-x) = 0$.
- C ($1^\infty$): $\frac1x\cdot 3x = 3$, so the limit is $e^3$.
- D ($0/0$): two applications of L'Hospital give $\frac{e^x}{2} \to \frac12$.

So A-2, B-3, C-4, D-1. Mixing up A and D (both involve $\frac12$) is the usual trap.""")

T.match(3, ["global-extrema"], r"Match each optimisation problem in List I with its optimal value in List II.",
        [r"greatest area of a rectangle inscribed in $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$",
         r"greatest volume of an open box made from a square sheet of side $a$ by cutting equal squares from the corners",
         r"greatest volume of a right circular cone inscribed in a sphere of radius $R$",
         r"greatest volume of a right circular cylinder inscribed in a sphere of radius $R$"],
        [r"$\dfrac{2a^3}{27}$", r"$\dfrac{4\pi R^3}{3\sqrt3}$", r"$2ab$", r"$\dfrac{32\pi R^3}{81}$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-1, C-2, D-4", r"A-1, B-3, C-4, D-2", r"A-3, B-4, C-1, D-2"],
        r"""- A: vertices $(\pm a\cos\theta, \pm b\sin\theta)$ give area $2ab\sin 2\theta \le 2ab$.
- B: cutting squares of side $x$, $V = x(a - 2x)^2$; $V' = (a - 2x)(a - 6x) = 0$ gives $x = \frac a6$ and $V = \frac a6\cdot\frac{4a^2}{9} = \frac{2a^3}{27}$.
- C: a cone of height $h$ has $r^2 = h(2R - h)$, so $V = \frac\pi3 h^2(2R - h)$; $V' = 0$ at $h = \frac{4R}{3}$, giving $V = \frac{32\pi R^3}{81}$.
- D: $V = \pi\left(R^2h - \frac{h^3}{4}\right)$ is greatest at $h = \frac{2R}{\sqrt3}$, giving $\frac{4\pi R^3}{3\sqrt3}$.

So A-3, B-1, C-4, D-2. Swapping C and D confuses the cone and the cylinder.""")

# ------------------------------------------------------- assertion-reason (4)
T.assertion_reason(1, ["local-extrema"],
                   r"$f(x) = x^3$ has no local extremum at $x = 0$.",
                   r"$f'(x)$ does not change sign as $x$ passes through $0$.",
                   0,
                   r"""Both are true: $f'(x) = 3x^2 \ge 0$ on both sides of $0$. By the first-derivative test, an extremum needs a change of sign of $f'$; with none, $f$ is increasing through $0$. So R explains A.

$f'(0) = 0$ alone does not give an extremum.""")

T.assertion_reason(2, ["lhospital"],
                   r"$\displaystyle\lim_{x\to\infty}\frac{x + \sin x}{x}$ does not exist.",
                   r"$\displaystyle\lim_{x\to\infty}\frac{1 + \cos x}{1}$ does not exist.",
                   3,
                   r"""R is true: $1 + \cos x$ oscillates between $0$ and $2$.

A is false: $\dfrac{x + \sin x}{x} = 1 + \dfrac{\sin x}{x} \to 1$, since $\lvert\sin x\rvert \le 1$.

L'Hospital's rule says: **if** $\lim f'/g'$ exists, then $\lim f/g$ equals it. When $\lim f'/g'$ fails to exist, the rule gives no information.""")

T.assertion_reason(3, ["higher-derivative-test"],
                   r"The function $f(x) = e^{-1/x^2}$ for $x \ne 0$, $f(0) = 0$, has a local minimum at $x = 0$.",
                   r"Every derivative of this $f$ at $x = 0$ is zero.",
                   1,
                   r"""A is true: $f(x) > 0 = f(0)$ for every $x \ne 0$.

R is true: each $f^{(n)}(x)$ for $x \ne 0$ is $P(1/x)e^{-1/x^2}$ for a polynomial $P$, and these tend to $0$; so $f^{(n)}(0) = 0$ for all $n$.

But R does not explain A: with no non-vanishing derivative, the higher-derivative test gives **no** conclusion. The minimum comes from comparing values directly.""")

T.assertion_reason(2, ["other-forms"],
                   r"$\displaystyle\lim_{x\to0^+}x^x = 1$.",
                   r"Every limit of the form $0^0$ equals $1$.",
                   2,
                   r"""A is true: $\ln x^x = x\ln x \to 0$, so $x^x \to 1$.

R is false: $0^0$ is an indeterminate form. For $x \to 0^+$, $x^{1/\ln x} = e^{\ln x/\ln x} = e$ for every $x$, although the base and the exponent both tend to $0$.""")


def check():
    import sympy as sp
    x, h, u, r, R, a, b, V, th = sp.symbols("x h u r R a b V theta", positive=True)
    lim = sp.limit

    def num(expr, x0, want, label, side=1):
        import mpmath
        mpmath.mp.dps = 40
        v = complex(sp.lambdify(x, expr, "mpmath")(mpmath.mpf(x0) + side * mpmath.mpf("1e-4")))
        w = complex(sp.N(want))
        if abs(v - w) > 1e-2 * max(1, abs(w)):
            sys.exit(f"NUMERIC CHECK FAILED {label}: {v} vs {w}")

    xr = sp.symbols("xr", real=True)
    # q1
    eq(lim((1 - sp.cos(xr)) / xr**2, xr, 0), sp.Rational(1, 2), "q1")
    # q2
    eq(lim(x**x, x, 0, "+"), 1, "q2"); eq(sp.exp(-1 / sp.E) - (1 / sp.E) ** (1 / sp.E), 0, "q2 min value")
    # q3
    eq(lim((1 + a / x) ** x, x, sp.oo), sp.exp(a), "q3")
    ar = sp.symbols("ar", real=True)
    eq(lim((1 - 3 / x) ** x, x, sp.oo), sp.exp(-3), "q3 negative a")
    # q4
    f = xr**3 - 6 * xr**2 + 9 * xr + 1
    assert sorted(sp.solve(sp.diff(f, xr), xr)) == [1, 3]
    assert sp.diff(f, xr, 2).subs(xr, 1) < 0 and sp.diff(f, xr, 2).subs(xr, 3) > 0
    eq(f.subs(xr, 1), 5, "q4"); eq(f.subs(xr, 3), 1, "q4 min"); eq(f.subs(xr, 2), 3, "q4 inflexion")
    assert sp.solve(sp.diff(f, xr, 2), xr) == [2]
    # q5
    A = 4 * r**2 * sp.sin(th) * sp.cos(th)
    eq(sp.maximum(A, th, sp.Interval(0, sp.pi / 2)), 2 * r**2, "q5")
    # q6
    g = xr**4
    assert [sp.diff(g, xr, k).subs(xr, 0) for k in range(1, 5)] == [0, 0, 0, 24]
    # q7, q8
    eq(lim((sp.sin(xr) / xr) ** (1 / xr**2), xr, 0), sp.exp(-sp.Rational(1, 6)), "q7")
    num((sp.sin(x) / x) ** (1 / x**2), 0, sp.exp(-sp.Rational(1, 6)), "q7 N")
    eq(lim((sp.tan(xr) / xr) ** (1 / xr**2), xr, 0), sp.exp(sp.Rational(1, 3)), "q8")
    num((sp.tan(x) / x) ** (1 / x**2), 0, sp.exp(sp.Rational(1, 3)), "q8 N")
    # q9
    eq(lim(1 / xr - 1 / (sp.exp(xr) - 1), xr, 0), sp.Rational(1, 2), "q9")
    # q10
    eq(lim((sp.tan(xr) - xr) / (xr - sp.sin(xr)), xr, 0), 2, "q10")
    eq(lim((xr - sp.sin(xr)) / xr**3, xr, 0), sp.Rational(1, 6), "notes x-sinx")
    eq(lim((sp.tan(xr) - xr) / xr**3, xr, 0), sp.Rational(1, 3), "notes tanx-x")
    # q11
    eq(lim(sp.sin(x) * sp.log(sp.cot(x)), x, 0, "+"), 0, "q11 log")
    num(sp.cot(x) ** sp.sin(x), 0, 1, "q11 N")
    # q12
    p = xr**5 - 5 * xr**4 + 5 * xr**3 - 1
    eq(sp.factor(sp.diff(p, xr)) - 5 * xr**2 * (xr - 1) * (xr - 3), 0, "q12 f'")
    assert sp.diff(p, xr, 2).subs(xr, 0) == 0 and sp.diff(p, xr, 3).subs(xr, 0) == 30
    assert sp.diff(p, xr).subs(xr, sp.Rational(-1, 2)) > 0 and sp.diff(p, xr).subs(xr, sp.Rational(1, 2)) > 0
    eq(p.subs(xr, 1), 0, "q12 max"); eq(p.subs(xr, 3), -28, "q12 min")
    assert sp.diff(p, xr, 2).subs(xr, 1) == -10 and sp.diff(p, xr, 2).subs(xr, 3) == 90
    # q13
    Vc = sp.pi * (R**2 * h - h**3 / 4)
    hs = sp.solve(sp.diff(Vc, h), h)
    assert len(hs) == 1
    eq(hs[0], 2 * R / sp.sqrt(3), "q13")
    eq(Vc.subs(h, hs[0]), 4 * sp.pi * R**3 / (3 * sp.sqrt(3)), "q13 V / m2 D")
    # q14
    S = 2 * sp.pi * r**2 + 2 * V / r
    rs = sp.solve(sp.diff(S, r), r)[0]
    eq((V / (sp.pi * rs**2)) / rs, 2, "q14")
    So = sp.pi * r**2 + 2 * V / r  # open top
    ro = sp.solve(sp.diff(So, r), r)[0]
    eq((V / (sp.pi * ro**2)) / ro, 1, "q14 open-top distractor")
    # q15
    D = u + (u - 2) ** 2
    us = sp.solve(sp.diff(D, u), u)[0]
    eq(us, sp.Rational(3, 2), "q15 u")
    eq(sp.sqrt(D.subs(u, us)), sp.sqrt(7) / 2, "q15")
    eq(sp.minimum(xr**2 + (xr**2 - 2) ** 2, xr, sp.S.Reals), sp.Rational(7, 4), "q15 direct")
    # q16
    q = 2 * xr**3 - 3 * xr**2 - 12 * xr
    eq(sp.minimum(q, xr, sp.Interval(-2, 3)), -20, "q16")
    eq(sp.maximum(q, xr, sp.Interval(-2, 3)), 7, "q16 max")
    assert [q.subs(xr, t) for t in (-2, -1, 2, 3)] == [-4, 7, -20, -9]
    # q17
    lg = sp.diff(sp.log(x) / x, x)
    assert sp.solve(lg, x) == [sp.E]
    assert lg.subs(x, 2) > 0 and lg.subs(x, 3) < 0
    eq((x ** (1 / x)).subs(x, sp.E), sp.exp(1 / sp.E), "q17")
    assert sp.N(sp.pi**sp.E) < sp.N(sp.E**sp.pi)
    # q18
    eq(lim(1 / xr**2 - sp.cot(xr) ** 2, xr, 0), sp.Rational(2, 3), "q18")
    eq(lim(1 / xr**2 - 1 / sp.sin(xr) ** 2, xr, 0), -sp.Rational(1, 3), "q18 notes")
    # q19
    for aa, bb in [(2, 3), (5, 7)]:
        eq(lim(((sp.Integer(aa) ** xr + sp.Integer(bb) ** xr) / 2) ** (1 / xr), xr, 0), sp.sqrt(aa * bb), f"q19 {aa},{bb}")
    eq(lim((a**x - 1) / x, x, 0), sp.log(a), "notes a^x")
    # q20
    eq(lim(((1 + x) ** (1 / x) - sp.E) / x, x, 0, "+"), -sp.E / 2, "q20")
    num(((1 + x) ** (1 / x) - sp.E) / x, 0, -sp.E / 2, "q20 N")
    # q21
    aa = sp.symbols("aa")
    ser = sp.series(aa * sp.sin(xr) - sp.sin(2 * xr), xr, 0, 4).removeO()
    eq(ser.coeff(xr, 1), aa - 2, "q21 x-coeff")
    eq(lim((2 * sp.sin(xr) - sp.sin(2 * xr)) / sp.tan(xr) ** 3, xr, 0), 1, "q21")
    assert lim((sp.sin(xr) - sp.sin(2 * xr)) / sp.tan(xr) ** 3, xr, 0) in (sp.oo, -sp.oo, sp.zoo)

    # statements 1
    s3 = xr**2 * sp.sin(1 / xr) / sp.sin(xr)
    eq(lim(xr / sp.sin(xr), xr, 0), 1, "st1 factor"); eq(lim(xr * sp.sin(1 / xr), xr, 0), 0, "st1 3")
    ratio = (2 * xr * sp.sin(1 / xr) - sp.cos(1 / xr)) / sp.cos(xr)
    eq(sp.diff(xr**2 * sp.sin(1 / xr), xr) - 2 * xr * sp.sin(1 / xr) + sp.cos(1 / xr), 0, "st1 f'")
    v1 = ratio.subs(xr, 1 / (2 * sp.pi * 1000)); v2 = ratio.subs(xr, 1 / (sp.pi * 1001))
    assert abs(sp.N(v1) + 1) < 1e-2 and abs(sp.N(v2) - 1) < 1e-2  # oscillates: no limit
    # statements 2: x^4 counterexample; |x|
    assert sp.diff(xr**4, xr).subs(xr, 0) == 0 and sp.diff(xr**4, xr, 2).subs(xr, 0) == 0
    eq(sp.minimum(xr**4, xr, sp.S.Reals), 0, "st2 x^4 min")
    eq(sp.minimum(sp.Abs(xr), xr, sp.S.Reals), 0, "st2 |x| min")
    # statements 3
    y3 = xr**4 - 4 * xr**3
    eq(sp.factor(sp.diff(y3, xr, 2)) - 12 * xr * (xr - 2), 0, "st3 y''")
    yy = sp.diff(y3, xr, 2)
    assert yy.subs(xr, -1) > 0 and yy.subs(xr, 1) < 0 and yy.subs(xr, 3) > 0  # two sign changes
    eq(y3.subs(xr, 2), -16, "st3 point")
    assert sp.diff(xr**3, xr, 2).subs(xr, -1) < 0 < sp.diff(xr**3, xr, 2).subs(xr, 1)
    # match 1
    eq(lim(sp.cos(xr) ** (1 / xr**2), xr, 0), sp.exp(-sp.Rational(1, 2)), "m1 A")
    eq(lim(x * sp.log(x), x, 0, "+"), 0, "m1 B")
    eq(lim((1 + 3 * xr) ** (1 / xr), xr, 0), sp.exp(3), "m1 C")
    eq(lim((sp.exp(xr) - 1 - xr) / xr**2, xr, 0), sp.Rational(1, 2), "m1 D")
    # match 2
    eq(sp.maximum(2 * a * b * sp.sin(2 * th), th, sp.Interval(0, sp.pi / 2)), 2 * a * b, "m2 A")
    Vb = x * (a - 2 * x) ** 2
    eq(sp.maximum(Vb, x, sp.Interval(0, a / 2)), 2 * a**3 / 27, "m2 B")
    Vk = sp.pi / 3 * h**2 * (2 * R - h)
    hk = [s for s in sp.solve(sp.diff(Vk, h), h) if s != 0][0]
    eq(hk, 4 * R / 3, "m2 C h"); eq(Vk.subs(h, hk), 32 * sp.pi * R**3 / 81, "m2 C")
    # AR1
    assert sp.diff(xr**3, xr).subs(xr, -sp.Rational(1, 10)) > 0 and sp.diff(xr**3, xr).subs(xr, sp.Rational(1, 10)) > 0
    # AR2
    eq(lim((x + sp.sin(x)) / x, x, sp.oo), 1, "AR2 A false")
    # AR3: derivatives of e^{-1/x^2} tend to 0 at 0
    e = sp.exp(-1 / xr**2)
    for k in range(0, 4):
        eq(lim(sp.diff(e, xr, k), xr, 0), 0, f"AR3 d{k}")
    eq(lim((e - 0) / xr, xr, 0), 0, "AR3 f'(0)")
    # AR4: counterexample to R
    eq(sp.simplify(x ** (1 / sp.log(x))), sp.E, "AR4 R false")
    eq(lim(1 / sp.log(x), x, 0, "+"), 0, "AR4 exponent -> 0")
    # notes extras
    eq(lim((sp.exp(x) + sp.exp(-x)) / (sp.exp(x) - sp.exp(-x)), x, sp.oo), 1, "notes circles")
    eq(lim(x ** (1 / x), x, sp.oo), 1, "notes inf^0")
    eq(lim((xr + 1) / (xr + 2), xr, 0), sp.Rational(1, 2), "notes not indeterminate")
    gg = xr**3 - 3 * xr**2
    assert [gg.subs(xr, t) for t in (-1, 0, 2, 4)] == [-4, 0, -4, 16]
    eq((xr + 1 / xr).subs(xr, -1), -2, "notes x+1/x")
    eq(lim((sp.sin(xr) / xr) ** (1 / (1 - sp.cos(xr))), xr, 0), sp.exp(-sp.Rational(1, 3)), "aux")


T.write(check)
