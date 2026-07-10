---
title: 'Basic Proportionality Theorem'
weight: 3
---

### 4.3 Thales Theorem and Angle Bisector Theorem

#### 4.3.1 Introduction

Thales, (640-540 BC (BCE)) the most famous Greek mathematician and philosopher lived around seventh century BC (BCE). He possessed knowledge to the extent that he became the first of seven sages of Greece. Thales was the first man to announce that any idea that emerged should be tested scientifically and only then it can be accepted. In this aspect, he did great investigations in mathematics and astronomy and discovered many concepts. He was credited for providing first proof in mathematics, which today is called by the name "Basic Proportionality Theorem". It is also called "Thales Theorem" named after its discoverer.

The discovery of the Thales theorem itself is a very interesting story. When Thales travelled to Egypt, he was challenged by Egyptians to determine the height of one of several magnificent pyramids that they had constructed. Thales accepted the challenge and used similarity of triangles to determine the same successfully, another triumphant application of Geometry. Since \( X_0 \), \( X_1 \) and \( H_0 \) are known, we can determine the height \( H_1 \) of the pyramid.

<center>Fig.4.27</center>

#### Theorem 1: Basic Proportionality Theorem (Thales Theorem)

##### Statement

If a straight line is drawn parallel to one side of a triangle intersecting the other two sides, then it divides the other two sides in the same ratio.

##### Proof

Given: In \( \Delta ABC \), \( D \) is a point on \( AB \) and \( E \) is a point on \( AC \) such that \( DE \parallel BC \).

To prove: \( \frac{AD}{DB} = \frac{AE}{EC} \)

<center>Fig.4.28</center>

Construction: Join \( BE \) and \( CD \). Draw \( EF \perp AB \) and \( DG \perp AC \).

Proof:

| No. | Statement | Reason |
|---|---|---|
| 1. | \( \frac{\text{area}(\Delta ADE)}{\text{area}(\Delta BDE)} = \frac{AD}{DB} \) | Triangles with same vertex \( E \) and bases \( AD \) and \( DB \) on same line \( AB \), so ratio of areas equals ratio of bases. |
| 2. | \( \frac{\text{area}(\Delta ADE)}{\text{area}(\Delta CDE)} = \frac{AE}{EC} \) | Triangles with same vertex \( D \) and bases \( AE \) and \( EC \) on same line \( AC \), so ratio of areas equals ratio of bases. |
| 3. | \( \text{area}(\Delta BDE) = \text{area}(\Delta CDE) \) | Triangles on the same base \( DE \) and between the same parallels \( DE \) and \( BC \). |
| 4. | \( \frac{AD}{DB} = \frac{AE}{EC} \) | From (1), (2) and (3). Hence proved. |

#### Corollary of Basic Proportionality Theorem

If in \( \Delta ABC \), a straight line \( DE \) parallel to \( BC \), intersects \( AB \) at \( D \) and \( AC \) at \( E \), then

\[
\text{(i) } \frac{AB}{AD} = \frac{AC}{AE} \qquad \text{(ii) } \frac{AB}{DB} = \frac{AC}{EC}
\]

##### Proof

In \( \Delta ABC \), \( DE \parallel BC \),

Therefore,

\[
\frac{AD}{DB} = \frac{AE}{EC}
\]

(by Basic Proportionality Theorem)

(i) Taking reciprocals, we get

\[
\frac{DB}{AD} = \frac{EC}{AE}
\]

Add 1 to both the sides

\[
\frac{DB}{AD} + 1 = \frac{EC}{AE} + 1
\]

\[
\frac{DB + AD}{AD} = \frac{EC + AE}{AE}
\]

so,

\[
\frac{AB}{AD} = \frac{AC}{AE}
\]

(ii) Add 1 to both the sides of \( \frac{AD}{DB} = \frac{AE}{EC} \)

\[
\frac{AD}{DB} + 1 = \frac{AE}{EC} + 1
\]

