import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.taylor-series")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["taylor-theorem"],
         r"Let $f^{(n)}$ be continuous on $[a, a + h]$ and $f^{(n+1)}$ exist on $(a, a + h)$. In $f(a + h) = \sum_{k=0}^{n}\frac{h^k}{k!}f^{(k)}(a) + R_{n+1}$, the Lagrange form of $R_{n+1}$ is ($0 < \theta < 1$)",
         [r"$\dfrac{h^{n+1}}{(n+1)!}f^{(n+1)}(a + \theta h)$", r"$\dfrac{h^{n+1}}{n!}f^{(n+1)}(a + \theta h)$",
          r"$\dfrac{h^{n+1}(1 - \theta)^n}{(n+1)!}f^{(n+1)}(a + \theta h)$", r"$\dfrac{h^{n+1}}{(n+1)!}f^{(n+1)}(\theta h)$"],
         r"""The Lagrange remainder looks like the next term of the series, evaluated at an intermediate point:
$$R_{n+1} = \frac{h^{n+1}}{(n+1)!}f^{(n+1)}(a + \theta h).$$
The factor $(1 - \theta)^n$ belongs to the Cauchy form, which has $n!$ (not $(n+1)!$) in the denominator. Writing $f^{(n+1)}(\theta h)$ forgets that the intermediate point lies between $a$ and $a + h$.
Check with $n = 0$: you must get Lagrange's MVT, $f(a + h) = f(a) + hf'(a + \theta h)$.""")

T.single(1, ["standard-expansions"], r"For $a > 0$, the coefficient of $x^n$ in the Maclaurin series of $a^x$ is",
         [r"$\dfrac{(\ln a)^n}{n!}$", r"$\dfrac{a^n}{n!}$", r"$(\ln a)^n$", r"$\dfrac{(\ln a)^{n-1}}{n!}$"],
         r"""$a^x = e^{x\ln a}$, so
$$a^x = \sum_{n=0}^{\infty}\frac{(x\ln a)^n}{n!}, \qquad c_n = \frac{(\ln a)^n}{n!}.$$
$\frac{a^n}{n!}$ treats $a^x$ like $e^{ax}$. Check with $a = e$: the coefficient must reduce to $\frac{1}{n!}$, which only the first option does.""")

T.single(1, ["standard-expansions"], r"The largest set of real $x$ on which the Maclaurin series of $\log(1 + x)$ converges to $\log(1 + x)$ is",
         [r"$-1 < x \le 1$", r"$-1 \le x \le 1$", r"$-1 < x < 1$", r"$-1 \le x < 1$"],
         r"""For $\lvert x\rvert < 1$ the remainder tends to $0$ (Lagrange form on $[0, 1)$, Cauchy form on $(-1, 0)$). At $x = 1$ the Lagrange remainder satisfies $\lvert R_{n+1}\rvert \le \frac{1}{n + 1} \to 0$, giving
$$\log 2 = 1 - \tfrac12 + \tfrac13 - \cdots.$$
At $x = -1$ the series is $-(1 + \frac12 + \frac13 + \cdots)$, which diverges, and $\log 0$ is undefined. So the set is $(-1, 1]$.
$[-1, 1)$ is the range for $-\log(1 - x)$, the mirror series.""")

T.single(1, ["expansion-by-series"], r"Up to the term in $x^3$, the Maclaurin expansion of $e^x\sin x$ is",
         [r"$x + x^2 + \dfrac{x^3}{3}$", r"$x + x^2 + \dfrac{x^3}{6}$", r"$x + x^2 - \dfrac{x^3}{3}$", r"$x - x^2 + \dfrac{x^3}{3}$"],
         r"""Multiply the series and keep powers up to $x^3$:
$$\left(1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6}\right)\left(x - \tfrac{x^3}{6}\right) = x + x^2 + \left(\tfrac12 - \tfrac16\right)x^3 + \cdots = x + x^2 + \tfrac{x^3}{3} + \cdots$$
$\frac{x^3}{6}$ forgets the $-\frac{x^3}{6}$ from $\sin x$, or the $\frac{x^2}{2}\cdot x$ product. Check: $f'(0) = 1$ and $f''(0) = 2$, so $c_2 = 1$, ruling out $-x^2$.""")

T.single(1, ["non-analytic"], r"Let $f(x) = e^{-1/x^2}$ for $x \ne 0$ and $f(0) = 0$. The Maclaurin series of $f$ is",
         [r"identically $0$, since $f^{(n)}(0) = 0$ for every $n$",
          r"$1 - x^2 + \dfrac{x^4}{2!} - \cdots$",
          r"not defined, since $f'(0)$ does not exist",
          r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n!\,x^{2n}}$"],
         r"""Each derivative for $x \ne 0$ is $P_n(1/x)e^{-1/x^2}$, and $t^k e^{-t^2} \to 0$ as $\lvert t\rvert \to \infty$. So every difference quotient at $0$ tends to $0$, and $f^{(n)}(0) = 0$ for all $n$. The Maclaurin series is $0 + 0x + 0x^2 + \cdots$.
$1 - x^2 + \frac{x^4}{2!} - \cdots$ is the series of $e^{-x^2}$, a different function. The last option is the series of $e^{-1/x^2}$ in powers of $1/x$, not a Maclaurin series.""")

