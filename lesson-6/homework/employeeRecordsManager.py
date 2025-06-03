while True:
  option = 6
  try:
    option = int(input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n\nPlease enter a option: "))
  except ValueError:
    print("You should choose one of the number of option list")
  if option == 1:
    name = input("Please, enter employee's name: ")
    position = input("Please, enter employee's postion: ")
    salary = input("Please, enter employee's salary: ")
    if name and position and salary:
      last_employee_id = 0
      with open("employees.txt", "r") as file:
        employees = file.read().split("\n")
        if len(employees) > 2:
          last_employee_id = int(employees[-2].split(", ")[0])
      with open("employees.txt", "a") as file:
        emp_id = str(last_employee_id + 1)
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Added successfully")
    else:
      print("One or more fields may be empty or wrong. Please, check and try again.\n\n")
  elif option == 2:
    with open("employees.txt", "r") as file:
      for line in file.readlines():
        details = line.replace("\n", "").split(", ")
        if len(details) < 1:
          continue
        print(f"{details[0]:11} {details[1]:15} {details[2]:20} {details[3]}")
  elif option == 3:
    employee_id = 0
    ok = False
    try:
      employee_id = int(input("Enter employee ID: "))
    except ValueError:
      print("You should enter a number!")
      continue
    with open("employees.txt", "r") as file:
      for line in file.readlines():
        employee = line.replace("\n", "").split(", ")
        if employee[0] == "Employee ID":
          continue
        if employee_id == int(employee[0]):
          ok = True
          print(f"Employee ID Name            Position             Salary\n{employee[0]:11} {employee[1]:15} {employee[2]:20} {employee[3]}")
          break
      else:
        if not ok:
          print("Nothing found through this ID :(")
  elif option == 4:
    employee_id = 0
    ok = False
    try:
      employee_id = int(input("Enter employee ID: "))
    except ValueError:
      print("You should enter a number!")
      continue
    with open("employees.txt", "r") as file:
      for line in file.readlines():
        employee_ = line.split(", ")
        if employee_[0] == "Employee ID":
          continue
        if employee_id == int(employee_[0]):
          ok = True
          break
      else:
        if not ok:
          print("Nothing found through this ID :(")
    if ok:
      name = input("Please, enter employee's name: ")
      position = input("Please, enter employee's postion: ")
      salary = input("Please, enter employee's salary: ")
      if name and position and salary:
        last_employee_id = 0
        with open("employees.txt", "r") as file:
          lines = ""
          for line in file.readlines():
            employee = line.replace("\n", "").split(", ")
            if employee[0] == "Employee ID":
              continue
            if int(employee[0]) == employee_id:
              lines += f"{employee_id}, {name}, {position}, {salary}\n"
              print("Updated successfully")
            else:
              lines += line
        with open("employees.txt", "w") as file:
          file.write("Employee ID, Name, Position, Salary\n" + lines)
      else:
        print("One or more fields may be empty or wrong. Please, check and try again.\n\n")
  elif option == 5:
    with open("employees.txt", "w") as file:
      file.write("Employee ID, Name, Position, Salary\n")
      print("Cleared successfully")
  elif option == 6:
    break
  if input("\nDo you continue? (y/N): ") in ["Y", "y"]:
    continue
  else:
    break