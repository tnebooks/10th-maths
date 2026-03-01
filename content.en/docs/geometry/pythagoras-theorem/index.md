---
title: 'Pythagoras Theorem '
weight: 3
---

# 4.4 Pythagoras Theorem

Among all existing theorems in mathematics, Pythagoras theorem is considered to be the most important because it has maximum number of proofs. There are more than 350 ways of proving Pythagoras theorem through different methods. Each of these proofs was discovered by eminent mathematicians, scholars, engineers and math enthusiasts, including one by the 20th American president James Garfield. The book titled "The Pythagorean Proposition" written by Elisha Scott Loomis, published by the National Council of Teaching of Mathematics (NCTM) in America contains 367 proofs of Pythagoras Theorem.

Three natural numbers {{< katex >}}  (a, b, c)
{{< /katex >}} 
are said to form **Pythagorean Triplet**, if they form sides of a right triangle. Thus {{< katex >}}  (a, b, c)
{{< /katex >}} 
is a Pythagorean Triplet if and only if {{< katex >}}  c^2 = a^2 + b^2
{{< /katex >}}.

Now we are in a position to study this most famous and important theorem not only in Geometry but in whole of mathematics.

![](activity1.png)
![](ativity2.png)

**Note:**
- In a right angled triangle, the side opposite to {{< katex >}}  90°
{{< /katex >}} (the right angle) is called the **hypotenuse**.
- The other two sides are called **legs** of the right angled triangle.
- The hypotenuse will be the longest side of the triangle.

---

## Theorem 5: Pythagoras Theorem

**Statement:** In a right angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.

![](4.46.png)

**Proof:**

**Given:** In {{< katex >}}  \triangle ABC
{{< /katex >}},
 {{< katex >}}  \angle A = 90°
{{< /katex >}}

**To prove:** {{< katex >}}  AB^2 + AC^2 = BC^2
{{< /katex >}}

**Construction:** Draw {{< katex >}}  AD \perp BC
{{< /katex >}}

| No. | Statement | Reason |
|:---|:---|:---|
| 1. | Compare {{< katex >}}  \triangle ABC{{< /katex >}} and {{< katex >}}  \triangle DBA{{< /katex >}} | |
| | {{< katex >}}  \angle B{{< /katex >}} is common | |
| | {{< katex >}}  \angle BAC = \angle BDA = 90°{{< /katex >}} | Given {{< katex >}}  \angle BAC = 90°{{< /katex >}}  and by construction {{< katex >}}  \angle BDA = 90°{{< /katex >}} |
| | Therefore, {{< katex >}}  \triangle ABC \sim \triangle DBA{{< /katex >}} | By AA similarity |
| | {{< katex >}}  \frac{AB}{BD} = \frac{BC}{AB}{{< /katex >}} | |
| | {{< katex >}}  AB^2 = BC \times BD{{< /katex >}} ... (1) | |
| 2. | Compare {{< katex >}}  \triangle ABC{{< /katex >}} and {{< katex >}}  \triangle DAC{{< /katex >}} | |
| | {{< katex >}}  \angle C{{< /katex >}} is common | |
| | {{< katex >}}  \angle BAC = \angle ADC = 90°{{< /katex >}} | Given {{< katex >}}  \angle BAC = 90°{{< /katex >}}  and by construction {{< katex >}}  \angle ADC = 90°{{< /katex >}} |
| | Therefore, {{< katex >}}  \triangle ABC \sim \triangle DAC{{< /katex >}} | By AA similarity |
| | {{< katex >}}  \frac{BC}{AC} = \frac{AC}{DC}{{< /katex >}} | |
| | {{< katex >}}  AC^2 = BC \times DC{{< /katex >}} ... (2) | |

Adding (1) and (2) we get:

{{< katex >}}  AB^2 + AC^2 = BC \times BD + BC \times DC
{{< /katex >}}
{{< katex >}}  = BC(BD + DC)
{{< /katex >}}
{{< katex >}}  = BC \times BC
{{< /katex >}}
{{< katex >}}  AB^2 + AC^2 = BC^2
{{< /katex >}}

