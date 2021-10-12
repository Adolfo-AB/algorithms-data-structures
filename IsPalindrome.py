def is_palindrome(input):
    input = list(input.replace(" ", ""))
    reverse_input = input[::-1]

    if input == reverse_input:
        return True
    else:
        return False

assert is_palindrome('aba') == True
assert is_palindrome('baa') == False
assert is_palindrome('was it a car or a cat i saw')