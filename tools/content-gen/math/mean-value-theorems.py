import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.mean-value-theorems")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["derivative"], r"At $x = 0$, the function $f(x) = \lvert x\rvert$ is",
         [r"continuous but not differentiable", r"differentiable but not continuous",
          r"both continuous and differentiable", r"neither continuous nor differentiable"],
         r"""$f(h) \to 0 = f(0)$, so $f$ is continuous at $0$. The one-sided derivatives are
$$Rf'(0) = \lim_{h\to0^+}\frac{|h|}{h} = 1, \qquad Lf'(0) = \lim_{h\to0^-}\frac{|h|}{h} = -1,$$
and they differ, so $f'(0)$ does not exist (a corner).

"Differentiable but not continuous" is impossible: differentiability always implies continuity.""")

# q2
T.single(1, ["rolle"], r"The value of $c$ in Rolle's theorem for $f(x) = x^2 - 4x + 3$ on $[1, 3]$ is",
         [r"$2$", r"$\dfrac32$", r"$\dfrac52$", r"$1$"],
         r"""$f(1) = f(3) = 0$ and $f$ is a polynomial, so Rolle applies.
$$f'(c) = 2c - 4 = 0 \implies c = 2 \in (1, 3).$$
$c = 1$ is an end point, and Rolle's $c$ must be strictly inside. Check: for a quadratic with equal end values, $c$ is the midpoint.""")

# q3
T.single(1, ["successive-derivatives"], r"The $n$th derivative of $\dfrac{1}{x + 2}$ is",
         [r"$\dfrac{(-1)^n\,n!}{(x + 2)^{n + 1}}$", r"$\dfrac{(-1)^{n}\,n!}{(x + 2)^{n}}$",
          r"$\dfrac{(-1)^{n-1}(n - 1)!}{(x + 2)^{n}}$", r"$\dfrac{n!}{(x + 2)^{n + 1}}$"],
         r"""$y_1 = -(x + 2)^{-2}$, $y_2 = 2(x + 2)^{-3}$, $y_3 = -6(x + 2)^{-4}$, so
$$y_n = \frac{(-1)^n n!}{(x + 2)^{n + 1}}.$$
Check at $n = 1$: $\frac{-1}{(x + 2)^2}$. The option with $(n - 1)!$ and power $n$ is the $n$th derivative of $\ln(x + 2)$; the one without $(-1)^n$ has the wrong sign at $n = 1$.""")

# q4
T.single(1, ["lagrange-mvt"],
         r"For $f(x) = x^2$, the number $\theta$ in $f(a + h) = f(a) + h f'(a + \theta h)$, $0 < \theta < 1$, equals",
         [r"$\dfrac12$", r"$\dfrac13$", r"$\dfrac{1}{\sqrt3}$", r"$\dfrac{a}{a + h}$"],
         r"""$$(a + h)^2 - a^2 = 2ah + h^2 \quad\text{and}\quad h f'(a + \theta h) = 2ah + 2\theta h^2.$$
Equating, $2\theta = 1$, so $\theta = \frac12$, for every $a$ and every $h \ne 0$.

$\frac{1}{\sqrt3}$ is the value for $f(x) = x^3$ at $a = 0$.""")

# q5
T.single(1, ["rolle", "exam-tips"],
         r"Rolle's theorem does not apply to $f(x) = \lvert x\rvert$ on $[-1, 1]$ because",
         [r"$f$ is not differentiable at $x = 0$", r"$f$ is not continuous on $[-1, 1]$",
          r"$f(-1) \ne f(1)$", r"$f$ is not bounded on $[-1, 1]$"],
         r"""$f$ is continuous on $[-1, 1]$ and $f(-1) = f(1) = 1$. But $Lf'(0) = -1 \ne 1 = Rf'(0)$, so $f$ is not differentiable at $0 \in (-1, 1)$.

The conclusion indeed fails: $f'(x) = \pm1$ wherever it exists, never $0$.""")

# q6
T.single(1, ["differentials"], r"Using differentials, the approximate value of $\sqrt{26}$ is",
         [r"$5.1$", r"$5.01$", r"$5.2$", r"$5.05$"],
         r"""Take $f(x) = \sqrt x$, $a = 25$, $h = 1$:
$$f(26) \approx f(25) + h f'(25) = 5 + \frac{1}{2\cdot 5} = 5.1.$$
(The true value is $5.0990\ldots$.)

$5.2$ forgets the $\frac12$ in $f'(x) = \frac{1}{2\sqrt x}$; $5.01$ misplaces the decimal in $\frac{1}{10}$.""")

