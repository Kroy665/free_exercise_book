# Higher-Order Linear Equations

## Linear equations and the structure of solutions {#linear-theory}

A **linear equation of order $n$** has the form

$$L[y] \equiv a_0(x)y^{(n)} + a_1(x)y^{(n-1)} + \cdots + a_{n-1}(x)y' + a_n(x)y = R(x).$$

It is linear because $y$ and its derivatives occur only to the first degree and are never multiplied together. It is **homogeneous** if $R \equiv 0$. (First-order linear, Bernoulli and Clairaut equations belong to the previous topics.)

**Linearity of the operator.** $L[c_1y_1 + c_2y_2] = c_1L[y_1] + c_2L[y_2]$. Two consequences:

- **Superposition:** any linear combination of solutions of $L[y] = 0$ is again a solution.
- If $L[y_1] = R_1$ and $L[y_2] = R_2$, then $L[y_1 + y_2] = R_1 + R_2$. So a right side that is a sum can be handled term by term.

:::keyfacts
- **Existence and uniqueness (statement).** If $a_0, \dots, a_n, R$ are continuous on an interval $I$ and $a_0(x) \ne 0$ on $I$, then for each $x_0 \in I$ and any numbers $b_0, \dots, b_{n-1}$ there is **exactly one** solution on $I$ with $y(x_0) = b_0, \dots, y^{(n-1)}(x_0) = b_{n-1}$.
- **Dimension.** Under the same hypotheses, the solutions of $L[y] = 0$ form a vector space of dimension exactly $n$. Any $n$ linearly independent solutions $y_1, \dots, y_n$ (a **fundamental set**) give every solution as $c_1y_1 + \cdots + c_ny_n$.
- **General solution** of $L[y] = R$:
  $$y = \underbrace{c_1y_1 + \cdots + c_ny_n}_{\text{complementary function (CF)}} + \underbrace{y_p}_{\text{particular integral (PI)}}.$$
:::

The difference of two solutions of $L[y] = R$ solves $L[y] = 0$. So any one particular solution, plus the CF, gives all solutions. Two different-looking PIs are both correct if they differ by a member of the CF.

**Example.** $y = x$ solves $y'' + y = x$, and the CF is $c_1\cos x + c_2\sin x$. So the general solution is $y = c_1\cos x + c_2\sin x + x$. The PI $x + 3\cos x$ is equally valid.

:::caution
Uniqueness is for an **initial value problem** (all conditions at one point). A **boundary value problem** can have none or infinitely many solutions: $y'' + y = 0$, $y(0) = 0$, $y(\pi) = 0$ is solved by $c\sin x$ for every $c$.
:::

:::exam-tip
The number of arbitrary constants in the general solution equals the order $n$. An answer with the wrong number of independent constants is wrong at sight.
:::

## The Wronskian and linear independence {#wronskian}

Functions $y_1, \dots, y_n$ are **linearly dependent** on $I$ if $c_1y_1 + \cdots + c_ny_n \equiv 0$ on $I$ for some constants not all zero; otherwise they are **independent**. The **Wronskian** of $n$ functions that are $(n-1)$ times differentiable is

$$W(y_1, \dots, y_n) = \begin{vmatrix} y_1 & y_2 & \cdots & y_n \\ y_1' & y_2' & \cdots & y_n' \\ \vdots & & & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \cdots & y_n^{(n-1)} \end{vmatrix}.$$

For two functions, $W(y_1, y_2) = y_1y_2' - y_2y_1'$. Examples:

- $W(e^{ax}, e^{bx}) = (b - a)e^{(a + b)x}$, nonzero when $a \ne b$.
- $W(\cos\beta x, \sin\beta x) = \beta$; $W(e^{ax}, xe^{ax}) = e^{2ax}$; $W(1, x, x^2) = 2$.

| Statement | True for |
|:---|:---|
| $W(x_0) \ne 0$ at one point $\Rightarrow$ independent on $I$ | **any** differentiable functions |
| $W \equiv 0$ on $I$ $\Rightarrow$ dependent | **false** in general; true for solutions of one linear equation |
| $W$ is either $\equiv 0$ or never $0$ on $I$ | solutions of one linear equation (continuous coefficients, $a_0 \ne 0$) |

**Abel's formula.** If $y_1, y_2$ solve $y'' + P(x)y' + Q(x)y = 0$ with $P, Q$ continuous on $I$, then

