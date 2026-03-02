---
title: 'Arithmetic Progression'
weight: 6
---
## 2.7 Arithmetic Progression

![Matchstick triangles Fig. 2.11](matchstick_triangles.jpg)

Let us begin with the following two illustrations

### Illustration 1

Make the following figures using match sticks:
- (i) How many match sticks are required for each figure? 3, 5, 7 and 9.
- (ii) Can we find the difference between the successive numbers?
{{< katex >}}5 - 3 = 7 - 5 = 9 - 7 = 2{{< /katex >}}

Therefore, the difference between successive numbers is always 2.

### Illustration 2

A man got a job whose initial monthly salary is fixed at ₹10,000 with an annual increment of ₹2000. His salary during {{< katex >}}1^{\text{st}}{{< /katex >}},
 {{< katex >}}2^{\text{nd}}{{< /katex >}}
  and {{< katex >}}3^{\text{rd}}{{< /katex >}} years will be ₹10000, ₹12000 and ₹14000 respectively.

If we now calculate the difference of the salaries for the successive years, we get {{< katex >}}12000 - 10000 = 2000{{< /katex >}};
 {{< katex >}}14000 - 12000 = 2000{{< /katex >}}. Thus the difference between the successive numbers (salaries) is always 2000.

Did you observe the common property behind these two illustrations? In these two examples, the difference between successive terms always remains constant. Moreover, each term is obtained by adding a fixed number (2 and 2000 in illustrations 1 and 2 presented above) to the preceding term except the first term. This fixed number which is a constant for the differences between successive terms is called the **"common difference"**.

### Definition

Let {{< katex >}}a{{< /katex >}}
 and {{< katex >}}d{{< /katex >}} 
 be real numbers. Then the numbers of the form {{< katex >}}a, a+d, a+2d, a+3d, a+4d, \ldots{{< /katex >}} 
 is said to form **Arithmetic Progression** denoted by **A.P.** The number '{{< katex >}}a{{< /katex >}}'
  is called the **first term** and '{{< katex >}}d{{< /katex >}}' is called the **common difference**.

Simply, an Arithmetic Progression is a sequence whose successive terms differ by a constant number. Thus, for example, the set of even positive integers {{< katex >}}2, 4, 6, 8, 10, 12, \ldots{{< /katex >}}
 is an A.P. whose first term is {{< katex >}}a = 2{{< /katex >}}
  and common difference is also {{< katex >}}d = 2{{< /katex >}} 
  since {{< katex >}}4 - 2 = 2{{< /katex >}}, 
  {{< katex >}}6 - 4 = 2{{< /katex >}},
   {{< katex >}}8 - 6 = 2{{< /katex >}},
    {{< katex >}}\ldots{{< /katex >}}

> **Note**
> - The difference between any two consecutive terms of an A.P. is always constant. That constant value is called the common difference.
> - If there are finite numbers of terms in an A.P. then it is called **Finite Arithmetic Progression**. If there are infinitely many terms in an A.P. then it is called **Infinite Arithmetic Progression**.

### 2.7.1 Terms and Common Difference of an A.P.

1. The terms of an A.P. can be written as:
{{< katex >}}\begin{aligned}
t_1 &= a = a + (1-1)d \\
t_2 &= a + d = a + (2-1)d \\
t_3 &= a + 2d = a + (3-1)d \\
t_4 &= a + 3d = a + (4-1)d \\
&\vdots
\end{aligned}{{</ katex >}}

In general, the {{< katex >}}n^{\text{th}}{{< /katex >}} 
term denoted by {{< katex >}}t_n{{< /katex >}} can be written as:
{{< katex >}}\boxed{t_n = a + (n-1)d}{{< /katex >}}

In an AP, {{< katex >}}n^{\text{th}}{{< /katex >}} 
term is, {{< katex >}}t_n = a + (n-1)d{{< /katex >}},
 here, {{< katex >}}a{{< /katex >}}
  is the first term, {{< katex >}}d{{< /katex >}} is the common difference.

2. In general to find the common difference of an A.P. we should subtract first term from the second term, second from the third and so on.

For example, {{< katex >}}t_1 = a, t_2 = a + d{{< /katex >}}
{{< katex >}}\therefore t_2 - t_1 = (a + d) - a = d{{< /katex >}}

Similarly, {{< katex >}}t_2 = a + d, t_3 = a + 2d, \ldots{{< /katex >}}
{{< katex >}}\therefore t_3 - t_2 = (a + 2d) - (a + d) = d{{< /katex >}}

In general, {{< katex >}}d = t_2 - t_1 = t_3 - t_2 = t_4 - t_3 = \ldots{{< /katex >}}

