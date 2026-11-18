import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.limits-continuity")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}\frac{\sin 3x}{x}$ equals",
         [r"$3$", r"$1$", r"$\tfrac13$", r"$0$"],
         r"""Write it as a standard form:
$$\lim_{x\to 0}\frac{\sin 3x}{x} = 3\lim_{x\to 0}\frac{\sin 3x}{3x} = 3\cdot 1 = 3.$$
$1$ forgets the scaling factor; $\frac13$ inverts it.""")

T.single(1, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}\frac{e^{2x} - 1}{\sin x}$ equals",
         [r"$2$", r"$1$", r"$\tfrac12$", r"$e^{2}$"],
         r"""$$\frac{e^{2x} - 1}{\sin x} = \frac{e^{2x} - 1}{2x}\cdot\frac{x}{\sin x}\cdot 2 \to 1\cdot 1\cdot 2 = 2.$$
$1$ ignores the factor $2$ in the exponent; $e^2$ wrongly substitutes into the exponential only.""")

T.single(1, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}\frac{2^{x} - 1}{x}$ equals ($\log$ is the natural logarithm)",
         [r"$\log 2$", r"$2$", r"$1$", r"$\tfrac{1}{\log 2}$"],
         r"""Since $2^x = e^{x\log 2}$,
$$\frac{2^x - 1}{x} = \log 2\cdot\frac{e^{x\log 2} - 1}{x\log 2} \to \log 2 \approx 0.693.$$
$1$ would be correct only for base $e$; $\frac{1}{\log 2}$ inverts the answer.""")

T.single(1, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}(1 + 3x)^{1/x}$ equals",
         [r"$e^{3}$", r"$e$", r"$e^{1/3}$", r"$1$"],
         r"""Put $t = 3x$:
$$(1 + 3x)^{1/x} = \left[(1 + t)^{1/t}\right]^{3} \to e^{3}.$$
$1$ treats the $1^\infty$ form as $1$; $e^{1/3}$ inverts the exponent.""")

T.single(1, ["limit-definition", "discontinuities"], r"For the greatest integer function $[x]$, $\displaystyle\lim_{x\to 2-}[x]$ equals",
         [r"$1$", r"$2$", r"$3$", r"does not exist"],
         r"""For $1 \le x < 2$, $[x] = 1$, so the left-hand limit is $1$.
The right-hand limit is $2$ (and $[2] = 2$), so the two-sided limit does not exist, but the **one-sided** limit asked for does. $2$ is the right-hand limit.""")

T.single(1, ["discontinuities"], r"Which function has a **removable** discontinuity at $x = 0$?",
         [r"$f(x) = \frac{\sin x}{x}$ for $x \ne 0$, $f(0) = 0$",
          r"$f(x) = [x]$",
          r"$f(x) = \sin\frac1x$ for $x \ne 0$, $f(0) = 0$",
          r"$f(x) = \frac1x$ for $x \ne 0$, $f(0) = 0$"],
         r"""$\lim_{x\to 0}\frac{\sin x}{x} = 1$ exists but differs from $f(0) = 0$: removable (redefine $f(0) = 1$).

$[x]$ has a jump at $0$ ($-1$ on the left, $0$ on the right). $\sin\frac1x$ oscillates and $\frac1x$ is unbounded: both are of the second kind.""")

