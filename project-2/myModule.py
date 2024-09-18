from datetime import datetime
import os

class employee:
  ''' 
  This class repersents an employee 
  
  Attributes :
  name (str) : The name of the employee
  job_title (str) : The employess's job title
  department (str) : The employee's department
  salary (float) : The employee's salary for one year
  hire_year (int) : The year the employee has started
  '''
  


  def __init__(self, name: str , job_title:str , department:str ,salary:float , hire_year: int ):
    self.name = name 
    self.job_title = job_title
    self.department = department
    self.salary = salary
    self.hire_year = hire_year

    
    ''' 
    Initilizes an Empolyee object with name, job_title , department, salary and hire_year
    
    Arguments:
    name (str) : The name of the employee
    job_title (str) : The jobe title of the employee
    department (str) : The employee's department
    salary (float) : The salary of the employee in a year
    hire_year (int) : The year the employee has started
    '''
        



  def __str__(self):
    return  ( f"\n      Name: {self.name}\n"
              f" Job Title: {self.job_title}\n"
              f"Department: {self.department}\n"
              f"    Salary: {self.salary}\n"
              f" Hire Year: {self.hire_year}\n") 
  
  '''
  Returns a string representation of the Employee object.
  Returns:
  A string containing the employee's name, job title, department,
  salary, and hire year, each on a new line.
  '''
 




 
  def years_worked(self):
    working_time = datetime.now().year - self.hire_year
    if  self.hire_year > datetime.now().year:
       print("The hire year might be this year or past not future")
    return f"\n{self.name} has worked here for {working_time} years\n"
  '''
  Calculates the number of years the employee has worked at the company.
  returns str: A formatted string stating the employee's name and the number of years they have worked at the company.
  '''
  

  
  def total_expense(self):
    total_expens = (self.salary) * (datetime.now().year - self.hire_year)
    return f"\nThe total salary for {self.name} is {total_expens} $\n"
  '''
  Calculates the total salary expense for the employee since their hire date.
  returns str: A formatted string stating the total salary expense for the employee.
  '''
  



  def print_employee_information(self):
     
     file_name = f"{self.name.lower()}.txt"
     
     with open(file_name, "w") as file:
          file.write(f"Name: {self.name}\n"
                     f"Job Title: {self.job_title}\n"
                     f"Department: {self.department}\n"
                     f"Salary: {self.salary}\n"
                     f"Hire Year: {self.hire_year}")
  """
  This method writes employee's information into a text file.
  This method creates a text file named with emplyee's (in lowercase) name
  The file is saved in the current working dirctory
  This method returns None
  """
  
 



  "Access methods"
  def get_name(self):  #access to the Name, returns None
    print("Name:",self.name)
 
  def get_job_title(self):  #access to the Job title, returns None
   print("Job Title:" ,self.job_title)

  def get_department(self):   #access to the Department, returns None
    print("Department:",self.department)

  def get_salary(self):  #access to the Salary, returns None
   print("Salary",self.salary)

  def get_hire_year(self):  #access to the Hire Year, returns None
   print("Hire Year:",self.hire_year)





  def set_name(self, new_name:str):   

    old_file_name = f"{self.name.lower()}.txt"  

    if os.path.exists(old_file_name):
      os.remove(f"{self.name}.txt")
      print(f"The {self.name}.txt file  has been deleted.")
    else:
      print(f"The  {self.name.lower()}.txt file updated to ---> {new_name.lower()}.txt")

    self.name = new_name
    
    self.print_employee_information()
  '''
  Updates the employee's name 
  This method removes the saved txt file created with employee's name
  This method replaces the current name with the new_name passed to the method.
  new_name(str) : The new name to be assigned to the empolyee
  returnes None
     
  '''
  

  def set_job_title(self , new_job_title:str):
     self.job_title = new_job_title
     self.print_employee_information()
  '''
  Updates the Job employee's Job title at the txt file
  This method replaces the current job_title with the new_job_title passed to the method.
  new_job_title(str) : The new job title to be assigned to the empolyee
  returnes None
  '''





  def set_department(self, new_department):
     self.department = new_department
     self.print_employee_information()
  '''
  Updates the employee's department at the txt file
  This method replaces the current department with the new_department passed to the method.
  new_name(str) : The new_department to be assigned to the empolyee
  returnes None
  '''


  def set_salary(self, new_salary):
     self.salary = new_salary
     self.print_employee_information()
  '''
  Updates the employee's salary at the txt file
  This method replaces the current salary with the new_salary passed to the method.
  new_salary(float) : The new_salary to be assigned to the empolyee
  returnes None
  '''



  def set_hire_year(self, new_hire_year:int):
     self.hire_year = new_hire_year
     self.print_employee_information()
  '''
  Updates the employee's hire year txt file
  This method replaces the current hire_year with the new_hire_year passed to the method.
  new_name(int) : The new_hire_year to be assigned to the empolyee
  returnes None
  '''



if __name__ == '__main__':
  employee
     
    