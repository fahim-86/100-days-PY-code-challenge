# Separate the Input degit and make an addition between them

# two_digit_number = input("Type a two digit number: ")

# firstNum = two_digit_number[0]
# secondNum = two_digit_number[1]
# print(int(firstNum) + int(secondNum))

# !--- PEMDAS (L2R) ----!
# Parentheses - ()
# Exponents - x^2
# Multiplication - *
# Division - /
# Addition - +
# Subtraction "-"


# equation for calculate BMI = weight(KG) / height(Meter)^2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight) / float(height)**2
print(int(BMI))
