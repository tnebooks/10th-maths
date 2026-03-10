---
title: 'Euclids Division Algorithm'
weight: 2
---
## 2.3 Euclid's Division Algorithm

In the previous section, we have studied about Euclid's division lemma and its applications. We now study the concept Euclid's Division Algorithm. The word 'algorithm' comes from the name of 9th century Persian Mathematician Al-khwarizmi. An algorithm means a series of methodical step-by-step procedure of calculating successively on the results of earlier steps till the desired answer is obtained.

Euclid's division algorithm provides an easier way to compute the Highest Common Factor (HCF) of two given positive integers.

### Theorem 2

If {{< katex >}}a{{< /katex >}} 
and {{< katex >}}b{{< /katex >}}
 are positive integers such that {{< katex >}}a = bq + r{{< /katex >}},
  then every common divisor of {{< katex >}}a{{< /katex >}} 
  and {{< katex >}}b{{< /katex >}}
   is a common divisor of {{< katex >}}b{{< /katex >}}
    and {{< katex >}}r{{< /katex >}} and vice-versa.

### Euclid's Division Algorithm

To find Highest Common Factor of two positive integers {{< katex >}}a{{< /katex >}} 
and {{< katex >}}b{{< /katex >}},
 where {{< katex >}}a \gt b{{< /katex >}}:

**Step 1:** Using Euclid's division lemma {{< katex >}}a = bq + r{{< /katex >}};
 {{< katex >}}0 \leq r \lt b{{< /katex >}}. 
 where {{< katex >}}q{{< /katex >}} 
 is the quotient, {{< katex >}}r{{< /katex >}} 
 is the remainder. If {{< katex >}}r = 0{{< /katex >}} 
 then {{< katex >}}b{{< /katex >}}
  is the Highest Common Factor of {{< katex >}}a{{< /katex >}} 
  and {{< katex >}}b{{< /katex >}}.

**Step 2:** Otherwise applying Euclid's division lemma divide {{< katex >}}b{{< /katex >}}
 by {{< katex >}}r{{< /katex >}} 
 to get {{< katex >}}b = rq_1 + r_1{{< /katex >}}; 
 {{< katex >}}0 \leq r_1 \lt r{{< /katex >}}

**Step 3:** If {{< katex >}}r_1 = 0{{< /katex >}} 
then {{< katex >}}r{{< /katex >}}
 is the Highest common factor of {{< katex >}}a{{< /katex >}} 
 and {{< katex >}}b{{< /katex >}}.

**Step 4:** Otherwise using Euclid's division lemma, repeat the process until we get the remainder zero. In that case, the corresponding divisor is the HCF of {{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}}.

 **Note**
 - The above algorithm will always produce remainder zero at some stage. Hence the algorithm should terminate.
 - Euclid's Division Algorithm is a repeated application of Division Lemma until we get zero remainder.
 - Highest Common Factor (HCF) of two positive numbers is denoted by {{< katex >}}(a,b){{< /katex >}}.
 - Highest Common Factor (HCF) is also called as Greatest Common Divisor (GCD).

---

### Progress Check

1. Euclid's division algorithm is a repeated application of division lemma until we get remainder as _____.
2. The HCF of two equal positive integers {{< katex >}}k, k{{< /katex >}} is _____.

---

### Illustration 1

Using the above Algorithm, let us find HCF of two given positive integers. Let {{< katex >}}a = 273{{< /katex >}}
 and {{< katex >}}b = 119{{< /katex >}}
  be the two given positive integers such that {{< katex >}}a \gt b{{< /katex >}}.

We start dividing 273 by 119 using Euclid's division lemma.

We get, {{< katex >}}273 = 119 \times 2 + 35{{< /katex >}} ... (1)

The remainder is {{< katex >}}35 \neq 0{{< /katex >}}.

Therefore, applying Euclid's Division Algorithm to the divisor 119 and remainder 35, we get:

{{< katex >}}119 = 35 \times 3 + 14{{< /katex >}} ... (2)

The remainder is {{< katex >}}14 \neq 0{{< /katex >}}.

Applying Euclid's Division Algorithm to the divisor 35 and remainder 14.

We get {{< katex >}}35 = 14 \times 2 + 7{{< /katex >}} ... (3)

The remainder is {{< katex >}}7 \neq 0{{< /katex >}}.

Applying Euclid's Division Algorithm to the divisor 14 and remainder 7.

We get {{< katex >}}14 = 7 \times 2 + 0{{< /katex >}}

The remainder at this stage = 0.
The divisor at this stage = 7.

Therefore, Highest Common Factor of 273, 119 = **7**.

---

### Example 2.4

If the Highest Common Factor of 210 and 55 is expressible in the form {{< katex >}}55x - 325{{< /katex >}},
 find {{< katex >}}x{{< /katex >}}.

**Solution:** Using Euclid's Division Algorithm, let us find the HCF of given numbers

{{< katex >}}\begin{aligned}
210 &= 55 \times 3 + 45 \\
55 &= 45 \times 1 + 10 \\
45 &= 10 \times 4 + 5 \\
10 &= 5 \times 2 + 0 \\
\end{aligned}{{</ katex >}}

The remainder is zero. So, the last divisor **5** is the Highest Common Factor (HCF) of 210 and 55.

HCF is expressible in the form {{< katex >}}55x - 325 = 5{{< /katex >}}

{{< katex >}}\begin{aligned}
\implies 55x &= 330 \\
x &= 6 \\
\end{aligned}{{</ katex >}}

---

### Example 2.5

Find the greatest number that will divide 445 and 572 leaving remainders 4 and 5 respectively.

**Solution:** Since the remainders are 4, 5 respectively the required number is the HCF of the number {{< katex >}}445 - 4 = 441{{< /katex >}},
 {{< katex >}}572 - 5 = 567{{< /katex >}}.

Hence, we will determine the HCF of 441 and 567. Using Euclid's Division Algorithm, we have:

{{< katex >}}\begin{aligned}
567 &= 441 \times 1 + 126 \\
441 &= 126 \times 3 + 63 \\
126 &= 63 \times 2 + 0 \\
\end{aligned}{{</ katex >}}

Therefore, HCF of {{< katex >}}[441, 567 = 63]{{< /katex >}} and so the required number is **63**.

---

### Activity 1

This activity helps you to find HCF of two positive numbers. We first observe the following instructions.

(i) Construct a rectangle whose length and breadth are the given numbers.
(ii) Try to fill the rectangle using small squares.
(iii) Try with {{< katex >}}1 \times 1{{< /katex >}} 
square; Try with {{< katex >}}2 \times 2{{< /katex >}}
 square; Try with {{< katex >}}3 \times 3{{< /katex >}} square and so on.
(iv) The side of the largest square that can fill the whole rectangle without any gap will be HCF of the given numbers.
(v) Find the HCF of (a) 12, 20 (b) 16, 24 (c) 11, 9

### Theorem 3

If {{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}}
  are two positive integers with {{< katex >}}a \gt b{{< /katex >}}
   then G.C.D of {{< katex >}}(a,b){{< /katex >}}
    = G.C.D of {{< katex >}}(a-b, b){{< /katex >}}.

### Activity 2

This is another activity to determine HCF of two given positive integers.

(i) From the given numbers, subtract the smaller from the larger number.
(ii) From the remaining numbers, subtract smaller from the larger.
(iii) Repeat the subtraction process by subtracting smaller from the larger.
(iv) Stop the process, when the numbers become equal.
(v) The number representing equal numbers obtained in step (iv), will be the HCF of the given numbers.

Using this Activity, find the HCF of:
- (i) 90, 15
- (ii) 80, 25
- (iii) 40, 16
- (iv) 23, 12
- (v) 93, 13

