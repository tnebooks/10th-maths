---
title: 'Concurrency Theorems'
weight: 5
---

# 4.6 Concurrency Theorems

## Definition

A **cevian** is a line segment that extends from one vertex of a triangle to the opposite side. In the diagram, {{< katex >}}  AD
{{< /katex >}}
 is a cevian, from {{< katex >}}  A
{{< /katex >}}.

![](24.png)

## Special Cevians

- **(i) A median** is a cevian that divides the opposite side into two congruent (equal) lengths.
- **(ii) An altitude** is a cevian that is perpendicular to the opposite side.
- **(iii) An angle bisector** is a cevian that bisects the corresponding angle.

The term cevian comes from the name of Italian engineer **Giovanni Ceva**, who proved a well known theorem about cevians.

![](25.png)

---

## Ceva's Theorem (without proof)

**Statement:** Let {{< katex >}}  ABC
{{< /katex >}}
 be a triangle and let {{< katex >}}  D, E, F
{{< /katex >}} 
 be points on lines {{< katex >}}  BC
{{< /katex >}},
  {{< katex >}}  CA
{{< /katex >}},
   {{< katex >}}  AB
{{< /katex >}} 
   respectively. Then the cevians {{< katex >}}  \overline{AD}, \overline{BE}, \overline{CF}
{{< /katex >}} are concurrent if and only if:

{{< katex >}}
{{< /katex >}}


![](26.png)


where the lengths are directed. This also works for the reciprocal of each of the ratios as the reciprocal of 1 is 1.

![](27.png)

**Note:** The cevians do not necessarily lie within the triangle, although they do in the diagram.

---

## Menelaus Theorem (without proof)

**Statement:** A necessary and sufficient condition for points {{< katex >}}  P, Q, R
{{< /katex >}} 
on the respective sides {{< katex >}}  BC, CA, AB
{{< /katex >}}
 (or their extension) of a triangle {{< katex >}}  ABC
{{< /katex >}} to be collinear is that:

{{< katex >}}  \frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{AR}{RB} = -1
{{< /katex >}}


![](28.png)

where all segments in the formula are directed segments.

![](29.png)

**Note:** 
- Menelaus theorem can also be given as {{< katex >}}  \frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{AR}{RB} = -1
{{< /katex >}}.
- If {{< katex >}}  BP
{{< /katex >}} 
is replaced by {{< katex >}}  PB
{{< /katex >}}
 (or) {{< katex >}}  CQ
{{< /katex >}} by 
 {{< katex >}}  QC
{{< /katex >}} (or) 
 {{< katex >}}  AR
{{< /katex >}} by
  {{< katex >}}  RA
{{< /katex >}},
   or if any one of the six directed line segments {{< katex >}}  BP, PC, CQ, QA, AR, RB
{{< /katex >}} is interchanged, then the product will be 1.

---

## Examples

### Example 4.32

Show that in a triangle, the medians are concurrent.

![](30.png)

**Solution:** Medians are line segments joining each vertex to the midpoint of the corresponding opposite sides.

Thus medians are the cevians where {{< katex >}}  D, E, F
{{< /katex >}} 
are midpoints of {{< katex >}}  BC, CA
{{< /katex >}} 
and {{< katex >}}  AB
{{< /katex >}} respectively.

Since {{< katex >}}  D
{{< /katex >}}
 is a midpoint of {{< katex >}}  BC
{{< /katex >}},
  {{< katex >}}  BD = DC so \frac{BD}{DC} = 1
{{< /katex >}} ... (1)

Since, {{< katex >}}  E
{{< /katex >}} 
is a midpoint of {{< katex >}}  CA
{{< /katex >}}, 
{{< katex >}}  CE = EA
{{< /katex >}} 
so {{< katex >}}  \frac{CE}{EA} = 1
{{< /katex >}} ... (2)

Since, {{< katex >}}  F
{{< /katex >}}
 is a midpoint of {{< katex >}}  AB
{{< /katex >}},
  {{< katex >}}  AF = FB
{{< /katex >}}
   so {{< katex >}}  \frac{AF}{FB} = 1
{{< /katex >}} ... (3)

Thus, multiplying (1), (2) and (3) we get:

{{< katex >}}  \frac{BD}{DC} \times \frac{CE}{EA} \times \frac{AF}{FB} = 1 \times 1 \times 1 = 1
{{< /katex >}}