Therefore,

\[
\frac{AB}{DB} = \frac{AC}{EC}
\]

<center>Fig.4.29</center>

<center>Fig.4.30</center>

Is the converse of Basic Proportionality Theorem also true? To examine let us do the following illustration.

#### Illustration

Draw an angle \( XAY \) on your notebook as shown in Fig.4.31 and on ray \( AX \), mark points \( B_1, B_2, B_3, B_4 \) and \( B \) such that

\[
AB_1 = B_1B_2 = B_2B_3 = B_3B_4 = B_4B = 1 \text{ cm}
\]

Similarly on ray \( AY \), mark points \( C_1, C_2, C_3, C_4 \) and \( C \), such that

\[
AC_1 = C_1C_2 = C_2C_3 = C_3C_4 = C_4C = 2 \text{ cm}
\]

Join \( B_1C_1 \) and \( BC \).

<center>Fig.4.31</center>

Observe that

\[
\frac{AB_1}{B_1B} = \frac{AC_1}{C_1C} = \frac{1}{4}
\]

and

\[
B_1C_1 \parallel BC
\]

Similarly joining \( B_2C_2 \), \( B_3C_3 \) and \( B_4C_4 \) you see that

\[
\frac{AB_2}{B_2B} = \frac{AC_2}{C_2C} = \frac{2}{3}
\]

and

\[
B_2C_2 \parallel BC
\]

\[
\frac{AB_3}{B_3B} = \frac{AC_3}{C_3C} = \frac{3}{2}
\]

and

\[
B_3C_3 \parallel BC
\]

\[
\frac{AB_4}{B_4B} = \frac{AC_4}{C_4C} = \frac{4}{1}
\]

and

\[
B_4C_4 \parallel BC
\]

From this we observe that if a line divides two sides of a triangle in the same ratio, then the line is parallel to the third side.

Therefore, we obtain the following theorem called converse of the Thales theorem.

#### Theorem 2: Converse of Basic Proportionality Theorem

##### Statement

If a straight line divides any two sides of a triangle in the same ratio, then the line must be parallel to the third side.

##### Proof

Given: In \( \Delta ABC \),

\[
\frac{AD}{DB} = \frac{AE}{EC}
\]

To prove: \( DE \parallel BC \)

Construction: If \( DE \) is not parallel to \( BC \), draw \( DF \parallel BC \).

<center>Fig.4.32</center>

| No. | Statement | Reason |
|---|---|---|
| 1. | \( \frac{AD}{DB} = \frac{AE}{EC} \) ... (1) | Given |
| 2. | In \( \triangle ABC \), \( DF \parallel BC \) | Construction |
| 3. | \( \frac{AD}{DB} = \frac{AF}{FC} \) ... (2) | Thales theorem |
| 4. | \( \frac{AE}{EC} = \frac{AF}{FC} \) | From (1) and (2) |
| 5. | \( \frac{AE}{EC} + 1 = \frac{AF}{FC} + 1 \) | Adding 1 to both sides |
| 6. | \( \frac{AE + EC}{EC} = \frac{AF + FC}{FC} \) | Simplifying |
| 7. | \( \frac{AC}{EC} = \frac{AC}{FC} \) | Simplifying |
| 8. | \( EC = FC \) | Cancelling \( AC \) on both sides |
| 9. | Therefore, \( E = F \) | From step 8 |
| 10. | Thus \( DE \parallel BC \) | Our assumption that \( DE \) is not parallel to \( BC \) is wrong. Hence proved. |

#### Theorem 3: Angle Bisector Theorem

##### Statement

The internal bisector of an angle of a triangle divides the opposite side internally in the ratio of the corresponding sides containing the angle.

##### Proof

Given: In \( \Delta ABC \), \( AD \) is the internal bisector of \( \angle A \).

To prove: \( \frac{BD}{DC} = \frac{AB}{AC} \)

