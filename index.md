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

<img src="./images/Calculator_ln_2.png" width=30% title="Pictured:  The natural log of 2 to 32 digits on the built-in Microsoft calculator">

*Pictured:  The natural log of 2 to (an arbitrary) 32 digits on the built-in Microsoft calculator.*

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

While these equations of polynomials contain a *finite* number of terms, we can have polynomials 
with an *infinite* number of terms.  These are called **series**, and one of the simplest types of 
series is called a **geometric series**.  A geometric series contains an initial term, usually 
denoted by the variable $a$, and each successive term is multiplied by a ratio, usually denoted by 
the variable $r$.  The basic formula is 

$$\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ... + ar^n + ...$$

If we set this series equal to $s$, we can do some rearranging to find a function that 
this series is equivalent to:

$$s = a + ar + ar^2 + ... + ar^n + ...$$

By pulling an $r$ out of all the terms after the first one, we get

$$s = a + r(a + ar + ar^2 + ... + ar^{n-1} + ...)$$

Despite the fact that $ar^n$ becomes $ar^{n-1}$, we have an infinite number of terms, 
so if we were to expand out the terms in the parentheses, we get the same series as $s$ 
in the first line; therefore, we can substitute the terms in the parentheses with $s$!

$$s = a + rs$$

Move $rs$ to the left side of the equation:

$$s - rs = a,$$

combine like-terms:

$$s(1 - r) = a,$$

and solve for $s$:

$$s = \frac{a}{1 - r}.$$

We can now set both $s$ expressions equal to each other:

$$\frac{a}{1 - r} = \sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ... + ar^n + ...$$

There is one caveat to this equality:  it is only true if the sum *converges* to a 
value, which happens when each term gets successively smaller; if the terms blow 
up to infinity as they increase in degree, the series *diverges*.

The geometric series we are interested in regarding the logarithm is the one where $a = 1$ 
and $r = -x$:

$$\frac{1}{1-(-x)} = 1 + (-x) + (-x)^2 + (-x)^3 + ... + (-x)^n + ...$$

$$\frac{1}{1+x} = 1 - x + x^2 - x^3 + x^4 + ... + (-x)^n + ...$$

This series converges when $|x| < 1$.  Now, you might think that some of the algebraic 
manipulation we did earlier was invalid, but we can check our work.  Below, I have a Desmos 
graph with both the function $\frac{1}{1+x}$ and the infinite series.  By moving the slider for $N$, 
you can add successive terms to the series and see that, as more and more terms are added, 
the series graph becomes a better and better approximation to the function graph for $|x| < 1$.

[Desmos: Geometric Series](https://www.desmos.com/calculator/7hczeiyf4b)

## Getting a series for the natural logarithm

"This is all very interesting, but what does this have to do with computing logarithms?"

It turns out that the function $\frac{1}{1+x}$ and the natural logarithm are directly related. 
Specifically, the area under the curve $\frac{1}{1+t}$ from 0 to any value $x$ is the 
natural logarithm of $1+x$.  In mathematical symbols, this is rendered as

$$\int_{0}^{x} \frac{1}{1+t} dt = \ln{(1+x)}$$


