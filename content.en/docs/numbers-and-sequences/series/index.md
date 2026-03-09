---
title: 'Series'
weight: 7
---
## 2.8 Series

The sum of the terms of a sequence is called **series**. Let {{< katex >}}a_1, a_2, a_3, \ldots, a_n, \ldots{{< /katex >}}
 be the sequence of real numbers. Then the real number {{< katex >}}a_1 + a_2 + a_3 + \cdots{{< /katex >}} is defined as the series of real numbers.

If a series has finite number of terms then it is called a **Finite series**. If a series has infinite number of terms then it is called an **Infinite series**. Let us focus our attention only on studying finite series.

### 2.8.1 Sum to {{< katex >}}n{{< /katex >}} terms of an A.P.

A series whose terms are in Arithmetic progression is called **Arithmetic series**.

Let {{< katex >}}a, a+d, a+2d, a+3d, \ldots{{< /katex >}} be the Arithmetic Progression.

The sum of first {{< katex >}}n{{< /katex >}}
 terms of a Arithmetic Progression denoted by {{< katex >}}S_n{{< /katex >}} is given by:
{{< katex >}}S_n = a + (a+d) + (a+2d) + \cdots + (a+(n-1)d) \quad \ldots(1){{< /katex >}}

Rewriting the above in reverse order:
{{< katex >}}S_n = (a+(n-1)d) + (a+(n-2)d) + \cdots + (a+d) + a \quad \ldots(2){{< /katex >}}

Adding (1) and (2) we get:
{{< katex >}}\begin{aligned}
2S_n &= [a + a + (n-1)d] + [a+d + a+(n-2)d] + \cdots + [a+(n-2)d + (a+d)] + [a+(n-1)d + a] \\
&= [2a + (n-1)d] + [2a + (n-1)d] + \cdots + [2a + (n-1)d] \quad \text{(n terms)} \\
2S_n &= n \times [2a + (n-1)d] \\
\implies S_n &= \frac{n}{2}[2a + (n-1)d]
\end{aligned} {{< /katex >}}


![](1.png)

**Example 2.31** Find the sum of first 15 terms of the A.P. {{< katex >}}8, 7\frac{1}{4}, 6\frac{1}{2}, 5\frac{3}{4}, \ldots{{< /katex >}}

**Solution:** Here the first term {{< katex >}}a = 8{{< /katex >}},
 common difference {{< katex >}}d = 7\frac{1}{4} - 8 = -\frac{3}{4}{{< /katex >}},

Sum of first {{< katex >}}n{{< /katex >}} 
terms of an A.P. {{< katex >}}S_n = \frac{n}{2}[2a + (n-1)d]{{< /katex >}}

{{< katex >}}\begin{aligned}
S_{15} &= \frac{15}{2}\left[2 \times 8 + (15-1)\left(-\frac{3}{4}\right)\right] \\
&= \frac{15}{2}\left[16 - \frac{21}{2}\right] = \frac{165}{4}
\end{aligned}{{< /katex >}}

**Example 2.32** Find the sum of {{< katex >}}0.40 + 0.43 + 0.46 + \cdots + 1{{< /katex >}}.

**Solution:** Here the value of {{< katex >}}n{{< /katex >}}
 is not given. But the last term is given. From this, we can find the value of {{< katex >}}n{{< /katex >}}.

Given, {{< katex >}}a = 0.40{{< /katex >}} 
and {{< katex >}}l = 1{{< /katex >}},
 we find {{< katex >}}d = 0.43 - 0.40 = 0.03{{< /katex >}}.

{{< katex >}}\begin{aligned}
\text{Therefore, } n &= \left(\frac{l-a}{d}\right) + 1 \\
&= \left(\frac{1-0.40}{0.03}\right) + 1 = 21
\end{aligned}{{< /katex >}}

Sum of first {{< katex >}}n{{< /katex >}} 
terms of an A.P. {{< katex >}}S_n = \frac{n}{2}[a + l]{{< /katex >}},
 {{< katex >}}n = 21{{< /katex >}}.

