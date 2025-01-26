from academy_module import Student
from group_module import Group, GroupLimitReachedException



def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Female', 25, 'Olivia', 'Whittle', 'AN145')
    st4 = Student('Female', 24, 'Amelia', 'Ferguson', 'AN145')
    st5 = Student('Female', 22, 'Ava', 'Wilkins', 'AN145')
    st6 = Student('Female', 23, 'Evelyn', 'Watson', 'AN145')
    st7 = Student('Male', 25, 'Liam', 'Gordon', 'AN145')
    st8 = Student('Male', 24, 'Oliver', 'Banks', 'AN145')
    st9 = Student('Male', 26, 'Henry', 'Thompson', 'AN145')
    st10 = Student('Male', 27, 'William', 'Smith', 'AN145')
    st11 = Student('Male', 28, 'Leo', 'Mcdaniel', 'AN145')

    gr = Group('PD1')

    try:
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        gr.add_student(st5)
        gr.add_student(st6)
        gr.add_student(st7)
        gr.add_student(st8)
        gr.add_student(st9)
        gr.add_student(st10)
        gr.add_student(st11)

    except GroupLimitReachedException as error:
        print(error)
    except Exception as error:
        print(error)

    print(gr)



if __name__ == '__main__':
    main()

# from test import show_data_from_test
#
# print(__name__)
# show_data_from_test()