And so, Ceva's theorem is satisfied.

Hence the Medians are concurrent.

![](31.png)

---

### Example 4.33

In {{< katex >}}  \triangle ABC
{{< /katex >}}
, points {{< katex >}}  D, E, F
{{< /katex >}} 
lies on {{< katex >}}  BC, CA, AB
{{< /katex >}}
 respectively. Suppose {{< katex >}}  AB, AC
{{< /katex >}}
  and {{< katex >}}  BC
{{< /katex >}} 
  have lengths 13, 14 and 15 respectively. If {{< katex >}}  \frac{AF}{FB} = \frac{2}{5}
{{< /katex >}} 
      and {{< katex >}}  \frac{CE}{EA} = \frac{5}{8}{{< /katex >}}LM.{{< katex >}}   Find    BD {{< /katex >}} {{< katex >}} LM and DC{{< /katex >}}.

![](32.png)

**Solution:** Given that {{< katex >}}  AB = 13
{{< /katex >}},
 {{< katex >}}  AC = 14
{{< /katex >}}
  and {{< katex >}}  BC = 15
{{< /katex >}}.

Let {{< katex >}}  BD = x
{{< /katex >}}, 
{{< katex >}}  DC = y
{{< /katex >}}

Using Ceva's theorem, we have:

{{< katex >}}  \frac{BD}{DC} \times \frac{CE}{EA} \times \frac{AF}{FB} = 1 \text{ ... (1)}
{{< /katex >}}

Substitute the values of {{< katex >}}  \frac{AF}{FB}
{{< /katex >}}
 and {{< katex >}}  \frac{CE}{EA}
{{< /katex >}} in (1):

{{< katex >}}  \frac{x}{y} \times \frac{5}{8} \times \frac{2}{5} = 1
{{< /katex >}}

{{< katex >}}  \frac{x}{y} \times \frac{10}{40} = 1
{{< /katex >}}

{{< katex >}}  \frac{x}{y} \times \frac{1}{4} = 1
{{< /katex >}}

Hence, {{< katex >}}  \frac{x}{y} = 4
{{< /katex >}},
 so {{< katex >}}  x = 4y
{{< /katex >}} ... (2)

{{< katex >}}  BC = BD + DC = 15
{{< /katex >}} so,
 {{< katex >}}  x + y = 15
{{< /katex >}} ... (3)

From (2), using {{< katex >}}  x = 4y
{{< /katex >}}
 in (3) we get, {{< katex >}}  4y + y = 15
{{< /katex >}}
  gives {{< katex >}}  5y = 15
{{< /katex >}} 
  then {{< katex >}}  y = 3
{{< /katex >}}

Substitute {{< katex >}}  y = 3
{{< /katex >}} 
in (3) we get, {{< katex >}}  x = 12
{{< /katex >}}.

Hence {{< katex >}}  BD = 12
{{< /katex >}}
, {{< katex >}}  DC = 3
{{< /katex >}}.

---

### Example 4.34

In a garden containing several trees, three particular trees {{< katex >}}  P, Q, R
{{< /katex >}} 
are located in the following way, {{< katex >}}  BP = 2
{{< /katex >}} 
m, {{< katex >}}  CQ = 3
{{< /katex >}} 
m, {{< katex >}}  RA = 10
{{< /katex >}}
 m, {{< katex >}}  PC = 6
{{< /katex >}}
  m, {{< katex >}}  QA = 5
{{< /katex >}}
   m, {{< katex >}}  RB = 2
{{< /katex >}} 
   m, where {{< katex >}}  A, B, C
{{< /katex >}} 
   are points such that {{< katex >}}  P
{{< /katex >}} 
   lies on {{< katex >}}  BC
{{< /katex >}},
    {{< katex >}}  Q
{{< /katex >}}
    lies on {{< katex >}}  AC
{{< /katex >}} 
    and {{< katex >}}  R
{{< /katex >}}
     lies on {{< katex >}}  AB
{{< /katex >}}.
      Check whether the trees {{< katex >}}  P, Q, R
{{< /katex >}} lie on a same straight line.

![](33.png)

**Solution:** By Menelaus's theorem, the trees {{< katex >}}  P, Q, R
{{< /katex >}} will be collinear (lie on same straight line) if:

{{< katex >}}  \frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{AR}{RB} = 1 \text{ ... (1)}
{{< /katex >}}

