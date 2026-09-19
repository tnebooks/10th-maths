---
title: 'algebra'
weight: 3
---

# Chapter 3

## ALGEBRA

> “A person who can, within a year, solve $x^2 - 92y^2 = 1$ is a mathematician” - Brahmagupta

Niccolo Fontana Tartaglia was an Italian mathematician, engineer, surveyor and bookkeeper from then Republic of Venice (now Italy). He published many books, including the first Italian translations of Archimedes and Euclid, and an acclaimed compilation of mathematics. Tartaglia was the first to apply mathematics to the investigation of the paths of cannonballs; his work was later validated by Galileo’s studies on falling bodies.

Tartaglia along with Cardano were credited for finding methods to solve any third degree polynomials called cubic equations. He also provided a nice formula for calculating volume of any tetrahedron using distance between pairs of its four vertices.

![Niccolo Fontana Tartaglia 1499/1500 – 1557 AD(CE)]()

### Learning Outcomes

- To solve system of linear equations in three variables by the method of elimination
- To find GCD and LCM of polynomials
- To simplify algebraic rational expressions
- To understand and compute the square root of polynomials
- To learn about quadratic equations
- To draw quadratic graphs
- To learn about matrix, its types and operations on matrices

### 3.1 Introduction

Algebra can be thought of as the next level of study of numbers. If we need to determine anything subject to certain specific conditions, then we need Algebra. In that sense, the study of Algebra is considered as “Science of determining unknowns”. During third century AD(CE) Diophantus of Alexandria wrote a monumental book titled “Arithmetica” in thirteen volumes of which only six has survived. This book is the first source where the conditions of the problems are stated as equations and they are eventually solved. Diophantus realized that for many real life situation problems, the variables considered are usually positive integers.

The term “Algebra” has evolved as a misspelling of the word ‘al-jabr’ from one of the important work titled Al-Kitāb al-mukhtaşar fī hisāb al-jabr wa’l-muqābala (“The Compendious Book on Calculation by Completion and Balancing”) written by Persian Mathematician Al-Khwarizmi of 9th Century AD(CE) Since Al-Khwarizmi’s Al-Jabr book provided the most appropriate methods of solving equations, he is hailed as “Father of Algebra”.

In the earlier classes, we had studied several important concepts in Algebra. In this class, we will continue our journey to understand other important concepts which will be of much help in solving problems of greater scope. Real understanding of these ideas will benefit much in learning higher mathematics in future classes.

### Simultaneous Linear Equations in Two Variables

Let us recall solving a pair of linear equations in two variables.

**Definition**

Linear Equation in two variables Any first degree equation containing two variables x and y is called a linear equation in two variables. The general form of linear equation in two variables x and y is ax+by+c = 0 , where atleast one of a, b is non-zero and a, b, c are real numbers. Note that linear equations are first degree equations in the given variables.

**Note**

- xy – 7 = 3 is not a linear equation in two variables since the term xy is of degree 2.
- A linear equation in two variables represent a straight line in xy plane.
**Example 3.1**
The father’s age is six times his son’s age. Six years hence, the age of father

will be four times his son’s age. Find the present ages (in years) of the son and father. Solution Let the present age of father be x years and the present age of son be y years Given, x = 6y … (1)

$x + 6 = 4(y + 6) 						… (2)$

Substituting (1) in (2), 6y + 6 = 4 (y + 6)

$6y + 6 = 4y + 24 \\Rightarrow  y = 9$

Therefore, son’s age = 9 years and father’s age = 54 years.

**Example 3.2**
Solve 2x − 3y = 6 , x + y = 1

Solution 2x − 3y = 6 … (1)

$x + y = 1 							… (2)$

$(1) \\times  1 \\Rightarrow  2x - 3y = 6                                                                    3$

Y

$2x–3y =6$

$(2) \\times  2 \\Rightarrow  2x +2y = 2                                                       x+y =1        2$

1 ------------------------------------------------------------- −4 0 X′ -3 -2 -1 1 2 3 4 5 6 7X

$-5y = 4 \\Rightarrow  y =                             -1$

5 -2 9   , − 4   5  −4 4 9 5  -4 Substituting y = in (2), x − = 1 we get, x = Y¢ 5 5 5 9 −4 ![Fig. 3.1]() Therefore, x = , y = . 5 5

### 3.2 Simultaneous Linear Equations in Three Variables

Right from the primitive needs of calculating amount spent for various items in a super market, finding ages of people under specific conditions, finding path of an object when it is thrown upwards at an angle, Algebra plays a vital role in our daily life. Any point in the space can be determined uniquely by knowing its latitude, longitude and altitude. Hence to locate the position of an object at a particular place situated on the Earth, three satellites are positioned to arrive three equations. Among these three equations, we get two linear equations and one quadratic (second degree) equation. Hence we can solve for the variables latitude, longitude and altitude to uniquely fix the position of any object at a given point of time. This is the basis of ![Fig. 3.2]() Global Positioning System (GPS). Hence the concept of linear equations in three variables is used in GPS systems.

#### 3.2.1 System of Linear Equations in Three Variables

In earlier classes, we have learnt different methods of solving Simultaneous Linear Equations in two variables. Here we shall learn to solve the system of linear equations in three variables namely, x, y and z. The general form of a linear equation in three variables x, y and z is ax + by + cz + d = 0 where a, b, c, d are real numbers, and atleast one of a, b, c is non-zero.

**Note**

- A linear equation in two variables of the form ax + by + c = 0, represents a straight line.
- A linear equation in three variables of the form ax + by + cz + d = 0, represents a plane.

$ax+by+cz+d =0$

ax +b y+ c

$=0$

O X O X′ X Y ¢ ![Fig. 3.3(i)]() Y ![Fig. 3.3(ii)]() Y¢ 

General Form: A system of linear equations in three variables x, y, z has the general form

$a1x + b1y + c1z + d1 = 0$

$a2x + b2y + c2z + d2 = 0$

$a 3x + b3y + c3z + d3 = 0$

Each equation in the system represents a plane in three dimensional space and solution of the system of equations is precisely the point of intersection of the three planes defined by the three linear equations of the system. The system may have only one solution, infinitely many solutions or no solution depending on how the planes intersect one another. The figures presented below illustrate each of these possibilities

only one solution Infinitely many No solution solutions

![Fig. 3.4]()

**Procedure for solving system of linear equations in three variables**

Step 1: By taking any two equations from the given three, first multiply by some suitable non-zero constant to make the co-efficient of one variable (either x or y or z) numerically equal. Step 2: Eliminate one of the variables whose co-efficients are numerically equal from the equations. Step 3: Eliminate the same variable from another pair. Step 4: Now we have two equations in two variables. Step 5: Solve them using any method studied in earlier classes. Step 6: The remaining variable is then found by substituting in any one of the given equations.

**Note**

- If you obtain a false equation such as 0=1, in any of the steps then the system has no
solution.

- If you do not obtain a false solution, but obtain an identity, such as 0=0 then the system
has infinitely many solutions.

**Example 3.3**
Solve the following system of linear equations in three variables

$3x – 2y + z =$

$2 , 2x + 3y – z = 5 , x + y + z = 6 .$

Solution 3x − 2y + z = 2 …(1) 2x + 3y – z = 5 …(2) x +y +z = 6 …(3)

Adding (1) and (2), 3x – 2y + z

$= 2$

(+)

$2x + 3y – z = 5$

$5x + y       = 7				…(4)$

Adding (2) and (3), 2x + 3y – z = 5 (+)

$x + y +z = 6$

$3x + 4y      = 11				…(5)$

$4 \\times  (4)-(5)                  20x + 4y = 28$

(−)

$3x + 4y = 11$

$17x        = 17     \\Rightarrow  x =1$

Substituting x = 1 in (4), 5 + y = 7 Þ y = 2 Substituting x = 1 , y = 2 in (3), 1 + 2 + z = 6 we get, z = 3 Therefore, x = 1, y = 2 , z = 3

**Example 3.4**
In an interschool atheletic meet, with total of 24 individual prizes, securing

a total of 56 points, a first place secures 5 points, a second place secures 3 points, and a third place secures 1 point. Having as many third place finishers as first and second place finishers, find how many athletes finished in each place. Solution Let the number of I, II and III place finishers be x , y and z respectively. Total number of prizes = 24; Total number of points = 56. Hence, the linear equations in three variables are

$x + y + z = 24 …(1) 		                             5x + 3y + z = 56 …(2)         x +y = z   …(3)$

Substituting (3) in (1) we get, z + z = 24 Þ z = 12 ∴ (3) will be, x + y = 12

$(2) \\Rightarrow                    5x + 3y = 44$

(−)

$3\\times (3) \\Rightarrow                       3x + 3y = 36$

$2x        =8       we get, x = 4$

Substituting x = 4 , z = 12 in (3) we get, y = 12 − 4 = 8 Therefore, Number of first place finishers is 4 Number of second place finishers is 8 Number of third place finishers is 12.

**Example 3.5**
Solve x + 2y – z = 5 ; x − y + z = −2 ; −5x − 4y + z = −11

Solution x + 2y – z =5 …(1) x – y + z =–2 …(2) –5x –4y + z = –11 …(3) Adding (1) and (2) we get, x + 2y – z = 5 (+)

$x – y + z = –2$

$2x + y       = 3					…(4)$

Subtracting (2) and (3), x − y +z = – 2 (−)

$-5x - 4y + z = – 11$

$6x + 3y           =9$

Dividing by 3 2x + y = 3 …(5) Subtracting (4) and (5), 2x + y =3

$2x + y     =3$

$0 =0$

Here, we arrive at an identity 0=0. Hence, the system has an infinite number of solutions.

**Example 3.6**
Solve 3x + y – 3z = 1 ; –2x – y + 2z = 1 ; –x – y + z = 2 .

Solution 3x + y − 3z = 1 … (1) –2x – y + 2z = 1 …(2) −x − y + z = 2 …(3)

Adding (1) and (2), 3x + y − 3z = 1 (+)

$-2x - y + 2z = 1$

$x     –      z = 2				… (4)$

Adding (1) and (3), 3x + y − 3z = 1 (+)

$-x - y + z = 2$

$2x      - 2z = 3				… (5)$

$2x      - 2z = 3$

(−)

$Now, (5) -2\\times (4) we get,              2x      - 2z = 4$

$0 = –1$

Here, we arrive at a contradiction as 0 ≠ –1. This means that the system is inconsistent and has no solution. x y z y z

**Example 3.7**
Solve

$- 1 = + 1 = + 2 ; + = 13$

2 6 7 3 2 x y Solution Considering, −1 = +1 2 6 x y 6x − 2y

$- = 1+1 \\Rightarrow          = 2 we get, 3x - y = 12                               … (1)$

2 6 12 x z Considering, −1 = + 2 2 7 x z 7x − 2z

$- =1+2 \\Rightarrow           = 3 we get, 7x - 2z = 42                              … (2)$

2 7 14 y z 2y + 3z Also, from + = 13 Þ = 13 we get, 2y + 3z = 78 … (3) 3 2 6

Eliminating z from (2) and (3)

$(2) \\times  3 \\Rightarrow                              21x         – 6z = 126$

(+)

$(3) \\times  2 \\Rightarrow                                     4y + 6z = 156$

$21x + 4y        = 282$

(+) (1) × 4 Þ 12x

$- 4y       = 48$

$33x             = 330 so, x = 10$

Substituting x = 10 in (1), 30 − y = 12 we get, y = 18 Substituting x = 10 in (2), 70 − 2z = 42 then, z = 14

$\\therefore  x = 10 , y = 18 , z = 14 .$

1 1 1 1 1 1 1 1 4 2

**Example 3.8**
Solve : + − = ; = ; − + =2

2x 4y 3z 4 x 3y x 5y z 15 1 1 1 Solution Let =p , =q , =r x y z The given equations are written as

p q r 1

$+ -   =$

2 4 3 4 q

$p =$

3 q 2 32

$p - + 4r = 2    =$

5 15 15 By simplifying we get,

$6p + 3q - 4r = 3					…(1)$

$3p = q					…(2)$

$15p - 3q + 60r = 32					…(3)$

Substituting (2) in (1) and (3) we get, 15p - 4r

$= 3					…(4)$

$6p + 60r = 32 reduces to 3p + 30r = 16   …(5)$

Solving (4) and (5),

$15p - 4r = 3$

(−)

$15p + 150r = 80$

1

$-154r = – 77       we get, r =$

2 1 1 Substituting r =

$in (4) we get, 15p - 2 = 3 \\Rightarrow  p =$

2 3 From (2), q = 3p we get

$⇒q =1$

1 1 1 Therefore, x = = 3, y = = 1, z = = 2 . i.e., x = 3, y = 1, z = 2 . p q r 

**Example 3.9**
The sum of thrice the first number, second number and twice the third

number is 5. If thrice the second number is subtracted from the sum of first number and thrice the third we get 2. If the third number is subtracted from the sum of twice the first, thrice the second, we get 1. Find the numbers. Solution Let the three numbers be x, y, z From the given data we get the following equations,

$3x + y + 2z = 5 …(1)              x + 3z – 3y = 2      …(2)		       2x + 3y – z = 1 …(3)$

$(1) \\times  1 \\Rightarrow                             3x + y + 2z = 5$

(−)

$(2) \\times  3 \\Rightarrow                            3x – 9y + 9z = 6                    Thinking Corner$

10y – 7z = –1 …(4) 1. The number of possible solutions

$(1) \\times  2 \\Rightarrow            6x + 2y + 4z = 10$

(−) when solving system

$(3) \\times 3 \\Rightarrow                             6x + 9y - 3z = 3                        of linear equations$

$-7y + 7z = 7		           …(5)         in three variables are$

_____. Adding (4) and (5), 10y – 7z = –1

2. If    three    planes
$-7y + 7z = 7$

are parallel then 3y =6 Þ y =2 the number of possible point(s) of Substituting y = 2 in (5), −14 + 7z = 7 Þ z = 3 intersection is/are Substituting y = 2 and z = 3 in (1), _____.

$3x + 2 + 6 = 5 we get$

$⇒ x = -1$

Therefore, x = –1, y = 2, z = 3.

### Progress Check

1. For a system of linear equations in three variables the minimum number of
equations required to get unique solution is _______.

2. A system with _______ will reduce to identity.
3. A system with _______ will provide absurd equation.
**Exercise 3.1**

1. Solve the following system of linear equations in three variables
(i) x + y + z = 5 ; 2x − y + z = 9 ; x − 2y + 3z = 16
1 2 1 1 2 3

(ii)   − + 4 = 0;      − + 1 = 0;    + = 14
x y y z z x 3y

(iii) x + 20 =    + 10 = 2z + 5 = 110 – (y + z)
2

2.      Discuss the nature of solutions of the following system of equations
(i) x + 2y − z = 6 ; −3x − 2y + 5z = −12 ; x − 2z = 3
1

(ii) 2y + z = 3 (−x + 1) ; −x + 3y − z = −4 ; 3x + 2y + z = −
2 y +z z +x x +y

(iii)         =      =      ; x + y + z = 27
4 3 2

3. Vani, her father and her grand father have an average age of 53. One-half of her
grand father’s age plus one-third of her father’s age plus one fourth of Vani’s age is 65. Four years ago if Vani’s grandfather was four times as old as Vani then how old are they all now ?

4. The sum of the digits of a three-digit number is 11. If the digits are reversed, the new
number is 46 more than five times the former number. If the hundreds digit plus twice the tens digit is equal to the units digit, then find the original three digit number ?

5. There are 12 pieces of five, ten and twenty rupee currencies whose total value is ₹105.
When first 2 sorts are interchanged in their numbers its value will be increased by ₹20. Find the number of currencies in each sort.

### 3.3 GCD and LCM of Polynomials

#### 3.3.1 Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of Polynomials

In our previous class we have learnt how to find the GCD (HCF) of second degree and third degree expressions by the method of factorization. Now we shall learn how to find the GCD of the given polynomials by the method of long division. As discussed in Chapter 2, (Numbers and Sequences) to find GCD of two positive integers using Euclidean Algorithm, similar techniques can be employed for two given polynomials also. The following procedure gives a systematic way of finding Greatest Common Divisor of two given polynomials f (x ) and g(x ) . Step 1: First, divide f(x) by g(x ) to obtain f (x ) = g(x )q(x ) + r (x ) where q(x ) is the quotient and r (x ) is the remainder. Then, deg r (x ) < deg g(x ) Step 2: If the remainder r (x ) is non-zero, divide g(x ) by r (x ) to obtain g(x ) = r (x )q1(x ) + r1(x ) where r1(x ) is the new remainder. Then deg r1(x ) < deg r (x ) . If the remainder r1(x ) is zero, then r (x ) is the required GCD. Step 3: If r1(x ) is non-zero, then continue the process until we get zero as remainder. The divisor at this stage will be the required GCD. We write GCD  f (x ), g(x ) to denote the GCD of the polynomials f (x ), g(x ).

**Note**

If f (x ) and g(x ) are two polynomials of same degree then the polynomial carrying the highest coefficient will be the dividend. In case, if both have the same coefficient then compare the next least degree’s coefficient and proceed with the division. 

### Progress Check

1. When two polynomials of same degree has to be divided, __________ should be
considered to fix the dividend and divisor.

2. If r (x ) = 0 when f(x) is divided by g(x) then g(x) is called ________ of the
polynomials.

3. If f (x ) = g(x )q(x ) + r (x ), _________ must be added to f(x) to make f(x) completely
divisible by g(x).

4. If f (x ) = g(x )q(x ) + r (x ), _________ must be subtracted to f(x) to make f(x)
completely divisible by g(x).

**Example 3.10**
Find the GCD of the polynomials x 3 + x 2 − x + 2 and 2x 3 − 5x 2 + 5x − 3 .

Solution Let f (x ) = 2x 3 − 5x 2 + 5x − 3 and g(x ) = x 3 + x 2 − x + 2 2 x3 + x2 − x + 2 2x 3 − 5x 2 + 5x − 3 2x 3 + 2x 2 − 2x + 4 (−) (−) (+) (−) −7x 2 + 7x − 7

$= -7(x^2 - x + 1)$

−7(x 2 − x + 1) ≠ 0 , note that -7 is not a divisor of g(x )

Now, dividing g(x ) = x 3 + x 2 − x + 2 by the new remainder x2–x+1 (leaving the constant factor), we get x+2 2 x −x +1 x3 + x2 − x + 2 x3 − x2 + x (−) (+) (−) 2x 2 − 2x + 2 2x 2 − 2x + 2 (−) (+) (−) 0 Here, we get zero remainder. Therefore, GCD(2x 3 − 5x 2 + 5x − 3, x 3 + x 2 − x + 2) = x 2 − x + 1 .

