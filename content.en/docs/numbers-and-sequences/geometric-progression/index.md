---
title: 'Geometric Progression'
weight: 8
---
## 2.9 Geometric Progression

In the diagram given in Fig. 2.13, {{< katex >}}\triangle DEF{{< /katex >}}
 is formed by joining the mid points of the sides {{< katex >}}AB, BC{{< /katex >}}
  and {{< katex >}}CA{{< /katex >}}
   of {{< katex >}}\triangle ABC{{< /katex >}}. 
   Then the size of the triangle {{< katex >}}DEF{{< /katex >}} 
   is exactly one-fourth of the size of {{< katex >}}\triangle ABC{{< /katex >}}.
    Similarly {{< katex >}}\triangle GHI{{< /katex >}} 
    is also one-fourth of {{< katex >}}\triangle DEF{{< /katex >}} and so on. In general, the successive areas are one-fourth of the previous areas.

![](1.png)

The area of these triangles are:
{{< katex >}}\triangle ABC, \frac{1}{4}\triangle ABC, \frac{1}{4} \times \frac{1}{4}\triangle ABC, \ldots{{< /katex >}}

That is, {{< katex >}}\triangle ABC, \frac{1}{4}\triangle ABC, \frac{1}{16}\triangle ABC, \ldots{{< /katex >}}


![](3.png)


In this case, we see that beginning with {{< katex >}}\triangle ABC{{< /katex >}},
 we see that the successive triangles are formed whose areas are precisely one-fourth the area of the previous triangle. So, each term is obtained by multiplying {{< katex >}}\frac{1}{4}{{< /katex >}} to the previous term.

As another case, let us consider that a viral disease is spreading in a way such that at any stage two new persons get affected from an affected person. At first stage, one person is affected, at second stage two persons are affected and is spreading to four persons and so on. Then, number of persons affected at each stage are:
{{< katex >}}1, 2, 4, 8, \ldots{{< /katex >}}

Here each term is precisely twice the previous term.

From the above examples, it is clear that each term is got by multiplying a fixed number to the preceding number. This idea leads us to the concept of **Geometric Progression**.

### Definition

A **Geometric Progression** is a sequence in which each term is obtained by multiplying a fixed non-zero number to the preceding term except the first term. The fixed number is called **common ratio**. The common ratio is usually denoted by {{< katex >}}r{{< /katex >}}.

### 2.9.1 General form of Geometric Progression

Let {{< katex >}}a{{< /katex >}}
 and {{< katex >}}r \neq 0{{< /katex >}}
  be real numbers. Then the numbers of the form {{< katex >}}a, ar, ar^2, ar^3, \ldots, ar^{n-1}, \ldots{{< /katex >}} 
  is called a **Geometric Progression**. The number '{{< katex >}}a{{< /katex >}}'
   is called the **first term** and number '{{< katex >}}r{{< /katex >}}' is called the **common ratio**.

We note that beginning with first term {{< katex >}}a{{< /katex >}}, 
each term is obtained by multiplied with the common ratio {{< katex >}}r{{< /katex >}} 
to give {{< katex >}}ar, ar^2, ar^3, \ldots{{< /katex >}}

### 2.9.2 General term of Geometric Progression

We try to find a formula for {{< katex >}}n^{\text{th}}{{< /katex >}} term or general term of Geometric Progression (G.P.) whose terms are in the common ratio.

{{< katex >}}a, ar, ar^2, \ldots, ar^{n-1}, \ldots{{< /katex >}}

where {{< katex >}}a{{< /katex >}}
 is the first term and '{{< katex >}}r{{< /katex >}}'
  is the common ratio. Let {{< katex >}}t_n{{< /katex >}}
   be the {{< katex >}}n^{\text{th}}{{< /katex >}} term of the G.P.