$$W(x) = W(x_0)\exp\left(-\int_{x_0}^{x}P(t)\,dt\right).$$

**Proof idea.** $W' = y_1y_2'' - y_2y_1'' = -PW$, a first-order linear equation for $W$. Since the exponential never vanishes, $W$ is either identically zero or never zero. This gives the dichotomy in the table.

Example: for $y'' + 2y' + 5y = 0$ with $W(0) = 3$, we have $W(x) = 3e^{-2x}$.

:::caution
$y_1 = x^2$ and $y_2 = x\lvert x\rvert$ on $(-1, 1)$: $W \equiv 0$, yet they are independent ($y_2 = y_1$ for $x > 0$ and $y_2 = -y_1$ for $x < 0$, so no single constant works). This does not contradict Abel's formula: they do not solve a common equation $y'' + Py' + Qy = 0$ with continuous $P, Q$ on $(-1, 1)$.
:::

**Reduction of order** (one line): if $y_1$ is known, putting $y = vy_1$ gives a first-order equation for $v'$. This is how $xe^{ax}$ arises from a repeated root, and $x\ln x$ in a Cauchy–Euler equation.

## Homogeneous equations with constant coefficients {#constant-coefficients}

Write $D = \frac{d}{dx}$. The equation $(a_0D^n + a_1D^{n-1} + \cdots + a_n)y = 0$, with real constants $a_i$, is $f(D)y = 0$. Trying $y = e^{mx}$ gives $f(m)e^{mx} = 0$, so $m$ must be a root of the **auxiliary (characteristic) equation** $f(m) = 0$.

| Roots of $f(m) = 0$ | Contribution to the CF |
|:---|:---|
| real, distinct $m_1, m_2$ | $c_1e^{m_1x} + c_2e^{m_2x}$ |
| real $m$, repeated $k$ times | $(c_1 + c_2x + \cdots + c_kx^{k-1})e^{mx}$ |
| complex pair $\alpha \pm i\beta$ | $e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$ |
| complex pair $\alpha \pm i\beta$, repeated twice | $e^{\alpha x}\left[(c_1 + c_2x)\cos\beta x + (c_3 + c_4x)\sin\beta x\right]$ |

Because the $a_i$ are real, complex roots come in conjugate pairs. Euler's formula $e^{(\alpha + i\beta)x} = e^{\alpha x}(\cos\beta x + i\sin\beta x)$ turns each pair into two real solutions.

**Examples.**

