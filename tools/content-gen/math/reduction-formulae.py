import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.integral.reduction-formulae")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["wallis"], r"$\displaystyle\int_0^{\pi/2}\sin^5 x\,dx$ equals",
         [r"$\frac{8}{15}$", r"$\frac{4\pi}{15}$", r"$\frac{5\pi}{32}$", r"$\frac{15}{8}$"],
         r"""$n = 5$ is odd, so there is no factor $\frac{\pi}{2}$:
$$\int_0^{\pi/2}\sin^5x\,dx = \frac{4\cdot2}{5\cdot3\cdot1} = \frac{8}{15}.$$
$\frac{4\pi}{15}$ wrongly multiplies by $\frac{\pi}{2}$ (that factor needs an even index). $\frac{5\pi}{32}$ is the value for $\sin^6 x$.""")

T.single(1, ["wallis", "sin-cos-powers"], r"$\displaystyle\int_0^{\pi/2}\cos^4 x\,dx$ equals",
         [r"$\frac{3\pi}{16}$", r"$\frac{3}{8}$", r"$\frac{3\pi}{8}$", r"$\frac{8}{15}$"],
         r"""$\int_0^{\pi/2}\cos^n x\,dx = \int_0^{\pi/2}\sin^n x\,dx$, and $n = 4$ is even:
$$\frac{3\cdot1}{4\cdot2}\cdot\frac{\pi}{2} = \frac{3\pi}{16}.$$
$\frac38$ forgets the factor $\frac{\pi}{2}$; $\frac{3\pi}{8}$ is the value over $[0, \pi]$.""")

T.single(1, ["tan-sec-cot", "exam-tips"], r"If $I_n = \displaystyle\int_0^{\pi/4}\tan^n x\,dx$, then $I_4 + I_2$ equals",
         [r"$\frac13$", r"$\frac14$", r"$\frac12$", r"$\frac{\pi}{4}$"],
         r"""$$I_n + I_{n-2} = \int_0^{\pi/4}\tan^{n-2}x\sec^2x\,dx = \left[\frac{\tan^{n-1}x}{n-1}\right]_0^{\pi/4} = \frac{1}{n-1}.$$
With $n = 4$: $I_4 + I_2 = \frac13$. The tempting $\frac14$ uses $\frac1n$ instead of $\frac{1}{n-1}$.
Check: $I_2 = 1 - \frac{\pi}{4}$ and $I_4 = \frac{\pi}{4} - \frac23$ add to $\frac13$.""")

T.single(1, ["method", "sin-cos-powers"], r"For $n \ge 2$, $I_n = \displaystyle\int\sin^n x\,dx$ satisfies",
         [r"$I_n = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}I_{n-2}$",
          r"$I_n = \frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}I_{n-2}$",
          r"$I_n = -\frac{\sin^{n-1}x\cos x}{n} - \frac{n-1}{n}I_{n-2}$",
          r"$I_n = -\frac{\sin^{n-1}x\cos x}{n-1} + \frac{n-2}{n-1}I_{n-2}$"],
         r"""Parts with $u = \sin^{n-1}x$, $dv = \sin x\,dx$, then $\cos^2 = 1 - \sin^2$:
$$I_n = -\sin^{n-1}x\cos x + (n-1)(I_{n-2} - I_n) \;\Rightarrow\; nI_n = -\sin^{n-1}x\cos x + (n-1)I_{n-2}.$$
Check at $n = 2$: $\int\sin^2 x\,dx = -\frac12\sin x\cos x + \frac{x}{2}$, which is correct. The $+$ boundary sign belongs to the $\cos^n x$ formula.""")

T.single(1, ["other-reductions", "exam-tips"], r"$\displaystyle\int_0^{\infty}x^5e^{-x}\,dx$ equals",
         [r"$120$", r"$24$", r"$720$", r"$5$"],
         r"""With $I_n = \int_0^\infty x^ne^{-x}\,dx$, parts gives $I_n = nI_{n-1}$ (the boundary term $-x^ne^{-x}$ vanishes at both ends), and $I_0 = 1$. So
$$I_5 = 5! = 120.$$
$24 = 4!$ comes from the wrong recurrence $I_n = (n-1)I_{n-1}$; $720 = 6!$ is $\Gamma(7)$.""")

