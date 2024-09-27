import csv

with open('favorite_colors.csv', 'r') as f:
    data = csv.DictReader(f)
    count = 0
    answers = {}
    for row in data:
        if row['grade'] not in answers:
            answers[row['grade']] = {}
        answers[row['grade']][row['favorite_color']] = answers[row['grade']].get(row['favorite_color'], 0) + 1
    print(answers)