<center>Fig.4.33</center>

Construction: Draw \( CE \parallel DA \) meeting \( BA \) extended at \( E \).

| No. | Statement | Reason |
|---|---|---|
| 1. | \( \angle AEC = \angle BAE = \angle 1 \) | Two parallel lines \( DA \parallel CE \) cut by transversal \( AE \), corresponding angles are equal. |
| 2. | \( \angle ABD = \angle ECD = \angle 2 \) | Two parallel lines \( DA \parallel CE \) cut by transversal \( AC \), alternate angles are equal. |
| 3. | \( \Delta ACE \) is isosceles | In \( \Delta ACE \), \( \angle CAE = \angle CEA \), so \( AC = CE \) ... (1) |
| 4. | \( \Delta ABD \sim \Delta ECD \) | By AA Similarity |
| 5. | \( \frac{AB}{CE} = \frac{BD}{CD} \) | Corresponding sides of similar triangles are proportional |
| 6. | \( \frac{AB}{AC} = \frac{BD}{DC} \) | From (1) \( AC = CE \). Hence proved. |

#### Activity 3

Step 1: Take a chart and cut it like a triangle as shown in Fig.4.34(a).

Step 2: Then fold it along the symmetric line \( AD \). Then C and B will be one upon the other.

Step 3: Similarly fold it along CE, then \( B \) and \( A \) will be one upon the other.

Step 4: Similarly fold it along BF, then \( A \) and \( C \) will be one upon the other.

<center>Fig.4.34</center>

Find \( AB, AC, BD, DC \) using a scale. Find \( \frac{AB}{AC}, \frac{BD}{DC} \) check if they are equal?

In the three cases, the internal bisector of an angle of a triangle divides the opposite side internally in the ratio of the corresponding sides containing the angle.

What do you conclude from this activity?

#### Theorem 4: Converse of Angle Bisector Theorem

##### Statement

If a straight line through one vertex of a triangle divides the opposite side internally in the ratio of the other two sides, then the line bisects the angle internally at the vertex.

##### Proof

Given: ABC is a triangle. \( AD \) divides \( BC \) in the ratio of the sides containing the angles \( \angle A \) to meet \( BC \) at \( D \).

That is

\[
\frac{AB}{AC} = \frac{BD}{DC} \tag{1}
\]

To prove: AD bisects \( \angle A \) i.e. \( \angle 1 = \angle 2 \)

Construction: Draw \( CE \parallel DA \). Extend \( BA \) to meet at \( E \).

<center>Fig.4.35</center>

| No. | Statement | Reason |
|---|---|---|
| 1. | Let \( \angle BAD = \angle 1 \) and \( \angle DAC = \angle 2 \) | Assumption |
| 2. | \( \angle BAD = \angle AEC = \angle 1 \) | Since \( DA \parallel CE \) and \( AC \) is transversal, corresponding angles are equal |
| 3. | \( \angle DAC = \angle ACE = \angle 2 \) | Since \( DA \parallel CE \) and \( AC \) is transversal, Alternate angles are equal |
| 4. | \( \frac{BA}{AE} = \frac{BD}{DC} \) ... (2) | In \( \triangle BCE \) by Thales theorem |
| 5. | \( \frac{AB}{AC} = \frac{BD}{DC} \) | From (1) |
| 6. | \( \frac{AB}{AE} = \frac{AB}{AC} \) | From (1) and (2) |
| 7. | \( AC = AE \) ... (3) | Cancelling \( AB \) on both sides |
| 8. | \( \angle 1 = \angle 2 \) | \( \triangle ACE \) is isosceles by (3), so base angles are equal |
| 9. | AD bisects \( \angle A \) | Since, \( \angle 1 = \angle BAD = \angle 2 = \angle DAC \). Hence proved. |

#### Example 4.10