{{< katex >}}d = t_n - t_{n-1} \quad \text{for } n = 2, 3, 4, \ldots{{< /katex >}}

**Progress Check**
1. The difference between any two consecutive terms of an A.P. is _______.
2. If {{< katex >}}a{{< /katex >}}
 and {{< katex >}}d{{< /katex >}}
  are the first term and common difference of an A.P. then the {{< katex >}}8^{\text{th}}{{< /katex >}} term is _______.
3. If {{< katex >}}t_n{{< /katex >}}
 is the {{< katex >}}n^{\text{th}}{{< /katex >}} 
 term of an A.P., then {{< katex >}}t_{n+2} - t_n{{< /katex >}} is _______.

Let us try to find the common differences of the following A.P.'s:
- (i) {{< katex >}}1, 4, 7, 10, \ldots{{< /katex >}}
 {{< katex >}}d = 4 - 1 = 7 - 4 = 10 - 7 = \ldots = 3{{< /katex >}}
- (ii) {{< katex >}}6, 2, -2, -6, \ldots{{< /katex >}} 
{{< katex >}}d = 2 - 6 = -2 - 2 = -6 - (-2) = \ldots = -4{{< /katex >}}

The common difference of an A.P. can be positive, negative or zero.

> **Thinking Corner**
> If {{< katex >}}t_n{{< /katex >}} 
is the {{< katex >}}n^{\text{th}}{{< /katex >}}
 term of an A.P. then the value of {{< katex >}}t_{n+1} - t_{n-1}{{< /katex >}} is _______.

**Example 2.23** Check whether the following sequences are in A.P. or not?
- (i) {{< katex >}}x+2, x+3, x+4, \ldots{{< /katex >}}
- (ii) {{< katex >}}2, 4, 8, 16, \ldots{{< /katex >}}
- (iii) {{< katex >}}3\sqrt{2}, 5\sqrt{2}, 7\sqrt{2}, 9\sqrt{2}, \ldots{{< /katex >}}

**Solution:** To check that the given sequence is in A.P., it is enough to check if the differences between the consecutive terms are equal or not.

**(i)** {{< katex >}}t_2 - t_1 = (x+3) - (x+2) = 1{{< /katex >}}
{{< katex >}}t_3 - t_2 = (x+4) - (x+3) = 1{{< /katex >}}

Thus, the differences between consecutive terms are equal. Hence the sequence {{< katex >}}x+2, x+3, x+4, \ldots{{< /katex >}} is in A.P.

**(ii)** {{< katex >}}t_2 - t_1 = 4 - 2 = 2{{< /katex >}}
{{< katex >}}t_3 - t_2 = 8 - 4 = 4{{< /katex >}}

{{< katex >}}t_2 - t_1 \neq t_3 - t_2{{< /katex >}}

Thus, the differences between consecutive terms are not equal. Hence the terms of the sequence {{< katex >}}2, 4, 8, 16, \ldots{{< /katex >}} are not in A.P.

**(iii)** {{< katex >}}t_2 - t_1 = 5\sqrt{2} - 3\sqrt{2} = 2\sqrt{2}{{< /katex >}}
{{< katex >}}t_3 - t_2 = 7\sqrt{2} - 5\sqrt{2} = 2\sqrt{2}{{< /katex >}}
{{< katex >}}t_4 - t_3 = 9\sqrt{2} - 7\sqrt{2} = 2\sqrt{2}{{< /katex >}}

Thus, the differences between consecutive terms are equal. Hence the terms of the sequence {{< katex >}}3\sqrt{2}, 5\sqrt{2}, 7\sqrt{2}, 9\sqrt{2}, \ldots{{< /katex >}} are in A.P.

**Example 2.24** Write an A.P. whose first term is 20 and common difference is 8.

**Solution:** First term {{< katex >}}= a = 20{{< /katex >}}; 
common difference {{< katex >}}= d = 8{{< /katex >}}

Arithmetic Progression is {{< katex >}}a, a+d, a+2d, a+3d, \ldots{{< /katex >}}

In this case, we get {{< katex >}}20, 20+8, 20+2(8), 20+3(8), \ldots{{< /katex >}}

So, the required A.P. is {{< katex >}}20, 28, 36, 44, \ldots{{< /katex >}}

> **Note**
> An Arithmetic progression having a common difference of zero is called a constant arithmetic progression.

**Example 2.25** Find the {{< katex >}}15^{\text{th}}{{< /katex >}},
 {{< katex >}}24^{\text{th}}{{< /katex >}} 
 and {{< katex >}}n^{\text{th}}{{< /katex >}}
  term (general term) of an A.P. given by {{< katex >}}3, 15, 27, 39, \ldots{{< /katex >}}

