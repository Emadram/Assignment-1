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
            self.__sex
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
      """
      #- Manages a list of Student objects.
      """
      def __init__(self):
          self.students = []
  
      def addStudent(self, student):
          """
          #- Add a student to the list.
          """
          if len(self.students) < 100:
              self.students.append(student)
          else:
              print("Student list is full!")
  
      def findStudent(self, student_number):
          """
          #- Find a student by student number.
          """
          for student in self.students:
              if student.getStudentNumber() == student_number:
                  return student
          return None
  
      def showStudents(self):
          """
          #- Display all students.
          """
          for student in self.students:
              print(student.toList())
  
      
      def saveToFile(self, filename):
        """
        #- Save students to a CSV file.
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Student Number", "First Name", "Last Name", "Date of Birth", "Country of Birth", "Sex"])
            for student in self.students:
                writer.writerow(student.toList())

      def loadFromFile(self, filename):
        """
        #- Load students from a CSV file.
        """
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                self.students = [Student(row[0], row[1], row[2], Student.formatDate(row[3]), row[4], row[5]) for row in reader]
        except FileNotFoundError:
            print("File not found!")

#-------------------------#
# Main Menu Section      #
#-------------------------#
def main():
    return    

if __name__ == "__main__":
    main()
