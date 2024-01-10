---
title: 'JulySimultaneous Linear Equations in Three Variables '
weight: 1
---
{{< katex display >}}{{< /katex >}}

# Simultaneous Linear Equations in Two Variables

Let us recall solving a pair of linear equations in two variables

**Definition**
**Linear Equation in two variables**
Any first degree equation containing two variables x and y is called a linear equation in two variables. The general form of linear equation in two variables x and y is ax+by+c = 0, where atleast one of a, b is non-zero and a, b, c are real numbers. 
Note that linear equations are first degree equations in the given variables

 **NOTE** 
1. xy – 7 = 3 is not a linear equation in two variables since the term xy is of degree 2.
2. A linear equation in two variables represent a straight line in xy plane.


**Example 3.1** The father’s age is six times his son’s age. Six years hence the age of father 
will be four times his son’s age. Find the present ages (in years) of the son and father. 
**Solution** Let the present age of father be x years and 
the present age of son be y years

Given, x = 6y        …(1)
x + 6 = 4(y + 6)      … (2)  
Substituting (1) in (2), 6y + 6 = 4 (y + 6)
6y + 6 = 4y + 24 => y = 9
Therefore, son’s age = 9 years and father’s age = 54 years.

**Example 3.2**	 Solve 2x − 3y = 6 , x + y = 1
**Solution**	2x − 3y = 6  … (1)  

![figure](fig3-1.png)
 x + y = 1	… (2)
     (1)×1 => 2x-3y = 6 
     (2)×2 => 2x+2y = 2  
     ----------------------------
   -5y = 4 =>  y =  x = $\frac{-4}{5}$

Substituting y =$\frac{-4}{5}$ in (2), x −$\frac{4}{5}$=1 we get, x=$\frac{9}{5}$
Therefore, x=$\frac{9}{5}$, y =$\frac{-4}{5}$. 

## Simultaneous Linear Equations in Three Variables
![Figure with 50%](fig3-2.png "w-50 float-end")

 Right from the primitive needs of calculating amount spent for various items in a super market, finding ages of people under specific conditions, finding path of an object when it is thrown upwards at an angle, Algebra plays a vital role in our daily life.

Any point in the space can be determined uniquely by knowing its   latitude,   longitude   and   altitude.   Hence to locate the position of an object at a particular place situated on the Earth, three satellites are positioned to arrive   three   equations.   Among   these   three   equations, we get two linear equations and one quadratic (second degree) equation. Hence we can solve for the variables latitude, longitude and altitude to uniquely fix the position of any object at a given point of time. This is the basis of Global Positioning System (GPS). Hence the concept of linear equations in three variables is used in GPS systems.


### System of Linear Equations in Three Variables
In earlier classes, we have learnt different methods of solving Simultaneous Linear Equations in two variables. Here we shall learn to solve the system of linear equations in three variables namely, x, y and z. The general form of a linear equation in three variablesx, y and z is ax + + by cz + =d 0 where a, b, c, d are real numbers, and atleast one of a, b, c is non-zero.

**NOTE**
![figure3.4](fig3-3.png)

**General Form:** A system of linear equations in three variables x, y, z has the general form
$a_{1}x + b_{1}y + c_{1}z + d_{1}  = 0$
$a_{2}x + b_{2}y + c_{2}z + d_{2} = 0$
$a_{3}x + b_{3}y + c_{3}z + d_{3} = 0$
Each equation in the system represents a plane in three dimensional space and solution of the system of equations is precisely the point of intersection of the three planes defined by the three linear equations of the system. The system may have only one solution, infinitely many solutions or no solution depending on how the planes intersect one another

The figures presented below illustrate each of these possibilities
![figure3.4](fig3-4.png)


**Procedure for solving system of linear equations in three variables**

**Step 1:** By taking any two equations from the given three, first multiply by some suitable non-zero constant to make the co-efficient of one variable (either x or y or z) numerically equal.
**Step 2:** Eliminate one of the variables whose co-efficients are numerically equal from the equations.
**Step 3:** Eliminate the same variable from another pair.
**Step 4:** Now we have two equations in two variables.
**Step 5:** Solve them using any method studied in earlier classes.
**Step 6:** The remaining variable is then found by substituting in any one of the given equations.

**NOTE** 
1. If you obtain a false equation such as 0=1, in any of the steps then the system has no
solution.
2. If you do not obtain a false solution, but obtain an identity, such as 0=0 then the system
has infinitely many solutions.


**Example 3.3**
 Solve the following system of linear equations in three variables
