# Here you will be asked to write your email address. 
# My little slicer robot will then tell you what your 
# username will be, and what the domain name is.

# Get user email address
email = input("what is your email address? : ").strip()

# slice out user name
user = email[:email.index("@")]

# slice out domain name
domain = email[email.index("@") + 1 :]

# format message
output = "Your username is {} and your domain name is {}"
message = output.format(user, domain)

# display output message
print(message)
