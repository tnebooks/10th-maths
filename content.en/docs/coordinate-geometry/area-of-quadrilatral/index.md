---
title: 'Area of Quadrilatral'
weight: 3
---
## 5.3 Area of a Quadrilateral

If {{< katex >}}ABCD{{< /katex >}} is a quadrilateral, then considering the diagonal {{< katex >}}AC{{< /katex >}}, we can split the quadrilateral {{< katex >}}ABCD{{< /katex >}} into two triangles {{< katex >}}ABC{{< /katex >}} and {{< katex >}}ACD{{< /katex >}}.

Using area of triangle formula given its vertices, we can calculate the areas of triangles {{< katex >}}ABC{{< /katex >}} and {{< katex >}}ACD{{< /katex >}}.

Now, Area of the quadrilateral {{< katex >}}ABCD{{< /katex >}} = Area of triangle {{< katex >}}ABC{{< /katex >}} + Area of triangle {{< /katex >}}ACD{{< /katex >}}

We use this information to find area of a quadrilateral when its vertices are given.

Let {{< katex >}}A(x_1, y_1){{< /katex >}}, {{< katex >}}B(x_2, y_2){{< /katex >}}, {{< katex >}}C(x_3, y_3){{< /katex >}} and {{< katex >}}D(x_4, y_4){{< /katex >}} be the vertices of a quadrilateral {{< katex >}}ABCD{{< /katex >}}.

Now, Area of quadrilateral {{< katex >}}ABCD{{< /katex >}}:
{{< katex >}}= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_4 + x_4y_1) - (x_2y_1 + x_3y_2 + x_4y_3 + x_1y_4)\} \text{ sq. units}{{< /katex >}}

or

{{< katex >}}= \frac{1}{2}\{(x_1 - x_3)(y_2 - y_4) - (x_2 - x_4)(y_1 - y_3)\} \text{ sq. units}{{< /katex >}}

> **Note:** 
> - To find the area of a quadrilateral, we divide it into triangular regions, which have no common area and then add the area of these regions.
> - The area of the quadrilateral is never negative. That is, we always take the area of quadrilateral as positive.

### Thinking Corner

How many triangles exist, whose area is zero?
1. If the area of a quadrilateral formed by the points {{< katex >}}(a,a){{< /katex >}}, {{< katex >}}(-a,a){{< /katex >}}, {{< katex >}}(a,-a){{< /katex >}} and {{< katex >}}(-a,-a){{< /katex >}}, where {{< katex >}}a \neq 0{{< /katex >}} is 64 square units, then identify the type of the quadrilateral.
2. Find all possible values of {{< katex >}}a{{< /katex >}}.

---


### Example 5.1

Find the area of the triangle whose vertices are {{< katex >}}(-3,5){{< /katex >}}, {{< katex >}}(5,6){{< /katex >}} and {{< katex >}}(5,-2){{< /katex >}}.

**Solution:** Plot the points in a rough diagram and take them in counter-clockwise order.

Let the vertices be {{< katex >}}A(-3,5){{< /katex >}}, {{< katex >}}B(5,-2){{< /katex >}}, {{< katex >}}C(5,6){{< /katex >}}.

The area of {{< katex >}}\triangle ABC{{< /katex >}} is:
{{< katex >}}= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_1) - (x_2y_1 + x_3y_2 + x_1y_3)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{(6 + 30 + 25) - (-25 - 10 - 18)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{61 + 53\} = \frac{1}{2} \times 114 = 32 \text{ sq. units}{{< /katex >}}

---

### Example 5.2

Show that the points {{< katex >}}P(-1,5){{< /katex >}}, {{< katex >}}Q(6,2){{< /katex >}}, {{< katex >}}R(-3,4){{< /katex >}} are collinear.

**Solution:** The points are {{< katex >}}P(-1,5){{< /katex >}}, {{< katex >}}Q(6,2){{< /katex >}}, {{< katex >}}R(-3,4){{< /katex >}}.

Area of {{< katex >}}\triangle PQR{{< /katex >}}:

{{< katex >}}= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_1) - (x_2y_1 + x_3y_2 + x_1y_3)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{(-2 + 24 - 15) - (30 - 6 - 4)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{7 - 20\} = \frac{1}{2} \times (-18) = 0{{< /katex >}}

Therefore, the given points are collinear.

---

### Example 5.3

If the area of the triangle formed by the vertices {{< katex >}}A(-1,2){{< katex >}}, {{< katex >}}B(k,-2){{< katex >}} and {{< katex >}}C(7,4){{< katex >}} (taken in order) is 22 sq. units, find the value of {{< katex >}}k{{< katex >}}.

**Solution:** The vertices are {{< katex >}}A(-1,2){{< /katex >}}, {{< katex >}}B(k,-2){{< /katex >}} and {{< katex >}}C(7,4){{< /katex >}}.

Area of triangle {{< katex >}}ABC{{< /katex >}} is 22 sq. units:

{{< katex >}}\frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_1) - (x_2y_1 + x_3y_2 + x_1y_3)\} = 22{{< /katex >}}