**Example 3.11**
Find the GCD of 6x 3 − 30x 2 + 60x − 48 and 3x 3 − 12x 2 + 21x − 18 .

Solution Let, f (x) = 6x 3 − 30x 2 + 60x − 48 = 6(x 3 − 5x 2 + 10x − 8) and

$g (x) = 3x 3 - 12x 2 + 21x - 18 = 3 (x^3 - 4x 2 + 7x - 6)$

Now, we shall find the GCD of x 3 − 5x 2 + 10x − 8 and x 3 − 4x 2 + 7x − 6 1 x 3 − 5x 2 + 10x − 8 x 3 − 4x 2 + 7x − 6 x 3 − 5x 2 + 10x − 8 (−) (+) (−) (+) 2 x − 3x + 2 x -2 x 2 − 3x + 2 x 3 − 5x 2 + 10x − 8 x 3 − 3x 2 + 2x (−) (+) (−) 2 −2x + 8x − 8 −2x 2 + 6x − 4 (+) (−) (+) 2x - 4

$= 2(x - 2)$

x -1 x -2 x 2 − 3x + 2 x 2 - 2x (−) (+) −x + 2 −x + 2 (+) (−) 0 Here, we get zero remainder. GCD of leading coefficients 3 and 6 is 3.

$Thus, GCD (6x 3 - 30x 2 + 60x - 48, 3x 3 - 12x 2 + 21x - 18) = 3(x - 2) .$

 

#### 3.3.2 Least Common Multiple (LCM) of Polynomials

The Least Common Multiple of two or more algebraic expressions is the expression of highest degree (or power) such that the expressions exactly divide it. Consider the following simple expressions a 3b 2 , a 2b 3 .

$For these expressions LCM = a 3b 3 .$

To find LCM by factorization method

(i) Each expression is first resolved into its factors.
(ii) The highest power of the factors will be the LCM.
(iii) If the expressions have numerical coefficients, find their LCM.
(iv) The product of the LCM of factors and coefficient is the required LCM.
**Example 3.12**
Find the LCM of the following

(i) 8x 4y 2 , 48x 2y 4 			(ii) 5x - 10, 5x 2 - 20
(iii) x 4 - 1, x 2 − 2x + 1 			(iv) x 3 - 27, (x - 3)2 , x 2 - 9

Solution (i) 8x 4y 2 , 48x 2y 4 First let us find the LCM of the numerical coefficients. That is, LCM (8, 48) = 2 × 2 × 2 × 6 = 48 Then find the LCM of the terms involving variables. That is, LCM (x 4y 2, x 2y 4 ) = x 4y 4 Finally find the LCM of the given expression. We condclude that the LCM of the given expression is the product of the LCM of the numerical coefficient and the LCM of the terms with variables. Therefore, LCM (8x 4y 2, 48x 2y 4 ) = 48x 4y 4

(ii) (5x - 10), (5x 2 - 20)
$5x - 10 = 5(x - 2)$

$5x 2 - 20 = 5(x^2 - 4) = 5(x + 2)(x - 2)$

Therefore, LCM [(5x − 10),(5x 2 − 20)] = 5(x + 2)(x − 2)

(iii) (x 4 - 1), x 2 − 2x + 1
$x^4 - 1 = (x^2 )2 - 1 = (x^2 + 1)(x^2 - 1) = (x^2 + 1)(x + 1)(x - 1)$

$x^2 - 2x + 1 = (x - 1)2$

Therefore, LCM [(x 4 − 1),(x 2 − 2x + 1)] = (x 2 + 1)(x + 1)(x − 1)2

(iv) x 3 - 27, (x - 3)2 , x 2 - 9
$x^3 - 27 = (x - 3)(x^2 + 3x + 9) ; (x - 3)2 = (x - 3)2 ; (x^2 - 9) = (x + 3)(x - 3)$

Therefore, LCM [(x 3 - 27),(x - 3)2,(x 2 - 9)] = (x − 3)2 (x + 3)(x 2 + 3x + 9)

### Thinking Corner

Complete the factor tree for the given polynomials f(x) and g(x). Hence find their GCD and LCM.

$f(x) = 2x3 – 9x2 – 32x –21             g(x) = 2x3 – 7x2 – 43x – 42$

2x + 3 x+1 x+2

$GCD [f (x) and g (x)] = _____                   LCM [f (x) and g (x)] = _____$

**Exercise 3.2**

1. Find the GCD of the given polynomials
(i) x 4 + 3x 3 − x − 3, x 3 + x 2 − 5x + 3              (ii) x 4 - 1 , x 3 − 11x 2 + x − 11
(iii) 3x 4 + 6x 3 − 12x 2 − 24x , 4x 4 + 14x 3 + 8x 2 − 8x
(iv) 3x 3 + 3x 2 + 3x + 3 , 6x 3 + 12x 2 + 6x + 12
2. Find the LCM of the given expressions.
(i) 4x 2y, 8x 3y 2 		 (ii)
-9a 3b 2 , 12a 2b 2c (iii) 16m,-12m 2n 2 , 8n 2

(iv) p 2 − 3p + 2, p 2 - 4              (v) 2x 2 - 5x - 3, 4x 2 - 36
(vi) (2x 2 - 3xy )2 , (4x - 6y )3 , 8x 3 - 27y 3
#### 3.3.3 Relationship between LCM and GCD

Let us consider two numbers 12 and 18. We observe that, LCM (12, 18) = 36, GCD (12, 18) = 6 .

$Now, LCM (12,18) \\times  GCD(12,18) = 36 \\times  6 = 216 = 12 \\times  18$

Thus LCM × GCD is equal to the product of two given numbers. Similarly, the product of two polynomials is the product of their LCM and GCD, That is, f (x ) × g(x ) = LCM [ f (x ), g(x )]×GCD[ f (x ), g(x )] Illustration

$Consider                                    f(x) = 12(x^2 - y^2 ) and g(x ) = 8(x^3 - y^3 )$

$Now,                                        f(x) = 12(x^2 - y^2 ) = 22 \\times  3 \\times  (x + y )(x - y )                ...(1)$

$and                                         g(x) = 8(x^3 - y^3 ) = 23 \\times  (x - y )(x^2 + xy + y^2 )            ...(2)$

From (1) and (2) we get,

$LCM[f(x), g(x)] = 23 \\times  3 \\times  (x + y )(x - y )(x^2 + xy + y^2 )$

$= 24 \\times  (x^2 - y^2 )(x^2 + xy + y^2 )$

$GCD  f (x ), g(x ) = 22 \\times  (x - y ) = 4(x - y )$

$LCM ´GCD = 24 \\times  4 \\times  (x^2 - y^2 ) \\times  (x^2 + xy + y^2 ) \\times  (x - y )$

$LCM ´GCD = 96(x^3 - y^3 )(x^2 - y^2 ) 		                                         ...(3)$

$product of f(x) and g(x) = 12(x^2 - y^2 ) \\times  8(x^3 - y^3 )$

$= 96(x^2 - y^2 )(x^3 - y^3 ) 		                                                                                        ...(4)$

From (3) and (4) we obtain LCM × GCD = f (x ) × g(x )

### Thinking Corner

$Is f (x ) ´ g(x ) ´ r (x ) =LCM [ f (x ), g(x ), r (x )] \\times  GCD [ f (x ), g(x ), r (x )] ?$

**Exercise 3.3**

1. Find the LCM and GCD for the following and verify that f (x ) × g(x ) = LCM ×GCD
(i) 21x 2y, 35xy 2             (ii) (x 3 − 1)(x + 1), (x 3 + 1)             (iii) (x 2y + xy 2 ), (x 2 + xy )
2. Find the LCM of each pair of the following polynomials
(i) a 2 + 4a − 12, a 2 − 5a + 6 whose GCD is a - 2
(ii) x 4 - 27a 3x , (x - 3a )2 whose GCD is (x - 3a )

3. Find the GCD of each pair of the following polynomials
(i) 12(x 4 - x 3 ), 8(x 4 − 3x 3 + 2x 2 ) whose LCM is 24x 3 (x - 1)(x - 2)
(ii) (x 3 + y 3 ), (x 4 + x 2y 2 + y 4 ) whose LCM is (x 3 + y 3 )(x 2 + xy + y 2 )
4. Given the LCM and GCD of the two polynomials p(x) and q(x) find the unknown
polynomial in the following table S.No. LCM GCD p(x) q(x)

(i) a 3 − 10a 2 + 11a + 70                 a -7       a 2 − 12a + 35
(ii) (x 4 − y 4 )(x 4 + x 2y 2 + y 4 ) (x 2 - y 2 )                     (x 4 − y 4 )(x 2 + y 2 − xy )
### 3.4 Rational Expressions

Definition : An expression is called a rational expression if it can be written in the form p(x ) where p(x) and q(x) are polynomials and q(x) ¹ 0 . A rational expression is the ratio q(x ) of two polynomials. The following are examples of rational expressions. 9 2y + 1 z3 + 5 a , 2 , , . x y − 4y + 9 z − 4 a + 10 The rational expressions are applied for describing distance-time, modeling multi- task problems, to combine workers or machines to complete a job schedule and much more.

#### 3.4.1 Reduction of Rational Expression

p(x ) A rational expression is said to be in its lowest form if GCD (p(x ), q(x )) = 1 . q(x ) To reduce a rational expression to its lowest form, follow the given steps

(i) Factorize the numerator and the denominator
(ii) If there are common factors in the numerator and denominator, cancel them.
(iii) The resulting expression will be a rational expression in its lowest form.
**Example 3.13**
Reduce the rational expressions to its lowest form

x -3 x 2 − 16

(i)        (ii)
x2 - 9 x 2 + 8x + 16 x -3 x −3 1 Solution (i) 2 = = x -9 (x + 3)(x − 3) x +3 2 x − 16 (x + 4)(x − 4) x −4

(ii) 2                  =                  =
x + 8x + 16 (x + 4)2 x +4

#### 3.4.2 Excluded Value

p(x ) A value that makes a rational expression (in its lowest form) undefined is called q(x ) an Excluded value.

To find excluded value for a given rational expression in its lowest form, say p(x )

$, consider the denominator q(x) = 0.$

q(x ) 5 For example, the rational expression is undefined when x = 10 . So, 10 is x - 10 5 called an excluded value for . x - 10

**Example 3.14**
Find the excluded values of the following expressions (if any).

x + 10 7p + 2 x

(i)           		                (ii)     2
(iii)     2
8x 8 p + 13p + 5 x +1

**Solution**

x + 10

(i)
8x x + 10 The expression is undefined when 8x = 0 or x = 0 . Hence, the excluded 8x value is 0.

7p + 2

(ii)              2
8 p + 13p + 5 7p + 2 The expression is undefined when 8p 2 + 13p + 5 = 0 2 8 p + 13p + 5 that is, (8 p + 5)(p + 1) = 0 −5 -5 p= , p = −1 . The excluded values are and -1 . 8 8 x

(iii)          2
x +1 Here, x 2 ³ 0 for all x. Therefore, x 2 + 1 ≥ 0 + 1 = 1 . Hence, x 2 + 1 ≠ 0 for any x. Therefore, there can be no real excluded values for the given rational x expression 2 . x +1

### Thinking Corner

sin x

1. Are x 2 - 1 and tan x =    rational expressions?
cos x x 3 + x 2 − 10x + 8

2. The number of excluded values of                     is _____.
x 4 + 8x 2 − 9

**Exercise 3.4**

1. Reduce each of the following rational expressions to its lowest form.
x2 −1 x 2 − 11x + 18 9x 2 + 81x p 2 − 3p − 40

(i) 2                         (ii) 2                  (iii) 3                  (iv) 3
x +x x − 4x + 4 x + 8x 2 − 9x 2p − 24 p 2 + 64 p

2. Find the excluded values, if any of the following expressions.
y t x 2 + 6x + 8 x 3 − 27

(i) 2                         (ii) 2                  (iii) 2                  (iv) 3
y - 25 t − 5t + 6 x +x −2 x + x 2 − 6x 

#### 3.4.3 Operations of Rational Expressions

We have studied the concepts of addition, subtraction, multiplication and division of rational numbers in previous classes. Now, let us generalize the above for rational expressions.

**Multiplication of Rational Expressions**

p(x ) r (x ) If and are two rational expressions where q(x ) ¹ 0, s(x ) ¹ 0 , q(x ) s(x ) p(x ) r (x ) p(x ) × r (x )

$their product is           ´      =$

q(x ) s(x ) q(x ) × s(x ) In other words, the product of two rational expression is the product of their numerators divided by the product of their denominators and the resulting expression is then reduced to its lowest form.

**Division of Rational Expressions**

p(x ) r (x ) If and are two rational expressions, where q(x ), s(x ) ¹ 0 then, q(x ) s(x ) p(x ) r (x ) p(x ) s(x ) p(x ) × s(x )

$\\div √       =      \\times       =$

q(x ) s(x ) q(x ) r (x ) q(x ) × r (x ) Thus division of one rational expression by other is equivalent to the product of first and reciprocal of the second expression. If the resulting expression is not in its lowest form then reduce to its lowest form.

### Progress Check

Find the unknown expression in the following figures.

1.                                                                  2.                altitude =
2(x + y ) m x −y

$(x - 4)(x + 3)                 breadth = ?$

$Area =                     km 2                                                       (x > y)$

3x − 12

$Area=?$

x -3

$length =        km                                 base = (x+y)(x+y)m$

3

![Fig. 3.5]()

![Fig. 3.6]()

x3 27y x 4b 2 x2 -1

**Example 3.15**
(i) Multiply by 5 (ii) Multiply by 4 3

9y 2 x x -1 ab x 3 27y 3 xb4 2 x − 1 x × b (x + 1)(x − 1) x 4 (x + 1) 2 4 2 Solution (i) ´ 5 = 2 (ii) × = × = 9y 2 x xy x − 1 a 4b 3 x −1 a 4 ×b 3 a 4b

**Example 3.16**
Find

14x 4 7x x 2 − 16 x − 4 16x 2 − 2x − 3 8x 2 + 11x + 3

(i)       ÷
√ 4 (ii) ÷ (iii) 2 ÷ 2 y 3y x +4 x +4 3x − 2x − 1 3x − 11x − 4

14x 4 7x 14x 4 3y 4 Solution : (i) ÷√ 4 = × = 6x 3y 3 y 3y y 7x 2 x − 16 x − 4 (x + 4)(x − 4)  x + 4 

(ii)          ÷       =                 ×          = x + 4
x +4 x +4 (x + 4)  x − 4  16x 2 − 2x − 3 8x 2 + 11x + 3 16x 2 − 2x − 3 3x 2 − 11x − 4

(iii)                                     ÷                 =                ×
3x 2 − 2x − 1 3x 2 − 11x − 4 3x 2 − 2x − 1 8x 2 + 11x + 3 (8x + 3)(2x − 1) (3x + 1)(x − 4) (2x − 1)(x − 4) 2x 2 − 9x + 4

$=                   \\times                 =                 =$

(3x + 1)(x − 1) (8x + 3)(x + 1) (x − 1)(x + 1) x2 −1

**Exercise 3.5**

1. Simplify
4x 2y 6xz 3 p 2 − 10p + 21 p 2 + p − 12 5t 3 6t − 12

(i)         ´                  (ii)                 ×                  (iii)          ×
2z 2 20y 4 p −7 (p − 3)2 4t − 8 10t

2. Simplify
x +4 9x 2 − 16y 2 x 3 − y3 x 2 + 2xy + y 2

(i)           × 2            		                      (ii)                     ×
3x + 4y 2x + 3x − 20 3x 2 + 9xy + 6y 2 x 2 − y2

3. Simplify
2a 2 + 5a + 3 a 2 + 6a + 5 b 2 + 3b − 28 b 2 − 49

(i)               ÷                                  (ii) 2            ÷
2a 2 + 7a + 6 −5a 2 − 35 a − 50 b + 4b + 4 b 2 − 5b − 14 x + 2 x2 − x − 6 12t 2 − 22t + 8 3t 2 + 2t − 8

(iii)         ÷           			(iv)                ÷
4y 12y 2 3t 2t 2 + 4t

a 2 + 3a − 4 a 2 + 2a − 8

4. If x =               2
$and y =    2$

find the value of x 2y -2 . 3a − 3 2a − 2a − 4

5. If a polynomial p(x ) = x 2 − 5x − 14 is divided by another polynomial q(x ) we get
x −7 , find q(x ) . x +2

#### Activity 1 

(i) The length of a rectangular garden is the sum of a number
and its reciprocal. The breadth is the difference of the square of the same number and its reciprocal. Find the length, breadth and the ratio of the length to the breadth of the rectangle.

(ii) Find the ratio of the perimeter to the area of the given 13x                                 37x
12x

triangle. 5x 35x

**Addition and Subtraction of Rational Expressions**

**Addition and Subtraction of Rational Expressions with Like Denominators**

(i) Add or Subtract the numerators
(ii) Write the sum or difference of the numerators found in step (i) over the common
denominator.

(iii) Reduce the resulting rational expression into its lowest form.
x 2 + 20x + 36 x 2 + 12x + 4

**Example 3.17**
Find − 2

x 2 − 3x − 28 x − 3x − 28 x + 20x + 36 x + 12x + 4 (x 2 + 20x + 36) − (x 2 + 12x + 4) 2 2 Solution − 2 = x 2 − 3x − 28 x − 3x − 28 x 2 − 3x − 28 8x + 32 8(x + 4) 8

$= 2                                                   =              =$

x − 3x − 28 (x − 7)(x + 4) x − 7

**Addition and Subtraction of Rational Expressions with unlike Denominators**

(i) Determine the Least Common Multiple of the denominator.
(ii) Rewrite each fraction as an equivalent fraction with the LCM obtained in
step (i). This is done by multiplying both the numerators and denominator of each expression by any factors needed to obtain the LCM.

(iii) Follow the same steps given for doing addition or subtraction of the rational
expression with like denominators.

### Progress Check

1.      Write an expression that represents the 2.   Find the base of the given parallelogram
perimeter of the figure and simplify. 4x 2 + 10x − 50 whose perimeter is (x − 3)(x + 5) 2 cm x +1 cm 3x x 5 m 3 x- 6 cm ? x2

1 1 1

**Example 3.18**
Simplify + 2

2 − 2 x − 5x + 6 x − 3x + 2 x − 8x + 15 1 1 1 Thinking Corner Solution 2 + 2 − 2 x − 5x + 6 x − 3x + 2 x − 8x + 15 Say True or False 1 1 1 1. The sum of two rational

$=                       +                -$

(x − 2)(x − 3) (x − 2)(x − 1) (x − 5)(x − 3) expressions is always a rational expression. (x − 1)(x − 5) + (x − 3)(x − 5) − (x − 1)(x − 2)

$=                                                            2. The product of two$

