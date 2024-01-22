---
title: 'Geometric Progression'
weight: 8
---

# Geometric Progression

In the diagram given in Fig.2.13,{{<katex>}} \Delta DEF{{</katex>}} is formed by joining the mid points of the sides AB, BC and CA of {{<katex>}} \Delta ABC{{</katex>}} . Then the size of the triangle {{<katex>}} \Delta DEF{{</katex>}} is exactly one-fourth of the size of {{<katex>}} \Delta ABC{{</katex>}} . Similarly {{<katex>}} \Delta GHI{{</katex>}} is also one-fourth of {{<katex>}} \Delta DEF{{</katex>}} and so on. In general, the successive areas are one-fourth of the previous areas.

The area of these triangles are

![](1.png)
![](2.png)
![](3.png)

In this case, we see that beginning with {{<katex>}} \Delta ABC{{</katex>}}, we see that the successive triangles are formed whose areas are precisely one-fourth the area of the previous triangle. So, each term is obtained by multiplying 1/4 to the previous term.

As another case, let us consider that a viral disease is spreading in a way such that at any stage two new persons get affected from an affected person. At
first stage, one person is affected, at second stage two persons are affected and is spreading to four persons and so on. Then, number of persons affected at each stage are 1 , 2 , 4 , 8 , ... where except the first term, each term is precisely twice the previous term.

From the above examples, it is clear that each term is got by multiplying a fixed number to the preceding number. This idea leads us to the concept of Geometric Progression.

**Definition**
A Geometric Progression is a sequence in which each term is obtained by multiplying a fixed non-zero number to the preceding term except the first term. The fixed number is called common ratio. The common ratio is usually denoted by r.

**2.9.1** General form of Geometric Progression
Let a and r!=10 be real numbers. Then the numbers of the form a, ar, {{<katex>}}ar^{2}{{</katex>}} , ... {{<katex>}}ar^{n-1}{{</katex>}} ... is called a Geometric Progression. The number ‘ a ’ is called the first term and number ‘ r ’ is called the common ratio.

We note that beginning with first term a , each term is obtained by multiplied with
the common ratio ‘ r ’ to give ar , {{<katex>}}ar^{2}{{</katex>}} , {{<katex>}}ar^{3}{{</katex>}} ,...
**2.9.2** General term of Geometric Progression
We try to find a formula for n th term or general term of Geometric Progression (G P.) whose terms are in the common ratio.

{{<katex>}}a, a r, a r^{2}, \ldots, a r^{n-1}, \ldots{{</katex>}} where a is the first term and ' r ' is the common ratio. Let {{<katex>}}t_{n}{{</katex>}} be the {{<katex>}}n^{\text {th }}{{</katex>}} term of the G.P.

{{<katex>}}
\begin{aligned}
& t_{1}=a=a \times r^{0}=a \times r^{1-1} \\
& t_{2}=t_{1} \times r=a \times r=a \times r^{2-1} \\
& t_{3}=t_{2} \times r=a r \times r=a r^{2}=a r^{3-1} \\
& \vdots \\
& \quad \vdots \\
& t_{n}=t_{n-1} \times r=a r^{n-2} \times r=a r^{n-2+1}=a r^{n-1}
\end{aligned}
{{</katex>}}

Thus, the general term or {{<katex>}}n^{\text {th }}{{</katex>}} term of a G.P. is {{<katex>}}t_{n}=a r^{n-1}{{</katex>}}

Note

If we consider the ratio of successive terms of the G.P. then we have

{{<katex>}}
\frac{t_{2}}{t_{1}}=\frac{a r}{a}=r, \frac{t_{3}}{t_{2}}=\frac{a r^{2}}{a r}=r, \frac{t_{4}}{t_{3}}=\frac{a r^{3}}{a r^{2}}=r, \frac{t_{5}}{t_{4}}=\frac{a r^{4}}{a r^{3}}=r, \ldots
{{</katex>}}

Thus, the ratio between any two consecutive terms of the Geometric Progression is always constant and that constant is the common ratio of the given Progression.

![](4.png)

Example 2.40 Which of the following sequences form a Geometric Progression?
(i) {{<katex>}}7,14,21,28, \ldots{{</katex>}}
(ii) {{<katex>}}\frac{1}{2}, 1,2,4, \ldots{{</katex>}}
(iii) {{<katex>}}5,25,50,75, \ldots{{</katex>}}

