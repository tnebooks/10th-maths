---
title: 'Sequences'
weight: 5
---

## 2.6 Sequences

Consider the following pictures.

![Fig. 2.9 - Sequences in nature](sequences.png)

There is some pattern or arrangement in these pictures. In the first picture, the first row contains one apple, the second row contains two apples and in the third row there are three apples etc... The number of apples in each of the rows are {{< katex >}}1, 2, 3, \ldots{{< /katex >}}.


In the second picture each step have 0.5 feet height. The total height of the steps from the base are {{< katex >}}0.5{{< /katex >}} 
feet, {{< katex >}}1{{< /katex >}}
 feet, {{< katex >}}1.5{{< /katex >}} feet, ... In the third picture one square, 3 squares, 5 squares, ... These numbers belong to category called **"Sequences"**.

### Definition

A real valued sequence is a function defined on the set of natural numbers and taking real values.

Each element in the sequence is called a **term** of the sequence. The element in the first position is called the **first term** of the sequence. The element in the second position is called **second term** of the sequence and so on.

If the {{< katex >}}n^{\text{th}}{{< /katex >}} 
term is denoted by {{< katex >}}a_n{{< /katex >}},
 then {{< katex >}}a_1{{< /katex >}} 
 is the first term, {{< katex >}}a_2{{< /katex >}} is the second term, and so on.

A sequence can be written as {{< katex >}}a_1, a_2, a_3, \ldots, a_n, \ldots{{< /katex >}}

### Illustration

1. {{< katex >}}1, 3, 5, 7, \ldots{{< /katex >}} 
is a sequence with general term {{< katex >}}a_n = 2n - 1{{< /katex >}}.
 When we put {{< katex >}}n = 1, 2, 3, \ldots{{< /katex >}},
  we get {{< katex >}}a_1 = 1, a_2 = 3, a_3 = 5, a_4 = 7, \ldots{{< /katex >}}

2. {{< katex >}}\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}, \ldots{{< /katex >}}
 is a sequence with general term {{< katex >}}\frac{1}{n+1}{{< /katex >}}.
  When we put {{< katex >}}n = 1, 2, 3, \ldots{{< /katex >}},
   we get {{< katex >}}a_1 = \frac{1}{2}, a_2 = \frac{1}{3}, a_3 = \frac{1}{4}, a_4 = \frac{1}{5}, \ldots{{< /katex >}}

If the number of elements in a sequence is finite then it is called a **Finite sequence**. If the number of elements in a sequence is infinite then it is called an **Infinite sequence**.

### Sequence as a Function

A sequence can be considered as a function defined on the set of natural numbers {{< katex >}}\mathbb{N}{{< /katex >}}.
 In particular, a sequence is a function {{< katex >}}f: \mathbb{N} \to \mathbb{R}{{< /katex >}}
  where {{< katex >}}\mathbb{R}{{< /katex >}} is the set of all real numbers.
  ![](6.png)

If the sequence is of the form {{< katex >}}a_1, a_2, a_3, \ldots{{< /katex >}}
 by then we can associate the function to the sequence {{< katex >}}a_1, a_2, a_3, \ldots{{< /katex >}}
  by {{< katex >}}f(k) = a_k{{< /katex >}},
   {{< katex >}}k = 1, 2, 3, \ldots{{< /katex >}}


> **Note**
> Though all the sequences are functions, not all the functions are sequences.

**Progress Check**
1. Fill in the blanks for the following sequences:
   - (i) {{< katex >}}7, 13, 19, \_\_\_\_\_, \ldots{{< /katex >}}
   - (ii) {{< katex >}}2, \_\_\_\_\_, 10, 17, 26, \ldots{{< /katex >}}
   - (iii) {{< katex >}}1000, 100, 10, 1, \_\_\_\_\_, \ldots{{< /katex >}}

2. A sequence is a function defined on the set of _____.

3. The {{< katex >}}n^{\text{th}}{{< /katex >}}
 term of the sequence {{< katex >}}\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots{{< /katex >}} can be expressed as _____.

