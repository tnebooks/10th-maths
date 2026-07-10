---
title: 'Concurrency Theorem'
weight: 6
---

### 4.6 Concurrency Theorems

#### Definition

A cevian is a line segment that extends from one vertex of a triangle to the opposite side. In the diagram, AD is a cevian, from \( A \).

<center>Fig.4.78</center>

#### Special cevians

(i) A median is a cevian that divides the opposite side into two congruent (equal) lengths.

(ii) An altitude is a cevian that is perpendicular to the opposite side.

(iii) An angle bisector is a cevian that bisects the corresponding angle.

<center>Fig.4.79</center>

#### Ceva's Theorem (without proof)

##### Statement

Let ABC be a triangle and let \( D, E, F \) be points on lines \( BC, CA, AB \) respectively. Then the cevians \( AD, BE, CF \) are concurrent if and only if

\[
\frac{BD}{DC} \times \frac{CE}{EA} \times \frac{AF}{FB} = 1
\]

where the lengths are directed. This also works for the reciprocal of each of the ratios as the reciprocal of 1 is 1.

<center>Fig.4.80</center>

#### Giovanni Ceva (Dec 7, 1647 - June 15, 1734)

In 1686, Ceva was designated as the professor of Mathematics, University of Mantua and worked there for the rest of the life. In 1678, he published an important theorem on synthetic geometry for a triangle called Ceva's theorem.

Ceva also rediscovered and published in the Journal Opuscula mathematica and Geometria motus in 1692. He applied these ideas in mechanics and hydraulics.

#### Note

The cevians do not necessarily lie within the triangle, although they do in the diagram.

#### Menelaus Theorem (without proof)

##### Statement

A necessary and sufficient condition for points \( P, Q, R \) on the respective sides \( BC, CA, AB \) (or their extension) of a triangle \( ABC \) to be collinear is that

\[
\frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{AR}{RB} = -1
\]

where all segments in the formula are directed segments.

<center>Fig.4.81</center>

#### Menelaus

Menelaus was a Greek mathematician who lived during the Roman empire in both Alexandria and Rome during first century (CE). His work was largely on the geometry of spheres.

Menelaus theorem was first discussed in his book, sphaerica and later mentioned by Ptolemy in his work Almagest.

Menelaus theorem proves that spheres are made up of spherical triangles.

#### Note

Menelaus theorem can also be given as

\[
BP \times CQ \times AR = -PC \times QA \times RB
\]

If BP is replaced by \( PB \) (or) \( CQ \) by \( QC \) (or) \( AR \) by \( RA \), or if any one of the six directed line segments \( BP, PC, CQ, QA, AR, RB \) is interchanged, then the product will be 1.

#### Example 4.30

Show that in a triangle, the medians are concurrent.

<center>Fig.4.82</center>

#### Solution

Medians are line segments joining each vertex to the midpoint of the corresponding opposite sides.

Thus medians are the cevians where \( D, E, F \) are midpoints of \( BC, CA \) and \( AB \) respectively.

Since \( D \) is a midpoint of \( BC \),

\[
BD = DC
\]

so

\[
\frac{BD}{DC} = 1 \tag{1}
\]

Since \( E \) is a midpoint of \( CA \),

\[
CE = EA
\]

so

\[
\frac{CE}{EA} = 1 \tag{2}
\]

Since \( F \) is a midpoint of \( AB \),

\[
AF = FB
\]

so

\[
\frac{AF}{FB} = 1 \tag{3}
\]

Thus, multiplying (1), (2) and (3) we get,

\[
\frac{BD}{DC} \times \frac{CE}{EA} \times \frac{AF}{FB} = 1 \times 1 \times 1 = 1
\]

And so, Ceva's theorem is satisfied.

Hence the Medians are concurrent.

Centroid is the point of concurrence of the median of a triangle.

#### Example 4.31

In \( \triangle ABC \), points \( D, E, F \) lie on \( BC, CA, AB \) respectively. Suppose \( AB, AC \) and \( BC \) have lengths 13, 14 and 15 respectively. If

\[
\frac{AF}{FB} = \frac{2}{5} \quad \text{and} \quad \frac{CE}{EA} = \frac{5}{8}
\]

Find \( BD \) and \( DC \).

<center>Fig. 4.83</center>

#### Solution

Given that

\[
AB = 13, \quad AC = 14, \quad BC = 15
\]

Let

\[
BD = x \quad \text{and} \quad DC = y
\]

Using Ceva's theorem, we have,

\[
\frac{BD}{DC} \times \frac{CE}{EA} \times \frac{AF}{FB} = 1 \tag{1}
\]

Substitute the values of \( \frac{AF}{FB} \) and \( \frac{CE}{EA} \) in (1),

we have

\[
\frac{BD}{DC} \times \frac{5}{8} \times \frac{2}{5} = 1
\]

\[
\frac{x}{y} \times \frac{10}{40} = 1
\]

we get,

\[
\frac{x}{y} \times \frac{1}{4} = 1
\]

Hence,

\[
x = 4y \tag{2}
\]

\[
BC = BD + DC = 15
\]

so,

\[
x + y = 15 \tag{3}
\]

From (2), using \( x = 4y \) in (3) we get,

