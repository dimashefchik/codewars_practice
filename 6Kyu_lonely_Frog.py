# Example
# For x = 1, y = 8, the output should be 3.
#  step  from   to      action
#   1:     1 --> 2     forward(or double)
#   2:     2 --> 4       double
#   3:     4 --> 8       double

# For x = 1, y = 17, the output should be 5.
#  step  from    to      action
#   1:     1  --> 2     forward(or double)
#   2:     2  --> 4       double
#   3:     4  --> 8       double
#   4:     8  --> 16      double
#   5:     16 --> 17     forward

# For x = 1, y = 15, the output should be 6.
#  step  from    to      action
#   1:     1  --> 2      forward(or double)
#   2:     2  --> 3      forward
#   3:     3  --> 6      double
#   5:     6  --> 7      forward
#   6:     7  --> 14     double
#   7:     14 --> 15     forward

def jump_to(x, y):
    count = 0
    while y != x:
        if y%2 == 1 and y//2 >= x:
            y = y -1
        elif y%2 == 0 and y//2 >= x:
            y = y/2
        elif y//2 < x:
            y = y -1
        count += 1
    return count