(x − 1)(x − 2)(x − 3)(x − 5) rational expressions 2 2 2 (x − 6x + 5) + (x − 8x + 15) − (x − 3x + 2) is always a rational = expression. (x − 1)(x − 2)(x − 3)(x − 5)

x 2 − 11x + 18 (x − 9)(x − 2)

$=                             =$

(x − 1)(x − 2)(x − 3)(x − 5) (x − 1)(x − 2)(x − 3)(x − 5) x −9

$=$

(x − 1)(x − 3)(x − 5)

**Exercise 3.6**

x (x + 1) x (1 − x ) x + 2 x −1 x3 y3

1. Simplify (i)                      +               (ii)        +             (iii)        +
x −2 x −2 x + 3 x −2 x −y y −x (2x + 1)(x − 2) (2x 2 − 5x + 2) 4x x +1

2. Simplify (i)                −                                    (ii)       −
x −4 x −4 x −1 x −1 2

1 2x 3 + x 2 + 3

3. Subtract 2   from
x +2 (x 2 + 2)2 x 2 + 6x + 8 3

4. Which rational expression should be subtracted from                           3
to get 2 x +8 x − 2x + 4 2x + 1 2x − 1 1 2B

5. If A =                     ,B=        find      - 2
2x − 1 2x + 1 A - B A - B2 x 1 (A + B )2 + (A − B )2 2(x 2 + 1)

6. If A =      ,B=         , prove that                       =
x +1 x +1 A÷B x (x + 1)2

7. Pari needs 4 hours to complete a work. His friend Yuvan needs 6 hours to complete
the same work. How long will it take to complete if they work together?

8. Iniya bought 50 kg of fruits consisting of apples and bananas. She paid twice as
much per kg for the apple as she did for the banana. If Iniya bought ₹ 1800 worth of apples and ₹ 600 worth bananas, then how many kgs of each fruit did she buy?

### 3.5 Square Root of Polynomials

The square root of a given positive real number is another number which when multiplied with itself is the given number. Similarly, the square root of a given expression p(x) is another expression q(x) which when multiplied by itself gives p(x), that is, q(x ). q(x ) = p(x ) So, q(x ) = p(x ) where q(x ) is the absolute value of q(x). The following two methods are used to find the square root of a given expression

(i) Factorization method                (ii) Division method
### Progress Check

1. Is x 2 + 4x + 4 a perfect square?                       2. What is the value of x in 3 x = 9 ?
3. The square root of 361x 4y 2 is _______. 4.                 a 2x 2 + 2abx + b 2 = _______.
5. If a polynomial is a perfect square then, its factors will be repeated _______ number
of times (odd / even).

#### 3.5.1 Find the Square Root by Factorization Method

**Example 3.19**
Find the square root of the following expressions

144 a 8 b 12 c 16

(i) 256(x - a ) (x - b) (x - c) (x - d )
8 4 16 20

(ii)
81 f 12g 4 h 14

Solution (i) 256(x - a )8 (x - b)4 (x - c)16 (x - d )20 = 16 (x − a )4 (x − b)2 (x − c)8 (x − d )10 144a 8b 12c 16 4 a 4b 6c 8

(ii)                                        =
81f 12g 4h 14 3 f 6g 2h 7

**Example 3.20**
Find the square root of the following expressions

(i) 16x 2 + 9y 2 − 24xy + 24x − 18y + 9                             (ii) (6x 2 + x − 1)(3x 2 + 2x − 1)(2x 2 + 3x + 1)
(iii)  15x 2 +
 ( 3 + 10 )x + 2   5x + (2 5 + 1)x + 2  3x + ( 2 + 2 3 )x + 2 2  2 2

Solution (i) 16x 2 + 9y 2 − 24xy + 24x − 18y + 9

$= (4x )2 + (-3y )2 + (3)2 + 2(4x )(-3y ) + 2(-3y )(3) + 2(4x )(3)$

$= (4x - 3y + 3)2 = 4x - 3y + 3$

(ii) (6x 2 + x − 1)(3x 2 + 2x − 1)(2x 2 + 3x + 1)
$= (3x - 1)(2x + 1)(3x - 1)(x + 1)(2x + 1)(x + 1) = (3x - 1)(2x + 1)(x + 1)$

(iii) First let us factorize the polynomials
$( 3 + 10 )x + 2 = 15x + 3x + 10x + 2$

15x 2 + 2

$= 3x ( 5x + 1) + 2 ( 5x + 1)$

$= ( 5x + 1) \\times  ( 3x + 2 )$

$5x + (2 5 + 1) x + 2 = 5x + 2 5x + x + 2$

2 2

$= 5x (x + 2) + 1(x + 2) = ( 5x + 1)(x + 2)$

$3x + ( 2 + 2 3 ) x + 2 2 = 3x + 2x + 2 3x + 2 2$

2 2

$= x ( 3x + 2 ) + 2 ( 3x + 2 ) = (x + 2)( 3x + 2 )$

Therefore,  ( 3 + 10 )x + 2   5x + (2 5 + 1)x + 2  3x + ( 2 + 2 3 )x + 2 2  2  15x +  2 2

$= ( 5x + 1) ( 3x + 2 )( 5x + 1)(x + 2) ( 3x + 2 )(x + 2) = ( 5x + 1) ( 3x + 2 )(x + 2)$

**Exercise 3.7**

1. Find the square root of the following rational expressions.
400x 4y 12z 16 7x 2 + 2 14x + 2 121(a + b)8 (x + y )8 (b − c)8

(i)                		                  (ii)                             (iii)
100x 8y 4z 4 1 1 81(b − c)4 (a − b)12 (b − c)4 x2 − x + 2 16

2. Find the square root of the following
(i) 4x 2 + 20x + 25 		                 (ii)     9x 2 − 24xy + 30xz − 40yz + 25z 2 + 16y 2
(iii) (4x 2 − 9x + 2) (7x 2 - 13x - 2) (28x 2 - 3x - 1)
 17  3  4 11 

(iv) 2x 2 +         x + 1  x 2 + 4x + 2  x 2 + x + 2
 6   2   3 3 

#### 3.5.2 Finding the Square Root of a Polynomial by Division Method

The long division method in finding the square root of a polynomial is useful when the degree of the polynomial is higher.

**Example 3.21**
Find the square root of 64x 4 − 16x 3 + 17x 2 − 2x + 1

Solution Note 8x 2 − x + 1 4 3 2 8x 2 64x − 16x + 17x − 2x + 1 Before proceeding to find the 64x 4 square root of a polynomial, (−) one has to ensure that the 16x 2 - x −16x 3 + 17x 2 degrees of the variables are −16x 3 + x 2 in descending or ascending (+) (−) order. 16x 2 − 2x + 1 16x 2 − 2x + 1 16x 2 − 2x + 1 (−) (+) (−) 0

Therefore, 64x 4 − 16x 3 + 17x 2 − 2x + 1 = 8x 2 − x + 1

**Example 3.22**
If 9x 4 + 12x 3 + 28x 2 + ax + b is a perfect square, find the values of a and b.

Solution 3x 2 + 2x + 4 4 3 2 3x 2 9x + 12x + 28x + ax + b 9x 4 (−) 6x 2 + 2x 12x 3 + 28x 2 12x 3 + 4x 2 (−) (−) 6x 2 + 4x + 4 24x 2 + ax + b 24x 2 + 16x + 16 (−) (−) (−) (a–16)x + (b–16)

Because the given polynomial is a perfect square a − 16 = 0 , b − 16 = 0 Therefore, a = 16, b = 16 .

**Exercise 3.8**

1. Find the square root of the following polynomials by division method
(i) x 4 − 12x 3 + 42x 2 − 36x + 9   (ii) 37x 2 − 28x 3 + 4x 4 + 42x + 9
(iii) 16x 4 + 8x 2 + 1 			(iv) 121x 4 − 198x 3 − 183x 2 + 216x + 144
2. Find the values of a and b if the following polynomials are perfect squares
(i) 4x 4 − 12x 3 + 37x 2 + bx + a      (ii) ax 4 + bx 3 + 361x 2 + 220x + 100
3. Find the values of m and n if the following polynomials are perfect sqaures
(i) 36x 4 − 60x 3 + 61x 2 − mx + n 		         (ii) x 4 − 8x 3 + mx 2 + nx + 16
### 3.6 Quadratic Equations

**Introduction**

Arab mathematician Abraham bar Hiyya Ha-Nasi, often known by the Latin name Savasorda, is famed for his book ‘Liber Embadorum’ published in 1145 AD(CE) which is the first book published in Europe to give the complete solution of a quadratic equation. For a period of more than three thousand years beginning from early civilizations to current times, humanity knew how to solve a general quadratic equation in terms of its co-efficients by using four arithmetical operations and extraction of roots. This process is called “Solving by Radicals”. Huge amount of research has been carried to this day in solving various types of equations.

**Quadratic Expression**

An expression of degree n in variable x is a 0x n + a1x n −1 + a2x n −2 + ... + an −1x + an where a 0 ¹ 0 and a1, a2 ,...an are real numbers. a 0 , a1, a2 , ... an are called coefficients of the expression. In particular an expression of degree 2 is called a Quadratic Expression which is

$expressed as p(x ) = ax 2 + bx + c, a ¹ 0 and a, b, c are real numbers.$

#### 3.6.1 Zeroes of a Quadratic Polynomial

Let p(x) be a polynomial. x=a is called zero of p(x) if p(a)=0

For example, if p(x)=x2–2x–8 then p(–2)=4+4–8 = 0 and p(4)= 16– 8 –8 = 0

Therefore, –2 and 4 are zeros of the polynomial p(x)=x2–2x–8.

#### 3.6.2 Roots of Quadratic Equations

Let ax 2 + bx + c = 0, (a ≠ 0) be a quadratic equation. The values of x such that the expression ax 2 + bx + c becomes zero are called roots of the quadratic equation

$ax 2 + bx + c = 0 .$

$We have, ax 2 + bx + c = 0$

 b c

$a x^2 + x +  = 0$

 a a   b c x2 + x + a a

$=0           (since a ≠ 0)$

2 2 b b  b  c x + (2x ) +   −   + 2

$=0$

2a  2a   2a  a 2 b  b  b2 c That is, x + (2x )  +   2

$= 2-$

 2a   2a  4a a 2   b 2 − 4ac

$x + b      =$

 2a  4a 2

b ± b 2 − 4ac

$x+    =$

2a 2a −b ± b 2 − 4ac

$x =$

2a −b + b 2 − 4ac -b - b 2 - 4ac Therefore, the roots are and 2a 2a

#### 3.6.3 Formation of a Quadratic Equation

If a and b are roots of a quadratic equation ax 2 + bx + c = 0 then −b + b 2 − 4ac −b − b 2 − 4ac

$a =                  and b =                .$

2a 2a −b + b 2 − 4ac − b − b 2 − 4ac −b

$Also,           \\alpha +\\beta  =                                  =$

2a a      −b + b 2 − 4ac   −b − b 2 − 4ac  c

**Note**

$and              \\alpha \\beta  =                     \\times$

$                   = .$

 2a 

$     2a           a         ax 2 + bx + c = 0$

 can equivalently Since, (x - a) and (x - b ) are factors of ax + bx + c = 0 , 2 be expressed as

$We have              (x - \\alpha )(x - \\beta  ) = 0          b   c$

$x2 +     x+ =0 .$

a a

$Hence, x^2 - (\\alpha  + \\beta  )x + \\alpha \\beta  = 0           since a≠0$

That is, x 2 - (sum of roots) x + product of roots = 0 is the general form of the quadratic equation when the roots are given.

#### Activity 2 

(2k+6)m Consider a rectangular garden in front of a house, whose dimensions are (2k + 6) metre

k metre and k metre. A smaller rectangular portion of the garden of dimensions k metre and 3 metres 3 metres is leveled. Find the area of the garden, not leveled. k metre

**Example 3.23**
Find the zeroes of the quadratic expression x 2 + 8x + 12 .

Solution Let p(x)= x 2 + 8x + 12 =(x+2)(x+6)

$p(–2)= 4 – 16 + 12=0$

$p(–6)= 36 – 48 + 12=0$

Therefore, –2 and –6 are zeros of p(x)= x 2 + 8x + 12

**Example 3.24**
Write down the quadratic equation in general form for which sum and

product of the roots are given below. 7 5 3 1

(i) 9, 14              (ii) - ,        		      (iii) - , -
2 2 5 2 Solution (i) General form of the quadratic equation when the roots are given is

$x^2 - (sum of the roots) x + product of the roots = 0$

$x^2 - 9x + 14 = 0$

 7 5

(ii) x 2 − −  x +      =0 Þ
$⇒ 2x 2 + 7x + 5 = 0$

 2  2

 3  1 10x 2 + 6x − 5

(iii) x 2 − −  x + −  = 0 ⇒                  =0
 5   2  10 Therefore, 10x 2 + 6x − 5 = 0 .

**Example 3.25**
Find the sum and product of the roots for each of the following quadratic

$equations : (i) x^2 + 8x - 65 = 0       (ii) 2x 2 + 5x + 7 = 0$

(iii) kx 2 − k 2x − 2k 3 = 0
Solution Let a and b be the roots of the given quadratic equation

(i)      x 2 + 8x − 65 = 0
$a = 1, b = 8, c = –65$

b c

$\\alpha +\\beta  =-      = –8 and \\alpha \\beta  = = –65$

a a

$\\alpha  + \\beta  = -8 ; \\alpha \\beta  = -65$

(ii) 2x 2 + 5x + 7 = 0
$a = 2, b = 5, c = 7$

b -5 c 7

$\\alpha +\\beta  =-           =    and \\alpha \\beta  = =$

a 2 a 2 5 7

$\\alpha  + \\beta  = - ; \\alpha \\beta  =$

2 2

(iii) kx 2 − k 2x − 2k 3 = 0
$a = k, b = -k 2 , c = –2k3$

b -(-k 2 ) c -2k 3

$\\alpha +\\beta  =-           =          =k and \\alpha \\beta  = =       =–2k 2$

a k a k

**Exercise 3.9**

1. Determine the quadratic equations, whose sum and product of roots are
5 -3

(i) -9, 20          (ii)     , 4     (iii)      , -1        (iv)     −(2 − a )2 , (a + 5)2
3 2

2. Find the sum and product of the roots for each of the following quadratic equations
1 10

(i) x 2 + 3x − 28 = 0          (ii) x 2 + 3x = 0       (iii) 3 +     = 2       (iv) 3y 2 − y − 4 = 0
a a

#### 3.6.4 Solving Quadratic Equations

We have already learnt how to solve linear equations in one, two and three variable(s). Recall that the values of the variables which satisfies a given equation are called its solution(s). In this section, we are going to study three methods of solving quadratic equation, namely factorization method, completing the square method and using formula.

**Solving a quadratic equation by factorization method.**

We follow the steps provided below to solve a quadratic equation through factorization method. Step 1: Write the equation in general form ax 2 + bx + c = 0 Step 2: By splitting the middle term, factorize the given equation. Step 3: After factorizing, the given quadratic equation can be written as product of two linear factors. Step 4: Equate each linear factor to zero and solve for x. These values of x gives the roots of the equation.

**Example 3.26**
Solve 2x 2 − 2 6 x + 3 = 0

Solution 2x 2 − 2 6 x + 3 = 2x 2 − 6 x − 6x + 3 (by spliting the middle term)

$= 2x          ( 2x - 3 ) - 3 ( 2x - 3 ) = ( 2x - 3 )( 2x - 3 )$

Now, equating the factors to zero we get,

$( 2x - 3 )( 2x - 3 ) = 0$

$( 2x - 3 ) = 0$

2

$2x - 3 = 0$

3 ∴ the solution is x = . 2

**Example 3.27**
Solve 2m 2 + 19m + 30 = 0

Solution 2m 2 + 19m + 30 = 2m 2 + 4m + 15m + 30 = 2m(m + 2) + 15(m + 2)

$= (m + 2)(2m + 15)$

Equating the factors to zero we get,

$(m + 2)(2m + 15) = 0$

−15

$m + 2 = 0 \\Rightarrow  m = – 2 or 2m + 15 = 0 we get, m =$

2 -15 Therefore, the roots are -2 , . 2 Some equations which are not quadratic can be solved by reducing them to quadratic equations by suitable substitutions. Such examples are illustrated below.

**Example 3.28**
Solve x 4 − 13x 2 + 42 = 0

Solution Let x 2 = a . Then, (x 2 )2 − 13x 2 + 42 = a 2 − 13a + 42 = (a − 7)(a − 6) Given, (a − 7)(a − 6) = 0 we get, a = 7 or 6.

Since a = x 2 , x 2 = 7 then, x = ± 7 or x 2 = 6 we get, x = ± 6

Therefore, the roots are x = ± 7 , ± 6 x x −1 1

**Example 3.29**
Solve + =2

x −1 x 2 x 1 x −1 Solution Let y = then = . x −1 y x x x −1 1 1 5 Therefore, + = 2 becomes y + = x −1 x 2 y 2 1 2y 2 − 5y + 2 = 0 then, y = , 2 2

x 1

$= we get, 2x = x - 1 implies x = -1$

x −1 2 x

$= 2 we get, x = 2x - 2 implies x = 2$

x −1 Therefore, the roots are x = −1 , 2.

**Exercise 3.10**

1. Solve the following quadratic equations by factorization method
(i) 4x 2 − 7x − 2 = 0                     (ii) 3(p 2 − 6) = p(p + 5)         (iii) a(a − 7) = 3 2
1

(iv) 2x 2 + 7x + 5 2 = 0                  (v) 2x 2 − x +       =0
8

2. The number of volleyball games that must be scheduled in a league with n teams is
n2 − n given by G (n ) = where each team plays with every other team exactly once. A 2 league schedules 15 games. How many teams are in the league?

Solving a Quadratic Equation by Completing the Square Method In deriving the formula for the roots of a quadratic equation we used completing the squares method. The same technique can be applied in solving any given quadratic equation through the following steps. Step 1: Write the quadratic equation in general form ax 2 + bx + c = 0 . Step 2: Divide both sides of the equation by the coefficient of x2 if it is not 1. Step 3: Shift the constant term to the right hand side. Step 4: Add the square of one-half of the coefficient of x to both sides. Step 5: Write the left hand side as a square and simplify the right hand side. Step 6: Take the square root on both sides and solve for x.

**Example 3.30**
Solve x 2 − 3x − 2 = 0

Solution x 2 − 3x − 2 = 0

$x^2 - 3x                 = 2 		             (Shifting the Constant to RHS)$

2 2 2 3 3 1 

$x - 3x +   = 2 +  $

2

 2   2  ( ) (Add  co-efficient of x  to both sides) 2  2   17 x − 3  = (writing the LHS as complete square)  2  4

