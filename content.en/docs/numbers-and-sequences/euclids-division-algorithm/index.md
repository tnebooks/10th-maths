---
title: 'Euclids Division Algorithm'
weight: 2
---
<<<<<<< HEAD:content.en/numbers-and-sequences/euclids-division-algorithm/index.md


# Euclid’s Division Algorithm
=======
{{< katex display >}}{{< /katex >}}
## Euclid’s Division Algorithm
>>>>>>> cd7627df52a8cb3492e7174b98c680e96d62c77a:content.en/numbers-and-sequences/euclids_division_algorithm.md
In the previous section, we have studied about Euclid’s division lemma and its applications. We now study the concept Euclid’s Division Algorithm. The word         ‘algorithm’ comes from the name of 9 th century Persian Mathematician Al-khwarizmi. An algorithm means a series of methodical step-by-step procedure of calculating successively on the results of earlier steps till the desired answer is obtained.

Euclid’s division algorithm provides an easier way to compute the Highest Common Factor (HCF) of two given positive integers. Let us now prove the following theorem.

**Theorem 2**

    If a and b are positive integers such that a = bq + r , then every common divisor of a and b is a common divisor of b and r and vice-versa.

**Euclid’s Division Algorithm**

To find Highest Common Factor of two positive integers a and b , where a > b

**Step1:** Using Euclid’s division lemma a = bq + r ; {{<katex>}}0\le r < b{{</katex>}}. where q is the quotient, r is the remainder. If r = 0 then b is the Highest Common Factor of a and b .

**Step 2:** Otherwise applying Euclid’s division lemma divide b by r to get b={{<katex>}}rq_{1}+r_{1}{{</katex>}} , {{<katex>}}0\le r_{1} < r{{</katex>}}

**Step 3:** If {{<katex>}}r_{1}{{</katex>}} = 0 then r is the Highest common factor of a and b .

**Step 4:** Otherwise using Euclid’s division lemma, repeat the process until we get the remainder zero. In that case, the corresponding divisor is the HCF of a and b .

**Note:**

<!-- <div style="border: 1px solid red; padding: 10px;">  -->

* The above algorithm will always produce remainder zero at some stage. Hence the algorithm should terminate.

* Euclid’s Division Algorithm is a repeated application of Division Lemma until we get zero remainder.

* Highest Common Factor (HCF) of two positive numbers is denoted by ( a,b ).

* Highest Common Factor (HCF) is also called as Greatest Common Divisor (GCD).
<!-- 
<span style="background-color:blue; color:white"> Progress Check</span>
<div style="border: 1px solid blue; padding: 10px;">  -->

**Progress Check**

1. Euclid’s division algorithm is a repeated application of division lemma until we get remainder as _____.
2. The HCF of two equal positive integers k , k is _____.

**Illustration 1**

Using the above Algorithm, let us find HCF of two given positive integers. Let a = 273 and b = 119 be the two given positive integers such that a > b .

We start dividing 273 by 119 using Euclid’s division lemma.

we get, 273 = 119 × 2 + 35 		...( 1 )

The remainder is 35 !=0.

Therefore, applying Euclid’s Division Algorithm to the divisor 119 and remainder 35 . 

we get, 119 = 35 × 3 + 14               ...( 2 )

The remainder is 14 !=0 .

Applying Euclid’s Division Algorithm to the divisor 35 and remainder 14 .

we get, 35 =  14 ×  2 +  7      ...( 3 )

The remainder is 7!=10 .

Applying Euclid’s Division Algorithm to the divisor 14 and remainder 7 .

we get, 14 =  7 × 2 +  0      ...( 4 )

The remainder at this stage = 0 .

The divisor at this stage = 7 .

Therefore, Highest Common Factor of 273 , 119 = 7 .

**Example 2.4**  If the Highest Common Factor of 210 and 55 is expressible in the form 55 x - 325 , find x .

***Solution***  Using Euclid’s Division Algorithm, let us find the HCF of given numbers
210 = 55 × 3 + 45

55 = 45 × 1 + 10

45 = 10 × 4 + 5

10 = 5 × 2 + 0

The remainder is zero.
So, the last divisor 5 is the Highest Common Factor (HCF) of 210 and 55.

:.HCF is expressible in the form 55 x − 325 = 5

⇒55x = 330

x = 6

