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
'''height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight) / float(height)**2
print(int(BMI))'''

# Your LIFE left in Weeks
'''age = input("What is your current age? ")
yearLeft = 90 - int(age)
monthsLeft = yearLeft * 12
weeksLeft = yearLeft * 52
daysLeft = yearLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")'''

# Tip Calculator
print("Welcome to the tip calculator!")

billAmount = input("What was the total bill? $")
tipAmount = input("How much tip would you like to give? 10, 12, or 15? ")
billSplit = input("How many people to split the bill? ")
addedTip = 0.0

if tipAmount == "12":
    addedTip = float(billAmount) * 1.12
elif tipAmount == "10":
    addedTip = float(billAmount) * 1.1
elif tipAmount == "15":
    addedTip = float(billAmount) * 1.15

splitedAmount = addedTip / int(billSplit)
print(round(splitedAmount, 2))