{{< katex >}}\frac{1}{2}\{(2 + 4k + 14) - (-2k - 14 - 4)\} = 22{{< /katex >}}

{{< katex >}}\frac{1}{2}\{2k + 34\} = 22{{< /katex >}}

{{< katex >}}2k + 34 = 44 \text{ gives } 2k = 10 \text{ so } k = 5{{< /katex >}}

---

### Example 5.4

If the points {{< katex >}}P(-1,4){{< /katex >}}, {{< katex >}}Q(b,c){{< /katex >}} and {{< katex >}}R(5,-1){{< /katex >}} are collinear and if {{< katex >}}2b + c = 4{{< /katex >}}, then find the values of {{< katex >}}b{{< /katex >}} and {{< katex >}}c{{< /katex >}}.

**Solution:** Since the three points {{< katex >}}P(-1,4){{< /katex >}}, {{< katex >}}Q(b,c){{< /katex >}} and {{< katex >}}R(5,-1){{< /katex >}} are collinear,

Area of triangle {{< katex >}}PQR = 0{{< /katex >}}:

{{< katex >}}\frac{1}{2}\{(-c - b - 20) - (-4b + 5c + 1)\} = 0{{< /katex >}}

{{< katex >}}-c - b - 20 + 4b - 5c - 1 = 0{{< /katex >}}

{{< katex >}}3b - 6c - 21 = 0{{< /katex >}}

{{< katex >}}b - 2c = 7 \quad \text{...(1)}{{< /katex >}}

Also, {{< katex >}}2b + c = 4 \quad \text{...(2)}{{< /katex >}} (from given information)

Solving (1) and (2) we get {{< katex >}}b = 3{{< /atex >}}, {{< katex >}}c = -2{{< /katex >}}.

---

### Example 5.5

The floor of a hall is covered with identical tiles which are in the shapes of triangles. One such triangle has the vertices at {{< katex >}}(-3,2){{< /katex >}}, {{< katex >}}(-1,-1){{< /katex >}} and {{< katex >}}(1,2){{< /katex >}}. If the floor of the hall is completely covered by 110 tiles, find the area of the floor.

**Solution:** Vertices of one triangular tile are at {{< katex >}}(-3,2){{< /katex >}}, {{< katex >}}(-1,-1){{< /katex >}} and {{< katex >}}(1,2){{< /katex >}}.

Area of this tile:

{{< katex >}}= \frac{1}{2}\{(3 - 2 + 2) - (-2 - 1 - 6)\} \text{ sq. units}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{3 + 9\} = 6 \text{ sq. units}{{< /katex >}}

Since the floor is covered by 110 triangle shaped identical tiles,

{{< katex >}}\text{Area of floor} = 110 \times 6 = 660 \text{ sq. units}{{< /katex >}}

---

### Example 5.6

Find the area of the quadrilateral formed by the points {{< katex >}}(8,6){{< /katex >}}, {{< katex >}}(5,11){{< /katex >}}, {{< katex >}}(-5,12){{< /katex >}} and {{< katex >}}(-4,3){{< /katex >}}.

**Solution:** Before determining the area of quadrilateral, plot the vertices in a graph.

Let the vertices be {{< katex >}}A(8,6){{< /katex >}}, {{< katex >}}B(5,11){{< /katex >}}, {{< katex >}}C(-5,12){{< /katex >}} and {{< katex >}}D(-4,3){{< /katex >}}.

Therefore, area of the quadrilateral {{< katex >}}ABCD{{< /katex >}}:

