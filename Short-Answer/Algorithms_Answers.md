#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because it will only be as big as a.


b) O(n^2) because of the nested loops and is reliant on size of n.


c) O(n) becuase it will only be as big as 'bunnies'.

## Exercise II

I think to minimise the amount of dropped and broken eggs we will want to go with a binary search. (O(log n))

Steps:

1. Divide total number of floors by 2 and go to resulting floor. (Middle floor)

2. Drop egg and see if it breaks.

    a. If it breaks, find the middle of the lower half of buildings floors. Repeat step 2.

    b. If it does not break, find the middle of the upper half of buildings floors. Repeat step 2.

4) When only one floor is left, we know we have our answer.
