---
title: 'Euclids Division Lemma'
weight: 1
---
## 2.2 Euclid's Division Lemma

Euclid, one of the most important mathematicians wrote an important book named "Elements" in 13 volumes. The first six volumes were devoted to Geometry and for this reason, Euclid is called the "Father of Geometry". But in the next few volumes, he made fundamental contributions to understand the properties of numbers. One among them is the "Euclid's Divison Lemma". This is a simplified version of the long division process that you were performing for division of numbers in earlier classes.

Let us now discuss Euclid's Lemma and its application through an Algorithm termed as "Euclid's Division Algorithm".

&gt; **Lemma** is an auxiliary result used for proving an important theorem. It is usually considered as a mini theorem.

### Theorem 1: Euclid's Division Lemma

Let {{< katex  >}}a{{</ katex  >}} 
and {{< katex  >}}b{{</ katex  >}} 
be any two positive integers. Then, there exist unique integers {{< katex  >}}q{{</ katex  >}} 
and {{< katex  >}}r{{</ katex  >}} such that:
{{< katex  >}}a = bq + r, \quad 0 \leq r &lt; b{{</ katex  >}}

The remainder is always less than the divisor. If {{< katex  >}}r = 0{{</ katex  >}} 
then {{< katex  >}}a{{</ katex  >}} 
is divisible by {{< katex  >}}b{{</ katex  >}}.
Conversely, if {{< katex  >}}b{{</ katex  >}} 
divides {{< katex  >}}a{{</ katex  >}} 
then {{< katex  >}}a = bq{{</ katex  >}}.

---

### Example 2.1

We have 34 cakes. Each box can hold 5 cakes only. How many boxes we need to pack and how many cakes are unpacked?

**Solution:** We see that 6 boxes are required to pack 30 cakes with 4 cakes left over. This distribution of cakes can be understood as follows:

| 34 | = | 5 | × | 6 | + | 4 |
|:---|:---|:---|:---|:---|:---|:---|
| Total number of cakes | | Number of cakes in each box | × | Number of boxes | + | Number of cakes leftover |
| ↓ | | ↓ | | ↓ | | ↓ |
| (Dividend) {{< katex  >}}a{{</ katex  >}} 
| | (Divisor) {{< katex  >}}b{{</ katex  >}} 
| × | (Quotient) {{< katex  >}}q{{</ katex  >}} 
| + | (Remainder) {{< katex  >}}r{{</ katex  >}} |

&gt; **Note**
&gt; - The above lemma is nothing but a restatement of the long division process, the integers {{< katex  >}}q{{</ katex  >}} 
and {{< katex  >}}r{{</ katex  >}} are called quotient and remainder respectively.
&gt; - When a positive integer is divided by 2 the remainder is either 0 or 1. So, any positive integer will be of the form {{< katex  >}}2k{{</ katex  >}}, 
{{< katex  >}}2k+1{{</ katex  >}} 
for some integer {{< katex  >}}k{{</ katex  >}}.

Euclid's Division Lemma can be generalised to any two integers.

### Generalised form of Euclid's division lemma

If {{< katex  >}}a{{</ katex  >}} 
and {{< katex  >}}b{{</ katex  >}} 
are any two integers then there exist unique integers {{< katex  >}}q{{</ katex  >}} 
and {{< katex  >}}r{{</ katex  >}} such that:
{{< katex  >}}a = bq + r \quad \text{where} \quad 0 \leq r &lt; |b|{{</ katex  >}}

### Example 2.2

Find the quotient and remainder when {{< katex  >}}a{{</ katex  >}} 
is divided by {{< katex  >}}b{{</ katex  >}} in the following cases:
- (i) {{< katex  >}}a = -12{{</ katex  >}}, 
{{< katex  >}}b = 5{{</ katex  >}}
- (ii) {{< katex  >}}a = 17{{</ katex  >}}, 
{{< katex  >}}b = -3{{</ katex  >}}
- (iii) {{< katex  >}}a = -19{{</ katex  >}}, 
{{< katex  >}}b = -4{{</ katex  >}}

