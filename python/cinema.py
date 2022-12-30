# Tyler's Cinema

films = {
    "Nemo": [3,5],
    "Gangsters": [18,5],
    "Power": [15,5]
}

# a dictionary featuring the current films showing

while True:
    choice = input("The current films showing are Nemo, Gangsters and Power! Which film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("What is your age?: ").strip())
        # input always saves as a string, so we need to convert to an integer
        
        if age >= films[choice][0]:
        # if the customer's age is greater than the age rating, they can proceed

            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                # checking to see if there are tickets available
            else:
                print("Sorry, we are sold out")
        else:
            print("You are too young to see that film")

    else:
        print("Sorry, we don't have that choice")