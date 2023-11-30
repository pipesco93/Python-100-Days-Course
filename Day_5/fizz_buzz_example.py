
for i in range(1,101):
    div_three = i % 3
    div_five = i % 5

    if div_three == 0 and div_five == 0:
        print("FizzBuzz")
    elif div_three == 0:
        print("Fizz")
    elif div_five == 0:
        print("Buzz")
    else:
        print(i)