# q7
T.single(1, ["differentials", "exam-tips"],
         r"An error of $1\%$ is made in measuring the radius of a circle. The approximate percentage error in its area is",
         [r"$2\%$", r"$1\%$", r"$3\%$", r"$\pi\%$"],
         r"""$A = \pi r^2$, so $\ln A = \ln\pi + 2\ln r$ and
$$\frac{\delta A}{A} \approx 2\,\frac{\delta r}{r} = 2 \times 1\% = 2\%.$$
$3\%$ is the error in the volume of a sphere ($r^3$). The constant $\pi$ does not affect a relative error.""")

# q8
T.single(1, ["monotonicity-darboux"],
         r"The largest interval on which $f(x) = x^3 - 3x$ is strictly decreasing is",
         [r"$[-1, 1]$", r"$[0, \sqrt3]$", r"$[-\sqrt3, \sqrt3]$", r"$[1, \infty)$"],
         r"""$f'(x) = 3x^2 - 3 = 3(x - 1)(x + 1)$, which is negative on $(-1, 1)$ and zero only at $\pm1$. So $f$ is strictly decreasing on $[-1, 1]$, and $f' > 0$ outside it.

$\pm\sqrt3$ are the zeros of $f$, not of $f'$. On $[1, \infty)$, $f$ is increasing.""")

# q9
T.single(2, ["lagrange-mvt"],
         r"The value of $c$ in Lagrange's mean value theorem for $f(x) = \sqrt x$ on $[1, 4]$ is",
         [r"$\dfrac94$", r"$\dfrac52$", r"$\dfrac32$", r"$2$"],
         r"""$$\frac{f(4) - f(1)}{4 - 1} = \frac{2 - 1}{3} = \frac13 = \frac{1}{2\sqrt c} \implies \sqrt c = \frac32 \implies c = \frac94.$$
$\frac94 \in (1, 4)$. The midpoint $\frac52$ is the answer only for quadratics; $\frac32$ is $\sqrt c$, not $c$.""")

# q10
T.single(2, ["lagrange-mvt"],
         r"The value of $c$ in Lagrange's mean value theorem for $f(x) = \ln x$ on $[1, e]$ is",
         [r"$e - 1$", r"$\dfrac{1}{e - 1}$", r"$\dfrac{e + 1}{2}$", r"$\sqrt e$"],
         r"""$$\frac{\ln e - \ln 1}{e - 1} = \frac{1}{e - 1} = f'(c) = \frac1c \implies c = e - 1 \approx 1.718 \in (1, e).$$
$\frac{1}{e - 1}$ is the slope $f'(c)$, not $c$; it is also less than $1$, outside the interval.""")

# q11
T.single(2, ["rolle"],
         r"The value of $c$ in Rolle's theorem for $f(x) = x(x - 1)(x - 2)$ on $[0, 1]$ is",
         [r"$1 - \dfrac{1}{\sqrt3}$", r"$1 + \dfrac{1}{\sqrt3}$", r"$\dfrac12$", r"$\dfrac{1}{\sqrt3}$"],
         r"""$f(0) = f(1) = 0$. $f(x) = x^3 - 3x^2 + 2x$, so
$$f'(x) = 3x^2 - 6x + 2 = 0 \implies x = 1 \pm \frac{1}{\sqrt3}.$$
Only $1 - \frac{1}{\sqrt3} \approx 0.42$ lies in $(0, 1)$; $1 + \frac{1}{\sqrt3}$ is the Rolle point for $[1, 2]$.""")

# q12
T.single(2, ["rolle"],
         r"The value of $c$ in Rolle's theorem for $f(x) = e^x\sin x$ on $[0, \pi]$ is",
         [r"$\dfrac{3\pi}{4}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{2\pi}{3}$"],
         r"""$f(0) = f(\pi) = 0$, and
$$f'(x) = e^x(\sin x + \cos x) = 0 \implies \tan c = -1 \implies c = \frac{3\pi}{4} \in (0, \pi).$$
$\frac{\pi}{4}$ solves $\tan c = 1$ (a sign slip); $\frac{\pi}{2}$ is the Rolle point of $\sin x$ alone.""")

# q13
T.single(2, ["successive-derivatives"], r"If $y = x^2 e^x$, then $y_n = \dfrac{d^n y}{dx^n}$ equals",
         [r"$e^x\left(x^2 + 2nx + n(n - 1)\right)$", r"$e^x\left(x^2 + 2nx + n^2\right)$",
          r"$e^x\left(x^2 + nx + n(n - 1)\right)$", r"$e^x\left(x^2 + 2nx + \dfrac{n(n - 1)}{2}\right)$"],
         r"""By Leibniz with $u = e^x$, $v = x^2$ ($v_1 = 2x$, $v_2 = 2$, $v_3 = 0$):
$$y_n = e^x x^2 + \binom n1 e^x\cdot 2x + \binom n2 e^x\cdot 2 = e^x\left(x^2 + 2nx + n(n - 1)\right).$$
Check at $n = 1$: $y_1 = e^x(x^2 + 2x)$. The $n^2$ option gives $e^x(x^2 + 2x + 1)$, wrong; the $\frac{n(n-1)}{2}$ option forgets $v_2 = 2$.""")

