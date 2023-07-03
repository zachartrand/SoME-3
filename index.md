<!---
Summer of Math Exposition 3
How does a computer/calculator compute natural logarithms?

Author:  Zach Chartrand
Created on 2 July 2023
-->

# How does a computer/calculator compute logarithms?

## The curious student's frustration
There are many functions on a scientific or graphing calculator that we are 
introduced to as high school students that, we are told, just work.  You select 
the function, put in the value that you need to calculate, hit "=" or "ENTER", 
and SHABAM!  You have the correct answer to some arbitrary number of digits that
you are ensured are all 100% accurate.

<img src="" title="Pictured:  The natural log of 2 to 32 digits on the built-in Microsoft calculator">

*Pictured:  The natural log of 2 to an arbitrary 32 digits on the built-in Microsoft calculator*

This is wonderful!  Necessary, even, for if our calculators and computers calculated 
logarithms inaccurately, as well as exponentials, trig functions, and square roots, 
to name but a few, a lot of scientific and engineering work would be broken and 
end in catastrophe.  But how do we know that the value on the calculator is, in fact, 
accurate?  How did the calculator crunch the input number and give us the output?  
I remember this question being asked in high school, and the answer being no more than
a handwave.  To be fair to Algebra II teachers (which is where I was first introduced 
to logarithms, if memory serves), the answer is beyond the scope of algebra, and lies in 
calculus.  But it is an answer worth knowing, and it's an answer that is very 
knowable, even if you don't have a background in calculus.  Calculus is the method 
for deriving the formula used in calculators and computers, but the formula itself 
is a pretty simple polynomial.

## The Geometric Series
Most of us were introduced to polynomial equations in algebra.  For a quick refresher, a 
polynomial is an expression involving at least one variable (usually $x$) and addition, 
subtraction, multiplication, division, and integer power operators.  Here are a few examples:

[Line](https://www.desmos.com/calculator/o0i7zoysc2):  <br> $y = 5 + 2x$

[Parabola](https://www.desmos.com/calculator/zdjd1sn77k):  <br> $y = 1 - x - x^{2}$

[Quartic](https://www.desmos.com/calculator/3jjshmktba):  <br> $y = 4 - 2x - 5x^{2} + \frac{1}{2}x^{3} + x^{4}$

*Note:  The links lead to Desmos graphs where you can change the parameters to see how it changes the graph.*


