numbers = [1, 2, 3, 4, 5, 15]

for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'FizzBuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = "Fizz"
    elif numbers[i] % 5 == 0:
        numbers[i] = "Buzz"

print(numbers)

    