Given {{< katex >}}  BP = 2
{{< /katex >}} m,
 {{< katex >}}  CQ = 3
{{< /katex >}} m,
  {{< katex >}}  RA = 10
{{< /katex >}} 
  m, {{< katex >}}  PC = 6
{{< /katex >}}
   m, {{< katex >}}  QA = 5
{{< /katex >}}
    m and {{< katex >}}  RB = 2
{{< /katex >}} m

Substituting these values in (1) we get:

{{< katex >}}  \frac{BP}{PC} \times \frac{CQ}{QA} \times \frac{RA}{RB} = \frac{2}{6} \times \frac{3}{5} \times \frac{10}{2} = \frac{1}{3} \times \frac{3}{5} \times 5 = \frac{60}{60} = 1
{{< /katex >}}

Hence the trees {{< katex >}}  P, Q, R
{{< /katex >}} lie on a same straight line.

![](34.png)

## Exercise 4.4

1. The length of the tangent to a circle from a point P, which is 25cm away from the centre is 24cm. What is the radius of the circle?

2. LMN is a right angled triangle with ∠L = 90°. A circle is inscribed in it. The lengths of the sides containing the right angle are 6cm and 8cm. Find the radius of the circle.

3. A circle is inscribed in ΔABC having sides 8cm, 10cm and 12cm as shown in figure, Find AD, BE and CF.

![](35.png)

4. PQ is a tangent drawn from a point P to a circle with centre O and QOR is a diameter of the circle such that ∠POR = 120°. Find ∠OPQ.

5. A tangent ST to a circle touches it at B. AB is a chord such that ∠ABT = 65°. Find ∠AOB, where "O" is the centre of the circle.

6. In figure, O is the centre of the circle with radius 5cm. T is a point such that OT = 13cm and OT intersects the circle at E, if AB is the tangent to the circle at E, find the length of AB.

![](36.png)

7. In two concentric circles, a chord of length 16cm of larger circle becomes a tangent to the smaller circle whose radius is 6cm. Find the radius of the larger circle.

8. Two circles with centres O and O' of radii 3cm and 4cm, respectively intersect at two points P and Q, such that OP and O'P are tangents to the two circles. Find the length of the common chord PQ.

9. Show that the angle bisectors of a triangle are concurrent.

10. An artist has created a triangular stained glass window and has one strip of small length left before completing the window. She needs to figure out the length of left out portion based on the lengths of the other sides as shown in the figure.

![](37.png)

11. Draw a tangent at any point R on the circle of radius 3.4cm and centre at P.

12. Draw a circle of radius 4.5cm. Take a point on the circle. Draw the tangent at that point using the alternate segment theorem.

13. Draw the two tangents from a point which is 10cm away from the centre of a circle of radius 5cm. Also, measure the lengths of the tangents.

14. Take a point which is 11cm away from the centre of a circle of radius 4cm and draw the two tangents to the circle from that point.

15. Draw the two tangents from a point which is 5cm away from the centre of a circle of diameter 6cm. Also, measure the lengths of the tangents.

16. Draw a tangent to the circle from the point P having radius 3.6cm, and centre at O. Point P is at a distance 7.2cm from the centre.

---

## Exercise 4.5 (Multiple Choice Questions)

1. If in triangles ABC and EDF, AB/DE = BC/FD then they will be similar, when
   (A) ∠B = ∠E
   (B) ∠A = ∠D
   (C) ∠B = ∠D
   (D) ∠A = ∠F

2. In ΔLMN, ∠L = 60°, ∠M = 50°. If ΔLMN ~ ΔPQR then the value of ∠R is
   (A) 40°
   (B) 70°
   (C) 30°
   (D) 110°

3. If ΔABC is an isosceles triangle with ∠C = 90° and AC = 5cm, then AB is
   (A) 2.5cm
   (B) 5cm
   (C) 10cm
   (D) 5√2 cm

4. In a given figure ST || QR, PS = 2cm and SQ = 3cm. Then the ratio of the area of ΔPQR to the area of ΔPST is
   (A) 25:4
   (B) 25:7
   (C) 25:11
   (D) 25:13

![](38.png)

5. The perimeters of two similar triangles ΔABC and ΔPQR are 36cm and 24cm respectively. If PQ = 10cm, then the length of AB is
   (A) 6⅔ cm
   (B) 10⅔ cm
   (C) 6⅔ cm
   (D) 15cm

