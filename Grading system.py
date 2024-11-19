num_grades = int(input("Enter the number of grades: "))
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0

for i in range(num_grades):
    grade = int(input("Enter grade  (0-100): "))
    if 90 <= grade <= 100:
        count_A += 1
    elif 75 <= grade <= 89:
        count_B += 1
    elif 60 <= grade <= 74:
        count_C += 1
    elif 50 <= grade <= 59:
        count_D += 1
    elif 0 <= grade <= 49:
        count_F += 1
    else:
        print("enter a grade between 0 and 100.")

total_grades = count_A + count_B + count_C + count_D + count_F
print("grade statistics:")


if total_grades > 0:
    overwall_A = (count_A / total_grades * 100)
    grade_coorecting_A = "grade" if count_A == 1 or count_A==0 else "grades"
    print(f": {count_A} {grade_coorecting_A} {overwall_A:}")

    overwall_B = (count_B / total_grades * 100)
    grade_coorecting_B = "grade" if count_B == 1 or count_B==0 else "grades"
    print(f": {count_B} {grade_coorecting_B} {overwall_B:}")

    overwall_C = (count_C / total_grades * 100)
    grade_coorecting_C = "grade" if count_C == 1 or count_C==0 else "grades"
    print(f": {count_C} {grade_coorecting_C} {overwall_C:}")

    overwall_D = (count_D / total_grades * 100)
    grade_coorecting_D = "grade" if count_D == 1 or count_D==0  else "grades"
    print(f": {count_D} {grade_coorecting_D} {overwall_D:}")

    overwall_F = (count_F / total_grades * 100)
    grade_coorecting_F = "grade" if count_F == 1 or count_F==0 else "grades"
    print(f": {count_F} {grade_coorecting_F} {overwall_F:}")
else:
    print("No  grades entered.")
    # I have already done this projcet so it is only for commit
    # it is last my commit 