T.single(1, ["algebra-sandwich"], r"$\displaystyle\lim_{x\to 0} x\sin\frac{1}{x}$ equals",
         [r"$0$", r"$1$", r"does not exist", r"$\infty$"],
         r"""$$-|x| \le x\sin\frac1x \le |x|,$$
and $\pm|x| \to 0$, so by the sandwich rule the limit is $0$.

$1$ confuses it with $\frac{\sin x}{x}$ (or with $x\sin\frac1x$ as $x \to \infty$). "Does not exist" applies to $\sin\frac1x$, not to its product with $x$.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["continuity", "standard-limits"], r"$f(x) = \dfrac{1 - \cos 2x}{x^2}$ for $x \ne 0$ and $f(0) = k$. $f$ is continuous at $0$ if $k$ equals",
         [r"$2$", r"$1$", r"$\tfrac12$", r"$4$"],
         r"""$1 - \cos 2x = 2\sin^2 x$, so
$$\lim_{x\to 0}\frac{1 - \cos 2x}{x^2} = 2\left(\lim\frac{\sin x}{x}\right)^2 = 2.$$
Continuity needs $k = 2$. $\frac12$ is $\lim\frac{1 - \cos x}{x^2}$; $4$ wrongly uses $1 - \cos 2x \approx \frac{(2x)^2}{2}\cdot 2$.""")

T.single(2, ["continuity"], r"$f(x) = \dfrac{\sqrt{1 + x} - 1}{x}$ for $x \ne 0$, $x \ge -1$, and $f(0) = k$. $f$ is continuous at $0$ if $k$ equals",
         [r"$\tfrac12$", r"$1$", r"$2$", r"$0$"],
         r"""Rationalise:
$$\frac{\sqrt{1 + x} - 1}{x} = \frac{(1 + x) - 1}{x(\sqrt{1 + x} + 1)} = \frac{1}{\sqrt{1 + x} + 1} \to \frac12.$$
So $k = \frac12$. $0$ comes from substituting $x = 0$ in the numerator only; $2$ inverts the result.""")

T.single(2, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}\frac{\log(1 + 2x)}{\sin 5x}$ equals ($\log$ is the natural logarithm)",
         [r"$\tfrac25$", r"$\tfrac52$", r"$1$", r"$\tfrac{2}{5}\log 2$"],
         r"""$$\frac{\log(1 + 2x)}{\sin 5x} = \frac{\log(1 + 2x)}{2x}\cdot\frac{5x}{\sin 5x}\cdot\frac{2}{5} \to \frac25.$$
$\frac52$ swaps the scalings; $1$ ignores them.""")

T.single(2, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}\frac{3^{x} - 2^{x}}{x}$ equals ($\log$ is the natural logarithm)",
         [r"$\log\tfrac32$", r"$\log 6$", r"$1$", r"$\log\tfrac23$"],
         r"""Split into two standard limits:
$$\frac{3^x - 2^x}{x} = \frac{3^x - 1}{x} - \frac{2^x - 1}{x} \to \log 3 - \log 2 = \log\frac32.$$
$\log 6$ adds instead of subtracting; $\log\frac23$ has the sign reversed. Check: for small $x > 0$, $3^x > 2^x$, so the limit is positive.""")

T.single(2, ["standard-limits"], r"$\displaystyle\lim_{x\to\infty}\left(1 + \frac{2}{x}\right)^{3x}$ equals",
         [r"$e^{6}$", r"$e^{2/3}$", r"$e^{3/2}$", r"$e^{5}$"],
         r"""This is a $1^\infty$ form:
$$\lim\left(1 + \frac2x\right)^{3x} = e^{\lim 3x\cdot\frac{2}{x}} = e^{6}.$$
Equivalently $\left[\left(1 + \frac2x\right)^{x}\right]^3 \to (e^2)^3$. $e^5$ adds the exponents instead of multiplying.""")

T.single(2, ["closed-interval"], r"By the intermediate value theorem, the equation $x^3 - x - 1 = 0$ has a root in",
         [r"$(1, 2)$", r"$(0, 1)$", r"$(-1, 0)$", r"$(2, 3)$"],
         r"""Let $p(x) = x^3 - x - 1$, continuous on $\R$.
$$p(1) = -1 < 0, \qquad p(2) = 5 > 0,$$
so Bolzano's theorem gives a root in $(1, 2)$ (it is $\approx 1.3247$).
On $(0, 1)$: $p(0) = -1$, $p(1) = -1$, no sign change; on $(-1, 0)$: $p(-1) = -1$, $p(0) = -1$; on $(2, 3)$: both values are positive. Since $p$ has only one real root, the other intervals contain none.""")

T.single(2, ["discontinuities"], r"Let $f(x) = [x] + [-x]$, where $[\,\cdot\,]$ is the greatest integer function. At each integer $n$, $f$ has",
         [r"a removable discontinuity", r"a jump discontinuity", r"a discontinuity of the second kind", r"no discontinuity"],
         r"""If $x = n$ is an integer, $f(n) = n - n = 0$. If $x$ is not an integer, $[-x] = -[x] - 1$, so $f(x) = -1$.

So $f(n-) = f(n+) = -1 \ne f(n) = 0$: the limit exists but differs from the value, a **removable** discontinuity.
"Jump" is the trap: each of $[x]$ and $[-x]$ jumps at $n$, but the jumps cancel.""")

T.single(2, ["continuity"], r"$f(x) = x^2 + a$ for $x < 1$, $f(1) = 3$, and $f(x) = bx + 1$ for $x > 1$. $f$ is continuous at $x = 1$ if",
         [r"$a = 2,\ b = 2$", r"$a = 3,\ b = 2$", r"$a = 2,\ b = 3$", r"$a = 1,\ b = 2$"],
         r"""Continuity at $1$ needs $f(1-) = f(1) = f(1+)$:
$$f(1-) = 1 + a = 3, \qquad f(1+) = b + 1 = 3.$$
So $a = 2$ and $b = 2$. $a = 3,\ b = 2$ forgets the $1^2$ term; $b = 3$ forgets the $+1$.""")

T.single(2, ["standard-limits"], r"$\displaystyle\lim_{x\to 0}(1 + \sin x)^{\cot x}$ equals",
         [r"$e$", r"$1$", r"$e^{-1}$", r"$0$"],
         r"""A $1^\infty$ form:
$$\lim(1 + \sin x)^{\cot x} = e^{\lim \cot x\cdot\sin x} = e^{\lim\cos x} = e^{1} = e.$$
$1$ treats $1^\infty$ as $1$.""")

T.single(2, ["discontinuities", "exam-tips"], r"The Thomae function $T$ ($T(p/q) = 1/q$ for $p/q$ in lowest terms with $q > 0$, $T(x) = 0$ for irrational $x$) is continuous",
         [r"at every irrational point and at no rational point", r"at every rational point and at no irrational point",
          r"at no point", r"only at $x = 0$"],
         r"""For every $c$, $\lim_{x\to c} T(x) = 0$: in a bounded interval only finitely many rationals have denominator $q \le 1/\varepsilon$, so $T < \varepsilon$ near $c$ except possibly at $c$.

- At irrational $c$: $T(c) = 0$, which equals the limit, so $T$ is continuous.
- At rational $c = p/q$: $T(c) = 1/q \ne 0$, a removable discontinuity. This includes $c = 0 = 0/1$, where $T(0) = 1$.

"At no point" describes the Dirichlet function.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["limit-definition"], r"Let $x_n = \dfrac{2}{(4n + 1)\pi}$. What is $\displaystyle\lim_{n\to\infty}\sin\frac{1}{x_n}$, and what does Heine's definition then give for $\displaystyle\lim_{x\to 0}\sin\frac1x$?",
         [r"$1$; does not exist, since $y_n = \frac{1}{n\pi}$ gives the limit $0$",
          r"$0$; equals $0$",
          r"$1$; equals $1$",
          r"$-1$; does not exist, since $y_n = \frac{1}{n\pi}$ gives the limit $0$"],
         r"""$\frac{1}{x_n} = 2n\pi + \frac{\pi}{2}$, so $\sin\frac{1}{x_n} = 1$ for every $n$, and the limit is $1$.

With $y_n = \frac{1}{n\pi} \to 0$, $\sin\frac{1}{y_n} = \sin n\pi = 0$. Two sequences tending to $0$ give different limits of $f$, so by Heine's definition $\lim_{x\to 0}\sin\frac1x$ does not exist.
"Equals $1$" is wrong: a single sequence cannot prove a limit exists; Heine needs **every** sequence.""")

