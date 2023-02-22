repeat = 'yes'
while repeat != 'no':
    rate = float(input("What is your rate?\n>>> "))
    hours = float(input("How many hours do you work in the pay period?\n>>> "))
    effectiveness = float(input("What is your effectiveness?\n>>> "))
    total_bills = rate * hours
    effectiveness = effectiveness * .01
    failed_bills = total_bills * (1 - effectiveness)

    if failed_bills > total_bills*.4:   
        difference = (failed_bills - (total_bills * .4))*.01
        print(f"You are going to have ${difference:.2f} taken out of your pay per hour for a total of ${(difference * hours):.2f}.")
    else:
        print("You are not going to loose any money because you are above 60 percent effectivness")
    repeat = input("press enter to go again.")