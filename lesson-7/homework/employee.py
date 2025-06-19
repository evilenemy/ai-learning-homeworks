class Employee:
  def __init__(self, id_, name, salary, position):
    self.id = int(id_)
    self.name = name
    self.salary = int(salary)
    self.position = position

  def __str__(self):
    return f"{type(self).__name__}(id={self.id}, name={self.name}, salary={self.salary}, position={self.position})"

  def to_txt(self):
    return f"{self.id}, {self.name}, {self.salary}, {self.position}\n"

  def to_dict(self):
    return {'id': self.id, 'name': self.name, 'salary': self.salary, 'position': self.position}

class EmployeeManager:
  employees = []
  filename = ""
  def __init__(self, filename="employee.txt"):
    self.filename = filename
    self.sync()

  def __str__(self):
    return f"{type(self).__name__}(employees_count={len(self.employees)})"

  def search_employee(self, employee_id):
    for employee in self.employees:
      if employee.id == employee_id:
        return employee
    else:
      return False

  def insert_employee(self, employee_id, name, salary, position):
    if self.search_employee(employee_id):
      raise IndexError("ID for this employee was already taken")
    employee = Employee(employee_id, name, salary, position)
    self.employees.append(employee)
    with open(self.filename, 'a') as file:
      file.write(employee.to_txt())
    return "Added successfully"

  def sync(self):
    try:
      with open(self.filename, 'r'):
        pass
    except Exception as e:
      with open(self.filename, 'w'):
        pass
    with open(self.filename, 'r+') as file:
      for line in file.readlines():
        arguments = line.replace("\n", "").split(", ")
        self.employees.append(Employee(arguments[0], arguments[1], arguments[2], arguments[3]))
    return f"Synced with '{self.filename}'"

  def update_employee(self, employee_id, name=None, salary=None, position=None):
    if not self.search_employee(employee_id):
      raise ValueError("Wrong ID given")
    with open(self.filename, 'w') as file:
      for employee in self.employees:
        if employee.id == employee_id:
          if name: employee.name = name
          if salary: employee.salary = salary
          if position: employee.position = position
          file.write(employee.to_txt())
          break
        else:
          file.write(employee.to_txt())
    return "\nUpdated successfully!"
  def delete_employee(self, employee_id):
    if not self.search_employee(employee_id):
      raise ValueError("Wrong ID given")
    lines = []
    with open(self.filename, 'r') as file:
      lines = file.readlines()
      for i in range(len(self.employees)):
        if self.employees[i].id == employee_id:
          lines.remove(self.employees[i].to_txt())
          self.employees.remove(self.employees[i])
    with open(self.filename, 'w') as file:
      file.writelines(lines)
    return "\nSuccessfully deleted!\n\n"
      
  def show_employees(self):
    if len(self.employees) == 0:
      print("Employees is empty.")
      return
    for employee in self.employees:
      print(f"{employee.id:4} {employee.name:15} {employee.salary:7} {employee.position}")

manager = EmployeeManager()

while True:
  option = int(input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n\nPlease enter a option: "))
  if option == 1:
    try:
      print(manager.insert_employee(int(input("Enter ID: ")), input("Enter name: "), int(input("Enter salary: ")), input("Enter position: ")))
    except ValueError as e:
      print(f"Malumotlardan bir xato kiritildi!\n{e}")
    except Exception as e:
      print(e)
    print("\n\n")
  elif option == 2:
    manager.show_employees()
    print("\n\n")
  elif option == 3:
    try:
      employee = manager.search_employee(int(input("Enter employee ID: ")))
      if employee:
        print(f"{employee.id:4} {employee.name:15} {employee.salary:7} {employee.position}")
      else:
        print("Foydalanuvchi topilmadi!")
    except ValueError as e:
      print(f"Ma'lumotlar xato kiritildi!\n{e}")
    except Exception as e:
      print(f"Noma'lum xatolik!\n{e}")
    print("\n\n")
  elif option == 4:
    try:
      employee_id = int(input("Enter employe ID: "))
      name = input("Enter new name or skip (press Enter): ")
      salary = input("Enter new salary or skip (press Enter): ")
      position = input("Enter new position or skip (press Enter): ")
      print(manager.update_employee(employee_id, name=name if name else None, salary=int(salary) if salary else None, position=position if position else None))
    except ValueError as e:
      print(f"Ma'lumot kiritishda xatolik!\n{e}")
    except Exception as e:
      print(e)
    print("\n\n")
  elif option == 5:
    try:
      print(manager.delete_employee(int(input("Enter employee ID: "))))
    except Exception as e:
      print(f"Noma'lum xatolik!\n{e}")
    print("\n\n")
  elif option == 6:
    break;