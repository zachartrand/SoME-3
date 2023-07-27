<!---
Summer of Math Exposition 3
How does a computer/calculator compute logarithms?

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

<img src="./images/Calculator_ln_2.png" width=30%
  title="Pictured:  The natural log of 2 to 32 digits on the built-in Microsoft calculator">

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
the variable $r$.  Here are a couple of examples:

$$ \sum_{n=1}^{\infty} \frac{1}{2^n} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$

$$ \sum_{n=0}^{\infty} 2 \cdot (-3)^n = 2 - 6 + 18 - 54 + ... $$

In the first series, the initial value is $\frac{1}{2}$, and each term after it is the
previous term multiplied by $\frac{1}{2}$.  The second series begins with the number 2,
and each term after it is the previous term multiplied by 3.  Because the first series'
terms get smaller in absolute value for each successive term, the sum approaches, or
**converges**, to a value.  The second series' terms get larger in absolute value
with each successive term, so the series **diverges** without resolving to a defined value.

The general formula for a geometric series is

$$\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ... + ar^n + ...$$

If we set this formula equal to $s$, we can do some rearranging to find a function that
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

Note that this assumes the series converges.  This formula does not hold if the
series diverges.

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

While the understanding of the calculus involved is beyond the scope of this article,
I made a [Desmos graph](https://www.desmos.com/calculator/czktma6spu) where you can play
with values of $x$ ($a$ in the graph) and see the area under the curve, with its exact
value shown and a 1x1 square area as a comparison.

Taking integrals is an inverse problem, and for most functions, is very difficult, if not impossible.
However, for polynomials, it's actually very easy.  For a given polynomial term, increase the degree
by one, divide the term by the new degree, and take the difference of the function evaluated at the two
integrand values (the values at the top and bottom of the $\int$ ).

We'll start by setting the natural logarithm equal to the integral of our geometric series:

$$\ln{(1+x)} = \int_{0}^{x} \frac{1}{1+t} dt = \int_{0}^{x} (1 - t + t^2 - t^3 + t^4 + ... + (-t)^n + ...) dt$$

The integral of a sum is the sum of the integrals of each term, so we can take this one term at a time.
Starting with the first term,

$$ \int_{0}^{x} 1 dt = \int_{0}^{x} 1t^0 dt = \frac{t^{0+1}}{0+1} \Big|_0^x = \frac{t^1}{1} \Big|_0^x = t \Big|_0^x = x - 0 = x$$

Let me explain the symbols above.  We start with taking the integral of 1, a constant, in terms of $t$
(which is a dummy variable to distinguish it from $x$ in the answer).  A constant can be represented as
a zero-degree polynomial term, so we can represent 1 as 1 times $t^0$.  We add one to the degree, so 0
becomes 1, then we divide by the new degree, which is 1 in this case.  Our result is $t$.  We then need to
evaluate this term at $t = x$ and $t = 0$ and subtract them (this is what the vertical bar represents).
The result is $x - 0$, which reduces to $x$.  So the first term of our infinite series for
$\ln{(1+x)}$ is $x$!  Let's do the second term:

$$ \int_{0}^{x} -t dt = \int_{0}^{x} -t^1 dt = -\frac{t^{1+1}}{1+1} \Big|_0^x = -\frac{t^2}{2} \Big|_0^x = -\frac{x^2}{2} - \biggl(-\frac{0^2}{2} \biggr) = -\frac{x^2}{2} - 0 = -\frac{x^2}{2}$$

Our second term is $-\frac{x^2}{2}$.  You may start to see the overall pattern, but we'll do one more:

$$ \int_{0}^{x} t^2 dt = \frac{t^{2+1}}{2+1} \Big|_0^x = \frac{t^3}{3} \Big|_0^x = \frac{x^3}{3} - \frac{0^3}{3} = \frac{x^3}{3} $$

With this, the pattern starts to come into focus.  We have a series where each term is a polynomial
divided by its degree, where all of the odd degree polynomial terms are positive and all the even
terms are negative.  Written as a series,

$$ \ln{(1+x)} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{n+1}}{n+1} $$

In fact, if we were to integrate the general term of the geometric series, this is exactly what we get:

$$ \int_0^x \frac{1}{1+t} dt = \int_0^x \sum_{n=0}^{\infty} (-t)^n dt $$

$$ = \sum_{n=0}^\infty \biggl( \int_0^x (-t)^n dt \biggr) $$

$$ = \sum_{n=0}^\infty \biggl( \int_0^x (-1)^n t^n dt \biggr) $$

$$ = \Biggl( \sum_{n=0}^\infty (-1)^n \frac{t^{n+1}}{n+1} \Biggr) \Bigg|_0^x $$

$$ = \sum_{n=0}^{\infty} (-1)^n \frac{x^{n+1}}{n+1} $$

So, we did it!  We have a polynomial series that calculates the natural logarithm!  Granted, we need to shift our
input by 1, as this series is $\ln{(1+x)}$, but that's a simple hurdle to jump!

Except we're limited.  Very limited.  Remember, the geometric series only applies to the function $\frac{1}{1+x}$ for
$|x| < 1$, otherwise it diverges.  The same limitation exists here.  What's worse, the series only converges quickly
for $|x| < \frac{1}{2}$; outside this range, the number of terms becomes too much even for a computer to calculate in
a reasonable amount of time. This is fine if all the values you need to calculate a logarithm for are between 0.5 and 1.5,
but most problems involving logarithms tend to have very large values.

Well, we tried.  Pack up, go home, see you next time.

## Properties of logarithms

Actually, as it turns out, this *would* be the end if we were dealing with almost any other function.
But we are dealing with logarithms, and logarithms are special.  There are two properties that we
can use to reduce our inputs so that we can calculate the logarithm of any value we want!

The first property is that *multiplication in the input is equivalent to addition of the outputs*.

This means that if the input is the product of two factors, the logarithm of that product is the same
as the logarithms of each factor taken individually and added together.  For example, if we wanted to
find the natural logarithm of the value 6, we can compute either $\ln(6)$ or $\ln(2) + \ln(3)$, because
$6 = 2 \cdot 3$.

The general form of this property is

$$ \log_b{(ac)} = \log_b{(a)} + \log_b{(c)} $$

The second property is that *the logarithm of a value raised to some power is that power times the
logarithm of the (unraised) value*.

This means that exponents in the input of the logarithm can hop out and
become a coefficient of the output. For example, the number 8 can also be written as
$2^3$ $(2 \cdot 2 \cdot 2 = 8)$, so $\ln(8) = \ln(2^3) = 3\ln(2)$.

The general form of this property is

$$ \log_b{(a^c)} = c \log_b{(a)} $$

Each of these properties allow us to reduce the argument of the logarithm in different ways. Using the
first property, if we have the natural logarithm of a known value (2 and 10 are popular choices), we can
reduce the argument by powers of that constant until we get a small enough input. Let's use 15 as an
example. If we have the natural logarithm of 2 calculated, we can keep dividing 15 until it is close
to 1 while keeping track of the number of times we divided by 2. After dividing by 2 four times,
we reduce 15 to 0.9375, so $0.9375 \cdot 2^4 = 15$. We can plug this value into our series like this:

$$ \ln(15) = \ln(2^4 \cdot 0.9375) = 4 \ln(2) + \ln(0.9375) $$

$$ = 4 \ln(2) + \ln(1 + (0.9375 - 1)) = 4 \ln(2) + \ln(1 + (-0.0625)) $$

$$ = 4 \ln(2) + (-0.0625) - \frac{(-0.0625)^2}{2} + \frac{(-0.0625)^3}{3} + ... $$
