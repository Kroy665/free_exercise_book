# Methods of Integration

## Standard integrals {#standard-forms}

Throughout, $\ln$ is the natural logarithm, $a > 0$, and every answer carries an arbitrary constant $+C$. An antiderivative is valid **on an interval** where the integrand is continuous; two antiderivatives of the same function on an interval differ by a constant.

| Integrand | Integral |
|:---|:---|
| $x^n\ (n \ne -1)$ | $\dfrac{x^{n+1}}{n+1}$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert$ |
| $\tan x$ | $\ln\lvert\sec x\rvert$ |
| $\cot x$ | $\ln\lvert\sin x\rvert$ |
| $\sec x$ | $\ln\lvert\sec x + \tan x\rvert = \ln\left\lvert\tan\left(\frac{\pi}{4} + \frac{x}{2}\right)\right\rvert$ |
| $\operatorname{cosec} x$ | $\ln\lvert\operatorname{cosec} x - \cot x\rvert = \ln\left\lvert\tan\frac{x}{2}\right\rvert$ |
| $\dfrac{1}{a^2 + x^2}$ | $\dfrac{1}{a}\tan^{-1}\dfrac{x}{a}$ |
| $\dfrac{1}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert$ |
| $\dfrac{1}{a^2 - x^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{a + x}{a - x}\right\rvert$ |
| $\dfrac{1}{\sqrt{a^2 - x^2}}$ | $\sin^{-1}\dfrac{x}{a}$ |
| $\dfrac{1}{\sqrt{x^2 \pm a^2}}$ | $\ln\left\lvert x + \sqrt{x^2 \pm a^2}\right\rvert$ |
| $\dfrac{1}{x\sqrt{x^2 - a^2}}$ | $\dfrac{1}{a}\sec^{-1}\dfrac{x}{a}\quad (x > a)$ |
| $\sqrt{a^2 - x^2}$ | $\dfrac{x}{2}\sqrt{a^2 - x^2} + \dfrac{a^2}{2}\sin^{-1}\dfrac{x}{a}$ |
| $\sqrt{x^2 \pm a^2}$ | $\dfrac{x}{2}\sqrt{x^2 \pm a^2} \pm \dfrac{a^2}{2}\ln\left\lvert x + \sqrt{x^2 \pm a^2}\right\rvert$ |

**Completing the square** reduces any $\dfrac{1}{ax^2 + bx + c}$ or $\dfrac{1}{\sqrt{ax^2 + bx + c}}$ to one row of the table:

$$\int\frac{dx}{x^2 + 4x + 13} = \int\frac{dx}{(x + 2)^2 + 3^2} = \frac{1}{3}\tan^{-1}\frac{x + 2}{3} + C.$$

:::caution
Do not swap the two logarithmic forms. $\int\frac{dx}{x^2 - a^2}$ has $\frac{x - a}{x + a}$, while $\int\frac{dx}{a^2 - x^2}$ has $\frac{a + x}{a - x}$. They differ by a sign, not a constant. Also, $\ln\lvert\operatorname{cosec} x + \cot x\rvert$ is $-\ln\lvert\tan\frac{x}{2}\rvert$, so it is the **negative** of $\int\operatorname{cosec} x\,dx$.
:::

:::exam-tip
To test an option, differentiate it. This is almost always faster than integrating, and it settles sign and factor slips at once.
:::

## Substitution {#substitution}

If $x = \phi(t)$ with $\phi$ differentiable and $\phi'$ continuous, then

$$\int f(x)\,dx = \int f(\phi(t))\,\phi'(t)\,dt.$$

Read the other way: if the integrand has the shape $g(\psi(x))\,\psi'(x)$, put $u = \psi(x)$. Three patterns cover most exam questions:

$$\int\frac{f'(x)}{f(x)}\,dx = \ln\lvert f(x)\rvert, \qquad \int [f(x)]^n f'(x)\,dx = \frac{[f(x)]^{n+1}}{n + 1}\ (n \ne -1), \qquad \int f(ax + b)\,dx = \frac{F(ax + b)}{a}.$$

**Examples.**

- $\displaystyle\int\frac{\cos x}{(1 + \sin x)^2}\,dx$: with $u = 1 + \sin x$ this is $\int u^{-2}\,du = -\frac{1}{1 + \sin x} + C$.
- $\displaystyle\int\frac{dx}{e^x + e^{-x}} = \int\frac{e^x\,dx}{e^{2x} + 1} = \tan^{-1}(e^x) + C$ (put $u = e^x$).
- $\displaystyle\int\frac{dx}{x\ln x} = \ln\lvert\ln x\rvert + C$ (put $u = \ln x$; valid for $x > 0$, $x \ne 1$).

**Trigonometric substitutions** remove square roots:

| Expression | Substitution |
|:---|:---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ (or $a\sinh t$) |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ (or $a\cosh t$) |
| $\sqrt{\dfrac{a - x}{a + x}}$ | $x = a\cos 2\theta$ |

:::caution
**Different-looking answers can both be right.** $\int\sin x\cos x\,dx$ is $\frac{1}{2}\sin^2 x$ (put $u = \sin x$), or $-\frac{1}{2}\cos^2 x$ (put $u = \cos x$), or $-\frac{1}{4}\cos 2x$. They differ by constants. Before rejecting an option, check whether it differs from yours only by a constant.
:::

## Integration by parts {#by-parts}

For $u, v$ with continuous derivatives:

$$\int u\,v'\,dx = uv - \int u'\,v\,dx.$$

Choose $u$ as the factor that comes first in **ILATE**: Inverse trigonometric, Logarithmic, Algebraic, Trigonometric, Exponential.

- $\int\ln x\,dx = x\ln x - x$ (take $v' = 1$).
- $\int\tan^{-1}x\,dx = x\tan^{-1}x - \frac{1}{2}\ln(1 + x^2)$.
- $\int x^2 e^x\,dx = e^x(x^2 - 2x + 2)$. In general, for a polynomial $p$, $\int p(x)e^x\,dx = e^x(p - p' + p'' - \cdots)$.

**The $e^x(f + f')$ rule.** Since $\frac{d}{dx}\left(e^x f(x)\right) = e^x\left(f(x) + f'(x)\right)$,

$$\int e^x\left(f(x) + f'(x)\right)dx = e^x f(x) + C.$$

Split the integrand into a function plus its derivative:

- $\int e^x\left(\frac{1}{x} - \frac{1}{x^2}\right)dx = \frac{e^x}{x}$.
- $\int\frac{x e^x}{(x + 1)^2}\,dx$: $\frac{x}{(x+1)^2} = \frac{1}{x + 1} - \frac{1}{(x + 1)^2}$, so the answer is $\frac{e^x}{x + 1}$.
- $\int e^x\frac{1 + \sin x}{1 + \cos x}\,dx$: $\frac{1 + \sin x}{1 + \cos x} = \tan\frac{x}{2} + \frac{1}{2}\sec^2\frac{x}{2}$, so the answer is $e^x\tan\frac{x}{2}$.

**Recurring integrals.** Parts twice brings back the original integral $I$; solve for $I$:

$$\int e^{ax}\sin bx\,dx = \frac{e^{ax}(a\sin bx - b\cos bx)}{a^2 + b^2}, \qquad \int e^{ax}\cos bx\,dx = \frac{e^{ax}(a\cos bx + b\sin bx)}{a^2 + b^2}.$$

The same method proves the $\sqrt{a^2 - x^2}$ and $\sqrt{x^2 \pm a^2}$ rows of the table.

:::exam-tip
Check the recurring formulas at $x = 0$ by differentiating: $\frac{d}{dx}\left[e^{ax}(a\sin bx - b\cos bx)\right]$ at $x = 0$ is $-ab + ab = 0 = \sin 0\cdot(a^2 + b^2)$. With the sign $+b\cos bx$ instead, you get $2ab \ne 0$.
:::

## Rational functions: partial fractions {#partial-fractions}

Let $P/Q$ be a rational function with real coefficients.

1. **Make it proper.** If $\deg P \ge \deg Q$, divide first: $\frac{P}{Q} = S + \frac{R}{Q}$ with $\deg R < \deg Q$.
2. **Factor $Q$ over $\R$** into linear factors and irreducible quadratics ($b^2 < 4ac$).
3. **Write the form:**

| Factor of $Q$ | Terms contributed |
|:---|:---|
| $(x - a)$ | $\dfrac{A}{x - a}$ |
| $(x - a)^k$ | $\dfrac{A_1}{x - a} + \dfrac{A_2}{(x - a)^2} + \cdots + \dfrac{A_k}{(x - a)^k}$ |
| $x^2 + px + q$ (irreducible) | $\dfrac{Bx + C}{x^2 + px + q}$ |

**Cover-up rule.** For a simple factor $(x - a)$ of $Q$, $A = \dfrac{P(a)}{Q'(a)}$; equivalently, cover the factor and put $x = a$ in the rest.

**Examples.**

$$\frac{1}{(x - 1)(x + 2)} = \frac{1/3}{x - 1} - \frac{1/3}{x + 2}, \qquad \int = \frac{1}{3}\ln\left\lvert\frac{x - 1}{x + 2}\right\rvert.$$

$$\frac{1}{x(x + 1)^2} = \frac{1}{x} - \frac{1}{x + 1} - \frac{1}{(x + 1)^2}, \qquad \int = \ln\left\lvert\frac{x}{x + 1}\right\rvert + \frac{1}{x + 1}.$$

$$\frac{1}{x(x^2 + 1)} = \frac{1}{x} - \frac{x}{x^2 + 1}, \qquad \int = \ln\lvert x\rvert - \frac{1}{2}\ln(x^2 + 1).$$

**Integrating $\frac{Bx + C}{x^2 + px + q}$.** Write $Bx + C = \frac{B}{2}(2x + p) + \left(C - \frac{Bp}{2}\right)$. The first part gives a logarithm, the second a $\tan^{-1}$ after completing the square.

**The $x^4 + 1$ trick.** Divide by $x^2$ and substitute:

$$\int\frac{x^2 + 1}{x^4 + 1}\,dx = \int\frac{1 + 1/x^2}{(x - 1/x)^2 + 2}\,dx = \frac{1}{\sqrt2}\tan^{-1}\frac{x^2 - 1}{\sqrt2\,x},$$

$$\int\frac{x^2 - 1}{x^4 + 1}\,dx = \int\frac{1 - 1/x^2}{(x + 1/x)^2 - 2}\,dx = \frac{1}{2\sqrt2}\ln\left\lvert\frac{x^2 - \sqrt2\,x + 1}{x^2 + \sqrt2\,x + 1}\right\rvert.$$

:::caution
A repeated factor $(x - a)^2$ needs **both** $\frac{A_1}{x - a}$ and $\frac{A_2}{(x - a)^2}$. An irreducible quadratic needs a **linear** numerator $Bx + C$, not a constant.
:::

## The half-angle substitution: $\int\frac{dx}{a + b\cos x}$ {#half-angle}

Put $t = \tan\frac{x}{2}$. Then

$$\cos x = \frac{1 - t^2}{1 + t^2}, \qquad \sin x = \frac{2t}{1 + t^2}, \qquad dx = \frac{2\,dt}{1 + t^2},$$

and

$$\int\frac{dx}{a + b\cos x} = \int\frac{2\,dt}{(a + b) + (a - b)t^2}.$$

Take $a, b > 0$ (a negative $b$ is handled by $x \mapsto \pi - x$). Three cases:

| Case | $\displaystyle\int\frac{dx}{a + b\cos x}$ |
|:---|:---|
| $a > b$ | $\dfrac{2}{\sqrt{a^2 - b^2}}\tan^{-1}\left(\sqrt{\dfrac{a - b}{a + b}}\tan\dfrac{x}{2}\right)$ |
| $a < b$ | $\dfrac{1}{\sqrt{b^2 - a^2}}\ln\left\lvert\dfrac{\sqrt{b + a} + \sqrt{b - a}\,\tan\frac{x}{2}}{\sqrt{b + a} - \sqrt{b - a}\,\tan\frac{x}{2}}\right\rvert$ |
| $a = b$ | $\dfrac{1}{a}\tan\dfrac{x}{2}$, since $1 + \cos x = 2\cos^2\frac{x}{2}$ |

Similarly $\int\frac{dx}{a(1 - \cos x)} = -\frac{1}{a}\cot\frac{x}{2}$. The same substitution handles $\frac{1}{a + b\sin x}$ and $\frac{1}{a + b\cos x + c\sin x}$.

**Example.** $\int\frac{dx}{5 + 4\cos x}$: $a = 5$, $b = 4$, $\sqrt{a^2 - b^2} = 3$, $\sqrt{\frac{a - b}{a + b}} = \frac{1}{3}$, so the answer is $\frac{2}{3}\tan^{-1}\left(\frac{1}{3}\tan\frac{x}{2}\right)$.

**Example.** $\int\frac{dx}{3 + 5\cos x}$: $a < b$, $\sqrt{b^2 - a^2} = 4$, $\sqrt{b + a} = 2\sqrt2$, $\sqrt{b - a} = \sqrt2$. Cancelling $\sqrt2$ gives $\frac{1}{4}\ln\left\lvert\frac{2 + \tan(x/2)}{2 - \tan(x/2)}\right\rvert$.

```plot
title: $\int\frac{dx}{2 + \cos x}$, the $\tan\frac{x}{2}$ form jumps at $x = \pm\pi$
x: -3pi, 3pi
y: -3, 7
xticks: pi
f: 1/(2 + cos(x)) | integrand
f: 2/sqrt(3)*atan(tan(x/2)/sqrt(3)) | $\tan\frac{x}{2}$ form
f: 2/sqrt(3)*atan(tan(x/2)/sqrt(3)) + 2pi/sqrt(3)*floor((x + pi)/(2pi)) | continuous antiderivative
vline: pi
vline: -pi
```

:::caution
The formula from $t = \tan\frac{x}{2}$ is an antiderivative only on intervals avoiding $x = (2k + 1)\pi$, where $\tan\frac{x}{2}$ is undefined. Across those points it jumps by $\frac{2\pi}{\sqrt{a^2 - b^2}}$. This matters for **definite** integrals over $[0, 2\pi]$ (a later topic).
:::

## Trigonometric quotients {#trig-quotients}

### $\int\frac{l\sin x + m\cos x}{n\sin x + p\cos x}\,dx$

Write the numerator as a multiple of the denominator **plus** a multiple of its derivative $n\cos x - p\sin x$:

$$l\sin x + m\cos x = A(n\sin x + p\cos x) + B(n\cos x - p\sin x).$$

Comparing coefficients, $l = An - Bp$ and $m = Ap + Bn$, so

$$A = \frac{ln + mp}{n^2 + p^2}, \quad B = \frac{mn - lp}{n^2 + p^2}, \qquad \int = Ax + B\ln\lvert n\sin x + p\cos x\rvert + C.$$

**Example.** $\int\frac{\sin x}{\sin x + \cos x}\,dx$: $\sin x = \frac{1}{2}(\sin x + \cos x) - \frac{1}{2}(\cos x - \sin x)$, so the answer is $\frac{x}{2} - \frac{1}{2}\ln\lvert\sin x + \cos x\rvert$.

### $\int\frac{dx}{a\sin x + b\cos x}$

Write $a\sin x + b\cos x = r\sin(x + \alpha)$ with $r = \sqrt{a^2 + b^2}$, $\tan\alpha = \frac{b}{a}$. Then

$$\int\frac{dx}{a\sin x + b\cos x} = \frac{1}{r}\int\operatorname{cosec}(x + \alpha)\,dx = \frac{1}{\sqrt{a^2 + b^2}}\ln\left\lvert\tan\frac{x + \alpha}{2}\right\rvert.$$

For example, $\sin x + \cos x = \sqrt2\sin\left(x + \frac{\pi}{4}\right)$, so $\int\frac{dx}{\sin x + \cos x} = \frac{1}{\sqrt2}\ln\left\lvert\tan\left(\frac{x}{2} + \frac{\pi}{8}\right)\right\rvert$.

### $\int\frac{dx}{a + b\sin^2 x}$ and relatives

Divide the numerator and denominator by $\cos^2 x$ and put $t = \tan x$:

$$\int\frac{\sec^2 x\,dx}{a\sec^2 x + b\tan^2 x} = \int\frac{dt}{a + (a + b)t^2}.$$

For $a > 0$, $a + b > 0$ this is $\dfrac{1}{\sqrt{a(a + b)}}\tan^{-1}\left(\sqrt{\dfrac{a + b}{a}}\tan x\right)$. The same move gives

$$\int\frac{dx}{a^2\sin^2 x + b^2\cos^2 x} = \frac{1}{ab}\tan^{-1}\left(\frac{a\tan x}{b}\right) \quad (a, b > 0).$$

:::exam-tip
Use $t = \tan x$ when the integrand is even in $\sin x$ and $\cos x$ together (only $\sin^2$, $\cos^2$, $\sin x\cos x$). Use $t = \tan\frac{x}{2}$ for first powers such as $a + b\cos x$.
:::

## Irrational integrands {#irrational}

**Type 1: $\int\frac{dx}{\sqrt{ax^2 + bx + c}}$ and $\int\sqrt{ax^2 + bx + c}\,dx$.** Complete the square and use the table:

$$\int\frac{dx}{\sqrt{x^2 + 2x + 5}} = \int\frac{dx}{\sqrt{(x + 1)^2 + 2^2}} = \ln\left\lvert x + 1 + \sqrt{x^2 + 2x + 5}\right\rvert + C.$$

The sign of $a$ decides the family: $a > 0$ gives logarithms, $a < 0$ gives $\sin^{-1}$.

**Type 2: $\int\frac{px + q}{\sqrt{ax^2 + bx + c}}\,dx$.** Write $px + q = \lambda(2ax + b) + \mu$. The $\lambda$ part integrates to $2\lambda\sqrt{ax^2 + bx + c}$; the $\mu$ part is Type 1.

Example: $\int\frac{x + 2}{\sqrt{x^2 + 1}}\,dx = \sqrt{x^2 + 1} + 2\ln\left(x + \sqrt{x^2 + 1}\right)$.

**Type 3: $\int\frac{dx}{(px + q)\sqrt{ax^2 + bx + c}}$.** Put $px + q = \frac{1}{t}$. This reduces it to Type 1 in $t$.

Example: $\int\frac{dx}{(x + 1)\sqrt{x^2 - 1}}$ for $x > 1$. Put $x + 1 = \frac{1}{t}$, so $dx = -\frac{dt}{t^2}$ and $x^2 - 1 = \frac{1 - 2t}{t^2}$. Then

$$\int\frac{-dt/t^2}{(1/t)\sqrt{1 - 2t}/t} = -\int\frac{dt}{\sqrt{1 - 2t}} = \sqrt{1 - 2t} = \sqrt{\frac{x - 1}{x + 1}} + C.$$

**Type 4: $\int\frac{dx}{(px + q)\sqrt{rx + s}}$.** Put $rx + s = u^2$; this gives a rational function of $u$.

:::caution
$\int\frac{dx}{\sqrt{x^2 + a^2}}$ is a **logarithm**, not $\sin^{-1}$ or $\tan^{-1}$. Also, keep the "$+1$" from completing the square inside the logarithm: $\ln\left\lvert x + 1 + \sqrt{\cdots}\right\rvert$, not $\ln\left\lvert x + \sqrt{\cdots}\right\rvert$.
:::

## Quick checks and traps {#exam-tips}

- **Differentiate the options.** One derivative usually settles a question in under a minute.
- **Constants hide in answers.** $\tan^{-1}x$ and $-\cot^{-1}x$, $\frac{1}{2}\sin^2 x$ and $-\frac{1}{4}\cos 2x$ differ only by constants.
- **$\ln\lvert x\rvert$, not $\ln x$**, for $\int\frac{dx}{x}$ on $x < 0$.
- **Standard-form slips:** $\int\frac{dx}{a^2 + x^2} = \frac{1}{a}\tan^{-1}\frac{x}{a}$, not $a\tan^{-1}\frac{x}{a}$; $\int\frac{dx}{x^2 - a^2}$ has the factor $\frac{1}{2a}$.
- **$e^x(f + f')$:** look for a function and its derivative side by side; for example $\int e^x(\sin x + \cos x)\,dx = e^x\sin x$.
- **$\frac{1}{a + b\cos x}$:** compare $a$ and $b$ first. $a > b$ gives $\tan^{-1}$, $a < b$ gives a logarithm, $a = b$ gives $\frac{1}{a}\tan\frac{x}{2}$.
- **$\frac{l\sin x + m\cos x}{n\sin x + p\cos x}$:** the answer is always $Ax + B\ln\lvert\text{denominator}\rvert$. Here $A = \frac{ln + mp}{n^2 + p^2}$ and $B = \frac{mn - lp}{n^2 + p^2}$; check by recombining $A(\text{den}) + B(\text{den})'$.
- **Partial fractions:** divide first if the fraction is improper; check a coefficient by the cover-up rule.
- **Later topics:** definite integrals and their properties, and reduction formulae such as $\int\sin^n x\,dx$, are treated separately.
