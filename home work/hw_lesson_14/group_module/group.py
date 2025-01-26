from .group_limit_reached_exception import GroupLimitReachedException

class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"Group limit {self.student_limit} reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if Group.find_student(self, last_name):
                self.group.remove(student)
                break

    def find_student(self, last_name):
        for student in self.group:
            if last_name in student.last_name:
                return student

    def __str__(self):
        all_students = ''
        for numbers in self.group:
            all_students += f'\n{numbers.last_name}'
        return f'Number:{self.number} {all_students} '
