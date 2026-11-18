# Reduction Formulae

## The idea: integrate by parts, then recycle {#method}

A **reduction formula** expresses an integral $I_n$ that depends on an integer index $n$ in terms of the same integral with a smaller index ($I_{n-1}$ or $I_{n-2}$). Applied repeatedly, it brings $I_n$ down to $I_0$ or $I_1$, which are elementary.

Almost every formula in this topic comes from one of two moves:

1. **Parts, then rewrite.** Split the integrand as $u\,dv$, integrate by parts, and use an identity ($\cos^2 x = 1 - \sin^2 x$, $\tan^2 x = \sec^2 x - 1$, $x^2 = (x^2 + a^2) - a^2$) to turn the new integral into a combination of $I_n$ and $I_{n-2}$. Then **solve for $I_n$**, since $I_n$ now appears on both sides.
2. **Peel off a derivative.** If $f'(x)$ appears as a factor, as $\sec^2 x$ does in $\tan^{n-2}x\,\sec^2 x$, integrate directly; no parts needed.

**Model derivation** ($I_n = \int \sin^n x\,dx$, $n \ge 2$). Take $u = \sin^{n-1}x$ and $dv = \sin x\,dx$:

$$I_n = -\sin^{n-1}x\cos x + (n-1)\int \sin^{n-2}x\cos^2 x\,dx = -\sin^{n-1}x\cos x + (n-1)(I_{n-2} - I_n).$$

Collect the two $I_n$ terms: $nI_n = -\sin^{n-1}x\cos x + (n-1)I_{n-2}$.

**Checking a formula.** Differentiate the boundary term and use the formula's claim. For example, the formula above is right exactly when

$$\frac{d}{dx}\left(-\frac{\sin^{n-1}x\cos x}{n}\right) = \sin^n x - \frac{n-1}{n}\sin^{n-2}x.$$

A quick check at $n = 2$: $\int\sin^2 x\,dx = -\tfrac12\sin x\cos x + \tfrac12 x$, which matches $\tfrac{x}{2} - \tfrac{\sin 2x}{4}$.

**Definite versions.** On limits where the boundary term vanishes (for example $[0, \pi/2]$ for $\sin^n x$), the formula becomes a pure recurrence between numbers. The definite recurrences give Wallis's formulae and the exam's favourite numerical questions.

:::exam-tip
In an MCQ, never re-derive. Test a candidate formula at the smallest index ($n = 2$, or $m = n = 1$) where both sides are known, or differentiate its boundary term.
:::

:::caution
A reduction formula has a **range of validity**: $n \ge 2$ for the $\sin^n$, $\tan^n$ and $\sec^n$ formulae, $m + n \ne 0$ for $\sin^m x\cos^n x$, and $n \ge 2$ for $1/(x^2 + a^2)^n$ (the coefficient $\frac{1}{n-1}$ explodes at $n = 1$).
:::

## Powers of sine and cosine {#sin-cos-powers}

For $n \ge 2$:

$$\int \sin^n x\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int \sin^{n-2}x\,dx,$$

$$\int \cos^n x\,dx = \frac{\cos^{n-1}x\sin x}{n} + \frac{n-1}{n}\int \cos^{n-2}x\,dx.$$

The cosine formula comes the same way, with $u = \cos^{n-1}x$ and $dv = \cos x\,dx$. **Sign memory:** the boundary term carries the sign of $\int\sin x = -\cos x$ (minus) or $\int\cos x = \sin x$ (plus). The coefficient $\frac{n-1}{n}$ is the same in both.

**Solved example.** $\int \cos^4 x\,dx$:

$$\int\cos^4 x\,dx = \frac{\cos^3 x\sin x}{4} + \frac34\left(\frac{\cos x\sin x}{2} + \frac{x}{2}\right) + C = \frac{\cos^3x\sin x}{4} + \frac{3\cos x\sin x}{8} + \frac{3x}{8} + C.$$

**Odd powers** are faster by substitution: $\int\sin^5 x\,dx = -\int(1 - c^2)^2\,dc$ with $c = \cos x$, which gives $-\cos x + \tfrac23\cos^3 x - \tfrac15\cos^5 x + C$.

