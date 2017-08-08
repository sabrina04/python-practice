""" Given the names and grades for each student in a Physics class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. """

n=int(raw_input())
students = []
if n>=2 and n<=5:
    for _ in range(n):
        name = raw_input()
        score = float(raw_input())
        students.append([name,score])
    
    std_sorted = sorted(students,key=lambda x: float(x[1]))
    second_min = std_sorted[0][1]
    final_list = []
    
    for i in range(len(std_sorted)-1):
        if second_min<std_sorted[i+1][1]:
            second_min = std_sorted[i+1][1]
            break
    
    for i in range(1,len(std_sorted)):
        if second_min==std_sorted[i][1]:     
            final_list.append(std_sorted[i][0])
                       
    final_list.sort()        
    for name in final_list:
        print name