T.single(1, ["standard-expansions"], r"In the Maclaurin series of $\cos x$, the coefficient of $x^6$ is",
         [r"$-\dfrac{1}{720}$", r"$\dfrac{1}{720}$", r"$-\dfrac{1}{120}$", r"$\dfrac{1}{24}$"],
         r"""$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$, and the signs alternate starting with $+1$. So the coefficient of $x^6$ is
$$-\frac{1}{6!} = -\frac{1}{720}.$$
$+\frac{1}{720}$ is the sign slip; $\frac{1}{24}$ is the $x^4$ coefficient.""")

T.single(1, ["standard-expansions"], r"Which of these functions is represented by its Maclaurin series for every real $x$?",
         [r"$\cos x$", r"$\log(1 + x)$", r"$\tan^{-1}x$", r"$(1 + x)^{1/2}$"],
         r"""All derivatives of $\cos x$ are bounded by $1$, so the Lagrange remainder satisfies
$$\lvert R_{n+1}\rvert \le \frac{\lvert x\rvert^{n+1}}{(n+1)!} \to 0 \quad\text{for every } x.$$
The others are valid only on bounded sets: $\log(1 + x)$ on $(-1, 1]$, $\tan^{-1}x$ on $[-1, 1]$ and $(1 + x)^{1/2}$ on $[-1, 1]$. ($\tan^{-1}x$ is defined for all $x$, but its series diverges for $\lvert x\rvert > 1$.)""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["expansion-by-series"], r"In the Maclaurin series of $\sqrt{1 + x}$, the coefficient of $x^3$ is",
         [r"$\dfrac{1}{16}$", r"$-\dfrac{1}{16}$", r"$\dfrac18$", r"$\dfrac{3}{16}$"],
         r"""$$\binom{1/2}{3} = \frac{\frac12\left(-\frac12\right)\left(-\frac32\right)}{3!} = \frac{3/8}{6} = \frac{1}{16}.$$
Two negative factors make it positive, so $-\frac{1}{16}$ is a sign slip. $\frac18$ is the size of the $x^2$ coefficient ($-\frac18$). $\frac{3}{16}$ forgets to divide by $3!$ correctly.""")

T.single(2, ["expansion-by-series"], r"Up to the term in $x^3$, the Maclaurin expansion of $\log(1 + \sin x)$ is",
         [r"$x - \dfrac{x^2}{2} + \dfrac{x^3}{6}$", r"$x - \dfrac{x^2}{2} + \dfrac{x^3}{3}$", r"$x - \dfrac{x^2}{2} - \dfrac{x^3}{6}$", r"$x + \dfrac{x^2}{2} + \dfrac{x^3}{6}$"],
         r"""Put $s = \sin x = x - \frac{x^3}{6} + \cdots$ into $\log(1 + s) = s - \frac{s^2}{2} + \frac{s^3}{3} - \cdots$:
$$\left(x - \tfrac{x^3}{6}\right) - \frac{x^2}{2} + \frac{x^3}{3} + \cdots = x - \frac{x^2}{2} + \frac{x^3}{6} + \cdots$$
$\frac{x^3}{3}$ copies $\log(1 + x)$ and forgets the $-\frac{x^3}{6}$ from $\sin x$; $-\frac{x^3}{6}$ forgets the $\frac{s^3}{3}$ term.""")

T.single(2, ["taylor-theorem"],
         r"For $f(x) = (1 - x)^{5/2}$, Taylor's theorem with Lagrange remainder gives $f(1) = f(0) + f'(0) + \frac{1}{2!}f''(\theta)$ with $0 < \theta < 1$. Then $\theta$ equals",
         [r"$\dfrac{9}{25}$", r"$\dfrac{16}{25}$", r"$\dfrac{1}{3}$", r"$\dfrac{4}{5}$"],
         r"""$f(0) = 1$, $f(1) = 0$, $f'(x) = -\frac52(1 - x)^{3/2}$ and $f''(x) = \frac{15}{4}(1 - x)^{1/2}$. So
$$0 = 1 - \frac52 + \frac12\cdot\frac{15}{4}\sqrt{1 - \theta} \;\Rightarrow\; \sqrt{1 - \theta} = \frac45 \;\Rightarrow\; \theta = 1 - \frac{16}{25} = \frac{9}{25}.$$
$\frac{16}{25}$ is $1 - \theta$, and $\frac45$ is $\sqrt{1 - \theta}$. $\frac13$ is only the limiting value of $\theta$ as $h \to 0$.""")

T.single(2, ["expansion-by-series"], r"If $f(x) = x^2e^x$, then $f^{(10)}(0)$ equals",
         [r"$90$", r"$45$", r"$720$", r"$\dfrac{1}{8!}$"],
         r"""$f(x) = \sum_{k \ge 0}\frac{x^{k+2}}{k!}$, so the coefficient of $x^{10}$ is $c_{10} = \frac{1}{8!}$. Then
$$f^{(10)}(0) = 10!\,c_{10} = \frac{10!}{8!} = 90.$$
$\frac{1}{8!}$ is the coefficient, not the derivative. $45 = \binom{10}{2}$ forgets the factor $2$ from $(x^2)''$ in Leibniz's rule: $\binom{10}{2}\cdot 2 = 90$.""")

T.single(2, ["expansion-by-series"], r"If $f(x) = \tan^{-1}x$, then $f^{(5)}(0)$ equals",
         [r"$24$", r"$-24$", r"$\dfrac15$", r"$120$"],
         r"""$\tan^{-1}x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$, so $c_5 = +\frac15$ and
$$f^{(5)}(0) = 5!\cdot\frac15 = 24.$$
$\frac15$ is the coefficient itself. $-24$ takes the sign of the $x^3$ term; the $x^5$ term is positive.""")

T.single(2, ["error-estimates"],
         r"Using the Lagrange remainder with $e^{\theta} < 3$, the smallest $n$ for which $\sum_{k=0}^{n}\frac{1}{k!}$ is guaranteed to approximate $e$ with error less than $10^{-3}$ is",
         [r"$n = 6$", r"$n = 5$", r"$n = 7$", r"$n = 4$"],
         r"""$e - \sum_{k=0}^{n}\frac{1}{k!} = \frac{e^\theta}{(n+1)!} < \frac{3}{(n+1)!}$. We need
$$\frac{3}{(n+1)!} < 10^{-3} \iff (n+1)! > 3000.$$
$6! = 720$ fails and $7! = 5040$ works, so $n + 1 = 7$ and $n = 6$ (seven terms, sum $2.71806$, true error $0.00023$).
$n = 5$ gives a true error of $0.0016$, too large. $n = 7$ wrongly solves $n! > 3000$.""")

T.single(2, ["expansion-by-series"], r"Up to the term in $x^5$, the Maclaurin expansion of $\tan x$ is",
         [r"$x + \dfrac{x^3}{3} + \dfrac{2x^5}{15}$", r"$x + \dfrac{x^3}{3} + \dfrac{x^5}{5}$", r"$x - \dfrac{x^3}{3} + \dfrac{2x^5}{15}$", r"$x + \dfrac{x^3}{6} + \dfrac{x^5}{120}$"],
         r"""Divide $\sin x$ by $\cos x$: write $\tan x = x + a x^3 + b x^5$ and match $\sin x = \tan x\cos x$:
$$x^3:\ a - \tfrac12 = -\tfrac16 \Rightarrow a = \tfrac13, \qquad x^5:\ b - \tfrac{a}{2} + \tfrac{1}{24} = \tfrac{1}{120} \Rightarrow b = \tfrac{2}{15}.$$
$x - \frac{x^3}{3} + \cdots$ is the start of $\tan^{-1}x$; $\frac{x^5}{5}$ guesses the arctan pattern with a plus sign. The last option is the series of $\sinh x$.""")

T.single(2, ["error-estimates"],
         r"$\sin x$ is approximated by $x - \frac{x^3}{6}$. Using the Lagrange remainder after the $x^4$ term (whose coefficient is $0$), the error bound at $x = 0.1$ is about",
         [r"$8.3 \times 10^{-8}$", r"$4.2 \times 10^{-6}$", r"$1.7 \times 10^{-4}$", r"$2.0 \times 10^{-11}$"],
         r"""The degree-4 Taylor polynomial of $\sin x$ is $x - \frac{x^3}{6}$, and
$$R_5 = \frac{x^5}{5!}\cos\theta x, \qquad \lvert R_5\rvert \le \frac{(0.1)^5}{120} \approx 8.3 \times 10^{-8}.$$
$4.2 \times 10^{-6} = \frac{(0.1)^4}{24}$ is the weaker bound from stopping after the $x^3$ term. $1.7 \times 10^{-4} = \frac{(0.1)^3}{6}$ is the last kept term, and $2.0 \times 10^{-11} = \frac{(0.1)^7}{5040}$ skips a term.""")

T.single(2, ["expansion-by-series"], r"The coefficient of $x^n$ in the Maclaurin series of $\dfrac{e^x}{1 - x}$ ($\lvert x\rvert < 1$) is",
         [r"$\displaystyle\sum_{k=0}^{n}\frac{1}{k!}$", r"$\dfrac{1}{n!}$", r"$\displaystyle\sum_{k=0}^{n-1}\frac{1}{k!}$", r"$\dfrac{n + 1}{n!}$"],
         r"""Multiply $e^x = \sum \frac{x^k}{k!}$ by $\frac{1}{1 - x} = \sum x^j$. The term $x^n$ arises from $x^k\cdot x^{n-k}$ for $k = 0, \dots, n$, so
$$c_n = \sum_{k=0}^{n}\frac{1}{k!}.$$
Check $n = 1$: $\frac{e^x}{1 - x} = (1 + x + \cdots)(1 + x + \cdots) = 1 + 2x + \cdots$, and $\frac{1}{0!} + \frac{1}{1!} = 2$. The sum to $n - 1$ gives $1$; $\frac{n + 1}{n!}$ gives $2$ here but $\frac32 \ne \frac52$ at $n = 2$.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["limits-by-series"], r"$\displaystyle\lim_{x \to 0}\left(\frac{1}{x^2} - \frac{1}{\sin^2 x}\right)$ equals",
         [r"$-\dfrac13$", r"$\dfrac13$", r"$0$", r"$-\dfrac16$"],
         r"""$\sin^2 x = x^2 - \frac{x^4}{3} + \cdots$, so
$$\frac{1}{\sin^2x} = \frac{1}{x^2}\left(1 - \frac{x^2}{3} + \cdots\right)^{-1} = \frac{1}{x^2} + \frac13 + \cdots$$
Hence the limit is $-\frac13$. $+\frac13$ is the sign slip (it is $\lim\left(\frac{1}{\sin^2x} - \frac{1}{x^2}\right)$). $-\frac16$ uses $\sin x$ instead of $\sin^2x$.""")

T.single(3, ["limits-by-series"], r"$\displaystyle\lim_{x \to 0}\frac{e - (1 + x)^{1/x}}{x}$ equals",
         [r"$\dfrac{e}{2}$", r"$-\dfrac{e}{2}$", r"$e$", r"$\dfrac12$"],
         r"""$\frac{\log(1 + x)}{x} = 1 - \frac{x}{2} + \frac{x^2}{3} - \cdots$, so
$$(1 + x)^{1/x} = e\cdot e^{-x/2 + \cdots} = e\left(1 - \frac{x}{2} + \cdots\right), \qquad e - (1 + x)^{1/x} = \frac{e}{2}x + \cdots$$
The limit is $\frac{e}{2}$. $-\frac{e}{2}$ is $\lim\frac{(1 + x)^{1/x} - e}{x}$; $\frac12$ forgets the factor $e$.""")

T.single(3, ["expansion-by-series"], r"In the Maclaurin series of $e^{\sin x}$, the coefficient of $x^4$ is",
         [r"$-\dfrac18$", r"$\dfrac{1}{24}$", r"$0$", r"$\dfrac18$"],
         r"""Put $s = \sin x = x - \frac{x^3}{6} + \cdots$ into $e^s = 1 + s + \frac{s^2}{2} + \frac{s^3}{6} + \frac{s^4}{24} + \cdots$ and collect $x^4$:
$$\frac{s^2}{2}:\ \frac12\cdot 2\cdot x\cdot\left(-\frac{x^3}{6}\right) = -\frac{x^4}{6}, \qquad \frac{s^4}{24}:\ \frac{x^4}{24}.$$
Total: $-\frac16 + \frac1{24} = -\frac{3}{24} = -\frac18$. ($s$ and $\frac{s^3}{6}$ have no $x^4$ term.)
$\frac{1}{24}$ keeps only $\frac{s^4}{24}$, as if $\sin x = x$.""")

T.single(3, ["taylor-theorem"],
         r"Let $f'''$ be continuous near $a$ with $f'''(a) \ne 0$, and $f(a + h) = f(a) + hf'(a) + \frac{h^2}{2}f''(a + \theta h)$, $0 < \theta < 1$. As $h \to 0$, $\theta$ tends to",
         [r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac16$", r"$\dfrac23$"],
         r"""Expand both sides one step further. The left side is $f(a) + hf'(a) + \frac{h^2}{2}f''(a) + \frac{h^3}{6}f'''(a + \theta_1 h)$; the right side, by the MVT on $f''$, is $f(a) + hf'(a) + \frac{h^2}{2}\left(f''(a) + \theta h f'''(a + \theta_2\theta h)\right)$. Comparing,
$$\frac{h^3}{6}f'''(a + \theta_1 h) = \frac{\theta h^3}{2}f'''(a + \theta_2\theta h) \;\Rightarrow\; \theta \to \frac{1}{3}.$$
Check with $f = x^3$, $a = 0$: $h^3 = \frac{h^2}{2}\cdot 6\theta h$ gives $\theta = \frac13$ exactly. $\frac12$ is the limit for Lagrange's MVT (one term fewer).""")

T.single(3, ["standard-expansions"], r"The largest set of real $x$ on which the binomial series of $(1 + x)^{-1/2}$ converges to $(1 + x)^{-1/2}$ is",
         [r"$-1 < x \le 1$", r"$-1 \le x \le 1$", r"$-1 < x < 1$", r"$-1 \le x < 1$"],
         r"""For $\lvert x\rvert < 1$ it converges to the function (Cauchy remainder). At the endpoints, with $m = -\frac12 \in (-1, 0)$:
- $x = 1$: the series $1 - \frac12 + \frac38 - \frac{5}{16} + \cdots$ alternates with terms decreasing to $0$, so it converges (conditionally), and by Abel's theorem the sum is $2^{-1/2}$.
- $x = -1$: all terms are positive, $\binom{-1/2}{n}(-1)^n = \frac{(2n)!}{4^n(n!)^2} \sim \frac{1}{\sqrt{\pi n}}$, so it diverges (and $(1 + x)^{-1/2}$ is undefined).

So the set is $(-1, 1]$. $(-1, 1)$ forgets the conditional convergence at $x = 1$, which happens exactly when $-1 < m < 0$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["standard-expansions"], r"Consider the following statements about Maclaurin series ($\log$ is the natural logarithm):",
             [r"The series of $\log(1 + x)$ converges to $\log(1 + x)$ for every $x$ with $-1 < x \le 1$.",
              r"The series of $\tan^{-1}x$ converges to $\tan^{-1}x$ only for $-1 < x < 1$.",
              r"The series $1 - x + x^2 - x^3 + \cdots$ of $(1 + x)^{-1}$ converges at $x = 1$."],
             [r"1 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** Lagrange remainder on $[0, 1]$, Cauchy remainder on $(-1, 0)$.
- **2 is false:** at $x = \pm 1$ the arctan series is alternating with terms decreasing to $0$, so it converges, and the sum is $\pm\frac{\pi}{4}$. The range is $[-1, 1]$.
- **3 is false:** at $x = 1$ the series is $1 - 1 + 1 - \cdots$, whose partial sums oscillate between $1$ and $0$.

So only statement 1 is correct.""")

T.statements(3, ["taylor-theorem"],
             r"Let $f^{(n)}$ be continuous on $[a, a + h]$ and $f^{(n+1)}$ exist on $(a, a + h)$, and let $R_{n+1}$ be the remainder after the term in $h^n$ in Taylor's theorem. Consider the following statements:",
             [r"The number $\theta$ in the remainder can be taken in the open interval $(0, 1)$.",
              r"The Cauchy form is $R_{n+1} = \dfrac{h^{n+1}(1 - \theta)^n}{n!}f^{(n+1)}(a + \theta h)$.",
              r"For given $f$, $a$, $h$ and $n$, the $\theta$ of the Lagrange form and the $\theta$ of the Cauchy form are always equal."],
             [r"1 and 2 only", r"1, 2 and 3", r"2 only", r"1 and 3 only"],
             r"""- **1 is true:** Rolle's theorem gives a point strictly inside $(a, a + h)$, i.e. $\theta \in (0, 1)$.
- **2 is true:** this is the Schlömilch–Roche form with $p = 1$.
- **3 is false:** take $f(x) = x^3$, $a = 0$, $n = 1$. Lagrange: $h^3 = \frac{h^2}{2}\cdot 6\theta h$ gives $\theta = \frac13$. Cauchy: $h^3 = h^2(1 - \theta)\cdot 6\theta h$ gives $\theta(1 - \theta) = \frac16$, so $\theta = \frac{3 \pm \sqrt3}{6}$, neither of which is $\frac13$.

So 1 and 2 only.""")

# ---------------------------------------------------------------- match
T.match(1, ["standard-expansions"], r"Match each function in List I with the largest set on which its Maclaurin series converges to it (List II).",
        [r"$e^x$", r"$\log(1 + x)$", r"$\tan^{-1}x$", r"$(1 + x)^{-1}$"],
        [r"$-1 < x \le 1$", r"$-1 < x < 1$", r"all real $x$", r"$-1 \le x \le 1$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-4, C-1, D-2", r"A-3, B-1, C-2, D-4", r"A-4, B-1, C-3, D-2"],
        r"""- A: $e^x$, Lagrange remainder $\frac{x^{n+1}e^{\theta x}}{(n+1)!} \to 0$ for every $x$: **3**.
- B: $\log(1 + x)$ converges at $x = 1$ (to $\log 2$) but not at $x = -1$: **1**.
- C: $\tan^{-1}x$ converges at both $x = \pm1$ (Leibniz test): **4**.
- D: $(1 + x)^{-1} = 1 - x + x^2 - \cdots$, a geometric series, needs $\lvert x\rvert < 1$: **2**.

So A-3, B-1, C-4, D-2. Swapping B and C is the usual slip.""")

T.match(2, ["limits-by-series"], r"Match each limit in List I (as $x \to 0$) with its value in List II.",
        [r"$\dfrac{x - \sin x}{x^3}$", r"$\dfrac{e^x - 1 - x}{x^2}$", r"$\dfrac{\tan x - x}{x^3}$", r"$\dfrac{\cos x - 1 + \frac{x^2}{2}}{x^4}$"],
        [r"$\dfrac12$", r"$\dfrac{1}{24}$", r"$\dfrac16$", r"$\dfrac13$"],
        [r"A-3, B-1, C-4, D-2", r"A-4, B-1, C-3, D-2", r"A-3, B-2, C-4, D-1", r"A-1, B-3, C-4, D-2"],
        r"""Expand each numerator to its first surviving term:
- A: $x - \sin x = \frac{x^3}{6} - \cdots$: **3** ($\frac16$).
- B: $e^x - 1 - x = \frac{x^2}{2} + \cdots$: **1** ($\frac12$).
- C: $\tan x - x = \frac{x^3}{3} + \cdots$: **4** ($\frac13$).
- D: $\cos x - 1 + \frac{x^2}{2} = \frac{x^4}{24} - \cdots$: **2** ($\frac{1}{24}$).

So A-3, B-1, C-4, D-2. Swapping A and C confuses $\sin x$ ($-\frac{x^3}{6}$) with $\tan x$ ($+\frac{x^3}{3}$).""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["maclaurin-theorem", "standard-expansions"],
                   r"$1 - \frac12 + \frac13 - \frac14 + \cdots = \log 2$.",
                   r"For $0 \le x \le 1$, the Lagrange remainder of $\log(1 + x)$ after the term in $x^n$ satisfies $\lvert R_{n+1}\rvert \le \frac{1}{n + 1}$.",
                   0,
                   r"""**R is true:** $R_{n+1} = \frac{(-1)^n}{n + 1}\left(\frac{x}{1 + \theta x}\right)^{n+1}$, and for $0 \le x \le 1$ the bracket lies in $[0, 1]$.

**A is true, and R explains it:** at $x = 1$, R gives $R_{n+1} \to 0$, so the partial sums of $1 - \frac12 + \frac13 - \cdots$ converge to $\log(1 + 1) = \log 2$. (The Leibniz test alone shows convergence, but not that the sum is $\log 2$; R gives both.)""")

T.assertion_reason(2, ["non-analytic"],
                   r"Let $f(x) = e^{-1/x^2}$ for $x \ne 0$ and $f(0) = 0$. The Maclaurin series of $f$ converges for every real $x$, but its sum equals $f(x)$ only at $x = 0$.",
                   r"$f$ is not infinitely differentiable at $x = 0$.",
                   2,
                   r"""**A is true:** $f^{(n)}(0) = 0$ for every $n$, so the Maclaurin series is identically $0$. It converges everywhere to $0$, while $f(x) > 0$ for $x \ne 0$.

**R is false:** $f$ is infinitely differentiable on $\R$, including at $0$, where every derivative equals $0$. That is exactly why the series exists and is $0$. The function is $C^\infty$ but not analytic.""")

T.assertion_reason(2, ["maclaurin-theorem", "non-analytic"],
                   r"Every function that is infinitely differentiable on $\R$ equals the sum of its Maclaurin series on some neighbourhood of $0$.",
                   r"The Maclaurin series of $f$ converges to $f(x)$ if and only if the remainder $R_n(x)$ in Maclaurin's theorem tends to $0$ as $n \to \infty$.",
                   3,
                   r"""**A is false:** $f(x) = e^{-1/x^2}$ ($f(0) = 0$) is $C^\infty$ with Maclaurin series $\equiv 0$, yet $f(x) > 0$ for every $x \ne 0$, so they differ on every neighbourhood of $0$.

**R is true:** $f(x) - S_n(x) = R_{n+1}(x)$ by Maclaurin's theorem, so $S_n(x) \to f(x)$ exactly when $R_n(x) \to 0$. For $e^{-1/x^2}$, $R_n(x) = f(x)$ for all $n$, which does not tend to $0$.""")

T.assertion_reason(3, ["standard-expansions"],
                   r"The Maclaurin series of $\tan^{-1}x$ converges at $x = 1$.",
                   r"The series $1 - x^2 + x^4 - x^6 + \cdots$ converges at $x = 1$.",
                   2,
                   r"""**A is true:** at $x = 1$ the series is $1 - \frac13 + \frac15 - \cdots$, alternating with terms decreasing to $0$, so it converges by the Leibniz test (to $\frac{\pi}{4}$).

**R is false:** at $x = 1$ it becomes $1 - 1 + 1 - \cdots$, whose partial sums oscillate between $1$ and $0$.

The trap: integrating a power series term by term can gain convergence at an endpoint, so the arctan series converges at $x = 1$ even though the series of $\frac{1}{1 + x^2}$ does not.""")

T.assertion_reason(3, ["standard-expansions", "maclaurin-theorem"],
                   r"The binomial series of $(1 + x)^{1/2}$ converges at $x = -1$.",
                   r"For $\lvert x\rvert < 1$, the Cauchy form of the remainder of $(1 + x)^{m}$ tends to $0$ as $n \to \infty$.",
                   1,
                   r"""**A is true:** at $x = -1$ the series is $1 - \frac12 - \frac18 - \frac{1}{16} - \cdots$. After the first term all terms are negative, and $\lvert\binom{1/2}{n}\rvert \sim \frac{1}{2\sqrt{\pi}\,n^{3/2}}$, so it converges absolutely (to $0 = \sqrt{1 - 1}$). In general the series converges at $x = -1$ exactly when $m \ge 0$.

**R is true:** this is how the binomial expansion is proved on $(-1, 1)$.

**But R does not explain A:** R is a statement about $\lvert x\rvert < 1$ and says nothing at the endpoint $x = -1$, which needs a separate comparison with $\sum n^{-3/2}$.""")


def check():
    import sympy as sp
    x, h, n, t = sp.symbols("x h n t")
    th = sp.symbols("theta", positive=True)
    E = sp.E

    def coeff(f, k, order=None):
        return sp.series(f, x, 0, (order or k) + 1).removeO().coeff(x, k)

    def poly(f, k):
        return sp.series(f, x, 0, k + 1).removeO()

    def ne(a, b, label):
        if sp.simplify(sp.sympify(a) - sp.sympify(b)) == 0:
            sys.exit(f"DISTRACTOR EQUALS KEY {label}: {a} vs {b}")

    # q1: Lagrange remainder; n = 0 reduces to the MVT, and for f = exp the formula with the
    # (n+1)! denominator is attained for some theta in (0,1) (check n = 2, h = 1).
    rem = E - sum(1 / sp.factorial(k) for k in range(3))
    thv = sp.nsolve(sp.exp(th) / sp.factorial(3) - rem, th, 0.3)
    assert 0 < thv < 1, "q1"
    # with n! instead of (n+1)! there is no theta in (0,1): e^theta/2 > 1/2 > rem
    assert sp.N(rem) < sp.Rational(1, 2), "q1 distractor"
    # q2
    a = sp.symbols("a", positive=True)
    for k in range(6):
        eq(coeff(a**x, k), sp.log(a)**k / sp.factorial(k), "q2")
    ne(coeff(a**x, 3), a**3 / 6, "q2")
    # q3: log(1+x) at x=1 and divergence at x=-1
    eq(sp.summation((-1)**(n + 1) / n, (n, 1, sp.oo)), sp.log(2), "q3")
    assert sp.summation(1 / n, (n, 1, sp.oo)) == sp.oo, "q3"
    # q4
    eq(poly(sp.exp(x) * sp.sin(x), 3), x + x**2 + x**3 / 3, "q4")
    # q5: derivatives of e^{-1/x^2} at 0 vanish (difference quotients of the derivatives)
    f = sp.exp(-1 / x**2)
    g = f
    for k in range(1, 5):
        assert sp.limit(g / x, x, 0) == 0, "q5"   # (g(x) - g(0))/x with g(0) = 0
        g = sp.diff(g, x)
    eq(poly(sp.exp(-x**2), 4), 1 - x**2 + x**4 / 2, "q5 distractor is exp(-x^2)")
    # q6
    eq(coeff(sp.cos(x), 6), -sp.Rational(1, 720), "q6")
    # q7: cos converges everywhere (ratio test), tan^{-1} series diverges at x = 2
    eq(sp.N(sp.summation((-1)**n * 3**(2 * n) / sp.factorial(2 * n), (n, 0, 60))), sp.N(sp.cos(3)), "q7")
    assert sp.limit(2**(2 * n + 1) / (2 * n + 1), n, sp.oo) == sp.oo, "q7 arctan terms unbounded at x=2"
    # q8
    eq(coeff(sp.sqrt(1 + x), 3), sp.Rational(1, 16), "q8")
    # q9
    eq(poly(sp.log(1 + sp.sin(x)), 3), x - x**2 / 2 + x**3 / 6, "q9")
    # q10
    F = (1 - x)**sp.Rational(5, 2)
    sol = sp.solve(sp.Eq(F.subs(x, 1), F.subs(x, 0) + sp.diff(F, x).subs(x, 0) + sp.diff(F, x, 2).subs(x, th) / 2), th)
    assert sol == [sp.Rational(9, 25)], f"q10 {sol}"
    # q11
    eq(sp.diff(x**2 * sp.exp(x), x, 10).subs(x, 0), 90, "q11")
    # q12
    eq(sp.diff(sp.atan(x), x, 5).subs(x, 0), 24, "q12")
    # q13
    errs = [sp.N(E - sum(1 / sp.factorial(k) for k in range(m + 1))) for m in range(10)]
    bound_ok = [m for m in range(10) if sp.Rational(3) / sp.factorial(m + 1) < sp.Rational(1, 1000)]
    assert bound_ok[0] == 6, "q13"
    assert errs[5] > 1e-3 and errs[6] < 1e-3, "q13 true errors"
    # q14
    eq(poly(sp.tan(x), 5), x + x**3 / 3 + 2 * x**5 / 15, "q14")
    # q15
    eq(sp.N(sp.Rational(1, 10)**5 / 120), sp.N(sp.Float("8.3333333333e-8")), "q15")
    actual = abs(sp.N(sp.sin(sp.Rational(1, 10)) - sp.Rational(1, 10) + sp.Rational(1, 6000), 30))
    assert actual <= sp.Rational(1, 10)**5 / 120, "q15 bound holds"
    eq(sp.N(sp.Rational(1, 10)**4 / 24), sp.N(sp.Float("4.16666666667e-6")), "q15 distractor")
    # q16
    for k in range(7):
        eq(coeff(sp.exp(x) / (1 - x), k), sum(sp.Rational(1, sp.factorial(j)) for j in range(k + 1)), "q16")
    ne(coeff(sp.exp(x) / (1 - x), 2), sp.Rational(3, 2), "q16")
    # q17
    eq(sp.limit(1 / x**2 - 1 / sp.sin(x)**2, x, 0), -sp.Rational(1, 3), "q17")
    # q18
    eq(sp.limit((E - (1 + x)**(1 / x)) / x, x, 0), E / 2, "q18")
    import mpmath
    mpmath.mp.dps = 40
    hv = mpmath.mpf(10)**-8
    assert abs((mpmath.e - (1 + hv)**(1 / hv)) / hv - mpmath.e / 2) < 1e-6, "q18 numeric"
    # q19
    eq(coeff(sp.exp(sp.sin(x)), 4), -sp.Rational(1, 8), "q19")
    # q20: theta -> 1/3, tested with f = exp, a = 0
    thh = sp.log(2 * (sp.exp(h) - 1 - h) / h**2) / h
    eq(sp.limit(thh, h, 0), sp.Rational(1, 3), "q20")
    eq(sp.solve(sp.Eq(h**3, h**2 / 2 * 6 * th * h), th)[0], sp.Rational(1, 3), "q20 x^3")
    # q21: (1+x)^{-1/2} at x = 1 (Abel) and divergence at x = -1
    eq(sp.N(sp.summation(sp.binomial(-sp.Rational(1, 2), n), (n, 0, sp.oo))), sp.N(1 / sp.sqrt(2)), "q21")
    assert sp.limit(sp.sqrt(n) * sp.factorial(2 * n) / (4**n * sp.factorial(n)**2), n, sp.oo) == 1 / sp.sqrt(sp.pi), "q21"
    # q22 (statements 1 only)
    eq(sp.summation((-1)**n / (2 * n + 1), (n, 0, sp.oo)), sp.pi / 4, "q22 st2 false")
    # partial sums of 1 - 1 + 1 - ... oscillate
    assert [sum((-1)**k for k in range(m + 1)) for m in range(4)] == [1, 0, 1, 0], "q22 st3"
    # q23 (statements): Lagrange theta = 1/3, Cauchy theta = (3 +- sqrt 3)/6 for f = x^3
    c = sp.solve(sp.Eq(h**3, h**2 * (1 - th) * 6 * th * h), th)
    assert sorted(c, key=lambda v: sp.N(v)) == sorted([(3 - sp.sqrt(3)) / 6, (3 + sp.sqrt(3)) / 6], key=lambda v: sp.N(v)), f"q23 {c}"
    assert sp.Rational(1, 3) not in c, "q23"
    # Schlömilch–Roche with p = 1 is the Cauchy form (check exponent algebra)
    p = 1; nn = sp.symbols("nn")
    eq((1 - th)**(nn + 1 - p) / (p * sp.factorial(nn)), (1 - th)**nn / sp.factorial(nn), "q23 cauchy")
    # q24 (match ranges)
    assert sp.limit(5**(n + 1) * sp.exp(5) / sp.factorial(n + 1), n, sp.oo) == 0, "q24A"
    eq(sp.summation((-1)**(n + 1) / n, (n, 1, sp.oo)), sp.log(2), "q24B")
    eq(sp.summation((-1)**n / (2 * n + 1), (n, 0, sp.oo)), sp.pi / 4, "q24C")
    assert sp.limit(sp.Integer(1)**n, n, sp.oo) != 0, "q24D terms of 1 - 1 + 1 - ... do not tend to 0"
    # q25 (match limits)
    eq(sp.limit((x - sp.sin(x)) / x**3, x, 0), sp.Rational(1, 6), "q25A")
    eq(sp.limit((sp.exp(x) - 1 - x) / x**2, x, 0), sp.Rational(1, 2), "q25B")
    eq(sp.limit((sp.tan(x) - x) / x**3, x, 0), sp.Rational(1, 3), "q25C")
    eq(sp.limit((sp.cos(x) - 1 + x**2 / 2) / x**4, x, 0), sp.Rational(1, 24), "q25D")
    # AR1: log 2 and Lagrange remainder bound
    r = (-1)**n / (n + 1) * (x / (1 + th * x))**(n + 1)
    for xv in [0, sp.Rational(1, 2), 1]:
        for tv in [sp.Rational(1, 10), sp.Rational(9, 10)]:
            for nv in [1, 5]:
                assert abs(r.subs({x: xv, th: tv, n: nv})) <= sp.Rational(1, nv + 1), "AR1"
    # AR2/AR3: e^{-1/x^2} positive off 0 (series 0), checked in q5
    assert sp.N(f.subs(x, sp.Rational(1, 2))) > 0, "AR2"
    # AR4: arctan at x = 1 converges (q22); 1 - 1 + 1 ... diverges (q22 st3)
    # AR5: sqrt(1+x) series at x = -1 sums to 0; |binom(1/2, n)| ~ n^{-3/2}/(2 sqrt(pi))
    # partial sums S_N = (-1)^N binom(-1/2, N) (telescoping) -> 0
    for N in [5, 12]:
        eq(sum(sp.binomial(sp.Rational(1, 2), k) * (-1)**k for k in range(N + 1)),
           (-1)**N * sp.binomial(-sp.Rational(1, 2), N), "AR5 partial sums")
    assert sp.limit(sp.factorial(2 * n) / (4**n * sp.factorial(n)**2), n, sp.oo) == 0, "AR5 sum is 0"
    bn = sp.gamma(sp.Rational(3, 2)) / (sp.gamma(n + 1) * sp.gamma(sp.Rational(3, 2) - n))
    eq(sp.binomial(sp.Rational(1, 2), 7), bn.subs(n, 7), "AR5 gamma form")
    assert abs(sp.N(abs(sp.binomial(sp.Rational(1, 2), 4000)) * 4000**sp.Rational(3, 2) * 2 * sp.sqrt(sp.pi)) - 1) < 1e-3, "AR5 rate"


T.write(check)
