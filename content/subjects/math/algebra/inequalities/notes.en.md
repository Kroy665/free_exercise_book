# Inequalities

## Basic rules and tools {#basics}

Every inequality in this topic is about **real** numbers; $\C$ has no order. The working rules are those of an ordered field:

- $a > b \Rightarrow a + c > b + c$ for every real $c$.
- $a > b$ and $c > 0 \Rightarrow ac > bc$; but $c < 0 \Rightarrow ac < bc$ (the sign flips).
- $a > b > 0 \Rightarrow \dfrac1a < \dfrac1b$ and $a^n > b^n$ for $n \in \N$.
- $a > b,\ c > d \Rightarrow a + c > b + d$. You may add inequalities, but not subtract or divide them.

**The one source of all of them:** $x^2 \ge 0$, with equality only at $x = 0$. For example,

$$a^2 + b^2 - 2ab = (a - b)^2 \ge 0, \qquad a^2 + b^2 + c^2 - ab - bc - ca = \tfrac12\left[(a-b)^2 + (b-c)^2 + (c-a)^2\right] \ge 0.$$

So $a^2 + b^2 + c^2 \ge ab + bc + ca$ for **all** real $a, b, c$, with equality iff $a = b = c$. A useful consequence:

$$(a + b + c)^2 \ge 3(ab + bc + ca).$$

In the other direction, $(a + b + c)^2 \ge 0$ gives $ab + bc + ca \ge -\frac12(a^2 + b^2 + c^2)$. So if $a^2 + b^2 + c^2 = 1$, then $-\frac12 \le ab + bc + ca \le 1$.

**Monotone functions** also give inequalities. If $f$ is strictly increasing, then $a > b \iff f(a) > f(b)$. Examples are $e^x$, $\ln x$ on $(0, \infty)$, and $x^n$ on $[0, \infty)$.

The identity behind $a^3 + b^3 + c^3 \ge 3abc$:

$$a^3 + b^3 + c^3 - 3abc = (a + b + c)\cdot\tfrac12\left[(a-b)^2 + (b-c)^2 + (c-a)^2\right].$$

So the inequality holds whenever $a + b + c \ge 0$, in particular for positive $a, b, c$.

:::caution
Multiplying an inequality by an expression whose sign you do not know is the commonest error. For example, $x > \frac1x$ does **not** give $x^2 > 1$ when $x < 0$; the solution set is $(-1, 0) \cup (1, \infty)$.
:::

## AM ≥ GM ≥ HM {#am-gm-hm}

For **positive** reals $a_1, \dots, a_n$ define

$$A = \frac{a_1 + \cdots + a_n}{n}, \qquad G = (a_1 a_2 \cdots a_n)^{1/n}, \qquad H = \frac{n}{\frac{1}{a_1} + \cdots + \frac{1}{a_n}}.$$

:::keyfacts
- **Theorem.** $A \ge G \ge H$, and equality in either place holds **iff** $a_1 = a_2 = \cdots = a_n$.
- $G \ge H$ is just $A \ge G$ applied to $\frac{1}{a_1}, \dots, \frac{1}{a_n}$.
- For **two** numbers: $G^2 = AH$, so $G$ is the geometric mean of $A$ and $H$.
- $\min a_i \le H \le G \le A \le \max a_i$.
:::

**Proof ideas.**

- **$n = 2$:** $\frac{a + b}{2} - \sqrt{ab} = \frac12\left(\sqrt a - \sqrt b\right)^2 \ge 0$.
- **Cauchy's forward–backward induction:** the case $n = 2$ gives $n = 4, 8, \dots, 2^k$. To go down from $n$ to $n - 1$, add the extra number $A$ itself.
- **Smoothing:** if two of the numbers differ, replace them by their mean. The sum is unchanged, but the product strictly increases.

**Example.** For the numbers $4$ and $9$: $A = \frac{13}{2}$ and $G = 6$, so $H = \frac{G^2}{A} = \frac{72}{13}$.