---

## Highest Common Factor of three numbers

We can apply Euclid's Division Algorithm twice to find the Highest Common Factor (HCF) of three positive integers using the following procedure.

Let {{< katex >}}a, b, c{{< /katex >}} be the given positive integers.

(i) Find HCF of {{< katex >}}a, b{{< /katex >}}.
 Call it as {{< katex >}}d = (a, b){{< /katex >}}
(ii) Find HCF of {{< katex >}}d{{< /katex >}} 
and {{< katex >}}c{{< /katex >}}.

This will be the HCF of the three given numbers {{< katex >}}a, b, c{{< /katex >}}

### Example 2.6

Find the HCF of 396, 504, 636.

**Solution:** To find HCF of three given numbers, first we have to find HCF of the first two numbers.

**To find HCF of 396 and 504:**

Using Euclid's division algorithm we get {{< katex >}}504 = 396 \times 1 + 108{{< /katex >}}

The remainder is {{< katex >}}108 \neq 0{{< /katex >}}

Again applying Euclid's division algorithm {{< katex >}}396 = 108 \times 3 + 72{{< /katex >}}

The remainder is {{< katex >}}72 \neq 0{{< /katex >}},

Again applying Euclid's division algorithm {{< katex >}}108 = 72 \times 1 + 36{{< /katex >}}

The remainder is {{< katex >}}36 \neq 0{{< /katex >}},

Again applying Euclid's division algorithm {{< katex >}}72 = 36 \times 2 + 0{{< /katex >}}

Here the remainder is zero. Therefore HCF of {{< katex >}}396, 504 = 36{{< /katex >}}.

**To find the HCF of 636 and 36:**

Using Euclid's division algorithm we get {{< katex >}}636 = 36 \times 17 + 24{{< /katex >}}

The remainder is {{< katex >}}24 \neq 0{{< /katex >}}

Again applying Euclid's division algorithm {{< katex >}}36 = 24 \times 1 + 12{{< /katex >}}

The remainder is {{< katex >}}12 \neq 0{{< /katex >}}

Again applying Euclid's division algorithm {{< katex >}}24 = 12 \times 2 + 0{{< /katex >}}

Here the remainder is zero. Therefore HCF of {{< katex >}}636, 36 = 12{{< /katex >}}

Therefore Highest Common Factor of 396, 504 and 636 is **12**.

---

 Two positive integers are said to be relatively prime or co prime if their Highest Common Factor is 1.

---

## Exercise 2.1

1. Find all positive integers, when divided by 3 leaves remainder 2.

2. A man has 532 flower pots. He wants to arrange them in rows such that each row contains 21 flower pots. Find the number of completed rows and how many flower pots are left over.

3. Prove that the product of two consecutive positive integers is divisible by 2.

4. When the positive integers {{< katex >}}a, b{{< /katex >}} 
and {{< katex >}}c{{< /katex >}} 
are divided by 13, the respective remainders are 9, 7 and 10. Show that {{< katex >}}a+b+c{{< /katex >}} is divisible by 13.

5. Prove that square of any integer leaves the remainder either 0 or 1 when divided by 4.

6. Use Euclid's Division Algorithm to find the Highest Common Factor (HCF) of:
   - (i) 340 and 412
   - (ii) 867 and 255
   - (iii) 10224 and 9648
   - (iv) 84, 90 and 120

7. Find the largest number which divides 1230 and 1926 leaving remainder 12 in each case.

8. If {{< katex >}}d{{< /katex >}} 
is the Highest Common Factor of 32 and 60, find {{< katex >}}x{{< /katex >}} 
and {{< katex >}}y{{< /katex >}}
 satisfying {{< katex >}}d = 32x + 60y{{< /katex >}}.

9. A positive integer when divided by 88 gives the remainder 61. What will be the remainder when the same number is divided by 11?

10. Prove that two consecutive positive integers are always coprime.

---
