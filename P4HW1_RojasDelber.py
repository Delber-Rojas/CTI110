# Delber Rojas
# 04/30/2026
# P4HW1
# Collect scores with loops, validate each score, drop the lowest one, and compute the modified average.


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if value > 0:
            return value
        print("Please enter a positive integer.")


def get_score(index):
    while True:
        try:
            score = float(input(f"Enter score #{index}: "))
        except ValueError:
            print("INVALID Score entered!!!!")
            print("Score should be a number between 0 and 100")
            continue
        if 0 <= score <= 100:
            return score
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")


def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0.0


def drop_lowest_score(scores):
    if not scores:
        return []
    trimmed = scores.copy()
    trimmed.remove(min(trimmed))
    return trimmed


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def display_results(lowest_score, modified_scores, average, grade):
    formatted_scores = [f"{score:.1f}" for score in modified_scores]
    print("\n-------------Results-------------")
    print(f"Lowest Score                         : {lowest_score:.1f}")
    print(f"Score List after dropping lowest score: {formatted_scores}")
    print(f"Scores Average                       : {average:.2f}")
    print(f"Grade                                : {grade}")


def main():
    score_count = get_positive_int("How many scores do you want to enter? ")
    scores = [get_score(i) for i in range(1, score_count + 1)]

    lowest_score = min(scores)
    modified_scores = drop_lowest_score(scores)
    average = calculate_average(modified_scores)
    grade = letter_grade(average)

    display_results(lowest_score, modified_scores, average, grade)


if __name__ == "__main__":
    main()