**Example.** For positive $a, b, c$:

$$(a + b)(b + c)(c + a) \ge 2\sqrt{ab}\cdot 2\sqrt{bc}\cdot 2\sqrt{ca} = 8abc.$$

Equality holds iff $a = b = c$.

**Example.** For $a, b, c > 0$ with $abc = 1$: $(1 + a)(1 + b)(1 + c) \ge 8\sqrt{abc} = 8$.

:::caution
AM ≥ GM needs **non-negative** numbers. For $a = -1$, $b = -4$: $A = -2.5$, but $\sqrt{ab} = 2$. Likewise, for $x < 0$, $x + \frac1x \le -2$, not $\ge 2$.
:::

:::exam-tip
The equality condition "all equal" tells you **where** an extremum occurs. Most one-minute questions are solved by putting all the terms equal and checking that the product (or the sum) is constant.
:::

## Weighted means {#weighted}

Let $a_1, \dots, a_n > 0$ and let the weights $w_1, \dots, w_n$ be positive, with $W = \sum w_i$.

:::keyfacts
- **Weighted AM ≥ GM ≥ HM:**
  $$\frac{w_1 a_1 + \cdots + w_n a_n}{W} \ \ge\ \left(a_1^{w_1} \cdots a_n^{w_n}\right)^{1/W} \ \ge\ \frac{W}{\frac{w_1}{a_1} + \cdots + \frac{w_n}{a_n}}.$$
- Equality holds iff $a_1 = \cdots = a_n$.
- For positive **integer** weights, this is the ordinary AM ≥ GM with $a_i$ repeated $w_i$ times.
:::

**Young's inequality** is the two-term case with weights $\frac1p, \frac1q$, where $\frac1p + \frac1q = 1$ and $p, q > 1$:

$$xy \le \frac{x^p}{p} + \frac{y^q}{q} \qquad (x, y \ge 0).$$

**Using weights for a maximum.** To maximise $x^m y^n$ when $x + y = s$ (with $x, y > 0$), split $x$ into $m$ equal parts $\frac{x}{m}$ and $y$ into $n$ equal parts $\frac{y}{n}$. These $m + n$ numbers have the fixed sum $s$, so

$$\left(\frac{x}{m}\right)^m\left(\frac{y}{n}\right)^n \le \left(\frac{s}{m + n}\right)^{m + n}.$$

Equality holds when $\frac{x}{m} = \frac{y}{n}$, that is, when $x : y = m : n$.

**Example.** If $x + y = 5$, the maximum of $x^3y^2$ is at $x = 3$, $y = 2$. Its value is $27 \cdot 4 = 108$.

**Example.** If $x + y = 3$, then $x^2y$ is largest at $x = 2$, $y = 1$, where it equals $4$. Putting $x = y = \frac32$ gives only $\frac{27}{8}$.

:::caution
Splitting into equal parts must keep the **sum constant**. With $x + y = 3$, the three numbers $\frac x2, \frac x2, y$ have the sum $3$, which is constant. The three numbers $x, x, y$ do not: their sum is $2x + y$, which varies, so AM ≥ GM gives no fixed bound for them.
:::

## Power means {#power-means}

For positive $a_1, \dots, a_n$ and real $p \ne 0$, the **power mean of order $p$** is

$$M_p = \left(\frac{a_1^p + \cdots + a_n^p}{n}\right)^{1/p}, \qquad M_0 = G \ \text{(the limit as } p \to 0).$$

So $M_{-1} = H$, $M_0 = G$, $M_1 = A$ and $M_2 = \sqrt{\frac{\sum a_i^2}{n}}$ (the root mean square).

