---
title: 'Fundamental Theorem of Arithmetic'
weight: 3
---

## 2.4 Fundamental Theorem of Arithmetic

Let us consider the following conversation between a Teacher and students.

**Teacher:** Factorise the number 240.
- **Malar:** {{< katex >}}24 \times 10{{< /katex >}}
- **Raghu:** {{< katex >}}8 \times 30{{< /katex >}}
- **Iniya:** {{< katex >}}12 \times 20{{< /katex >}}
- **Kumar:** {{< katex >}}15 \times 16{{< /katex >}}

**Malar:** Whose answer is correct Sir?
**Teacher:** All the answers are correct.
**Raghu:** How sir?
**Teacher:** Split each of the factors into product of prime numbers.
- **Malar:** {{< katex >}}2 \times 2 \times 2 \times 3 \times 2 \times 5{{< /katex >}}
- **Raghu:** {{< katex >}}2 \times 2 \times 2 \times 2 \times 3 \times 5{{< /katex >}}
- **Iniya:** {{< katex >}}2 \times 2 \times 3 \times 2 \times 2 \times 5{{< /katex >}}
- **Kumar:** {{< katex >}}3 \times 5 \times 2 \times 2 \times 2 \times 2{{< /katex >}}

**Teacher:** Good! Now, count the number of 2's, 3's and 5's.
- **Malar:** I got four 2's, one 3 and one 5.
- **Raghu:** I got four 2's, one 3 and one 5.
- **Iniya:** I also got the same numbers too.
- **Kumar:** Me too sir.

**Malar:** All of us got four 2's, one 3 and one 5. This is very surprising to us.
**Teacher:** Yes, It should be. Once any number is factorized up to a product of prime numbers, everyone should get the same collection of prime numbers.

This concept leads us to the following important theorem.

---

### Theorem 4 (Fundamental Theorem of Arithmetic) (without proof)

 "Every positive integer (except the number 1) can be represented in exactly one way apart from rearrangement as a product of one or more primes."

The fundamental theorem asserts that every composite number can be decomposed as a product of prime numbers and that the decomposition is unique. In the sense that there is one and only way to express the decomposition as product of primes.

In general, we conclude that given a composite number {{< katex >}}N{{< /katex >}}, we decompose it uniquely in the form:

![Prime Factorization Tree Fig. 2.2](fundamental.png)

{{< katex >}}N = p_1^{q_1} \times p_2^{q_2} \times p_3^{q_3} \times \cdots \times p_n^{q_n}{{< /katex >}}

where {{< katex >}}p_1, p_2, p_3, ..., p_n{{< /katex >}}
 are primes and {{< katex >}}q_1, q_2, q_3, \ldots, q_n{{< /katex >}} are natural numbers.

First, we try to factorize {{< katex >}}N{{< /katex >}} into its factors. If all the factors are themselves primes then we can stop. Otherwise, we try to further split the factors which are not prime. Continue the process till we get only prime numbers.

 **Thinking Corner**
 Is 1 a prime number?

---

### Progress Check

1. Every natural number except ______ can be expressed as ______.
2. In how many ways a composite number can be written as product of power of primes?
3. The number of divisors of any prime number is ______.

---

### Illustration

For example, if we try to factorize 32760 we get:

{{< katex >}}32760 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 13 = 2^3 \times 3^2 \times 5^1 \times 7^1 \times 13^1{{< /katex >}}

Thus, in whatever way we try to factorize 32760, we should finally get three 2's, two 3's, one 5, one 7 and one 13.

The fact that "Every composite number can be written uniquely as the product of power of primes" is called **Fundamental Theorem of Arithmetic**.

---

### 2.4.1 Significance of the Fundamental Theorem of Arithmetic

The fundamental theorem about natural numbers except 1, that we have stated above has several applications, both in Mathematics and in other fields. The theorem is vastly important in Mathematics, since it highlights the fact that prime numbers are the 'Building Blocks' for all the positive integers. Thus, prime numbers can be compared to atoms making up a molecule.

---

 **KNOW?**
 1. If a prime number {{< katex >}}p{{< /katex >}} 
divides {{< katex >}}ab{{< /katex >}}
 then either {{< katex >}}p{{< /katex >}} 
 divides {{< katex >}}a{{< /katex >}}
  or {{< katex >}}p{{< /katex >}}
   divides {{< katex >}}b{{< /katex >}}
    that is {{< katex >}}p{{< /katex >}} divides at least one of them.
 2. If a composite number {{< katex >}}n{{< /katex >}}
 divides {{< katex >}}ab{{< /katex >}},
  then {{< katex >}}n{{< /katex >}} 
  neither divide {{< katex >}}a{{< /katex >}} 
  nor {{< katex >}}b{{< /katex >}}.
   For example, 6 divides {{< katex >}}4 \times 3{{< /katex >}} but 6 neither divide 4 nor 3.

---

### Example 2.7