Hence the theorem is proved.

![](dyk.png)
---

## Converse of Pythagoras Theorem

**Statement:** If the square of the longest side of a triangle is equal to sums of squares of other two sides, then the triangle is a right angle triangle.

---

## Examples

### Example 4.20

An insect 8m away initially from the foot of a lamp post which is 6m tall, crawls towards it moving through a distance. If its distance from the top of the lamp post is equal to the distance it has moved, how far is the insect away from the foot of the lamp post?


![](4.47.png)
**Solution:** Distance between the insect and the foot of the lamp post {{< katex >}}  BD = 8
{{< /katex >}} m

The height of the lamp post, {{< katex >}}  AB = 6
{{< /katex >}} m

After moving a distance of {{< katex >}}  x
{{< /katex >}} 
m, let the insect be at {{< katex >}}  C
{{< /katex >}}.

Let, {{< katex >}}  AC = CD = x
{{< /katex >}}.
 Then {{< katex >}}  BC = BD - CD = 8 - x
{{< /katex >}}

In {{< katex >}}  \triangle ABC
{{< /katex >}},
 {{< katex >}}  \angle B = 90°
{{< /katex >}}

{{< katex >}}  AC^2 = AB^2 + BC^2 \text{ gives } x^2 = 6^2 + (8-x)^2
{{< /katex >}}
{{< katex >}}  x^2 = 36 + 64 - 16x + x^2
{{< /katex >}}
{{< katex >}}  16x = 100 \text{ then } x = 6.25
{{< /katex >}}

Then, {{< katex >}}  BC = 8 - x = 8 - 6.25 = 1.75
{{< /katex >}} m

Therefore the insect is **1.75 m** away from the foot of the lamp post.

---

### Example 4.21

{{< katex >}}  P
{{< /katex >}} 
and {{< katex >}}  Q
{{< /katex >}} 
are the mid-points of the sides {{< katex >}}  CA
{{< /katex >}} 
and {{< katex >}}  CB
{{< /katex >}}
 respectively of a {{< katex >}}  \triangle ABC
{{< /katex >}},
 right angled at {{< katex >}}  C
{{< /katex >}}.
  Prove that {{< katex >}}  4(AQ^2 + BP^2) = 5AB^2
{{< /katex >}}.

![](4.48.png)

**Solution:** {{< katex >}}  \triangle AQC
{{< /katex >}} 
is a right triangle at {{< katex >}}  C
{{< /katex >}},

{{< katex >}}  AQ^2 = AC^2 + QC^2 \text{ ... (1)}
{{< /katex >}}

{{< katex >}}  \triangle BPC
{{< /katex >}} 
is a right triangle at {{< katex >}}  C
{{< /katex >}},

{{< katex >}}  BP^2 = BC^2 + CP^2 \text{ ... (2)}
{{< /katex >}}

{{< katex >}}  \triangle ABC
{{< /katex >}} 
is a right triangle at {{< katex >}}  C
{{< /katex >}},

{{< katex >}}  AB^2 = AC^2 + BC^2 \text{ ... (3)}
{{< /katex >}}

From (1) and (2),

{{< katex>}}  AQ^2 + BP^2 = AC^2 + QC^2 + BC^2 + CP^2{{< /katex >}}
    
 {{< katex >}}  4(AQ^2 + BP^2) = 4(AC^2 + QC^2 + BC^2 + CP^2){{< /katex >}}
    \
 {{< katex >}}  = 4AC^2 + 4QC^2 + 4BC^2 + 4CP^2{{< /katex >}}
    \
{{< katex >}}  = 4AC^2 + BC^2 + 4BC^2 + AC^2 \text{ (Since } P \text{ and } Q \text{ are mid points)}{{< /katex >}}
\
{{< katex >}}  = 5AC^2 + 5BC^2 = 5(AC^2 + BC^2){{< /katex >}}

{{< katex >}}  = 5AB^2 \text{ (From equation (3))}{{< /katex >}}
\
{{< katex >}}  \therefore 4(AQ^2 + BP^2) = 5AB^2{{< /katex >}}