Solution To check if a given sequence form a G.P. we have to see if the ratio between successive terms are equal.

(i) {{<katex>}}7,14,21,28, \ldots{{</katex>}}

{{<katex>}}
\frac{t_{2}}{t_{1}}=\frac{14}{7}=2 ; \quad \frac{t_{3}}{t_{2}}=\frac{21}{14}=\frac{3}{2} ; \quad \frac{t_{4}}{t_{3}}=\frac{28}{21}=\frac{4}{3}
{{</katex>}}

Since the ratios between successive terms are not equal, the sequence 7, 14, 21, {{<katex>}}28, \ldots{{</katex>}} is not a Geometric Progression.

(ii) {{<katex>}}\frac{1}{2}, 1,2,4, \ldots{{</katex>}}

{{<katex>}}
\frac{t_{2}}{t_{1}}=\frac{1}{\frac{1}{2}}=2 ; \quad \frac{t_{3}}{t_{2}}=\frac{2}{1}=2 ; \quad \frac{t_{4}}{t_{3}}=\frac{4}{2}=2
{{</katex>}}

Here the ratios between successive terms are equal. Therefore the sequence {{<katex>}}\frac{1}{2}, 1,2,4, \ldots{{</katex>}} is a Geometric Progression with common ratio r=2.

(iii) {{<katex>}}5,25,50,75, \ldots{{</katex>}}

{{<katex>}}\frac{t_{2}}{t_{1}}=\frac{25}{5}=5 ; \quad \frac{t_{3}}{t_{2}}=\frac{50}{25}=2 ; \quad \frac{t_{4}}{t_{3}}=\frac{75}{50}=\frac{3}{2}{{</katex>}}

**Example 2.41** Find the geometric progression whose first term and common ratios are given by (i) {{<katex>}}a=-7, r=6{{</katex>}} (ii) {{<katex>}}a=256, r=0.5{{</katex>}}

*Solution* (i) The general form of Geometric progression is {{<katex>}}a, a r, a r^{2}, \ldots{{</katex>}}

{{<katex>}}a=-7{{</katex>}}, ar {{<katex>}}=-7 \times 6=-42, a r^{2}=-7 \times 6^{2}=-252{{</katex>}}

Therefore the required Geometric Progression is {{<katex>}}-7,-42,-252, \ldots{{</katex>}}

(ii) The general form of Geometric progression is {{<katex>}}a, a r, a r^{2}, \ldots{{</katex>}}

{{<katex>}}a=256, a r=256 \times 0.5=128, a r^{2}=256 \times(0.5)^{2}=64{{</katex>}}

Therefore the required Geometric progression is {{<katex>}}256,128,64, \ldots{{</katex>}}.

![](5.png)

**Example 2.42** Find the {{<katex>}}8^{\text {th }}{{</katex>}} term of the G.P. 9, 3, 1,...

Solution To find the {{<katex>}}8^{\text {th }}{{</katex>}} term we have to use the {{<katex>}}n^{\text {th }}{{</katex>}} term formula {{<katex>}}t_{n}=a r^{n-1}{{</katex>}}

First term a=9, Common ratio {{<katex>}}r=\frac{t_{2}}{t_{1}}=\frac{3}{9}=\frac{1}{3}{{</katex>}}

{{<katex>}}
t_{8}=9 \times\left(\frac{1}{3}\right)^{8-1}=9 \times\left(\frac{1}{3}\right)^{7}=\frac{1}{243}
{{</katex>}}

Therefore the {{<katex>}}8^{\text {th }}{{</katex>}} term of the G.P. is {{<katex>}}\frac{1}{243}{{</katex>}}.

**Example 2.43** In a Geometric progression, the {{<katex>}}4^{\text {th }}{{</katex>}} term is {{<katex>}}\frac{8}{9}{{</katex>}} and the {{<katex>}}7^{\text {th }}{{</katex>}} term is {{<katex>}}\frac{64}{243}{{</katex>}}. Find the Geometric Progression.

*Solution* {{<katex>}}4^{\text {th }}{{</katex>}} term, {{<katex>}}t_{4}=\frac{8}{9} \Rightarrow a r^{3}=\frac{8}{9}{{</katex>}}

