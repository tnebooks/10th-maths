---
title: 'GCD and LCM of Polynomials'
weight: 2
---
## 3.3 GCD and LCM of Polynomials

### 3.3.1 Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of Polynomials

In our previous class we have learnt how to find the GCD (HCF) of second degree and third degree expressions by the method of factorization. Now we shall learn how to find the GCD of the given polynomials by the method of long division.

As discussed in Chapter 2, (Numbers and Sequences) to find GCD of two positive integers using Euclidean Algorithm, similar techniques can be employed for two given polynomials also.

The following procedure gives a systematic way of finding Greatest Common Divisor of two given polynomials f(x) and g(x).

**Step 1:** First, divide f(x) by g(x) to obtain f(x) = g(x)q(x) + r(x) where q(x) is the quotient and r(x) is the remainder. Then, deg(r(x)) < deg(g(x))

**Step 2:** If the remainder r(x) is non-zero, divide g(x) by r(x) to obtain g(x) = r(x)q₁(x) + r₁(x) where r₁(x) is the new remainder. Then deg(r₁(x)) < deg(r(x)). If the remainder r₁(x) is zero, then r(x) is the required GCD.

**Step 3:** If r₁(x) is non-zero, then continue the process until we get zero as remainder. The divisor at this stage will be the required GCD.

We write GCD[f(x), g(x)] to denote the GCD of the polynomials f(x), g(x).

**Note:** If f(x) and g(x) are two polynomials of same degree then the polynomial carrying the highest coefficient will be the dividend. In case, if both have the same coefficient then compare the next least degree's coefficient and proceed with the division.

### Progress Check

1. When two polynomials of same degree has to be divided, ________ should be considered to fix the dividend and divisor.
2. If r(x) = 0 when f(x) is divided by g(x) then g(x) is called ________ of the polynomials.
3. If f(x) = g(x)q(x) + r(x), _________ must be added to f(x) to make f(x) completely divisible by g(x).
4. If f(x) = g(x)q(x) + r(x), _________ must be subtracted to f(x) to make f(x) completely divisible by g(x).

### Example 3.10

Find the GCD of the polynomials x³ + x² - x + 2 and 2x³ - 5x² + 5x - 3

**Solution:**

Let f(x) = 2x³ - 5x² + 5x - 3 and g(x) = x³ + x² - x + 2

![](example3-10-1.png)

Dividing f(x) by g(x):
Quotient: 2
Remainder: -7x² + 7x - 7 = -7(x² - x + 1)

Since -7 is not a divisor of g(x), we consider x² - x + 1

Now, dividing g(x) = x³ + x² - x + 2 by x² - x + 1:
Quotient: x + 2
Remainder: 0

![](example3-10-2.png)

Here, we get zero remainder.

Therefore, GCD(2x³ - 5x² + 5x - 3, x³ + x² - x + 2) = x² - x + 1

### Example 3.11

Find the GCD of 6x³ - 30x² + 60x - 48 and 3x³ - 12x² + 21x - 18

**Solution:**

Let f(x) = 6x³ - 30x² + 60x - 48 = 6(x³ - 5x² + 10x - 8)
and g(x) = 3x³ - 12x² + 21x - 18 = 3(x³ - 4x² + 7x - 6)

Now, we shall find the GCD of x³ - 5x² + 10x - 8 and x³ - 4x² + 7x - 6

Dividing first by second:
Quotient: 1
Remainder: -x² + 3x - 2 = -(x² - 3x + 2) = -(x-1)(x-2)

Dividing x³ - 4x² + 7x - 6 by x² - 3x + 2:
Quotient: x - 1
Remainder: 2x - 4 = 2(x - 2)

Dividing x² - 3x + 2 by x - 2:
Quotient: x - 1
Remainder: 0

![](example3-11.png)

GCD of leading coefficients 3 and 6 is 3.

Thus, GCD[(6x³ - 30x² + 60x - 48, 3x³ - 12x² + 21x - 18)] = 3(x - 2)

### 3.3.2 Least Common Multiple (LCM) of Polynomials

The Least Common Multiple of two or more algebraic expressions is the expression of highest degree (or power) such that the expressions exactly divide it.

Consider the following simple expressions a³b², ab³.
For these expressions LCM = a³b³.

**To find LCM by factorization method:**
- (i) Each expression is first resolved into its factors.
- (ii) The highest power of the factors will be the LCM.
- (iii) If the expressions have numerical coefficients, find their LCM.
- (iv) The product of the LCM of factors and coefficient is the required LCM.