In \( \Delta ABC \), if \( DE \parallel BC \), \( AD = x \), \( DB = x - 2 \), \( AE = x + 2 \) and \( EC = x - 1 \) then find the lengths of the sides \( AB \) and \( AC \).

<center>Fig. 4.36</center>

#### Solution

In \( \Delta ABC \) we have \( DE \parallel BC \).

By Thales theorem, we have

\[
\frac{AD}{DB} = \frac{AE}{EC}
\]

\[
\frac{x}{x - 2} = \frac{x + 2}{x - 1}
\]

gives

\[
x(x - 1) = (x - 2)(x + 2)
\]

Hence,

\[
x^2 - x = x^2 - 4
\]

so,

\[
x = 4
\]

When \( x = 4 \),

\[
AD = 4, \quad DB = x - 2 = 2
\]

\[
AE = x + 2 = 6, \quad EC = x - 1 = 3
\]

Hence,

\[
AB = AD + DB = 4 + 2 = 6
\]

\[
AC = AE + EC = 6 + 3 = 9
\]

Therefore,

\[
AB = 6, \quad AC = 9
\]

#### Example 4.11

\( D \) and \( E \) are respectively the points on the sides \( AB \) and \( AC \) of a \( \Delta ABC \) such that \( AB = 5.6 \text{ cm} \), \( AD = 1.4 \text{ cm} \), \( AC = 7.2 \text{ cm} \) and \( AE = 1.8 \text{ cm} \), show that \( DE \parallel BC \).

<center>Fig.4.37</center>

#### Solution

We have

\[
AB = 5.6 \text{ cm}, \quad AD = 1.4 \text{ cm}
\]

\[
AC = 7.2 \text{ cm}, \quad AE = 1.8 \text{ cm}
\]

\[
BD = AB - AD = 5.6 - 1.4 = 4.2 \text{ cm}
\]

and

\[
EC = AC - AE = 7.2 - 1.8 = 5.4 \text{ cm}
\]

\[
\frac{AD}{DB} = \frac{1.4}{4.2} = \frac{1}{3}
\]

and

\[
\frac{AE}{EC} = \frac{1.8}{5.4} = \frac{1}{3}
\]

\[
\frac{AD}{DB} = \frac{AE}{EC}
\]

Therefore, by converse of Basic Proportionality Theorem, we have \( DE \) is parallel to \( BC \). Hence proved.

#### Example 4.12

In the Fig.4.38, \( DE \parallel AC \) and \( DC \parallel AP \). Prove that

\[
\frac{BE}{EC} = \frac{BC}{CP}
\]

<center>Fig.4.38</center>

#### Solution

In \( \Delta BPA \), we have \( DC \parallel AP \). By Basic Proportionality Theorem,

we have

\[
\frac{BC}{CP} = \frac{BD}{DA} \tag{1}
\]

In \( \Delta BCA \), we have \( DE \parallel AC \). By Basic Proportionality Theorem, we have,

\[
\frac{BE}{EC} = \frac{BD}{DA} \tag{2}
\]

From (1) and (2) we get,

\[
\frac{BE}{EC} = \frac{BC}{CP}
\]

Hence proved.

#### Example 4.13

In the Fig.4.39, \( AD \) is the bisector of \( \angle A \). If \( BD = 4 \text{ cm} \), \( DC = 3 \text{ cm} \) and \( AB = 6 \text{ cm} \), find \( AC \).

<center>Fig.4.39</center>

#### Solution

In \( \Delta ABC \), \( AD \) is the bisector of \( \angle A \)

By Angle Bisector Theorem

\[
\frac{BD}{DC} = \frac{AB}{AC}
\]

\[
\frac{4}{3} = \frac{6}{AC}
\]

gives

\[
4AC = 18
\]

Hence,

\[
AC = \frac{9}{2} = 4.5 \text{ cm}
\]

#### Example 4.14

