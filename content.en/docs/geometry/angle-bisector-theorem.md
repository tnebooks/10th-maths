---
title: 'Angle Bisector Theorem'
weight: 4
---

### 4.4 Pythagoras Theorem

Among all existing theorems in mathematics, Pythagoras theorem is considered to be the most important because it has maximum number of proofs. There are more than 350 ways of proving Pythagoras theorem through different methods. Each of these proofs was discovered by eminent mathematicians, scholars, engineers and math enthusiasts, including one by the \( 20^{\text{th}} \) American president James Garfield. The book titled "The Pythagorean Proposition" written by Elisha Scott Loomis, published by the National Council of Teaching of Mathematics (NCTM) in America contains 367 proofs of Pythagoras Theorem.

Three natural numbers \( (a, b, c) \) are said to form Pythagorean Triplet, if they form sides of a right triangle. Thus \( (a, b, c) \) is a Pythagorean Triplet if and only if

\[
c^2 = a^2 + b^2
\]

Now we are in a position to study this most famous and important theorem not only in Geometry but in whole of mathematics.

<center>Fig. 4.48</center>

#### Activity 4

Step 1: Take a chart paper, cut out a right angled triangle of measurement as given in triangle (i).

Step 2: Take three more different colour chart papers and cut out three triangles such that the sides of triangle (ii) is three times of the triangle (i), the sides of triangle (iii) is four times of the triangle (i), the sides of triangle (iv) is five times of triangle (i).

Step 3: Now keeping the common side length 12 place the triangle (ii) and (iii) over the triangle (iv) such that the sides of these two triangles [(ii) and (iii)] coincide with the triangle (iv).

Observe the hypotenuse side and write down the equation. What do you conclude?

#### Note

In a right angled triangle, the side opposite to \( 90^\circ \) (the right angle) is called the hypotenuse. The other two sides are called legs of the right angled triangle. The hypotenuse will be the longest side of the triangle.

#### Theorem 5: Pythagoras Theorem

##### Statement

In a right angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.

##### Proof

Given: In \( \Delta ABC \), \( \angle A = 90^\circ \)

To prove: \( AB^2 + AC^2 = BC^2 \)

<center>Fig.4.49</center>

Construction: Draw \( AD \perp BC \)

| No. | Statement | Reason |
|---|---|---|
| 1. | Compare \( \Delta ABC \) and \( \Delta DBA \) | |
|    | \( \angle B \) is common | |
|    | \( \angle BAC = \angle BDA = 90^\circ \) | Given \( \angle BAC = 90^\circ \) and by construction \( \angle BDA = 90^\circ \) |
|    | Therefore, \( \Delta ABC \sim \Delta DBA \) | By AA similarity |
|    | \( \frac{AB}{BD} = \frac{BC}{AB} \) | Corresponding sides of similar triangles are proportional |
|    | \( AB^2 = BC \times BD \) ... (1) | Cross multiplication |
| 2. | Compare \( \Delta ABC \) and \( \Delta DAC \) | |
|    | \( \angle C \) is common | |
|    | \( \angle BAC = \angle ADC = 90^\circ \) | Given \( \angle BAC = 90^\circ \) and by construction \( \angle ADC = 90^\circ \) |
|    | Therefore, \( \Delta ABC \sim \Delta DAC \) | By AA similarity |
|    | \( \frac{BC}{AC} = \frac{AC}{DC} \) | Corresponding sides of similar triangles are proportional |
|    | \( AC^2 = BC \times DC \) ... (2) | Cross multiplication |
| 3. | \( AB^2 + AC^2 = BC \times BD + BC \times DC \) | Adding (1) and (2) |
|    | \( = BC(BD + DC) \) | Taking \( BC \) common |
|    | \( = BC \times BC \) | Since \( BD + DC = BC \) |
|    | \( = BC^2 \) | |
|    | Hence, \( AB^2 + AC^2 = BC^2 \) | Proved |

#### Converse of Pythagoras Theorem

##### Statement

If the square of the longest side of a triangle is equal to sums of squares of other two sides, then the triangle is a right angle triangle.

#### Activity 5

(i) Take two consecutive odd numbers.

(ii) Write the reciprocals of the above numbers and add them. You will get a number of the form \( \frac{p}{q} \).

(iii) Add 2 to the denominator of \( \frac{p}{q} \) to get \( q + 2 \).

(iv) Now consider the numbers \( p, q, q + 2 \). What relation you get between these three numbers? Try for three pairs of consecutive odd numbers and conclude your answer.

#### Thinking Corner

1. Write down any five Pythagorean triplets?

2. In a right angle triangle the sum of other two angles is ______.

3. Can all the three sides of a right angled triangle be odd numbers? Why?

#### Example 4.18

An insect \( 8 \) m away initially from the foot of a lamp post which is \( 6 \) m tall, crawls towards it moving through a distance. If its distance from the top of the lamp post is equal to the distance it has moved, how far is the insect away from the foot of the lamp post?

<center>Fig.4.50</center>

#### Solution

Distance between the insect and the foot of the lamp post \( BD = 8 \) m

The height of the lamp post, \( AB = 6 \) m

After moving a distance of \( x \) m, let the insect be at \( C \)

Let, \( AC = CD = x \). Then \( BC = BD - CD = 8 - x \)

In \( \Delta ABC \), \( \angle B = 90^\circ \)

\[
AC^2 = AB^2 + BC^2
\]

gives

\[
x^2 = 6^2 + (8 - x)^2
\]

\[
x^2 = 36 + 64 - 16x + x^2
\]

\[
16x = 100
\]

then

\[
x = 6.25
\]

Then,