T.single(3, ["standard-limits", "exam-tips"], r"$\displaystyle\lim_{x\to 0}(\cos x)^{1/x^{2}}$ equals",
         [r"$e^{-1/2}$", r"$e^{1/2}$", r"$1$", r"$e^{-1}$"],
         r"""A $1^\infty$ form:
$$\lim(\cos x)^{1/x^2} = e^{\lim\frac{\cos x - 1}{x^2}} = e^{-1/2},$$
using $\frac{1 - \cos x}{x^2} \to \frac12$. $e^{1/2}$ drops the sign of $\cos x - 1 < 0$; $e^{-1}$ forgets the $\frac12$.
Check: $(\cos 0.1)^{100} \approx 0.6065 \approx e^{-0.5}$.""")

T.single(3, ["limit-definition"], r"For the $\varepsilon$–$\delta$ proof of $\displaystyle\lim_{x\to 3}x^2 = 9$, which choice of $\delta$ works for **every** $\varepsilon > 0$?",
         [r"$\delta = \min\{1, \varepsilon/7\}$", r"$\delta = \varepsilon/7$", r"$\delta = \min\{1, \varepsilon/6\}$", r"$\delta = \varepsilon/6$"],
         r"""If $|x - 3| < \delta$, then $|x^2 - 9| = |x - 3|\,|x + 3| < \delta(6 + \delta)$, and this bound is approached.

- $\delta = \min\{1, \varepsilon/7\}$: $\delta(6 + \delta) \le 7\delta \le \varepsilon$. Works.
- $\delta = \varepsilon/7$: for $\varepsilon = 70$, $\delta = 10$ and $\delta(6 + \delta) = 160 > 70$. Fails.
- $\delta = \min\{1, \varepsilon/6\}$: for $\varepsilon = 1$, $\delta(6 + \delta) = 1 + \frac1{36} > 1$. Fails.
- $\delta = \varepsilon/6$ fails for the same reason.

The restriction $\delta \le 1$ bounds $|x + 3|$ by $7$, not $6$.""")

