# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes:
    # name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to
# hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each
# employee on the screen.

# Title: Employee Class
# Author: Arianna Endres
# Date: 11/07/2025

class Employee:
    # Class Employee holds name, ID number, department, and job title attributes.
    def __init__(self, name, ID, department, job_title):
        self.name = name
        self.ID = ID
        self.department = department
        self.job_title = job_title

def main():
    # Create three Employee objects.
    employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    # Display the data for each employee.
    print(f'{employee1.name}:'
          f'\n\tID: {employee1.ID}'
          f'\n\tDepartment: {employee1.department}'
          f'\n\tJob Title: {employee1.job_title}')

    print(f'\n{employee2.name}:'
          f'\n\tID: {employee2.ID}'
          f'\n\tDepartment: {employee2.department}'
          f'\n\tJob Title: {employee2.job_title}')

    print(f'\n{employee3.name}:'
          f'\n\tID: {employee3.ID}'
          f'\n\tDepartment: {employee3.department}'
          f'\n\tJob Title: {employee3.job_title}')

if __name__ == '__main__':
    main()