\[
BC = 8 - x = 8 - 6.25 = 1.75 \text{ m}
\]

Therefore the insect is \( 1.75 \) m away from the foot of the lamp post.

#### Example 4.19

\( P \) and \( Q \) are the mid-points of the sides \( CA \) and \( CB \) respectively of a \( \Delta ABC \), right angled at \( C \). Prove that

\[
4(AQ^2 + BP^2) = 5AB^2
\]

<center>Fig.4.51</center>

#### Solution

\( \Delta AQC \) is a right triangle at \( C \)

\[
AQ^2 = AC^2 + QC^2 \tag{1}
\]

\( \Delta BPC \) is a right triangle at \( C \)

\[
BP^2 = BC^2 + CP^2 \tag{2}
\]

\( \Delta ABC \) is a right triangle at \( C \)

\[
AB^2 = AC^2 + BC^2 \tag{3}
\]

From (1) and (2),

\[
AQ^2 + BP^2 = AC^2 + QC^2 + BC^2 + CP^2
\]

\[
4(AQ^2 + BP^2) = 4AC^2 + 4QC^2 + 4BC^2 + 4CP^2
\]

\[
= 4AC^2 + (2QC)^2 + 4BC^2 + (2CP)^2
\]

\[
= 4AC^2 + BC^2 + 4BC^2 + AC^2
\]

(Since \( P \) and \( Q \) are mid points, \( BC = 2QC \) and \( AC = 2CP \))

\[
= 5(AC^2 + BC^2)
\]

From equation (3),

\[
4(AQ^2 + BP^2) = 5AB^2
\]

#### Example 4.20

What length of ladder is needed to reach a height of 7 ft along the wall when the base of the ladder is 4 ft from the wall? Round off your answer to the next tenth place.

<center>Fig.4.52</center>

#### Solution

Let \( x \) be the length of the ladder. \( BC = 4 \) ft, \( AC = 7 \) ft.

By Pythagoras theorem we have,

\[
AB^2 = AC^2 + BC^2
\]

\[
x^2 = 7^2 + 4^2 \Rightarrow x^2 = 49 + 16
\]

\[
x^2 = 65
\]

Hence,

\[
x = \sqrt{65}
\]

The number \( \sqrt{65} \) is between 8 and 8.1.

\[
8^2 = 64 < 65 < 65.61 = 8.1^2
\]

Therefore, the length of the ladder is approximately 8.1 ft.

#### Example 4.21

An Aeroplane after take off from an airport and flies due north at a speed of \( 1000 \) km/hr. At the same time, another aeroplane take off from the same airport and flies due west at a speed of \( 1200 \) km/hr. How far apart will be the two planes after \( 1\frac{1}{2} \) hours?

<center>Fig.4.53</center>

#### Solution

Let the first aeroplane starts from \( O \) and goes upto \( A \) towards north,

(Distance \( = \) Speed \( \times \) time)

\[
OA = \left(1000 \times \frac{3}{2}\right) \text{ km} = 1500 \text{ km}
\]

Let the second aeroplane starts from \( O \) at the same time and goes upto \( B \) towards west,

\[
OB = \left(1200 \times \frac{3}{2}\right) = 1800 \text{ km}
\]

The required distance to be found is \( BA \)

In right angled triangle \( AOB \)

\[
AB^2 = OA^2 + OB^2
\]

\[
AB^2 = 1500^2 + 1800^2
\]

\[
= 2250000 + 3240000 = 5490000
\]

\[
AB = \sqrt{5490000} = 300\sqrt{61} \text{ km}
\]

Therefore, the two planes are \( 300\sqrt{61} \) km apart.

#### Progress Check

1. ______ is the longest side of the right angled triangle.

2. The first theorem in mathematics is ______.

3. If the square of the longest side of a triangle is equal to sums of squares of other two sides, then the triangle is ______.

4. State True or False. Justify them.

(i) Pythagoras Theorem is applicable to all triangles.

(ii) One side of a right angled triangle must always be a multiple of 4.

### Exercise 4.2

1. A man goes 18 m due east and then 24 m due north. Find the distance of his current position from the starting point?

2. There are two paths that one can choose to go from Sarah's house to James house. One way is to take \( C \) street, and the other way requires to take \( B \) street and then \( A \) street. How much shorter is the direct path along \( C \) street? (Using figure).

<center>Fig.4.54</center>

3. To get from point \( A \) to point \( B \) you must avoid walking through a pond. You must walk \( 34 \) m south and \( 41 \) m east. To the nearest meter, how many meters would be saved if it were possible to make a way through the pond?

4. In the rectangle \( WXYZ \), \( XY + YZ = 17 \) cm, and \( XZ + YW = 26 \) cm. Calculate the length and breadth of the rectangle?

<center>Fig.4.55</center>

5. The hypotenuse of a right triangle is \( 6 \) m more than twice of the shortest side. If the third side is \( 2 \) m less than the hypotenuse, find the sides of the triangle.

6. \( 5 \) m long ladder is placed leaning towards a vertical wall such that it reaches the wall at a point \( 4 \) m high. If the foot of the ladder is moved \( 1.6 \) m towards the wall, then find the distance by which the top of the ladder would slide upwards on the wall.

7. The perpendicular \( PS \) on the base \( QR \) of a \( \Delta PQR \) intersects \( QR \) at \( S \), such that \( QS = 3SR \). Prove that

\[
2PQ^2 = 2PR^2 + QR^2
\]

8. In the adjacent figure, \( ABC \) is a right angled triangle with right angle at \( B \) and points \( D \), \( E \) trisect \( BC \). Prove that

\[
8AE^2 = 3AC^2 + 5AD^2
\]