T.single(1, ["wallis", "sin-m-cos-n"], r"$\displaystyle\int_0^{\pi/2}\sin^2 x\cos^2 x\,dx$ equals",
         [r"$\frac{\pi}{16}$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{32}$", r"$\frac{1}{8}$"],
         r"""Both indices are even, so $K = \frac{\pi}{2}$:
$$\frac{1\cdot1}{4\cdot2}\cdot\frac{\pi}{2} = \frac{\pi}{16}.$$
Check: $\sin^2x\cos^2x = \frac{1}{8}(1 - \cos4x)$, whose integral over $[0, \pi/2]$ is $\frac{\pi}{16}$. $\frac18$ drops the $\frac{\pi}{2}$.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["wallis"], r"For $m, n > -1$, $\displaystyle\int_0^{\pi/2}\sin^m x\cos^n x\,dx$ equals",
         [r"$\frac12 B\!\left(\frac{m+1}{2}, \frac{n+1}{2}\right)$", r"$B\!\left(\frac{m+1}{2}, \frac{n+1}{2}\right)$",
          r"$\frac12 B(m+1, n+1)$", r"$\frac12 B\!\left(\frac{m}{2}, \frac{n}{2}\right)$"],
         r"""Put $t = \sin^2x$, so $dt = 2\sin x\cos x\,dx$:
$$\int_0^{\pi/2}\sin^mx\cos^nx\,dx = \frac12\int_0^1 t^{\frac{m-1}{2}}(1 - t)^{\frac{n-1}{2}}\,dt = \frac12B\!\left(\frac{m+1}{2}, \frac{n+1}{2}\right).$$
Check at $m = n = 0$: $\frac12B(\frac12, \frac12) = \frac{\pi}{2}$, as required. Without the $\frac12$ you get $\pi$.""")

T.single(2, ["wallis", "exam-tips"], r"$\displaystyle\int_0^{\pi/2}\sin^6 x\cos^4 x\,dx$ equals",
         [r"$\frac{3\pi}{512}$", r"$\frac{3}{256}$", r"$\frac{3\pi}{256}$", r"$\frac{3\pi}{1024}$"],
         r"""Both indices are even, so $K = \frac{\pi}{2}$:
$$\frac{(5\cdot3\cdot1)(3\cdot1)}{10\cdot8\cdot6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{45}{3840}\cdot\frac{\pi}{2} = \frac{3}{256}\cdot\frac{\pi}{2} = \frac{3\pi}{512}.$$
$\frac{3}{256}$ forgets the factor $\frac{\pi}{2}$; $\frac{3\pi}{256}$ multiplies by $\pi$ instead of $\frac{\pi}{2}$.""")

T.single(2, ["wallis", "sin-m-cos-n"], r"$\displaystyle\int_0^{\pi/2}\sin^5 x\cos^4 x\,dx$ equals",
         [r"$\frac{8}{315}$", r"$\frac{4\pi}{315}$", r"$\frac{16}{315}$", r"$\frac{8}{105}$"],
         r"""$m = 5$ is odd, so $K = 1$:
$$\frac{(4\cdot2)(3\cdot1)}{9\cdot7\cdot5\cdot3\cdot1} = \frac{24}{945} = \frac{8}{315}.$$
$\frac{4\pi}{315}$ wrongly includes $\frac{\pi}{2}$. Check by $c = \cos x$: $\int_0^1(1 - c^2)^2c^4\,dc = \frac15 - \frac27 + \frac19 = \frac{8}{315}$.""")

T.single(2, ["tan-sec-cot", "exam-tips"],
         r"Let $I_n = \displaystyle\int_0^{\pi/4}\tan^n x\,dx$. Given $I_3 = \frac12 - \frac12\ln 2$, the value of $I_5$ is",
         [r"$\frac12\ln2 - \frac14$", r"$\frac34 - \frac12\ln2$", r"$\frac12\ln2 - \frac{3}{10}$", r"$\frac12\ln2 + \frac14$"],
         r"""$I_5 + I_3 = \frac{1}{5-1} = \frac14$, so
$$I_5 = \frac14 - \left(\frac12 - \frac12\ln2\right) = \frac12\ln2 - \frac14 \approx 0.097.$$
$\frac34 - \frac12\ln2$ adds $I_3$ instead of subtracting it. $\frac12\ln2 - \frac{3}{10}$ uses $\frac15$ instead of $\frac14$, and it is negative, which is impossible for $I_5 > 0$.""")

T.single(2, ["tan-sec-cot"], r"$\displaystyle\int\sec^3 x\,dx$ equals",
         [r"$\frac12\sec x\tan x + \frac12\ln\lvert\sec x + \tan x\rvert + C$",
          r"$\frac12\sec x\tan x - \frac12\ln\lvert\sec x + \tan x\rvert + C$",
          r"$\sec x\tan x + \ln\lvert\sec x + \tan x\rvert + C$",
          r"$\frac12\sec x\tan x + \frac12\ln\lvert\sec x\rvert + C$"],
         r"""$(n-1)I_n = \sec^{n-2}x\tan x + (n-2)I_{n-2}$ with $n = 3$:
$$2I_3 = \sec x\tan x + \int\sec x\,dx = \sec x\tan x + \ln\lvert\sec x + \tan x\rvert.$$
Divide by 2. The third option is twice the answer: it forgets to divide by $n - 1 = 2$. The minus sign comes from a sign slip in $\tan^2 = \sec^2 - 1$.""")

T.single(2, ["other-reductions"], r"$\displaystyle\int_0^{1}\frac{dx}{(1 + x^2)^2}$ equals",
         [r"$\frac{\pi}{8} + \frac14$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{8} - \frac14$", r"$\frac{\pi}{4} + \frac14$"],
         r"""The reduction formula with $a = 1$, $n = 2$ gives
$$\int\frac{dx}{(1 + x^2)^2} = \frac{x}{2(1 + x^2)} + \frac12\tan^{-1}x.$$
From $0$ to $1$: $\frac14 + \frac12\cdot\frac{\pi}{4} = \frac{\pi}{8} + \frac14$.
$\frac{\pi}{8}$ drops the boundary term; $\frac{\pi}{4} + \frac14$ forgets the coefficient $\frac12$ on $I_1$.""")

T.single(2, ["other-reductions"],
         r"For $I_n = \displaystyle\int\frac{dx}{(x^2 + a^2)^n}$ ($n \ge 2$), the reduction formula is $I_n = \dfrac{x}{2(n-1)a^2(x^2 + a^2)^{n-1}} + k\,I_{n-1}$, where $k$ equals",
         [r"$\frac{2n-3}{2(n-1)a^2}$", r"$\frac{2n-1}{2na^2}$", r"$\frac{2n-3}{2(n-1)}$", r"$\frac{n-2}{(n-1)a^2}$"],
         r"""Parts on $I_{n-1}$ with $x^2 = (x^2 + a^2) - a^2$:
$$I_{n-1} = \frac{x}{(x^2 + a^2)^{n-1}} + 2(n-1)(I_{n-1} - a^2I_n).$$
So $2(n-1)a^2I_n = \frac{x}{(x^2 + a^2)^{n-1}} + (2n-3)I_{n-1}$, and $k = \frac{2n-3}{2(n-1)a^2}$.
Check at $a = 1$, $n = 2$: $k = \frac12$. The option without $a^2$ fails dimensionally.""")

T.single(2, ["other-reductions"],
         r"Let $J_n = \displaystyle\int_0^1 x^n e^x\,dx$, so that $J_n = e - nJ_{n-1}$ and $J_0 = e - 1$. Then $J_3$ equals",
         [r"$6 - 2e$", r"$3e - 6$", r"$e - 2$", r"$2e - 5$"],
         r"""Step by step:
$$J_1 = e - (e - 1) = 1, \quad J_2 = e - 2\cdot1 = e - 2, \quad J_3 = e - 3(e - 2) = 6 - 2e \approx 0.563.$$
$e - 2$ is $J_2$. Check: $0 < J_3 < J_2$, since $x^3 < x^2$ on $(0, 1)$, and $6 - 2e$ fits.""")

T.single(2, ["wallis", "sin-m-cos-n"], r"$\displaystyle\int_0^{\pi/2}\sin^4 x\cos^3 x\,dx$ equals",
         [r"$\frac{2}{35}$", r"$\frac{\pi}{35}$", r"$\frac{4}{35}$", r"$\frac{3\pi}{70}$"],
         r"""$n = 3$ is odd, so $K = 1$:
$$\frac{(3\cdot1)(2)}{7\cdot5\cdot3\cdot1} = \frac{6}{105} = \frac{2}{35}.$$
Check with $s = \sin x$: $\int_0^1 s^4(1 - s^2)\,ds = \frac15 - \frac17 = \frac{2}{35}$. $\frac{\pi}{35}$ wrongly multiplies by $\frac{\pi}{2}$.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["wallis"], r"$\displaystyle\int_0^{2\pi}\sin^4 x\cos^6 x\,dx$ equals",
         [r"$\frac{3\pi}{128}$", r"$\frac{3\pi}{512}$", r"$\frac{3\pi}{256}$", r"$0$"],
         r"""Both powers are even, so the integrand has period $\pi$ and is symmetric about $\frac{\pi}{2}$. The integral is $4$ times the Wallis value:
$$4\cdot\frac{(3\cdot1)(5\cdot3\cdot1)}{10\cdot8\cdot6\cdot4\cdot2}\cdot\frac{\pi}{2} = 4\cdot\frac{3\pi}{512} = \frac{3\pi}{128}.$$
$\frac{3\pi}{512}$ is only the $[0, \pi/2]$ part. $0$ would need an odd power.""")

T.single(3, ["wallis"], r"$\displaystyle\int_0^{1}x^4\sqrt{1 - x^2}\,dx$ equals",
         [r"$\frac{\pi}{32}$", r"$\frac{\pi}{16}$", r"$\frac{1}{16}$", r"$\frac{3\pi}{32}$"],
         r"""Put $x = \sin\theta$, so $dx = \cos\theta\,d\theta$:
$$\int_0^{\pi/2}\sin^4\theta\cos^2\theta\,d\theta = \frac{(3\cdot1)(1)}{6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{\pi}{32}.$$
$\frac{\pi}{16}$ multiplies by $\pi$ instead of $\frac{\pi}{2}$; $\frac{1}{16}$ drops the $\frac{\pi}{2}$ although both indices are even. Do not forget the $\cos\theta$ from $dx$: it turns $\sqrt{1 - x^2} = \cos\theta$ into $\cos^2\theta$.""")

T.single(3, ["other-reductions", "wallis"], r"$\displaystyle\int_0^{\infty}\frac{dx}{(1 + x^2)^4}$ equals",
         [r"$\frac{5\pi}{32}$", r"$\frac{5\pi}{16}$", r"$\frac{3\pi}{16}$", r"$\frac{16}{35}$"],
         r"""Put $x = \tan\theta$: $dx = \sec^2\theta\,d\theta$ and $(1 + x^2)^4 = \sec^8\theta$, so
$$\int_0^{\pi/2}\cos^6\theta\,d\theta = \frac{5\cdot3\cdot1}{6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{5\pi}{32}.$$
$\frac{3\pi}{16}$ uses $\cos^4\theta$ (forgetting the $\sec^2\theta$ from $dx$ raises the power); $\frac{16}{35}$ is $\int_0^{\pi/2}\cos^7$.""")

T.single(3, ["tan-sec-cot"], r"If $I_n = \displaystyle\int_0^{\pi/4}\tan^n x\,dx$, then $\displaystyle\lim_{n\to\infty} nI_n$ equals",
         [r"$\frac12$", r"$1$", r"$0$", r"$\frac{\pi}{4}$"],
         r"""$I_n$ is decreasing, since $0 \le \tan x \le 1$. With $I_n + I_{n-2} = \frac{1}{n-1}$:
$$2I_n < I_n + I_{n-2} = \frac{1}{n-1}, \qquad 2I_n > I_n + I_{n+2} = \frac{1}{n+1}.$$
So $\frac{n}{2(n+1)} < nI_n < \frac{n}{2(n-1)}$, and both bounds tend to $\frac12$.
$1$ is the limit of $n(I_n + I_{n+2})$, not of $nI_n$. $0$ is the limit of $I_n$ alone.""")

T.single(3, ["sin-cos-powers", "wallis"], r"If $I_n = \displaystyle\int_0^{\pi/2}\sin^n x\,dx$, then $\displaystyle\lim_{n\to\infty}\frac{I_{n+1}}{I_n}$ equals",
         [r"$1$", r"$0$", r"$\frac12$", r"$\frac{\pi}{2}$"],
         r"""$0 < \sin x < 1$ on $(0, \pi/2)$, so $I_{n+1} < I_n < I_{n-1}$. Hence
$$\frac{n}{n+1} = \frac{I_{n+1}}{I_{n-1}} < \frac{I_{n+1}}{I_n} < 1,$$
using $I_{n+1} = \frac{n}{n+1}I_{n-1}$. The left side tends to $1$, so the limit is $1$. (Each $I_n \to 0$, but the ratio does not.) This squeeze is the key step in Wallis's product.""")

T.single(3, ["sin-m-cos-n"], r"$\displaystyle\int_0^{\pi}\frac{\sin 6x}{\sin x}\,dx$ equals",
         [r"$0$", r"$\pi$", r"$6\pi$", r"$\frac{\pi}{2}$"],
         r"""Let $J_n = \int_0^\pi\frac{\sin nx}{\sin x}\,dx$. Since $\sin nx - \sin(n-2)x = 2\cos(n-1)x\sin x$,
$$J_n - J_{n-2} = 2\int_0^\pi\cos(n-1)x\,dx = 0 \quad (n \ge 2).$$
So $J_6 = J_4 = J_2 = J_0 = 0$. The value $\pi$ belongs to odd $n$, where the chain ends at $J_1 = \pi$.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["tan-sec-cot"],
             r"Let $I_n = \displaystyle\int_0^{\pi/4}\tan^n x\,dx$ for integers $n \ge 0$. Consider the following statements:",
             [r"$I_n + I_{n-2} = \frac{1}{n-1}$ for every $n \ge 2$.",
              r"$I_{n+1} < I_n$ for every $n \ge 0$.",
              r"$I_n > \frac{1}{2(n-1)}$ for every $n \ge 2$."],
             [r"1 and 2 only", r"1 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** $I_n + I_{n-2} = \int_0^{\pi/4}\tan^{n-2}x\sec^2x\,dx = \frac{1}{n-1}$.
- **2 is true:** $0 \le \tan x \le 1$ on $[0, \pi/4]$, with $\tan x < 1$ on $[0, \pi/4)$, so $\tan^{n+1}x \le \tan^n x$ with strict inequality on a set of positive length.
- **3 is false:** the inequality goes the other way. Since $I_n < I_{n-2}$, $2I_n < I_n + I_{n-2} = \frac{1}{n-1}$, so $I_n < \frac{1}{2(n-1)}$. For example, $I_2 = 1 - \frac{\pi}{4} \approx 0.215 < \frac12$.""")

T.statements(3, ["wallis", "exam-tips"],
             r"For non-negative integers $m$ and $n$, consider the following statements:",
             [r"$\displaystyle\int_0^{\pi/2}\sin^m x\cos^n x\,dx = \int_0^{\pi/2}\sin^n x\cos^m x\,dx$.",
              r"$\displaystyle\int_0^{\pi/2}\sin^n x\,dx = \int_0^{\pi/2}\cos^n x\,dx$.",
              r"$\displaystyle\int_0^{\pi}\sin^m x\cos^n x\,dx = 0$ whenever $n$ is odd."],
             [r"1, 2 and 3", r"1 and 2 only", r"2 and 3 only", r"2 only"],
             r"""- **1 is true:** the substitution $x \mapsto \frac{\pi}{2} - x$ swaps $\sin$ and $\cos$ and keeps the interval.
- **2 is true:** it is statement 1 with $m = 0$.
- **3 is true:** $x \mapsto \pi - x$ keeps $\sin x$ and changes $\cos x$ to $-\cos x$. With $n$ odd the integrand changes sign, so the integral equals its own negative. For example, $\int_0^\pi\sin^2x\cos x\,dx = \left[\frac{\sin^3x}{3}\right]_0^\pi = 0$.

The trap is to double the $[0, \pi/2]$ value in statement 3; that works only for even $n$.""")

# ---------------------------------------------------------------- match
T.match(2, ["tan-sec-cot", "sin-cos-powers"], r"Match each integral $I_n$ in List I ($n \ge 2$) with its reduction formula in List II.",
        [r"$\int\tan^n x\,dx$", r"$\int\cot^n x\,dx$", r"$\int\sec^n x\,dx$", r"$\int\cos^n x\,dx$"],
        [r"$\frac{\sec^{n-2}x\tan x}{n-1} + \frac{n-2}{n-1}I_{n-2}$", r"$-\frac{\cot^{n-1}x}{n-1} - I_{n-2}$",
         r"$\frac{\tan^{n-1}x}{n-1} - I_{n-2}$", r"$\frac{\cos^{n-1}x\sin x}{n} + \frac{n-1}{n}I_{n-2}$"],
        [r"A-3, B-2, C-1, D-4", r"A-2, B-3, C-1, D-4", r"A-3, B-2, C-4, D-1", r"A-1, B-2, C-3, D-4"],
        r"""- A: $\tan^n = \tan^{n-2}(\sec^2 - 1)$ gives $\frac{\tan^{n-1}x}{n-1} - I_{n-2}$: **3**.
- B: $\cot^n = \cot^{n-2}(\csc^2 - 1)$, and $\int\cot^{n-2}x\csc^2x\,dx = -\frac{\cot^{n-1}x}{n-1}$: **2**.
- C: parts with $u = \sec^{n-2}x$, $dv = \sec^2x\,dx$: **1**.
- D: parts with $u = \cos^{n-1}x$, $dv = \cos x\,dx$: **4**.

So A-3, B-2, C-1, D-4. Swapping A and B misses the minus sign that $\frac{d}{dx}\cot x = -\csc^2x$ brings in.""")

T.match(1, ["wallis"], r"Match each integral in List I with its value in List II.",
        [r"$\int_0^{\pi/2}\sin^3 x\,dx$", r"$\int_0^{\pi/2}\cos^6 x\,dx$",
         r"$\int_0^{\pi/2}\sin^2 x\cos^4 x\,dx$", r"$\int_0^{\pi/2}\sin^3 x\cos^3 x\,dx$"],
        [r"$\frac{1}{12}$", r"$\frac{\pi}{32}$", r"$\frac23$", r"$\frac{5\pi}{32}$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-4, C-1, D-2"],
        r"""- A: $\frac{2}{3\cdot1} = \frac23$: **3**.
- B: $\frac{5\cdot3\cdot1}{6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{5\pi}{32}$: **4**.
- C: $\frac{(1)(3\cdot1)}{6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{\pi}{32}$: **2**.
- D: $\frac{(2)(2)}{6\cdot4\cdot2} = \frac{1}{12}$, with no $\frac{\pi}{2}$ because the indices are odd: **1**.

So A-3, B-4, C-2, D-1. Only the even-index integrals carry a $\pi$.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["wallis", "sin-cos-powers"],
                   r"$\displaystyle\int_0^{\pi/2}\sin^8 x\,dx = \frac{35\pi}{256}$.",
                   r"If $I_n = \displaystyle\int_0^{\pi/2}\sin^n x\,dx$, then $I_n = \frac{n-1}{n}I_{n-2}$ for $n \ge 2$, and $I_0 = \frac{\pi}{2}$.",
                   0,
                   r"""**R is true:** the boundary term $-\frac{\sin^{n-1}x\cos x}{n}$ vanishes at $0$ and $\frac{\pi}{2}$.

**A is true, and R explains it:** applying R four times,
$$I_8 = \frac78\cdot\frac56\cdot\frac34\cdot\frac12\cdot\frac{\pi}{2} = \frac{105}{384}\cdot\frac{\pi}{2} = \frac{35\pi}{256}.$$""")

T.assertion_reason(2, ["tan-sec-cot"],
                   r"$\displaystyle\int_0^{\pi/4}\tan^3 x\,dx = \frac12$.",
                   r"If $I_n = \displaystyle\int_0^{\pi/4}\tan^n x\,dx$, then $I_n + I_{n-2} = \frac{1}{n-1}$ for $n \ge 2$.",
                   3,
                   r"""**R is true:** $I_n + I_{n-2} = \left[\frac{\tan^{n-1}x}{n-1}\right]_0^{\pi/4} = \frac{1}{n-1}$.

**A is false:** by R, $I_3 = \frac12 - I_1$, and $I_1 = \int_0^{\pi/4}\tan x\,dx = \frac12\ln 2$. So
$$I_3 = \frac12 - \frac12\ln2 \approx 0.153 \ne \frac12.$$
The value $\frac12$ is $I_3 + I_1$, not $I_3$.""")

T.assertion_reason(2, ["other-reductions", "exam-tips"],
                   r"$\displaystyle\int_0^{\infty}x^4e^{-x}\,dx = 24$.",
                   r"If $I_n = \displaystyle\int_0^{\infty}x^ne^{-x}\,dx$, then $I_n = (n-1)I_{n-1}$ for $n \ge 1$.",
                   2,
                   r"""**A is true:** $\int_0^\infty x^4e^{-x}\,dx = \Gamma(5) = 4! = 24$.

**R is false:** parts with $u = x^n$ gives
$$I_n = \left[-x^ne^{-x}\right]_0^\infty + n\int_0^\infty x^{n-1}e^{-x}\,dx = nI_{n-1}.$$
The factor is $n$, not $n - 1$. The shift by one comes from mixing this with $\Gamma(n) = (n-1)\Gamma(n-1)$.""")

T.assertion_reason(3, ["sin-cos-powers", "exam-tips"],
                   r"If $I_n = \displaystyle\int_0^{\pi/2}\sin^n x\,dx$, then $nI_nI_{n-1} = \frac{\pi}{2}$ for every $n \ge 1$.",
                   r"If $I_n = \displaystyle\int_0^{\pi/2}\sin^n x\,dx$, then $I_n$ is strictly decreasing in $n$.",
                   1,
                   r"""**A is true:** from $nI_n = (n-1)I_{n-2}$,
$$nI_nI_{n-1} = (n-1)I_{n-1}I_{n-2} = \cdots = 1\cdot I_1I_0 = \frac{\pi}{2}.$$

**R is true:** $0 < \sin x < 1$ on $(0, \pi/2)$, so $\sin^{n+1}x < \sin^n x$ there.

**But R does not explain A.** A follows from the recurrence by telescoping; monotonicity is never used. (R is what gives $I_{n+1}/I_n \to 1$ and Wallis's product.)""")

T.assertion_reason(2, ["other-reductions"],
                   r"$\displaystyle\int\frac{dx}{(x^2 + 1)^2} = \frac{x}{2(x^2 + 1)} + \frac12\tan^{-1}x + C$.",
                   r"For $n \ge 2$ and $a > 0$, $I_n = \displaystyle\int\frac{dx}{(x^2 + a^2)^n}$ satisfies $I_n = \dfrac{x}{2(n-1)a^2(x^2 + a^2)^{n-1}} + \dfrac{2n-3}{2(n-1)a^2}I_{n-1}$.",
                   0,
                   r"""**R is true:** integrate $I_{n-1}$ by parts and write $x^2 = (x^2 + a^2) - a^2$; then solve for $I_n$.

**A is true, and R explains it:** put $a = 1$, $n = 2$ in R:
$$I_2 = \frac{x}{2(x^2 + 1)} + \frac12I_1 = \frac{x}{2(x^2 + 1)} + \frac12\tan^{-1}x + C.$$""")


def check():
    import sympy as sp
    x, n = sp.symbols("x n")
    pi, ln, E = sp.pi, sp.log, sp.E
    R = sp.Rational

    def ne(a, b, label):
        if abs(complex(sp.N(a - b, 30))) < 1e-9:
            sys.exit(f"DISTRACTOR EQUALS KEY {label}: {a} vs {b}")

    def num(val, key, label):
        eq(sp.N(val, 30), sp.N(key, 30), label + " numeric")

    def I(f, a, b, label, key, wrong=()):
        v = sp.integrate(f, (x, a, b))
        eq(v, key, label)
        num(sp.Integral(f, (x, a, b)).evalf(30), key, label)
        for w in wrong:
            ne(key, w, label)

    def deriv_ok(F, f, label, pts=(R(3, 10), R(7, 10), R(11, 10))):
        for p in pts:
            eq(sp.N(sp.diff(F, x).subs(x, p) - f.subs(x, p), 30), 0, label)

    def deriv_bad(F, f, label, pts=(R(3, 10), R(7, 10))):
        if all(abs(sp.N(sp.diff(F, x).subs(x, p) - f.subs(x, p), 30)) < 1e-9 for p in pts):
            sys.exit(f"WRONG FORMULA PASSES {label}")

    s, c, t = sp.sin(x), sp.cos(x), sp.tan(x)
    S = lambda k: sp.integrate(sp.sin(x)**k, (x, 0, pi / 2))
    Tn = lambda k: sp.integrate(sp.tan(x)**k, (x, 0, pi / 4))

    I(s**5, 0, pi / 2, "q1", R(8, 15), [4 * pi / 15, 5 * pi / 32, R(15, 8)])
    I(c**4, 0, pi / 2, "q2", 3 * pi / 16, [R(3, 8), 3 * pi / 8, R(8, 15)])
    eq(Tn(4) + Tn(2), R(1, 3), "q3"); ne(R(1, 3), R(1, 4), "q3")
    # q4: formula check, n = 2..6, by differentiating F_n = boundary + coefficient * (antiderivative of I_{n-2})
    for k in range(2, 7):
        Fm2 = sp.integrate(s**(k - 2), x)
        deriv_ok(-s**(k - 1) * c / k + R(k - 1, k) * Fm2, s**k, f"q4 n={k}")
        deriv_bad(s**(k - 1) * c / k + R(k - 1, k) * Fm2, s**k, f"q4 d1 n={k}")
        deriv_bad(-s**(k - 1) * c / k - R(k - 1, k) * Fm2, s**k, f"q4 d2 n={k}")
        if k > 2:
            deriv_bad(-s**(k - 1) * c / (k - 1) + R(k - 2, k - 1) * Fm2, s**k, f"q4 d3 n={k}")
    I(x**5 * sp.exp(-x), 0, sp.oo, "q5", 120, [24, 720, 5])
    I(s**2 * c**2, 0, pi / 2, "q6", pi / 16, [pi / 8, pi / 32, R(1, 8)])
    # q7: beta form at several (m, n)
    for m_, n_ in [(0, 0), (2, 3), (6, 4), (5, 4), (R(1, 2), R(3, 2))]:
        lhs = sp.Integral(s**m_ * c**n_, (x, 0, pi / 2)).evalf(30)
        eq(lhs, sp.N(sp.beta(R(m_ + 1, 1) / 2, R(n_ + 1, 1) / 2) / 2, 30), f"q7 {m_},{n_}")
        ne(lhs, sp.beta(R(m_ + 1, 1) / 2, R(n_ + 1, 1) / 2), "q7 d")
        ne(lhs, sp.beta(m_ + 1, n_ + 1) / 2, "q7 d")
    I(s**6 * c**4, 0, pi / 2, "q8", 3 * pi / 512, [R(3, 256), 3 * pi / 256, 3 * pi / 1024])
    I(s**5 * c**4, 0, pi / 2, "q9", R(8, 315), [4 * pi / 315, R(16, 315), R(8, 105)])
    eq(Tn(3), R(1, 2) - ln(2) / 2, "q10 given"); eq(Tn(1), ln(2) / 2, "q10 I1")
    eq(Tn(5), ln(2) / 2 - R(1, 4), "q10")
    num(sp.Integral(t**5, (x, 0, pi / 4)).evalf(30), ln(2) / 2 - R(1, 4), "q10")
    for w in [R(3, 4) - ln(2) / 2, ln(2) / 2 - R(3, 10), ln(2) / 2 + R(1, 4)]:
        ne(ln(2) / 2 - R(1, 4), w, "q10")
    sec = 1 / c
    F12 = sec * t / 2 + ln(sec + t) / 2
    deriv_ok(F12, sec**3, "q11")
    deriv_bad(sec * t / 2 - ln(sec + t) / 2, sec**3, "q11 d1")
    deriv_bad(sec * t + ln(sec + t), sec**3, "q11 d2")
    deriv_bad(sec * t / 2 + ln(sec) / 2, sec**3, "q11 d3")
    I(1 / (1 + x**2)**2, 0, 1, "q12", pi / 8 + R(1, 4), [pi / 8, pi / 8 - R(1, 4), pi / 4 + R(1, 4)])
    # q13: verify the formula for a = 2, 3 and n = 2, 3, 4
    for a_ in [2, 3]:
        for k in [2, 3, 4]:
            In = 1 / (x**2 + a_**2)**k
            Fm1 = sp.integrate(1 / (x**2 + a_**2)**(k - 1), x)
            kk = R(2 * k - 3, 2 * (k - 1) * a_**2)
            deriv_ok(x / (2 * (k - 1) * a_**2 * (x**2 + a_**2)**(k - 1)) + kk * Fm1, In, f"q13 a={a_} n={k}")
            for wk in [R(2 * k - 1, 2 * k * a_**2), R(2 * k - 3, 2 * (k - 1)), R(k - 2, (k - 1) * a_**2)]:
                deriv_bad(x / (2 * (k - 1) * a_**2 * (x**2 + a_**2)**(k - 1)) + wk * Fm1, In, f"q13 d a={a_} n={k}")
    eq(sp.integrate(sp.exp(x), (x, 0, 1)), E - 1, "q14 J0")
    for k in range(1, 5):
        eq(sp.integrate(x**k * sp.exp(x), (x, 0, 1)), E - k * sp.integrate(x**(k - 1) * sp.exp(x), (x, 0, 1)), f"q14 rec {k}")
    I(x**3 * sp.exp(x), 0, 1, "q14", 6 - 2 * E, [3 * E - 6, E - 2, 2 * E - 5])
    I(s**4 * c**3, 0, pi / 2, "q15", R(2, 35), [pi / 35, R(4, 35), 3 * pi / 70])
    I(s**4 * c**6, 0, 2 * pi, "q16", 3 * pi / 128, [3 * pi / 512, 3 * pi / 256, 0])
    # q17: SymPy cannot do the x-integral directly; integrate after x = sin(theta), and check the original numerically
    I(s**4 * c**2, 0, pi / 2, "q17", pi / 32, [pi / 16, R(1, 16), 3 * pi / 32])
    num(sp.Integral(x**4 * sp.sqrt(1 - x**2), (x, 0, 1)).evalf(30), pi / 32, "q17 original")
    I(1 / (1 + x**2)**4, 0, sp.oo, "q18", 5 * pi / 32, [5 * pi / 16, 3 * pi / 16, R(16, 35)])
    # q19: bounds 1/(2(n+1)) < I_n < 1/(2(n-1)) for n = 2..12, and n I_n near 1/2 at n = 400
    for k in range(2, 13):
        v = Tn(k)
        if not (sp.N(1 / sp.Integer(2 * (k + 1))) < sp.N(v) < sp.N(1 / sp.Integer(2 * (k - 1)))):
            sys.exit(f"CHECK FAILED q20 bounds n={k}")
    v400 = 400 * sp.Integral(t**400, (x, 0, pi / 4)).evalf(30)
    if abs(v400 - 0.5) > 0.01:
        sys.exit(f"CHECK FAILED q20 limit {v400}")
    eq(sp.limit(n / (2 * (n + 1)), n, sp.oo), R(1, 2), "q19 lo"); eq(sp.limit(n / (2 * (n - 1)), n, sp.oo), R(1, 2), "q19 hi")
    # q20: I_{n+1}/I_n via the gamma form, limit 1
    Ig = lambda k: sp.sqrt(pi) * sp.gamma((k + 1) / 2) / (2 * sp.gamma(k / 2 + 1))
    for k in range(0, 9):
        eq(Ig(k), S(k), f"q20 gamma form n={k}")
    ratio = sp.N(Ig(sp.Integer(2001)) / Ig(sp.Integer(2000)), 30)
    if abs(ratio - 1) > 1e-3:
        sys.exit(f"CHECK FAILED q21 ratio {ratio}")
    eq(sp.limit(n / (n + 1), n, sp.oo), 1, "q20")
    # q21: J_n = int_0^pi sin(nx)/sin(x); J_6 = 0, J_5 = pi
    def J(k):
        f = sp.expand_trig(sp.sin(k * x)) / s
        return sp.integrate(sp.simplify(f), (x, 0, pi))
    eq(J(6), 0, "q21"); eq(J(5), pi, "q21 odd")
    num(sp.Integral(sp.sin(6 * x) / s, (x, 0, pi)).evalf(30), 0, "q21")
    for k in range(2, 8):
        eq(sp.expand(sp.expand_trig(sp.sin(k * x) - sp.sin((k - 2) * x) - 2 * sp.cos((k - 1) * x) * s)), 0, f"q21 identity {k}")
    # q22 statements: 1 true, 2 true, 3 false
    for k in range(2, 9):
        eq(Tn(k) + Tn(k - 2), R(1, k - 1), f"q22 s1 n={k}")
    for k in range(0, 9):
        if not sp.N(Tn(k + 1)) < sp.N(Tn(k)):
            sys.exit(f"CHECK FAILED q23 s2 n={k}")
    if not sp.N(Tn(2)) < sp.Rational(1, 2):
        sys.exit("CHECK FAILED q23 s3 counterexample")
    # q23 statements: all true
    for m_ in range(0, 5):
        for n_ in range(0, 5):
            eq(sp.integrate(s**m_ * c**n_, (x, 0, pi / 2)), sp.integrate(s**n_ * c**m_, (x, 0, pi / 2)), f"q23 s1 {m_},{n_}")
            if n_ % 2:
                eq(sp.integrate(s**m_ * c**n_, (x, 0, pi)), 0, f"q23 s3 {m_},{n_}")
    # q24 match: formulas by differentiation at n = 3, 4
    cot, csc = 1 / t, 1 / s
    for k in [3, 4]:
        deriv_ok(t**(k - 1) / (k - 1) - sp.integrate(t**(k - 2), x), t**k, f"q24 A {k}")
        deriv_ok(-cot**(k - 1) / (k - 1) - sp.integrate(cot**(k - 2), x), cot**k, f"q24 B {k}")
        deriv_ok(sec**(k - 2) * t / (k - 1) + R(k - 2, k - 1) * sp.integrate(sec**(k - 2), x), sec**k, f"q24 C {k}")
        deriv_ok(c**(k - 1) * s / k + R(k - 1, k) * sp.integrate(c**(k - 2), x), c**k, f"q24 D {k}")
    # q25 match values
    I(s**3, 0, pi / 2, "q25 A", R(2, 3)); I(c**6, 0, pi / 2, "q25 B", 5 * pi / 32)
    I(s**2 * c**4, 0, pi / 2, "q25 C", pi / 32); I(s**3 * c**3, 0, pi / 2, "q25 D", R(1, 12))
    # q26 AR
    I(s**8, 0, pi / 2, "q26", 35 * pi / 256)
    for k in range(2, 9):
        eq(S(k), R(k - 1, k) * S(k - 2), f"q26 R n={k}")
    # q27 AR: A false, R true
    ne(Tn(3), R(1, 2), "q27 A false")
    eq(Tn(3) + Tn(1), R(1, 2), "q27 R")
    # q28 AR: A true, R false
    I(x**4 * sp.exp(-x), 0, sp.oo, "q28", 24)
    G = lambda k: sp.integrate(x**k * sp.exp(-x), (x, 0, sp.oo))
    for k in range(1, 6):
        eq(G(k), k * G(k - 1), f"q28 true rec {k}")
    ne(G(4), 3 * G(3), "q28 R false")
    # q29 AR: A true, R true
    for k in range(1, 9):
        eq(k * S(k) * S(k - 1), pi / 2, f"q29 A n={k}")
        if not sp.N(S(k)) < sp.N(S(k - 1)):
            sys.exit(f"CHECK FAILED q30 R n={k}")
    # q30 AR: formula at a = 1, n = 2
    deriv_ok(x / (2 * (x**2 + 1)) + sp.atan(x) / 2, 1 / (x**2 + 1)**2, "q30")


T.write(check)
