# Recursive approach
# def find_nth_fibonacci(n):
#     if n == 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return find_nth_fibonacci(n-1) + find_nth_fibonacci(n-2)

# Dynamic programming approach
def find_nth_fibonacci(n, fib_array = {1:0, 2:1}):
    if n in fib_array:
        return fib_array[n]
    
    fib_array[n] = find_nth_fibonacci(n-1, fib_array) + find_nth_fibonacci(n-2, fib_array)
    return fib_array[n]


assert find_nth_fibonacci(1) == 0
assert find_nth_fibonacci(2) == 1
assert find_nth_fibonacci(3) == 1
assert find_nth_fibonacci(6) == 5
