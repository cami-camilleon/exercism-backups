"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded = []

    while student_scores:
        rounded.append(round(student_scores.pop()))

    return rounded




def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    sum = 0

    for item in student_scores:
        if item <= 40:
            sum = sum + 1
            print(sum)

    return sum


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best = []

    for item in student_scores:
        if item >= threshold:
            best.append(item)

    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    interval = (highest - 40) // 4
    grades = [41]
    for num in range(0, 3):
        grades.append(grades[num] + interval)

    return grades


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranked_list = []

    for num in range(0, len(student_scores)):
        ranked_list.append(f'{num + 1}. {student_names[num]}: {student_scores[num]}')

    return ranked_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    
    perfect_list = []

    for item in student_info:
        print(item)
        if item[1] == 100:
            perfect_list.extend(item)
            break

    return perfect_list

count_failed_students([40, 40, 35, 70, 30, 41, 90])