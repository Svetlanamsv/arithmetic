print("Enter three-digit number")
b=int(input())

b_hundreds=b//100
b_dezons=(b%100)//10
b_numbers=(b%100)%10

addition = b_hundreds+b_dezons+b_numbers
multiplication = b_hundreds*b_dezons*b_numbers
print("Addition three number is ", addition)
print("Multiplication three number is ", multiplication )