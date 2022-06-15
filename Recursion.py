# We're going to take a look at recursion with a famous example—the Fibonacci Sequence.

# The Fibonacci Sequence follows one rule: get the next number in the sequence by adding the two previous numbers. Here is an example of the sequence:

# function getFib(position) {
#   if (position == 0) { return 0; }
#   if (position == 1) { return 1; }
#   var first = 0,
#       second = 1,
#       next = first + second;
#   for (var i = 2; i < position; i++) {
#     first = second;
#     second = next;
#     next = first + second;
#   }
#   return next;
# }


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)