Then:
{{< katex >}}\begin{aligned}
t_1 &= a = a \times r^0 = a \times r^{1-1} \\
t_2 &= t_1 \times r = a \times r = a \times r^{2-1} \\
t_3 &= t_2 \times r = ar \times r = ar^2 = ar^{3-1} \\
&\vdots \qquad \vdots \\
t_n &= t_{n-1} \times r = ar^{n-2} \times r = ar^{n-2+1} = ar^{n-1}
\end{aligned}{{< /katex >}}

Thus, the general term or {{< katex >}}n^{\text{th}}{{< /katex >}} term of a G.P. is:
{{< katex >}}\boxed{t_n = ar^{n-1}}{{< /katex >}}

If we consider the ratio of successive terms of the G.P. then we have:
{{< katex >}}\frac{t_2}{t_1} = \frac{ar}{a} = r, \quad \frac{t_3}{t_2} = \frac{ar^2}{ar} = r, \quad \frac{t_4}{t_3} = \frac{ar^3}{ar^2} = r, \ldots{{< /katex >}}

> **Note**
> Thus, the ratio between any two consecutive terms of the Geometric Progression is always constant and that constant is the common ratio of the given Progression.

**Progress Check**
1. A G.P. is obtained by multiplying _____ to the preceding term.
2. The ratio between any two consecutive terms of the G.P. is _____ and it is called _____.
3. Fill in the blanks if the following are in G.P.:
   - (i) {{< katex >}}\frac{1}{8}, \frac{3}{4}, \frac{9}{2}, \_\_\_\_\_{{< /katex >}}
   - (ii) {{< katex >}}\sqrt{7}, \_\_\_\_\_, \_\_\_\_\_{{< /katex >}}
   - (iii) {{< katex >}}\_\_\_\_\_, 2, 24, \ldots{{< /katex >}}

**Example 2.40** Which of the following sequences form a Geometric Progression?
- (i) {{< katex >}}7, 14, 21, 28, \ldots{{< /katex >}}
- (ii) {{< katex >}}\frac{1}{2}, 1, 2, 4, \ldots{{< /katex >}}
- (iii) {{< katex >}}5, 25, 50, 75, \ldots{{< /katex >}}

**Solution:** To check if a given sequence form a G.P. we have to see if the ratio between successive terms are equal.

**(i)** {{< katex >}}7, 14, 21, 28, \ldots{{< /katex >}}
{{< katex >}}\frac{t_2}{t_1} = \frac{14}{7} = 2; \quad \frac{t_3}{t_2} = \frac{21}{14} = \frac{3}{2}; \quad \frac{t_4}{t_3} = \frac{28}{21} = \frac{4}{3}{{< /katex >}}

Since the ratios between successive terms are not equal, the sequence {{< katex >}}7, 14, 21, 28, \ldots{{< /katex >}} is not a Geometric Progression.

**(ii)** {{< katex >}}\frac{1}{2}, 1, 2, 4, \ldots{{< /katex >}}

Here the ratios between successive terms are equal. Therefore the sequence {{< katex >}}\frac{1}{2}, 1, 2, 4, \ldots{{< /katex >}}
 is a Geometric Progression with common ratio {{< katex >}}r = 2{{< /katex >}}.

**(iii)** {{< katex >}}5, 25, 50, 75, \ldots{{< /katex >}}
{{< katex >}}\frac{t_2}{t_1} = \frac{25}{5} = 5; \quad \frac{t_3}{t_2} = \frac{50}{25} = 2; \quad \frac{t_4}{t_3} = \frac{75}{50} = \frac{3}{2}{{< /katex >}}

Since the ratios between successive terms are not equal, the sequence {{< katex >}}5, 25, 50, 75, \ldots{{< /katex >}} is not a Geometric Progression.

> **Thinking Corner**
> Is the sequence {{< katex >}}2, 2^2, 2^{2^2}, 2^{2^{2^2}}, \ldots{{< /katex >}} a G.P.?

**Example 2.41** Find the geometric progression whose first term and common ratios are given by:
- (i) {{< katex >}}a = -7, r = 6{{< /katex >}}
- (ii) {{< katex >}}a = 256, r = 0.5{{< /katex >}}

**Solution:**