In the given factorisation, find the numbers {{< katex >}}m{{< /katex >}} 
and {{< katex >}}n{{< /katex >}}.

![Factorization Diagram Fig. 2.3](image_4.png)

**Solution:**

Value of the first box from bottom {{< katex >}}= 5 \times 2 = 10{{< /katex >}}

{{< katex >}}n = 5 \times 10 = 50{{< /katex >}}

Value of the second box from bottom {{< katex >}}= 3 \times 50 = 150{{< /katex >}}

Value of {{< katex >}}m = 2 \times 150 = 300{{< /katex >}}

Thus, the required numbers are {{< katex >}}m = 300{{< /katex >}},
 {{< katex >}}n = 50{{< /katex >}}

---

### Example 2.8

Can the number {{< katex >}}6^n{{< /katex >}},
 {{< katex >}}n{{< /katex >}} being a natural number end with the digit 5? Give reason for your answer.

**Solution:** Since {{< katex >}}6^n = (2 \times 3)^n = 2^n \times 3^n{{< /katex >}}

{{< katex >}}6^n{{< /katex >}}
 is always even for any natural number {{< katex >}}n{{< /katex >}}.

But any number whose last digit is 5 is always odd.

Hence, {{< katex >}}6^n{{< /katex >}} **cannot** end with the digit 5.

---

### Example 2.9

Is {{< katex >}}7 \times 5 \times 3 \times 2 + 3{{< /katex >}} a composite number? Justify your answer.

**Solution:** Yes, the given number is a composite number, because:

{{< katex >}}7 \times 5 \times 3 \times 2 + 3 = 3 \times (7 \times 5 \times 2 + 1) = 3 \times 71{{< /katex >}}

Since the given number can be factorized in terms of two primes, it is a composite number.

---

### Progress Check

1. Let {{< katex >}}m{{< /katex >}}
 divides {{< katex >}}n{{< /katex >}}.
  Then GCD and LCM of {{< katex >}}m, n{{< /katex >}} are ____ and ____.
2. The HCF of numbers of the form {{< katex >}}2^m{{< /katex >}} 
and {{< katex >}}3^n{{< /katex >}} is _____.

---

### Example 2.10

{{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}} 
 are two positive integers such that {{< katex >}}a^b \times b^a = 800{{< /katex >}}.
  Find {{< katex >}}a{{< /katex >}} 
  and {{< katex >}}b{{< /katex >}}.

**Solution:** The number 800 can be factorized as:

{{< katex >}}800 = 2 \times 2 \times 2 \times 2 \times 2 \times 5 \times 5 = 2^5 \times 5^2{{< /katex >}}

Hence, {{< katex >}}a^b \times b^a = 2^5 \times 5^2{{< /katex >}}

This implies that {{< katex >}}a = 2{{< /katex >}}
 and {{< katex >}}b = 5{{< /katex >}}
  (or) {{< katex >}}a = 5{{< /katex >}}
   and {{< katex >}}b = 2{{< /katex >}}.

 **Thinking Corner**
 Can you think of positive integers {{< katex >}}a, b{{< /katex >}}
 such that {{< katex >}}a^b = b^a{{< /katex >}}?

---

### Activity 3

Can you find the 4-digit pin number 'pqrs' of an ATM card such that:

{{< katex >}}p^2 \times q^1 \times r^4 \times s^3 = 3,15,000{{< /katex >}}

![ATM Card Activity Fig. 2.4](image_5.png)

## Exercise 2.2

1. For what values of natural number {{< katex >}}n{{< /katex >}},
 {{< katex >}}4^n{{< /katex >}} can end with the digit 6?

2. If {{< katex >}}m, n{{< /katex >}}
 are natural numbers, for what values of {{< katex >}}m{{< /katex >}},
  does {{< katex >}}2^{5n} \times 5^m{{< /katex >}} ends in 5?

3. Find the HCF of 252525 and 363636.

4. If {{< katex >}}13824 = 2^a \times 3^b{{< /katex >}} 
then find {{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}}.

5. If {{< katex >}}p_1^{x_1} \times p_2^{x_2} \times p_3^{x_3} \times p_4^{x_4} = 113400{{< /katex >}}
 where {{< katex >}}p_1, p_2, p_3, p_4{{< /katex >}}
  are primes in ascending order and {{< katex >}}x_1, x_2, x_3, x_4{{< /katex >}} 
  are integers, find the value of {{< katex >}}p_1, p_2, p_3, p_4{{< /katex >}}
   and {{< katex >}}x_1, x_2, x_3, x_4{{< /katex >}}.

6. Find the LCM and HCF of 408 and 170 by applying the fundamental theorem of arithmetic.

7. Find the greatest number consisting of 6 digits which is exactly divisible by 24, 15, 36?

8. What is the smallest number that when divided by three numbers such as 35, 56 and 91 leaves remainder 7 in each case?

9. Find the least number that is divisible by the first ten natural numbers.

---