In the Fig. 4.40, \( AD \) is the bisector of \( \angle BAC \), if \( AB = 10 \text{ cm} \), \( AC = 14 \text{ cm} \) and \( BC = 6 \text{ cm} \). Find \( BD \) and \( DC \).

<center>Fig.4.40</center>

#### Solution

Let \( BD = x \text{ cm} \), then \( DC = (6 - x) \text{ cm} \)

\( AD \) is the bisector of \( \angle A \)

By Angle Bisector Theorem

\[
\frac{AB}{AC} = \frac{BD}{DC}
\]

\[
\frac{10}{14} = \frac{x}{6 - x}
\]

gives

\[
\frac{5}{7} = \frac{x}{6 - x}
\]

\[
5(6 - x) = 7x
\]

\[
30 - 5x = 7x
\]

\[
30 = 12x
\]

\[
x = \frac{30}{12} = 2.5 \text{ cm}
\]

Therefore,

\[
BD = 2.5 \text{ cm}, \quad DC = 6 - x = 6 - 2.5 = 3.5 \text{ cm}
\]

#### Progress Check

1. A straight line drawn ______ to a side of a triangle divides the other two sides proportionally.

2. Basic Proportionality Theorem is also known as ______.

3. Let \( \Delta ABC \) be equilateral. If \( D \) is a point on \( BC \) and \( AD \) is the internal bisector of \( \angle A \). Using Angle Bisector Theorem, \( \frac{BD}{DC} \) is ______.

4. The ______ of an angle of a triangle divides the opposite side internally in the ratio of the corresponding sides containing the angle.

5. If the median \( AD \) to the side \( BC \) of a \( \Delta ABC \) is also an angle bisector of \( \angle A \) then \( \frac{AB}{AC} \) is ______.

#### 4.3.2 Construction of triangle

We have already learnt in previous class how to construct triangles when sides and angles are given.

In this section, let us construct a triangle when the following are given :

(i) the base, vertical angle and the median on the base

(ii) the base, vertical angle and the altitude on the base

(iii) the base, vertical angle and the point on the base where the bisector of the vertical angle meets the base.

First, we consider the following construction,

#### Construction of a segment of a circle on a given line segment containing an angle \( \theta \)

##### Construction

Step 1: Draw a line segment \( AB \).

Step 2: At \( A \), take \( \angle BAE = \theta \). Draw \( AE \).

Step 3: Draw, \( AF \perp AE \).

Step 4: Draw the perpendicular bisector of \( AB \) meeting \( AF \) at \( O \).

<center>Fig. 4.41</center>

Step 5: With \( O \) as centre and \( OA \) as radius draw a circle \( ABH \).

Step 6: Take any point \( C \) on the circle, By the alternate segments theorem, the major arc \( ACB \) is the required segment of the circle containing the angle \( \theta \).

#### Note

If \( C_1, C_2, \ldots \) are points on the circle, then all the triangles \( \Delta BAC_1, \Delta BAC_2, \ldots \) are with same base and the same vertical angle.

#### Construction of a triangle when its base, the vertical angle and the median from the vertex of the base are given.

#### Example 4.15

Construct a \( \Delta PQR \) in which \( PQ = 8 \text{ cm} \), \( \angle R = 60^\circ \) and the median \( RG \) from \( R \) to \( PQ \) is \( 5.8 \text{ cm} \). Find the length of the altitude from \( R \) to \( PQ \).

<center>Fig.4.42</center>

##### Construction

Step 1: Draw a line segment \( PQ = 8 \text{ cm} \).

Step 2: At \( P \), draw \( PE \) such that \( \angle QPE = 60^\circ \).

Step 3: At \( P \), draw \( PF \) such that \( \angle EPF = 90^\circ \).

Step 4: Draw the perpendicular bisector to \( PQ \), which intersects \( PF \) at \( O \) and \( PQ \) at \( G \).

Step 5: With \( O \) as centre and \( OP \) as radius draw a circle.

