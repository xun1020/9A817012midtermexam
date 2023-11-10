employee_list = []
total_salary = 0
output = "-" * 50
print("員工薪資輸入".center(50))
print("若姓名處未輸入則代表結束".center(50))

print("{}".format(output))
while True:
    eName = input("請輸入姓名:")
    if not eName:
        break
    eSalary = float(input("請輸入薪資:"))
    print()

    employee_dict = {'eName': eName, 'eSalary': eSalary}
    employee_list.append(employee_dict)

total_salary = sum(employee['eSalary'] for employee in employee_list)
average_salary = total_salary / len(employee_list)if len(employee_list) > 0 else 0


print("{}".format(output))

for employee in employee_list:
    formatted_eSalary = "{:>14,.0f}".format(employee['eSalary'])
    print(f"員工{employee['eName']:<7}的薪資為{formatted_eSalary}")

print("{}".format(output))

formatted_total_salary = "{:>25,.0f}".format(total_salary)
formatted_average_salary = "{:>29,.3f}".format(average_salary)
print(f"合計薪資:{formatted_total_salary}")
print(f"平均薪資:{formatted_average_salary}")
print('='*50)
