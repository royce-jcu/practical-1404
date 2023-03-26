def main():
    score = get_valid_score()
    while score != -1:
        print("\nMENU")
        print("====")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").lower()
        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            print_result(score)
        elif choice == 's':
            show_stars(score)
        elif choice == 'q':
            print("farewell!")
            break
        else:
            print("Invalid choice.")


def get_valid_score():
    while True:
        score = input("Enter a valid score (0-100): ")
        if int(score) >= 0 or int(score) <= 100:
            return score
        else:
            print("Invalid score.")


def print_result(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


def show_stars(score):
    print("*" * score)


main()
