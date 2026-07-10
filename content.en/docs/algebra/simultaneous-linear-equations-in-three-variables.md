---
title: 'Simultaneous Linear Equations in Three Variables'
weight: 2
---

### 3.2 Simultaneous Linear Equations in Three Variables

Right from the primitive needs of calculating amount spent for various items in a super market, finding ages of people under specific conditions, finding path of an object when it is thrown upwards at an angle, Algebra plays a vital role in our daily life.

Any point in the space can be determined uniquely by knowing its latitude, longitude and altitude. Hence to locate the position of an object at a particular place situated on the Earth, three satellites are positioned to arrive three equations. Among these three equations, we get two linear equations and one quadratic (second degree) equation. Hence we can solve for the variables latitude, longitude and altitude to uniquely fix the position of any object at a given point of time. This is the basis of Global Positioning System (GPS). Hence the concept of linear equations in three variables is used in GPS systems.

<center>Fig. 3.2</center>

#### 3.2.1 System of Linear Equations in Three Variables

In earlier classes, we have learnt different methods of solving Simultaneous Linear Equations in two variables. Here we shall learn to solve the system of linear equations in three variables namely, \( x \), \( y \) and \( z \). The general form of a linear equation in three variables \( x \), \( y \) and \( z \) is

\[
ax + by + cz + d = 0
\]

where \( a \), \( b \), \( c \), \( d \) are real numbers, and atleast one of \( a \), \( b \), \( c \) is non-zero.

| A linear equation in two variables of the form \( ax + by + c = 0 \), represents a straight line. | A linear equation in three variables of the form \( ax + by + cz + d = 0 \), represents a plane. |
|---|---|
| <center>Fig. 3.3(i)</center> | <center>Fig. 3.3(ii)</center> |

**General Form:** A system of linear equations in three variables \( x \), \( y \), \( z \) has the general form

\[
a_1x + b_1y + c_1z + d_1 = 0
\]

\[
a_2x + b_2y + c_2z + d_2 = 0
\]

\[
a_3x + b_3y + c_3z + d_3 = 0
\]

Each equation in the system represents a plane in three dimensional space and solution of the system of equations is precisely the point of intersection of the three planes defined by the three linear equations of the system. The system may have only one solution, infinitely many solutions or no solution depending on how the planes intersect one another.

The figures presented below illustrate each of these possibilities

<center>Fig. 3.4</center>

#### Procedure for solving system of linear equations in three variables

**Step 1:** By taking any two equations from the given three, first multiply by some suitable non-zero constant to make the co-efficient of one variable (either \( x \) or \( y \) or \( z \)) numerically equal.

**Step 2:** Eliminate one of the variables whose co-efficient are numerically equal from the equations.

**Step 3:** Eliminate the same variable from another pair.

**Step 4:** Now we have two equations in two variables.

**Step 5:** Solve them using any method studied in earlier classes.

**Step 6:** The remaining variable is then found by substituting in any one of the given equations.

#### Note

If you obtain a false equation such as \( 0 = 1 \), in any of the steps then the system has no solution.

If you do not obtain a false solution, but obtain an identity, such as \( 0 = 0 \) then the system has infinitely many solutions.

#### Example 3.3

Solve the following system of linear equations in three variables

\[
3x - 2y + z = 2, \quad 2x + 3y - z = 5, \quad x + y + z = 6
\]

#### Solution

\[
3x - 2y + z = 2 \tag{1}
\]

\[
2x + 3y - z = 5 \tag{2}
\]

\[
x + y + z = 6 \tag{3}
\]

Adding (1) and (2):

\[
3x - 2y + z = 2
\]

\[
2x + 3y - z = 5
\]

\[
5x + y = 7 \tag{4}
\]

Adding (2) and (3):

\[
2x + 3y - z = 5
\]

\[
x + y + z = 6
\]

\[
3x + 4y = 11 \tag{5}
\]

(4) \( \times 4 \):

\[
20x + 4y = 28
\]

(5) \( \times 1 \):

\[
3x + 4y = 11
\]

Subtracting,

\[
17x = 17 \Rightarrow x = 1
\]

Substituting \( x = 1 \) in (4):

\[
5(1) + y = 7 \Rightarrow y = 2
\]

Substituting \( x = 1 \), \( y = 2 \) in (3):

\[
1 + 2 + z = 6 \Rightarrow z = 3
\]

