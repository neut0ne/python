# Travis the friendly (and quite silly) security bot keeps a list of people accepted to a system. 
# If you're not on the list, he will ask if you want to get added - no hassle!
# If you're on his list, he will ask if you would like to be removed - no hard feelings at all. 
# However, you might upset Travis if you don't want to get added.
# Travis likes to keep his list growing.

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

# print(len(known_users))

# While is a loop that runs over and over forever (that is, if nothing untrue happens..!)

while True:
    print("Hi, my name is Travis!")
    name = input("What is your name? : ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
            print("I'm sure you're coming back soon. See you later! \n")
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway! \n")
            
    else:
        print("Hmmm, I don't see you on my list, {}.".format(name))
        add_me = input("Would you like to be added to the system? (y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("Ok, you're added! \n")
        elif add_me == "n":
            regret = input("Are you really sure? (y/n): ").strip().lower()
            if regret == "n":
                known_users.append(name)
                print("I knew you would change your mind! Welcome to the system! \n")
            elif regret == "y":
                print("Alright then. But you don't know what you're missing out. Mumble, grumble. \n")            

