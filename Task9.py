print("\nTask 9 - Prime Numbers from 2 to 50")

prime_numbers = []

for number in range(2, 51):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(number)

print("Prime Numbers:", prime_numbers)