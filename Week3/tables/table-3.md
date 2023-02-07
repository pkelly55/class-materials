# Price = [4,5,7,3,2,1,6,8]
           1 2 3 1 1 1 2 3
           0 1 2 3 4 5 6 7
## Table

## While Condition -- D != {} and done = false

i   h   done    D       Span
0   -1  false   {0}     S[0] = 1
1   -1  false    {1}    S[1] = 2
2   -1   false    {2}   S[2] = 3
3   2   true    {2,3}   S[3] = 1
4   4   true    {2,3,4}   S[4] = 1
5   4   true    {2,3,4,5}   S[5] = 1
6   2  true    {2,6} S[6] = 4
7   -1   false    {7} S[7] = 5