{{<katex>}}
7^{\text {th }} \text { term, } t_{7}=\frac{64}{243} \Rightarrow a r^{6}=\frac{64}{243}
{{</katex>}}

Dividing (2) by (1) we get, {{<katex>}}\frac{a r^{6}}{a r^{3}}=\frac{\frac{64}{243}}{\frac{8}{9}}{{</katex>}}

{{<katex>}}
r^{3}=\frac{8}{27} \Rightarrow r=\frac{2}{3}
{{</katex>}}

Substituting the value of r in (1), we get {{<katex>}}a \times\left[\frac{2}{3}\right]^{3}=\frac{8}{9} \Rightarrow a=3{{</katex>}}

Therefore the Geometric Progression is a, {{<katex>}}a r, a r^{2}, \ldots{{</katex>}} That is, {{<katex>}}3,2, \frac{4}{3}, \ldots{{</katex>}}

![](6.png)

**Example 2.44** The product of three consecutive terms of a Geometric Progression is 343 and their sum is {{<katex>}}\frac{91}{3}{{</katex>}}. Find the three terms.

*Solution* Since the product of 3 consecutive terms is given.

we can take them as {{<katex>}}\frac{a}{r}, a, a r{{</katex>}}.

Product of the terms =343

{{<katex>}}
\begin{aligned}
\frac{a}{r} \times a \times a r & =343 \\
a^{3}=7^{3} \Rightarrow a & =7
\end{aligned}
{{</katex>}}

Sum of the terms {{<katex>}}=\frac{91}{3}{{</katex>}}

Hence {{<katex>}}a\left(\frac{1}{r}+1+r\right)=\frac{91}{3} \Rightarrow 7\left(\frac{1+r+r^{2}}{r}\right)=\frac{91}{3}{{</katex>}}

{{<katex>}}3+3 r+3 r^{2}=13 r \Rightarrow 3 r^{2}-10 r+3=0{{</katex>}}

{{<katex>}}(3 r-1)(r-3)=0 \Rightarrow r=3{{</katex>}} or {{<katex>}}r=\frac{1}{3}{{</katex>}}

If a=7, r=3 then the three terms are {{<katex>}}\frac{7}{3}, 7,21{{</katex>}}.

If {{<katex>}}a=7, r=\frac{1}{3}{{</katex>}} then the three terms are {{<katex>}}21,7, \frac{7}{3}{{</katex>}}.

**Condition for three numbers to be in G.P.**

If a, b, c are in G.P. then {{<katex>}}b=a r, c=a r^{2}{{</katex>}}. So {{<katex>}}a c=a \times a r^{2}=(a r)^{2}=b^{2}{{</katex>}}. Thus {{<katex>}}b^{2}=a c{{</katex>}}

Similarly, if {{<katex>}}b^{2}=a c{{</katex>}}, then {{<katex>}}\frac{b}{a}=\frac{c}{b}{{</katex>}}. So a, b, c are in G.P.

Thus three non-zero numbers a, b, c are in G.P. if and only if {{<katex>}}b^{2}=a c{{</katex>}}.

**Example 2.45** The present value of a machine is ₹40,000 and its value depreciates each year by {{<katex>}}10 \%{{</katex>}}. Find the estimated value of the machine in the {{<katex>}}6^{\text {th }}{{</katex>}} year.

*Solution* The value of the machine at present is ₹40,000. Since it is depreciated at the rate of {{<katex>}}10 \%{{</katex>}} after one year the value of the machine is {{<katex>}}90 \%{{</katex>}} of the initial value.

That is the value of the machine at the end of the first year is {{<katex>}}40,000 \times \frac{90}{100}{{</katex>}}

After two years, the value of the machine is {{<katex>}}90 \%${{</katex>}}of the value in the first year.

Value of the machine at the end of the {{<katex>}}2^{\text {nd }}{{</katex>}} year is {{<katex>}}40,000 \times\left(\frac{90}{100}\right)^{2}{{</katex>}}

Continuing this way, the value of the machine depreciates in the following way as

{{<katex>}}
40000,40000 \times \frac{90}{100}, 40000 \times\left(\frac{90}{100}\right)^{2} \ldots
{{</katex>}}

