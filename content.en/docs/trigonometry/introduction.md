---
title: 'Introduction'
weight: 1
---

# Chapter 6

## TRIGONOMETRY

"The deep study of nature is the most fruitful source of mathematical discoveries" - Joseph Fourier.

French mathematician Francois Viete used trigonometry in the study of Algebra for solving certain equations by making suitable trigonometric substitutions. His famous formula for \( \pi \) can be derived with repeated use of trigonometric ratios. One of his famous works titled Canon Mathematics covers trigonometry; it contains trigonometric tables, it also gives the mathematics behind the construction of the tables, and it details how to solve both plane and spherical triangles. He also provided the means for extracting roots and solutions of equations of degree atmost six. Viete introduced the term "coefficient" in mathematics.

<center>Francois Viete (1540 - 1603)</center>

He provided a simple formula relating the roots of a equation with its coefficients. He also provided geometric methods to solve doubling the cube and trisecting the angle problems. He was also involved in deciphering codes.

### Learning Outcomes

To recall trigonometric ratios. To recall fundamental relations between the trigonometric ratios of an angle. To recall trigonometric ratios of complementary angles. To understand trigonometric identities. To know methods of solving problems concerning heights and distances of various objects.

### 6.1 Introduction

From very ancient times surveyors, navigators and astronomers have made use of triangles to determine distances that could not be measured directly. This gave birth to the branch of mathematics what we call today as "Trigonometry".

Hipparchus of Rhodes around 200 BC(BCE), constructed a table of chord lengths for a circle of circumference \( 360 \times 60 = 21600 \) units which corresponds to one unit of circumference for each minute of arc. For this achievement, Hipparchus is considered as "The Father of Trigonometry" since it became the basis for further development.

Indian scholars of the 5th century AD(CE), realized that working with half-chords for half-angles greatly simplified the theory of chords and its application to astronomy. Mathematicians like Aryabhata, the two Bhaskaras and several others developed astonishingly sophisticated techniques for calculating half-chord (Jya) values.

Mathematician Abu Al-Wafa of Baghdad believed to have invented the tangent function, which he called the "Shadow". Arabic scholars did not know how to translate the word Jya, into their texts and simply wrote jiba as a close approximate word.

Misinterpreting the Arabic word 'jiba' for 'cove' or 'bay', translators wrote the Arabic word 'jiba' as 'sinus' in Latin to represent the half-chord. From this, we have the name 'sine' used to this day. The word "Trigonometry" itself was invented by German mathematician Bartholomaeus Piticus in the beginning of 17th century AD(CE).

### Recall

#### Trigonometric Ratios

Let \( 0^\circ < \theta < 90^\circ \)

<center>Fig.6.1</center>

Let us take right triangle OMP

\[
\sin \theta = \frac{\text{Opposite side}}{\text{Hypotenuse}} = \frac{MP}{OP}
\]

\[
\cos \theta = \frac{\text{Adjacent side}}{\text{Hypotenuse}} = \frac{OM}{OP}
\]

From the above two ratios we can obtain other four trigonometric ratios as follows.

\[
\tan \theta = \frac{\sin \theta}{\cos \theta} = \frac{MP}{OM}
\]

\[
\csc \theta = \frac{1}{\sin \theta} = \frac{OP}{MP}
\]

\[
\sec \theta = \frac{1}{\cos \theta} = \frac{OP}{OM}
\]

\[
\cot \theta = \frac{1}{\tan \theta} = \frac{OM}{MP}
\]

#### Trigonometric ratios of complementary angle

| | |
|---|---|
| \( \sin(90^\circ - \theta) = \cos \theta \) | \( \cos(90^\circ - \theta) = \sin \theta \) |
| \( \tan(90^\circ - \theta) = \cot \theta \) | \( \csc(90^\circ - \theta) = \sec \theta \) |
| \( \sec(90^\circ - \theta) = \csc \theta \) | \( \cot(90^\circ - \theta) = \tan \theta \) |

#### Visual proof of trigonometric complementary angle