- $y'' - 5y' + 6y = 0$: $m = 2, 3$, so $y = c_1e^{2x} + c_2e^{3x}$.
- $y'' - 6y' + 9y = 0$: $m = 3, 3$, so $y = (c_1 + c_2x)e^{3x}$.
- $y'' - 2y' + 5y = 0$: $m = 1 \pm 2i$, so $y = e^{x}(c_1\cos 2x + c_2\sin 2x)$.
- $y''' - y = 0$: $m^3 = 1$ gives $m = 1, -\frac12 \pm \frac{\sqrt3}{2}i$, so
  $$y = c_1e^{x} + e^{-x/2}\left(c_2\cos\tfrac{\sqrt3}{2}x + c_3\sin\tfrac{\sqrt3}{2}x\right).$$

**Working backwards.** If the solution is $e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$, the roots are $\alpha \pm i\beta$. The equation is then $y'' - 2\alpha y' + (\alpha^2 + \beta^2)y = 0$. The lowest-order real equation with $xe^{x}$ and $\sin x$ among its solutions is $(D - 1)^2(D^2 + 1)y = 0$, of order 4.

**Behaviour as $x \to \infty$.** Every solution tends to $0$ exactly when every root has a negative real part. Example: $y'' + 3y' + 2y = 0$ has roots $-1, -2$, so every solution tends to $0$.

```plot
title: Damped oscillation $e^{-x/4}\cos 2x$ (roots $-\tfrac14 \pm 2i$) and the resonant PI $\tfrac{x}{4}\sin 2x$
x: 0, 4pi
y: -3.5, 3.5
f: exp(-x/4)cos(2x) | $e^{-x/4}\cos 2x$
f: x sin(2x)/4 | $\frac{x}{4}\sin 2x$
f: x/4 | envelope $\pm x/4$
f: -x/4
```

:::exam-tip
A repeated root needs the extra factor $x$. Writing $c_1e^{3x} + c_2e^{3x}$ gives only one independent constant, so it is not the general solution.
:::

## The D-operator and particular integrals {#d-operator}

$\frac{1}{f(D)}R$ means a function $y$ with $f(D)y = R$ (any one PI). The basic inverse is

$$\frac{1}{D - a}R = e^{ax}\int e^{-ax}R\,dx, \qquad \frac{1}{D}R = \int R\,dx.$$

Factorising $f(D)$ or using partial fractions reduces every case to this. The rules below are shortcuts.

| Right side $R$ | Rule | Failure case |
|:---|:---|:---|
| $e^{ax}$ | $\dfrac{e^{ax}}{f(a)}$, if $f(a) \ne 0$ | $f(a) = 0$: $x\dfrac{e^{ax}}{f'(a)}$; if $a$ is a root of order $k$, $\dfrac{x^k e^{ax}}{f^{(k)}(a)}$ |
| $\sin ax$, $\cos ax$ | write $f(D) = \phi(D^2)$: $\dfrac{\sin ax}{\phi(-a^2)}$ | $\dfrac{1}{D^2 + a^2}\sin ax = -\dfrac{x\cos ax}{2a}$, $\;\dfrac{1}{D^2 + a^2}\cos ax = \dfrac{x\sin ax}{2a}$ |
| $x^m$ | expand $[f(D)]^{-1}$ in ascending powers of $D$ up to $D^m$ | none |
| $e^{ax}V$ | $e^{ax}\dfrac{1}{f(D + a)}V$ (exponential shift) | none |
| $xV$ | $x\dfrac{1}{f(D)}V - \dfrac{f'(D)}{[f(D)]^2}V$ | none |

If $f(D)$ has odd powers of $D$ and $R = \sin ax$, put $D^2 = -a^2$, then rationalise: multiply the top and bottom by the conjugate linear factor in $D$.

**Examples.**

- $(D^2 + 3D + 2)y = e^{3x}$: $y_p = \frac{e^{3x}}{9 + 9 + 2} = \frac{e^{3x}}{20}$.
- $(D^2 - 3D + 2)y = e^{x}$: $f(1) = 0$ and $f'(1) = -1$, so $y_p = -xe^{x}$.
- $(D^2 + 4)y = \sin x$: $y_p = \frac{\sin x}{-1 + 4} = \frac{\sin x}{3}$.
- $(D^2 - 4)y = x^2$:
  $$y_p = -\frac14\left(1 - \frac{D^2}{4}\right)^{-1}x^2 = -\frac14\left(1 + \frac{D^2}{4}\right)x^2 = -\frac{x^2}{4} - \frac18.$$
- $(D - 1)^2y = xe^{x}$: shift gives $e^{x}\frac{1}{D^2}x = \frac{x^3e^{x}}{6}$.
- $(D^2 - 2D + 5)y = e^{x}\cos 2x$: shift gives $e^{x}\frac{1}{(D + 1)^2 - 2(D + 1) + 5}\cos 2x = e^{x}\frac{1}{D^2 + 4}\cos 2x = \frac{xe^{x}\sin 2x}{4}$.

:::caution
$\frac{1}{f(D)}e^{ax} = \frac{e^{ax}}{f(a)}$ is meaningless when $f(a) = 0$. This is exactly the case where $e^{ax}$ already lies in the CF (resonance), and the PI picks up a factor $x$.
:::

## The $xV$ rule and harder particular integrals {#d-operator-advanced}

**$xV$ rule.** Differentiating $f(D)(xu) = xf(D)u + f'(D)u$ and choosing $u = \frac{1}{f(D)}V$ gives

$$\frac{1}{f(D)}(xV) = x\frac{1}{f(D)}V - \frac{f'(D)}{[f(D)]^2}V.$$

**Easier route for $x\sin ax$ or $x\cos ax$:** write $x\sin ax = \operatorname{Im}(xe^{iax})$, shift the exponential, and expand in powers of $D$.

**Example.** $(D^2 + 1)y = x\sin x$. Take the imaginary part of

$$\frac{1}{D^2 + 1}xe^{ix} = e^{ix}\frac{1}{(D + i)^2 + 1}x = e^{ix}\frac{1}{2iD\left(1 + \frac{D}{2i}\right)}x.$$

Now $\frac{1}{2iD}\left(1 - \frac{D}{2i}\right)x = \frac{1}{2i}\left(\frac{x^2}{2} - \frac{x}{2i}\right) = -\frac{ix^2}{4} + \frac{x}{4}$. Multiply by $e^{ix} = \cos x + i\sin x$ and take the imaginary part:

$$y_p = -\frac{x^2\cos x}{4} + \frac{x\sin x}{4}.$$

**Right side a sum.** Find the PI of each term separately and add (superposition). Example:

$$(D^2 + 1)y = e^{2x} + \cos x \;\Rightarrow\; y_p = \frac{e^{2x}}{5} + \frac{x\sin x}{2}.$$

**Products like $e^{ax}\sin bx$.** Use the shift, then the $\sin$ rule with $D^2 \to -b^2$:

$$\frac{1}{D^2 + 1}e^{x}\sin x = e^{x}\frac{1}{D^2 + 2D + 2}\sin x = e^{x}\frac{1}{2D + 1}\sin x = e^{x}\frac{(2D - 1)\sin x}{4D^2 - 1} = \frac{e^{x}(\sin x - 2\cos x)}{5}.$$

**Initial value problems.** First write the full general solution (CF + PI), then impose the conditions. Do not impose them on the CF alone.

Example: $y'' + 4y = 4$, $y(0) = 0$, $y'(0) = 0$. The general solution is $y = c_1\cos 2x + c_2\sin 2x + 1$. The conditions give $c_1 = -1$ and $c_2 = 0$, so $y = 1 - \cos 2x$.

:::exam-tip
Check any PI by applying $f(D)$ to it. For $\frac{x\sin 2x}{4}$ and $D^2 + 4$: $D^2\left(\frac{x\sin 2x}{4}\right) = \cos 2x - x\sin 2x$, and adding $4 \cdot \frac{x\sin 2x}{4}$ leaves $\cos 2x$. This takes about 20 seconds.
:::

## Variation of parameters {#variation-of-parameters}

The D-operator shortcuts need $R$ to be built from $e^{ax}$, $\sin$, $\cos$ and polynomials. For a general $R$ (such as $\sec x$, $\tan x$ or $\frac{e^x}{x}$), use **variation of parameters** (Lagrange). It also works for variable coefficients once the CF is known.

For $y'' + P(x)y' + Q(x)y = R(x)$ with CF $c_1y_1 + c_2y_2$, try $y_p = u_1y_1 + u_2y_2$ and impose $u_1'y_1 + u_2'y_2 = 0$. Then

$$u_1' = -\frac{y_2R}{W}, \qquad u_2' = \frac{y_1R}{W}, \qquad W = W(y_1, y_2) \ne 0.$$

:::caution
The formulas need the equation in **normalised form**, with the coefficient of $y''$ equal to $1$. For $x^2y'' + \cdots = g(x)$, use $R = g(x)/x^2$.
:::

**Example.** $y'' + y = \sec x$ on $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Take $y_1 = \cos x$, $y_2 = \sin x$, so $W = 1$. Then

$$u_1' = -\sin x\sec x = -\tan x \Rightarrow u_1 = \ln\cos x, \qquad u_2' = \cos x\sec x = 1 \Rightarrow u_2 = x.$$

$$y_p = \cos x\,\ln\cos x + x\sin x.$$

**Example.** $y'' + y = \tan x$: $u_1' = -\frac{\sin^2 x}{\cos x}$ and $u_2' = \sin x$. This gives

$$y_p = -\cos x\,\ln\lvert\sec x + \tan x\rvert.$$

**Example.** $y'' - 2y' + y = \frac{e^{x}}{x}$ ($x > 0$): $y_1 = e^{x}$, $y_2 = xe^{x}$, $W = e^{2x}$. So $u_1' = -1$ and $u_2' = \frac1x$, giving

$$y_p = -xe^{x} + xe^{x}\ln x.$$

The $-xe^{x}$ part lies in the CF and may be dropped.

**For order $n$:** $u_k' = \frac{W_k R}{W}$, where $W_k$ is $W$ with its $k$th column replaced by $(0, \dots, 0, 1)^T$. This needs the leading coefficient to be $1$.

:::exam-tip
Sign check: in $u_1' = -\frac{y_2R}{W}$, the minus sign goes with $u_1$, the coefficient of $y_1$, and the numerator holds the **other** function $y_2$. Swapping these is the commonest slip.
:::

## Cauchy–Euler and Legendre equations {#cauchy-euler}

A **Cauchy–Euler** (homogeneous linear) equation has the form

$$x^n y^{(n)} + k_1 x^{n-1}y^{(n-1)} + \cdots + k_n y = R(x), \qquad k_i \text{ constants}.$$

On $x > 0$, put $x = e^{z}$ and $\theta = \frac{d}{dz}$. Then

$$xD = \theta, \qquad x^2D^2 = \theta(\theta - 1), \qquad x^3D^3 = \theta(\theta - 1)(\theta - 2),$$

and in general $x^kD^k = \theta(\theta - 1)\cdots(\theta - k + 1)$. The equation becomes one with constant coefficients in $z$, and the whole of the previous sections applies.

Equivalently, try $y = x^m$ in the homogeneous equation. For $x^2y'' + axy' + by = 0$ this gives the **indicial equation** $m(m - 1) + am + b = 0$.

| Roots of $m(m - 1) + am + b = 0$ | Solutions ($x > 0$) |
|:---|:---|
| real, distinct $m_1, m_2$ | $c_1x^{m_1} + c_2x^{m_2}$ |
| repeated $m$ | $(c_1 + c_2\ln x)x^{m}$ |
| $\alpha \pm i\beta$ | $x^{\alpha}\left[c_1\cos(\beta\ln x) + c_2\sin(\beta\ln x)\right]$ |

**Examples.**

- $x^2y'' - 2xy' + 2y = 0$: $m^2 - 3m + 2 = 0$, so $m = 1, 2$ and $y = c_1x + c_2x^2$.
- $x^2y'' + xy' + y = 0$: $m^2 + 1 = 0$, so $y = c_1\cos(\ln x) + c_2\sin(\ln x)$.
- $x^2y'' - xy' + y = \ln x$: the equation is $(\theta - 1)^2y = z$. The PI is
  $$(1 - \theta)^{-2}z = (1 + 2\theta + \cdots)z = z + 2.$$
  So $y = (c_1 + c_2\ln x)x + \ln x + 2$.

**Legendre's linear equation.** Terms $(a + bx)^k y^{(k)}$ are handled by $a + bx = e^{z}$, which gives $(a + bx)^kD^k = b^k\theta(\theta - 1)\cdots(\theta - k + 1)$. Example: $(1 + x)^2y'' + (1 + x)y' + y = 0$ becomes $(\theta^2 + 1)y = 0$, so

$$y = c_1\cos\ln(1 + x) + c_2\sin\ln(1 + x).$$

:::caution
$x^2D^2 \ne \theta^2$. Forgetting the $-\theta$ in $\theta(\theta - 1)$ changes the indicial equation. For $x^2y'' - 2xy' + 2y = 0$ it would give complex roots $1 \pm i$ instead of $1, 2$. Also, not every Cauchy–Euler equation has a real power solution $x^m$: $x^2y'' + xy' + y = 0$ has none.
:::

## Quick checks and traps {#exam-tips}

- **Count constants:** the order $n$ equals the number of independent arbitrary constants.
- **Substitute back.** Apply $f(D)$ to a proposed PI; a CF member gives $0$, never $R$.
- **Resonance:** if $e^{ax}$, $\sin ax$ or $\cos ax$ is in the CF, the PI has an extra factor $x$ (or $x^k$ for a root of multiplicity $k$).
- **$\sin$/$\cos$ signs:** $\frac{1}{D^2 + a^2}\sin ax = -\frac{x\cos ax}{2a}$ and $\frac{1}{D^2 + a^2}\cos ax = +\frac{x\sin ax}{2a}$.
- **Shift direction:** $\frac{1}{f(D)}e^{ax}V = e^{ax}\frac{1}{f(D + a)}V$, with $+a$, not $-a$.
- **Wronskian:** $W \ne 0$ somewhere means independent, for any functions. $W \equiv 0$ means dependent only for solutions of a common linear equation ($x^2$ and $x\lvert x\rvert$ show why).
- **Abel:** for $y'' + Py' + Qy = 0$, $W = Ce^{-\int P\,dx}$, read straight from the equation.
- **Variation of parameters:** normalise first; $W$ in the denominator; $u_1' = -y_2R/W$.
- **Cauchy–Euler:** $x^2D^2 = \theta(\theta - 1)$; solutions involve $\ln x$, and $\cos(\ln x)$ for complex roots.
- **Simultaneous linear equations** such as $\frac{dx}{dt} = ay + \cdots$, $\frac{dy}{dt} = bx + \cdots$ (one line): eliminate one variable with the D-operator to get a single higher-order equation.
