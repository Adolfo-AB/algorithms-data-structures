
# Naive approach
#def two_sum_problem(lst, target):
#    for i in range(0, len(lst)-1):
#        for j in range(1, len(lst)):
#            if lst[i] + lst[j] == target:
#                return (i, j)
#    return None

# Smart approach
def two_sum_problem(lst, target):
    hash_table = dict()

    for i in range(len(lst)):
        complement = target - lst[i]
        if complement in hash_table:
            return (i, hash_table[complement])
        else:
             hash_table[lst[i]] = i
             print(hash_table)
    return None

assert two_sum_problem([1, 2, 3], 4) in [(0,2), (2,0)]
assert two_sum_problem([1, 2, 3], 19) == None