# q14
T.single(2, ["successive-derivatives"], r"The $n$th derivative of $e^x\sin x$ is",
         [r"$2^{n/2}e^x\sin\!\left(x + \dfrac{n\pi}{4}\right)$", r"$2^{n}e^x\sin\!\left(x + \dfrac{n\pi}{4}\right)$",
          r"$2^{n/2}e^x\sin\!\left(x + \dfrac{n\pi}{2}\right)$", r"$e^x\sin\!\left(x + \dfrac{n\pi}{4}\right)$"],
         r"""For $e^{ax}\sin(bx + c)$, $y_n = r^n e^{ax}\sin(bx + c + n\phi)$ with $r = \sqrt{a^2 + b^2}$, $\tan\phi = \frac ba$. Here $a = b = 1$: $r = \sqrt2$, $\phi = \frac{\pi}{4}$, so
$$y_n = (\sqrt2)^n e^x\sin\!\left(x + \frac{n\pi}{4}\right).$$
Check at $n = 1$: $e^x(\sin x + \cos x) = \sqrt2 e^x\sin(x + \frac{\pi}{4})$. The $\frac{n\pi}{2}$ shift belongs to $\sin x$ alone.""")

# q15
T.single(2, ["cauchy-mvt"],
         r"For $f(x) = e^x$ and $g(x) = e^{-x}$ on $[a, b]$, the value of $c$ in Cauchy's mean value theorem is",
         [r"$\dfrac{a + b}{2}$", r"$\sqrt{ab}$", r"$\dfrac{2ab}{a + b}$", r"$\ln\dfrac{e^a + e^b}{2}$"],
         r"""$g'(x) = -e^{-x} \ne 0$. Then
$$\frac{e^b - e^a}{e^{-b} - e^{-a}} = -e^{a + b}, \qquad \frac{f'(c)}{g'(c)} = \frac{e^c}{-e^{-c}} = -e^{2c}.$$
So $2c = a + b$: the arithmetic mean. The GM and HM arise from $\left(\sqrt x, \frac{1}{\sqrt x}\right)$ and $\left(\frac{1}{x^2}, \frac1x\right)$.""")

# q16
T.single(2, ["lagrange-mvt"], r"For every $x > 0$, which of the following holds?",
         [r"$\dfrac{x}{1 + x} < \ln(1 + x) < x$", r"$x < \ln(1 + x) < \dfrac{x}{1 + x}$",
          r"$\ln(1 + x) < \dfrac{x}{1 + x} < x$", r"$\dfrac{x}{1 + x} < x < \ln(1 + x)$"],
         r"""Apply the MVT to $\ln(1 + t)$ on $[0, x]$:
$$\ln(1 + x) = \frac{x}{1 + c}, \qquad 0 < c < x.$$
Since $1 < 1 + c < 1 + x$, $\frac{x}{1 + x} < \ln(1 + x) < x$.

Quick check at $x = 1$: $0.5 < 0.693 < 1$.""")

# q17
T.single(2, ["monotonicity-darboux"],
         r"Which of the following functions on $[-1, 1]$ is the derivative of some function differentiable on $[-1, 1]$?",
         [r"$g(x) = 2x\sin\frac1x - \cos\frac1x$ for $x \ne 0$, $g(0) = 0$",
          r"$g(x) = \operatorname{sgn} x$",
          r"$g(x) = 1$ for $x \ge 0$, $g(x) = 0$ for $x < 0$",
          r"$g(x) = 1$ for $x \ne 0$, $g(0) = 0$"],
         r"""The first $g$ is the derivative of $F(x) = x^2\sin\frac1x$, $F(0) = 0$: for $x \ne 0$ differentiate directly, and $F'(0) = \lim h\sin\frac1h = 0$.

By Darboux's theorem a derivative has the intermediate value property. $\operatorname{sgn}x$ and the unit step have jumps, and the last $g$ has a removable discontinuity; each skips values on an interval around $0$, so none is a derivative.""")