This sequence is in the form of G.P. with first term 40,000 and common ratio {{<katex>}}\frac{90}{100}{{</katex>}}. For finding the value of the machine at the end of {{<katex>}}5^{\text {th }}{{</katex>}} year (i.e. in {{<katex>}}6^{\text {th }}{{</katex>}} year), we need to find the sixth term of this G.P.

Thus, {{<katex>}}n=6, a=40,000, r=\frac{90}{100}{{</katex>}}.

Using {{<katex>}}\quad t_{n}=a r^{n-1}{{</katex>}}, we have {{<katex>}}t_{6}=40,000 \times\left(\frac{90}{100}\right)^{6-1}=40000 \times\left(\frac{90}{100}\right)^{5}{{</katex>}}

{{<katex>}}
t_{6}=40,000 \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10} \times \frac{9}{10}=23619.6
{{</katex>}}

Therefore the value of the machine in {{<katex>}}6^{\text {th }}{{</katex>}} year {{<katex>}}=₹ 23619.60{{</katex>}}

**Exercise 2.7**

1. Which of the following sequences are in G.P.?
(i) {{<katex>}}3,9,27,81, \ldots{{</katex>}}
(ii) {{<katex>}}4,44,444,4444, \ldots{{</katex>}}
(iii) {{<katex>}}0.5,0.05,0.005, \ldots{{</katex>}}
(iv) {{<katex>}}\frac{1}{3}, \frac{1}{6}, \frac{1}{12}, \ldots{{</katex>}}
(v) {{<katex>}}1,-5,25,-125, \ldots{{</katex>}}
(vi) {{<katex>}}120,60,30,18, \ldots{{</katex>}}
(vii) {{<katex>}}16,4,1, \frac{1}{4}, \ldots{{</katex>}}
2. Write the first three terms of the G.P. whose first term and the common ratio are given below.
(i) a=6, r=3
(ii) {{<katex>}}a=\sqrt{2}, r=\sqrt{2}{{</katex>}}
(iii) {{<katex>}}a=1000, r=\frac{2}{5}{{</katex>}}
3. In a G.P. {{<katex>}}729,243,81, \ldots{{</katex>}} find {{<katex>}}t_{7}{{</katex>}}.
4. Find x so that {{<katex>}}x+6, x+12{{</katex>}} and {{<katex>}}x+15{{</katex>}} are consecutive terms of a Geometric Progression.
5. Find the number of terms in the following G.P.
(i) {{<katex>}}4,8,16, \ldots, 8192{{</katex>}} ?
(ii) {{<katex>}}\frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \ldots, \frac{1}{2187}{{</katex>}}
6. In a G.P. the {{<katex>}}9^{\text {th }}{{</katex>}} term is 32805 and {{<katex>}}6^{\text {th }}{{</katex>}} term is 1215 . Find the {{<katex>}}12^{\text {th }}{{</katex>}} term.
7. Find the {{<katex>}}10^{\text {th }}{{</katex>}} term of a G.P. whose {{<katex>}}8^{\text {th }}{{</katex>}} term is 768 and the common ratio is 2.
8. If a, b, c are in A.P. then show that {{<katex>}}3^{a}, 3^{b}, 3^{c}{{</katex>}} are in G.P.
9. In a G.P. the product of three consecutive terms is 27 and the sum of the product of two terms taken at a time is {{<katex>}}\frac{57}{2}{{</katex>}}. Find the three terms.
10.  A man joined a company as Assistant Manager. The company gave him a starting salary of ₹ 60,000 and agreed to increase his salary {{<katex>}}5 \%{{</katex>}} annually. What will be his salary after 5 years?
11. Sivamani is attending an interview for a job and the company gave two offers to him. Offer A: ₹20,000 to start with followed by a guaranteed annual increase of {{<katex>}}6 \%{{</katex>}} for the first 5 years.

Offer B: ₹22,000 to start with followed by a guaranteed annual increase of $3 \%$ for the first 5 years.

What is his salary in the {{<katex>}}4^{\text {th }}{{</katex>}} year with respect to the offers A and B ?

12. If a, b, c are three consecutive terms of an A.P. and x, y, z are three consecutive terms of a G.P. then prove that {{<katex>}}x^{b-c} \times y^{c-a} \times z^{a-b}=1{{</katex>}}.