**(i)** The general form of Geometric progression is {{< katex >}}a, ar, ar^2, \ldots{{< /katex >}}
{{< katex >}}a = -7, ar = -7 \times 6 = -42, \quad ar^2 = -7 \times 6^2 = -252{{< /katex >}}

Therefore the required Geometric Progression is {{< katex >}}-7, -42, -252, \ldots{{< /katex >}}

**(ii)** The general form of Geometric progression is {{< katex >}}a, ar, ar^2, \ldots{{< /katex >}}
{{< katex >}}a = 256, ar = 256 \times 0.5 = 128, \quad ar^2 = 256 \times (0.5)^2 = 64{{< /katex >}}

Therefore the required Geometric Progression is {{< katex >}}256, 128, 64, \ldots{{< /katex >}}

**Progress Check**
1. If first term {{< katex >}}= a{{< /katex >}},
 common ratio {{< katex >}}= r{{< /katex >}},
  then find the value of {{< katex >}}t_9{{< /katex >}}
   and {{< katex >}}t_{27}{{< /katex >}}
2. In a G.P. if {{< katex >}}t_1 = \frac{1}{5}{{< /katex >}}
 and {{< katex >}}t_2 = \frac{1}{25}{{< /katex >}} then the common ratio is ______.

**Example 2.42** Find the {{< katex >}}8^{\text{th}}{{< /katex >}}
 term of the G.P. {{< katex >}}9, 3, 1, \ldots{{< /katex >}}

**Solution:** To find the {{< katex >}}8^{\text{th}}{{< /katex >}}
 term we have to use the {{< katex >}}n^{\text{th}}{{< /katex >}} 
 term formula {{< katex >}}t_n = ar^{n-1}{{< /katex >}}

First term {{< katex >}}a = 9{{< /katex >}},
 Common ratio {{< katex >}}r = \frac{t_2}{t_1} = \frac{3}{9} = \frac{1}{3}{{< /katex >}}.

{{< katex >}}t_8 = 9 \times \left(\frac{1}{3}\right)^{8-1} = 9 \times \left(\frac{1}{3}\right)^7 = \frac{1}{243}{{< /katex >}}

Therefore the {{< katex >}}8^{\text{th}}{{< /katex >}} 
term of the G.P. is {{< katex >}}\frac{1}{243}{{< /katex >}}.

**Example 2.43** In a Geometric progression, the {{< katex >}}4^{\text{th}}{{< /katex >}} 
term is {{< katex >}}\frac{8}{9}{{< /katex >}}
 and the {{< katex >}}7^{\text{th}}{{< /katex >}}
  term is {{< katex >}}\frac{64}{243}{{< /katex >}}. Find the Geometric Progression.

**Solution:** {{< katex >}}4^{\text{th}}{{< /katex >}}
 term, {{< katex >}}t_4 = \frac{8}{9} \implies ar^3 = \frac{8}{9} \quad \ldots(1){{< /katex >}}

{{< katex >}}7^{\text{th}}{{< /katex >}} 
term, {{< katex >}}t_7 = \frac{64}{243} \implies ar^6 = \frac{64}{243} \quad \ldots(2){{< /katex >}}

Dividing (2) by (1) we get:
{{< katex >}}\frac{ar^6}{ar^3} = \frac{64/243}{8/9} \implies r^3 = \frac{8}{27} \implies r = \frac{2}{3}{{< /katex >}}

Substituting the value of {{< katex >}}r{{< /katex >}} in (1), we get:
{{< katex >}}a \times \left[\frac{2}{3}\right]^3 = \frac{8}{9} \implies a = 3{{< /katex >}}

Therefore the Geometric Progression is {{< katex >}}a, ar, ar^2, \ldots{{< /katex >}} 
That is, {{< katex >}}3, 2, \frac{4}{3}, \ldots{{< /katex >}}

