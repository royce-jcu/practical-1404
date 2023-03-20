name = input("Enter name: ")
menu = ["(H)ello", "(G)oodbye", "(Q)uit"]
user_choice = input(menu[0] + "\n" + menu[1] + "\n" + menu[2] + "\n")

while user_choice != "Q":
    if user_choice == "H":
        print("Hello", name)
    elif user_choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    menu = ["(H)ello", "(G)oodbye", "(Q)uit"]
    user_choice = input(menu[0] + "\n" + menu[1] + "\n" + menu[2] + "\n")

print("Finished.")
