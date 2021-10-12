def is_odd(x):
    return bool(x % 2)

result = [is_odd(x) for x in range(1,100)]
print(result)