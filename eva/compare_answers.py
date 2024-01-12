import csv

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return {rows[0]: rows[1] for rows in reader}

def compare_answers(correct_answers, student_answers):
    correct_count = 0
    wrong_count = 0
    invalid_count = 0
    wrong_answers = []  # List to store question numbers of wrong answers

    for question, correct_answer in correct_answers.items():
        student_answer = student_answers.get(question)

        if student_answer not in ['A', 'B', 'C', 'D']:
            invalid_count += 1
        elif student_answer == correct_answer:
            correct_count += 1
        else:
            wrong_count += 1
            wrong_answers.append(question)  # Add the question number to the list

    return correct_count, wrong_count, invalid_count, wrong_answers

# Replace 'correct_answers.csv' and 'student_answers.csv' with your file paths
correct_answers = read_csv('rigth_answers.csv')
student_answers = read_csv('gpt3_answers.csv')

correct_count, wrong_count, invalid_count, wrong_answers = compare_answers(correct_answers, student_answers)

print(f'Correct Answers: {correct_count}')
print(f'Wrong Answers: {wrong_count}')
print(f'Invalid Answers: {invalid_count}')
print(f'Questions with Wrong Answers: {wrong_answers}')