# q18
T.single(3, ["lagrange-mvt"],
         r"For $f(x) = e^x$ and $a = 0$, let $\theta \in (0, 1)$ satisfy $f(h) = f(0) + h f'(\theta h)$. Then $\displaystyle\lim_{h \to 0}\theta$ equals",
         [r"$\dfrac12$", r"$1$", r"$0$", r"$\dfrac{1}{e}$"],
         r"""$e^h - 1 = h e^{\theta h}$ gives
$$\theta = \frac1h\ln\frac{e^h - 1}{h}.$$
Since $\frac{e^h - 1}{h} = 1 + \frac h2 + O(h^2)$, its log is $\frac h2 + O(h^2)$, so $\theta \to \frac12$.

This is the general fact: if $f''$ is continuous at $a$ and $f''(a) \ne 0$, then $\theta \to \frac12$.""")

# q19
T.single(3, ["successive-derivatives"],
         r"If $y = \sin^{-1}x$, then $y_5(0)$, the fifth derivative at $x = 0$, equals",
         [r"$9$", r"$1$", r"$25$", r"$0$"],
         r"""From $(1 - x^2)y_2 - xy_1 = 0$, Leibniz gives
$$(1 - x^2)y_{n+2} - (2n + 1)xy_{n+1} - n^2y_n = 0.$$
At $x = 0$: $y_{n+2}(0) = n^2y_n(0)$. With $y_1(0) = 1$: $y_3(0) = 1^2\cdot 1 = 1$, and $y_5(0) = 3^2\cdot 1 = 9$.

$25$ uses $n = 5$ instead of $n = 3$ in the last step; $0$ is the value of every even-order derivative.""")

# q20
T.single(3, ["lagrange-mvt"],
         r"Applying the mean value theorem to $\tan^{-1}x$ on $\left[1, \dfrac43\right]$ shows that $\tan^{-1}\dfrac43$ lies between",
         [r"$\dfrac{\pi}{4} + \dfrac{3}{25}$ and $\dfrac{\pi}{4} + \dfrac16$", r"$\dfrac{\pi}{4} + \dfrac16$ and $\dfrac{\pi}{4} + \dfrac{1}{3}$",
          r"$\dfrac{\pi}{4} + \dfrac{1}{25}$ and $\dfrac{\pi}{4} + \dfrac{3}{25}$", r"$\dfrac{\pi}{4} + \dfrac{3}{16}$ and $\dfrac{\pi}{4} + \dfrac{1}{4}$"],
         r"""For $0 < a < b$: $\tan^{-1}b - \tan^{-1}a = \frac{b - a}{1 + c^2}$ with $a < c < b$, so
$$\frac{b - a}{1 + b^2} < \tan^{-1}b - \tan^{-1}a < \frac{b - a}{1 + a^2}.$$
With $a = 1$, $b = \frac43$: $b - a = \frac13$, $1 + b^2 = \frac{25}{9}$, $1 + a^2 = 2$. So the difference lies between $\frac{3}{25}$ and $\frac16$; add $\tan^{-1}1 = \frac{\pi}{4}$.

Check: $\tan^{-1}\frac43 \approx 0.9273$, and $0.7854 + 0.12 = 0.9054 < 0.9273 < 0.9521$. The other intervals do not contain $0.9273$; the upper end $\frac13 = b - a$ forgets to divide by $1 + c^2$.""")

# q21
T.single(3, ["derivative"],
         r"Let $f(x) = x^p\sin\dfrac1x$ for $x \ne 0$ and $f(0) = 0$. For which value of $p$ is $f$ differentiable at $0$ but $f'$ discontinuous at $0$?",
         [r"$p = 2$", r"$p = 1$", r"$p = 3$", r"$p = 0$"],
         r"""- $p = 0$: $\sin\frac1x$ has no limit at $0$; $f$ is not even continuous.
- $p = 1$: continuous, but $\frac{f(h)}{h} = \sin\frac1h$ oscillates; not differentiable.
- $p = 2$: $\frac{f(h)}{h} = h\sin\frac1h \to 0$, so $f'(0) = 0$; but $f'(x) = 2x\sin\frac1x - \cos\frac1x$ has no limit at $0$. **This one.**
- $p = 3$: $f'(x) = 3x^2\sin\frac1x - x\cos\frac1x \to 0 = f'(0)$, so $f'$ is continuous.""")