3 17 x- =± (Taking the square root on both sides) 2 2 3 17 3 17

$x=       +    or x = -$

2 2 2 2 3 + 17 3 - 17 Therefore, x = , 2 2

**Example 3.31**
Solve 2x 2 − x − 1 = 0

Solution 2x 2 − x − 1 = 0 x 1

$x2 -    -   =0 		                    (\\div 2 make co-efficient of x^2 as 1)$

2 2 x 1

$x2 -   =$

2 2 2 2 x 1 1 1 x − +   2

$= +  $

2  4  2  4  2 2   3

$x - 1     =$

9

$=  $

 4  16  4  1 3 1

$x-                          = ± ⇒ x = 1, -$

4 4 2 Solving a Quadratic Equation by Formula Method The formula for finding roots of a quadratic equation ax 2 + bx + c = 0 (derivation −b ± b 2 − 4ac given in section 3.6.2) is x = . 2a The formula for finding roots of a quadratic equation was known to Ancient Babylonians, though not in a form as we derived. They found the roots by creating the steps as a verse, which is a common practice at their times. Babylonians used quadratic equations for deciding to choose the dimensions of their land for agriculture.

**Example 3.32**
Solve x 2 + 2x − 2 = 0 by formula method

Solution Compare x 2 + 2x − 2 = 0 with the standard form ax 2 + bx + c = 0

$a = 1, b = 2, c = -2$

−b ± b 2 − 4ac

$x =$

2a substituting the values of a, b and c in the formula we get,

−2 ± (2)2 − 4(1)(−2) −2 ± 12

$x=                       =        = -1 ± 3$

2(1) 2 Therefore, x = −1 + 3 , −1 − 3

**Example 3.33**
Solve 2x 2 − 3x − 3 = 0 by formula method.

Solution Compare 2x 2 − 3x − 3 = 0 with the standard form ax 2 + bx + c = 0

$a = 2, b = -3 , c = -3$

−b ± b 2 − 4ac

$x=$

2a substituting the values of a, b and c in the formula we get,

−(−3) ± (−3)2 − 4(2)(−3) 3 ± 33

$x =                         =$

2(2) 4 3 + 33 3 − 33 Therefore, x = x =, 4 4

**Example 3.34**
Solve 3p 2 + 2 5p − 5 = 0 by formula method.

Solution Compare 3p 2 + 2 5p − 5 = 0 with the Standard form ax 2 + bx + c = 0

$a = 3, b = 2 5, c = -5 .$

− b ± b 2 − 4ac

$p=$

2a substituting the values of a, b and c in the formula we get,

( ) 2 ± − 2 5± 2 5 − 4(3)(− 5) −2 5 ± 80 − 5 ± 2 5

$p=                                     =             =$

2(3) 6 3

5 Therefore, x = ,- 5 3

**Example 3.35**
Solve pqx 2 − (p + q )2 x + (p + q )2 = 0

Solution Compare the coefficients of the given equation with the standard form

$ax 2 + bx + c = 0$

$a = pq , b = -(p + q )2 , c = (p + q )2$

± b 2 − 4ac −b ±

$x=$

2a substituting the values of a, b and c in the formula we get, 2 − −(p + q )2  ± ± −(p + q )  − 4(pq )(p + q ) 2 2

$x =                $

2pq

± (p + q )4 − 4(pq )(p + q )2 (p + q )2 ±

$=$

2pq

(p + q )2 ± (p + q )2 (p + q )2 − 4pq 

$=                                         $

2pq (p + q )2 ± (p + q )2 (p 2 + q 2 + 2pq − 4 pq )

$=$

2pq (p + q )2 ± (p + q )2 (p − q )2

$=$

2pq (p + q )2 ± (p + q )(p − q ) (p + q ){(p + q ) ± (p − q )}

$=                                                      =$

2pq 2pq p +q p +q p +q p +q Therefore, x = × 2p , × 2q we get, x = , 2pq 2pq q p

#### Activity 3 

Serve the fishes (Equations) with its appropriate food (roots). Identify a fish which cannot be served?

$4x2+12x+9 =0$

$x2 + 6x + 9 =0$

$x2–x–20 =0$

2x 2

$–5x–12=0$

$x2 –1=0$

$3   3                                                         x2+16 = 0$

- ,- 2 2

4.5

1, –1 –4, 5 3 4,–4 – ,4 2 –3, –3

**Exercise 3.11**

1. Solve the following quadratic equations by completing the square method
5x + 7

(i) 9x 2 − 12x + 4 = 0 		                 (ii)          = 3x + 2
x −1

2. Solve the following quadratic equations by formula method
(i) 2x 2 − 5x + 2 = 0 		                    (ii) 2 f 2 − 6 f + 3 2 = 0         (iii) 3y 2 − 20y − 23 = 0
(iv) 36y 2 − 12ay + (a 2 − b 2 ) = 0
3. A ball rolls down a slope and travels a distance d = t 2 − 0.75t feet in t seconds. Find
the time when the distance travelled by the ball is 11.25 feet.

#### 3.6.5 Solving Problems Involving Quadratic Equations

Steps to solve a problem Step 1: Convert the word problem to a quadratic equation form Step 2: Solve the quadratic equation obtained in any one of the above three methods. Step 3: Relate the mathematical solution obtained to the statement asked in the question.

**Example 3.36**
The product of Kumaran’s age (in years) two years ago and his age four

years from now is one more than twice his present age. What is his present age? Solution Let the present age of Kumaran be x years.

$Two years ago, his age = (x - 2) years.$

Four years from now, his age = (x + 4) years. Given, (x − 2)(x + 4) = 1 +2x x 2 + 2x − 8 = 1 +2x Þ (x − 3)(x + 3) = 0 then, x = ±3 Therefore, x = 3 (Rejecting −3 as age cannot be negative) Kumaran’s present age is 3 years.

**Example 3.37**
A ladder 17 feet long is leaning against a wall. If the ladder, vertical wall

and the floor from the bottom of the wall to the ladder form a right triangle, find the height of the wall where the top of the ladder meets if the distance between bottom of the wall to bottom of the ladder is 7 feet less than the height of the wall? A

Solution Let the height of the wall AB = x feet As per the given data BC = (x–7) feet x

$In the right triangle ABC, AC =17 ft, BC = (x–7) feet                          17$

fe e wall

t

$By Pythagoras theorem, AC 2 = AB 2 + BC 2$

$(17)2 = x^2 + (x - 7)2 ; 289 = x^2 + x^2 - 14x + 49                       B      x–7       C$

![Fig. 3.7]()

x 2 − 7x − 120 = 0 hence, (x − 15)(x + 8) = 0 then, x = 15 (or) −8

Therefore, height of the wall AB = 15 ft (Rejecting −8 as height cannot be negative)

**Example 3.38**
A flock of swans contained x 2 members. As the clouds gathered, 10x went

to a lake and one-eighth of the members flew away to a garden. The remaining three pairs played about in the water. How many swans were there in total? Solution As given there are x2 swans. 1 As per the given data x 2 − 10x − x 2 = 6 we get, 7x 2 − 80x − 48 = 0 8 −b ± b 2 − 4ac 80 ± 6400 − 4(7)(−48) 80 ± 88

$x =                 =                     =$

2a 14 14

4 Therefore, x = 12, - . 7 4 Here x = - is not possible as the number of swans cannot be negative. 7 Hence, x = 12. Therefore total number of swans is x 2 = 144.

**Example 3.39**
A passenger train takes 1 hr more than an express train to travel a distance

of 240 km from Chennai to Virudhachalam. The speed of the express train is more than that of the passenger train by 20 km per hour. Find the average speed of both the trains. Solution Let the average speed of passenger train be x km/hr. Then the average speed of express train will be (x + 20) km/hr

$Time taken by the passenger train to cover distance of 240 km =       hr$

x

$Time taken by express train to cover distance of 240 km =           hr$

x + 20 240 240 Given, = +1 x x + 20 1 1   x + 20 − x 

$240  -          = 1 \\Rightarrow  240                = 1 we get, 4800 = (x^2 + 20x )$

 x x + 20   x (x + 20)     

$x^2 + 20x - 4800 = 0 \\Rightarrow  (x + 80)(x - 60) = 0 we get, x = –80 or 60.$

Therefore x = 60 (Rejecting -80 as speed cannot be negative) Average speed of the passenger train is 60 km/hr Average speed of the express train is 80 km/hr.

**Exercise 3.12**

1. If the difference between a number and its reciprocal is
, find the number. 5

2. A garden measuring 12m by 16m is to have a pedestrian pathway that is ‘w’ meters
wide installed all the way around so that it increases the total area to 285 m2. What is the width of the pathway?

3. A bus covers a distance of 90 km at a uniform speed. Had the speed been 15 km/hour
more it would have taken 30 minutes less for the journey. Find the original speed of the bus.

4. A girl is twice as old as her sister. Five years hence, the product of their ages (in
years) will be 375. Find their present ages.

5. A pole has to be erected at a point on the boundary of a circular ground of diameter
20 m in such a way that the difference of its distances from two diametrically opposite fixed gates P and Q on the boundary is 4 m. Is it possible to do so? If answer is yes at what distance from the two gates should the pole be erected?

6. From a group of 2x 2 black bees , square root of half of the group went to a tree. Again
eight-ninth of the bees went to the same tree. The remaining two got caught up in a fragrant lotus. How many bees were there in total?

7. Music is been played in two opposite galleries with certain group of people. In the
first gallery a group of 4 singers were singing and in the second gallery 9 singers were singing. The two galleries are separated by the distance of 70 m. Where should a person stand for hearing the same intensity of the singers voice? (Hint: The ratio of the sound intensity is equal to the square of the ratio of their corresponding distances).

8. There is a square field whose side is 10 m. A square flower bed is prepared in its
centre leaving a gravel path all round the flower bed. The total cost of laying the flower bed and gravelling the path at ₹3 and ₹4 per square metre respectively is ₹364. Find the width of the gravel path.

9. The hypotenuse of a right angled triangle is 25 cm and its perimeter 56 cm. Find
the length of the smallest side.

#### 3.6.6 Nature of Roots of a Quadratic Equation

The roots of the quadratic equation ax 2 + bx + c = 0 , a ¹ 0 are found using the

formula x = -b ± b - 4ac . Here, b 2 - 4ac called as the discriminant (which is denoted 2

2a by D ) of the quadratic equation, decides the nature of roots as follows

Values of Discriminant Nature of Roots 2

$\\Delta  = b - 4ac$

D >0 Real and Unequal roots

$D =0              Real and Equal roots$

D< 0 No Real root

**Example 3.40**
Determine the nature of roots for the following quadratic equations

(i) x 2 − x − 20 = 0           (ii) 9x 2 − 24x + 16 = 0    (iii) 2x 2 − 2x + 9 = 0
Solution (i) x 2 − x − 20 = 0 Here, a = 1 , b = −1 , c = −20

$Now, \\Delta  = b 2 - 4ac$

$\\Delta  = (-1)2 - 4(1)(-20) = 81$

Here, ∆ = 81 > 0 . So, the equation will have real and unequal roots

(ii) 9x 2 − 24x + 16 = 0
Here, a = 9 , b = −24 , c = 16

$Now, \\Delta  = b 2 - 4ac = (-24) - 4 (9)(16) =0$

2

Here, ∆ = 0 . So, the equation will have real and equal roots.

(iii) 2x 2 − 2x + 9 = 0
Here, a = 2 , b = −2 , c = 9

$Now, \\Delta  = b 2 - 4ac = (-2) - 4 (2)(9) = -68$

2

Here, ∆ = −68 < 0 . So, the equation will have no real roots.

**Example 3.41**
(i) F

 ind the values of ‘k’, for which the quadratic equation

$kx 2 - (8k + 4)x + 81 = 0 has real and equal roots?$

(ii) F
 ind the values of ‘k’ such that quadratic equation

$(k + 9)x^2 + (k + 1)x + 1 = 0 has no real roots?$

Solution (i) kx 2 − (8k + 4)x + 81 = 0 Since the equation has real and equal roots, ∆ = 0 . That is, b 2 − 4ac = 0 Here, a = k , b = −(8k + 4) , c = 81 2 That is,  

$-(8k + 4) - 4(k )(81) = 0$

$64k 2 + 64k + 16 - 324k = 0$

$64k 2 - 260k + 16 = 0$

Dividing by 4 we get 16k 2 − 65k + 4 = 0 1 (16k − 1)(k − 4) = 0 then, k = or k = 4

(ii) (k + 9)x 2 + (k + 1)x + 1 = 0
Since the equation has no real roots, ∆ < 0 That is, b 2 − 4ac < 0 Here, a = k + 9 , b = k + 1 , c = 1 That is, (k + 1)2 − 4(k + 9)(1) < 0

k 2 + 2k + 1 − 4k − 36 < 0

k 2 − 2k − 35 < 0

(k + 5)(k − 7) < 0

Therefore, −5 < k < 7 . {If α < β and if (x − α)(x − β ) < 0 then, α < x < β }.

**Example 3.42**
Prove that the equation x 2 (p 2 + q 2 ) + 2x (pr + qs ) + r 2 + s 2 = 0 has no real

roots. If ps = qr , then show that the roots are real and equal.

Solution The given quadratic equation is, x 2 (p 2 + q 2 ) + 2x (pr + qs ) + r 2 + s 2 = 0 Here, a = p 2 + q 2 , b = 2(pr + qs ) , c = r 2 + s 2 2

$Now, \\Delta  = b 2 - 4ac = 2(pr + qs ) - 4(p 2 + q 2 )(r 2 + s 2 )$

$= 4  p 2r 2 + 2pqrs + q 2s 2 - p 2r 2 - p 2s 2 - q 2r 2 - q 2s 2 $

 

$= 4 -p s + 2pqrs - q r  = -4 (ps - qr )  <0$

2 2 2 2 2 ...(1)    

$since, D = b - 4ac < 0 , the roots are not real.$

2

2 2 If ps = qr then D = −4  ps − qr  = −4 qr − qr  = 0 (using (1)) Thus, D = 0 if ps = qr and so the roots will be real and equal.

**Exercise 3.13**

1. Determine the nature of the roots for the following quadratic equations
(i) 15x 2 + 11x + 2 = 0                 (ii) x 2 − x − 1 = 0       (iii) 2t 2 − 3t + 3 2 = 0
(iv) 9y 2 − 6 2y + 2 = 0                (v) 9a 2b 2x 2 − 24abcdx + 16c 2d 2 = 0 , a ¹ 0 , b ¹ 0
2. Find the value(s) of ‘k’ for which the roots of the following equations are real and
$equal. (i) (5k - 6)x^2 + 2kx + 1 = 0 		   (ii) kx 2 + (6k + 2)x + 16 = 0$

3. If the roots of (a − b)x 2 + (b − c)x + (c − a ) = 0 are real and equal, then prove that b,
a, c are in arithmetic progression.

4. If a, b are real then show that the roots of the equation
$(a - b)x^2 - 6(a + b)x - 9(a - b) = 0 are real and unequal.$

5. If the roots of the equation (c 2 − ab)x 2 − 2(a 2 − bc)x + b 2 − ac = 0 are real and equal
prove that either a=0 (or) a 3 + b 3 + c 3 = 3abc

### Thinking Corner

Fill in the empty box in each of the given expression so that the resulting quadratic polynomial becomes a perfect square.

(i) x 2 + 14x +              (ii) x 2 − 24x +            (iii) p 2 + 2qp +
#### 3.6.7 The Relation between Roots and Coefficients of a Quadratic Equation

Let a and b are the roots of the equation ax 2 + bx + c = 0 then, −b + b 2 − 4ac −b − b 2 − 4ac

$a =                  ,          b =$

2a 2a From 3.6.3, we get −b −Co-efficient of x

$\\alpha +\\beta  =           =$

a Co -efficient of x 2

c Constant term

$\\alpha \\beta  =     =$

a Co-efficient of x 2

### Progress Check

Roots of co-efficients Sum Product Quadratic quadratic of x 2 , x and of of constants b c Conclusion equation equation Roots roots - α and β α+β αβ a a

$4x2–9x+2=0$

2  

$x - 4  = 0$

 5 

$2x2–15x–27=0$

**Example 3.43**
If the difference between the roots of the equation x 2 − 13x + k = 0 is 17

find k. Solution x 2 − 13x + k =0 here, a = 1 , b = −13 , c = k Thinking Corner If the constant term Let ,  be the roots of the equation. Then of ax2+bx+c=0 is −b −(−13) zero, then the sum

$\\alpha  + \\beta  =              =          = 13 ...(1) Also \\alpha  - \\beta  = 17 ...(2) and product of roots$

a 1 are and

$(1)+(2) we get, 2a = 30 \\Rightarrow  a = 15$

. Therefore, 15 + b = 13 (from (1)) Þ b = −2 c k

$But, \\alpha \\beta  =                           = \\Rightarrow  15 \\times  (-2) = k we get, k = -30$

a 1

**Example 3.44**
If  and  are the roots of x 2 + 7x + 10 = 0 find the values of

α β α2 β 2

(i) (α - β )             (ii) α + β
2 2

(iii) α - β
3 3

(iv) α + β
4 4

(v)  +      (vi)   +
β α β α Solution x 2 + 7x + 10 = 0 here, a = 1 , b = 7 , c = 10

If  and  are roots of the equation then, −b −7 c 10

$\\alpha  + \\beta  =                        =   = -7 ; \\alpha \\beta  = =    = 10$

a 1 a 1

(i)          α-β        = (α + β )2 − 4αβ = (−7)2 − 4 × 10 = 9 =3
(ii) α2 + β 2 = (α + β )2 − 2αβ = (−7)2 − 2 × 10 = 29
(iii) α 3 - β 3 = (α − β )3 + 3αβ(α − β ) = (3)3 + 3(10)(3) =117
(iv) α 4 + β 4 = (α2 + β 2 )2 − 2α2 β 2 = 292 − 2 × (10)2 = 641 (from (ii), α2 + β 2 = 29 )
α β α2 + β 2 (α + β )2 − 2αβ 49 − 20 29

(v)            +  =         =               =       =
β α αβ αβ 10 10

α2 β 2 α 3 + β 3 (α + β )3 − 3αβ(α + β )

(vi)       +    =          =
β α αβ αβ

$=$

$(        ) = -343 + 210 = -133$

(−343) − 3 10 × (−7) 10 10 10

**Example 3.45**
If ,  are the roots of the equation 3x + 7x − 2 = 0 , find the values of

2

α β α2 β 2

(i) +        (ii)    +
β α β α Solution 3x + 7x − 2 = 0 here, a = 3 , b = 7 , c = −2 2

since, ,  are the roots of the equation −b −7 c −2

(i)           α+β =      =   ; αβ = =
a 3 a 3 2  −7      − 2  −2  α β α2 + β 2 (α + β )2 − 2αβ  3   3  −61