{{< katex >}}= \frac{1}{2}\{(x_1y_2 + x_2y_3 + x_3y_4 + x_4y_1) - (x_2y_1 + x_3y_2 + x_4y_3 + x_1y_4)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{(88 + 60 + 15 - 24) - (30 - 55 - 48 + 24)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{139 + 49\} = \frac{1}{2} \times 158 = 79 \text{ sq. units}{{< /katex >}}

---

### Example 5.7

The given diagram shows a plan for constructing a new parking lot at a campus. It is estimated that such construction would cost ₹1300 per square feet. What will be the total cost for making the parking lot?

**Solution:** The parking lot is a quadrilateral whose vertices are at {{< katex >}}A(2,2){{< /katex >}}, {{< katex >}}B(5,5){{< /katex >}}, {{< katex >}}C(4,9){{< /katex >}} and {{< katex >}}D(1,7){{< /katex >}}.

Area of parking lot:

{{< katex >}}= \frac{1}{2}\{(10 + 45 + 28 + 2) - (10 + 20 + 9 + 14)\}{{< /katex >}}

{{< katex >}}= \frac{1}{2}\{85 - 53\} = \frac{1}{2} \times 32 = 16 \text{ sq. units}{{< /katex >}}

Area of parking lot = 16 sq. feet

Construction rate per square feet = ₹1300

{{< katex >}}\text{Total cost for constructing the parking lot} = 16 \times 1300 = ₹20800{{< /katex >}}

---

## Activity 1

(i) Take a graph sheet.
(ii) Consider a triangle whose base is the line joining the points {{< katex >}}(0,0){{< /katex >}} and {{< katex >}}(6,0){{< /katex >}}.
(iii) Take the third vertex as {{< katex >}}(1,1){{< /katex >}}, {{< katex >}}(2,2){{< /katex >}}, {{< katex >}}(3,3){{< /katex >}}, {{< katex >}}(4,4){{< /katex >}}, {{< katex >}}(5,5){{< /katex >}} and find their areas. Fill in the details given.
(iv) Do you see any pattern with {{< katex >}}A_1, A_2, A_3, A_4, A_5{{< /katex >}}? If so mention it.
(v) Repeat the same process by taking third vertex in step (iii) as {{< katex >}}(1,2){{< /katex >}}, {{< katex >}}(2,4){{< /katex >}}, {{< katex >}}(3,8){{< /katex >}}, {{< katex >}}(4,16){{< /katex >}}, {{< katex >}}(5,32){{< /katex >}}.
(vi) Fill the table with these new vertices.
(vii) What pattern do you observe now with {{< katex >}}A_1, A_2, A_3, A_4, A_5{{< /katex >}}?

| Third vertex | Area of Triangle |
|-------------|------------------|
| {{< katex >}}(1,1){{< /katex >}} | {{< katex >}}A_1 = {{< /katex >}} |
| {{< katex >}}(2,2){{< /katex >}} | {{< katex >}}A_2 = {{< /katex >}} |
| {{< katex >}}(3,3){{< /katex >}} | {{< katex >}}A_3 = {{< /katex >}} |
| {{< katex >}}(4,4){{< /katex >}} | {{< katex >}}A_4 = {{< /katex >}} |
| {{< katex >}}(5,5){{< /katex >}} | {{< katex >}}A_5 = {{< /katex >}} |

| Third vertex | Area of Triangle |
|-------------|------------------|
| {{< katex >}}(1,2){{< /katex >}} | {{< katex >}}A_1 = {{< /katex >}} |
| {{< katex >}}(2,4){{< /katex >}} | {{< katex >}}A_2 = {{< /katex >}} |
| {{< katex >}}(3,8){{< /katex >}} | {{< katex >}}A_3 = {{< /katex >}} |
| {{< katex >}}(4,16){{< /katex >}} | {{< katex >}}A_4 = {{< /katex >}} |
| {{< katex >}}(5,32){{< /katex >}} | {{< katex >}}A_5 = {{< /katex >}} |

---

## Activity 2

Find the area of the shaded region.

---

## Exercise 5.1

1. Find the area of the triangle formed by the points
   - (i) {{< katex >}}(1,-1){{< /katex >}}, {{< katex >}}(-4,6){{< /katex >}} and {{< katex >}}(-3,-5){{< /katex >}}
   - (ii) {{< katex >}}(-10,-4){{< /katex >}}, {{< katex >}}(-8,-1){{< /katex >}} and {{< katex >}}(-3,-5){{< /katex >}}

2. Determine whether the sets of points are collinear?
   - (i) {{< katex >}}\left(-\frac{1}{2}, 3\right){{< /katex >}}, {{< katex >}}(-5,6){{< /katex >}} and {{< katex >}}(-8,8){{< /katex >}}
   - (ii) {{< katex >}}(a, b+c){{< /katex >}}, {{< katex >}}(b, c+a){{< /katex >}} and {{< katex >}}(c, a+b){{< /katex >}}

3. Vertices of given triangles are taken in order and their areas are provided aside. In each case, find the value of '{{< katex >}}p{{< /katex >}}'.

| S.No. | Vertices | Area (sq.units) |
|-------|----------|-----------------|
| (i) | {{< katex >}}(0, 0){{< /katex >}}, {{< katex >}}(p, 8){{< /katex >}}, {{< katex >}}(6, 2){{< /katex >}} | 20 |
| (ii) | {{< katex >}}(p, p){{< /katex >}}, {{< katex >}}(5, 6){{< /katex >}}, {{< katex >}}(5, -2){{< /katex >}} | 32 |

4. In each of the following, find the value of '{{< katex >}}a{{< katex >}}' for which the given points are collinear.
   - (i) {{< katex >}}(2,3){{< /katex >}}, {{< katex >}}(4,a){{< /katex >}} and {{< katex >}}(6,-3){{< /katex >}}
   - (ii) {{< katex >}}(a, 2-2a){{< /katex >}}, {{< katex >}}(-a+1, 2a){{< /katex >}} and {{< katex >}}(-4-a, 6-2a){{< /katex >}}

5. Find the area of the quadrilateral whose vertices are at
   - (i) {{< katex >}}(-9,-2){{< /katex >}}, {{< katex >}}(-8,-4){{< /katex >}}, {{< katex >}}(2,2){{< /katex >}} and {{< katex >}}(1,-3){{< /katex >}}
   - (ii) {{< katex >}}(-9,0){{< /katex >}}, {{< katex >}}(-8,6){{< /katex >}}, {{< katex >}}(-1,-2){{< /katex >}} and {{< katex >}}(-6,-3){{< /katex >}}

6. Find the value of {{< katex >}}k{{< /katex >}}, if the area of a quadrilateral is 28 sq.units, whose vertices are taken in the order {{< katex >}}(-4,-2){{< /katex >}}, {{< katex >}}(-3,k){{< /katex >}}, {{< katex >}}(3,-2){{< /katex >}} and {{< katex >}}(2,3){{< /katex >}}.

7. If the points {{< katex >}}A(-3,9){{< /katex >}}, {{< katex >}}B(a,b){{< /katex >}} and {{< katex >}}C(4,-5){{< /katex >}} are collinear and if {{< katex >}}a+b=1{{< /katex >}}, then find {{< katex >}}a{{< /katex >}} and {{< katex >}}b{{< /katex >}}.

8. Let {{< katex >}}P(11,7){{< /katex >}}, {{< katex >}}Q(13.5, 4){{< /katex >}} and {{< katex >}}R(9.5, 4){{< /katex >}} be the midpoints of the sides {{< katex >}}AB{{< /katex >}}, {{< katex >}}BC{{< /katex >}} and {{< katex >}}AC{{< /katex >}} respectively of {{< katex >}}\triangle ABC{{< /katex >}}. Find the coordinates of the vertices {{< katex >}}A, B{{</ katex >}} and {{< katex >}}C{{< /katex >}}. Hence find the area of {{< katex >}}\triangle ABC{{< /katex >}} and compare this with area of {{< katex >}}\triangle PQR{{< /katex >}}.

9. In the figure, the quadrilateral swimming pool shown is surrounded by concrete patio. Find the area of the patio.

10. A triangular shaped glass with vertices at {{< katex >}}A(-5,-4){{< /katex >}}, {{< katex >}}B(1,6){{< /katex >}} and {{< katex >}}C(7,-4){{< /katex >}} has to be painted. If one bucket of paint covers 6 square feet, how many buckets of paint will be required to paint the whole glass, if only one coat of paint is applied.

11. In the figure, find the area of (i) triangle {{< katex >}}AGF{{< /katex >}} (ii) triangle {{< katex >}}FED{{< /katex >}} (iii) quadrilateral {{< katex >}}BCEG{{< /katex >}}.

---