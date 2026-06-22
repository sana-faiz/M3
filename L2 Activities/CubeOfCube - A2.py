def cube(num):
    return num ** 3

def check_number(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return "Number is not divisible by 3"

n = int(input("Enter a number: "))

print(check_number(n))