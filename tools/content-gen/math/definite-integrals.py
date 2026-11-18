import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.integral.definite-integrals")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["sum-to-integral"], r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\frac{r^2}{n^3}$ equals",
         [r"$\tfrac13$", r"$\tfrac12$", r"$\tfrac16$", r"$1$"],
         r"""Pull out $\frac1n$: $\displaystyle\sum_{r=1}^{n}\frac{r^2}{n^3} = \frac1n\sum_{r=1}^{n}\left(\frac rn\right)^2$, so
$$\lim_{n\to\infty}\frac1n\sum_{r=1}^{n}\left(\frac rn\right)^2 = \int_0^1 x^2\,dx = \frac13.$$
Check: the exact sum is $\frac{(n+1)(2n+1)}{6n^2} \to \frac{2}{6}$. $\frac16$ forgets the factor $2$ from $2n + 1$; $\frac12$ is $\int_0^1 x\,dx$.""")

T.single(1, ["fundamental-theorem"], r"$\dfrac{d}{dx}\displaystyle\int_0^{x^2}\cos t\,dt$ equals",
         [r"$2x\cos(x^2)$", r"$\cos(x^2)$", r"$2x\cos x$", r"$\sin(x^2)$"],
         r"""By the Leibniz rule with upper limit $v(x) = x^2$:
$$\frac{d}{dx}\int_0^{x^2}\cos t\,dt = \cos(x^2)\cdot 2x.$$
Check: the integral is $\sin(x^2)$, whose derivative is $2x\cos(x^2)$. $\cos(x^2)$ forgets the chain-rule factor $v'(x) = 2x$; $\sin(x^2)$ is the integral itself, not its derivative.""")

T.single(1, ["symmetry"], r"$\displaystyle\int_{-\pi/2}^{\pi/2}\left(x^3 + x\cos x + \sin^5 x + 1\right)dx$ equals",
         [r"$\pi$", r"$0$", r"$2\pi$", r"$\tfrac{\pi}{2}$"],
         r"""$x^3$, $x\cos x$ and $\sin^5 x$ are continuous odd functions, so each integrates to $0$ over the symmetric interval. Only the constant remains:
$$\int_{-\pi/2}^{\pi/2}1\,dx = \pi.$$
$0$ forgets that the constant $1$ is even, not odd; $\frac{\pi}{2}$ integrates $1$ over $[0, \frac{\pi}{2}]$ only.""")

T.single(1, ["properties", "standard-results"], r"$\displaystyle\int_0^{\pi/2}\frac{\sin^{10}x}{\sin^{10}x + \cos^{10}x}\,dx$ equals",
         [r"$\tfrac{\pi}{4}$", r"$\tfrac{\pi}{2}$", r"$\tfrac{\pi}{8}$", r"$0$"],
         r"""Call it $I$. The substitution $x \to \frac{\pi}{2} - x$ swaps $\sin$ and $\cos$:
$$I = \int_0^{\pi/2}\frac{\cos^{10}x}{\cos^{10}x + \sin^{10}x}\,dx, \qquad 2I = \int_0^{\pi/2}1\,dx = \frac{\pi}{2}.$$
So $I = \frac{\pi}{4}$, whatever the exponent. $\frac{\pi}{2}$ is $2I$, the sum of the two forms.""")

T.single(1, ["symmetry"], r"$\displaystyle\int_0^{10\pi}\lvert\sin x\rvert\,dx$ equals",
         [r"$20$", r"$10$", r"$0$", r"$40$"],
         r"""$\lvert\sin x\rvert$ has period $\pi$, and $\int_0^{\pi}\sin x\,dx = 2$. Over $10$ periods:
$$\int_0^{10\pi}\lvert\sin x\rvert\,dx = 10 \times 2 = 20.$$
$0$ is $\int_0^{10\pi}\sin x\,dx$, without the modulus; $10$ uses $1$ per period instead of $2$.""")

T.single(1, ["mean-value-bounds"], r"The mean value of $f(x) = x^2$ on $[0, 3]$ is",
         [r"$3$", r"$9$", r"$\tfrac92$", r"$\tfrac94$"],
         r"""The mean value is $\frac{1}{b - a}\int_a^b f$:
$$\frac13\int_0^3 x^2\,dx = \frac13\cdot 9 = 3.$$
It is attained at $\xi = \sqrt3$, as the first mean value theorem promises. $9$ is the integral itself (not divided by $3$); $\frac94 = f(\frac32)$ wrongly assumes $\xi$ is the midpoint; $\frac92$ is the average of $f(0)$ and $f(3)$.""")