Therefore,

\[
x = 1, \quad y = 2, \quad z = 3
\]

#### Example 3.4

In an interschool athletic meet, with total of 24 individual prizes, securing a total of 56 points, a first place secures 5 points, a second place secures 3 points, and a third place secures 1 point. Having as many third place finishers as first and second place finishers, find how many athletes finished in each place.

#### Solution

Let the number of I, II and III place finishers be \( x \), \( y \) and \( z \) respectively.

Total number of prizes \( = 24 \); Total number of points \( = 56 \).

Hence, the linear equations in three variables are

\[
x + y + z = 24 \tag{1}
\]

\[
5x + 3y + z = 56 \tag{2}
\]

\[
x + y = z \tag{3}
\]

Substituting (3) in (1) we get,

\[
z + z = 24 \Rightarrow 2z = 24 \Rightarrow z = 12
\]

From (3),

\[
x + y = 12 \tag{4}
\]

Substituting \( z = 12 \) in (2):

\[
5x + 3y + 12 = 56
\]

\[
5x + 3y = 44 \tag{5}
\]

(4) \( \times 3 \):

\[
3x + 3y = 36
\]

(5) \( \times 1 \):

\[
5x + 3y = 44
\]

Subtracting,

\[
2x = 8 \Rightarrow x = 4
\]

Substituting \( x = 4 \), \( z = 12 \) in (3):

\[
4 + y = 12 \Rightarrow y = 8
\]

Therefore,

Number of first place finishers is 4
Number of second place finishers is 8
Number of third place finishers is 12.

#### Example 3.5

Solve

\[
x + 2y - z = 5, \quad x - y + z = -2, \quad -5x - 4y + z = -11
\]

#### Solution

\[
x + 2y - z = 5 \tag{1}
\]

\[
x - y + z = -2 \tag{2}
\]

\[
-5x - 4y + z = -11 \tag{3}
\]

Adding (1) and (2):

\[
x + 2y - z = 5
\]

\[
x - y + z = -2
\]

\[
2x + y = 3 \tag{4}
\]

Adding (2) and (3):

\[
x - y + z = -2
\]

\[
-5x - 4y + z = -11
\]

Subtracting,

\[
6x + 3y = 9
\]

Dividing by 3,

\[
2x + y = 3 \tag{5}
\]

From (4) and (5), we get the same equation \( 2x + y = 3 \).

Thus, the system has infinitely many solutions.

Let \( x = t \). Then from (4),

\[
2t + y = 3 \Rightarrow y = 3 - 2t
\]

Substituting in (1):

\[
t + 2(3 - 2t) - z = 5
\]

\[
t + 6 - 4t - z = 5
\]

\[
-3t - z = -1
\]

\[
z = 1 - 3t
\]

Therefore, the solution is

\[
x = t, \quad y = 3 - 2t, \quad z = 1 - 3t
\]

where \( t \) is any real number.

#### Example 3.6

Solve

\[
x + y + z = 3, \quad 2x - y + z = 2, \quad x - 2y + 2z = 1
\]

#### Solution

\[
x + y + z = 3 \tag{1}
\]

\[
2x - y + z = 2 \tag{2}
\]

\[
x - 2y + 2z = 1 \tag{3}
\]

(1) \( \times 2 \):

\[
2x + 2y + 2z = 6
\]

(3) \( \times 1 \):

\[
x - 2y + 2z = 1
\]

Subtracting,

\[
x + 4y = 5 \tag{4}
\]

(1) \( \times 1 \):

\[
x + y + z = 3
\]

(2) \( \times 1 \):

\[
2x - y + z = 2
\]

Subtracting,

\[
- x + 2y = -1 \tag{5}
\]

(4) and (5):

\[
x + 4y = 5
\]

\[
-x + 2y = -1
\]

Adding,

\[
6y = 4 \Rightarrow y = \frac{2}{3}
\]

Substituting \( y = \frac{2}{3} \) in (4):

\[
x + 4\left(\frac{2}{3}\right) = 5
\]

\[
x + \frac{8}{3} = 5 \Rightarrow x = \frac{7}{3}
\]

Substituting \( x = \frac{7}{3} \), \( y = \frac{2}{3} \) in (1):

\[
\frac{7}{3} + \frac{2}{3} + z = 3
\]

