---
title: 'Area of triangle'
weight: 2
---
## 5.2 Area of a Triangle

In your earlier classes, you have studied how to calculate the area of a triangle when its base and corresponding height (altitude) are given. You have used the formula:

{{<katex>}}
\text{Area of triangle} = \frac{1}{2} \times \text{base} \times \text{altitude} \text{ sq. units}
{{</katex>}}

With any three non-collinear points {{<katex>}}
A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3)
{{</katex>}}on a plane, we can form a triangle {{<katex>}}ABC{{</katex>}}.

![Triangle ABC with coordinates](image_triangle_area.png)

Using distance between two points formula, we can calculate {{<katex>}}AB = c{{</katex>}}, {{<katex>}}BC = a{{</katex>}}, {{<katex>}}CA = b{{</katex>}}. {{<katex>}}a, b, c{{</katex>}} represent the lengths of the sides of the triangle {{<katex>}}ABC{{</katex>}}.

Using {{<katex>}}2s = a + b + c{{</katex>}}, we can calculate the area of triangle {{<katex>}}ABC{{</katex>}} by using the Heron's formula {{<katex>}}\sqrt{s(s-a)(s-b)(s-c)}{{</katex>}}. But this procedure of finding length of sides of {{<katex>}}\triangle ABC{{</katex>}} and then calculating its area will be a tedious procedure.

There is an elegant way of finding area of a triangle using the coordinates of its vertices. We shall discuss such a method below.

Let {{<katex>}}ABC{{</katex>}} be any triangle whose vertices are at {{<katex>}}
A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3)
{{</katex>}}.

Draw {{<katex>}}
AP{{</katex>}}, {{<katex>}}BQ{{</katex>}} and {{<katex>}}CR{{</katex>}} perpendiculars from {{<katex>}}A, B{{</katex>}} and {{<katex>}}C
{{</katex>}} to the x-axis, respectively.

Clearly {{<katex>}}
ABQP{{</katex>}}, {{<katex>}}APRC{{</katex>}} and {{<katex>}}BQRC
{{</katex>}} are all trapeziums.

Now from the figure, it is clear that

{{<katex>}}
\text{Area of } \triangle ABC = \text{Area of trapezium } ABQP + \text{Area of trapezium } APRC - \text{Area of trapezium } BQRC
{{</katex>}}

You also know that, the area of trapezium {{<katex>}}
= \frac{1}{2} \times (\text{sum of parallel sides}) \times (\text{perpendicular distance between the parallel sides})
{{</katex>}}

Therefore,

{{<katex>}}
\text{Area of } \triangle ABC = \frac{1}{2}(BQ + AP)QP + \frac{1}{2}(AP + CR)PR - \frac{1}{2}(BQ + CR)QR
{{</katex>}}

{{<katex>}}
= \frac{1}{2}(y_2 + y_1)(x_1 - x_2) + \frac{1}{2}(y_1 + y_3)(x_3 - x_1) - \frac{1}{2}(y_2 + y_3)(x_3 - x_2)
{{</katex>}}

{{<katex>}}
= \frac{1}{2}\{x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\}
{{</katex>}}

Thus, the area of {{<katex>}}
\triangle ABC
{{</katex>}} is the absolute value of the expression

{{<katex>}}
\text{Area} = \frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)| \text{ sq. units}
{{</katex>}}

**Note:** The vertices {{<katex>}}
A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3){{</katex>}} of {{<katex>}}\triangle ABC{{</katex>}} are said to be "taken in order" if {{<katex>}}A, B, C{{</katex>}} are taken in anticlockwise direction. If we do this, then area of {{<katex>}}\triangle ABC
{{</katex>}} will never be negative.

### Another form

{{<katex>}}
\text{Area of } \triangle ABC = \frac{1}{2}\left|\begin{matrix} x_1 & x_2 & x_3 & x_1 \\ y_1 & y_2 & y_3 & y_1 \end{matrix}\right|
{{</katex>}}

{{<katex>}}
= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_1) - (x_2y_1 + x_3y_2 + x_1y_3)\} \text{ sq. units}
{{</katex>}}

> **Note:** As the area of a triangle can never be negative, we must take the absolute value, in case area happens to be negative.

---

## Progress Check

The vertices of {{<katex>}}
\triangle PQR{{</katex>}} are {{<katex>}}P(0,4){{</katex>}}, {{<katex>}}Q(3,1){{</katex>}} and {{<katex>}}R(8,1)
{{</katex>}}

1. Draw {{<katex>}}
\triangle PQR
{{</katex>}} on a graph paper.
2. Check if {{<katex>}}
\triangle PQR
{{</katex>}} is equilateral.
3. Find the area of {{<katex>}}
\triangle PQR
{{</katex>}}.
4. Find the coordinates of {{<katex>}}
M{{</katex>}}, the mid-point of {{<katex>}}QP
{{</katex>}}.
5. Find the coordinates of {{<katex>}}
N{{</katex>}}, the mid-point of {{<katex>}}QR
{{</katex>}}.
6. Find the area of {{<katex>}}
\triangle MPN
{{</katex>}}.
7. What is the ratio between the areas of {{<katex>}}
\triangle MPN{{</katex>}} and {{<katex>}}\triangle PQR
{{</katex>}}?

---

## 5.2.1 Collinearity of three points

If three distinct points {{<katex>}}
A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3){{</katex>}} are collinear, then we cannot form a triangle, because for such a triangle there will be no altitude (height). Therefore, three points {{<katex>}}A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3){{</katex>}} will be collinear if the area of {{<katex>}}\triangle ABC = 0
{{</katex>}}.

### Another condition for collinearity

If {{<katex>}}
A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3)
{{</katex>}} are collinear points, then

{{<katex>}}
x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) = 0
{{</katex>}}

or

{{<katex>}}
x_1y_2 + x_2y_3 + x_3y_1 = x_2y_1 + x_3y_2 + x_1y_3
{{</katex>}}

Similarly, if the area of {{<katex>}}
\triangle ABC{{</katex>}} is zero, then the three points lie on the same straight line. Thus, three distinct points {{<katex>}}A(x_1, y_1){{</katex>}}, {{<katex>}}B(x_2, y_2){{</katex>}} and {{<katex>}}C(x_3, y_3){{</katex>}} will be collinear if and only if area of {{<katex>}}\triangle ABC = 0
{{</katex>}}.

---