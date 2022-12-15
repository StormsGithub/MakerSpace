# Python Workshop, Activity 05

# Ask user what operation to do
mode = input("add or subtract:")

# Create two variables with different values
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# If the user enters "add"
if mode == "add":
    # Add them together
    result = x + y

# If the user enters "subtract"
if mode == "subtract":
    # Subtract y from x
    result = x - y

# Print the result
print("Result is:", result)
