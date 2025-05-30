from datetime import datetime, date #Using to get age and storing date_of_birth
import csv  # Using for file operations

class Student:
    """
    #-Student class with private attribtutes.
    #- We used __ before the attiribute to indicate that they are private attributes
    #-With getter and setter
    @param __student_number: Student number which is used as a unique identifier @Type = Str
    @param __first_name: Student first name @Type = Str
    @param __last_name: Student last name @Type = Str
    @param __date_of_birth: Student date of birth @Type = Int
    @param __country_of_birth: Student country of birth @Type = Str
    @param __sex: Student sex (Male/Female) @Type = Str
    """
    def __init__(self, student_number, first_name, \
        last_name, date_of_birth, country_of_birth, sex):
        self.__student_number = str(student_number)
        self.__first_name = str(first_name)
        self.__last_name = str(last_name)
        self.__date_of_birth = self.formatDate(date_of_birth)
        self.__country_of_birth = str(country_of_birth)
        self.__sex = str(sex)

    #-------------------------#
    # Getter Methods Section  #
    #-------------------------#
    """
    #-Student number getter
    @returns students number @Type = Str
    """
    def getStudentNumber(self):
        return self.__student_number

    """
    #-Student first_name getter
    @returns first name of student @Type = Str
    """
    def getFirstName(self):
        return self.__first_name

    """
    #-Student last_name getter
    @returns last name of student @Type = Str
    """
    def getLastName(self):
        return self.__last_name

    """
    #-Student date of birth getter
    @returns students date of birth @Type = Str
    """
    def getDateOfBirth(self): 
        return self.__date_of_birth.strftime("%Y-%m-%d")


    """
    #-Student country of birth getter
    @returns students country of birth @Type = Str
    """
    def getCountryOfBirth(self):
        return self.__country_of_birth

    """
    #-Student sex getter
    @returns students sex @Type = Str
    """
    def getSex(self):
        return self.__sex

    """
    #-Student age getter
    @returns students age @Type = Str
    """
    def getAge(self): 
        return datetime.today().year - self.__date_of_birth.year

    #-------------------------#
    # Setter Methods Section  #
    #-------------------------#
    """
    #-Student number setter
    @param student_number = passed student number @Type = Str
    """
    def setStudentNumber(self, student_number):
        self.__student_number = student_number

    """
    #-Student first_name setter
    @param first_name = passed student first_name @Type = Str
    """
    def setFirstName(self, first_name):
        self.__first_name = first_name

    """
    #-Student last_name setter
    @param last_name = passed student last_name @Type = Str
    """
    def setLastName(self, last_name):
        self.__last_name = last_name

    """
    #-Student date_of_birth setter
    @param date_of_birth = passed student date_of_birth @Type = Str
    """
    def setDateOfBirth(self, date_of_birth): 
        self.__date_of_birth = self.formatDate(date_of_birth)

    """
    #-Student country_of_birth setter
    @param country_of_birth = passed student country_of_birth @Type = Str
    """
    def setCountryOfBirth(self, country_of_birth):
        self.__country_of_birth = country_of_birth

    """
    #-Student sex setter
    @param sex = passed student sex @Type = Str
    """
    def setSex(self, sex):
        self.__sex = sex

    def toList(self):
        """
        #- Convert student object to list format for CSV storage
        """
        return [
            self.__student_number,
            self.__first_name,
            self.__last_name,
            self.__date_of_birth.strftime("%Y-%m-%d"),
            self.__country_of_birth,
            self.__sex,
            self.getAge()
        ]
    @staticmethod
    def formatDate(date_str):
        """
        #- Ensure the date is correctly formatted, accepting multiple formats.
        """
        if isinstance(date_str, datetime):
            return date_str  # If it's already a datetime object, return it directly
        
        for fmt in ("%Y-%m-%d", "%Y%m%d"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError("Invalid date format. Please use YYYY-MM-DD or YYYYMMDD.")

class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = self.loadFromFile()

    def loadFromFile(self):
        students = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    student = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                    students.append(student)
        except FileNotFoundError:
            pass  # If the file does not exist, it will be created on save
        return students

    def saveToFile(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Number", "First Name", "Last Name", "Date of Birth", "Country of Birth", "Sex"])
            for student in self.students:
                writer.writerow(student.toList())

    def addStudent(self, student):
        if len(self.students) < 100:
            self.students.append(student)
            self.saveToFile()
            print(f"Student {student.getFirstName()} {student.getLastName()} added successfully.")
        else:
            print("Cannot add more students. The student list is full.")

    def findStudent(self, student_number):
        for student in self.students:
            if student.getStudentNumber() == student_number:
                return student
        return None


    def showStudents(self):
        for student in self.students:
            print(student.toList())


#-------------------------#
# Main Menu Section       #
#-------------------------#

def main():
    student_manager = StudentManager()  # initializes the class to store student records
    
    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Show All Students Born in a Given Year")
        print("5. Modify Student Record")
        print("6. Delete Student")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':  # adds student
            student_number = input("Enter student number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            country_of_birth = input("Enter country of birth: ")
            sex = input("Enter sex (Male/Female): ")
            
            student = Student(student_number, first_name, last_name, date_of_birth, country_of_birth, sex)
            student_manager.addStudent(student)
        
        elif choice == '2':  # shows all students
            student_manager.showStudents()
        
        elif choice == '3':  # finds a student by student number
            student_number = input("Enter student number to search: ")
            student = student_manager.findStudent(student_number)
            if student:
                # Display all information about the student (this part was missing)
                print(f"Student Number: {student.getStudentNumber()}")
                print(f"First Name: {student.getFirstName()}")
                print(f"Last Name: {student.getLastName()}")
                print(f"Date of Birth: {student.getDateOfBirth()}")
                print(f"Country of Birth: {student.getCountryOfBirth()}")
                print(f"Sex: {student.getSex()}")
                print(f"Age: {student.getAge()}")
            else:
                print("Student not found.")

        
        elif choice == '4':  # shows all students born in the given year
            year = input("Enter year to search for students born in that year: ")
            year = int(year)
            for student in student_manager.students:
                if student.getDateOfBirth().startswith(str(year)):
                    print(student.toList())
        
        elif choice == '5':  # modifies student record
            student_number = input("Enter student number to modify: ")
            student = student_manager.findStudent(student_number)
            if student:
                print("What field would you like to modify?")
                print("1. First Name")
                print("2. Last Name")
                print("3. Date of Birth")
                print("4. Country of Birth")
                print("5. Sex")
                field = input("Choose a field to modify: ")
                
                if field == '1':
                    new_first_name = input("Enter new first name: ")
                    student.setFirstName(new_first_name)
                elif field == '2':
                    new_last_name = input("Enter new last name: ")
                    student.setLastName(new_last_name)
                elif field == '3':
                    new_date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")
                    student.setDateOfBirth(new_date_of_birth)
                elif field == '4':
                    new_country = input("Enter new country of birth: ")
                    student.setCountryOfBirth(new_country)
                elif field == '5':
                    new_sex = input("Enter new sex (Male/Female): ")
                    student.setSex(new_sex)
                
                student_manager.saveToFile()
                print("Student record updated successfully.")
            else:
                print("Student not found.")
        
        elif choice == '6':  # deletes the student
            student_number = input("Enter student number to delete: ")
            student = student_manager.findStudent(student_number)
            if student:
                student_manager.students.remove(student)
                student_manager.saveToFile()
                print(f"Student {student.getFirstName()} {student.getLastName()} deleted successfully.")
            else:
                print("Student not found.")
        
        elif choice == '7':  # exit
            print("Exiting...")
            break
        
        else:
            print("Invalid option, please try again.")

#Main function
if __name__ == "__main__": #Only executes the main() function when the file is not imported
    main()
