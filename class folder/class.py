class Employee():
    def __init__(self,firstName,lastName,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + "." + lastName + "@" + "gmail.com"
        self.pay = pay
    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

emp_1 = Employee("vidit","gupta",9999999999999999999999999999)
print(emp_1)
print(emp_1.email)
print(emp_1.fullName())
# emp_1 = (Employee)
# emp_1.firstName = "VIDIT"
# emp_1.lastName = "GUPTA"
# emp_1.email = "gupta.vidit@icloud.com"
# emp_1.pay = 99999999999999999999999999999999999999999999
# print(emp_1.email)
# print(emp_1.pay)
# print(emp_1.firstName)
# print(emp_1.lastName)

# emp_2 = (Employee)
# emp_2.firstName = "tanishq"
# emp_2.lastName = "kaushik"
# emp_2.email = "tanishq.kaushik@icloud.com"
# emp_2.pay = 100000000000000000
# print(emp_2.email)
# print(emp_2.pay)
# print(emp_2.firstName)
# print(emp_2.lastName)

# emp_3 = (Employee)
# emp_3.firstName = "Jainam"
# emp_3.lastName = "hemani"
# emp_3.email = "hemani.Jainam@icloud.com"
# emp_3.pay = 1000000000000000002000000000030000
# print(emp_3.email)
# print(emp_3.pay)
# print(emp_3.firstName)
# print(emp_3.lastName)

# emp_4 = (Employee)
# emp_4.firstName = "daiwik"
# emp_4.lastName = "charabudla"
# emp_4.email = "charabudla.daiwik@icloud.com"
# emp_4.pay = 10000000000000000000000
# print(emp_4.email)
# print(emp_4.pay)
# print(emp_4.firstName)
# print(emp_4.lastName)
# print("jainam is manager")
# print("i am founder")
