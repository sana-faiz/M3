def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

num = int(input("Enter a number: "))

print("Sum of whole numbers =", sum_numbers(num))