**Over $[0, \pi/2]$.** The boundary terms $\sin^{n-1}x\cos x$ and $\cos^{n-1}x\sin x$ vanish at both ends when $n \ge 2$, so with $I_n = \int_0^{\pi/2}\sin^n x\,dx$:

$$I_n = \frac{n-1}{n}\,I_{n-2}, \qquad I_0 = \frac{\pi}{2}, \quad I_1 = 1.$$

The substitution $x \mapsto \frac{\pi}{2} - x$ shows $\int_0^{\pi/2}\cos^n x\,dx = \int_0^{\pi/2}\sin^n x\,dx$, so one table serves both.

**Two consequences** of the recurrence:

- $nI_nI_{n-1} = (n-1)I_{n-1}I_{n-2} = \cdots = 1\cdot I_1 I_0 = \dfrac{\pi}{2}$, so $nI_nI_{n-1} = \dfrac{\pi}{2}$ for all $n \ge 1$.
- $0 < \sin x < 1$ on $(0, \pi/2)$, so $I_n$ is **strictly decreasing**. With $\frac{I_{n+1}}{I_{n-1}} = \frac{n}{n+1} \to 1$, this squeeze gives $\frac{I_{n+1}}{I_n} \to 1$. Taking $n$ even turns this into **Wallis's product**:
  $$\frac{\pi}{2} = \lim_{n\to\infty}\frac{2\cdot2\cdot4\cdot4\cdots(2n)(2n)}{1\cdot3\cdot3\cdot5\cdots(2n-1)(2n+1)}.$$

## Wallis's formulae {#wallis}

Unwinding $I_n = \frac{n-1}{n}I_{n-2}$ down to $I_0$ or $I_1$:

:::keyfacts
- $\displaystyle\int_0^{\pi/2}\sin^n x\,dx = \int_0^{\pi/2}\cos^n x\,dx = \frac{(n-1)(n-3)\cdots}{n(n-2)\cdots}\times K$, where each product runs down to $1$ or $2$, and $K = \frac{\pi}{2}$ if $n$ is even, $K = 1$ if $n$ is odd.
- $\displaystyle\int_0^{\pi/2}\sin^m x\cos^n x\,dx = \frac{[(m-1)(m-3)\cdots]\,[(n-1)(n-3)\cdots]}{(m+n)(m+n-2)\cdots}\times K$, where $K = \frac{\pi}{2}$ **only if $m$ and $n$ are both even**, and $K = 1$ otherwise. An empty product (from $m = 0$ or $1$) counts as $1$.
- **Gamma form** (valid for all real $m, n > -1$):
  $$\int_0^{\pi/2}\sin^m x\cos^n x\,dx = \frac{\Gamma\!\left(\frac{m+1}{2}\right)\Gamma\!\left(\frac{n+1}{2}\right)}{2\,\Gamma\!\left(\frac{m+n+2}{2}\right)} = \frac12\,B\!\left(\frac{m+1}{2}, \frac{n+1}{2}\right).$$
:::

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\int_0^{\pi/2}\sin^n x\,dx$ | $\frac{\pi}{4}$ | $\frac23$ | $\frac{3\pi}{16}$ | $\frac{8}{15}$ | $\frac{5\pi}{32}$ | $\frac{16}{35}$ | $\frac{35\pi}{256}$ |

**Solved example** (the standard one). Both indices are even, so $K = \frac{\pi}{2}$:

$$\int_0^{\pi/2}\sin^6x\cos^4x\,dx = \frac{(5\cdot3\cdot1)(3\cdot1)}{10\cdot8\cdot6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{45}{3840}\cdot\frac{\pi}{2} = \frac{3\pi}{512}.$$

With one odd index, $K = 1$: $\displaystyle\int_0^{\pi/2}\sin^5x\cos^4x\,dx = \frac{(4\cdot2)(3\cdot1)}{9\cdot7\cdot5\cdot3\cdot1} = \frac{8}{315}$.

The integrals shrink as $n$ grows, because $\sin^n x \to 0$ everywhere on $[0, \pi/2)$:

```plot
title: $\sin^n x$ on $[0, \pi/2]$ for $n = 1, 2, 6$; the area under $\sin^6 x$ is $\frac{5\pi}{32}$
x: 0, pi/2
y: 0, 1.1
xticks: pi
f: sin(x) | $n = 1$
f: sin^2(x) | $n = 2$
f: sin^6(x) | $n = 6$
shade: sin^6(x), 0, pi/2
```

**Other ranges.** Use symmetry:
- $\int_0^{\pi}\sin^n x\,dx = 2\int_0^{\pi/2}\sin^n x\,dx$.
- $\int_0^{\pi}\sin^m x\cos^n x\,dx = 0$ for odd $n$; for even $n$ it is twice the $[0, \pi/2]$ value.
- $\int_0^{2\pi}\sin^m x\cos^n x\,dx = 4\int_0^{\pi/2}$ when $m, n$ are both even, and $0$ otherwise.

**Substitutions that lead to Wallis.** $x = \sin\theta$ turns $\int_0^1 x^m(1 - x^2)^{n/2}\,dx$ into $\int_0^{\pi/2}\sin^m\theta\cos^{n+1}\theta\,d\theta$. And $x = a\tan\theta$ turns $\int_0^\infty \frac{dx}{(x^2 + a^2)^n}$ into $\frac{1}{a^{2n-1}}\int_0^{\pi/2}\cos^{2n-2}\theta\,d\theta$.

:::exam-tip
Count the factors: the denominator always goes down from $m + n$ (or $n$) in steps of 2. Then decide $K$: $\frac{\pi}{2}$ appears **only** when every index is even. Forgetting $\frac{\pi}{2}$, or including it for an odd index, is the commonest wrong option.
:::

The Gamma form links this topic to the Beta and Gamma functions, which are treated with improper integrals.

## Products $\sin^m x\cos^n x$ {#sin-m-cos-n}

Let $I_{m,n} = \int \sin^m x\cos^n x\,dx$, with $m + n \ne 0$. Two reduction formulae lower one index by 2 and keep the other fixed.

**Lowering $n$.** Write the integrand as $\cos^{n-1}x\cdot(\sin^m x\cos x)$, take $u = \cos^{n-1}x$ and $v = \frac{\sin^{m+1}x}{m+1}$, then replace $\sin^{m+2} = \sin^m(1 - \cos^2)$:

$$I_{m,n} = \frac{\sin^{m+1}x\cos^{n-1}x}{m+n} + \frac{n-1}{m+n}\,I_{m,\,n-2}.$$

**Lowering $m$** (the same steps with the roles swapped):

$$I_{m,n} = -\frac{\sin^{m-1}x\cos^{n+1}x}{m+n} + \frac{m-1}{m+n}\,I_{m-2,\,n}.$$

On $[0, \pi/2]$ both boundary terms vanish (for $m \ge 2$ or $n \ge 2$ as needed), giving

$$I_{m,n} = \frac{n-1}{m+n}I_{m,n-2} = \frac{m-1}{m+n}I_{m-2,n}.$$

Repeating these gives Wallis's product formula above.

**Solved example.** $\int\sin^2x\cos^2x\,dx$ by lowering $n$:

$$I_{2,2} = \frac{\sin^3x\cos x}{4} + \frac14\int\sin^2x\,dx = \frac{\sin^3x\cos x}{4} + \frac{x}{8} - \frac{\sin x\cos x}{8} + C.$$

Over $[0, \pi/2]$ this is $\frac{\pi}{16}$, matching Wallis: $\frac{1\cdot1}{4\cdot2}\cdot\frac{\pi}{2}$.

**Negative indices.** The derivations use only the power rule, so the formulae hold for negative integers as long as no denominator vanishes. That covers quotients like $\int\frac{\sin^m x}{\cos^n x}\,dx = I_{m,-n}$. Some books state separate formulae for these, raising rather than lowering $n$.

**The "$\sin mx/\sin nx$" type.** The syllabus also lists an integral written $\int\sin^m x/\sin^n x\,dx$. A power quotient $\sin^m x/\sin^n x$ is just $\sin^{m-n}x$, so books read this item as the **multiple-angle quotient** $J_n = \int_0^{\pi}\frac{\sin nx}{\sin x}\,dx$. The identity $\sin nx - \sin(n-2)x = 2\cos(n-1)x\,\sin x$ gives

$$J_n - J_{n-2} = 2\int_0^{\pi}\cos(n-1)x\,dx = 0 \quad (n \ge 2),$$

so $J_n = J_1 = \pi$ for odd $n$ and $J_n = J_0 = 0$ for even $n$.

:::caution
Pick the formula that drives an index **to 0 or 1**. With $m$ odd, lower $m$; with $n$ odd, lower $n$. Lowering an even index of $\sin^3x\cos^2x$ leaves an odd one still to handle.
:::

## Powers of tangent, cotangent and secant {#tan-sec-cot}

For $n \ge 2$:

| Integral | Reduction formula | Key identity |
|:---|:---|:---|
| $\int\tan^n x\,dx$ | $\dfrac{\tan^{n-1}x}{n-1} - \int\tan^{n-2}x\,dx$ | $\tan^2 = \sec^2 - 1$ |
| $\int\cot^n x\,dx$ | $-\dfrac{\cot^{n-1}x}{n-1} - \int\cot^{n-2}x\,dx$ | $\cot^2 = \csc^2 - 1$ |
| $\int\sec^n x\,dx$ | $\dfrac{\sec^{n-2}x\tan x}{n-1} + \dfrac{n-2}{n-1}\int\sec^{n-2}x\,dx$ | parts, $\tan^2 = \sec^2 - 1$ |
| $\int\csc^n x\,dx$ | $-\dfrac{\csc^{n-2}x\cot x}{n-1} + \dfrac{n-2}{n-1}\int\csc^{n-2}x\,dx$ | parts, $\cot^2 = \csc^2 - 1$ |

**$\tan^n$ needs no parts:** $\tan^n x = \tan^{n-2}x\sec^2 x - \tan^{n-2}x$, and the first term integrates to $\frac{\tan^{n-1}x}{n-1}$.

**$\sec^n$:** take $u = \sec^{n-2}x$ and $dv = \sec^2x\,dx$:
$$I_n = \sec^{n-2}x\tan x - (n-2)\int\sec^{n-2}x\tan^2x\,dx = \sec^{n-2}x\tan x - (n-2)(I_n - I_{n-2}).$$
So $(n-1)I_n = \sec^{n-2}x\tan x + (n-2)I_{n-2}$. At $n = 3$:
$$\int\sec^3x\,dx = \frac12\sec x\tan x + \frac12\ln\lvert\sec x + \tan x\rvert + C.$$

### The relation on $[0, \pi/4]$

Let $I_n = \int_0^{\pi/4}\tan^n x\,dx$. Then

$$I_n + I_{n-2} = \int_0^{\pi/4}\tan^{n-2}x\sec^2x\,dx = \left[\frac{\tan^{n-1}x}{n-1}\right]_0^{\pi/4} = \frac{1}{n-1} \qquad (n \ge 2).$$

With $I_0 = \frac{\pi}{4}$ and $I_1 = \frac12\ln 2$:

$$I_2 = 1 - \frac{\pi}{4}, \quad I_3 = \frac12 - \frac12\ln2, \quad I_4 = \frac{\pi}{4} - \frac23, \quad I_5 = \frac12\ln2 - \frac14.$$

**Bounds.** $0 \le \tan x \le 1$ on $[0, \pi/4]$, so $I_n$ is strictly decreasing. Hence $2I_n < I_n + I_{n-2} = \frac{1}{n-1}$ and $2I_n > I_n + I_{n+2} = \frac{1}{n+1}$:

$$\frac{1}{2(n+1)} < I_n < \frac{1}{2(n-1)} \quad (n \ge 2), \qquad\text{so } I_n \to 0 \text{ and } nI_n \to \frac12.$$

:::exam-tip
"Find $I_5$ given $I_3$": $I_5 = \frac14 - I_3$. Use $\frac{1}{n-1}$ with the **larger** index $n = 5$, not $\frac1n$.
:::

## $x^n e^{ax}$ and $1/(x^2 + a^2)^n$ {#other-reductions}

### Exponential times a power

With $I_n = \int x^n e^{ax}\,dx$ ($a \ne 0$), take $u = x^n$ and $dv = e^{ax}dx$:

$$I_n = \frac{x^n e^{ax}}{a} - \frac{n}{a}\,I_{n-1}.$$

Unwinding gives $I_n = \dfrac{e^{ax}}{a}\left(x^n - \dfrac{n x^{n-1}}{a} + \dfrac{n(n-1)x^{n-2}}{a^2} - \cdots\right) + C$.

Definite versions:
- $\int_0^\infty x^n e^{-x}\,dx = n\int_0^\infty x^{n-1}e^{-x}\,dx = \cdots = n!$. This is $\Gamma(n+1)$, since the boundary term vanishes at both ends.
- $J_n = \int_0^1 x^n e^x\,dx$ satisfies $J_n = e - nJ_{n-1}$, with $J_0 = e - 1$. So $J_1 = 1$, $J_2 = e - 2$, $J_3 = 6 - 2e$.

The same pattern gives $\int(\ln x)^n\,dx = x(\ln x)^n - n\int(\ln x)^{n-1}\,dx$.

### $\int\dfrac{dx}{(x^2 + a^2)^n}$

Integrate $I_{n-1} = \int 1\cdot(x^2 + a^2)^{-(n-1)}\,dx$ by parts, then write $x^2 = (x^2 + a^2) - a^2$:

$$I_{n-1} = \frac{x}{(x^2 + a^2)^{n-1}} + 2(n-1)\left(I_{n-1} - a^2 I_n\right).$$

Solving for $I_n$ ($n \ge 2$):

$$I_n = \frac{x}{2(n-1)a^2(x^2 + a^2)^{n-1}} + \frac{2n-3}{2(n-1)a^2}\,I_{n-1}, \qquad I_1 = \frac1a\tan^{-1}\frac{x}{a}.$$

**Solved example.** For $a = 1$, $n = 2$:
$$\int\frac{dx}{(1 + x^2)^2} = \frac{x}{2(1 + x^2)} + \frac12\tan^{-1}x + C, \qquad \int_0^1\frac{dx}{(1 + x^2)^2} = \frac14 + \frac{\pi}{8}.$$

Over $[0, \infty)$ the boundary term vanishes. Alternatively, $x = \tan\theta$ gives Wallis directly: $\int_0^\infty\frac{dx}{(1 + x^2)^4} = \int_0^{\pi/2}\cos^6\theta\,d\theta = \frac{5\pi}{32}$.

:::caution
Do not mix the factors: the coefficient is $\frac{2n-3}{2(n-1)a^2}$ and the boundary term has denominator $2(n-1)a^2(x^2 + a^2)^{n-1}$. Check at $n = 2$, $a = 1$: the coefficient must be $\frac12$.
:::

## Quick checks and traps {#exam-tips}

- **Wallis in one line:** $\int_0^{\pi/2}\sin^6x\cos^4x\,dx = \frac{5\cdot3\cdot1\cdot3\cdot1}{10\cdot8\cdot6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{3\pi}{512}$. The factor $\frac{\pi}{2}$ appears only when all indices are even.
- **Symmetry:** $\int_0^{\pi/2}\sin^m x\cos^n x\,dx = \int_0^{\pi/2}\sin^n x\cos^m x\,dx$ (put $x \mapsto \frac{\pi}{2} - x$).
- **Tan on $[0, \pi/4]$:** $I_n + I_{n-2} = \frac{1}{n-1}$. So $I_4 + I_2 = \frac13$, $I_5 = \frac14 - I_3$, and $\frac{1}{2(n+1)} < I_n < \frac{1}{2(n-1)}$.
- **Sine powers on $[0, \pi/2]$:** $nI_n = (n-1)I_{n-2}$, $\;nI_nI_{n-1} = \frac{\pi}{2}$, and $I_{n+1}/I_n \to 1$.
- **Gamma integral:** $\int_0^\infty x^ne^{-x}\,dx = n!$, from $I_n = nI_{n-1}$ (not $(n-1)I_{n-1}$).
- **$\sec^3$:** $\frac12\sec x\tan x + \frac12\ln\lvert\sec x + \tan x\rvert$. Both halves have a $+$ sign.
- **Over $[0, \pi]$ or $[0, 2\pi]$:** an odd power of $\cos$ gives $0$ on $[0, \pi]$. With both indices even, $[0, 2\pi]$ gives four times the $[0, \pi/2]$ value.
- **$\int_0^\pi\frac{\sin nx}{\sin x}\,dx$** is $\pi$ for odd $n$ and $0$ for even $n$.
- **Verify a formula** by testing it at $n = 2$ against a known integral, or by differentiating the boundary term.