> **Note**
> - When the product of three consecutive terms of a G.P. are given, we can take the three terms as {{< katex >}}\frac{a}{r}, a, ar{{< /katex >}}.
> - When the products of four consecutive terms are given for a G.P. then we can take the four terms as {{< katex >}}\frac{a}{r^3}, \frac{a}{r}, ar, ar^3{{< /katex >}}.
> - When each term of a Geometric Progression is multiplied or divided by a non–zero constant then the resulting sequence is also a Geometric Progression.

**Example 2.44** The product of three consecutive terms of a Geometric Progression is 343 and their sum is {{< katex >}}\frac{91}{3}{{< /katex >}}. Find the three terms.

**Solution:** Since the product of 3 consecutive terms is given, we can take them as {{< katex >}}\frac{a}{r}, a, ar{{< /katex >}}.

Product of the terms {{< katex >}}= 343{{< /katex >}}:
{{< katex >}}\frac{a}{r} \times a \times ar = 343 \implies a^3 = 7^3 \implies a = 7{{< /katex >}}

Sum of the terms {{< katex >}}= \frac{91}{3}{{< /katex >}}:
{{< katex >}}\frac{a}{r} + a + ar = \frac{91}{3} \implies 7\left(\frac{1}{r} + 1 + r\right) = \frac{91}{3}{{< /katex >}}
{{< katex >}}\frac{1 + r + r^2}{r} = \frac{13}{3} \implies 3r^2 - 10r + 3 = 0{{< /katex >}}
{{< katex >}}(3r - 1)(r - 3) = 0 \implies r = 3 \quad \text{or} \quad r = \frac{1}{3}{{< /katex >}}

If {{< katex >}}a = 7, r = 3{{< /katex >}}
 then the three terms are {{< katex >}}\frac{7}{3}, 7, 21{{< /katex >}}.

If {{< katex >}}a = 7, r = \frac{1}{3}{{< /katex >}} 
then the three terms are {{< katex >}}21, 7, \frac{7}{3}{{< /katex >}}.

**Progress Check**
Three non-zero numbers {{< katex >}}a, b, c{{< /katex >}} are in G.P. if and only if _____.

### Condition for three numbers to be in G.P.

If {{< katex >}}a, b, c{{< /katex >}} 
are in G.P. then {{< katex >}}b = ar{{< /katex >}}, 
{{< katex >}}c = ar^2{{< /katex >}}. So:
{{< katex >}}ac = a \times ar^2 = (ar)^2 = b^2{{< /katex >}}

Thus, {{< katex >}}b^2 = ac{{< /katex >}}

Similarly, if {{< katex >}}b^2 = ac{{< /katex >}}, 
then {{< katex >}}\frac{b}{a} = \frac{c}{b}{{< /katex >}}.
 So {{< katex >}}a, b, c{{< /katex >}} are in G.P.

Thus three non-zero numbers {{< katex >}}a, b, c{{< /katex >}} 
are in G.P. if and only if {{< katex >}}\boxed{b^2 = ac}{{< /katex >}}

**Example 2.45** The present value of a machine is ₹40,000 and its value depreciates each year by 10%. Find the estimated value of the machine in the 6th year.

**Solution:** The value of the machine at present is ₹40,000. Since it is depreciated at the rate of 10% after one year the value of the machine is 90% of the initial value.

That is the value of the machine at the end of the first year is {{< katex >}}40000 \times \frac{90}{100}{{< /katex >}},

After two years, the value of the machine is 90% of the value in the first year.

Value of the machine at the end of the {{< katex >}}2^{\text{nd}}{{< /katex >}}
 year is {{< katex >}}40,000 \times \left(\frac{90}{100}\right)^2{{< /katex >}},

Continuing this way, the value of the machine depreciates in the following way as:
{{< katex >}}40000, 40000 \times \frac{90}{100}, 40000 \times \left(\frac{90}{100}\right)^2, \ldots{{< /katex >}}

This sequence is in the form of G.P. with first term 40,000 and common ratio {{< katex >}}\frac{90}{100}{{< /katex >}}.

For finding the value of the machine at the end of {{< katex >}}5^{\text{th}}{{< /katex >}} year (i.e. in 6th year), we need to find the sixth term of this G.P.