Consider a semicircle of radius 1 as shown in the figure.

Let \( \angle QOP = \theta \)

Then \( \angle QOR = 90^\circ - \theta \), so that \( OPQR \) forms a rectangle.

<center>Fig. 6.2</center>

From triangle \( OPQ \),

\[
\frac{OP}{OQ} = \cos \theta
\]

But \( OQ = \) radius \( = 1 \)

\[
\therefore OP = OQ \cos \theta = \cos \theta
\]

Similarly,

\[
\frac{PQ}{OQ} = \sin \theta \Rightarrow PQ = OQ \sin \theta = \sin \theta \quad (\because OQ = 1)
\]

\[
OP = \cos \theta, \quad PQ = \sin \theta \tag{1}
\]

Now, from triangle \( QOR \)

\[
\frac{OR}{OQ} = \cos(90^\circ - \theta)
\]

\[
\therefore OR = OQ \cos(90^\circ - \theta)
\]

\[
OR = \cos(90^\circ - \theta)
\]

Similarly,

\[
\frac{RQ}{OQ} = \sin(90^\circ - \theta)
\]

Then,

\[
RQ = \sin(90^\circ - \theta)
\]

\[
OR = \cos(90^\circ - \theta), \quad RQ = \sin(90^\circ - \theta) \tag{2}
\]

\( \because OPQR \) is a rectangle,

\( OP = RQ \) and \( OR = PQ \)

Therefore, from (1) and (2) we get,

\[
\sin(90^\circ - \theta) = \cos \theta
\]

and

\[
\cos(90^\circ - \theta) = \sin \theta
\]

#### Note

| | |
|---|---|
| \( (\sin \theta)^2 = \sin^2 \theta \) | \( (\cos \theta)^2 = \cos^2 \theta \) |
| \( (\sec \theta)^2 = \sec^2 \theta \) | \( (\tan \theta)^2 = \tan^2 \theta \) |
| \( (\csc \theta)^2 = \csc^2 \theta \) | \( (\cot \theta)^2 = \cot^2 \theta \) |

#### Table of Trigonometric Ratios for \( 0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ \)

| \( \theta \) | \( 0^\circ \) | \( 30^\circ \) | \( 45^\circ \) | \( 60^\circ \) | \( 90^\circ \) |
|---|---|---|---|---|---|
| \( \sin \theta \) | 0 | \( \frac{1}{2} \) | \( \frac{1}{\sqrt{2}} \) | \( \frac{\sqrt{3}}{2} \) | 1 |
| \( \cos \theta \) | 1 | \( \frac{\sqrt{3}}{2} \) | \( \frac{1}{\sqrt{2}} \) | \( \frac{1}{2} \) | 0 |
| \( \tan \theta \) | 0 | \( \frac{1}{\sqrt{3}} \) | 1 | \( \sqrt{3} \) | undefined |
| \( \csc \theta \) | undefined | 2 | \( \sqrt{2} \) | \( \frac{2}{\sqrt{3}} \) | 1 |
| \( \sec \theta \) | 1 | \( \frac{2}{\sqrt{3}} \) | \( \sqrt{2} \) | 2 | undefined |
| \( \cot \theta \) | undefined | \( \sqrt{3} \) | 1 | \( \frac{1}{\sqrt{3}} \) | 0 |

#### Thinking Corner

1. When will the values of \( \sin \theta \) and \( \cos \theta \) be equal?

2. For what values of \( \theta \), \( \sin \theta = 2 \)?

3. Among the six trigonometric quantities, as the value of angle \( \theta \) increase from \( 0^\circ \) to \( 90^\circ \), which of the six trigonometric quantities has undefined values?

4. Is it possible to have eight trigonometric ratios?

5. Let \( 0^\circ \leq \theta \leq 90^\circ \). For what values of \( \theta \) does

(i) \( \sin \theta > \cos \theta \)

(ii) \( \cos \theta > \sin \theta \)

(iii) \( \sec \theta = 2 \tan \theta \)

(iv) \( \csc \theta = 2 \cot \theta \)