:::keyfacts
- **Power mean inequality.** $M_p$ is an increasing function of $p$: if $p < q$ then $M_p \le M_q$. Equality holds iff all the $a_i$ are equal.
- Chain: $\min a_i \le H \le G \le A \le M_2 \le \max a_i$.
- **The $m$th power theorem.** For positive $a_i$, not all equal:
  $$\frac{a_1^m + \cdots + a_n^m}{n} \;>\; \left(\frac{a_1 + \cdots + a_n}{n}\right)^m \quad \text{if } m < 0 \text{ or } m > 1,$$
  and the inequality is **reversed** if $0 < m < 1$. Both sides are equal if $m = 0$ or $m = 1$.
:::

**Proof idea.** $t \mapsto t^m$ is convex on $(0, \infty)$ when $m < 0$ or $m > 1$, and concave when $0 < m < 1$. Jensen's inequality then gives the result. For $m = 2$ it is just the fact that the variance is non-negative: $\frac{\sum a_i^2}{n} - A^2 = \frac{\sum (a_i - A)^2}{n} \ge 0$.

| $m$ | $\frac{1}{n}\sum a_i^m$ vs $A^m$ |
|:---|:---|
| $m > 1$ | $\ge$ (e.g. $m = 2, 3$) |
| $0 < m < 1$ | $\le$ (e.g. $m = \frac12$) |
| $m < 0$ | $\ge$ (e.g. $m = -1$: this gives $A \ge H$) |

**Example.** If $a, b > 0$ and $a + b = 2$, then $\frac{a^4 + b^4}{2} \ge \left(\frac{a + b}{2}\right)^4 = 1$. So $a^4 + b^4 \ge 2$, with equality at $a = b = 1$.

**Example.** $\frac{a^3 + b^3}{2} \ge \left(\frac{a + b}{2}\right)^3$, so $a^3 + b^3 \ge \frac{(a + b)^3}{4}$ for $a, b > 0$.

:::exam-tip
The direction of the $m$th power theorem follows from one test case. Put $a = 0$ and $b = 2$ (by continuity): the left side is $2^{m-1}$ and the right side is $1$. So the left side is bigger iff $m > 1$, for $m > 0$.
:::

## Cauchy–Schwarz inequality {#cauchy-schwarz}