**Solution:** We have, first term {{< katex >}}= a = 3{{< /katex >}}
 and common difference {{< katex >}}= d = 15 - 3 = 12{{< /katex >}}.

We know that {{< katex >}}n^{\text{th}}{{< /katex >}}
 term (general term) of an A.P. with first term {{< katex >}}a{{< /katex >}}
  and common difference {{< katex >}}d{{< /katex >}} is given by:
{{< katex >}}t_n = a + (n-1)d{{< /katex >}}

{{< katex >}}\begin{aligned}
t_{15} &= a + (15-1)d = a + 14d = 3 + 14(12) = 171 \\
t_{24} &= a + (24-1)d = a + 23d = 3 + 23(12) = 279
\end{aligned}{{</ katex >}}

The {{< katex >}}n^{\text{th}}{{< /katex >}} (general term) term is given by:
{{< katex >}}\begin{aligned}
t_n &= 3 + (n-1)12 \\
t_n &= 12n - 9
\end{aligned}{{< / katex >}}

> **Note**
> In a finite A.P. whose first term is {{< katex >}}a{{< /katex >}} 
and last term {{< katex >}}l{{< /katex >}}, then the number of terms in the A.P. is given by:
> {{< katex >}}l = a + (n-1)d \implies n = \left(\frac{l-a}{d}\right) + 1{{< /katex >}}

**Example 2.26** Find the number of terms in the A.P. {{< katex >}}3, 6, 9, 12, \ldots, 111{{< /katex >}}.

**Solution:** First term {{< katex >}}a = 3{{< /katex >}};
 common difference {{< katex >}}d = 6 - 3 = 3{{< /katex >}};
  last term {{< katex >}}l = 111{{< /katex >}}

We know that:
{{< katex >}}n = \left|\frac{l-a}{d}\right| + 1 = \left|\frac{111-3}{3}\right| + 1 = 37{{< /katex >}}

Thus the A.P. contain 37 terms.

**Example 2.27** Determine the general term of an A.P. whose {{< katex >}}7^{\text{th}}{{< /katex >}} 
term is {{< katex >}}-1{{< /katex >}}
 and {{< katex >}}16^{\text{th}}{{< /katex >}} term is 17.

**Solution:** Let the A.P. be {{< katex >}}t_1, t_2, t_3, t_4, \ldots{{< /katex >}}

It is given that {{< katex >}}t_7 = -1{{< /katex >}}
 and {{< katex >}}t_{16} = 17{{< /katex >}}

{{<  katex >}}\begin{aligned}
a + (7-1)d &= -1 \quad \text{and} \quad a + (16-1)d = 17 \\
a + 6d &= -1 \quad \ldots(1) \\
a + 15d &= 17 \quad \ldots(2)
\end{aligned}{{<  /katex >}}

Subtracting equation (1) from equation (2), we get {{< katex >}}9d = 18 \implies d = 2{{< /katex >}}

Putting {{< katex >}}d = 2{{< /katex >}}
 in equation (1), we get {{< katex >}}a + 12 = -1 \therefore a = -13{{< /katex >}}

Hence, general term:
{{<  katex >}}\begin{aligned}
t_n &= a + (n-1)d \\
&= -13 + (n-1)2 \\
&= 2n - 15
\end{aligned}{{</  katex >}}

**Example 2.28** If {{< katex >}}l^{\text{th}}{{< /katex >}},
 {{< katex >}}m^{\text{th}}{{< /katex >}}
  and {{< katex >}}n^{\text{th}}{{< /katex >}}
   terms of an A.P. are {{< katex >}}x, y, z{{< /katex >}} respectively, then show that:
- (i) {{< katex >}}x(m-n) + y(n-l) + z(l-m) = 0{{< /katex >}}
- (ii) {{< katex >}}(x-y)n + (y-z)l + (z-x)m = 0{{< /katex >}}

**Solution:** (i) Let {{< katex >}}a{{< /katex >}} 
be the first term and {{< katex >}}d{{< /katex >}} be the common difference. It is given that:
{{<  katex >}}\begin{aligned}
t_l &= x \implies a + (l-1)d = x \\
t_m &= y \implies a + (m-1)d = y \\
t_n &= z \implies a + (n-1)d = z
\end{aligned}{{< / katex >}}

