def is_prime(number):
    is_prime = True
    for num in range(2, number - 1, 1):
        if number % num == 0:
            is_prime = False
    return is_prime

print(is_prime(number=49))