from itertools import permutations

def count_unique_arrangements(k, employee_departments):
    
    all_departments = set(d for deps in employee_departments for d in deps)
    department_list = list(all_departments)
    
    if len(department_list) < k:
        return 0

    valid_count = 0
    
    for selected_departments in permutations(department_list, k):
        valid = True
        for i in range(k):
            if selected_departments[i] not in employee_departments[i]:
                valid = False
                break
        if valid:
            valid_count += 1
            
    return valid_count

t = int(input())  
results = []
for _ in range(t):
    k = int(input())  # number of employees to send
    employee_departments = []
    for _ in range(k):
        n = int(input())  # number of departments the employee belongs to
        depts = list(map(int, input().split()))  # employee's departments
        employee_departments.append(depts)

    results.append(count_unique_arrangements(k, employee_departments))

for result in results:
    print(result)