6. If in ΔABC, DE || BC. AB = 3cm, AC = 2.4cm and AD = 2.1cm then the length of AE is
   (A) 1.4cm
   (B) 1.8cm
   (C) 1.2cm
   (D) 1.05cm

7. In a ΔABC, AD is the bisector of ∠BAC. If AB = 8cm, BD = 6cm and DC = 3cm. The length of the side AC is
   (A) 6cm
   (B) 4cm
   (C) 3cm
   (D) 8cm

8. In the adjacent figure ∠BAC = 90° and AD ⊥ BC then
   (A) BD × CD = BC²
   (B) AB × AC = BC²
   (C) BD × CD = AD²
   (D) AB × AC = AD²

![](39.png)

9. Two poles of heights 6m and 11m stand vertically on a plane ground. If the distance between their feet is 12m, what is the distance between their tops?
   (A) 13m
   (B) 14m
   (C) 15m
   (D) 12.8m

10. In the given figure, PR = 26cm, QR = 24cm, ∠PAQ = 90°, PA = 6cm and QA = 8cm. Find ∠PQR
    (A) 80°
    (B) 85°
    (C) 75°
    (D) 90°

![](40.png)

11. A tangent is perpendicular to the radius at the
    (A) centre
    (B) point of contact
    (C) infinity
    (D) chord

12. How many tangents can be drawn to the circle from an exterior point?
    (A) one
    (B) two
    (C) infinite
    (D) zero

13. The two tangents from an external points P to a circle with centre at O are PA and PB. If ∠APB = 70° then the value of ∠AOB is
    (A) 100°
    (B) 110°
    (C) 120°
    (D) 130°

14. In figure if AB is another tangent touching the circle at R. If CP = 11cm and BC = 7cm, then BR =
    (A) 6cm
    (B) 5cm
    (C) 8cm
    (D) 4cm

    ![](41.png)

15. In figure if PR is tangent to the circle at P and O is the centre of the circle, then ∠POQ is
    (A) 120°
    (B) 100°
    (C) 110°
    (D) 90°

 ![](42.png)

---

## Unit Exercise - 4

1. In the figure, if BD ⊥ AC and CE ⊥ AB, prove that
   (i) ΔAEC ~ ΔADB
   (ii) CA/AB = CE/DB

 ![](43.png)

2. In the given figure AB || CD || EF. If AB = 6cm, CD = x cm, EF = 4cm, BD = 5cm and DE = y cm. Find x and y.

 ![](44.png)

3. O is any point inside a triangle ABC. The bisector of ∠AOB, ∠BOC and ∠COA meet the sides AB, BC and CA in point D, E and F respectively. Show that (AD/DB) × (BE/EC) × (CF/FA) = 1

4. In the figure, ABC is a triangle in which AB = AC. Points D and E are points on the side AB and AC respectively such that AD = AE. Show that the points B, C, E and D lie on a same circle.

 ![](45.png)

5. Two trains leave a railway station at the same time. The first train travels due west and the second train due north. The first train travels at a speed of 20km/hr and the second train travels at 30km/hr. After 2 hours, what is the distance between them?

6. D is the mid point of side BC and AE ⊥ BC. If BC = a, AC = b, AB = c, ED = x, AD = p and AE = h, prove that
   (i) b² = p² + ax + a²/4
   (ii) c² = p² - ax + a²/4
   (iii) b² + c² = 2p² + a²/2

7. A man whose eye-level is 2m above the ground wishes to find the height of a tree. He places a mirror horizontally on the ground 20m from the tree and finds that if he stands at a point C which is 4m from the mirror B, he can see the reflection of the top of the tree. How height is the tree?

8. An Emu which is 8 feet tall is standing at the foot of a pillar which is 30 feet high. It walks away from the pillar. The shadow of the Emu falls beyond Emu. What is the relation between the length of the shadow and the distance from the Emu to the pillar?

9. Two circles intersect at A and B. From a point P on one of the circles lines PAC and PBD are drawn intersecting the second circle at C and D. Prove that CD is parallel to the tangent at P.

10. Let ABC be a triangle and D, E, F are points on the respective sides AB, BC, AC (or their extensions). Let AD:DB = 5:3, BE:EC = 3:2 and AC = 21. Find the length of the line segment CF.

 ![](46.png)

  ![](47.png)