# ---------------------------------------------------------------- statements (2)
T.statements(2, ["rolle"], r"Consider the following statements:",
             [r"Between two consecutive distinct real roots of a real polynomial $p$, there is at least one root of $p'$.",
              r"If $f$ is differentiable on $(a, b)$ and $f'(c) = 0$ for some $c \in (a, b)$, then $f(a) = f(b)$.",
              r"If $f$ is differentiable on $\R$ and $f'(x) \ne 0$ for every $x$, then $f$ is one-one."],
             [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: Rolle on $[\alpha, \beta]$, where $p(\alpha) = p(\beta) = 0$.
2. False: this is the converse of Rolle. For $f(x) = x^2$ on $(-1, 2)$, $f'(0) = 0$ but $f(-1) = 1 \ne 4 = f(2)$.
3. True: if $f(x_1) = f(x_2)$ with $x_1 < x_2$, Rolle gives a zero of $f'$ in $(x_1, x_2)$.""")

T.statements(3, ["monotonicity-darboux"], r"Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$. Consider the following statements:",
             [r"If $f'(x) > 0$ for every $x \in (a, b)$, then $f$ is strictly increasing on $[a, b]$.",
              r"If $f$ is strictly increasing on $[a, b]$, then $f'(x) > 0$ for every $x \in (a, b)$.",
              r"If $c \in (a, b)$ and $f'(c) > 0$, then $f$ is increasing on some interval $(c - \delta, c + \delta)$."],
             [r"1 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""1. True: for $x_1 < x_2$, $f(x_2) - f(x_1) = (x_2 - x_1)f'(\xi) > 0$ by the MVT.
2. False: $x^3$ on $[-1, 1]$ is strictly increasing, but $f'(0) = 0$.
3. False: $f(x) = x + 2x^2\sin\frac1x$, $f(0) = 0$ has $f'(0) = 1$, yet $f'\big(\frac{1}{2k\pi}\big) = -1$ for every $k$, so $f$ decreases somewhere in every neighbourhood of $0$.""")

# ---------------------------------------------------------------- match (2)
T.match(2, ["successive-derivatives"], r"Match each function in List I with its $n$th derivative in List II ($a \ne 0$, $x > 0$).",
        [r"$e^{ax}$", r"$\sin ax$", r"$\ln x$", r"$\dfrac1x$"],
        [r"$a^n\sin\!\left(ax + \dfrac{n\pi}{2}\right)$", r"$\dfrac{(-1)^n n!}{x^{n + 1}}$",
         r"$a^n e^{ax}$", r"$\dfrac{(-1)^{n-1}(n - 1)!}{x^n}$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-1, C-2, D-4", r"A-1, B-3, C-4, D-2", r"A-3, B-4, C-1, D-2"],
        r"""- A: each derivative of $e^{ax}$ brings a factor $a$: $a^ne^{ax}$.
- B: each derivative of $\sin$ shifts the angle by $\frac{\pi}{2}$: $a^n\sin(ax + \frac{n\pi}{2})$.
- C: $(\ln x)' = \frac1x$, so the $n$th derivative of $\ln x$ is the $(n - 1)$th of $\frac1x$: $\frac{(-1)^{n-1}(n - 1)!}{x^n}$.
- D: $\frac{(-1)^n n!}{x^{n + 1}}$.

Swapping C and D is the usual slip; check at $n = 1$: $(\ln x)' = \frac1x$.""")

T.match(3, ["cauchy-mvt"],
        r"For $0 < a < b$, match each pair $(f, g)$ in List I with the value of $c$ in Cauchy's mean value theorem on $[a, b]$ in List II.",
        [r"$e^x,\ e^{-x}$", r"$\sqrt x,\ \dfrac{1}{\sqrt x}$", r"$\dfrac{1}{x^2},\ \dfrac1x$", r"$x^2,\ x^3$"],
        [r"$\sqrt{ab}$", r"$\dfrac{2(a^2 + ab + b^2)}{3(a + b)}$", r"$\dfrac{a + b}{2}$", r"$\dfrac{2ab}{a + b}$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-4, C-1, D-2", r"A-1, B-3, C-4, D-2", r"A-3, B-1, C-2, D-4"],
        r"""- A: $\frac{e^b - e^a}{e^{-b} - e^{-a}} = -e^{a+b} = -e^{2c}$, so $c = \frac{a + b}{2}$.
- B: $\frac{\sqrt b - \sqrt a}{1/\sqrt b - 1/\sqrt a} = -\sqrt{ab}$ and $\frac{f'(c)}{g'(c)} = -c$, so $c = \sqrt{ab}$.
- C: $\frac{1/b^2 - 1/a^2}{1/b - 1/a} = \frac1a + \frac1b$ and $\frac{f'(c)}{g'(c)} = \frac2c$, so $c = \frac{2ab}{a + b}$.
- D: $\frac{b^2 - a^2}{b^3 - a^3} = \frac{2}{3c}$, so $c = \frac{2(a^2 + ab + b^2)}{3(a + b)}$.

Swapping GM and HM (B and C) is the tempting error.""")

# ---------------------------------------------------------------- assertion-reason (5)
T.assertion_reason(2, ["derivative"],
                   r"The function $f(x) = x^2\sin\dfrac1x$ ($x \ne 0$), $f(0) = 0$, is differentiable at $x = 0$.",
                   r"Every function continuous at a point is differentiable at that point.",
                   2,
                   r"""A is true: $\frac{f(h) - f(0)}{h} = h\sin\frac1h \to 0$, so $f'(0) = 0$.

R is false: $|x|$ is continuous at $0$ but not differentiable there. Only the converse (differentiable ⇒ continuous) holds.""")

T.assertion_reason(3, ["monotonicity-darboux"],
                   r"There is no function $F$, differentiable on $\R$, with $F'(x) = \operatorname{sgn} x$ for every real $x$.",
                   r"If $F$ is differentiable on an interval, then $F'$ has the intermediate value property on that interval.",
                   0,
                   r"""R is Darboux's theorem, so it is true. $\operatorname{sgn}x$ takes the values $-1$ and $1$ on $[-1, 1]$ but never $\frac12$, so it lacks the intermediate value property and cannot be a derivative there. So A is true, and R explains it.

Note that $|x|$ has derivative $\operatorname{sgn} x$ only for $x \ne 0$.""")

T.assertion_reason(2, ["rolle"],
                   r"For $f(x) = x^{2/3}$ on $[-1, 1]$, Rolle's theorem guarantees some $c \in (-1, 1)$ with $f'(c) = 0$.",
                   r"For $f(x) = x^{2/3}$, $f(-1) = f(1)$.",
                   3,
                   r"""R is true: $f(-1) = f(1) = 1$.

A is false: $f'(x) = \frac{2}{3}x^{-1/3}$ for $x \ne 0$, and $\frac{f(h)}{h} = h^{-1/3}$ is unbounded, so $f$ is not differentiable at $0$ (a cusp). Rolle does not apply, and indeed $f'(x) \ne 0$ wherever it exists.""")

T.assertion_reason(2, ["lagrange-mvt", "exam-tips"],
                   r"$\lvert\sin x - \sin y\rvert \le \lvert x - y\rvert$ for all real $x$ and $y$.",
                   r"The cosine function is continuous on $\R$.",
                   1,
                   r"""A is true: by the MVT, $\sin x - \sin y = (x - y)\cos c$, and $|\cos c| \le 1$.

R is true, but it is not the reason: the proof needs the bound $|\cos c| \le 1$ on the derivative of $\sin$, not the continuity of $\cos$. So R does not explain A.""")

T.assertion_reason(2, ["lagrange-mvt"],
                   r"If $f$ is differentiable on $(a, b)$ and $f'(x) = 0$ for every $x \in (a, b)$, then $f$ is constant on $(a, b)$.",
                   r"If $f$ is differentiable on $(a, b)$, then for any $a < x_1 < x_2 < b$ there is $c \in (x_1, x_2)$ with $f(x_2) - f(x_1) = (x_2 - x_1)f'(c)$.",
                   0,
                   r"""R is true: $f$ is continuous on $[x_1, x_2]$ (differentiable implies continuous) and differentiable on $(x_1, x_2)$, so Lagrange's MVT applies.

With $f' \equiv 0$, R gives $f(x_2) = f(x_1)$ for every pair, so $f$ is constant. R explains A.""")


def check():
    import sympy as sp
    x, h, a, b, n, k = sp.symbols("x h a b n k", real=True)
    p = sp.symbols("p", positive=True)

    # q1: |x| continuous, one-sided derivatives differ
    eq(sp.limit(sp.Abs(h), h, 0), 0, "q1 cont")
    eq(sp.limit(sp.Abs(h) / h, h, 0, "+"), 1, "q1 R")
    eq(sp.limit(sp.Abs(h) / h, h, 0, "-"), -1, "q1 L")
    # q2
    f = x**2 - 4 * x + 3
    assert f.subs(x, 1) == f.subs(x, 3)
    eq(sp.solve(sp.diff(f, x), x)[0], 2, "q2")
    # q3
    for m in range(1, 7):
        eq(sp.diff(1 / (x + 2), x, m), (-1) ** m * sp.factorial(m) / (x + 2) ** (m + 1), "q3")
    # q4
    th = sp.symbols("theta")
    eq(sp.solve(sp.Eq((a + h) ** 2 - a**2, h * 2 * (a + th * h)), th)[0], sp.Rational(1, 2), "q4")
    # q5: |x| on [-1,1]: equal end values, continuous, not differentiable at 0
    assert sp.Abs(-1) == sp.Abs(1)
    assert sp.limit(sp.Abs(h) / h, h, 0, "+") != sp.limit(sp.Abs(h) / h, h, 0, "-")
    # q6
    eq(sp.sqrt(25) + sp.diff(sp.sqrt(x), x).subs(x, 25), sp.Rational(51, 10), "q6")
    assert abs(sp.N(sp.sqrt(26)) - 5.1) < 0.001
    # q7
    r = sp.symbols("r", positive=True)
    eq(sp.diff(sp.log(sp.pi * r**2), r) * r, 2, "q7 factor")
    # q8
    f = x**3 - 3 * x
    assert sp.solve_univariate_inequality(sp.diff(f, x) < 0, x, relational=False) == sp.Interval.open(-1, 1)
    # q9
    c = sp.symbols("c", positive=True)
    sols = [s for s in sp.solve(sp.Eq(sp.diff(sp.sqrt(x), x).subs(x, c), (2 - 1) / sp.Integer(3)), c) if 1 < s < 4]
    eq(sols[0], sp.Rational(9, 4), "q9")
    # q10
    sols = [s for s in sp.solve(sp.Eq(1 / c, 1 / (sp.E - 1)), c)]
    eq(sols[0], sp.E - 1, "q10")
    assert 1 < sp.E - 1 < sp.E
    # q11
    f = x * (x - 1) * (x - 2)
    assert f.subs(x, 0) == f.subs(x, 1) == 0
    roots = [s for s in sp.solve(sp.diff(f, x), x) if 0 < sp.N(s) < 1]
    assert len(roots) == 1
    eq(roots[0], 1 - 1 / sp.sqrt(3), "q11")
    # q12
    f = sp.exp(x) * sp.sin(x)
    eq(sp.diff(f, x).subs(x, 3 * sp.pi / 4), 0, "q12")
    roots = sp.solveset(sp.diff(f, x), x, sp.Interval.open(0, sp.pi))
    assert roots == sp.FiniteSet(3 * sp.pi / 4)
    # q13
    for m in range(0, 7):
        eq(sp.diff(x**2 * sp.exp(x), x, m), sp.exp(x) * (x**2 + 2 * m * x + m * (m - 1)), "q13")
    assert sp.simplify(sp.diff(x**2 * sp.exp(x), x, 1) - sp.exp(x) * (x**2 + 2 * x + 1)) != 0
    # q14
    for m in range(0, 7):
        eq(sp.diff(sp.exp(x) * sp.sin(x), x, m), 2 ** sp.Rational(m, 2) * sp.exp(x) * sp.sin(x + m * sp.pi / 4), "q14")
    # q15 (also match 2 A)
    A, B = sp.Rational(1, 2), sp.Integer(3)
    def cauchy_c(F, G, lo, hi):
        lhs = (F.subs(x, hi) - F.subs(x, lo)) / (G.subs(x, hi) - G.subs(x, lo))
        sol = [s for s in sp.solve(sp.Eq(sp.diff(F, x) / sp.diff(G, x), lhs), x) if s.is_real and lo < s < hi]
        assert len(sol) == 1
        return sol[0]
    eq(cauchy_c(sp.exp(x), sp.exp(-x), A, B), (A + B) / 2, "q15")
    # q16
    for v in [sp.Rational(1, 10), 1, 2, 10, 100]:
        assert v / (1 + v) < sp.log(1 + v) < v, "q16"
    # q17: F = x^2 sin(1/x) has the given derivative; F'(0) = 0
    F = x**2 * sp.sin(1 / x)
    eq(sp.diff(F, x), 2 * x * sp.sin(1 / x) - sp.cos(1 / x), "q17")
    eq(sp.limit(h * sp.sin(1 / h), h, 0), 0, "q17 F'(0)")
    # q18
    thh = sp.log((sp.exp(h) - 1) / h) / h
    eq(sp.limit(thh, h, 0), sp.Rational(1, 2), "q18")
    assert 0 < sp.N(thh.subs(h, sp.Rational(1, 10))) < 1
    # q19
    y = sp.asin(x)
    eq(sp.diff(y, x, 5).subs(x, 0), 9, "q19")
    eq(sp.diff(y, x, 3).subs(x, 0), 1, "q19 y3")
    for m in range(0, 5):
        rel = (1 - x**2) * sp.diff(y, x, m + 2) - (2 * m + 1) * x * sp.diff(y, x, m + 1) - m**2 * sp.diff(y, x, m)
        eq(rel, 0, "q19 recurrence")
    # q20
    lo, hi = sp.pi / 4 + sp.Rational(3, 25), sp.pi / 4 + sp.Rational(1, 6)
    val = sp.atan(sp.Rational(4, 3))
    eq((hi - sp.pi / 4), (sp.Rational(4, 3) - 1) / (1 + 1), "q20 upper")
    eq((lo - sp.pi / 4), (sp.Rational(4, 3) - 1) / (1 + sp.Rational(16, 9)), "q20 lower")
    assert sp.N(lo) < sp.N(val) < sp.N(hi)
    # every distractor interval excludes the true value
    for l_, u_ in [(sp.Rational(1, 6), sp.Rational(1, 3)), (sp.Rational(1, 25), sp.Rational(3, 25)), (sp.Rational(3, 16), sp.Rational(1, 4))]:
        assert not (sp.N(sp.pi / 4 + l_) < sp.N(val) < sp.N(sp.pi / 4 + u_))
    # q21
    def props(pp):
        f = x**pp * sp.sin(1 / x)
        cont = sp.limit(f, x, 0) == 0 if pp > 0 else False
        dq = sp.limit(f / x, x, 0) if pp > 1 else None
        diffable = dq == 0
        fp = sp.diff(f, x)
        fpc = diffable and sp.limit(fp, x, 0) == 0 if pp > 2 else False
        return cont, diffable, fpc
    assert props(2) == (True, True, False), props(2)
    assert props(3) == (True, True, True)
    assert props(1)[1] is False
    eq(sp.diff(x**2 * sp.sin(1 / x), x).subs(x, 1 / (2 * sp.pi)), -1, 'q21 osc')
    eq(sp.diff(x**2 * sp.sin(1 / x), x).subs(x, 1 / sp.pi), 1, 'q21 osc2')

    # statements 1
    q = (x - 1) * (x - 3) * (x + 2)
    dr = [sp.N(s) for s in sp.solve(sp.diff(q, x), x)]
    assert any(-2 < s < 1 for s in dr) and any(1 < s < 3 for s in dr)
    f = x**2
    assert sp.diff(f, x).subs(x, 0) == 0 and f.subs(x, -1) != f.subs(x, 2)
    # statements 2
    f = x**3
    assert sp.diff(f, x).subs(x, 0) == 0
    assert sp.solve_univariate_inequality(sp.diff(f, x) < 0, x, relational=False) == sp.EmptySet
    g = x + 2 * x**2 * sp.sin(1 / x)
    eq(sp.limit(g / x, x, 0), 1, "st2 f'(0)")
    for kk in range(1, 6):
        eq(sp.diff(g, x).subs(x, 1 / (2 * kk * sp.pi)), -1, "st2 f' negative")

    # match 1: A-3, B-1, C-4, D-2
    al = sp.Integer(3)
    for m in range(1, 6):
        eq(sp.diff(sp.exp(al * x), x, m), al**m * sp.exp(al * x), "m1 A")
        eq(sp.diff(sp.sin(al * x), x, m), al**m * sp.sin(al * x + m * sp.pi / 2), "m1 B")
        eq(sp.diff(sp.log(x), x, m), (-1) ** (m - 1) * sp.factorial(m - 1) / x**m, "m1 C")
        eq(sp.diff(1 / x, x, m), (-1) ** m * sp.factorial(m) / x ** (m + 1), "m1 D")
    # match 2: A-3, B-1, C-4, D-2
    A, B = sp.Integer(1), sp.Integer(4)
    eq(cauchy_c(sp.exp(x), sp.exp(-x), A, B), (A + B) / 2, "m2 A")
    eq(cauchy_c(sp.sqrt(x), 1 / sp.sqrt(x), A, B), sp.sqrt(A * B), "m2 B")
    eq(cauchy_c(1 / x**2, 1 / x, A, B), 2 * A * B / (A + B), "m2 C")
    eq(cauchy_c(x**2, x**3, A, B), 2 * (A**2 + A * B + B**2) / (3 * (A + B)), "m2 D")
    eq(cauchy_c(x**2, x**3, 1, 2), sp.Rational(14, 9), "notes example")

    # AR1: x^2 sin(1/x) differentiable at 0; |x| continuous not differentiable
    eq(sp.limit(h * sp.sin(1 / h), h, 0), 0, "ar1")
    # AR2: sgn misses 1/2 on [-1,1]
    assert sp.Rational(1, 2) not in {-1, 0, 1}
    # AR3: x^(2/3) not differentiable at 0
    assert sp.limit(sp.cbrt(h**2) / h, h, 0, "+") == sp.oo
    # AR4: |cos| <= 1
    assert sp.maximum(sp.cos(x), x, sp.Interval(0, 2 * sp.pi)) == 1 and sp.minimum(sp.cos(x), x, sp.Interval(0, 2 * sp.pi)) == -1
    # AR5: f' = 0 => constant (integrate)
    assert sp.integrate(0, x) == 0


T.write(check)
