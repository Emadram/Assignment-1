import datetime #Using to get age and storing date_of_birth

class Student:
    """
    #-Student class with private attribtutes.
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
        self.__date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").year
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
        return self.__date_of_birth

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
        current_year = datetime.date.today().year
        return  current_year - self.__date_of_birth

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
        self.__date_of_birth = date.datetime.strptime(date_of_birth, "%Y-%m-%d")

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
        self.sex = sex

def main():
    return



if __name__ == "__main__":
    main()
