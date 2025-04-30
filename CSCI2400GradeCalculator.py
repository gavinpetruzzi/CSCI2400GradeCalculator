exam1 = float(input("Exam 1 Score: "))
exam2 = float(input("Exam 2 Score: "))
exam3 = float(input("Exam 3 Score: "))

# If exam 3 curve applies uncomment and change value
# exam3 += _____
# if exam3 > 100.0:
#     exam3 = 100.0
examTotal = (exam1 + exam2 + exam3)

labAvg = float(input("Lab Average: "))
quizAvg = float(input("Quiz Average: "))

examScore = ((examTotal / 3) * 0.48)
labScore = (labAvg * 0.42)
quizScore = (quizAvg * 0.1)

currGrade = examScore + labScore + quizScore

print("===================================================================================================================================================================")
print("(93%-100% A), (90%-93% A-), (87%-90% B+), (83%-87% B), (80%-83% B-), (77%-80% C+), (73%-77% C), (70%-73% C-), (67%-70% D+), (63%-67% D), (60%-63% D-), (0%-59.9% F)")
print("===================================================================================================================================================================")
print("Current grade in CSCI 2400 is %", currGrade)
print("===================================================================================================================================================================")
print("Grade on final needed for an A: %", round(((((93.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an A-: %", round(((((90.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an B+: %", round(((((87.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an B: %", round(((((83.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an B-: %", round(((((80.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an C+: %", round(((((77.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an C: %", round(((((73.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an C-: %", round(((((70.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an D+: %", round(((((67.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an D: %", round(((((63.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an D-: %", round(((((60.0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("Grade on final needed for an F: %", round(((((0 - labScore - quizScore) / 0.48) * 4) - examTotal), 2))
print("===================================================================================================================================================================")