**Example 2.5**
Find the greatest number that will divide 445 and 572 leaving remainders 4 and 5 respectively.
***Solution***
Since the remainders are 4 , 5 respectively the required number is the HCF of the number 445 − 4 = 441 , 572 − 5 = 567 .
Hence, we will determine the HCF of 441 and 567 . Using Euclid’s Division Algorithm,
we have,

567 = 441 × 1 + 126
441 = 126 × 3 + 63
126 = 63 × 2 + 0

Therefore, HCF of 441 , 567 = 63 and so the required number is 63 .

**Activity 1**

This activity helps you to find HCF of two positive numbers. We first observe the following instructions.

(i) Construct a rectangle whose length and breadth are the given numbers.

(ii) Try to fill the rectangle using small squares.

(iii) Try with 1 × 1 square; Try with 2 × 2 square; Try with 3  ́ 3 square and so on.

(iv) The side of the largest square that can fill the whole rectangle without any gap will be HCF of the given numbers.

(v) Find the HCF of (a) 12 , 20 (b) 16 , 24 (c) 11 , 9


**Theorem 3**

If a and b are two positive integers with a > b then G.C.D of ( a , b ) = GCD of ( a - b , b ) .


**Activity 2**

This is another activity to determine HCF of two given positive integers.

(i) From the given numbers, subtract the smaller from the larger number.

(ii) From the remaining numbers, subtract smaller from the larger.

(iii) Repeat the subtraction process by subtracting smaller from the larger.

(iv) Stop the process, when the numbers become equal.

(v) The number representing equal numbers obtained in step (iv), will be the
HCF of the given numbers.

Using this Activity, find the HCF of

(i) 90 , 15 (ii) 80 , 25 (iii) 40 , 16 (iv) 23 , 12 (v) 93 , 13


**Highest Common Factor of three numbers**

We can apply Euclid’s Division Algorithm twice to find the Highest Common Factor (HCF) of three positive integers using the following procedure.
Let a, b, c be the given positive integers.

(i) Find HCF of a,b . Call it as d = ( a,b )

(ii) Find HCF of d and c .
		
This will be the HCF of the three given numbers a, b, c

**Example 2.6**
Find the HCF of 396 , 504 , 636 .

***Solution***
To find HCF of three given numbers, first we have to find HCF of the first two numbers.

To find HCF of 396 and 504

Using Euclid’s division algorithm we get 504 = 396 × 1 + 108

The remainder is 108!=0

Again applying Euclid’s division algorithm 396 = 108 × 3 + 72

The remainder is 72!=0

Again applying Euclid’s division algorithm 108 = 72 × 1 + 36

The remainder is 36!=0

Again applying Euclid’s division algorithm 72 = 36 × 2 + 0

Here the remainder is zero. Therefore HCF of 396 , 504 = 36 .

To find the HCF of 636 and 36 .

Using Euclid’s division algorithm we get 636 = 36 × 17 + 24

The remainder is 24!=0

Again applying Euclid’s division algorithm 36 = 24 × 1 + 12

The remainder is 12!=0

Again applying Euclid’s division algorithm 24 = 12 × 2 + 0
Here the remainder is zero. Therefore HCF of 636 , 36 = 12

Therefore Highest Common Factor of 396 , 504 and 636 is 12.


***Do you Know?***

Two positive integers are said to be relatively prime or co prime if their
Highest Common Factor is 1 .

**Exercise 2**

1. Find all positive integers, when divided by 3 leaves remainder 2 .
2. A man has 532 flower pots. He wants to arrange them in rows such that each row contains 21 flower pots. Find the number of completed rows and how many flower pots are left over.
3. Prove that the product of two consecutive positive integers is divisible by 2 .
4. When the positive integers a , b and c are divided by 13 , the respective remainders are 9 , 7 and 10 . Show that a + b + c is divisible by 13 .
5. Prove that square of any integer leaves the remainder either 0 or 1 when divided by 4 .
6. Use Euclid’s Division Algorithm to find the Highest Common Factor (HCF) of
(i) 340 and 412 (ii) 867 and 255 (iii) 10224 and 9648 (iv) 84 , 90 and 120
7. Find the largest number which divides 1230 and 1926 leaving remainder 12 in each
case.
8. If d is the Highest Common Factor of 32 and 60 , find x and y satisfying d = 32 x + 60 y .
9. A positive integer when divided by 88 gives the remainder 61 . What will be the remainder when the same number is divided by 11 ?
9. Prove that two consecutive positive integers are always coprime.
