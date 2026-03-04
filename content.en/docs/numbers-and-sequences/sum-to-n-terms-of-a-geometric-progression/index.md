---
title: 'Sum to n terms of a Geometric Progression'
weight: 9
---

## 2.10 Sum to {{< katex >}}n{{< /katex >}} terms of a Geometric progression

A series whose terms are in Geometric progression is called **Geometric series**.

Let {{< katex >}}a, ar, ar^2, \ldots, ar^{n-1}, \ldots{{< /katex >}} be the Geometric Progression.

The sum of first {{< katex >}}n{{< /katex >}} terms of the Geometric progression is:
{{< katex >}}S_n = a + ar + ar^2 + \cdots + ar^{n-2} + ar^{n-1} \quad \ldots(1){{< /katex >}}

Multiplying both sides by {{< katex >}}r{{< /katex >}}, we get:
{{< katex >}}rS_n = ar + ar^2 + ar^3 + \cdots + ar^{n-1} + ar^n \quad \ldots(2){{< /katex >}}

{{< katex >}}(2) - (1) \Rightarrow rS_n - S_n = ar^n - a{{< /katex >}}
{{< katex >}}S_n(r-1) = a(r^n - 1){{< /katex >}}

Thus, the sum to {{< katex >}}n{{< /katex >}} terms is:
{{< katex >}}\boxed{S_n = \frac{a(r^n - 1)}{r-1}, \quad r \neq 1}{{< /katex >}}

> **Note**
> The above formula for sum of first {{< katex >}}n{{< /katex >}} 
terms of a G.P. is not applicable when {{< katex >}}r = 1{{< /katex >}}.
> If {{< katex >}}r = 1{{< /katex >}},
 then {{< katex >}}S_n = a + a + a + \cdots + a = na{{< /katex >}}

**Progress Check**
1. A series whose terms are in Geometric progression is called _______.
2. When {{< katex >}}r = 1{{< /katex >}},
 the formula for finding sum to {{< katex >}}n{{< /katex >}} terms of a G.P. is ______.
3. When {{< katex >}}r \neq 1{{< /katex >}},
 the formula for finding sum to {{< katex >}}n{{< /katex >}} terms of a G.P. is ______.

### 2.10.1 Sum to infinite terms of a G.P.

The sum of infinite terms of a G.P. is given by:
{{< katex >}}S_\infty = a + ar + ar^2 + ar^3 + \cdots = \frac{a}{1-r}, \quad -1 < r < 1{{< /katex >}}

**Example 2.46** Find the sum of 8 terms of the G.P. {{< katex >}}1, -3, 9, -27, \ldots{{< /katex >}}

**Solution:** Here, the first term {{< katex >}}a = 1{{< /katex >}},
 common ratio {{< katex >}}r = \frac{-3}{1} = -3 \neq 1{{< /katex >}}

Here, {{< katex >}}n = 8{{< /katex >}}.

Sum to {{< katex >}}n{{< /katex >}}
 terms of a G.P. is {{< katex >}}S_n = \frac{a(r^n - 1)}{r-1}{{< /katex >}} 
 if {{< katex >}}r \neq 1{{< /katex >}}

Hence, {{< katex >}}S_8 = \frac{1((-3)^8 - 1)}{(-3) - 1} = \frac{6561 - 1}{-4} = -1640{{< /katex >}}

**Example 2.47** Find the first term of a G.P. in which {{< katex >}}S_6 = 4095{{< /katex >}}
 and {{< katex >}}r = 4{{< /katex >}}.

**Solution:** Common ratio {{< katex >}}= 4 > 1{{< /katex >}},
 Sum of first 6 terms {{< katex >}}= 4095{{< /katex >}}

{{< katex >}}S_6 = \frac{a(r^n - 1)}{r-1} = 4095{{< /katex >}}

{{< katex >}}\because r = 4, \frac{a(4^6 - 1)}{4-1} = 4095 \implies a \times \frac{4095}{3} = 4095{{< /katex >}}

First term {{< katex >}}a = 3{{< /katex >}}

**Example 2.48** How many terms of the series {{< katex >}}1 + 4 + 16 + \cdots{{< /katex >}} make the sum 1365?

**Solution:** Let {{< katex >}}n{{< /katex >}} be the number of terms to be added to get the sum 1365

