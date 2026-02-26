---
title: 'Area of triangle'
weight: 2
---

## 5.2 Area of a Triangle

In your earlier classes, you have studied how to calculate the area of a triangle when its base and corresponding height (altitude) are given. You have used the formula:

{{< katex display=true >}}
\text{Area of triangle} = \frac{1}{2} \times \text{base} \times \text{altitude} \text{ sq. units}
{{< /katex >}}

With any three non-collinear points {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, {{< katex display=true >}}
B(x_2, y_2){{< katex display=true >}}
 and 
{{< /katex >}}C(x_3, y_3)
{{< /katex >}} on a plane, we can form a triangle 
{{< /katex >}}ABC
{{< /katex >}}.

Using distance between two points formula, we can calculate {{< katex display=true >}}
AB = c{{< katex display=true >}}
, {{< katex display=true >}}
BC = a{{< katex display=true >}}
, {{< katex display=true >}}
CA = b
{{< /katex >}}. 
{{< /katex >}}a, b, c
{{< /katex >}} represent the lengths of the sides of the triangle 
{{< /katex >}}ABC
{{< /katex >}}.

Using {{< katex display=true >}}
2s = a + b + c{{< katex display=true >}}
, we can calculate the area of triangle {{< katex display=true >}}
ABC{{< katex display=true >}}
 by using the **Heron's formula**: 
{{< /katex >}}\sqrt{s(s-a)(s-b)(s-c)}
{{< /katex >}}. But this procedure of finding length of sides of 
{{< /katex >}}\triangle ABC
{{< /katex >}} and then calculating its area will be a tedious procedure.

There is an elegant way of finding area of a triangle using the coordinates of its vertices. We shall discuss such a method below.

Let {{< katex display=true >}}
ABC{{< katex display=true >}}
 be any triangle whose vertices are at {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, 
{{< /katex >}}B(x_2, y_2)
{{< /katex >}} and 
{{< /katex >}}C(x_3, y_3)
{{< /katex >}}.

Draw {{< katex display=true >}}
AP{{< katex display=true >}}
, {{< katex display=true >}}
BQ{{< katex display=true >}}
 and {{< katex display=true >}}
CR{{< katex display=true >}}
 perpendiculars from 
{{< /katex >}}A
{{< /katex >}}, 
{{< /katex >}}B
{{< /katex >}} and 
{{< /katex >}}C
{{< /katex >}} to the x-axis, respectively.

Clearly {{< katex display=true >}}
ABQP{{< katex display=true >}}
, {{< katex display=true >}}
APRC
{{< /katex >}} and 
{{< /katex >}}BQRC
{{< /katex >}} are all trapeziums.

Now from the figure, it is clear that:

{{< katex display=true >}}
\text{Area of } \triangle ABC = \text{Area of trapezium } ABQP + \text{Area of trapezium } APRC - \text{Area of trapezium } BQRC
{{< /katex >}}

You also know that, the area of trapezium {{< katex display=true >}}
= \frac{1}{2} \times (\text{sum of parallel sides}) \times (\text{perpendicular distance between the parallel sides})
{{< /katex >}}

Therefore, Area of {{< katex display=true >}}
\triangle ABC
{{< /katex >}}:

{{< katex display=true >}}
= \frac{1}{2}(BQ + AP)QP + \frac{1}{2}(AP + CR)PR - \frac{1}{2}(BQ + CR)QR
{{< /katex >}}

After simplification:

{{< katex display=true >}}
\text{Area of } \triangle ABC = \frac{1}{2}\{x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\} \text{ sq. units}
{{< /katex >}}

Thus, the area of {{< katex display=true >}}
\triangle ABC
{{< /katex >}} is the **absolute value** of the expression.

> **Note:** The vertices {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, {{< katex display=true >}}
B(x_2, y_2){{< katex display=true >}}
 and {{< katex display=true >}}
C(x_3, y_3){{< katex display=true >}}
 of 
{{< /katex >}}\triangle ABC
{{< /katex >}} are said to be **"taken in order"** if 
{{< /katex >}}A, B, C
{{< /katex >}} are taken in anticlockwise direction. If we do this, then area of 
{{< /katex >}}\triangle ABC
{{< /katex >}} will never be negative.

> **Note:** As the area of a triangle can never be negative, we must take the absolute value, in case area happens to be negative.

### Another form

{{< katex display=true >}}
\text{Area of } \triangle ABC = \frac{1}{2}\begin{vmatrix} x_1 & x_2 & x_3 & x_1 \\ y_1 & y_2 & y_3 & y_1 \end{vmatrix}
{{< /katex >}}

{{< katex display=true >}}
= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_1) - (x_2y_1 + x_3y_2 + x_1y_3)\} \text{ sq. units}
{{< /katex >}}

---

## Progress Check

The vertices of {{< katex display=true >}}
\triangle PQR{{< katex display=true >}}
 are {{< katex display=true >}}
P(0,-4){{< katex display=true >}}
, 
{{< /katex >}}Q(3,1)
{{< /katex >}} and 
{{< /katex >}}R(-8,1)
{{< /katex >}}

1. Draw {{< katex display=true >}}
\triangle PQR
{{< /katex >}} on a graph paper.
2. Check if {{< katex display=true >}}
\triangle PQR
{{< /katex >}} is equilateral.
3. Find the area of {{< katex display=true >}}
\triangle PQR
{{< /katex >}}.
4. Find the coordinates of {{< katex display=true >}}
M{{< katex display=true >}}
, the mid-point of 
{{< /katex >}}QP
{{< /katex >}}.
5. Find the coordinates of {{< katex display=true >}}
N{{< katex display=true >}}
, the mid-point of 
{{< /katex >}}QR
{{< /katex >}}.
6. Find the area of {{< katex display=true >}}
\triangle MPN
{{< /katex >}}.
7. What is the ratio between the areas of {{< katex display=true >}}
\triangle MPN{{< katex display=true >}}
 and 
{{< /katex >}}\triangle PQR
{{< /katex >}}?

---

## 5.2.1 Collinearity of three points

If three distinct points {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, {{< katex display=true >}}
B(x_2, y_2){{< katex display=true >}}
 and {{< katex display=true >}}
C(x_3, y_3){{< katex display=true >}}
 are collinear, then we cannot form a triangle, because for such a triangle there will be no altitude (height). Therefore, three points {{< katex display=true >}}
A(x_1, y_1)
{{< /katex >}}, 
{{< /katex >}}B(x_2, y_2)
{{< /katex >}} and 
{{< /katex >}}C(x_3, y_3)
{{< /katex >}} will be collinear if the area of 
{{< /katex >}}\triangle ABC = 0
{{< /katex >}}.

### Another condition for collinearity

If {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, {{< katex display=true >}}
B(x_2, y_2)
{{< /katex >}} and 
{{< /katex >}}C(x_3, y_3)
{{< /katex >}} are collinear points, then:

{{< katex display=true >}}
x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) = 0
{{< /katex >}}

or

{{< katex display=true >}}
x_1y_2 + x_2y_3 + x_3y_1 = x_2y_1 + x_3y_2 + x_1y_3
{{< /katex >}}

Similarly, if the area of {{< katex display=true >}}
\triangle ABC{{< katex display=true >}}
 is zero, then the three points lie on the same straight line. Thus, three distinct points {{< katex display=true >}}
A(x_1, y_1){{< katex display=true >}}
, {{< katex display=true >}}
B(x_2, y_2)
{{< /katex >}} and 
{{< /katex >}}C(x_3, y_3)
{{< /katex >}} will be collinear if and only if area of 
{{< /katex >}}\triangle ABC = 0
{{< /katex >}}.

---