T.single(1, ["sum-to-integral"], r"$\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^{n}e^{r/n}$ equals",
         [r"$e - 1$", r"$e$", r"$1$", r"$e + 1$"],
         r"""With $\frac rn \to x$ and $\frac1n \to dx$:
$$\lim_{n\to\infty}\frac1n\sum_{r=1}^{n}e^{r/n} = \int_0^1 e^x\,dx = e - 1 \approx 1.718.$$
$e$ forgets the lower limit term $e^0 = 1$.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["sum-to-integral"], r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\frac{n}{n^2 + r^2}$ equals",
         [r"$\tfrac{\pi}{4}$", r"$\tfrac{\pi}{2}$", r"$\ln 2$", r"$\tfrac12\ln 2$"],
         r"""Divide numerator and denominator by $n^2$:
$$\sum_{r=1}^{n}\frac{n}{n^2 + r^2} = \frac1n\sum_{r=1}^{n}\frac{1}{1 + (r/n)^2} \;\to\; \int_0^1\frac{dx}{1 + x^2} = \tan^{-1}1 = \frac{\pi}{4}.$$
$\frac12\ln 2$ is the limit of $\sum\frac{r}{n^2 + r^2}$ (numerator $r$, not $n$); $\frac{\pi}{2}$ uses the limits $0$ to $\infty$.""")

T.single(2, ["limit-of-sum"], r"Divide $[0, 1]$ into $n$ equal parts. The right-endpoint sum $\displaystyle\frac1n\sum_{r=1}^{n}f\!\left(\frac rn\right)$ for $f(x) = x^2$ equals",
         [r"$\dfrac{(n+1)(2n+1)}{6n^2}$", r"$\dfrac{(n-1)(2n-1)}{6n^2}$", r"$\dfrac{(n+1)(2n+1)}{6n^3}$", r"$\dfrac{n+1}{2n}$"],
         r"""$$\frac1n\sum_{r=1}^{n}\frac{r^2}{n^2} = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6n^2},$$
which tends to $\frac13 = \int_0^1 x^2\,dx$. $\frac{(n-1)(2n-1)}{6n^2}$ is the **left**-endpoint sum ($r = 0$ to $n - 1$); $\frac{(n+1)(2n+1)}{6n^3}$ cancels $n$ wrongly and tends to $0$; $\frac{n+1}{2n}$ is the sum for $f(x) = x$.""")

T.single(2, ["fundamental-theorem"], r"For $x > 1$, $\dfrac{d}{dx}\displaystyle\int_x^{x^2}\frac{dt}{\ln t}$ equals",
         [r"$\dfrac{x - 1}{\ln x}$", r"$\dfrac{x + 1}{\ln x}$", r"$\dfrac{2x - 1}{\ln x}$", r"$\dfrac{x}{\ln x}$"],
         r"""Leibniz rule: upper limit $x^2$, lower limit $x$:
$$\frac{1}{\ln x^2}\cdot 2x - \frac{1}{\ln x}\cdot 1 = \frac{2x}{2\ln x} - \frac{1}{\ln x} = \frac{x - 1}{\ln x}.$$
$\frac{x + 1}{\ln x}$ adds the lower-limit term instead of subtracting it; $\frac{2x - 1}{\ln x}$ forgets that $\ln x^2 = 2\ln x$.""")

T.single(2, ["fundamental-theorem"], r"$\displaystyle\lim_{x\to 0}\frac{1}{x^3}\int_0^{x}\sin(t^2)\,dt$ equals",
         [r"$\tfrac13$", r"$1$", r"$0$", r"$\tfrac16$"],
         r"""It is of the form $\frac00$. By L'Hospital's rule and the fundamental theorem,
$$\lim_{x\to0}\frac{\sin(x^2)}{3x^2} = \frac13.$$
Check: $\sin(t^2) \approx t^2$, so the integral is about $\frac{x^3}{3}$. $1$ forgets the $3$ from differentiating $x^3$.""")

T.single(2, ["properties"], r"$\displaystyle\int_2^3\frac{\sqrt{x}}{\sqrt{x} + \sqrt{5 - x}}\,dx$ equals",
         [r"$\tfrac12$", r"$1$", r"$\tfrac52$", r"$0$"],
         r"""Call it $I$. Here $a + b = 5$, so $x \to 5 - x$ gives
