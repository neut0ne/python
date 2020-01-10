# Welcome to the cinema! We are showing 4 films, with different age limits. 
# Each film has 5 seats to begin with. 
# Choose your film, then type your age. Please be honest.
# If there are enough seats and you are the allowed age or more, enjoy the film!
# Observe that when your seat is taken, there will be one seat less available on that film...

films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5],
    }

while True:
    # .title() makes the first letter of every work capital.
    # .capitalize() would only capitalize the first letter of the first word.
    choice = input("What film would you like to see? : ").strip().title()

    # in: checks if the output from choice exists in films.
    # pass is a placeholder, saying "please move on..."
    if choice in films:
        age = int(input("How old are you? : ").strip())

        # Check user age
        if age >= films[choice][0]

        # Check enough seats

        num_seats = films[choice][1]
        
        if num_seats > 0:
            print("Enjoy the film!")
            # subtract one seat from the chosen film
            films[choice][1] = films[choice][1] - 1
        else:
            print("You are too young to see that film! Please choose a film within your age limit.")
        pass
    else:
        print("We don't have that film, please choose another one.")
