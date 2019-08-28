#COMPANIES AND EMPLOYEES

#Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.

class Employee:

    def __init__(self, first_name, last_name, job_title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date

#Create a Company type that employees can work for. A company should have a business name, address, and industry type.

class Company:

    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()

#Create two companies, and 5 people who want to work for them.

right_star = Company("Right Star", "123 Fake St", "Chemical")
left_star = Company("Left Star", "12 1st st", "Advertising" )

Mike_Jones = Employee("Mike", "Jones", "Regional Manager", "8/28/19")
Curt_Cato = Employee("Curt", "Cato", "Superintendant", "7/1/2018")
Dustin_Hobson = Employee("Dustin", "Hobson", "Executive", "6/28/18")
Joe_Kennerly = Employee("Joe", "Kennerly", "Accountant", "4/24/2019")
Adam_Knowles = Employee("Adam", "Knowles", "Nurse", "2/12/2019")

#Assign 2 people to be employees of the first company.
right_star.employees.append(Adam_Knowles)
right_star.employees.append(Mike_Jones)
#Assign 3 people to be employees of the second company.
left_star.employees.append(Dustin_Hobson)
left_star.employees.append(Curt_Cato)
left_star.employees.append(Joe_Kennerly)

companies = list()
companies.append(right_star)
companies.append(left_star)
#Output a report to the terminal the displays a business name, and its employees.
for company in companies:
    print(f'{company.business_name} is in the {company.industry_type} industry and has the following employees:')
    for employee in company.employees:
        print(f'    * {employee.first_name} {employee.last_name}')