{{< katex >}}\begin{aligned}
a &= 1, \quad r = \frac{4}{1} = 4 > 1 \\
S_n &= 1365 \implies \frac{a(r^n - 1)}{r-1} = 1365 \\
\frac{1(4^n - 1)}{4-1} &= 1365 \implies (4^n - 1) = 4095 \\
4^n &= 4096 \implies 4^n = 4^6 \\
n &= 6
\end{aligned}{{< /katex >}}

**Example 2.49** Find the sum {{< katex >}}3 + 1 + \frac{1}{3} + \ldots \infty{{< /katex >}}

Here {{< katex >}}a = 3{{< /katex >}},
 {{< katex >}}r = \frac{t_2}{t_1} = \frac{1}{3}{{< /katex >}}

Sum of infinite terms:
{{< katex >}}S_\infty = \frac{a}{1-r} = \frac{3}{1-\frac{1}{3}} = \frac{9}{2}{{< /katex >}}

**Progress Check**
1. Sum to infinite number of terms of a G.P. is ___.
2. For what values of {{< katex >}}r{{< /katex >}}, does the formula for infinite G.P. valid?

**Example 2.50** Find the rational form of the number {{< katex >}}0.\overline{6}{{< /katex >}}

**Solution:** We can express the number {{< katex >}}0.\overline{6}{{< /katex >}} as follows:
{{< katex >}}0.\overline{6} = 0.6 + 0.06 + 0.006 + 0.0006 + \ldots{{< /katex >}}

We now see that numbers {{< katex >}}0.6, 0.06, 0.006, \ldots{{< /katex >}}
 form a G.P. whose first term {{< katex >}}a = 0.6{{< /katex >}} 
 and common ratio {{< katex >}}r = \frac{0.06}{0.6} = 0.1{{< /katex >}}.
  Also {{< katex >}}-1 < r = 0.1 < 1{{< /katex >}}

Using the infinite G.P. formula:
{{< katex >}}0.\overline{6} = 0.6 + 0.06 + 0.006 + 0.0006 + \cdots = \frac{0.6}{1-0.1} = \frac{0.6}{0.9} = \frac{2}{3}{{< /katex >}}

Thus the rational number equivalent of {{< katex >}}0.\overline{6}{{< /katex >}}
 is {{< katex >}}\frac{2}{3}{{< /katex >}}

---

## Exercise 2.8

1. Find the sum of first {{< katex >}}n{{< /katex >}} terms of the G.P.
   - (i) {{< katex >}}5, -3, \frac{9}{5}, -\frac{27}{25}, \cdots{{< /katex >}}
   - (ii) {{< katex >}}256, 64, 16, \ldots{{< /katex >}}

2. Find the sum of first six terms of the G.P. {{< katex >}}5, 15, 45, \ldots{{< /katex >}}

3. Find the first term of the G.P. whose common ratio 5 and whose sum to first 6 terms is 46872.

4. Find the sum to infinity of:
   - (i) {{< katex >}}9 + 3 + 1 + \cdots{{< /katex >}}
   - (ii) {{< katex >}}21 + 14 + \frac{28}{3} + \cdots{{< /katex >}}

5. If the first term of an infinite G.P. is 8 and its sum to infinity is {{< katex >}}\frac{32}{3}{{< /katex >}} then find the common ratio.

6. Find the sum to {{< katex >}}n{{< /katex >}} terms of the series:
   - (i) {{< katex >}}0.4 + 0.44 + 0.444 + \ldots{{< /katex >}}
    to {{< katex >}}n{{< /katex >}} terms
   - (ii) {{< katex >}}3 + 33 + 333 + \ldots{{< /katex >}}
    to {{< katex >}}n{{< /katex >}} terms

7. Find the sum of the Geometric series {{< katex >}}3 + 6 + 12 + \cdots + 1536{{< /katex >}}.

8. Kumar writes a letter to four of his friends. He asks each one of them to copy the letter and mail to four different persons with the instruction that they continue the process similarly. Assuming that the process is unaltered and it costs ₹2 to mail one letter, find the amount spent on postage when {{< katex >}}8^{\text{th}}{{< /katex >}} set of letters is mailed.

9. Find the rational form of the number {{< katex >}}0.\overline{123}{{< /katex >}}.

10. If {{< katex >}}S_n = (x-y) + (x^2+xy+y^2) + (x^3+x^2y+xy^2+y^3) + \cdots n{{< /katex >}} terms then prove that:
{{< katex >}}(x-y)S_n = \left|\frac{x^2(x^n-1)}{x-1} - \frac{y^2(y^n-1)}{y-1}\right|{{< /katex >}}

---