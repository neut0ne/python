# Ask user for name
name = input("What is your name? : ")
print(name)

# Ask user for age
age = input("How old are you? : ")
print(age)

# Ask user for city
city = input("What city do you live in? : ")
print(city)

# Ask user for what they enjoy
love = input("What do you love to do? : ")
print(love)

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."

# order of placeholders {} :
output = string.format(name, age, city, love)

#Print output to screen
print(output)