Therefore, {{< katex >}}S_{21} = \frac{21}{2}[0.40 + 1] = 14.7{{< /katex >}}

So, the sum of 21 terms of the given series is 14.7.

**Example 2.33** How many terms of the series {{< katex >}}1 + 5 + 9 + \ldots{{< /katex >}} must be taken so that their sum is 190?

**Solution:** Here we have to find the value of {{< katex >}}n{{< /katex >}},
 such that {{< katex >}}S_n = 190{{< /katex >}}

First term {{< katex >}}a = 1{{< /katex >}},
 common difference {{< katex >}}d = 5 - 1 = 4{{< /katex >}}.

Sum of first {{< katex >}}n{{< /katex >}} terms of an A.P.:
{{< katex >}}\begin{aligned}
S_n &= \frac{n}{2}[2a + (n-1)d] = 190 \\
\frac{n}{2}[2 \times 1 + (n-1) \times 4] &= 190 \\
n[4n - 2] &= 380 \\
2n^2 - n - 190 &= 0 \\
(n-10)(2n+19) &= 0
\end{aligned}{{< /katex >}}

But, {{< katex >}}n = 10{{< /katex >}}
 as {{< katex >}}n = -\frac{19}{2}{{< /katex >}}
  is impossible. Therefore, {{< katex >}}n = 10{{< /katex >}}.

> **Thinking Corner**
> The value of {{< katex >}}n{{< /katex >}} must be positive. Why?

**Progress Check**

State True or False. Justify it.
1. The {{< katex >}}n^{\text{th}}{{< /katex >}}
 term of any A.P. is of the form {{< katex >}}pn + q{{< /katex >}}
  where {{< katex >}}p{{< /katex >}}
   and {{< katex >}}q{{< /katex >}} are some constants.
2. The sum to {{< katex >}}n^{\text{th}}{{< /katex >}}
 term of any A.P. is of the form {{< katex >}}pn^2 + qn + r{{< /katex >}}
  where {{< katex >}}p, q, r{{< /katex >}} are some constants.

  ![](2.png)

**Example 2.34** The {{< katex >}}13^{\text{th}}{{< /katex >}} term of an A.P. is 3 and the sum of first 13 terms is 234. Find the common difference and the sum of first 21 terms.

**Solution:** Given, the {{< katex >}}13^{\text{th}}{{< /katex >}}
 term {{< katex >}}= 3{{< /katex >}}
  so, {{< katex >}}t_{13} = a + 12d = 3 \quad \ldots(1){{< /katex >}}

Sum of first 13 terms {{< katex >}}= 234 \implies S_{13} = \frac{13}{2}[2a + 12d] = 234 \quad \ldots(2){{< /katex >}}

Solving (1) and (2) we get, {{< katex >}}a = 33{{< /katex >}},
 {{< katex >}}d = \frac{-5}{2}{{< /katex >}}

Therefore, common difference is {{< katex >}}\frac{-5}{2}{{< /katex >}}.

Sum of first 21 terms:
{{< katex >}}S_{21} = \frac{21}{2}\left[2 \times 33 + (21-1)\left(-\frac{5}{2}\right)\right] = \frac{21}{2}[66 - 50] = 168{{< /katex >}}

**Example 2.35** In an A.P. the sum of first {{< katex >}}n{{< /katex >}}
 terms is {{< katex >}}\frac{5n^2}{2} + \frac{3n}{2}{{< /katex >}}.
  Find the {{< katex >}}17^{\text{th}}{{< /katex >}} term.

**Solution:** The {{< katex >}}17^{\text{th}}{{< /katex >}} term can be obtained by subtracting the sum of first 16 terms from the sum of first 17 terms.

Now:
{{< katex >}}\begin{aligned}
S_{17} &= \frac{5 \times (17)^2}{2} + \frac{3 \times 17}{2} = \frac{1445}{2} + \frac{51}{2} = 748 \\
S_{16} &= \frac{5 \times (16)^2}{2} + \frac{3 \times 16}{2} = \frac{1280}{2} + \frac{48}{2} = 664 \\
t_{17} &= S_{17} - S_{16} = 748 - 664 = 84
\end{aligned}{{< /katex >}}