We have:
{{<  katex >}}\begin{aligned}
&x(m-n) + y(n-l) + z(l-m) \\
&= [a + (l-1)d](m-n) + [a + (m-1)d](n-l) + [a + (n-1)d](l-m) \\
&= a[(m-n) + (n-l) + (l-m)] + d[(l-1)(m-n) + (m-1)(n-l) + (n-1)(l-m)] \\
&= a[0] + d[lm - ln - m + n + mn - lm - n + l + ln - m - n + l + m] \\
&= a[0] + d[0] = 0
\end{aligned}{{</  katex >}}

(ii) On subtracting equation (2) from equation (1), equation (3) from equation (2) and equation (1) from equation (3), we get:
{{<  katex >}}\begin{aligned}
x - y &= (l-m)d \\
y - z &= (m-n)d \\
z - x &= (n-l)d \\
(x-y)n + (y-z)l + (z-x)m &= [(l-m)n + (m-n)l + (n-l)m]d \\
&= [ln - mn + lm - nl + nm - lm]d = 0
\end{aligned}{{</  katex >}}

> **Note**
> In an Arithmetic Progression:
> - If every term is added or subtracted by a constant, then the resulting sequence is also an A.P.
> - If every term is multiplied or divided by a non-zero number, then the resulting sequence is also an A.P.
> - If the sum of three consecutive terms of an A.P. is given, then they can be taken as {{< katex >}}a-d, a, a+d{{< /katex >}}. Here the common difference is
 {{< katex >}}d{{< /katex >}}.
> - If the sum of four consecutive terms of an A.P. is given then, they can be taken as {{< katex >}}a-3d, a-d, a+d, a+3d{{< /katex >}}. Here common difference is 
{{< katex >}}2d{{< /katex >}}.

**Example 2.29** In an A.P., sum of four consecutive terms is 28 and the sum of their squares is 276. Find the four numbers.

**Solution:** Let us take the four terms in the form {{< katex >}}(a-3d), (a-d), (a+d){{< /katex >}} 
and {{< katex >}}(a+3d){{< /katex >}}.

Since, sum of the four terms is 28:
{{< katex >}}(a-3d) + (a-d) + (a+d) + (a+3d) = 28{{< /katex >}}
{{< katex >}}4a = 28 \implies a = 7{{< /katex >}}

Similarly, since sum of their squares is 276:
{{< katex >}}\begin{aligned}
(a-3d)^2 + (a-d)^2 + (a+d)^2 + (a+3d)^2 &= 276 \\
a^2 - 6ad + 9d^2 + a^2 - 2ad + d^2 + a^2 + 2ad + d^2 + a^2 + 6ad + 9d^2 &= 276 \\
4a^2 + 20d^2 &= 276 \implies 4(7)^2 + 20d^2 = 276 \\
d^2 &= 4 \implies d = \pm\sqrt{4} = \pm 2
\end{aligned}{{< /katex >}}

If {{< katex >}}d = 2{{< /katex >}}
 then the four numbers are {{< katex >}}7-3(2), 7-2, 7+2, 7+3(2){{< /katex >}}
That is the four numbers are {{< katex >}}1, 5, 9{{< /katex >}}
 and {{< katex >}}13{{< /katex >}}.

If {{< katex >}}d = -2{{< /katex >}} 
then the four numbers are {{< katex >}}13, 9, 5{{< /katex >}} 
and {{< katex >}}1{{< /katex >}}.

Therefore, the four consecutive terms of the A.P. are {{< katex >}}1, 5, 9{{< /katex >}}
 and {{< katex >}}13{{< /katex >}}.

### Condition for three numbers to be in A.P.

If {{< katex >}}a, b, c{{< /katex >}} 
are in A.P. then {{< katex >}}b = a + d{{< /katex >}}, 
{{< katex >}}c = a + 2d{{< /katex >}} so:
{{< katex >}}a + c = a + (a + 2d) = 2(a + d) = 2b{{< /katex >}}

Thus, {{< katex >}}2b = a + c{{< /katex >}}

Similarly, if {{< katex >}}2b = a + c{{< /katex >}},
 then {{< katex >}}b - a = c - b{{< /katex >}} 
 so {{< katex >}}a, b, c{{< /katex >}} are in A.P.

Thus three non-zero numbers {{< katex >}}a, b, c{{< /katex >}} 
are in A.P. if and only if {{< katex >}}\boxed{2b = a + c}{{< /katex >}}

**Example 2.30** A mother divides ₹207 into three parts such that the amount are in A.P. and gives it to her three children. The product of the two least amounts that the children had ₹4623. Find the amount received by each child.

**Solution:** Let the amount received by the three children be in the form of A.P. is given by {{< katex >}}a-d, a, a+d{{< /katex >}}.

Since, sum of the amount is ₹207:
{{< katex >}}(a-d) + a + (a+d) = 207{{< /katex >}}
{{< katex >}}3a = 207 \implies a = 69{{< /katex >}}

