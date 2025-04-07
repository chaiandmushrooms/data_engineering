arr = [[input("Enter name: "), float(input("Enter score: "))] for i in range(int(input("Enter number of students: ")))]
arr = (sorted(arr, key = lambda arr: arr[1]))
lowest = arr[0][1]
second_lowest = float('-inf')
while(second_lowest < lowest):
    for student in arr:
        if student[1] > lowest:
            second_lowest = student[1]
            break
list_of_students = sorted([x[0] for x in arr if (x[1] == lowest)])
for students in list_of_students:
    print (students)

