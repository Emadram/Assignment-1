class Student:
    """
    #-Student class with private attribtutes.
    #-With getter and setter
    @param __student_number: Student number which is used as a unique identifier @Type = Str
    @param __first_name: Student first name @Type = Str
    @param __last_name: Student last name @Type = Str
    @param __date_of_birth: Student date of birth @Type = Str
    @param __country_of_birth: Student country of birth @Type = Str
    @param __sex: Student sex (Male/Female) @Type = Str
    """
    def __init__(self, student_number, first_name
        last_name, date_of_birth, country_of_birth, sex):
    self.__student_number = student_number
    self.__first_name = first_name
    self.__last_name = last_name
    self.__date_of_birth = date_of_birth
    self.__country_of_birth = country_of_birth
    self.__sex = sex

    #-------------------------#
    # Getter Methods Section  #
    #-------------------------#
    """
    #-Student number getter
    @returns students number @Type = Str
    """
    def get_student_number(self):
        return self.__student_number

    """
    #-Student first_name getter
    @returns first name of student @Type = Str
    """
    def get_first_name(self):
        return self.__first_name

    """
    #-Student last_name getter
    @returns last name of student @Type = Str
    """
    def get_last_name(self):
        return self.__last_name

    """
    #-Student date of birth getter
    @returns students date of birth @Type = Str
    """
    def get_date_of_birth(self):
        return self.__date_of_birth

    """
    #-Student country of birth getter
    @returns students country of birth @Type = Str
    """
    def get_country_of_birth(self):
        return self.__country_of_birth

    """
    #-Student sex getter
    @returns students sex @Type = Str
    """
    def get_sex(self):
        return self.__sex

    """
    #-Student age getter
    @returns students age @Type = Str
    """
    def get_age(self):
        return datetime.date.today().year - __date_of_birth.date.year

    #-------------------------#
    # Setter Methods Section  #
    #-------------------------#
    """
    #-Student number setter
    @param student_number = passed student number @Type = Str
    """
    def set_student_number(self, student_number):
        self.__student_number = student_number

    """
    #-Student first_name setter
    @param first_name = passed student first_name @Type = Str
    """
    def set_first_name(self, first_name):
        self.__first_name = first_name

    """
    #-Student last_name setter
    @param last_name = passed student last_name @Type = Str
    """
    def set_last_name(self, last_name):
        self.__last_name = last_name

    """
    #-Student date_of_birth setter
    @param date_of_birth = passed student date_of_birth @Type = Str
    """
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    """
    #-Student country_of_birth setter
    @param country_of_birth = passed student country_of_birth @Type = Str
    """
    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth

    """
    #-Student sex setter
    @param sex = passed student sex @Type = Str
    """
    def set_sex(self, sex):
        self.sex = sex


if __name__ == "__main__":
    main()