It is given that product of the two least amounts is 4623:
{{< katex >}}\begin{aligned}
(a-d) \cdot a &= 4623 \\
(69-d) \cdot 69 &= 4623 \\
d &= 2
\end{aligned}{{< /katex >}}

Therefore, amount given by the mother to her three children are ₹{{< katex >}}(69-2){{< /katex >}},
 ₹{{< katex >}}69{{< /katex >}},
  ₹{{< katex >}}(69+2){{< /katex >}}.
  That is, ₹{{< katex >}}67{{< /katex >}},
  ₹{{< katex >}}69{{</ katex >}} and ₹{{< katex >}}71{{< /katex >}}.

**Progress Check**
1. If every term of an A.P. is multiplied by 3, then the common difference of the new A.P. is _______.
2. Three numbers {{< katex >}}a, b{{< /katex >}}
 and {{< katex >}}c{{< /katex >}} will be in A.P. if and only if _______.

---

## Exercise 2.5

1. Check whether the following sequences are in A.P.
   - (i) {{< katex >}}a-3, a-5, a-7, \ldots{{< /katex >}}
   - (ii) {{< katex >}}\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}, \ldots{{< /katex >}}
   - (iii) {{< katex >}}9, 13, 17, 21, 25, \ldots{{< /katex >}}
   - (iv) {{< katex >}}-\frac{1}{3}, 0, \frac{1}{3}, \frac{2}{3}, \ldots{{< /katex >}}
   - (v) {{< katex >}}1, -1, 1, -1, 1, -1, \ldots{{< /katex >}}

2. First term {{< katex >}}a{{< /katex >}} and common difference {{< katex >}}d{{< /katex >}} are given below. Find the corresponding A.P.
   - (i) {{< katex >}}a = 5, d = 6{{< /katex >}}
   - (ii) {{< katex >}}a = 7, d = -5{{< /katex >}}
   - (iii) {{< katex >}}a = \frac{3}{4}, d = \frac{1}{2}{{< /katex >}}

3. Find the first term and common difference of the Arithmetic Progressions whose {{< katex >}}n^{\text{th}}{{< /katex >}} terms are given below:
   - (i) {{< katex >}}t_n = -3 + 2n{{< /katex >}}
   - (ii) {{< katex >}}t_n = 4 - 7n{{< /katex >}}

4. Find the {{< katex >}}19^{\text{th}}{{< /katex >}} 
term of an A.P. {{< katex >}}-11, -15, -19, \ldots{{< /katex >}}

5. Which term of an A.P. {{< katex >}}16, 11, 6, 1, \ldots{{< /katex >}}
 is {{< katex >}}-54{{< /katex >}}?

6. Find the middle term(s) of an A.P. {{< katex >}}9, 15, 21, 27, \ldots, 183{{< /katex >}}.

7. If nine times ninth term is equal to the fifteen times fifteenth term, show that six times twenty fourth term is zero.

8. If {{< katex >}}3+k, 18-k, 5k+1{{< /katex >}}
 are in A.P. then find {{< katex >}}k{{< /katex >}}.

9. Find {{< katex >}}x, y{{< /katex >}} 
and {{< katex >}}z{{< /katex >}},
 given that the numbers {{< katex >}}x, 10, y, 24, z{{< /katex >}} are in A.P.

10. In a theatre, there are 20 seats in the front row and 30 rows were allotted. Each successive row contains two additional seats than its front row. How many seats are there in the last row?

11. The sum of three consecutive terms that are in A.P. is 27 and their product is 288. Find the three terms.

12. The ratio of {{< katex >}}6^{\text{th}}{{< /katex >}} 
and {{< katex >}}8^{\text{th}}{{< /katex >}} 
term of an A.P. is {{< katex >}}7:9{{< /katex >}}.
 Find the ratio of {{< katex >}}9^{\text{th}}{{< /katex >}}
  term to {{< katex >}}13^{\text{th}}{{< /katex >}} term.

13. In a winter season let us take the temperature of Ooty from Monday to Friday to be in A.P. The sum of temperatures from Monday to Wednesday is {{< katex >}}0^\circ\text{C}{{< /katex >}} 
and the sum of the temperatures from Wednesday to Friday is {{< katex >}}18^\circ\text{C}{{< /katex >}}. Find the temperature on each of the five days.

14. Priya earned ₹15,000 in the first month. Thereafter her salary increased by ₹1500 per year. Her expenses are ₹13,000 during the first month and the expenses increases by ₹900 per year. How long will it take for her to save ₹20,000 per month.

---