T.single(3, ["discontinuities", "exam-tips"], r"$f(x) = x$ for rational $x$ and $f(x) = 1 - x$ for irrational $x$. The set of points where $f$ is continuous is",
         [r"$\{\tfrac12\}$", r"$\{0\}$", r"$\{0, 1\}$", r"empty"],
         r"""Near any $c$ there are rationals (values near $c$) and irrationals (values near $1 - c$). So $\lim_{x\to c} f$ exists only if $c = 1 - c$, i.e. $c = \frac12$.

At $c = \frac12$: $|f(x) - \tfrac12| = |x - \tfrac12|$ in both cases, so $f$ is continuous there (take $\delta = \varepsilon$).
$\{0\}$ is the answer for $f(x) = x$ on $\Q$, $0$ off $\Q$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["closed-interval"], r"Consider the following statements about real functions.",
             [r"Every function continuous on $(0, 1)$ is bounded on $(0, 1)$.",
              r"Every function continuous on $[a, b]$ attains its supremum on $[a, b]$.",
              r"Every continuous $f\colon [0, 1] \to [0, 1]$ satisfies $f(c) = c$ for some $c \in [0, 1]$."],
             [r"2 and 3 only", r"1 and 2 only", r"2 only", r"1, 2 and 3"],
             r"""1. **False.** $f(x) = \frac1x$ is continuous on $(0, 1)$ and unbounded; the interval must be closed.
2. **True.** This is the extreme value theorem for a continuous function on a closed bounded interval.
3. **True.** Let $g(x) = f(x) - x$. Then $g(0) = f(0) \ge 0$ and $g(1) = f(1) - 1 \le 0$, so by the intermediate value property $g(c) = 0$ for some $c$.""")

T.statements(3, ["algebra-sandwich", "continuity"], r"Consider the following statements, where $c, L, M \in \R$.",
             [r"$\lim_{x\to c}\,(f + g)(x)$ can exist even when neither $\lim_{x\to c} f(x)$ nor $\lim_{x\to c} g(x)$ exists.",
              r"If $f$ is continuous at $c$ and $g$ is continuous at $f(c)$, then $g \circ f$ is continuous at $c$.",
              r"If $\lim_{x\to c} f(x) = L$ and $\lim_{y\to L} g(y) = M$, then $\lim_{x\to c} g(f(x)) = M$."],
             [r"1 and 2 only", r"2 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. **True.** $f = \sin\frac1x$, $g = -\sin\frac1x$: neither has a limit at $0$, but $f + g = 0$.
2. **True.** This is the composite-function theorem.
3. **False.** Take $f \equiv 0$ and $g(y) = 0$ for $y \ne 0$, $g(0) = 1$. Then $L = 0$, $M = \lim_{y\to 0}g(y) = 0$, but $g(f(x)) = 1$ for all $x$. The statement needs $g$ continuous at $L$ (or $f(x) \ne L$ near $c$).""")