:::keyfacts
- **Cauchy–Schwarz (Cauchy's inequality).** For real $a_1, \dots, a_n$ and $b_1, \dots, b_n$:
  $$\left(a_1 b_1 + \cdots + a_n b_n\right)^2 \le \left(a_1^2 + \cdots + a_n^2\right)\left(b_1^2 + \cdots + b_n^2\right).$$
- **Equality** holds iff the two $n$-tuples are proportional: $a_i = \lambda b_i$ for all $i$ (or every $b_i = 0$).
- No sign condition is needed.
:::

**Proof idea (examinable).** For every real $x$,

$$\sum (a_i x + b_i)^2 = \Big(\sum a_i^2\Big)x^2 + 2\Big(\sum a_i b_i\Big)x + \sum b_i^2 \ge 0.$$

A quadratic that is never negative has discriminant $\le 0$, and that is exactly the inequality. Equality means the quadratic has a real root $x_0$. Then $a_i x_0 + b_i = 0$ for every $i$, so the tuples are proportional. (The form for vectors in an inner product space, $|\langle u, v\rangle| \le \lVert u\rVert\,\lVert v\rVert$, belongs to linear algebra.)

**Engel form (Titu's lemma).** For real $x_i$ and **positive** $y_i$:

$$\frac{x_1^2}{y_1} + \cdots + \frac{x_n^2}{y_n} \ \ge\ \frac{(x_1 + \cdots + x_n)^2}{y_1 + \cdots + y_n},$$

with equality iff $\frac{x_1}{y_1} = \cdots = \frac{x_n}{y_n}$. Apply Cauchy–Schwarz to $\frac{x_i}{\sqrt{y_i}}$ and $\sqrt{y_i}$.

**Linear function on a sphere.** If $x^2 + y^2 = 1$, then $(3x + 4y)^2 \le (9 + 16)(x^2 + y^2) = 25$. So $-5 \le 3x + 4y \le 5$, with the maximum at $(x, y) = \left(\frac35, \frac45\right)$.

**Least squares on a plane.** If $x + 2y + 2z = 9$, then $81 \le (1 + 4 + 4)(x^2 + y^2 + z^2)$. So $x^2 + y^2 + z^2 \ge 9$, with equality at $(1, 2, 2)$. This is the squared distance from the origin to the plane.

**Example.** If $x, y > 0$ and $x + y = 1$, then by Engel's form

$$\frac1x + \frac4y = \frac{1^2}{x} + \frac{2^2}{y} \ge \frac{(1 + 2)^2}{x + y} = 9,$$

with equality at $x = \frac13$, $y = \frac23$.

:::caution
Engel's form needs **positive** denominators. With $x = (1, 1)$ and $y = \left(1, -\frac12\right)$, the left side is $-1$ and the right side is $8$.
:::

## Maxima and minima under constraints {#extrema}

Two principles cover most one-minute questions. Both need **positive** variables.

:::keyfacts
- **Fixed product → least sum.** If $xy = k$, then $x + y \ge 2\sqrt k$, with the least value at $x = y$.
- **Fixed sum → greatest product.** If $x + y = s$, then $xy \le \frac{s^2}{4}$, with the greatest value at $x = y = \frac s2$. The same holds for $n$ variables: if $\sum x_i = s$, then $\prod x_i \le \left(\frac{s}{n}\right)^n$.
- $x + \frac1x \ge 2$ for $x > 0$, with equality only at $x = 1$.
- $ax + \frac{b}{x} \ge 2\sqrt{ab}$ for $a, b, x > 0$, with equality at $x = \sqrt{b/a}$.
:::

```plot
title: $y = x + \frac{1}{x}$ for $x > 0$: least value $2$ at $x = 1$
x: 0.2, 5
y: 0, 6
f: x + 1/x | $y = x + 1/x$
hline: 2
point: 1, 2 | $(1, 2)$
```

**Examples** ($x > 0$ unless stated otherwise):

| Expression | Least value | Attained at |
|:---|:---|:---|
| $x + \frac{4}{x}$ | $4$ | $x = 2$ |
| $4x + \frac{9}{x}$ | $12$ | $x = \frac32$ |
| $x^2 + \frac{2}{x} = x^2 + \frac1x + \frac1x$ | $3$ | $x = 1$ |
| $2x + 3y$, given $xy = 6$ | $12$ | $x = 3,\ y = 2$ |
| $9\tan^2\theta + 4\cot^2\theta$ | $12$ | $\tan^2\theta = \frac23$ |

**Three variables.**

- If $a + b + c = 1$, then $abc \le \frac{1}{27}$, and $ab + bc + ca \le \frac{(a + b + c)^2}{3} = \frac13$.
- If $xy + yz + zx = 12$, then AM ≥ GM on the three products gives $(xyz)^{2/3} \le 4$. So $xyz \le 8$, with equality at $x = y = z = 2$.

**A harder classic.** Let $x, y > 0$ with $x + y = 1$. Then $u^2 + v^2 \ge \frac{(u + v)^2}{2}$ gives

$$\Big(x + \frac1x\Big)^2 + \Big(y + \frac1y\Big)^2 \ge \frac12\Big(1 + \frac1x + \frac1y\Big)^2 \ge \frac12(1 + 4)^2 = \frac{25}{2}.$$

Here $\frac1x + \frac1y \ge \frac{4}{x + y} = 4$, and equality holds at $x = y = \frac12$.

:::caution
The bound is a minimum **only if equality can actually occur**. For $x \ge 3$, AM ≥ GM gives $x + \frac1x \ge 2$, but the least value is $3 + \frac13 = \frac{10}{3}$, because $x = 1$ is not allowed. The function is increasing on $[1, \infty)$.
:::

## Standard bounds and Weierstrass-type inequalities {#standard-bounds}

**Sum times sum of reciprocals.** For positive $a_1, \dots, a_n$:

$$(a_1 + \cdots + a_n)\left(\frac{1}{a_1} + \cdots + \frac{1}{a_n}\right) \ge n^2.$$

This is $A \ge H$ (or Cauchy–Schwarz with $\sqrt{a_i}$ and $\frac{1}{\sqrt{a_i}}$). So $(a + b)\left(\frac1a + \frac1b\right) \ge 4$ and $(a + b + c)\left(\frac1a + \frac1b + \frac1c\right) \ge 9$.

**A factorial bound.** Apply AM ≥ GM to $1, 2, \dots, n$:

$$\sqrt[n]{n!} \le \frac{1 + 2 + \cdots + n}{n} = \frac{n + 1}{2}, \qquad \text{so} \qquad n! < \left(\frac{n + 1}{2}\right)^n \text{ for } n \ge 2.$$

The inequality is strict because the numbers $1, \dots, n$ are not all equal. For $n = 1$ both sides equal $1$. A similar bound: $(n!)^2 \ge n^n$, since $k(n + 1 - k) \ge n$ for $1 \le k \le n$.

**Other bounds from the same tools.** If $a, b, c > 0$ and $a + b + c = 1$, then

$$\left(\frac1a - 1\right)\left(\frac1b - 1\right)\left(\frac1c - 1\right) = \frac{(b + c)(c + a)(a + b)}{abc} \ge 8.$$

**Weierstrass's inequalities.** Let $n \ge 2$.

:::keyfacts
- If $a_1, \dots, a_n > 0$, then $(1 + a_1)(1 + a_2)\cdots(1 + a_n) > 1 + (a_1 + \cdots + a_n)$.
- If $0 < a_i < 1$, then $(1 - a_1)(1 - a_2)\cdots(1 - a_n) > 1 - (a_1 + \cdots + a_n)$.
- If, in addition, $s = a_1 + \cdots + a_n < 1$, then
  $$\prod (1 + a_i) < \frac{1}{1 - s}, \qquad \prod (1 - a_i) < \frac{1}{1 + s}.$$
:::

**Proof idea.** Use induction. For example, $(1 - a)(1 - b) = 1 - a - b + ab > 1 - a - b$. Multiply by the next factor $(1 - c) > 0$ and repeat. With all $a_i = x$, the first inequality becomes **Bernoulli's inequality**: $(1 + x)^n > 1 + nx$ for $x > -1$, $x \ne 0$, $n \ge 2$.

:::exam-tip
To test a claimed bound quickly, try the equality case ($a = b = c$) and one lopsided case (one variable tiny). A wrong constant (for example $81abc$ instead of $27abc$ in $(a + b + c)^3 \ge 27abc$) fails at once at $a = b = c = 1$.
:::

## Quick checks and traps {#exam-tips}

- **Sign first.** AM ≥ GM ≥ HM and Engel's form need positive numbers. Cauchy–Schwarz holds for all real numbers.
- **Equality conditions:** "all equal" for the means; "proportional" for Cauchy–Schwarz; $\frac{x_i}{y_i}$ constant for Engel's form.
- **Two numbers:** $G^2 = AH$. If $A = 6.5$ and $G = 6$, then $H = \frac{72}{13}$.
- **Fixed sum, product $x^m y^n$:** the maximum is at $x : y = m : n$.
- **Linear form on a sphere:** the maximum of $\sum c_i x_i$ on $\sum x_i^2 = r^2$ is $r\sqrt{\sum c_i^2}$.
- **Bound vs extremum:** a bound from AM ≥ GM is the minimum only if the equality case is allowed by the constraints.
- **$m$th power theorem:** "$>$" for $m > 1$ or $m < 0$; "$<$" for $0 < m < 1$.
- **$n! < \left(\frac{n + 1}{2}\right)^n$** holds for $n \ge 2$; at $n = 1$ the two sides are equal.
- **With $a^2 + b^2 + c^2 = 1$:** $-\frac12 \le ab + bc + ca \le 1$.
