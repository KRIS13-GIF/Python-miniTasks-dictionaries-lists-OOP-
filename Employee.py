class Employee:

    def _init_(self, name, ID, department, job_title):
        self.__name=name
        self.__ID=ID
        self.__department=department
        self.__job_title=job_title
    def _str_(self):
        return self._name + " "+ str(self.ID)+ " "+ self.department+ " "+ self._job_title
    def getIDNr(self):
        return self.__ID
    def setID(self, newID):
        self.__ID=newID
    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name=newName
    def getDepartment(self):
        return self.__department
    def setDepartment(self, newDep):
        self.__department=newDep
    def getJobTitle(self):
        return self.__job_title
    def setJobTitle(self, newJobTitle):
        self.__job_title=newJobTitle
        
        
        
def main():

    e1=Employee("Susan Mayers", 47899, "Accounting", "Vice President")
    e2=Employee("Mark Jones", 39119, "IT", "Programmer")
    e3=Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    emp=[e1,e2,e3] # adding the employees into the list
    print(emp)
    print(e1,"\n",e2,"\n",e3)
    employees={e1.getIDNr():e1.getName(), e2.getIDNr():e2.getName(), e3.getIDNr():e3.getName()}
    print(employees.items()) # this is the dictionary right now




    option=int(input("Enter \n1 to add a new employee in dictionary\n2 for looking up in dictionary\n3 to change the properties of an employee\n4 to remove an employee\n0 to exit"))
    while option!=0:
        if option==1:
            name=input("Enter name for the employee: ")
            ID=int(input("Enter ID for the employee: "))
            department=input("Enter department for the employee: ")
            job_title=input("Enter the jobTitle: ")
            e=Employee(name, ID, department, job_title)
            employees[e.getIDNr()]=e.getName() #adding the employee into the dictionary
            emp.append(e) # adding employee into list
            print("Employee Added in the dictionary !")
            print(employees.items())

        elif option==2:
            print(employees.keys())
            id=int(input("Enter the id to search the person: "))
            if id in employees.keys():
                for em in emp:
                    if em.getIDNr()==id:
                        print(em)
            else:
                print("Employee not in the dictionary")

        elif option==3:
            id=int(input("Enter the id of the employee: "))
            if id in employees.keys():
                for em in emp:
                    if em.getIDNr()==id:
                        print(em)
                        print("Select 1 if you want to change the existing employee name\nSelect 2 if you want to change the "
                              "department\nSelect 3 if you want to change the job titile: ")
                        opt=int(input("Enter the option: "))
                        if opt==1:
                            name2=input("Enter the new name for the employee: ")
                            em.setName(name2) #changin the name of the employee inside the list
                            employees[id]=name2 
                            print("Employee Updated in list!")
                            print("Dictionary Updated!")
                            for i in emp:
                                print(i) # displays the list of the updated employee
                            print(employees.items())
                        elif opt==2:
                            department=input("Enter the new Department for this id: "+ str(id))
                            em.setDepartment(department)
                            print("Employee Updated in list! ")
                            for i in emp:
                                print(i) # displays the list of the updated employee
                        elif opt==3:
                            jobTitle=input("Enter the new job Title: ")
                            em.setJobTitle(jobTitle)
                            print("Employee Updated in list! ")
                            for i in emp:
                                print(i) # displays the list of the updated employee
            else:
                print("Id not in dictionary!")
        elif option==4:
            remove=int(input("Enter the Id which you want to remove from the list: "))
            if remove in employees.keys():
                employees.pop(remove) #removes the emplyee from dictionary
                for em in emp:
                    if em.getIDNr()==remove:
                        emp.remove(em)
                        for i in emp:
                            print(i)
                print("Employee deleted! ")
                print(employees.items())

        elif option ==0:
            print("You have exit the program")
            exit()
        print("\n")
        option = int(input(
        "Enter 1 to add a new employee in dictionary\n2 for looking up in dictionary\n3 to change the properties of an employee\n4 to remove an employee\n0 to exit"))

main()

# when arriving in this lesson finish this task by putting pickle files etc