4. Say True or False:
   - (i) All sequences are functions
   - (ii) All functions are sequences.

**Example 2.19** Find the next three terms of the sequences:
- (i) {{< katex >}}\frac{1}{12}, \frac{1}{6}, \frac{1}{10}, \frac{1}{14}, \ldots{{< /katex >}}
- (ii) {{< katex >}}5, 2, -1, -4, \ldots{{< /katex >}}
- (iii) {{< katex >}}1, 0.1, 0.01, \ldots{{< /katex >}}

**Solution:**

![](1.png)

In the above sequence the numerators are same and the denominator is increased by 4.

So the next three terms are:
{{< katex >}}\begin{aligned}
a_5 &= \frac{1}{14 + 4} = \frac{1}{18} \\
a_6 &= \frac{1}{18 + 4} = \frac{1}{22} \\
a_7 &= \frac{1}{22 + 4} = \frac{1}{26}
\end{aligned}{{< /katex >}}

![](2.png)

Here each term is decreased by 3. So the next three terms are {{< katex >}}-7, -10, -13{{< /katex >}}.

![](3.png)

Here each term is divided by 10. Hence, the next three terms are:
{{< katex >}}\begin{aligned}
a_4 &= \frac{0.01}{10} = 0.001 \\
a_5 &= \frac{0.001}{10} = 0.0001 \\
a_6 &= \frac{0.0001}{10} = 0.00001
\end{aligned}{{< /katex >}}

**Example 2.20** Find the general term for the following sequences:
- (i) {{< katex >}}3, 6, 9, \ldots{{< /katex >}}
- (ii) {{< katex >}}\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots{{< /katex >}}
- (iii) {{< katex >}}5, -25, 125, \ldots{{< /katex >}}

**Solution:**

**(i)** {{< katex >}}3, 6, 9, \ldots{{< /katex >}}

Here the terms are multiples of 3. So the general term is {{< katex >}}a_n = 3n{{< /katex >}}, 
{{< katex >}}n \in \mathbb{N}{{< /katex >}}

**(ii)** {{< katex >}}\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots{{< /katex >}}

We see that the numerator of {{< katex >}}n^{\text{th}}{{< /katex >}}
 term is {{< katex >}}n{{< /katex >}}, and the denominator is one more than the numerator. Hence:
{{< katex >}}a_n = \frac{n}{n+1}, \quad n \in \mathbb{N}{{< /katex >}}

**(iii)** {{< katex >}}5, -25, 125, \ldots{{< /katex >}}

The terms of the sequence have {{< katex >}}+{{< /katex >}} 
and {{< katex >}}-{{< /katex >}} sign alternatively and also they are in powers of 5.

So the general term:
{{< katex >}}a_n = (-1)^{n+1} 5^n, \quad n \in \mathbb{N}{{< /katex >}}

**Example 2.21** The general term of a sequence is defined as:
![](4.png)

Find the eleventh and eighteenth terms.

**Solution:** To find {{< katex >}}a_{11}{{< /katex >}},
 since 11 is odd, we put {{< katex >}}n = 11{{< /katex >}} 
 in {{< katex >}}a_n = \frac{n(n+3)}{2}{{< /katex >}}:
{{< katex >}}a_{11} = \frac{11 \times 14}{2} = 77{{< /katex >}}

To find {{< katex >}}a_{18}{{< /katex >}}, 
since 18 is even, we put {{< katex >}}n = 18{{< /katex >}} 
in {{< katex >}}a_n = \frac{n^2+1}{2}{{< /katex >}}:
{{< katex >}}a_{18} = \frac{18^2 + 1}{2} = \frac{325}{2} = 162.5{{< /katex >}}

**Example 2.22** Find the first five terms of the following sequence.
{{< katex >}}a_1 = 1, a_2 = 1, a_n = \frac{a_{n-1}}{a_{n-2} + 3}, \quad n \geq 3, n \in \mathbb{N}{{< /katex >}}

**Solution:** The first two terms of this sequence are given by {{< katex >}}a_1 = 1, a_2 = 1{{< /katex >}}.
 The third term {{< katex >}}a_3{{< /katex >}} depends on the first and second terms.