**Example 2.36** Find the sum of all natural numbers between 300 and 600 which are divisible by 7.

**Solution:** The natural numbers between 300 and 600 which are divisible by 7 are {{< katex >}}301, 308, 315, \ldots, 595{{< /katex >}}.

The sum of all natural numbers between 300 and 600 is {{< katex >}}301 + 308 + 315 + \cdots + 595{{< /katex >}}.

The terms of the above series are in A.P.

First term {{< katex >}}a = 301{{< /katex >}};
 common difference {{< katex >}}d = 7{{< /katex >}};
  Last term {{< katex >}}l = 595{{< /katex >}}.

{{< katex >}}\begin{aligned}
n &= \left\lfloor\frac{l-a}{d}\right\rfloor + 1 = \left(\frac{595-301}{7}\right) + 1 = 43 \\
\therefore S_n &= \frac{n}{2}[a + l] \\
S_{43} &= \frac{43}{2}[301 + 595] = 19264
\end{aligned}{{< /katex >}}

**Example 2.37** A mosaic is designed in the shape of an equilateral triangle, 12ft on each side. Each tile in the mosaic is in the shape of an equilateral triangle of 12 inch side. The tiles are alternate in colour as shown in the figure. Find the number of tiles of each colour and total number of tiles in the mosaic.

![](3.png)

**Solution:** Since the mosaic is in the shape of an equilateral triangle of 12 feet, and the tile is in the shape of an equilateral triangle of 12 inch (1 feet), there will be 12 rows in the mosaic.

From the figure, it is clear that number of white tiles in each row are {{< katex >}}1, 2, 3, 4, \ldots, 12{{< /katex >}} which clearly forms an Arithmetic Progression.

Similarly the number of blue tiles in each row are {{< katex >}}0, 1, 2, 3, \ldots, 11{{< /katex >}} which is also an Arithmetic Progression.

Number of white tiles {{< katex >}}= 1 + 2 + 3 + \cdots + 12 = \frac{12}{2}[1 + 12] = 78{{< /katex >}}

Number of blue tiles {{< katex >}}= 0 + 1 + 2 + 3 + \cdots + 11 = \frac{12}{2}[0 + 11] = 66{{< /katex >}}

The total number of tiles in the mosaic {{< katex >}}= 78 + 66 = 144{{< /katex >}}

**Example 2.38** The houses of a street are numbered from 1 to 49. Senthil's house is numbered such that the sum of numbers of the houses prior to Senthil's house is equal to the sum of numbers of the houses following Senthil's house. Find Senthil's house number?

**Solution:** Let Senthil's house number be {{< katex >}}x{{< /katex >}}.

It is given that:
{{< katex >}}\begin{aligned}
1 + 2 + 3 + \cdots + (x-1) &= (x+1) + (x+2) + \cdots + 49 \\
1 + 2 + 3 + \cdots + (x-1) &= [1 + 2 + 3 + \cdots + 49] - [1 + 2 + 3 + \cdots + x] \\
\frac{x-1}{2}[1 + (x-1)] &= \frac{49}{2}[1 + 49] - \frac{x}{2}[1 + x] \\
\frac{x(x-1)}{2} &= \frac{49 \times 50}{2} - \frac{x(x+1)}{2} \\
x^2 - x &= 2450 - x^2 - x \implies 2x^2 = 2450 \\
x^2 &= 1225 \implies x = 35
\end{aligned}{{< /katex >}}

Therefore, Senthil's house number is 35.

**Example 2.39** The sum of first {{< katex >}}n{{< /katex >}},
 {{< katex >}}2n{{< /katex >}}
  and {{< katex >}}3n{{< /katex >}}
   terms of an A.P. are {{< katex >}}S_1, S_2{{< /katex >}}
    and {{< katex >}}S_3{{< /katex >}}
     respectively. Prove that {{< katex >}}S_3 = 3(S_2 - S_1){{< /katex >}}.

