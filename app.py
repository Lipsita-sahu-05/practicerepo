name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("Next year, you will be", age + 1, "years old.")