Step 6: From \( G \) mark arcs of radius \( 5.8 \text{ cm} \) on the circle. Mark them as \( R \) and \( S \).

Step 7: Join \( PR \) and \( RQ \). Then \( \triangle PQR \) is the required triangle.

Step 8: From \( R \) draw a line \( RN \) perpendicular to \( LQ \). \( LQ \) meets \( RN \) at \( M \).

Step 9: The length of the altitude is \( RM = 3.8 \text{ cm} \).

#### Construction of a triangle when its base, the vertical angle and the altitude from the vertex to the base are given.

#### Example 4.16

Construct a triangle \( \Delta PQR \) such that \( QR = 5 \text{ cm} \), \( \angle P = 30^\circ \) and the altitude from \( P \) to \( QR \) is of length \( 4.2 \text{ cm} \).

<center>Fig.4.43</center>

##### Construction

Step 1: Draw a line segment \( QR = 5 \text{ cm} \).

Step 2: At \( Q \) draw \( QE \) such that \( \angle RQE = 30^\circ \).

Step 3: At \( Q \) draw \( QF \) such that \( \angle EQF = 90^\circ \).

Step 4: Draw the perpendicular bisector \( XY \) to \( QR \) which intersects \( QF \) at \( O \) and \( QR \) at \( G \).

Step 5: With \( O \) as centre and \( OQ \) as radius draw a circle.

Step 6: From \( G \) mark an arc in the line \( XY \) at \( M \), such that \( GM = 4.2 \text{ cm} \).

Step 7: Draw \( AB \) through \( M \) which is parallel to \( QR \).

Step 8: \( AB \) meets the circle at \( P \) and \( S \).

Step 9: Join \( QP \) and \( RP \). Then \( \Delta PQR \) is the required triangle.

#### Construction of a triangle when its base, the vertical angle and the point on the base where the bisector of the vertical angle meets the base

#### Example 4.17

Draw a triangle \( ABC \) of base \( BC = 8 \text{ cm} \), \( \angle A = 60^\circ \) and the bisector of \( \angle A \) meets \( BC \) at \( D \) such that \( BD = 6 \text{ cm} \).

<center>Fig. 4.44</center>

##### Construction

Step 1: Draw a line segment \( BC = 8 \text{ cm} \).

Step 2: At \( B \), draw \( BE \) such that \( \angle CBE = 60^\circ \).

Step 3: At \( B \), draw \( BF \) such that \( \angle EBF = 90^\circ \).

Step 4: Draw the perpendicular bisector to \( BC \), which intersects \( BF \) at \( O \) and \( BC \) at \( G \).

Step 5: With \( O \) as centre and \( OB \) as radius draw a circle.

Step 6: From \( B \), mark an arc of \( 6 \text{ cm} \) on \( BC \) at \( D \).

Step 7: The perpendicular bisector intersects the circle at I. Join \( ID \).

Step 8: \( ID \) produced meets the circle at \( A \). Now join \( AB \) and \( AC \).

Then \( \triangle ABC \) is the required triangle.

### Exercise 4.1

1. In \( \triangle ABC \), \( D \) and \( E \) are points on the sides \( AB \) and \( AC \) respectively such that \( DE \parallel BC \)

(i) If \( \frac{AD}{DB} = \frac{3}{4} \) and \( AC = 15 \text{ cm} \) find \( AE \).

(ii) If \( AD = 8x - 7 \), \( DB = 5x - 3 \), \( AE = 4x - 3 \) and \( EC = 3x - 1 \), find the value of \( x \).

2. ABCD is a trapezium in which \( AB \parallel DC \) and \( P, Q \) are points on \( AD \) and \( BC \) respectively, such that \( PQ \parallel DC \) if \( PD = 18 \text{ cm} \), \( BQ = 35 \text{ cm} \) and \( QC = 15 \text{ cm} \), find \( AD \).

