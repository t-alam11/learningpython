class Student:
    def __init__(self,name,id,grade=None):
        self.name = name
        self.id = id
        self.grade = grade if grade is not None else []




