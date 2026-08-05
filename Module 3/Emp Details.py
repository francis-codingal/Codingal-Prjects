def input_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    return {"name": name, "id": emp_id, "department": department, "salary": salary}

def display_employee(emp):
    print("\n--- Employee Details ---")
    print(f"ID         : {emp['id']}")
    print(f"Name       : {emp['name']}")
    print(f"Department : {emp['department']}")
    print(f"Salary     : ${emp['salary']:.2f}")

employee = input_employee()
display_employee(employee)