3. In \( \Delta ABC \), \( D \) and \( E \) are points on the sides \( AB \) and \( AC \) respectively. Show that \( DE \parallel BC \) if \( AB = 12 \text{ cm} \), \( AD = 8 \text{ cm} \), \( AE = 12 \text{ cm} \) and \( AC = 18 \text{ cm} \).

4. In fig. if \( PQ \parallel BC \) and \( PR \parallel CD \) prove that

\[
\text{(i) } \frac{AR}{AD} = \frac{AQ}{AB} \qquad \text{(ii) } \frac{QB}{AQ} = \frac{DR}{AR}
\]

<center>Fig.4.45</center>

5. Rhombus PQRB is inscribed in \( \Delta ABC \) such that \( \angle B \) is one of its angle. \( P, Q \) and \( R \) lie on \( AB, AC \) and \( BC \) respectively. If \( AB = 12 \text{ cm} \) and \( BC = 6 \text{ cm} \), find the sides \( PQ, RB \) of the rhombus.

<center>Fig.4.46</center>

6. In trapezium \( ABCD \), \( AB \parallel DC \), \( E \) and \( F \) are points on non-parallel sides \( AD \) and \( BC \) respectively, such that \( EF \parallel AB \). Show that

\[
\frac{AE}{ED} = \frac{BF}{FC}
\]

<center>Fig.4.47</center>

7. In figure \( DE \parallel BC \) and \( CD \parallel EF \). Prove that

\[
AD^2 = AB \times AF
\]

8. Check whether \( AD \) is bisector of \( \angle A \) of \( \Delta ABC \) in each of the following

(i) \( AB = 5 \text{ cm} \), \( AC = 10 \text{ cm} \), \( BD = 1.5 \text{ cm} \) and \( CD = 3.5 \text{ cm} \).

(ii) \( AB = 4 \text{ cm} \), \( AC = 6 \text{ cm} \), \( BD = 1.6 \text{ cm} \) and \( CD = 2.4 \text{ cm} \).

9. In figure \( \angle QPR = 90^\circ \), PS is its bisector. If \( ST \perp PR \), prove that

\[
ST \times (PQ + PR) = PQ \times PR
\]

10. \( ABCD \) is a quadrilateral in which \( AB = AD \), the bisector of \( \angle BAC \) and \( \angle CAD \) intersect the sides \( BC \) and \( CD \) at the points \( E \) and \( F \) respectively. Prove that \( EF \parallel BD \).

11. Construct a \( \Delta PQR \) which the base \( PQ = 4.5 \text{ cm} \), \( \angle R = 35^\circ \) and the median \( RG \) from \( R \) to \( PQ \) is \( 6 \text{ cm} \).

12. Construct a \( \Delta PQR \) in which \( QR = 5 \text{ cm} \), \( \angle P = 40^\circ \) and the median \( PG \) from \( P \) to \( QR \) is \( 4.4 \text{ cm} \). Find the length of the altitude from \( P \) to \( QR \).

13. Construct a \( \Delta PQR \) such that \( QR = 6.5 \text{ cm} \), \( \angle P = 60^\circ \) and the altitude from \( P \) to \( QR \) is of length \( 4.5 \text{ cm} \).

14. Construct a \( \Delta ABC \) such that \( AB = 5.5 \text{ cm} \), \( \angle C = 25^\circ \) and the altitude from \( C \) to \( AB \) is \( 4 \text{ cm} \).

15. Draw a triangle \( ABC \) of base \( BC = 5.6 \text{ cm} \), \( \angle A = 40^\circ \) and the bisector of \( \angle A \) meets \( BC \) at \( D \) such that \( CD = 4 \text{ cm} \).

16. Draw \( \Delta PQR \) such that \( PQ = 6.8 \text{ cm} \), vertical angle is \( 50^\circ \) and the bisector of the vertical angle meets the base at \( D \) where \( PD = 5.2 \text{ cm} \).