$+                           =          =                 =                              =$

β α αβ αβ −2 6 3 3  7     −  − 3 − 2  − 7  α2 β 2 α3 + β 3 (α + β )3 − 3αβ(α + β )  3   3   3  469

(ii)             +    =          =                         =                                      =
β α αβ αβ 2 18 − 3

**Example 3.46**
If ,  are the roots of the equation 2x 2 − x − 1 = 0 , then form the equation

1 1 whose roots are (i) , (ii) α2 β , β 2α (iii) 2α + β , 2β + α a b Solution 2x 2 − x − 1 = 0 here, a = 2 , b = −1 , c = −1 −b −(−1) 1 c 1

$\\alpha  + \\beta  =                   =       = ; \\alpha \\beta  = = -$

a 2 2 a 2 1 1

(i) Given roots are   ,
a b 1 1 1 α+β

$Sum of the roots = + =               = 2 = -1$

α β αβ 1 − 2 1 1 1 1

$Product of the roots = \\times  =          =      = -2$

α β αβ 1 − 2 The required equation is x2 –(Sum of the roots)x + (Product of the roots)=0

$x^2 - (-1)x - 2 = 0 \\Rightarrow  x^2 + x - 2 = 0$

(ii) Given roots are α2 β , β 2α
1 1   1

$Sum of the roots \\alpha 2 \\beta  + \\beta  2\\alpha  = \\alpha \\beta (\\alpha  + \\beta  ) = -   = -$

2  2  4

3  1 1

$Product of the roots (\\alpha  \\beta  ) \\times  (\\beta  \\alpha ) = \\alpha  \\beta  = (\\alpha \\beta  ) = -  = -$

2 2 3 3 3

 2  8

The required equation is x 2 - (Sum of the roots)x + (Product of the roots)=0  1 1

$x^2 - -  x - = 0 \\Rightarrow  8x 2 + 2x - 1 = 0$

 4  8

(iii) 2α + β , 2β + α
1 3

$Sum of the roots 2\\alpha  + \\beta  + 2\\beta  + \\alpha  = 3(\\alpha  + \\beta  ) = 3   =$

 2  2

$Product of the roots = (2\\alpha  + \\beta  )(2\\beta  + \\alpha ) = 4\\alpha \\beta  + 2\\alpha 2 + 2\\beta  2 + \\alpha \\beta$

 

$= 5\\alpha \\beta  + 2(\\alpha 2 + \\beta  2 ) = 5\\alpha \\beta  + 2 (\\alpha  + \\beta  ) - 2\\alpha \\beta  $

2

   1 1 1

$= 5 -  + 2  - 2 \\times -  =0$

 2  4 2   The required equation is x 2 - (Sum of the roots)x + (Product of the roots)=0 3

$x^2 - x + 0 = 0 \\Rightarrow  2x 2 - 3x = 0$

2

**Exercise 3.14**

1. Write each of the following expression in terms of α + β and αβ .
α β 1 1 α+3 β +3

(i)        +             (ii)      + 2           (iii) (3α - 1)(3β - 1)     (iv)          +
3β 3α 2 αβ βα β α

2. The roots of the equation 2x 2 − 7x + 5 = 0 are α and β. Without solving for the roots,
find 1 1 α β α +2 β +2

(i)     +                       (ii)    +               (iii)        +
α β β α β +2 α +2

3. The roots of the equation x 2 + 6x − 4 = 0 are α, β. Find the quadratic equation whose
roots are 2 2

(i) a2 and b 2                  (ii)     and            (iii) α2 β and β 2α
a b −13

4. If α, β are the roots of 7x 2 + ax + 2 = 0 and if β − α =                         . Find the values of a.
7

5. If one root of the equation 2y 2 − ay + 64 = 0 is twice the other then find the values
of a.

6. If one root of the equation 3x 2 + kx + 81 = 0 (having real roots) is the square of the
other then find k.

### 3.7 Graph of Variations

**Variables:**

Every day, Harini travels from her home, cycling at a uniform speed, to reach her school. You can state this mathematically by an equation d = rt, where d stands for distance travelled at any time t and r is the uniform rate of speed. Suppose you want to find the distance covered by her at a speed of 20 km per hour when she has cycled for fifteen minutes. 1 1 r = 20 and t = (how?) and we find d to be rt = 20 × = 5 km. 4 4 Here, we say that d is a dependent variable and r and t are independent variables. As the distance d travelled upon the rate r and time used t. Thus, an independent variable represents a quantity that is manipulated in a given situation where as a dependent variable represents a quantity whose value depends on how the independent variable is manipulated. Equations that describe the relationship between two variables in a sentence express the variation between those variables. Consider the monthly income of Server Suresh who works in a hotel where he is paid ` 50 per hour. There are two variables here. One is the monthly income and the other is the number of hours he works. Which among the two is the independent variable?

**Constants:**

You know how to calculate the area of a circle when the length of its radius is given. If the area required is A and the length of radius is r, then the formula

$A = pr2$

gives the required result. Here, the area A depends upon the length r of radius; thus A is a dependent variable and r is the independent variable. But what can we say about p? It is a number that remains the same in all the situations. It is constant. A constant is a quantity that assumes a fixed value throughout in a specific mathematical context.

**Two types of variation:**

When two things are in proportion, there is a relation between them, due to which, if the value of one of them 1000 (5,1000) 900 Scale changes, the value of the other also changes. We look into x axis 1 cm = 1 kg

$y axis 1 cm = `100$

800 (4,800) two types of variations here: 0x

