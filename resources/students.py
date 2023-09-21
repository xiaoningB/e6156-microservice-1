import json
import os


class StudentsResource:
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    students_file = os.path.join(os.path.dirname(__file__), "old-students.json")

    def __init__(self):
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def get_students(self):
        return self.students