3x – 2y + z =2 , 2x + 3y – z = 5 , x + y + z = 6 .
**Solution** 3x − 2y + z = 2   ...(1)	
2x + 3y – z = 5 ...(2)	 
x + y + z = 6 ...(3)
![soln3.3](soln3.3.png)

Substituting x = 1 in (4), 5 + y = 7=> y = 2
Substituting x = 1 , y = 2 in (3), 1 + 2 + z = 6 we get, z = 3
Therefore,  x = 1, y = 2 ,  z = 3

**Example 3.4**
     In an interschool atheletic meet, with total of 24 individual prices, securing a total of 56 points, a first place secures 5 points, a second place secures 3 points, and a third place secures 1 point. Having as many third place finishers as first and second place finishers, find how many athletes finished in each place.
**Solution** Let the number of I, II and III place finishers be x , y and z respectively.
Total number of events = 24; Total number of points = 56. Hence, the linear equations in three variables are
 
x + y + z = 24 …(1)	5x + 3y + z = 56 …(2)	x + y = z …(3)
 
Substituting (3) in (1) we get, z + z = 24 => z = 12
 (3) will be, x + y = 12

     (2)   =>	5x + 3y=44
                                (-)
     3x(3) =>       3x + 3y=36
    ---------------------------
 	                2x     = 8	we get, x = 4 
        
Substituting x = 4 , z = 12 in (3) we get, y = 12 − 4 = 8 
Therefore, Number of first place finishers is 4
Number of second place finishers is 8 
Number of third place finishers is 12.

**Example 3.5** Solve x + 2y – z = 5 ; x − y + z = −2 ; −5x − 4y + z = −11
**Solution**	x + 2y – z =5 ...(1) 	x – y + z =–2 ...(2)   –5x –4y + z = –11 ...(3)
    

     Adding(1)and(2) we get, x + 2y – z = 5
                                           (+)
                             x – y + z = –2 
                        -----------------------
                            2x + y	   = 3               …(4) 
                        -----------------------
    Subtracting (2) and (3),  x −  y + z = –2
                                               (−)
                            −5x − 4y + z = –11 
                        -----------------------
                             6x + 3y      =  9
                        -----------------------
    Dividing by 3            2x+y = 3                     …(5)
    Subtracting (4) and (5), 2x+y = 3
                             2x+y = 3
                        ----------------------
                                0 = 0
                        ----------------------
Here we arrive at an identity 0=0.
Hence the system has an infinite number of solutions.

**Example 3.6** 	Solve 3x + y – 3z = 1 ; –2x – y + 2z = 1 ; –x – y + z = 2 .
**Solution**	3x + y − 3z = 1	… (1)	–2x – y + 2z = 1 …(2)	−x − y + z = 2 …(3)

    Adding (1) and (2),      3x + y − 3z = 1  
                                            (+)
                            −2x − y + 2z = 1	
                            --------------------
                              x –      z  = 2	         ...(4)
                            --------------------
    Adding (1) and (3),      3x + y − 3z = 1
                                            (+)
                             −x − y +  z = 2
                            --------------------
                             2x   -   2z = 3
                             --------------------            ...(5)
                             2x   -   2z = 3
                                            (-)    
    Now,(5)−2×(4) we get,    2x   -   2z = 4
                             --------------------
                                       0 = -1
                             --------------------  
Here we arrive at a contradiction as 0 ≠ –1.
This means that the system is inconsistent and has no solution.

**Example 3.7** Solve $\frac{x}{2}-1=\frac{y}{6}+1=\frac{z}{7}+2;\frac{y}{3}+\frac{z}{2}$=13

**Solution** Considering, $\frac{x}{2}-1=\frac{y}{6}+1$

$\frac{x}{2}-\frac{y}{6}=1+1$ => $\frac{6x-2y}{12}=2$ we get, 3x-y=12  ...(1)

Considering, $\frac{x}{2}-1=\frac{z}{7}+2$
$\frac{x}{2}-\frac{z}{7}=1+2$ => $\frac{7x-2x}{14}=3$ we get, 7x − 2z = 42	… (2)

Also, from $\frac{y}{3}+\frac{z}{2}$=13 => $\frac{2y+3z}{6}$=13 we get, 2y + 3z = 78 … (3)

Eliminating z from (2) and (3)
![header](Example3-7.png)

Substituting x= 10 in (1), 30 12 − =y we get, y = 18
Substituting x = 10 in (2), 70 − = 2 4 z 2 then, z = 14
∴ x = 10 , y = 18 , z = 14 .



     







        

</blockquote>