(i) Direct variation
Cost (`)

600 (3,600)

$y=$

(ii) Indirect variation.                                                    500
(i) Direct variation:                                                            400             (2,400)
When you go to the market, to buy more apples, you’ll 200 (1,200) have to spend more amount of m ­ oney. If the cost of one kg 100 of apples is ` 200, you pay as follows: 1 2 3 4 5 6 7 8

Weight (Kg) 1 2 3 4 5 Weight (Kg)

![Fig. 3.8]()

Cost (`) 200 400 600 800 1000

1 2 3 4 5 You find that = = = = = ... 200 400 600 800 1000 This kind of proportionate variation is known as Direct variation. Here to find the cost, the weight is multiplied by the constant 200. If we denote the variable weight as x and the variable cost as y we can express this algebraically as y = 200x. The multiplying constant here is 200.

y If = k where k is a positive number (a constant), then x and y are said to vary directly. x Here, k is known as the constant of proportionality.

Mathematics in real life: This figure shows that doubling the force doubles the displacement. This is a consequence of what is known as Hooke’s law. It states F = kx where F is the force needed to produce a displacement of x in the position of a spring. To double the displacement, you double the force on the spring; the constant of proportionality k depends on the stiffness of the spring. So this is an example of a direct proportionality.

**Visualising Direct variation:**

### Thinking Corner

To identify direct variation is to look at the equation and determine if it is of What can you say if the variables x and y the form y = kx, where k is the constant of are related by the equation 3y – 7x = 0? proportionality. Thus, an equation like y = 5x It also indicates direct variation. How? will always indicate direct proportion among Think about it. In that case, what is the variables. constant of proportionality?

Observe this graph: The distance travelled and the time taken are proportional, but how do we know that? Note that Scale

$x axis 1 cm = 4 units$

i) The graph is a straight line.                                                   40
$y axis 1 cm = 4 units$

ii) The line passes through the origin. When both of these                         36
32 (16,32) features are present we know that the two quantities on Distance (km)

the graph must be directly proportional. 24 (12,24) 2x

Do you see this in the graph? 20

$y=$

16 (8,16) Time (in minutes) 4 8 12 16 12

Distance (in km) 8 16 24 32 8 (4,8) 4

If one variable doubles, the other also doubles. From 4 8 12 16 18 20 24 28 this you can see the relation d = rt and it is easy to guess the Time (minutes)

constant of proportionality. ![Fig. 3.9]()

**Example 3.47**
Varshika drew 6 circles with different

Scale

$sizes. Draw a graph for the relationship between the                                  x axis 1 cm = 1 unit$

$y axis 1 cm = 1 unit$

diameter and circumference (approximately related) of each circle as shown in the table and use it to find the circumference of a circle when its diameter is 6 cm.

Diameter (x) cm 1 2 3 4 5 Circumference (y) cm 3.1 6.2 9.3 12.4 15.5

Solution:

)x (3.1 From the table, we found that as x increses,

$y=$

y also increases. Thus, the variation is a direct variation. Let y = kx, where k is a constant of proportionality. From the given values, we have,

### 3.1 6.2 9.3 12.4

3.1x

$k=       =   =   =     = ... = 3.1$

1 2 3 4

$y=$

When you plot the points (1, 3.1) (2, 6.2) (3, 9.3), (4, 12.4), (5, 15.5), you find the relation

$y = (3.1)x forms a straight-line graph.$

Clearly, from the graph, when diameter is 6 cm, ![Fig. 3.10]() its circumference is 18.6 cm.

**Example 3.48**
A bus is travelling at a uniform speed of 50 km/hr. Draw the time-distance

graph and hence find

(i) the constant of variation
(ii) how far will it travel in 90 minutes?
(iii) the time required to cover a distance of 300 km from the graph.
**Solution**

Let x be the time taken in minutes and y be the distance travelled in km.

Time taken x (in minutes) 60 120 180 240 Distance y (in km) 50 100 150 200

(i) Observe that as time increases, the distance travelled also increases. Therefore, the
$variation is a direct variation. It is of the form y = kx .$

Constant of variation y 50 100 150 200 5

$k =           =   =   =   =   =$

x 60 120 180 240 6

Hence, the relation may be given as 5

$y = kx      \\Rightarrow           y= x$

6 5x

(ii) From the graph, y =                 , if x = 90 ,
5 6 Scale then y = ´ 90 = 75 km x axis 1 cm = 30 mins

$y axis 1 cm = 50 km$

6 The distance travelled for 90 minutes is 75 km. 300

5x

(iii) From the graph, y =    , if y = 300                                                         y=
5x 6 6 6y 6 then x = = ´ 300 = 360 minutes 5 5 (or) 6 hours.

The time taken to cover 300 km is 360 minutes (or) 6 hours.

![Fig. 3.11]()

(ii) Indirect variation:
The distance between Chennai and Madurai is (nearly) 480 km. Think of a train that starts from Chennai and travels towards Madurai. As it increases speed more and more, the time taken for travel will decrease. In the following table speed v is given in km and time t is given in hours:

Speed (v) (km/hr) 30 40 60 80 Time (t) (hours) 16 12 8 6

From the table it is clear that if you travel at a slower speed, the time increases and if the train is faster, the time decreases. You find, 30×16 = 40×12 = 60×8 = 80×6, which tells that vt is a constant. Here, vt = 480. In such a case, we say the variables v and t are inversely proportional. Observe that the graph of equation like vt = 480 will not be a straight line. Inverse Scale

$x axis 1 cm = 1 unit$

variation implies that as one variable increases, y axis 1 cm = 1 unit

the other variable decreases. 13

Visualising Indirect variation: 11

Look at the adjacent graph. It is a graph 9

of the equation xy = 8. We have taken only the 8 (1,8)

[positive values of x, y. 7

6

The table of values is: 5 (2,4) 4

x 1 2 4 8 3 (4,2) 2

$(8,1)        xy = 8$

8 1

$y=           8         4    2   1$

x 1 2 3 4 5 6 7 8 9 10 11 12 13

![Fig. 3.12]()

This is an illustration of inverse variation or indirect variation. The graph is a part of a curve called Rectangular Hyperbola.

**Example 3.49**
A company initially started with 40 workers to complete the work by 150

days. Later, it decided to fasten up the work increasing the number of workers as shown below.

Number of workers (x) 40 50 60 75 Number of days (y) 150 120 100 80

(i) Graph the above data and identify the type of variation.
(ii) From the graph, find the number of days required to complete the work if the company
decides to opt for 120 workers?

(iii) If the work has to be completed by 200 days, how many workers are required?
(i)
Scale

$x axis 1 cm = 10 workers$

$y axis 1 cm = 20 days$

xy

$=6$

0

![Fig. 3.13]()

From the given table, we observe that as x increases, y decreases. Thus, the variation is an inverse variation. k

$Let y =$

x ⇒ xy = k, k > 0 is called the constant of variation.

From the table, k = 40 ´ 150 = 50 ´ 120 = ... = 75 ´ 80 = 6000 Therefore, xy = 6000 Plot the points (40,150), (50,120), (60,100) of (75,80) and join to get a free hand smooth curve (Rectangular Hyperbola).

(ii) From the graph, the required number of days to complete the work when the
company decides to work with 120 workers is 50 days. 6000 Also, from xy = 6000 if x = 120 , then y = = 50

(iii) From the graph, if the work has to be completed by 200 days, the number of
workers required is 30.

Also, from xy = 6000 if y = 200, then x = 6000 = 30

**Example 3.50**

Nishanth is the winner in a Marathon race of 12 km distance. He ran at the uniform speed of 12 km/hr and reached the destination in 1 hour. He was followed by Aradhana, Jeyanth, Sathya and Swetha with their respective speed of 6 km/hr, 4 km/hr, 3 km/hr and 2 km/hr. And, they covered the distance in 2 hrs, 3 hrs, 4 hrs and 6 hours respectively. Draw the speed-time graph and use it to find the time taken to Kaushik with his speed of

### 2.4 km/hr.

Solution: Let us form the table with the given details.

Speed x (km/hr) 12 6 4 3 2 Time y (hours) 1 2 3 4 6 Scale From the table, we observe that as x axis 1 cm = 1 km

$y axis 1 cm = 1 hr$

x decreases, y increases. Hence, the type is inverse variation. k

$Let y =$

x ⇒ xy = k, k > 0 is called the constant

of variation. From the table k = 12 × 1 = 6 × 2 = …

$= 2 \\times  6 = 12$

Therefore, xy = 12. Plot the points (12,1), (6,2), (4,3), ![Fig. 3.14]() (3,4), (2,6) and join these points by a smooth curve (Rectangular Hyperbola). From the graph, we observe that Kaushik takes 5 hrs with a speed of 2.4 km/hr.

**Note**

Already we learned that, the linear equation of straight line is y = mx+c, where m is the slope of the straight line and c is the y – intercept. Also, the equation reduces to y = mx when the straight line passes through origin. As the graph of direct variation refer to straight line and its general form is y = kx, we can conclude that ‘constant of proportionality’ is nothing but ‘slope’ of its straight line.

**Exercise 3.15**

1. A garment shop announces a flat 50% discount on every purchase of items for their
customers. Draw the graph for the relation between the Marked Price and the Discount. Hence find

(i) the marked price when a customer gets a discount of ₹3250 (from graph)
(ii) the discount when the marked price is ₹2500
2. Draw the graph of xy = 24, x,y > 0. Using the graph find,
(i) y when x =3 and (ii) x when y = 6.
3. Graph the following linear function y = 1 x . Identify the constant of variation and
2 ­verify it with the graph. Also (i) find y when x = 9 (ii) find x when y = 7.5.

4. The following table shows the data about the number of pipes and the time taken to fill
the same tank.

No. of pipes (x) 2 3 6 9

Time Taken (in min) (y) 45 30 15 10

Draw the graph for the above data and hence

(i) find the time taken to fill the tank when five pipes are used
(ii) Find the number of pipes when the time is 9 minutes.
5. A school announces that for a certain competitions, the cash price will be distributed
for all the participants equally as show below

No. of participants (x) 2 4 6 8 10

Amount for each participant in ₹ (y) 180 90 60 45 36

(i) Find the constant of variation.
(ii)	Graph the above data and hence, find how much will each participant get if the
number of participants are 12.

6. A two wheeler parking zone near bus stand charges as below.
Time (in hours) (x) 4 8 12 24

Amount ₹ (y) 60 120 180 360

Check if the amount charged are in direct variation or in inverse variation to the parking time. Graph the data. Also (i) find the amount to be paid when parking time is 6 hr; (ii) find the parking duration when the amount paid is ₹150.

### 3.8 Quadratic Graphs

**Introduction**

The trajectory followed by an object (say, a ball) thrown upward at an angle gives a curve known as a parabola. Trajectory of water jets in a fountain or of a bouncing ball results in a parabolic path. A parabola represents a Quadratic function.

$A quadratic function has the form f (x ) = ax 2 + bx + c ,$

where a, b, c are constants, and a ≠ 0.

![Fig. 3.15]()

Many quadratic functions can be graphed easily by Y hand using the techniques of stretching/shrinking and 10 shifting the parabola y = x 2 (We can easily sketch the (–3, 9) (3, 9) curve y = x2 by preparing a table of values and plotting 8 the ordered pairs). 6 The “basic” parabola, y = x2, looks like this ![Fig.3.16](). The coefficient a in the general equation is (–2, 4) 4 (2, 4) responsible for parabolas to open upward or downward 2 and vary in “width” (“wider” or “skinnier”), but they all (–1, 1) (1, 1) have the same basic “ È ” shape. X′ –4 –2 0 2 4 X The greater the quadratic coefficient of x2, the Y′ narrower is the parabola. ![Fig. 3.16]() The lesser the quadratic coefficient of x2, the wider is the parabola.

Y Y

5 5

$y=4 2$

x

$y = x2$

4 4 4 x2

$y= 1$

$y = x2$

3 3

2 2

1 1

X′ –3 –2 –1 0 1 2 3 X X′ –3 –2 –1 0 1 2 3 X Y′ Y′

![Fig. 3.17]()

![Fig. 3.18]()

$Graph y = x^2 is broader than                             Graph y = x^2 is narrower than graph$

$graph y = 4x 2                                                                 1 2$

$y=         x$

4

A parabola is symmetric with respect to a line called the axis of symmetry. The point of intersection of the parabola and the axis of symmetry is called the vertex of the parabola. The graph of any second degree polynomial gives a curve called “parabola”.

−b Hint : For a quadratic equation , the axis is given by x = and the vertex is given by  −b −∆  2a  ,  where ∆ = b 2 − 4ac is the discriminant of the quadratic equation  2a 4a  ax 2 + bx + c = 0 . Where a ≠ 0.

We have already studied how to find the roots of any quadratic equation ax + bx + c = 0 where a,b,c Î ℝ and a ≠ 0 theoretically. In this section, we will learn how 2

to solve a quadratic equation and obtain its roots graphically.

#### 3.8.1 Finding the Nature of Solution of Quadratic Equations Graphically

To obtain the roots of the quadratic equation ax 2 + bx + c = 0 graphically, we first

$draw the graph of y = ax 2 + bx + c .$

The solutions of the quadratic equation are the x coordinates of the points of intersection of the curve with X axis. To determine the nature of solutions of a quadratic equation, we can use the following procedure.

(i) If the graph of the given quadratic equation intersect the X axis at two distinct
points, then the given equation has two real and unequal roots.

(ii) If the graph of the given quadratic equation touch the X axis at only one point, then
the given equation has only one root which is same as saying two real and equal roots.

(iii) If the graph of the given equation does not intersect the X axis at any point then the
given equation has no real root.

**Example 3.51**
Discuss the nature of solutions of the following quadratic equations.

(i) x 2 + x − 12 = 0 		 (ii) x 2 − 8x + 16 = 0  (iii) x 2 + 2x + 5 = 0
**Solution**

(i)       x 2 + x − 12 = 0
Step 1: Prepare the table of values for the equation y = x 2 + x − 12 .

x −5 −4 −3 −2 −1 0 1 2 3 4

y 8 0 −6 −10 −12 −12 −10 −6 0 8

Step 2: Plot the points for the above ordered Y Scale pairs (x, y) on the graph using x axis 1 cm = 1 unit

$y axis 1 cm = 2 units$

(−5, 8) 8 suitable scale.

) (4, 8 6 Step 3: Draw the parabola and mark the

2 x −1 4 co-ordinates of the parabola which

x2+ 2

$y=$

intersect the X axis. (−4, 0) (3, 0 )

X′ –6 –5 –4 –3 –2 –1 0 1 2 3 4 5 X Step 4: The roots of the equation are the x –2

coordinates of the intersecting points –4

(–4, 0) and (3,0)of the parabola –6 (−3, –6) (2, –6) with the X axis which are −4 and 3 –8

respectively. –10 (−2, –10) (1, –10)

Since there are two points of intersection (−1, –12) –12 (0, –12)

with the X axis, the quadratic equation –14

Y′

$x^2 + x - 12 = 0 has real and unequal roots.$

![Fig. 3.19]()

(ii) x − 8x + 16 = 0
2

Step 1: Prepare the table of values for the equation y = x 2 − 8x + 16 x −1 0 1 2 3 4 5 6 7 8 y 25 16 9 4 1 0 1 4 9 16

Step 2: Plot the points for the above ordered Y

pairs (x, y) on the graph using 26 Scale

$x axis 1 cm = 1 unit$

$(–1, 25)                                                  y axis 1 cm = 2 units$

suitable scale. 24

Step 3: Draw the parabola and mark the 20 coordinates of the parabola which 18

intersect with the X axis. 16 (0, 16) (8, 16)

Step 4: The roots of the equation are the x 14 8x +

coordinates of the intersecting points 12 x 2−

$y=$

of the parabola with the X axis (4,0) (1, 9) (7, 9) 8 which is 4. 6

Since there is only one point of intersection 4 (2, 4) (6, 4)

with X axis, the quadratic equation 2 ) (5, 1) (3, 1) ,0 (4 x 2 − 8x + 16 = 0 has real and equal roots. X′ –5 –4 –3 –2 –1 0 1 2 3 4 5 6 7 8 X –2

(iii) x 2 + 2x + 5 = 0                                                                                      Y′
![Fig. 3.20]()

$Let y = x^2 + 2x + 5$

Step 1: Prepare a table of values for the equation y = x 2 + 2x + 5 x −3 −2 −1 0 1 2 3 y 8 5 4 5 8 13 20

Y Step 2: Plot the above ordered pairs Scale

$x axis 1 cm = 1 unit      20              (3, 20)$

(x, y) on the graph using suitable y axis 1 cm = 2 units

5 2x + scale. 16

x 2+ Step 3: Join the points by a free-hand

$y=$

(2, 13) smooth curve this smooth curve 12

$is the graph of y = x^2 + 2x + 5                                                 10$

(−3, 8) 8 (1, 8) Step 4: The solutions of the given 6 quadratic equation are the x (−2, 5) 4 (0, 5)

coordinates of the intersecting (−1, 4) 2 points of the parabola the X axis. X –6 –5 –4 –3 –2 –1 0 1 2 3 4 5 6 7 X Here, the parabola doesn’t intersect Y

or touch the X axis. ![Fig. 3.21]()

So, we conclude that there is no real root for the given quadratic equation.

### Progress Check

Connect the graphs to its respective number of points of intersection with X axis and to its corresponding nature of solutions which is given in the following table.

S. No. Graphs Number of points of Nature of solutions Intersection with X axis Y

1. 2 Real and equal roots

X O X Y

Y

2. X O X 1 No real roots

Y Y O X X 2

3.                                                                      No real roots
Y

Y

0

4.                                                                      Real and equal roots
X O X Y

Y

5. X O X 0 Real and unequal roots

Y Y O X X

6.                                                     1                             Real and unequal roots
Y

#### 3.8.2 Solving quadratic equations through intersection of lines

We can determine roots of a quadratic equation graphically by choosing appropriate parabola and intersecting it with a desired straight line.

(i) If the straight line intersects the parabola at two distinct points, then the
x coordinates of those points will be the roots of the given quadratic equation.

(ii) If the straight line just touch the parabola at only one point, then the x coordinate
of the common point will be the single root of the quadratic equation.

(iii) If the straight line doesn’t intersect or touch the parabola then the quadratic
equation will have no real roots.

**Example 3.52**
Draw the graph of y = 2x 2 and Y

$hence solve 2x 2 - x - 6 = 0$

$x axis 1 cm = 1 unit$

$y axis 1 cm = 1 unit$

9 Solution Step 1: Draw the graph of y = 2x2 by 8 (2, 8) Scale 6

preparing the table of values as below + 8)

x 2,

$=$

7 (–

y

x −2 −1 0 1 2 (1,7) y 8 2 0 2 8 6 (0, 6) )

$Step 2: To solve 2x - x - 6 = 0 , subtract$

2 1 ,5 (– 5 2x 2 − x − 6 = 0 from y = 2x 2 2x 2 4)

$y = 2x 2                                                        4$

2,

$y=$

(–

(−)

$0 = 2x 2 - x - 6$

3

$y =x +6$

(–1, 2) 2 (1, 2) The equation y = x + 6 represents a

$straight line. Draw the graph of y = x+6 by                                                      1$

forming table of values as below (0, 0) x −2 −1 0 1 2 Y –2 –1 0 1 2 3 4 X y 4 5 6 7 8 Y

![Fig. 3.22]()

$Step 3: Mark the points of intersection of the curve y = 2x 2                                                   and the line$

y = x + 6 . That is, (–1.5, 4.5) and (2,8)

Step 4: The x coordinates of the respective points forms the solution set {–1.5,2} for

$2x 2 - x - 6 = 0$

**Example 3.53**
Draw the graph of Y

y = x 2 + 4x + 3 and hence find the roots of Scale

$2                                                                   x axis 1 cm = 1 unit                         (2, 15)$

$x +x +1 = 0                                                            y axis 1 cm = 2 units$

3

**Solution**

4x +

$Step 1: Draw the graph of y = x^2 + 4x + 3 by                                                              12$

x2+ preparing the table of values as below

$y=$

x −4 −3 −2 −1 0 1 2 (1, 8) 8

8) y

(2, 3 0 –1 0 3 8 15 6 Step 2: To solve

$x + x + 1 = 0 , subtract$

5) 2

(1, x + x + 1 = 0 from y = x 2 + 4x + 3 2 4 , 3)

$(-4                     (0, 3)           y=$

3x +

$y = x + 4x + 3$

2 2 2 (–) 0)

2)

$0 = x2 + x + 1$

3, (−1, 0 )

(0, (−

$y=        3x+2                    X       –4   –3        –2       –1      0          1        2        X$

(−2, –1) ) –1 –2 The equation represent a straight line. 1, (− )

$Draw the graph of y = 3x+2 forming the table                                                               –4$

–4 2,

of values as below. (−

Y x −2 −1 0 1 2 ![Fig. 3.23]() y –4 –1 2 5 8

Step 3: Observe that the graph of y = 3x+2 does not intersect or touch the graph of the

$parabola y = x^2 + 4x + 3 .$

$Thus x^2 + x + 1 = 0 has no real roots.$

**Example 3.54**
Draw the graph of y = x 2 + x − 2 and hence solve x 2 + x − 2 = 0 .

**Solution**

Step 1: Draw the graph of y = x 2 + x − 2 by preparing the table of values as below

x −3 −2 −1 0 1 2 y 4 0 –2 –2 0 4

Step 2: To solve x 2 + x − 2 = 0 subtract x 2 + x − 2 = 0 from y = x 2 + x − 2

Y that is y = x2 + x − 2

$x axis 1 cm = 1 unit$

$y axis 1 cm = 1 unit$

(–) (–3, 4) 4 (2, 4)

$0 = x2 + x - 2$

Scale

$y=        0                                                               3$

2 x− The equation y = 0 represents the X axis. 2

x 2+ Step 3: Mark the point of intersection of

$y=$

1 the curve y = x 2 + x − 2 with the (–2, 0) (1, 0) X axis. That is (–2,0) and (1,0) X –3 –2 –1 0 1 2 3 X Step 4: The x coordinates of the respective –1 points form the solution set {−2,1}

$for x^2 + x - 2 =0                                                                    (–1, –2)       –2        (0, –2)$

Y

**Example 3.55**
Draw the graph of

![Fig. 3.24]()

$y = x^2 - 4x + 3 and use it to solve x^2 - 6x + 9 = 0$

**Solution**

Step 1: Draw the graph of y = x 2 − 4x + 3 by preparing the table of values as below x −2 −1 0 1 2 3 4 y 15 8 3 0 –1 0 3 Step 2: To solve x 2 − 6x + 9 = 0 , subtract x 2 − 6x + 9 = 0 from y = x 2 − 4x + 3 that is y = x 2 − 4x + 3 Y (−) (–2, 15) Scale

$0 = x - 6x + 9               2$

$14                             x axis 1 cm = 1 unit$

3

$y axis 1 cm = 2 units$

− 4x +

$y=                                  2x - 6$

The equation y = 2x − 6 represent 2

$y =x$

a straight line. Draw the graph of y = 2x − 6 forming the table of values as 8 below. (–1, 8) y= 2x x 6 − 0 1 2 3 4 5 6 y –6 –4 –2 0 2 4 4 4) (0, 3) (4, 3) (5, The line intersect

$y = 2x - 6                                                   2                                               (4, 2)$

(3,

$y = x - 4x + 3 only at one point.$

2 (1, 0) 0) (3, 0) Step 3: Mark the point of intersection of X –2 –1 0 1 2 3 4 5 X – 1 )

$the curve y = x^2 - 4x + 3 and y = 2x - 6                                                    –2         (2,$

(2, –2) that is (3,0). –4 (1, –4) Therefore, the x coordinate 3 is the only solution for the equation –6 (0, –6)

$x^2 - 6x + 9 = 0 .                                                                                 Y$

![Fig. 3.25]()

**Exercise 3.16**

1. Graph the following quadratic equations and state their nature of solutions.
(i) x 2 − 9x + 20 = 0          (ii) x 2 − 4x + 4 = 0 (iii) x 2 + x + 7 = 0
(iv) x 2 − 9 = 0               (v) x 2 − 6x + 9 = 0               (vi) (2x − 3)(x + 2) = 0
2

2. Draw the graph of y = x − 4 and hence solve x 2 −x −12 = 0
3. Draw the graph of y = x 2 + x and hence solve x 2 + 1 = 0
4. Draw the graph of y = x 2 + 3x + 2 and use it to solve x 2 + 2x + 1 = 0
5. Draw the graph of y = x 2 + 3x − 4 and hence use it to solve x 2 + 3x − 4 = 0
6. Draw the graph of y = x 2 − 5x − 6 and hence solve x 2 − 5x − 14 = 0
7. Draw the graph of y = 2x 2 − 3x − 5 and hence solve 2x 2 − 4x − 6 = 0
8. Draw the graph of y = (x − 1)(x + 3) and hence solve x 2 − x − 6 = 0
### 3.9 Matrices

**Introduction**

Let us consider the following information. Vanitha has 12 story books, 20 notebooks and 4 pencils. Radha has 27 story books, 17 notebooks and 6 pencils. Gokul has 7 story books, 11 notebooks and 4 pencils. Geetha has 10 story books, 12 notebooks and 5 pencils. Details Story Books Note Books Pencils Vanitha 12 20 4 Radha 27 17 6 Gokul 7 11 4 Geetha 10 12 5 Now, we arrange this information in the tabular form as follows.

First row 12  20 4  Second row 27 17 6   Third row  7 11 4   Fourth row 10 12 5 First Second Third Column Column Column

Here, the items possessed by four people are aligned or positioned in a rectangular array containing four horizontal and three vertical arrangements. The horizontal arrangements are called “rows” and the vertical arrangements are called “columns”. The whole rectangular arrangement is called a “Matrix”. Generally, if we arrange things in a rectangular array, we call it as “ Matrix”. Applications of matrices are found in several scientific fields. In Physics, matrices are applied in the calculations of battery power outputs, resistor conversion of electrical

energy into other forms of energy. In computer based applications, matrices play a vital role in the projection of three dimensional image into a two dimensional screen, creating a realistic seeming motions. In graphic software, Matrix Algebra is used to process linear transformations to render images. One of the most important usage of matrices are encryption of message codes. The encryption and decryption process are carried out using matrix multiplication and inverse operations. The concept of matrices is used in transmission of codes when the messages are lengthy. In Geology, matrices are used for taking seismic surveys. In Robotics, matrices are used to identify the robot movements.

**Definition**

A matrix is a rectangular array of elements. The horizontal arrangements are called rows and vertical arrangements are called columns. 4 8 0  For example,   is a matrix. 1 9 −2 Usually capital letters such as A, B, C, X, Y, … etc., are used to represent the matrices and small letters such as a, b, c, l, m, n, a12 , a13 , ... to indicate the entries or elements of the matrices. The following are some examples of matrices  8 4 −1      3 + 1 2 −1   1  1 + x    5 4  x3 sin x  1.5 8 9 

(i)  2                    (ii)                              (iii)                           
 9 0 1   cos x 2 tan x   1 −7      13 3 9 

#### 3.9.1 Order of a Matrix

### Progress Check

If a matrix A has m number of rows and n number of columns, then the order of the matrix A 1. Find is the element in the second is (Number of rows)´ (Number of columns) that is, row and third column of the m ´n .We read m ´n as m cross n or m by n. It may 1 −2 3 matrix   be noted that m ´n is not a product of m and n. 2 1 5

General form of a matrix A with m rows 2. Find is the order of the matrix and n columns (order m ´n ) can be written in  sin q    the form  cos q    a ... a1n  tan q   11 a12 ... a1 j     a a22 ... a2 j ... a2n 

$A =  21                                                       3. Determine the entries denoted$

        by a11, a22 , a 33 , a 44 from the matrix   am 1 am 2 ... amj ... amn  2 1 3 4     where, a11, a12 ,... denote entries of the 5 9 −4 7    matrix. a11 is the element in first row, first 5  3 8 9  column, a12 is the element in the first row, second  2  7 4  column, and so on.  0 1

In general, aij is the element in the ith row and jth column and is referred as (i,j)th element. With this notation, we can express the matrix A as A = (aij )m×n where i = 1, 2,....m and

$j = 1, 2,...n .$

The total number of entries in the matrix A = (aij )m×n is mn.

**Note**

When giving the order of a matrix, you should always mention the number of rows first, followed by the number of columns.

For example, S.No. Matrices Elements of the matrix Order of the matrix

1.   sin q − cos q  a11 = sin q , a12 = −cos q ,
  cos q 2×2

$sin q  a21 = cos q , a22 = sin q$

 

2.      1        3           a11 = 1 , a12 = 3 ,
   

$    2 5           a21 = 2 , a22 = 5 ,                        3\\times 2$

 1   2 −4

$a 31 = 21 , a 32 = -4$

#### Activity 4 

(i) Take calendar sheets of a particular month in a particular year.
(ii) Construct matrices from the dates of the calendar sheet.
(iii) Write down the number of possible matrices of orders
2 ´ 2, 3 ´ 2, 2 ´ 3, 3 ´ 3, 4 ´ 3, etc.

(iv) Find the maximum possible order of a matrix that you can
create from the given calendar sheet.

(v) Mention the use of matrices to organize information from
daily life situations.

#### 3.9.2 Types of Matrices

In this section, we shall define certain types of matrices.

1. Row Matrix
A matrix is said to be a row matrix if it has only one row and any number of columns. A row matrix is also called as a row vector.  3  

$For example, A = (8 9 4 3) , B = -                                1   3  are row matrices of order 1´ 4$

 2  and 1×3 respectively.

$In general A = (a11 a12 a13 ... a1n ) is a row matrix of order 1´n .$

2. Column Matrix
A matrix is said to be a column matrix if it has only one column and any number of rows. It is also called as a column vector.

 8   sin x       5  −3   

$For example, A = cos x  , B =   and C =   are column matrices of order 3 ´ 1 ,$

    7   23   1     17  2 ´ 1 and 4 ´ 1 respectively.  a   11   a   21 

$In general, A = a 31  is a column matrix of order m ´1 .$

     a   m1 

3. Square Matrix
A matrix in which the number of rows is equal to the number of columns is called a square matrix. Thus a matrix A = (aij )m×n will be a square matrix if m = n −1 0 2 1 3     For example,   ,  3 6 8 are square matrices.  4 5   2×2   2 3 5 3×3 b  a   11 b12 b13  a  In general,  11 12  , b21 b22 b23  are square matrices of orders 2 ´ 2 and a21 a22    2×2 b31 b32 b33  3 ´ 3 respectively.

$A = (aij )m\\times m is a square matrix of order m.$

Definition : In a square matrix, the elements of the form a11, a22, a33, . . . (i.e) aii are 1 3   called leading diagonal elements. For example in the matrix 4 5 , 1 and 5 are leading   diagonal elements.

4. Diagonal Matrix
A square matrix, all of whose elements, except those in the leading diagonal are zero is called a diagonal matrix.

$(ie) A square matrix A = (aij ) is said to be diagonal matrix if aij = 0 for i ¹ j . Note$

that some elements of the leading diagonal may be zero but not all. 8 0 0  1 0 0     For example, 0 −3 0 , 0 1 0 are diagonal matrices.      0 0 11 0 0 0

5. Scalar Matrix
A diagonal matrix in which all the leading diagonal elements are equal is called a scalar matrix.

    4 0 k 0 0 5 0 0 For example,   , 0 k 0 , 0 5 0 0 4     0 0 k  0 0 5

$In general, A = (aij )m\\times m is said to be a scalar matrix if$

0 when i ≠ j aij =  where k is constant. k when i = j 

6. Identity (or) Unit Matrix
A square matrix in which elements in the leading diagonal are all “1” and rest are all zero is called an identity matrix or unit matrix.

$1 if i = j$

$Thus, the square matrix A = (aij ) is an identity matrix if aij = $

0 if i ≠ j A unit matrix of order n is written as I n . 

1 0 0 1 0    

$I 2 =         , I 3 = 0 1 0 are identity matrices of order 2 and 3 respectively.$

  0 1   0 0 1

7. Zero matrix (or) null matrix
A matrix is said to be a zero matrix or null matrix if all its elements are zero. 0 0 0  0 0  For example, (0),  0 0 0 are all zero matrices of order 1 ´ 1 , 2 ´ 2 and  ,   0 00 0 0   3 ´ 3 but of different orders. We denote zero matrix of order n ´ n by On . 0 0 0   is a zero matrix of the order 2 ´ 3 . 0 0 0

8. Transpose of a matrix
The matrix which is obtained by interchanging the elements in rows and columns of the given matrix A is called transpose of A and is denoted by AT . For example,  5 3 −1  5 2 −4     (a) If A =  2 8 9  then AT =  3 8 7      −4 7 5  −1 9 5  3×3 3×3

1 5   1 8 4 (b) If B = 8 9 then BT =     5 9 3 4 3 2×3 3×2

If order of A is m ´ n then order of AT is n ´ m . We note that (AT )T = A .

9. Triangular Matrix
A square matrix in which all the entries above the leading diagonal are zero is called a lower triangular matrix. If all the entries below the leading diagonal are zero, then it is called an upper triangular matrix.

Definition : A square matrix A = (aij )n×n is called upper triangular matrix if aij = 0 for i > j and is called lower triangular matrix if aij = 0 , i < j . 1 7 −3  8 0 0    

$For example, A = 0 2 4  is an upper triangular matrix and B =  4 5 0 is a$

    0 0 7  −11 3 1 lower triangular matrix. Equal Matrices Two matrices A and B are said to be equal if and Progress Check only if they have the same order and each element of matrix A is equal to the corresponding element of 1. The number of column(s) in a column matrix are matrix B. That is, aij = bij for all i, j. _______. 5 1 2. The number of row(s) in a

$For example, if A =               ,$

0 3 row matrix are _______.  12 + 22  3. The non-diagonal elements  sin2 q + cos2 q  then we in any unit matrix are

$B =                                         $

1 + 3 − 5 2 + sec2 q − tan2 q  ______.  2 2

note that A and B have same order and aij = bij for 4. Does there exist a square every i, j. Hence, A and B are equal matrices. matrix with 32 elements?

The negative of a matrix The negative of a matrix Am´n denoted by −Am×n is the matrix formed by replacing each element in the matrix Am´n with its additive inverse. Additive inverse of an element k is -k . That is, every element of –A is the negative of the corresponding element of A. 2 −4 9  −2 4 −9

$For example, if A =                  $

 then 

$-A =           $

5 − 3 − 1  −5 3 1  2×3 2×3

**Example 3.56**
Consider the following information regarding the number of men and

women workers in three factories I, II and III. Factory Men Women I 23 18 II 47 36 III 15 16 Represent the above information in the form of a matrix. What does the entry in the second row and first column represent?

Solution The information is represented in the form of a 3 ´ 2 matrix as follows 23 18   47 36 

$A =             $

  15 16 The entry in the second row and first column represent that there are 47 men workers in factory II.

**Example 3.57**
If a matrix has 16 elements, what are the possible orders it can have?

Solution We know that a matrix of order m ´ n , has mn elements. Thus to find all possible orders of a matrix with 16 elements, we will find all ordered pairs of natural numbers whose product is 16. Such ordered pairs are (1,16), (16,1), (4,4), (8,2), (2,8) Hence, possible orders are 1 ´ 16, 16 ´ 1 , 4 ´ 4 , 2 ´ 8 , 8 ´ 2

#### Activity 5 

No. Elements Possible orders Number of possible orders

1.          4                                             3
2.                      1×9, 9×1, 3×3
3.         20
4.          8                                             4
5.          1
6.        100
7.                  1×10, 10×1, 2×5, 5×2
Do you find any relationship between number of elements (second column) and number of possible orders (fourth column)? If so, what is it?

**Example 3.58**
Construct a 3 ´ 3 matrix whose elements are aij = i 2 j 2

a   11 a12 a13   Solution The general 3×3 matrix is given by A = a21 a22 a23  aij = i 2 j 2   a 31 a 32 a 33 

$a11 = 12 \\times  12 = 1 \\times  1 = 1 ;    a12 = 12 \\times  22 = 1 \\times  4 = 4 ;      a13 = 12 \\times  32 = 1 \\times  9 = 9 ;$

$a21 = 22 \\times  12 = 4 \\times  1 = 4 ;    a22 = 22 \\times  22 = 4 \\times  4 = 16 ;     a23 = 22 \\times  32 = 4 \\times  9 = 36$

$a 31 = 32 \\times  12 = 9 \\times  1 = 9 ;   a 32 = 32 \\times  22 = 9 \\times  4 = 36 ;    a 33 = 32 \\times  32 = 9 \\times  9 = 81$

1 4 9   

$Hence, the required matrix is A = 4 16 36$

  9 36 81  a −b 2a + c  1 5

**Example 3.59**
Find the value of a, b, c, d from the equation   =  

2a − b 3c + d  0 2

Solution The given matrices are equal. Thus all corresponding elements are equal.

Therefore, a − b = 1 …(1)

$2a + c = 5 		           …(2)$

$2a - b = 0 		          …(3)$

$3c + d = 2 		           …(4)$

$(3) \\Rightarrow                     2a - b = 0$

$2a = b 		          …(5)$

Put 2a = b in equation (1), a − 2a = 1 Þ a = −1 Put a = −1 in equation (5), 2(−1) = b Þ b = −2 Put a = −1 in equation (2), 2 (−1) + c = 5 Þ c = 7 Put c = 7 in equation (4), 3 (7) + d = 2 Þ d = −19 Therefore, a = −1, b = −2, c = 7, d = −19

**Exercise 3.17**

8  9 3 4     3 5

1. In the matrix A = −1                  7
2  , write (i) The number of elements   1 4 3 0  6   8 −11 1

(ii) The order of the matrix		                        (iii) Write the elements a22, a23, a24 , a 34 , a 43, a 44 .
2. If a matrix has 18 elements, what are the possible orders it can have? What if it has 6 elements?
3. Construct a 3 ´ 3 matrix whose elements are given by
(i + j )3

(i) aij = i − 2 j          (ii) aij =
3 5 4 3  

4. If A = 1 −7 9 then find the transpose of A.
  3 8 2  7 −3    

5. If A = − 5 2  then find the transpose of -A .
   3 −5    5  2 2    5 

6. If A = − 17             0. 7           then verify (AT )T = A
 2   8  3 1  

7. Find the values of x, y and z from the following equations
x + y + z  9 12 3 y z  x + y 2  6 2    

(i)         =           (ii)               =        (iii) x + z        = 5
 x 5 3 5  5 + z xy  5 8      7 y + z   

#### 3.9.3 Operations on Matrices

In this section, we shall discuss the addition and subtraction of matrices, multiplication of a matrix by a scalar and multiplication of matrices.

**Addition and subtraction of matrices**

Two matrices can be added or subtracted if they have the same order. To add or subtract two matrices, simply add or subtract the corresponding elements. a b c  g h i  a + g b + h c + i 

$For example,            +           =                       $

d e f   j k l  d + j e + k f + l      a − e b − f  a b  e f   

$c d  - g h  = c - g$

     d − h  If A = (aij ) , B = (bij ) , i = 1, 2, ... m , j = 1, 2, ... n then C = A + B is such that C = (cij ) where cij = aij + bij for all i = 1, 2, ... m and j = 1, 2, ... n 1  2 3 1 7 0   

**Example 3.60**
If A = 4 5 6 , B = 1 3 1 , find A+B.

    7 8 9 2 4 0 1 2  3 1 7 0  1 + 1 2 + 7 3 + 0 2 9 3        Solution A + B = 4 5 6 + 1 3 1 =  4 + 1 5 + 3 6 + 1 = 5 8 7         7 8 9 2 4 0 7 + 2 8 + 4 9 + 0 9 12 9

**Example 3.61**
Two examinations were conducted for three groups of students namely

group 1, group 2, group 3 and their data on average of marks for the subjects Tamil, English, Science and Mathematics are given below in the form of matrices A and B. Find the total marks of both the examinations for all the three groups. Tamil English Science Mathematics Group1 22 15 14 23  

$A = Group2 50                        62      21       30$

  Group3 53 80 32 40

Tamil English Science Mathematics Group1 20 38 15 40  

$B = Group2 18                      12      17       80$

  Group3 81 47 52 18

Solution The total marks in both the examinations for all the three groups is the sum of the given matrices. 22 + 20 15 + 38 14 + 15 23 + 40 42 53 29 63     

$A + B = 50 + 18 62 + 12 21 + 17 30 + 80 = 68$

 74 38 110     53 + 81 80 + 47 32 + 52 40 + 18 134 127 84 58 

1 3 −2 1 8    

**Example 3.62**
If A =  5 −4 6  , B = 3 4 , find A+B.

      −3 2 9  9 6 Solution It is not possible to add A and B because they have different orders. Multiplication of Matrix by a Scalar We can multiply the elements of the given matrix A by a non-zero number k to obtain a new matrix kA whose elements are multiplied by k. The matrix kA is called scalar multiplication of A. Thus if A = (aij )m×n then , kA = (kaij )m×n for all i = 1,2,…,m and ∀ j = 1,2,…,n.  7 8 6   4 11 −3    

**Example 3.63**
If A =  1 3 9  , B = −1 2 4  then Find 2A+B.

      −4 3 −1  7 5 0  Solution Since A and B have same order 3 ´ 3 , 2A + B is defined.  7 8 6   4 11 −3  14 16 12   4 11 −3        

$We have 2A+B = 2  1 3 9  + -1 2 4  =  2 6 18  + -1 2 4 $

             −4 3 −1  7 5 0  −8 6 −2  7 5 0   18 27 9   

$=  1             8 22 $

  −1 11 −2  5 4 −2 −7 4 −3      1 3   1 7 

**Example 3.64**
If A =  2  , B =  3  , find 4A - 3B .

 2 4   4 2   1 9 4   5 −6 9      Solution Since A, B are of the same order 3 ´ 3 , subtraction of 4A and 3B is defined. 5 4 −2 −7 4 −3      1 3   1 7 

$4A - 3B = 4                          2  - 3           3 $

 2 4   4 2   1 9 4   5 −6 9     

20 16 −8   21 −12 9        3 21 



$=  2 3 4 2  +  -       -    -9 $

   4 2   4 36 16  −15 18 −27      41 4 1     5 15 

$=         -    4 2 - 9$

 4 2  −11 54 −11   

Properties of Matrix Addition and Scalar Multiplication Let A, B, C be m ´ n matrices and p and q be two non-zero scalars (numbers). Then we have the following properties.

(i) A + B = B + A 			                     [Commutative property of matrix addition]
(ii) A + (B + C ) = (A + B ) + C           [Associative property of matrix addition]
(iii) (pq )A = p(qA) 			                    [Associative property of scalar multiplication]
(iv) IA=A 				[Scalar Identity property where I is the unit
matrix]

(v) p(A + B ) = pA + pB 		                [Distributive property of scalar and two matrices]
(vi) (p + q )A = pA + qA 		                 [Distributive property of two scalars with a matrix]
Additive Identity The null matrix or zero matrix is the identity for matrix addition. Let A be any matrix. Then, A + O = O + A = A where O is the null matrix or zero matrix of same order as that of A. Additive Inverse If A be any given matrix then –A is the additive inverse of A.

$In fact we have A + (-A) = (-A) + A = O$

**Example 3.65**
Find the value of a, b, c, d from the following matrix equation.

 d 8  3 a  2 2a   0 1   +    

$3b a  -2 -4 = b 4c  + -5 0$

       

**Solution**

First, we add the two matrices on both left, right hand sides to get d + 3 8 + a   2 2a + 1

$                              = $

   3b − 2 a − 4  b − 5 4c  Equating the corresponding elements of the two matrices, we have

$d + 3 = 2 		        \\Rightarrow  d = –1$

$8 + a = 2a + 1                            \\Rightarrow  a=7$

−3

$3b - 2 = b - 5                            \\Rightarrow  b=$

2 3 Substituting a = 7 in a − 4 = 4c Þ c = 4 3 3 Therefore, a = 7, b = − , c = , d = –1. 2 4

1 8 3 8 −6 −4 5 3 0      

**Example 3.66**
If A = 3 5 0 , B = 2 11 −3 , C = −1 −7 2

      8 7 6 0 1 5   1 4 3 1 3 compute the following : (i) 3A + 2B − C (ii) A - B 2 2 1 8 3 8 −6 −4  5 3 0       Solution (i) 3A + 2B − C = 3 3 5 0 + 2 2 11 −3 − −1 −7 2       8 7 6 0 1 5   1 4 3  3 24 9  16 −12 −8 −5 −3 0       

$=  9 15 0  +  4 22 -6 +  1$

   7 −2       24 21 18  0 2 10  −1 −4 −3 14 9  1  

$= 14 44 -8$

  23 19 25  1 3 1

(ii)
$A - B = (A - 3B )$

2 2 2 1 8 3 8 −6 −4     1   

$= 3 5 0 - 3 2 11 -3$

2     8 7 6 0 1 5  1 8 3 −24 18 12  −23 26 15       1     1  

$= 3 5 0 +  -6 -33 9  =  -3 -28 9 $

   2     2   8 7 6  0 −3 −15  8 4 −9  23 15  − 13   2 2   3 9 

$=  -                      -14             $

 2 2   9  4 2 −   2 

**Exercise 3.18**

1 9  5 7    

1. If A = 3 4 , B = 3 3 then verify that
      8 −3 1 0

(i) A + B = B + A            (ii) A + (−A) = (−A) + A = O.
4 3 1   2 3 4  8 3 4       

2. If A = 2 3 −8, B =  1 9 2  and C = 1 −2 3  then verify that
      1 0 −4 −7 1 −1 2 4 −1

$A + (B + C ) = (A + B ) + C .$

7 0 3 0

3. Find X and Y if X+Y =                       and X −Y =       
0 4 3 5   0 4 9 7 3 8

4. If A =       , B =         
1 4 9 find the value of (i) B - 5A (ii) 3A - 9B 8 3 7    x −3 3x − z  1 0

5. Find the values of x, y, z if (i)                          =     
x + y + 7 x + y + z  1 6

(ii) (x y − z z + 3) +(y 4 3) = (4 8 16)
 4  −2 4

6. Find x and y if x               +y   =  
−3  3  6    

7. Find the non-zero values of x satisfying the matrix equation
2x 2 8 5x  x 2 + 8 24

$x                        + 2         = 2            $

 3 x  4 4x   10 6x      x 2  −2x  5 

8. Solve for x, y :  2  + 2         =  
y   −y  8

Multiplication of Matrices 3×3 3×2 To multiply two matrices, the number of columns in the first matrix must be equal to the number of rows in the These numbers must be equal second matrix. Consider the multiplications of 3×3 and These numbers determine the 3×2 matrices. order of the Product Matrix.

(Order of left hand matrix) ´ (order of right hand matrix) ® (order of product matrix). (3 × 3 ) (3 × 2 ) ® (3 × 2 ) Matrices are multiplied by multiplying the elements in a row of the first matrix by the elements in a column of the second matrix, and adding the results. a b  ag + bk ah + bl ai + bm    g h i        For example, product of matrices c d  × 

$                     = cg + dk ch + dl ci + dm $

   k l m    e f  eg + fk eh + fl ei + fm  The product AB can be found if the number of columns of matrix A is equal to the number of rows of matrix B. If the order of matrix A is m ´ n and B is n ´ p then the order of AB is m ´ p . Properties of Multiplication of Matrix (a) Matrix multiplication is not commutative in general If A is of order m ´ n and B of the order n ´ p then AB is defined but BA is not defined. Even if AB and BA are both defined, it is not necessary that they are equal. In general AB ¹ BA.

(b) Matrix multiplication is distributive over matrix addition

(i) If A, B, C are m ´ n , n ´ p and n ´ p matrices respectively then
$A(B + C ) = AB + AC (Right Distributive Property)$

(ii) If A, B, C are m ´ n , m ´ n and n ´ p matrices respectively then
$(A + B )C = AC + BC (Left Distributive Property)$

(c) Matrix multiplication is always associative If A, B, C are m ´ n , n ´ p and p ´ q matrices respectively then (AB )C = A(BC )

(d) Multiplication of a matrix by a unit matrix If A is a square matrix of order n ´ n and I is the unit matrix of same order then

$AI = IA = A .$

**Note**

- If x and y are two real numbers such that xy = 0 then either x = 0 or y = 0 . But this
condition may not be true with respect to two matrices.

- AB = 0 does not necessarily imply that A = 0 or B = 0 or both A, B = 0
Illustration  1 −1 1 1

$         ≠ 0 and B =       $

$A =                         1 1 ≠ 0$

−1 1     1 −1 1 1  1−1 1 − 1  0 0

$        \\times    =                            $

$But         AB = $

$          -1 + 1 -1 + 1 = 0 0 = 0$

−1 1  1 1    

$Thus            A ¹ 0, B ¹ 0 but AB = 0 .$

8 3 1 1 2 0   

**Example 3.67**
If A =   , B = 2 4 1 , find AB.

   3 1 5 5 3 1   Solution We observe that A is a 2 ´ 3 matrix and B is a 3×3 matrix, hence AB is defined and it will be of the order 2 × 3. 8 3 1 1 2 0    Given A =   , B = 2 4 1 3 1 5   2×3 5 3 1  3×3 8 3 1 1 2 0  

$AB =             \\times 2 4 1$

3 1 5     5 3 1   8+4+0 3 + 8 + 0 1 + 2 + 0 12 11 3

$=                                                         =         $

24 + 2 + 25 9 + 4 + 15 3 + 1 + 5 51 28 9

2 1 2 0

**Example 3.68**
If A =   , B =  

1 3 find AB and BA. Verify AB = BA ? 1 3   Solution We observe that A is a 2 ´ 2 matrix and B is a 2 ´ 2 matrix, hence AB is defined and it will be of the order 2 ´ 2 . 2 1 2 0  4 + 1 0 + 3 5 3

$      \\times    =            =    $

$AB = $

  1 3 1 3 2 + 3 0 + 9 5 9  

2 0 2 1 4 + 0 2 + 0 4 2 

$BA =                               \\times    =             =     $

1 3 1 3 2 + 3 1 + 9  5 10    

Therefore, AB ¹ BA .  2 −2 2   2 2 2    

**Example 3.69**
If A =   and B = 

− 2   2 2   2   Show that A and B satisfy commutative property with respect to matrix multiplication. Solution We have to show that AB = BA  2 −2 2   2 2 2   2 2 2   2 −2 2     

$LHS = AB =           \\times                                          RHS = BA =              \\times           $

 2 2  − 2 2  − 2 2   2 2   4+4  4 2 − 4 2    4+4 −4 2 + 4 2 

$=                                         		          =                          $

2 2 − 2 2 4 + 4  −2 2 + 2 2 4 + 4      8 0 8 0   

$=                                         		          = $

0 8 0 8

$Hence, LHS = RHS (ie) AB = BA$

**Note**

2 1 x  4 ¾ If A and B are any two

**Example 3.70**
Solve     =  

1 2 y  5 non zero matrices, then 2 1 x   4 (A + B )2 ≠ A2 + 2AB + B 2 . Solution   ×   =   1 2   5 ¾ However if AB = BA then  2×2 y 2×1  

$(A + B )2 = A2 + 2AB + B 2$

2x + y  4

$By matrix multiplication                           =  $

x + 2y  5

$Rewriting 		                         2x + y = 4 			...(1)$

$x + 2y = 5 			...(2)$

$(1) -2 \\times  (2) \\Rightarrow                        2x + y = 4$

(−)

$2x + 4y = 10$

$-3y = - 6                  \\Rightarrow  y=2$

Substituting y = 2 in (1), 2x + 2 = 4 Þ x = 1 Therefore, x = 1 , y = 2 . 1 −1   1 2 

**Example 3.71**
If A = (1 −1 2) , B = 2 1  and C =  

  2 −1 1 3  show that (AB )C = A(BC ) .

Solution LHS = (AB )C 1 −1  

$AB = (1 -1 2)1\\times 3 \\times  2 1  = (1 - 2 + 2 -1 - 1 + 6) = (1 4)$

  1 3 3×2 1 2 

$        = (1 + 8 2 - 4) = (9 –2)$

$(AB )C         = (1 4)1\\times 2 \\times                                                            …(1)$

2 −1 2×2

$RHS = A(BC )$

1 −1 1 − 2 2 + 1 −1 3    1 2          

$BC = 2 1  \\times               = 2 + 2 4 - 1 =  4$

 3    2 −1     1 3 3×2 2×2 1 + 6 2 − 3  7 −1 −1 3   

$A(BC) = (1 -1 2)1\\times 3 \\times   4        3 $

   7 −1 3×2

$A(BC) = (-1 - 4 + 14                            3 - 3 - 2) = (9 -2) 				…(2)$

From (1) and (2), (AB )C = A(BC ) . 1 1  1 2 −7 6

**Example 3.72**
If A =   , B =   , C = 

−4 2  3 2 verify that A (B + C ) = AB + AC .  −1 3    

Solution LHS = A(B + C )  1 2 −7 6 −6 8

$       +     =     $

$B +C     = $

−4 2  3 2 −1 4  

 1 1 −6 8 −6 − 1 8 + 4  −7 12

$       \\times     =               =      $

$A(B + C ) =                                                              …(1)$

−1 3 −1 4  6 − 3 −8 + 12  3     4 

$RHS = AB + AC$

 1 1  1 2  1 − 4 2 + 2   −3 4

$        \\times       =                =       $

$AB = $

−1 3 −4 2 −1 − 12 −2 + 6 −13 4

 1 1 −7 6 −7 + 3 6 + 2  −4 8

$        \\times      =              =      $

$AC =                       $

−1 3  3 2  7 + 9 −6 + 6  16 0

 −3 4 −4 8 −7 12 Therefore, AB + AC =   +   =   …(2) −13 4  16 0  3 4 

From (1) and (2), A(B + C ) = AB + AC . Hence proved.  2 −1 1 2 1   

**Example 3.73**
If A =   and B = −1 4  show that (AB )T = BT AT

   2 −1 1  0   2 

**Solution**

$LHS = (AB )T                                           RHS = ( BT AT )$

1 2   2 −1  2 −1 0   1 2 1    

$ \\times  -1 4                                        , A = 2 -1$

 T T

$                                              B =$

$AB =                                                   -1 4 2                        $

 1 1  2 −1 12×3  0 2   3×2 1 2  2 − 2 + 0 −1 + 8 + 2 0 9   2 −1 0  

$                        =         T T $

$B A =                \\times   2 -1$

$=                                                                          $

4 + 1 + 0 −2 − 4 + 2 5 −4 −1 4 2 1 1  2×3  3×2 T 0 9  0 5   2−2 + 0 4 + 1 + 0 

$        =                                     $

$(AB )T =              9 -4            …(1)            =                         $

5 −4   −1 + 8 + 2 −2 − 4 + 2 0 5   

$BT AT =                                       …(2)$

9 −4

From (1) and (2), (AB )T = BT AT . Hence proved.

**Exercise 3.19**

1. Find the order of the product matrix AB if
(i)       (ii)    (iii)      (iv)       (v)
Orders of A 3×3 4×3 4×2 4×5 1×1 Orders of B 3×3 3×2 2×2 5×1 1×3

2. If A is of order p ´ q and B is of order q ´ r what is the order of AB and BA?
3. A has ‘a’ rows and ‘ a + 3 ’ columns. B has ‘b’ rows and ‘17–b’ columns, and if both
products AB and BA exist, find a, b? 2 5 1 −3

4. If A =      , B = 
  2 5  find AB, BA and verify AB = BA? 4 3   1 3  1 −1 2  1 3 2      

5. Given that A =             , B =          , C = 
5 −1 3 5 2 −4 1 3 verify that A(B + C ) = AB + AC .

1 2  1 −2

6. Show that the matrices A =                   , B =         
$-3 1  satisfy commutative propertyAB=BA$

3 1  

1 2 4 0 2 0

7. Let A =           , B = 


$ , C = $

1 5  1 2 Show that (i) A(BC ) = (AB )C 1 3    

(ii) (A − B )C = AC − BC (iii) (A − B )T = AT − BT
cos q 0  sin q 0 

8. If A =                          , B = 
 0  then show that A2 + B 2 = I .  0 cos q   sin q    cos q sin q 

9. If A =                     prove that AAT = I .
− sin q cos q  5 −4

10. Verify that A2 = I when A =                     
6 −5 a b  1 0

11. If A =          and I =          
0 1 show that A − (a + d )A = (bc − ad )I 2 2

c d    1 7  5 2 9  

12. If A =          , B = 1 2  verify that (AB )T = BT AT
1 2 8   5 −1   3 1

13. If A =                 show that A2 − 5A + 7I = 0
−1 2 2

**Exercise 3.20**

Multiple choice questions

1. A system of three linear equations in three variables is inconsistent if their planes
(A) intersect only at a point (B) intersect in a line (C) coincides with each other (D) do not intersect

2. The solution of the system x + y − 3z = −6 , − 7y + 7z = 7 , 3z = 9 is
$(A) x = 1, y = 2, z = 3                                (B) x = -1, y = 2, z = 3$

$(C) x = -1, y = -2, z = 3                              (D) x = 1, y = -2, z = 3$

3. If (x - 6) is the HCF of x 2 - 2x - 24 and x 2 - kx - 6 then the value of k is
(A) 3 (B) 5 (C) 6 (D) 8 3y − 3 7y − 7

4.             ÷      is
y 3y 2 9y 9y 3 21y 2 − 42y + 21 7(y 2 − 2y + 1) (A) (B) (C) ( D ) 7 (21y - 21) 3y 3 y2

1

5. y 2 +           is not equal to
y2 2 2 2 y4 + 1    1  1 (A) ( B ) y + 1  (C) y −  + 2 (D) y +  − 2 y2  y   y   y  x 8

6.           −            gives
x 2 − 25 x 2 + 6x + 5 x 2 − 7x + 40 x 2 + 7x + 40 (A) (B) (x − 5)(x + 5) (x − 5)(x + 5)(x + 1)

x 2 − 7x + 40 x 2 + 10 (C) (D) (x 2 − 25)(x + 1) (x 2 − 25)(x + 1)

256x 8y 4z 10

7. The square root of                         is equal to
25x 6y 6z 6 16 x 2z 4 y2 16 y 16 xz 2 (A) (B) 16 2 4 (C) (D) 5 y2 x z 5 xz 2 5 y

8. Which of the following should be added to make x 4 + 64 a perfect square
(A) 4x 2 (B) 16x 2 (C) 8x 2 (D) -8x 2

9. The solution of (2x − 1) = 9 is equal to
2

(A) -1 (B) 2 (C) –1, 2 (D) None of these

10. The values of a and b if 4x 4 − 24x 3 + 76x 2 + ax + b is a perfect square are
(A) 100,120 (B) 10,12 (C) -120 ,100 (D) 12,10

11. If the roots of the equation q 2x 2 + p 2x + r 2 = 0 are the squares of the roots of the
equation qx 2 + px + r = 0 , then q, p, r are in _______ (A) A.P (B) G.P (C) Both A.P and G.P (D) none of these

12. Graph of a linear equation is a _______
(A) straight line (B) circle (C) parabola (D) hyperbola

13. The number of points of intersection of the quadratic polynomial x 2 + 4x + 4 with
the X axis is (A) 0 (B) 1 (C) 0 or 1 (D) 2  1 3 5 7   

14. For the given matrix A =  2 4 6 8  the order of the matrix AT is
   9 11 13 15 (A) 2 ´ 3 (B) 3 ´ 2 (C) 3 ´ 4 (D) 4 ´ 3

15. If A is a 2 ´ 3 matrix and B is a 3 ´ 4 matrix, how many columns does AB have
(A) 3 (B) 4 (C) 2 (D) 5

16. If number of columns and rows are not equal in a matrix then it is said to be a
(A) diagonal matrix (B) rectangular matrix (C) square matrix (D) identity matrix

17. Transpose of a column matrix is
(A) unit matrix (B) diagonal matrix (C) column matrix (D) row matrix 1 3 5 7    

18.      Find the matrix X if 2X    +  5 7 = 9 5
    −2 −2 2 2  1 2 2 1 (A)    (  B)    (  C)   (D)    2 −1 2 −1 2 2 2 2

19. Which of the following can be calculated from the given matrices
1  2  1 2 3   3 

$A =                      4, B = 4 5 6 , (i) A2 (ii) B2      (iii) AB   (iv) BA$

5     6 7 8 9

(A) (i) and (ii) only (B) (ii) and (iii) only (C) (ii) and (iv) only (D) all of these 1 2 3 1  0  0 1 

20. If A =          , B = 2 −1 and C =           
3 2 1    −2 5 . Which of the following statements 0 2   

5 5  0  1 

$are correct? (i) AB + C =              		    (ii) BC =  2 -3$

5 5   −4 10 2 5 −8 20    

(iii) BA + C =  3 0          (iv) (AB )C =  −8 13
   

(A) (i) and (ii) only (B) (ii) and (iii) only (C) (iii) and (iv) only (D) all of these

### Unit Exercise - 3

1

1. Solve             (x + y − 5) = y − z = 2x − 11 = 9 − (x + 2z )
3

2. One hundred and fifty students are admitted to a school. They are distrbuted over
three sections A, B and C. If 6 students are shifted from section A to section C, the sections will have equal number of students. If 4 times of students of section C exceeds the number of students of section A by the number of students in section B, find the number of students in the three sections.

3. In a three-digit number, when the tens and the hundreds digit are interchanged the
new number is 54 more than three times the original number. If 198 is added to the number, the digits are reversed. The tens digit exceeds the hundreds digit by twice as that of the tens digit exceeds the unit digit. Find the original number.

4. Find the least common multiple of xy(k 2 + 1) + k (x 2 + y 2 ) and xy(k 2 − 1) + k (x 2 − y 2 )
5. Find the GCD of the following by division algorithm
2x 4 + 13x 3 + 27x 2 + 23x + 7 , x 3 + 3x 2 + 3x + 1 , x 2 + 2x + 1

6. Reduce the given Rational expressions to its lowest form
x 3a − 8 10x 3 − 25x 2 + 4x − 10

(i)                         (ii)
x 2a + 2x a + 4 −4 − 10x 2 1 1 + p q + r  q 2 + r 2 − p 2 

7. Simplify        × 1 +                   
1 1  2qr  − p q +r

8. Arul, Madan and Ram working together can clean a store in 6 hours. Working alone,
Madan takes twice as long to clean the store as Arul does. Ram needs three times as long as Arul does. How long would it take each if they are working alone?

9. Find the square root of 289x 4 − 612x 3 + 970x 2 − 684x + 361 .
10. Solve                y + 1 + 2y − 5 = 3
11. A boat takes 1.6 hours longer to go 36 kms up a river than down the river. If the speed
of the water current is 4 km per hr, what is the speed of the boat in still water?

12. Is it possible to design a rectangular park of perimeter 320 m and area 4800 m 2 ? If so
find its length and breadth. t2

13. At t minutes past 2 pm, the time needed to 3 pm is 3 minutes less than . Find t.
4

14. The number of seats in a row is equal to the total number of rows in a hall. The total
number of seats in the hall will increase by 375 if the number of rows is doubled and the number of seats in each row is reduced by 5. Find the number of rows in the hall at the beginning.

15. If a and b are the roots of the polynomial f (x ) = x 2 − 2x + 3, find the polynomial
a −1 b −1 whose roots are (i) a + 2, b + 2 (ii) , . a +1 b +1

16. If –4 is a root of the equation x 2 + px − 4 = 0 and if the equation x 2 + px + q = 0 has
equal roots, find the values of p and q.

17. Two farmers Thilagan and Kausigan cultivates three varieties of grains namely rice,
wheat and ragi. If the sale (in `) of three varieties of grains by both the farmers in the month of April is given by the matrix.

April sale in ` rice wheat ragi 500 1000 1500 Thilagan

$A =                                   $

2500 1500 500  Kausigan and the May month sale (in `) is exactly twice as that of the April month sale for each variety.