\[
3 + z = 3 \Rightarrow z = 0
\]

Therefore,

\[
x = \frac{7}{3}, \quad y = \frac{2}{3}, \quad z = 0
\]

#### Example 3.7

Solve

\[
x + y + z = 2, \quad 2x + 2y + 2z = 6, \quad x - y + z = 0
\]

#### Solution

\[
x + y + z = 2 \tag{1}
\]

\[
2x + 2y + 2z = 6 \tag{2}
\]

\[
x - y + z = 0 \tag{3}
\]

Dividing (2) by 2:

\[
x + y + z = 3 \tag{2'}
\]

But from (1), \( x + y + z = 2 \).

Thus, we have \( 2 = 3 \), which is false.

Therefore, the system has no solution.

#### Example 3.8

The sum of the digits of a three-digit number is 11. If the digits are reversed, the new number is 46 more than five times the former number. If the hundreds digit plus twice the tens digit is equal to the units digit, then find the original three digit number.

#### Solution

Let the digits in the hundreds, tens and units place be \( x \), \( y \) and \( z \) respectively.

The number is \( 100x + 10y + z \).

Given,

\[
x + y + z = 11 \tag{1}
\]

When digits are reversed, the new number is \( 100z + 10y + x \).

Given,

\[
100z + 10y + x = 5(100x + 10y + z) + 46
\]

\[
100z + 10y + x = 500x + 50y + 5z + 46
\]

\[
100z - 5z + 10y - 50y + x - 500x = 46
\]

\[
95z - 40y - 499x = 46 \tag{2}
\]

Also given,

\[
x + 2y = z \tag{3}
\]

Substituting \( z = x + 2y \) in (1):

\[
x + y + x + 2y = 11
\]

\[
2x + 3y = 11 \tag{4}
\]

Substituting \( z = x + 2y \) in (2):

\[
95(x + 2y) - 40y - 499x = 46
\]

\[
95x + 190y - 40y - 499x = 46
\]

\[
-404x + 150y = 46 \tag{5}
\]

Solving (4) and (5):

(4) \( \times 404 \):

\[
808x + 1212y = 4444
\]

(5) \( \times 2 \):

\[
-808x + 300y = 92
\]

Adding,

\[
1512y = 4536 \Rightarrow y = 3
\]

Substituting \( y = 3 \) in (4):

\[
2x + 9 = 11 \Rightarrow x = 1
\]

From (3),

\[
z = 1 + 2(3) = 7
\]

Therefore, the number is \( 100(1) + 10(3) + 7 = 137 \).

#### Progress Check

1. For a system of linear equations in three variables the minimum number of equations required to get unique solution is ______.

2. A system with ______ will reduce to identity.

3. A system with ______ will provide absurd equation.

### Exercise 3.1

1. Solve the following system of linear equations in three variables

(i) \( x + y + z = 5; \quad 2x - y + z = 9; \quad x - 2y + 3z = 16 \)

(ii) \( \frac{1}{x} - \frac{2}{y} + 4 = 0; \quad \frac{1}{y} - \frac{1}{z} + 1 = 0; \quad \frac{2}{z} + \frac{3}{x} = 14 \)

(iii) \( x + 20 = \frac{3y}{2} + 10 = 2z + 5 = 110 - (y + z) \)

2. Discuss the nature of solutions of the following system of equations

(i) \( x + 2y - z = 6; \quad -3x - 2y + 5z = -12; \quad x - 2z = 3 \)

(ii) \( 2y + z = 3(-x + 1); \quad -x + 3y - z = -4; \quad 3x + 2y + z = -\frac{1}{2} \)

(iii) \( \frac{y + z}{4} = \frac{z + x}{3} = \frac{x + y}{2}; \quad x + y + z = 27 \)

3. Vani, her father and her grand father have an average age of 53. One-half of her grand father's age plus one-third of her father's age plus one fourth of Vani's age is 65. Four years ago if Vani's grandfather was four times as old as Vani then how old are they all now?

4. The sum of the digits of a three-digit number is 11. If the digits are reversed, the new number is 46 more than five times the former number. If the hundreds digit plus twice the tens digit is equal to the units digit, then find the original three digit number?

5. There are 12 pieces of five, ten and twenty rupee currencies whose total value is 105. When first 2 sorts are interchanged in their numbers its value will be increased by 20. Find the number of currencies in each sort.