**Solutions:**

**(i)** {{< katex  >}}a = -12{{</ katex  >}}, 
{{< katex  >}}b = 5{{</ katex  >}}

By Euclid's division lemma {{< katex  >}}a = bq + r{{</ katex  >}}, where 
{{< katex  >}}0 \leq r &lt; |b|{{</ katex  >}}

{{< katex  >}}-12 = 5 \times (-3) + 3, \quad 0 \leq r &lt; |5|{{</ katex  >}}

Therefore, Quotient {{< katex  >}}q = -3{{</ katex  >}}, 
Remainder {{< katex  >}}r = 3{{</ katex  >}}

**(ii)** {{< katex  >}}a = 17{{</ katex  >}}, 
{{< katex  >}}b = -3{{</ katex  >}}

By Euclid's division lemma {{< katex  >}}a = bq + r{{</ katex  >}}, where 
{{< katex  >}}0 \leq r &lt; |b|{{</ katex  >}}

{{< katex  >}}17 = (-3) \times (-5) + 2, \quad 0 \leq r &lt; |-3|{{</ katex  >}}

Therefore Quotient {{< katex  >}}q = -5{{</ katex  >}}, 
Remainder {{< katex  >}}r = 2{{</ katex  >}}

**(iii)** {{< katex  >}}a = -19{{</ katex  >}}, 
{{< katex  >}}b = -4{{</ katex  >}}

By Euclid's division lemma {{< katex  >}}a = bq + r{{</ katex  >}}, 
where {{< katex  >}}0 \leq r &lt; |b|{{</ katex  >}}

{{< katex  >}}-19 = (-4) \times (5) + 1, \quad 0 \leq r &lt; |-4|{{</ katex  >}}

Therefore Quotient {{< katex  >}}q = 5{{</ katex  >}}, 
Remainder {{< katex  >}}r = 1{{</ katex  >}}

---

![](thinking.png)
---

### Progress Check

Find {{< katex  >}}q{{</ katex  >}}
and {{< katex  >}}r{{</ katex  >}}
for the following pairs of integers {{< katex  >}}a{{</ katex  >}}
and {{< katex  >}}b{{</ katex  >}} 
satisfying {{< katex  >}}a = bq + r{{</ katex  >}}.

1. {{< katex  >}}a = 13{{</ katex  >}}, 
{{< katex  >}}b = 3{{</ katex  >}}
2. {{< katex  >}}a = 18{{</ katex  >}}, 
{{< katex  >}}b = 4{{</ katex  >}}
3. {{< katex  >}}a = 21{{</ katex  >}}, 
{{< katex  >}}b = -4{{</ katex  >}}
4. {{< katex  >}}a = -32{{</ katex  >}}, 
{{< katex  >}}b = -12{{</ katex  >}}
5. {{< katex  >}}a = -31{{</ katex  >}}, 
{{< katex  >}}b = 7{{</ katex  >}}

---

### Example 2.3

Show that the square of an odd integer is of the form {{< katex  >}}4q + 1{{</ katex  >}}, 
for some integer {{< katex  >}}q{{</ katex  >}}.

**Solution:** Let {{< katex  >}}x{{</ katex  >}} be any odd integer. Since any odd integer is one more than an even integer, we have:
{{< katex  >}}x = 2k + 1, \quad \text{for some integer } k{{</ katex  >}}

{{< katex  >}}{{</ katex  >}}\begin{aligned}
x^2 &= (2k + 1)^2 \\
&= 4k^2 + 4k + 1 \\
&= 4k(k + 1) + 1 \\
&= 4q + 1, \quad \text{where } q = k(k+1) \text{ is some integer.}
\end{aligned}{{< katex  >}}{{</ katex  >}}

---
