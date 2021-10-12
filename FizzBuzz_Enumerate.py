numbers = [1, 2, 3, 4, 5, 15]

for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'FizzBuzz'
    elif num % 3 == 0:
        numbers[i] = "Fizz"
    elif num % 5 == 0:
        numbers[i] = "Buzz"

print(numbers)

    