\[
4y + y = 15
\]

gives

\[
5y = 15
\]

then

\[
y = 3
\]

Substitute \( y = 3 \) in (3) we get,

\[
x = 12
\]

Hence

\[
BD = 12, \quad DC = 3
\]

#### Example 4.32

In a garden containing several trees, three particular trees \( P, Q, R \) are located in the following way,

\[
BP = 2 \text{ m}, \quad CQ = 3 \text{ m}, \quad RA = 10 \text{ m}
\]

\[
PC = 6 \text{ m}, \quad QA = 5 \text{ m}, \quad RB = 2 \text{ m}
\]

where \( A, B, C \) are points such that \( P \) lies on \( BC \), \( Q \) lies on \( AC \) and \( R \) lies on \( AB \). Check whether the trees \( P, Q, R \) lie on a same straight line.

<center>Fig. 4.84</center>

#### Solution

By Menelaus theorem, the trees \( P, Q, R \) will be collinear (lie on same straight line) if

\[
\frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{RA}{RB} = 1 \tag{1}
\]

Given

\[
BP = 2 \text{ m}, \quad CQ = 3 \text{ m}, \quad RA = 10 \text{ m}
\]

\[
PC = 6 \text{ m}, \quad QA = 5 \text{ m}, \quad RB = 2 \text{ m}
\]

Substituting these values in (1) we get,

\[
\frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{RA}{RB} = \frac{2}{6} \times \frac{3}{5} \times \frac{10}{2} = \frac{60}{60} = 1
\]

Hence the trees \( P, Q, R \) lie on a same straight line.

#### Progress Check

1. A straight line that touches a circle at a common point is called a ______.

2. A chord is a subsection of ______.

3. The lengths of the two tangents drawn from ______ point to a circle are equal.

4. No tangent can be drawn from ______ of the circle.

5. ______ is a cevian that divides the angle, into two equal halves.

### Exercise 4.4

1. In \( \triangle ABC \), \( D, E, F \) are points on \( BC, CA, AB \) respectively such that
\[
\frac{BD}{DC} = \frac{1}{2}, \quad \frac{CE}{EA} = \frac{2}{3}, \quad \frac{AF}{FB} = \frac{3}{1}
\]
Check whether \( AD, BE, CF \) are concurrent.

2. In \( \triangle ABC \), \( D, E, F \) are points on \( BC, CA, AB \) respectively such that
\[
\frac{BD}{DC} = \frac{3}{4}, \quad \frac{CE}{EA} = \frac{4}{3}, \quad \frac{AF}{FB} = \frac{3}{4}
\]
Check whether \( AD, BE, CF \) are concurrent.

3. In \( \triangle ABC \), points \( D, E, F \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BD}{DC} = \frac{5}{6}, \quad \frac{CE}{EA} = \frac{3}{4}, \quad \frac{AF}{FB} = \frac{8}{5}
\]
Find whether \( AD, BE, CF \) are concurrent.

4. In \( \triangle ABC \), \( D, E, F \) are points on \( BC, CA, AB \) respectively such that
\[
\frac{BD}{DC} = \frac{3}{2}, \quad \frac{CE}{EA} = \frac{4}{5}, \quad \frac{AF}{FB} = \frac{5}{6}
\]
Check whether \( AD, BE, CF \) are concurrent.

5. In \( \triangle ABC \), \( D, E, F \) are points on \( BC, CA, AB \) respectively such that
\[
\frac{BD}{DC} = \frac{2}{3}, \quad \frac{CE}{EA} = \frac{3}{4}, \quad \frac{AF}{FB} = \frac{4}{5}
\]
Check whether \( AD, BE, CF \) are concurrent.

6. In \( \triangle ABC \), points \( P, Q, R \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BP}{PC} = \frac{3}{4}, \quad \frac{CQ}{QA} = \frac{4}{3}, \quad \frac{AR}{RB} = \frac{3}{4}
\]
Check whether \( P, Q, R \) are collinear.

7. In \( \triangle ABC \), points \( P, Q, R \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BP}{PC} = \frac{5}{6}, \quad \frac{CQ}{QA} = \frac{3}{4}, \quad \frac{AR}{RB} = \frac{8}{5}
\]
Check whether \( P, Q, R \) are collinear.

8. In \( \triangle ABC \), points \( P, Q, R \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BP}{PC} = \frac{2}{3}, \quad \frac{CQ}{QA} = \frac{3}{4}, \quad \frac{AR}{RB} = \frac{4}{5}
\]
Check whether \( P, Q, R \) are collinear.

9. In \( \triangle ABC \), points \( P, Q, R \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BP}{PC} = \frac{3}{2}, \quad \frac{CQ}{QA} = \frac{4}{3}, \quad \frac{AR}{RB} = \frac{5}{4}
\]
Check whether \( P, Q, R \) are collinear.

10. In \( \triangle ABC \), points \( P, Q, R \) are on \( BC, CA, AB \) respectively such that
\[
\frac{BP}{PC} = \frac{4}{5}, \quad \frac{CQ}{QA} = \frac{5}{6}, \quad \frac{AR}{RB} = \frac{6}{7}
\]
Check whether \( P, Q, R \) are collinear.