grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}

if len(grades)==len(students):
    students_list_sort =sorted(list(students))
    journal_itog = dict()
    for i in range(len(grades)):
        journal_itog[students_list_sort[i]] = sum(grades[i])/len(grades[i])

    print(journal_itog)
else:
    print("нет соотвествия между оценками и студентами ")