$$I = \int_2^3\frac{\sqrt{5 - x}}{\sqrt{5 - x} + \sqrt{x}}\,dx, \qquad 2I = \int_2^3 1\,dx = 1, \qquad I = \frac12.$$
$1$ is $2I$; $\frac52 = \frac{a + b}{2}$ uses the sum of the limits instead of their difference: the general result is $\frac{b - a}{2}$.""")

T.single(2, ["properties"], r"$\displaystyle\int_0^{\pi/4}\ln(1 + \tan x)\,dx$ equals",
         [r"$\tfrac{\pi}{8}\ln 2$", r"$\tfrac{\pi}{4}\ln 2$", r"$\tfrac{\pi}{2}\ln 2$", r"$-\tfrac{\pi}{8}\ln 2$"],
         r"""With $x \to \frac{\pi}{4} - x$: $1 + \tan\left(\frac{\pi}{4} - x\right) = \frac{2}{1 + \tan x}$. So
$$I = \int_0^{\pi/4}\big[\ln 2 - \ln(1 + \tan x)\big]dx = \frac{\pi}{4}\ln 2 - I, \qquad I = \frac{\pi}{8}\ln 2.$$
$\frac{\pi}{4}\ln 2$ is $2I$, forgetting to halve. The integrand is positive, so a negative answer is impossible.""")

T.single(2, ["properties"], r"With $[\cdot]$ the greatest integer function, $\displaystyle\int_0^{2}[x^2]\,dx$ equals",
         [r"$5 - \sqrt2 - \sqrt3$", r"$3 - \sqrt2$", r"$5 - \sqrt3$", r"$\tfrac83$"],
         r"""$[x^2]$ jumps at $x = 1, \sqrt2, \sqrt3$. Split there:
$$0\cdot 1 + 1(\sqrt2 - 1) + 2(\sqrt3 - \sqrt2) + 3(2 - \sqrt3) = 5 - \sqrt2 - \sqrt3 \approx 1.854.$$
$\frac83 = \int_0^2 x^2\,dx$ ignores the integer part. Missing the jump at $\sqrt3$ gives other wrong values; the answer must be below $\frac83$, since $[x^2] \le x^2$.""")

T.single(2, ["mean-value-bounds"], r"Let $I = \displaystyle\int_0^1 e^{x^2}\,dx$. Which of the following is true?",
         [r"$1 < I < e$", r"$0 < I < 1$", r"$I = e - 1$", r"$e < I < e^2$"],
         r"""On $[0, 1]$, $0 \le x^2 \le 1$, so $1 \le e^{x^2} \le e$, with equality only at the end points. Since the integrand is continuous and not constant,
$$1 \cdot (1 - 0) < I < e\cdot(1 - 0).$$
Numerically $I \approx 1.4627$. $e - 1 \approx 1.718$ is $\int_0^1 e^x\,dx$; $e^{x^2} \le e^x$ on $[0, 1]$, so $I < e - 1$.""")

T.single(2, ["sum-to-integral"], r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\frac{r}{n^2 + r^2}$ equals",
         [r"$\tfrac12\ln 2$", r"$\ln 2$", r"$\tfrac{\pi}{4}$", r"$\ln\sqrt3$"],
         r"""$$\sum_{r=1}^{n}\frac{r}{n^2 + r^2} = \frac1n\sum_{r=1}^{n}\frac{r/n}{1 + (r/n)^2} \;\to\; \int_0^1\frac{x\,dx}{1 + x^2} = \frac12\Big[\ln(1 + x^2)\Big]_0^1 = \frac12\ln 2.$$
