for number in range(1, 100):
    message = ""
    output = ""
    if number % 3 == 0:
        message = "Fizz"
    if number % 5 == 0:
        message += "Buzz"
    output = message if message else number
    print(output)