# ---------------------------------------------------------------- match
T.match(2, ["discontinuities", "algebra-sandwich"], r"Match each function (defined as shown, with the stated value at $0$) with its behaviour at $x = 0$.",
        [r"A. $\frac{\sin x}{x}$, $f(0) = 0$", r"B. $[x]$", r"C. $\sin\frac1x$, $f(0) = 0$", r"D. $x\sin\frac1x$, $f(0) = 0$"],
        [r"1. continuous", r"2. removable discontinuity", r"3. jump discontinuity", r"4. discontinuity of the second kind"],
        [r"A-2, B-3, C-4, D-1", r"A-1, B-3, C-4, D-2", r"A-2, B-4, C-3, D-1", r"A-3, B-2, C-4, D-1"],
        r"""- **A.** The limit $1$ exists but $\ne f(0) = 0$: removable (2).
- **B.** $[0-] = -1$, $[0+] = 0$: jump (3).
- **C.** Neither one-sided limit exists (oscillation): second kind (4).
- **D.** $x\sin\frac1x \to 0 = f(0)$ by the sandwich rule: continuous (1).

A-2, B-3, C-4, D-1.""")

T.match(1, ["standard-limits"], r"Match each limit (as $x \to 0$; $a > 0$, $\log$ natural) with its value.",
        [r"A. $\frac{a^x - 1}{x}$", r"B. $\frac{\log(1 + x)}{x}$", r"C. $(1 + x)^{1/x}$", r"D. $\frac{1 - \cos x}{x^2}$"],
        [r"1. $e$", r"2. $\frac12$", r"3. $\log a$", r"4. $1$"],
        [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-1, C-4, D-2", r"A-3, B-4, C-2, D-1"],
        r"""- **A.** $a^x = e^{x\log a}$, so the limit is $\log a$ (3).
- **B.** Standard: $1$ (4).
- **C.** Definition of $e$: $e$ (1).
- **D.** $1 - \cos x = 2\sin^2\frac{x}{2}$, giving $\frac12$ (2).

A-3, B-4, C-1, D-2.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["closed-interval"],
                   r"The equation $x^3 - 3x + 1 = 0$ has a root in $(0, 1)$.",
                   r"If $f$ is continuous on $[a, b]$ and $f(a)f(b) < 0$, then $f(c) = 0$ for some $c \in (a, b)$.",
                   0,
                   r"""Both are true. $p(x) = x^3 - 3x + 1$ is continuous with $p(0) = 1 > 0$ and $p(1) = -1 < 0$, so R (Bolzano's theorem) gives a root in $(0, 1)$ (it is $\approx 0.347$). R is exactly the reason for A.""")

T.assertion_reason(2, ["closed-interval"],
                   r"$f(x) = \frac{1}{x - 1}$ for $x \ne 1$, $f(1) = 0$, attains a maximum value on $[0, 2]$.",
                   r"A function continuous on a closed bounded interval is bounded and attains its bounds.",
                   3,
                   r"""R is the extreme value theorem: true.

A is false: $f(x) \to +\infty$ as $x \to 1+$, so $f$ is unbounded above on $[0, 2]$ and has no maximum. R does not apply because $f$ is not continuous at $1$.""")

T.assertion_reason(2, ["algebra-sandwich"],
                   r"$\displaystyle\lim_{x\to 0} x\sin\frac{1}{x} = 0$.",
                   r"$\displaystyle\lim_{x\to 0}\sin\frac{1}{x} = 0$.",
                   2,
                   r"""A is true by the sandwich rule: $|x\sin\frac1x| \le |x| \to 0$.

R is false: along $x_n = \frac{1}{n\pi}$ the values are $0$, but along $\frac{2}{(4n + 1)\pi}$ they are $1$, so the limit does not exist. A holds because $\sin\frac1x$ is **bounded**, not because it has a limit.""")

T.assertion_reason(3, ["discontinuities", "continuity"],
                   r"The Dirichlet function ($1$ on $\Q$, $0$ on $\R\setminus\Q$) is discontinuous at every real number.",
                   r"A function continuous at a point $c$ is bounded on some neighbourhood of $c$.",
                   1,
                   r"""A is true: every interval around $c$ contains rationals (value $1$) and irrationals (value $0$), so $\lim_{x\to c} D(x)$ does not exist for any $c$.

R is true: take $\varepsilon = 1$ in the definition of continuity, so $|f(x)| < |f(c)| + 1$ near $c$.

But R does not explain A: the Dirichlet function is bounded everywhere, so boundedness says nothing about its discontinuity. The reason is the density of $\Q$ and $\R\setminus\Q$.""")

T.assertion_reason(3, ["inverse-functions"],
                   r"$f(x) = x^5 + x$ has an inverse $f^{-1}\colon \R \to \R$ which is continuous.",
                   r"If $f$ is strictly increasing and continuous on an interval $I$, then $f^{-1}$ exists on the interval $f(I)$ and is strictly increasing and continuous.",
                   0,
                   r"""R is the inverse function theorem for monotone functions: true.

A: $f'(x) = 5x^4 + 1 > 0$, so $f$ is strictly increasing and continuous on $\R$, and $f(x) \to \pm\infty$ as $x \to \pm\infty$, so $f(\R) = \R$ by the IVT. By R, $f^{-1}\colon \R \to \R$ is continuous. A is true and R explains it.""")


def check():
    import sympy as sp
    x, y, n, eps = sp.symbols("x y n epsilon", real=True)
    L = sp.limit
    # singles
    eq(L(sp.sin(3*x)/x, x, 0), 3, "q1")
    eq(L((sp.exp(2*x) - 1)/sp.sin(x), x, 0), 2, "q2")
    eq(L((2**x - 1)/x, x, 0), sp.log(2), "q3")
    eq(L((1 + 3*x)**(1/x), x, 0), sp.exp(3), "q4")
    eq(L(sp.floor(x), x, 2, "-"), 1, "q5")
    eq(L(sp.floor(x), x, 2, "+"), 2, "q5 right")
    eq(L(sp.sin(x)/x, x, 0), 1, "q6")
    eq(L(sp.floor(x), x, 0, "-"), -1, "q6 floor left")
    eq(L(sp.floor(x), x, 0, "+"), 0, "q6 floor right")
    assert L(1/x, x, 0, "+") == sp.oo
    eq(L(x*sp.sin(1/x), x, 0), 0, "q7")
    eq(L(abs(x), x, 0), 0, "q7 sandwich bound")
    eq(L((1 - sp.cos(2*x))/x**2, x, 0), 2, "q8")
    eq(L((sp.sqrt(1 + x) - 1)/x, x, 0), sp.Rational(1, 2), "q9")
    eq(L(sp.log(1 + 2*x)/sp.sin(5*x), x, 0), sp.Rational(2, 5), "q10")
    eq(L((3**x - 2**x)/x, x, 0), sp.log(sp.Rational(3, 2)), "q11")
    eq(L((1 + 2/x)**(3*x), x, sp.oo), sp.exp(6), "q12")
    p = x**3 - x - 1
    assert p.subs(x, 1) < 0 < p.subs(x, 2)
    assert all(p.subs(x, a)*p.subs(x, b) > 0 for a, b in [(0, 1), (-1, 0), (2, 3)])
    assert len(sp.real_roots(p)) == 1
    r = sp.nsolve(p, x, 1.3); assert 1 < r < 2
    # q14: [x]+[-x]
    f14 = sp.floor(x) + sp.floor(-x)
    for k in (-2, 0, 3):
        eq(f14.subs(x, k), 0, "q14 value")
        eq(L(f14, x, k, "-"), -1, "q14 left")
        eq(L(f14, x, k, "+"), -1, "q14 right")
    a, b = sp.symbols("a b")
    sol = sp.solve([1 + a - 3, b*1 + 1 - 3], [a, b])
    eq(sol[a], 2, "q15 a"); eq(sol[b], 2, "q15 b")
    eq(L((1 + sp.sin(x))**sp.cot(x), x, 0), sp.E, "q16")
    # q17 Thomae: T(0)=1 since 0 = 0/1; T(1/2)=1/2 != 0 = the limit; spot values
    assert sp.Rational(0).q == 1 and sp.Rational(3, 6).q == 2
    # q18 Heine
    kk = sp.symbols("k", integer=True, positive=True)
    eq(sp.sin(1/(2/((4*kk + 1)*sp.pi))), 1, "q18 xn")
    eq(sp.sin(1/(1/(kk*sp.pi))), 0, "q18 yn")
    eq(L(2/((4*n + 1)*sp.pi), n, sp.oo), 0, "q18 xn->0")
    eq(L(sp.cos(x)**(1/x**2), x, 0), sp.exp(-sp.Rational(1, 2)), "q19")
    assert abs(sp.N(sp.cos(sp.Rational(1, 10))**100 - sp.exp(-sp.Rational(1, 2)))) < 1e-3
    # q20: sup |x^2-9| over |x-3|<d is d(6+d)
    bound = lambda d: d*(6 + d)
    d1 = lambda e: sp.Min(1, e/7)
    for e in [sp.Rational(1, 100), 1, 7, 70, 1000]:
        assert bound(d1(e)) <= e
    assert bound(sp.Rational(70, 7)) > 70            # eps/7 fails at eps = 70
    assert bound(sp.Min(1, sp.Rational(1, 6))) > 1   # min{1, eps/6} fails at eps = 1
    assert bound(sp.Rational(1, 6)) > 1              # eps/6 fails at eps = 1
    # q21: continuity only where x = 1 - x
    eq(sp.solve(sp.Eq(x, 1 - x), x)[0], sp.Rational(1, 2), "q21")
    # statements 1: 1/x unbounded on (0,1); fixed point example
    assert L(1/x, x, 0, "+") == sp.oo
    g = sp.cos(x) - x   # f = cos maps [0,1] into [0,1]
    assert g.subs(x, 0) >= 0 and sp.N(g.subs(x, 1)) <= 0
    # statements 2: f+g with f = sin(1/x), g = -sin(1/x) is identically 0
    eq(sp.sin(1/x) + (-sp.sin(1/x)), 0, "st2-1")
    gp = sp.Piecewise((1, sp.Eq(y, 0)), (0, True))
    eq(gp.subs(y, sp.Rational(1, 10**6)), 0, "st2-3 g near 0")
    eq(gp.subs(y, 0), 1, "st2-3 g(f(x))")
    # match 1
    eq(L(sp.sin(x)/x, x, 0), 1, "m1 A")
    eq(L(x*sp.sin(1/x), x, 0), 0, "m1 D")
    # match 2
    A = sp.symbols("a", positive=True)
    eq(L((A**x - 1)/x, x, 0), sp.log(A), "m2 A")
    eq(L(sp.log(1 + x)/x, x, 0), 1, "m2 B")
    eq(L((1 + x)**(1/x), x, 0), sp.E, "m2 C")
    eq(L((1 - sp.cos(x))/x**2, x, 0), sp.Rational(1, 2), "m2 D")
    # AR1
    q = x**3 - 3*x + 1
    assert q.subs(x, 0) > 0 > q.subs(x, 1)
    # AR2
    assert L(1/(x - 1), x, 1, "+") == sp.oo
    # AR3: two sequences give different values
    eq(sp.sin((4*kk + 1)*sp.pi/2), 1, "ar3"); eq(sp.sin(kk*sp.pi), 0, "ar3b")
    # AR5
    f5 = x**5 + x
    assert sp.solve(sp.diff(f5, x), x, domain=sp.S.Reals) == [] or all(not s.is_real for s in sp.solve(sp.diff(f5, x), x))
    assert L(f5, x, sp.oo) == sp.oo and L(f5, x, -sp.oo) == -sp.oo
    eq(f5.subs(x, 1), 2, "ar5 f(1)=2")


T.write(check)
