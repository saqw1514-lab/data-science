
num = int(input("Enter a positive number: "))

original_num = num
temp = num
digits = 0
total = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

if digits == 0:
    digits = 1

temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if num >= 0 and total == original_num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
