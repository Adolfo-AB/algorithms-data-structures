def find_longest_palindrome(input):
    palindrome = ''

    for i in range(len(input)):
        for j in range(len(input), i, -1):
            if len(palindrome) >= j-i:
                break

            elif input[i:j] == input[i:j][::-1]:
                palindrome = input[i:j]
                break
    return palindrome

assert find_longest_palindrome('babbab') == 'babbab'
assert find_longest_palindrome('babba') == 'abba'
assert find_longest_palindrome('abc') == 'a'