$\ln 2$ forgets the $\frac12$ in $\int\frac{x}{1 + x^2}\,dx$; $\frac{\pi}{4}$ is the limit when the numerator is $n$.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["sum-to-integral"], r"$\displaystyle\lim_{n\to\infty}\left(\frac{n!}{n^n}\right)^{1/n}$ equals",
         [r"$\tfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""Take logarithms:
$$\ln\left(\frac{n!}{n^n}\right)^{1/n} = \frac1n\sum_{r=1}^{n}\ln\frac rn \;\to\; \int_0^1\ln x\,dx = \Big[x\ln x - x\Big]_0^1 = -1.$$
So the limit is $e^{-1}$. $1$ comes from thinking $(n!)^{1/n}$ and $n$ grow alike; $0$ from $\frac{n!}{n^n} \to 0$, which ignores the $n$th root. (Stirling's formula gives the same answer.)""")

T.single(3, ["standard-results"], r"$\displaystyle\int_0^{\pi}\frac{x\sin x}{1 + \cos^2 x}\,dx$ equals",
         [r"$\dfrac{\pi^2}{4}$", r"$\dfrac{\pi^2}{2}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{\pi^2}{8}$"],
         r"""The integrand is $x f(\sin x)$ (since $\cos^2 x = 1 - \sin^2 x$), so
$$I = \frac{\pi}{2}\int_0^{\pi}\frac{\sin x}{1 + \cos^2 x}\,dx = \frac{\pi}{2}\Big[-\tan^{-1}(\cos x)\Big]_0^{\pi} = \frac{\pi}{2}\left(\frac{\pi}{4} + \frac{\pi}{4}\right) = \frac{\pi^2}{4}.$$
$\frac{\pi^2}{2}$ forgets the factor $\frac12$ in $\frac{\pi}{2}$, using $\pi\int f(\sin x)$; $\frac{\pi}{2}$ is the remaining integral alone.""")

T.single(3, ["standard-results"], r"$\displaystyle\int_0^{\pi}\frac{x}{1 + \sin x}\,dx$ equals",
         [r"$\pi$", r"$2\pi$", r"$\tfrac{\pi}{2}$", r"$\pi^2$"],
         r"""By the $x f(\sin x)$ result,
$$I = \frac{\pi}{2}\int_0^{\pi}\frac{dx}{1 + \sin x}.$$
By the $2a$ rule and then $x \to \frac{\pi}{2} - x$,
$$\int_0^{\pi}\frac{dx}{1 + \sin x} = 2\int_0^{\pi/2}\frac{dx}{1 + \cos x} = 2\int_0^{\pi/2}\frac12\sec^2\frac x2\,dx = 2\Big[\tan\frac x2\Big]_0^{\pi/2} = 2.$$
So
$$I = \frac{\pi}{2}\cdot 2 = \pi.$$
$2\pi$ uses $\pi$ instead of $\frac{\pi}{2}$ in front.""")

T.single(3, ["fundamental-theorem"], r"If $\phi(x) = \displaystyle\int_0^{x}(x - t)\sin t\,dt$, then $\phi''(x)$ equals",
         [r"$\sin x$", r"$x\sin x$", r"$1 - \cos x$", r"$x\cos x$"],
         r"""Take $x$ outside: $\phi(x) = x\int_0^x\sin t\,dt - \int_0^x t\sin t\,dt$. Then
$$\phi'(x) = \int_0^x\sin t\,dt + x\sin x - x\sin x = 1 - \cos x, \qquad \phi''(x) = \sin x.$$
Check: $\phi(x) = x - \sin x$, so $\phi'' = \sin x$. $1 - \cos x$ is $\phi'$, not $\phi''$; $x\sin x$ comes from differentiating under the integral sign without taking $x$ outside.""")

T.single(3, ["symmetry"], r"For a positive integer $n$ and $0 \le v < \pi$, $\displaystyle\int_0^{n\pi + v}\lvert\sin x\rvert\,dx$ equals",
         [r"$2n + 1 - \cos v$", r"$2n + \cos v$", r"$2n - 1 + \cos v$", r"$n + 1 - \cos v$"],
         r"""$\lvert\sin x\rvert$ has period $\pi$ with $\int_0^{\pi}\lvert\sin x\rvert\,dx = 2$. Split at $n\pi$ and shift the last piece by the period:
$$\int_0^{n\pi}\lvert\sin x\rvert\,dx + \int_{n\pi}^{n\pi + v}\lvert\sin x\rvert\,dx = 2n + \int_0^{v}\sin x\,dx = 2n + 1 - \cos v.$$
Check at $v = 0$: the value must be $2n$, and only $2n + 1 - \cos v$ gives that. $n + 1 - \cos v$ uses $1$ per period.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["properties", "symmetry"],
             r"Consider the following statements, where $f$ is continuous on $\R$:",
             [r"$\displaystyle\int_a^b f(x)\,dx = \int_a^b f(a + b - x)\,dx$ for all $a, b$.",
              r"If $f$ is odd, then $\displaystyle\int_{-a}^{a} f(x)\,dx = 2\int_0^{a} f(x)\,dx$.",
              r"If $f$ has period $T$, then $\displaystyle\int_a^{a + T} f(x)\,dx$ does not depend on $a$."],
             [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** substitute $x = a + b - t$; the limits swap and $dx = -dt$ swaps them back.
- **2 is false:** for odd $f$ the integral is $0$; $2\int_0^a f$ is the rule for **even** $f$. Counterexample: $f(x) = x$, $a = 1$ gives $0 \ne 1$.
- **3 is true:** $\frac{d}{da}\int_a^{a + T} f = f(a + T) - f(a) = 0$.

So 1 and 3 only.""")

T.statements(3, ["mean-value-bounds"],
             r"Consider the following statements about functions on $[a, b]$, $a < b$:",
             [r"If $f$ is continuous on $[a, b]$, then $\displaystyle\int_a^b f(x)\,dx = f(\xi)(b - a)$ for some $\xi \in [a, b]$.",
              r"If $f, g$ are continuous on $[a, b]$ and $g(x) \ge 0$ there, then $\displaystyle\int_a^b f g\,dx = f(\xi)\int_a^b g\,dx$ for some $\xi \in [a, b]$.",
              r"If $f$ is merely integrable on $[a, b]$, then $\displaystyle\int_a^b f(x)\,dx = f(\xi)(b - a)$ for some $\xi \in [a, b]$."],
             [r"1 and 2 only", r"1 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** the first mean value theorem. The average lies between $\min f$ and $\max f$, and the intermediate value theorem gives $\xi$.
- **2 is true:** the generalised first mean value theorem; $g$ must not change sign, and $g \ge 0$ ensures that.
- **3 is false:** take $f = 0$ on $[0, 1)$, $f = 1$ on $[1, 2]$. Then $\int_0^2 f = 1$, but $f(\xi)\cdot 2 = 1$ needs $f(\xi) = \frac12$, which never happens. Continuity is essential.

So 1 and 2 only.""")

# ---------------------------------------------------------------- match
T.match(2, ["standard-results"], r"Here $\log$ is the natural logarithm. Match each integral in List I with its value in List II.",
        [r"$\displaystyle\int_0^{\pi/2}\log\sin x\,dx$", r"$\displaystyle\int_0^{\pi}\log\sin x\,dx$",
         r"$\displaystyle\int_0^{\pi/2}\log\tan x\,dx$", r"$\displaystyle\int_0^{\pi/2}\frac{\sin x}{\sin x + \cos x}\,dx$"],
        [r"$0$", r"$-\pi\log 2$", r"$\dfrac{\pi}{4}$", r"$-\dfrac{\pi}{2}\log 2$"],
        [r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-4, B-1, C-2, D-3"],
        r"""- A: the standard result $-\frac{\pi}{2}\log 2$: **4**.
- B: $\sin(\pi - x) = \sin x$, so by the $2a$ rule it is twice A, $-\pi\log 2$: **2**.
- C: $\int\log\tan x = \int\log\sin x - \int\log\cos x = 0$, since the last two are equal by $x \to \frac{\pi}{2} - x$: **1**.
- D: the $\frac{\pi}{4}$ family with $n = 1$: **3**.

So A-4, B-2, C-1, D-3. Swapping A and B is the usual slip: the longer interval doubles the value.""")

T.match(3, ["sum-to-integral"], r"Match each limit in List I with its value in List II.",
        [r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\frac{1}{n + r}$", r"$\displaystyle\lim_{n\to\infty}\sum_{r=0}^{n-1}\frac{1}{\sqrt{n^2 - r^2}}$",
         r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\frac{r^3}{n^4}$", r"$\displaystyle\lim_{n\to\infty}\sum_{r=1}^{2n}\frac{1}{n + r}$"],
        [r"$\ln 3$", r"$\dfrac{\pi}{2}$", r"$\ln 2$", r"$\dfrac14$"],
        [r"A-3, B-2, C-4, D-1", r"A-1, B-2, C-4, D-3", r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-1, D-4"],
        r"""In each, pull out $\frac1n$ and put $\frac rn = x$.
- A: $\int_0^1\frac{dx}{1 + x} = \ln 2$: **3**.
- B: $\frac1n\sum\frac{1}{\sqrt{1 - (r/n)^2}} \to \int_0^1\frac{dx}{\sqrt{1 - x^2}} = \sin^{-1}1 = \frac{\pi}{2}$: **2**.
- C: $\frac1n\sum\left(\frac rn\right)^3 \to \int_0^1 x^3\,dx = \frac14$: **4**.
- D: $\frac rn$ now runs up to $2$, so $\int_0^2\frac{dx}{1 + x} = \ln 3$: **1**.

So A-3, B-2, C-4, D-1. Swapping A and D comes from ignoring the upper limit $2n$.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["standard-results"],
                   r"$\displaystyle\int_0^{\pi} x\sin x\,dx = \pi$.",
                   r"For $f$ continuous on $[0, 1]$, $\displaystyle\int_0^{\pi} x f(\sin x)\,dx = \frac{\pi}{2}\int_0^{\pi} f(\sin x)\,dx$.",
                   0,
                   r"""**R is true:** with $x \to \pi - x$, $I = \int_0^{\pi}(\pi - x)f(\sin x)\,dx$; adding gives $2I = \pi\int_0^{\pi} f(\sin x)\,dx$.

**A is true, and R explains it:** with $f(u) = u$,
$$\int_0^{\pi}x\sin x\,dx = \frac{\pi}{2}\int_0^{\pi}\sin x\,dx = \frac{\pi}{2}\cdot 2 = \pi.$$
(Integration by parts confirms: $\big[-x\cos x + \sin x\big]_0^{\pi} = \pi$.)""")

T.assertion_reason(2, ["fundamental-theorem", "exam-tips"],
                   r"$\displaystyle\int_{-1}^{1}\frac{dx}{x^2} = -2$.",
                   r"If $f$ is integrable on $[a, b]$ and $\phi' = f$ on $[a, b]$, then $\displaystyle\int_a^b f(x)\,dx = \phi(b) - \phi(a)$.",
                   3,
                   r"""**R is true:** it is the fundamental theorem of integral calculus.

**A is false:** $\frac{1}{x^2} > 0$, so no integral of it over $[-1, 1]$ can be negative. The computation $\left[-\frac1x\right]_{-1}^{1} = -2$ misuses R: $\frac{1}{x^2}$ is unbounded near $0$ (so not integrable on $[-1, 1]$), and $-\frac1x$ is not differentiable at $0$. In fact the improper integral diverges to $+\infty$.""")

T.assertion_reason(2, ["properties", "symmetry"],
                   r"$\displaystyle\int_0^{\pi/2}\sin^2 x\,dx = \frac{\pi}{4}$.",
                   r"$\sin^2 x$ is an even function of $x$.",
                   1,
                   r"""**A is true:** with $x \to \frac{\pi}{2} - x$, $\int_0^{\pi/2}\sin^2 x\,dx = \int_0^{\pi/2}\cos^2 x\,dx$. Adding, $2I = \int_0^{\pi/2}1\,dx = \frac{\pi}{2}$, so $I = \frac{\pi}{4}$.

**R is true:** $\sin^2(-x) = \sin^2 x$.

**But R does not explain A:** evenness is about symmetry about $0$, and the interval $[0, \frac{\pi}{2}]$ is not symmetric. The reason is the $\sin \leftrightarrow \cos$ swap from $\int_0^a f(x)\,dx = \int_0^a f(a - x)\,dx$.""")

T.assertion_reason(1, ["mean-value-bounds"],
                   r"If $f$ is continuous on $[a, b]$, then $\displaystyle\int_a^b f(x)\,dx = f(\xi)(b - a)$ for some $\xi \in [a, b]$.",
                   r"If $f$ is continuous on $[a, b]$, then $\displaystyle\int_a^b f(x)\,dx = f\!\left(\frac{a + b}{2}\right)(b - a)$.",
                   2,
                   r"""**A is true:** it is the first mean value theorem of integral calculus.

**R is false:** $\xi$ exists but need not be the midpoint. For $f(x) = x^2$ on $[0, 3]$: $\int_0^3 x^2\,dx = 9$, but $f(\frac32)\cdot 3 = \frac{27}{4}$. Here $\xi = \sqrt3$. (R holds for linear $f$ only.)""")

T.assertion_reason(2, ["symmetry"],
                   r"$\displaystyle\int_0^{\pi}\cos^3 x\,dx = 0$.",
                   r"$\cos^3(\pi - x) = -\cos^3 x$ for all $x$.",
                   0,
                   r"""**R is true:** $\cos(\pi - x) = -\cos x$, so $\cos^3(\pi - x) = -\cos^3 x$.

**A is true, and R explains it:** by the $2a$ rule with $2a = \pi$, $\int_0^{2a} f = 0$ when $f(2a - x) = -f(x)$. Direct check: $\int_0^{\pi}\cos^3 x\,dx = \Big[\sin x - \frac{\sin^3 x}{3}\Big]_0^{\pi} = 0$.""")


def check():
    import sympy as sp
    x, t, v = sp.symbols("x t v", real=True)
    n, r = sp.symbols("n r", positive=True, integer=True)
    pi, E, ln = sp.pi, sp.E, sp.log
    I = lambda f, a, b: sp.integrate(f, (x, a, b))
    Nq = lambda f, a, b: sp.Integral(f, (x, a, b)).evalf(30)

    def lim_sum(term, upper, want, label):
        """Symbolic limit where SymPy manages it, plus a numeric partial sum at large n."""
        try:
            got = sp.limit(sp.summation(term, (r, 1, upper)), n, sp.oo)
            if not got.has(sp.Limit, sp.Sum):
                eq(got, want, label)
        except NotImplementedError:
            pass
        N = 20000
        f = sp.lambdify((n, r), term, "math")
        up = int(upper.subs(n, N)) if hasattr(upper, "subs") else upper
        S = sum(f(N, k) for k in range(1, up + 1))
        if abs(S - float(want)) > 1e-3:
            sys.exit(f"CHECK FAILED {label} numeric: {S} vs {want}")

    def ne(a, b, label):
        if abs(complex(sp.N(a - b, 30))) < 1e-9:
            sys.exit(f"DISTRACTOR EQUALS KEY {label}: {a} vs {b}")

    # q1
    lim_sum(r**2 / n**3, n, sp.Rational(1, 3), "q1")
    # q2
    eq(sp.diff(sp.integrate(sp.cos(t), (t, 0, x**2)), x), 2 * x * sp.cos(x**2), "q2")
    # q3
    eq(I(x**3 + x * sp.cos(x) + sp.sin(x)**5 + 1, -pi / 2, pi / 2), pi, "q3")
    # q4 (numeric; also n = 1, 3)
    for k in (1, 3, 10):
        eq(Nq(sp.sin(x)**k / (sp.sin(x)**k + sp.cos(x)**k), 0, pi / 2), sp.N(pi / 4, 30), f"q4 n={k}")
    # q5
    eq(10 * I(sp.sin(x), 0, pi), 20, "q5"); eq(Nq(sp.Abs(sp.sin(x)), 0, 10 * pi), 20, "q5n")
    # q6
    eq(I(x**2, 0, 3) / 3, 3, "q6"); ne(3, sp.Rational(9, 4), "q6")
    # q7
    eq(sp.limit(sp.summation(sp.exp(r / n), (r, 1, n)) / n, n, sp.oo), E - 1, "q7")
    # q8
    lim_sum(n / (n**2 + r**2), n, pi / 4, "q8"); eq(I(1 / (1 + x**2), 0, 1), pi / 4, "q8b")
    if abs(sum(100000 / (100000**2 + k**2) for k in range(1, 100001)) - float(pi / 4)) > 1e-4:
        sys.exit("CHECK FAILED q8 numeric")
    # q9
    s9 = sp.summation((r / n)**2, (r, 1, n)) / n
    eq(s9, (n + 1) * (2 * n + 1) / (6 * n**2), "q9")
    eq(sp.summation((r / n)**2, (r, 0, n - 1)) / n, (n - 1) * (2 * n - 1) / (6 * n**2), "q9-left")
    eq(sp.limit(s9, n, sp.oo), sp.Rational(1, 3), "q9-lim")
    # q10
    xp = sp.symbols("xp", positive=True)
    F10 = sp.Integral(1 / ln(t), (t, xp, xp**2))
    d10 = sp.diff(F10, xp).doit()
    eq(sp.simplify(d10.subs(xp, 3)), (3 - 1) / ln(3), "q10")
    eq(sp.simplify(d10.subs(xp, sp.Rational(7, 2))), (sp.Rational(7, 2) - 1) / ln(sp.Rational(7, 2)), "q10b")
    # q11
    eq(sp.limit(sp.integrate(sp.sin(t**2), (t, 0, x)) / x**3, x, 0), sp.Rational(1, 3), "q11")
    # q12
    eq(Nq(sp.sqrt(x) / (sp.sqrt(x) + sp.sqrt(5 - x)), 2, 3), sp.Rational(1, 2), "q12")
    # q13
    eq(Nq(ln(1 + sp.tan(x)), 0, pi / 4), sp.N(pi / 8 * ln(2), 30), "q13")
    # q14
    v14 = sum(k * (sp.sqrt(k + 1) - sp.sqrt(k)) for k in range(3)) + 3 * (2 - sp.sqrt(3))
    eq(v14, 5 - sp.sqrt(2) - sp.sqrt(3), "q14")
    num14 = sum(int((2 * (j + 0.5) / 200000)**2) for j in range(200000)) * 2 / 200000
    if abs(num14 - float(5 - sp.sqrt(2) - sp.sqrt(3))) > 1e-4:
        sys.exit("CHECK FAILED q14 numeric")
    # q15
    v15 = Nq(sp.exp(x**2), 0, 1)
    if not (1 < v15 < sp.E.evalf()) or not (v15 < (E - 1).evalf()):
        sys.exit("CHECK FAILED q15")
    # q16
    lim_sum(r / (n**2 + r**2), n, ln(2) / 2, "q16"); eq(I(x / (1 + x**2), 0, 1), ln(2) / 2, "q16b")
    # q17
    eq(I(ln(x), 0, 1), -1, "q17")
    eq(sp.limit(ln(sp.factorial(n) / n**n) / n, n, sp.oo), -1, "q17-lim")
    # q18
    eq(I(x * sp.sin(x) / (1 + sp.cos(x)**2), 0, pi), pi**2 / 4, "q18")
    eq(Nq(x * sp.sin(x) / (1 + sp.cos(x)**2), 0, pi), sp.N(pi**2 / 4, 30), "q18n")
    # q19
    eq(Nq(x / (1 + sp.sin(x)), 0, pi), sp.N(pi, 30), "q19")
    eq(Nq(1 / (1 + sp.sin(x)), 0, pi), 2, "q19b")
    # q20
    phi = sp.integrate((x - t) * sp.sin(t), (t, 0, x))
    eq(phi, x - sp.sin(x), "q20"); eq(sp.diff(phi, x, 2), sp.sin(x), "q20b")
    # q21
    for nn, vv in [(3, sp.Rational(1, 2)), (5, 2)]:
        tot = sum(sp.Abs(I(sp.sin(x), k * pi, (k + 1) * pi)) for k in range(nn)) + sp.Abs(I(sp.sin(x), nn * pi, nn * pi + vv))
        eq(tot, 2 * nn + 1 - sp.cos(vv), "q21")
        import mpmath
        mpmath.mp.dps = 30
        qn = mpmath.quad(lambda s_: abs(mpmath.sin(s_)), [k * mpmath.pi for k in range(nn + 1)] + [nn * mpmath.pi + float(vv)])
        if abs(qn - float(2 * nn + 1 - sp.cos(vv))) > 1e-12:
            sys.exit("CHECK FAILED q21 numeric")
    # q22 statements
    a, b = sp.Rational(1, 3), sp.Rational(9, 4)
    eq(Nq(sp.exp(x) * x**2, a, b), Nq((sp.exp(x) * x**2).subs(x, a + b - x), a, b), "q22-1")
    ne(I(x, -1, 1), 2 * I(x, 0, 1), "q22-2")
    for a0 in (0, sp.Rational(7, 10), 3):
        eq(Nq(sp.sin(x)**2 + sp.cos(x), a0, a0 + 2 * pi), pi, "q22-3")
    # q23 statements: 3 false via step function
    step_int = sp.integrate(sp.Piecewise((0, x < 1), (1, True)), (x, 0, 2))
    eq(step_int, 1, "q23-3")
    # 1: xi for x^2 on [0,3]
    eq((sp.sqrt(3))**2 * 3, I(x**2, 0, 3), "q23-1")
    # 2: f = x, g = x on [0,1]: int x^2 = 1/3 = xi * 1/2 -> xi = 2/3 in [0,1]
    eq(sp.Rational(2, 3) * I(x, 0, 1), I(x**2, 0, 1), "q23-2")
    # q24 match
    eq(Nq(ln(sp.sin(x)), 0, pi / 2), sp.N(-pi / 2 * ln(2), 30), "q24A")
    eq(Nq(ln(sp.sin(x)), 0, pi), sp.N(-pi * ln(2), 30), "q24B")
    eq(Nq(ln(sp.tan(x)), 0, pi / 2), 0, "q24C")
    eq(Nq(sp.sin(x) / (sp.sin(x) + sp.cos(x)), 0, pi / 2), sp.N(pi / 4, 30), "q24D")
    eq(Nq(ln(x) / sp.sqrt(1 - x**2), 0, 1), sp.N(-pi / 2 * ln(2), 30), "notes-logx")
    # q25 match
    lim_sum(1 / (n + r), n, ln(2), "q25A")
    eq(I(1 / sp.sqrt(1 - x**2), 0, 1), pi / 2, "q25B")
    nB = 200000
    sB = sum(1 / (nB**2 - k**2)**0.5 for k in range(nB))
    if abs(sB - float(pi / 2)) > 1e-2:
        sys.exit("CHECK FAILED q25B numeric")
    lim_sum(r**3 / n**4, n, sp.Rational(1, 4), "q25C")
    lim_sum(1 / (n + r), 2 * n, ln(3), "q25D")
    # q26 AR
    eq(I(x * sp.sin(x), 0, pi), pi, "q26"); eq(pi / 2 * I(sp.sin(x), 0, pi), pi, "q26R")
    # q27 AR: A false (diverges)
    eq(I(1 / x**2, -1, 1), sp.oo, "q27")
    # q28 AR
    eq(I(sp.sin(x)**2, 0, pi / 2), pi / 4, "q28"); eq(sp.sin(-x)**2, sp.sin(x)**2, "q28R")
    # q29 AR: R false
    ne(I(x**2, 0, 3), sp.Rational(3, 2)**2 * 3, "q29R")
    # q30 AR
    eq(I(sp.cos(x)**3, 0, pi), 0, "q30"); eq(sp.cos(pi - x)**3 + sp.cos(x)**3, 0, "q30R")
    # notes examples
    eq(I(sp.sin(x)**3, 0, pi), sp.Rational(4, 3), "notes-sin3")
    eq(I(x**5 * sp.cos(x) + x**2, -1, 1), sp.Rational(2, 3), "notes-odd")


T.write(check)