**Solution:** If {{< katex >}}S_1, S_2{{< /katex >}}
 and {{< katex >}}S_3{{< /katex >}}
  are sum of first {{< katex >}}n, 2n{{< /katex >}}
   and {{< katex >}}3n{{< /katex >}} terms of an A.P. respectively then:
{{< katex >}}\begin{aligned}
S_1 &= \frac{n}{2}[2a + (n-1)d] \\
S_2 &= \frac{2n}{2}[2a + (2n-1)d] \\
S_3 &= \frac{3n}{2}[2a + (3n-1)d]
\end{aligned}{{< /katex >}}

Consider:
{{< katex >}}\begin{aligned}
S_2 - S_1 &= \frac{2n}{2}[2a + (2n-1)d] - \frac{n}{2}[2a + (n-1)d] \\
&= \frac{n}{2}[[2a + 2(2n-1)d] - [2a + (n-1)d]] \\
S_2 - S_1 &= \frac{n}{2} \times [2a + (3n-1)d]
\end{aligned}{{< /katex >}}

Hence {{< katex >}}3(S_2 - S_1) = \frac{3n}{2}[2a + (3n-1)d] = S_3{{< /katex >}}

---

![](4.png)

1. Find the sum of the following:
   - (i) {{< katex >}}3, 7, 11, \ldots{{< /katex >}} up to 40 terms.
   - (ii) {{< katex >}}102, 97, 92, \ldots{{< /katex >}} up to 27 terms.
   - (iii) {{< katex >}}6 + 13 + 20 + \cdots + 97{{< /katex >}}

2. How many consecutive odd integers beginning with 5 will sum to 480?

3. Find the sum of first 28 terms of an A.P. whose {{< katex >}}n^{\text{th}}{{< /katex >}}
 term is {{< katex >}}4 - 3n{{< /katex >}}.

4. The sum of first {{< katex >}}n{{< /katex >}}
 terms of a certain series is given as {{< katex >}}2n^2 - 3n{{< /katex >}}. Show that the series is an A.P.

5. The {{< katex >}}104^{\text{th}}{{< /katex >}}
 term and {{< katex >}}4^{\text{th}}{{< /katex >}} term of an A.P. are 125 and 0. Find the sum of first 35 terms.

6. Find the sum of all odd positive integers less than 450.

7. Find the sum of all natural numbers between 602 and 902 which are not divisible by 4.

8. An IT company organizes a sports meet, the winner of the competition gets ₹4800 in the first month, ₹4750 in the second month, ₹4700 in the third month and so on. If he pays the money in this fashion, find:
   - (i) total amount paid in 10 installments.
   - (ii) how much extra amount that he has to pay than the cost?

9. A man repays a loan of ₹65,000 by paying ₹400 in the first month and then increasing the payment by ₹300 every month. How long will it take for him to clear the loan?

10. A brick staircase has a total of 30 steps. The bottom step requires 100 bricks. Each successive step requires two bricks less than the previous step.
    - (i) How many bricks are required for the top most step?
    - (ii) How many bricks are required to build the stair case?

11. If {{< katex >}}S_1, S_2, S_3, \ldots, S_m{{< /katex >}}
 are the sums of {{< katex >}}n{{< /katex >}} 
 terms of {{< katex >}}m{{< /katex >}}
  A.P.'s whose first terms are {{< katex >}}1, 2, 3, \ldots, m{{< /katex >}}
   and whose common differences are {{< katex >}}1, 3, 5, \ldots, (2m-1){{< /katex >}} respectively, then show that:
{{< katex >}}S_1 + S_2 + S_3 + \cdots + S_m = \frac{1}{2}mn(mn + 1){{< /katex >}}

12. Find the sum {{< katex >}}\left[\frac{a-b}{a+b} + \frac{3a-2b}{a+b} + \frac{5a-3b}{a+b} + \cdots \text{to 12 terms}\right]{{< /katex >}}.

---