---
title: 'Fundamental Theorem of Arithmetic'
weight: 4
---

# Fundamental Theorem of Arithmetic
Let us consider the following conversation between a Teacher and students.
<div style="border: 1px solid red; padding: 10px;"> 

**Teacher**: Factorise the number 240.

Malar: 24 × 10

Raghu : 8 × 30

Iniya: 12 × 20

Kumar : 15 × 16

Malar: Whose answer is correct Sir?

**Teacher** : All the answers are correct.

Raghu : How sir?

**Teacher** : Split each of the factors into product of prime numbers.

Malar: 2 × 2 × 2 × 3 × 2 × 5

Raghu : 2 × 2 × 2 × 2 × 3 × 5

Iniya: 2 × 2 × 3 × 2 × 2 × 5

Kumar : 3 × 5 × 2 × 2 × 2 × 2

**Teacher** : Good! Now, count the number of 2 ’s, 3 ’s and 5 ’s.

Malar: I got four 2 ’s, one 3 and one 5.

Raghu : I got four 2 ’s, one 3 and one 5.

Iniya: I also got the same numbers too.

Kumar : Me too sir.

Malar: All of us got four 2 ’s, one 3 and one 5 . This is very surprising to us.

**Teacher** : Yes, It should be. Once any number is factorized up to a product of prime numbers, everyone should get the same collection of prime numbers.
</div>

This concept leads us to the following important theorem.

**Theorem 4 (Fundamental Theorem of Arithmetic) (without proof )**

<div style="border: 1px solid green; padding: 10px;"> 
“Every positive integer (except the number 1) can be represented in exactly one
way apart from rearrangement as a product of one or more primes.”
</div>

![fundamental](fundamental.png)

<!-- <img src="fundamental.png" alt="image" style="float:right; margin-right:10px;" /> -->
The fundamental theorem asserts that every composite number can be decomposed as a product of prime numbers and that the decomposition is unique. In the sense that there is one and only way to express the decomposition as product of primes.

In general, we conclude that given a composite number N, we decompose it uniquely in the form N = p 1 × p 2 × p 3 ×  × p n where p 1 , p 2 , p 3 ,..., p n are primes and q 1 , q 2 , q 3 ,..., q n are natural numbers.

First, we try to factorize N into its factors. If all the factors are themselves primes then we can stop. Otherwise, we try to further split the factors which are not prime. Continue the process till we get only prime numbers.

**<span style="color:red">Illustration**
For example, if we try to factorize 32760 we get

{{<katex>}}32760 = 2×2×2×3×3×5×7×13

=2<sup>3</sup>×3<sup>2</sup>×5×7×13

Thus, in whatever way we try to factorize 32760 , we should finally get three 2 ’s, two 3 ’s, one 5 , one 7 and one 13 .

The fact that “Every composite number can be written uniquely as the product of power of primes” is called <span style="color:pink;">Fundamental Theorem of Arithmetic.</span>


<span style="color:blue;">

## Significance of the Fundamental Theorem of Arithmetic
</span>

The fundamental theorem about natural numbers except 1 , that we have stated above has several applications, both in Mathematics and in other fields. The theorem is vastly important in Mathematics, since it highlights the fact that prime numbers are the ‘Building Blocks’ for all the positive integers. Thus, prime numbers can be compared to atoms making up a molecule.

1. If a prime number p divides ab then either p divides a or p divides b ,that is p divides at least one of them.
2. If a composite number n divides ab , then n neither divide a nor b .For example, 6 divides 4 × 3 but 6 neither divide 4 nor 3 .

**<span style="color:red">Example 2.7**
</span> In the given factorisation, find the numbers m and n .

*<span style="color:blue">solution*</span>

Value of the first box from bottom = 5 × 2 = 10 

Value of n = 5 × 10 = 50

Value of the second box from bottom = 3 × 50 = 150

Value of m = 2 × 150 = 300

Thus, the required numbers are m = 300, n = 50
![progress check](1.png)<br>
**<span style="color:red">Example 2.8**</span>
Can the number 6 n , n being a natural number end with the digit 5 ? Give reason for your answer.

*<span style="color:blue">solution*</span>

Since 6<sup>n</sup>=(2×3)<sup>n</sup>=2<sup>n</sup>×3<sup>n</sup>

> 2 is a factor of 6<sup>n</sup> . So, 6<sup>n</sup> is always even.

**<span style="color:red">Example 2.9**</span> Is 7×5×3×2+3 a composite number?justify your answer.

*<span style="color:blue">Solution*</span>
Yes, the given number is a composite number, because

7 × 5 × 3 × 2 + 3 = 3 × ( 7 × 5 × 2 + 1 ) = 3 × 71

Since the given number can be factorized in terms of two primes, it is a composite number.

**<span style="color:red">Example 2.10**</span> ‘ a ’ and ‘ b ’ are two positive integers such that a <sup>b</sup> × b <sup>a</sup> = 800. Find ‘ a ’ and ‘ b ’.

*<span style="color:blue">Solution*</span> The number 800 can be factorized as<br>
800 = 2 × 2 × 2 × 2 × 2 × 5 × 5 = 2<sup>5</sup> × 5<sup>2</sup><br>
Hence a <sup>b</sup> × b <sup>a</sup> =2<sup>5</sup> × 5<sup>2</sup><br>
This implies that a = 2 and b = 5 (or) a = 5 and b = 2
![activity](ten.png)
**<div align="center" style="color:green" >Exercise 2 . 2</div>**
1. For what values of natural number n , {{<katex>}}4^{n} {{</katex>}}can end with the digit 6 ?
2. If m , n are natural numbers, for what values of m , does {{<katex>}}2^{n} 5^{m} {{</katex>}} ends in 5 ?
3. Find the HCF of 252525 and 363636 .
4. If 13824 = 2 <sup>a</sup> × 3 <sup>b</sup> then find a and b .
5. If p 1 x × p 2 x × p 3 x × p 4 x = 113400 where p 1 , p 2 , p 3 , p 4 are primes in ascending order and x 1 , x 2 , x 3 , x 4 are integers, find the value of p1, p2 , p 3 , p 4 and x 1 , x 2 , x 3 , x 4 .
6. Find the LCM and HCF of 408 and 170 by applying the fundamental theorem of arithmetic.
7. Find the greatest number consisting of 6 digits which is exactly divisible by 24, 15, 36 ?
8. What is the smallest number that when divided by three numbers such as 35, 56 and 91 leaves remainder 7 in each case?
9. Find the least number that is divisible by the first ten natural numbers.