### Example 3.12

Find the LCM of the following:
- (i) 8x⁴y², 48x²y⁴
- (ii) 5x - 5, 5x² - 20
- (iii) x⁴ - 1, x² - 2x + 1
- (iv) x³ - 27, (x - 3)², x² - 9

**Solution:**

**(i)** 8x⁴y², 48x²y⁴

First find the LCM of numerical coefficients: LCM(8, 48) = 48 = 2⁴ × 3

Then find LCM of variable terms: LCM(x⁴y², x²y⁴) = x⁴y⁴

Therefore, LCM(8x⁴y², 48x²y⁴) = 48x⁴y⁴

**(ii)** (5x - 5), (5x² - 20)

5x - 5 = 5(x - 1)
5x² - 20 = 5(x² - 4) = 5(x + 2)(x - 2)

Therefore, LCM[(5x - 5), (5x² - 20)] = 5(x - 1)(x + 2)(x - 2)

**(iii)** (x⁴ - 1), (x² - 2x + 1)

x⁴ - 1 = (x²)² - 1 = (x² + 1)(x² - 1) = (x² + 1)(x + 1)(x - 1)
x² - 2x + 1 = (x - 1)²

Therefore, LCM[(x⁴ - 1), (x² - 2x + 1)] = (x² + 1)(x + 1)(x - 1)²

**(iv)** x³ - 27, (x - 3)², x² - 9

x³ - 27 = (x - 3)(x² + 3x + 9)
(x - 3)² = (x - 3)²
x² - 9 = (x + 3)(x - 3)

Therefore, LCM[(x³ - 27), (x - 3)², (x² - 9)] = (x - 3)²(x + 3)(x² + 3x + 9)

![](think-corner-3.1.png)

## Exercise 3.2

1. Find the GCD of the given polynomials
   - (i) x⁴ + 3x³ - x - 3, x³ + 5x² + 3x - 1
   - (ii) x⁴ - 1, x³ - x² + x - 1
   - (iii) 36x⁴ + 12x³ - 24x² - 12x, 4x⁴ + 14x³ + 8x² - 8x
   - (iv) 3x³ + 3x² + 3x + 3, 6x³ + 12x² + 6x + 12

2. Find the LCM of the given expressions.
   - (i) 4x²y, 8x³y²
   - (ii) -9a³b², 12a²b²c
   - (iii) 16m, -12m²n², 8n²
   - (iv) p² - 3p + 2, p² - 4
   - (v) 2x² - 5x - 3, 4x² - 36
   - (vi) (2x² - 3xy)², (4x - 6y)³, 8x³ - 27y³

### 3.3.3 Relationship between LCM and GCD

Let us consider two numbers 12 and 18. We observe that, LCM(12, 18) = 36, GCD(12, 18) = 6.

Now, LCM(12, 18) × GCD(12, 18) = 36 × 6 = 216 = 12 × 18

Thus LCM × GCD is equal to the product of two given numbers.

Similarly, the product of two polynomials is the product of their LCM and GCD.

That is, **f(x) × g(x) = LCM[f(x), g(x)] × GCD[f(x), g(x)]**

![](think-corner-3.3.png)

## Exercise 3.3

1. Find the LCM and GCD for the following and verify that f(x) × g(x) = LCM × GCD
   - (i) 21x²y, 35xy²
   - (ii) (x³ - 1)(x + 1), (x³ + 1)
   - (iii) (x²y + xy²), (x² + xy)

2. Find the LCM of each pair of the following polynomials
   - (i) a² + 4a - 12, a² - 5a + 6 whose GCD is a - 2
   - (ii) x⁴ - a⁴, (x - a)² whose GCD is (x - a)

3. Find the GCD of each pair of the following polynomials
   - (i) 12(x⁴ - x³), 8(x⁴ - 3x³ + 2x²) whose LCM is 24x³(x - 1)(x - 2)
   - (ii) (x³ + y³), (x⁴ + x²y² + y⁴) whose LCM is (x³ + y³)(x² + xy + y²)

4. Given the LCM and GCD of the two polynomials p(x) and q(x) find the unknown polynomial in the following table

| S.No. | LCM | GCD | p(x) | q(x) |
|:---|:---|:---|:---|:---|
| (i) | a³ - 10a² + 11a + 70 | a - 7 | a² - 12a + 35 | |
| (ii) | (x⁴ - y⁴)(x⁴ + x²y² + y⁴) | (x² - y²) | | (x⁴ - y⁴)(x² + y² - xy) |

