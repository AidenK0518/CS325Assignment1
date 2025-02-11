# CS325Assignment1

This project sets out to use definitions to find the run time of a Colltaz Conjuncture.

## How the code works

The code works by first calling a colltaz method that uses the definition, which loops through the normal Colltaz Conjecture function until it reaches 1. 
For an Even number, divide n by 2
For an Odd number, multiply n by 3, then subtract 1.

This is done with this code:
<code>
    checkcase = n % 2
    if checkcase == 0:
        print(n)
        return colltaz(n/2)
    elif n == 1:
        print(n)
        return 1
    else:
        print(n)
        return colltaz((3*n)+1)
</code>

### Misc Content

This code was inspired by a Youtube video from Veritasium "The Simplest Math Problem No One Can Solve - Collatz Conjecture" (https://youtu.be/094y1Z2wpJg?si=0dFji01YLuq2rXU9)
An image relating to Collatz conjecture can be seen here.
![An image showing off a binary tree of the Collatz Conjecture, the top nodes are at 3, 9, 15, 33, 39, 43, and 45](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Collatz-graph-50-no27.svg/800px-Collatz-graph-50-no27.svg.png)

![A photo of my pet dog Luna, for moral support in this readme](https://i.ibb.co/vChG9FYL/IMG-1543.jpg)
