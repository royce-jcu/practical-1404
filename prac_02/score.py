def main():
    user_score = float(input("Enter your score: "))
    result = determine_result(user_score)
    print("Your result is:", result)


def determine_result(user_score):
    if user_score > 100 or user_score < 0:
        return "Invalid score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
