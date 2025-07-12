class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added.")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure: {total}")

    def display_employees(self):
        if not self.employees:
            print("No employees in the department.")
        else:
            print(f"Employees in {self.department_name} Department:")
            for emp in self.employees:
                emp.display_details()


if __name__ == "__main__":
    name = input("Enter department name: ")
    dept = Department(name)

    while True:
        print("\nMenu:")
        print("1. Add employee")
        print("2. Display all employees")
        print("3. Update employee salary")
        print("4. View total salary expenditure")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Employee name: ")
            emp_id = input("Employee ID: ")
            try:
                salary = float(input("Salary: "))
                dept.add_employee(Employee(name, emp_id, salary))
            except:
                print("Invalid salary.")

        elif choice == "2":
            dept.display_employees()

        elif choice == "3":
            emp_id = input("Enter employee ID to update: ")
            for emp in dept.employees:
                if emp.employee_id == emp_id:
                    try:
                        new_salary = float(input("New salary: "))
                        emp.update_salary(new_salary)
                        print("Salary updated.")
                    except:
                        print("Invalid salary.")
                    break
            else:
                print("Employee not found.")

        elif choice == "4":
            dept.total_salary_expenditure()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")