Thus, {{< katex >}}n = 6, a = 40,000, r = \frac{90}{100}{{< /katex >}}.

Using {{< katex >}}t_n = ar^{n-1}{{< /katex >}}:
{{< katex >}}t_6 = 40000 \times \left(\frac{90}{100}\right)^5 = 40000 \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10} = 23619.60{{< /katex >}}

Therefore the value of the machine in 6th year = ₹23619.60

---

## Exercise 2.7

1. Which of the following sequences are in G.P.?
   - (i) {{< katex >}}3, 9, 27, 81, \ldots{{< /katex >}}
   - (ii) {{< katex >}}4, 44, 444, 4444, \ldots{{< /katex >}}
   - (iii) {{< katex >}}0.5, 0.05, 0.005, \ldots{{< /katex >}}
   - (iv) {{< katex >}}\frac{1}{3}, \frac{1}{6}, \frac{1}{12}, \ldots{{< /katex >}}
   - (v) {{< katex >}}1, -5, 25, -125, \ldots{{< /katex >}}
   - (vi) {{< katex >}}120, 60, 30, 18, \ldots{{< /katex >}}
   - (vii) {{< katex >}}16, 4, 1, \frac{1}{4}, \ldots{{< /katex >}}

2. Write the first three terms of the G.P. whose first term and the common ratio are given below.
   - (i) {{< katex >}}a = 6, r = 3{{< /katex >}}
   - (ii) {{< katex >}}a = \sqrt{2}, r = \sqrt{2}{{< /katex >}}
   - (iii) {{< katex >}}a = 1000, r = \frac{2}{5}{{< /katex >}}

3. In a G.P. {{< katex >}}729, 243, 81, \cdots{{< /katex >}}
 find {{< katex >}}t_7{{< /katex >}}

4. Find {{< katex >}}x{{< /katex >}} so that {{< katex >}} x + 6, x + 12{{< /katex >}}
 and {{< katex >}}x + 15{{< /katex >}} are consecutive terms of a Geometric Progression.

5. Find the number of terms in the following G.P.
   - (i) {{< katex >}}4, 8, 16, \ldots, 8192{{< /katex >}}?
   - (ii) {{< katex >}}\frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \ldots, \frac{1}{2187}{{< /katex >}}

6. In a G.P. the {{< katex >}}9^{\text{th}}{{< /katex >}} 
term is 32805 and {{< katex >}}6^{\text{th}}{{< /katex >}}
 term is 1215. Find the {{< katex >}}12^{\text{th}}{{< /katex >}} term.

7. Find the {{< katex >}}10^{\text{th}}{{< /katex >}} 
term of a G.P. whose {{< katex >}}8^{\text{th}}{{< /katex >}} term is 768 and the common ratio is 2.

8. If {{< katex >}}a, b, c{{< /katex >}} 
are in A.P. then show that {{< katex >}}3^a, 3^b, 3^c{{< /katex >}} are in G.P.

9. In a G.P. the product of three consecutive terms is 27 and the sum of the product of two terms taken at a time is {{< katex >}}\frac{57}{2}{{< /katex >}}. Find the three terms.

10. A man joined a company as Assistant Manager. The company gave him a starting salary of ₹60,000 and agreed to increase his salary 5% annually. What will be his salary after 5 years?

11. Sivamani is attending an interview for a job and the company gave two offers to him.
    - Offer A: ₹20,000 to start with followed by a guaranteed annual increase of 6% for the first 5 years.
    - Offer B: ₹22,000 to start with followed by a guaranteed annual increase of 3% for the first 5 years.
    
    What is his salary in the {{< katex >}}4^{\text{th}}{{< /katex >}} year with respect to the offers A and B?

12. If {{< katex >}}a, b, c{{< /katex >}}
 are three consecutive terms of an A.P. and {{< katex >}}x, y, z{{< /katex >}} 
 are three consecutive terms of a G.P. then prove that {{< katex >}}x^{b-c} \times y^{c-a} \times z^{a-b} = 1{{< /katex >}}.

---