---

### Example 4.22

What length of ladder is needed to reach a height of 7ft along the wall when the base of the ladder is 4ft from the wall? Round off your answer to the next tenth place.

![](4.49.png)

**Solution:** Let {{< katex >}}  x
{{< /katex >}}
 be the length of the ladder. {{< katex >}}  BC = 4
{{< /katex >}} 
 ft, {{< katex >}}  AC = 7
{{< /katex >}} ft.

By Pythagoras theorem we have:

{{< katex >}}  AB^2 = AC^2 + BC^2
{{< /katex >}}
{{< katex >}}  x^2 = 7^2 + 4^2 = 49 + 16 = 65
{{< /katex >}}

Hence, {{< katex >}}  x = \sqrt{65}
{{< /katex >}}

The number 65 is between 8 and 8.1.
{{< katex display=true >}}
8^2 = 64 < 65 < 65.61 = (8.1)^2
{{< /katex >}}

Therefore, the length of the ladder is approximately **8.1 ft**.

---

### Example 4.23

An Aeroplane after take off from an airport and flies due north at a speed of 1000 km/hr. At the same time, another aeroplane take off from the same airport and flies due west at a speed of 1200 km/hr. How far apart will be the two planes after {{< katex >}}  1\frac{1}{2}
{{< /katex >}} hours?

![](4.50.png)

**Solution:** Let the first aeroplane starts from {{< katex >}}  O
{{< /katex >}} 
and goes up to {{< katex >}}  A
{{< /katex >}} towards north,

{{< katex >}}  OA = 1000 \times \frac{3}{2} = 1500 \text{ km}
{{< /katex >}}

Let the second aeroplane starts from {{< katex >}}  O
{{< /katex >}} 
at the same time and goes up to {{< katex >}}  B
{{< /katex >}} towards west,

{{< katex >}}  OB = 1200 \times \frac{3}{2} = 1800 \text{ km}
{{< /katex >}}

The required distance to be found is {{< katex >}}  BA
{{< /katex >}}.

In right angled triangle {{< katex >}}  AOB
{{< /katex >}},

{{< katex >}}  AB^2 = OA^2 + OB^2
{{< /katex >}}
\
{{< katex >}}  = 1500^2 + 1800^2
{{< /katex >}}
\
{{< katex >}}  = 100^2(15^2 + 18^2)
{{< /katex >}}
\
{{< katex >}}  = 100^2 \times 549 = 100^2 \times 9 \times 61
{{< /katex >}}
\
{{< katex >}}  AB = 100 \times 3 \times \sqrt{61} = 300\sqrt{61} \text{ km}
{{< /katex >}}

## Exercise 4.3

1. A man goes 18m due east and then 24m due north. Find the distance of his current position from the starting point?

2. There are two paths that one can choose to go from Sarah's house to James house. One way is to take C street, and the other way requires to take B street and then A street. How much shorter is the direct path along C street? (Using figure).

![](1.png)


3. To get from point A to point B you must avoid walking through a pond. You must walk 34m south and 41m east. To the nearest meter, how many meters would be saved if it were possible to make a way through the pond?

4. In the rectangle WXYZ, XY + YZ = 17cm, and XZ + YW = 26cm. Calculate the length and breadth of the rectangle?

![](2.png)


5. The hypotenuse of a right triangle is 6m more than twice of the shortest side. If the third side is 2m less than the hypotenuse, find the sides of the triangle.

6. 5m long ladder is placed leaning towards a vertical wall such that it reaches the wall at a point 4m high. If the foot of the ladder is moved 1.6m towards the wall, then find the distance by which the top of the ladder would slide upwards on the wall.

7. The perpendicular PS on the base QR of a ΔPQR intersects QR at S, such that QS = 3SR. Prove that 2PQ² + 2PR² = 5QR².

8. In the adjacent figure, ABC is a right angled triangle with right angle at B and points D, E trisect BC. Prove that 8AE² = 3AC² + 5AD².

![](3.png)


---