from myModule import employee






"-------------------------------------- Creating an Employee Object---------------------------------------------"

# Create an instance of the Employee class with the initial details
person = employee("Joe" , "Developer" , "Front_end" , 90000 , 2010)


# print(person)    # Display the employee's initial information          



'------------------------------------ Testing all Functions-----------------------------------------------------'

print(person.__doc__)                # Display class documentation for verification
# print(person)                        # Print the employee's details to the terminal     
print(person.years_worked())         # Verify the calculation of years worked
print(person.total_expense())        # Check the total salary calculation
person.print_employee_information()  # Ensure a text file is created with the correct information



'''....................................Acess Methodes.........................................................'''

# Access and verify individual employee attributes

# person.get_name()
# person.get_department()
# person.get_hire_year()
# person.get_job_title()
# person.get_salary()


"------------Testing Methods for Update Employee's Information and Saving at txt.file---------------------------"


# print(person)        # Display the current employee information                        


# Update the employee's name and verify the old file is removed and information is updated
# person.set_name("David")                          
# print(p298erson)    


# person.set_job_title("New Job")  # Update the job title and verify the change
# print(person)        



# person.set_department("New Department")  # Update the department and verify the change
# print(person) 


# person.set_salary(100000)  # Update the salary and verify the change
# print(person)   


# person.set_hire_year(2023)  # Update the hire year and verify the change
# print(person)


# Re-check years worked and total expense after updates
# print(person.years_worked())         # Verify if years worked is recalculated correctly
# print(person.total_expense())        # Verify if the total expense reflects the updated salary




"------------------------------------Testing After Updates-----------------------------------------------"

# print(person)    # Final check: print all updated information