{{< katex >}}a_3 = \frac{a_{3-1}}{a_{3-2} + 3} = \frac{a_2}{a_1 + 3} = \frac{1}{1 + 3} = \frac{1}{4}{{< /katex >}}

Similarly the fourth term {{< katex >}}a_4{{< /katex >}} 
depends upon {{< katex >}}a_3{{< /katex >}} 
and {{< katex >}}a_2{{< /katex >}}:
{{< katex >}}a_4 = \frac{a_{4-1}}{a_{4-2} + 3} = \frac{a_3}{a_2 + 3} = \frac{\frac{1}{4}}{1 + 3} = \frac{\frac{1}{4}}{4} = \frac{1}{4} \times \frac{1}{4} = \frac{1}{16}{{< /katex >}}

In the same way, the fifth term {{< katex >}}a_5{{< /katex >}} can be calculated as:
{{< katex >}}a_5 = \frac{a_{5-1}}{a_{5-2} + 3} = \frac{a_4}{a_3 + 3} = \frac{\frac{1}{16}}{\frac{1}{4} + 3} = \frac{1}{16} \times \frac{4}{13} = \frac{1}{52}{{< /katex >}}

Therefore, the first five terms of the sequence are {{< katex >}}1, 1, \frac{1}{4}, \frac{1}{16}, \frac{1}{52}{{< /katex >}}.

---
![](5.png)

1. Find the next three terms of the following sequence.
   - (i) {{< katex >}}8, 24, 72, \ldots{{< /katex >}}
   - (ii) {{< katex >}}5, 1, -3, \ldots{{< /katex >}}
   - (iii) {{< katex >}}\frac{1}{4}, \frac{2}{9}, \frac{3}{16}, \ldots{{< /katex >}}

2. Find the first four terms of the sequences whose {{< katex >}}n^{\text{th}}{{< /katex >}} terms are given by:
   - (i) {{< katex >}}a_n = n^3 - 2{{< /katex >}}
   - (ii) {{< katex >}}a_n = (-1)^{n+1} n(n+1){{< /katex >}}
   - (iii) {{< katex >}}a_n = \frac{n^2 - 6}{2}{{< /katex >}}

3. Find the {{< katex >}}n^{\text{th}}{{< /katex >}} term of the following sequences:
   - (i) {{< katex >}}2, 5, 10, 17, \ldots{{< /katex >}}
   - (ii) {{< katex >}}0, \frac{1}{2}, \frac{2}{3}, \ldots{{< /katex >}}
   - (iii) {{< katex >}}3, 8, 13, 18, \ldots{{< /katex >}}

4. Find the indicated terms of the sequences whose {{< katex >}}n^{\text{th}}{{< /katex >}} terms are given by:
   - (i) {{< katex >}}a_n = \frac{5n}{n+2}{{< /katex >}};
    {{< katex >}}a_6{{< /katex >}}
     and {{< katex >}}a_{13}{{< /katex >}}
   - (ii) {{< katex >}}a_n = -(n^2 - 4){{< /katex >}};
    {{< katex >}}a_4{{< /katex >}},
     {{< katex >}}a_{11}{{< /katex >}}
      and {{< katex >}}a_{20}{{< /katex >}}

5. Find {{< katex >}}a_8{{< /katex >}}
 and {{< katex >}}a_{15}{{< /katex >}}
  whose {{< katex >}}n^{\text{th}}{{< /katex >}} term is:
{{< katex >}}a_n = \begin{cases} \frac{n^2 - 1}{n+3} & ; \quad n \text{ is even}, \quad n \in \mathbb{N} \\ \frac{n^2}{2n+1} & ; \quad n \text{ is odd}, \quad n \in \mathbb{N} \end{cases}{{< /katex >}}

6. If {{< katex >}}a_1 = 1, a_2 = 1{{< /katex >}} 
and {{< katex >}}a_n = a_{n-1} + a_{n-2}, \quad n \geq 3, n \in \mathbb{N}{{< /katex >}}, then find the first six terms of the sequence.

---