(i) What is the average sales of the months April and May.
(ii) If the sales continues to increase in the same way in the successive months, what
will be sales in the month of August?  cos q sin q   x − cos q 

18. If cos q                             + sin q 
cos q  = I , find x. − sin q cos q   x  2

p 0 0 −q  2 −2

$       , B =        , C =                      2$

19. Given A =                               1 0          2 2  and if BA = C , find p and q.
 0 2     3 0 6 3 3 6

$      , B =      , C =       $

20.       A =                8 5        1 1 find the matrix D, such that CD–AB = 0
4 5    

### Points to Remember

- A system of linear equations in three variables will be according to one of the
following cases.

(i) Unique solution (ii) Infinitely many solutions (iii) No solution
- The least common multiple of two or more algebraic expressions is the expression
of lowest degree (or power) such that the expressions exactly divides it.

- A polynomial of degree two in variable x is called a quadratic polynomial in x. Every
quadratic polynomial can have atmost two zeroes. Also the zeroes of a quadratic polynomial intersects the x-axis.

- The roots of the quadratic equation ax 2 + bx + c = 0 , (a ¹ 0) are given by
−b ± b 2 − 4ac . 2a

- For a quadratic equation ax 2 + bx + c = 0 , a ¹ 0
−b −Co-efficient of x

$Sum of the roots \\alpha  + \\beta  =                      =$

a Co -efficient of x 2

c Constant term

$Product of the roots \\alpha \\beta  =                  =$

a Co-efficient of x 2

- If the roots of a quadratic equation are a and b , then the equation is given by
$x^2 - (\\alpha  + \\beta  )x + \\alpha \\beta  = 0 .$

- The value of the discriminant (∆ = b 2 − 4ac) decides the nature of roots as follows
(i) When ∆ > 0 , the roots are real and unequal.
(ii) When ∆ = 0 , the roots are real and equal.
(iii) When ∆ < 0 , there are no real roots.
- Solving quadratic equation graphically.
- A matrix is a rectangular array of elements arranged in rows and columns.
- Order of a matrix
If a matrix A has m number of rows and n number of columns, then the order of the matrix A is (Number of rows)´ (Number of columns) that is, m ´n .We read m ´n as m cross n or m by n. It may be noted that m ´n is not a product of m and n.

- Types of matrices
(i) A matrix is said to be a row matrix if it has only one row and any number of
columns. A row matrix is also called as a row vector.

(ii) A matrix is said to be a column matrix if it has only one column and any
number of rows. It is also called as a column vector.

(iii) A matrix in which the number of rows is equal to the number of columns is
called a square matrix.

(iv) A matrix is said to be a zero matrix or null matrix if all its elements are zero.
(v) If A is a matrix, the matrix obtained by interchanging the rows and columns of
A is called its transpose and is denoted by AT .

(vi) A square matrix, all of whose elements, except those in the leading diagonal
are zero is called a diagonal matrix.

(vii) A diagonal matrix in which all the leading diagonal elements are same is called
a scalar matrix.

(viii)       A square matrix in which elements in the leading diagonal are all “1” and rest
are all zero is called an identity matrix (or) unit matrix.

(ix) A square matrix in which all the entries above the leading diagonal are zero is
called a lower triangular matrix. If all the entries below the leading diagonal are zero, then it is called an upper triangular matrix.

(x) Two matrices A and B are said to be equal if and only if they have the same
order and each element of matrix A is equal to the corresponding element of matrix B. That is, aij = bij for all i, j.

- The negative of a matrix Am´n denoted by −Am×n is the matrix formed by replacing
each element in the matrix Am´n with its additive inverse.

- Addition and subtraction of matrices
Two matrices can be added or subtracted if they have the same order. To add or subtract two matrices, simply add or subtract the corresponding elements.

- Multiplication of matrix by a scalar
We can multiply the elements of the given matrix A by a non-zero number k to obtain a new matrix kA whose elements are multiplied by k. The matrix kA is called scalar multiplication of A. Thus if A = (aij )m×n then , kA = (kaij )m×n for all i = 1,2,…,m and for all

$j = 1,2,…,n.$

### ICT CORNER

ICT 3.1 Step 1: Open the Browser type the URL Link given below (or) Scan the QR Code. Chapter named “Algebra” will open. Select the work sheet “Simultaneous equations” Step 2: In the given worksheet you can see three linear equations and you can change the equations by typing new values for a, b and c for each equation. You can move the 3-D graph to observe. Observe the nature of solutions by changing the equations. Step 1 Step 2 Expected results

ICT 3.2 Step – 1: Open the Browser type the URL Link given below (or) Scan the QR Code. GeoGebra work book named “ALGEBRA” will open. Click on the worksheet named “Nature of Quadratic Equation”. Step - 2: In the given worksheet you can change the co-efficient by moving the sliders given. Click on “New position” and move the sliders to fix the boundary for throwing the shell. Then click on “Get Ball” and click “fire” to hit the target. Here you can learn what happen to the curve when each co-efficient is changed. Step 1 Step 2 Expected results

You can repeat the same steps for other activities https://www.geogebra.org/m/jfr2zzgy#chapter/356193 or Scan the QR Code.