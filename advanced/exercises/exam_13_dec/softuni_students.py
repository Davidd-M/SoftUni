def softuni_students(*args, **courses):
    # Dictionary to store student information grouped by courses
    course_students = {}
    invalid_students = []

    # Process positional arguments (students)
    for student_id, user_name in args:
        # Check if the course for the student ID exists in the courses dictionary
        if student_id in courses:
            # Get the course name for the student ID
            course_name = courses[student_id]
            # Check if the course exists in the course_students dictionary
            if course_name not in course_students:
                # If the course doesn't exist, initialize it with an empty list
                course_students[course_name] = []
            # Add student information to the list under the corresponding course
            course_students[course_name].append({'student_id': student_id, 'user_name': user_name})
        else:
            # If the course for the student ID doesn't exist, add it to the list of invalid students
            invalid_students.append(user_name)

    # Sort courses based on the usernames of the students enrolled in each course
    sorted_courses = sorted(course_students.items(), key=lambda x: sorted([student['user_name'] for student in x[1]]))

    # Prepare the result string
    result = ''
    for course_name, students_info in sorted_courses:
        # Print usernames first, sorted alphabetically
        usernames = sorted([student['user_name'] for student in students_info])
        for username in usernames:
            result += f"*** A student with the username {username} has successfully finished the course {course_name}!\n"

    # Sort the list of invalid students alphabetically
    invalid_students.sort()
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(invalid_students)}\n"

    return result


import unittest


class SoftUniStudentsTestCase(unittest.TestCase):
    def test_multiple_students_valid_invalid_with_sorting(self):
        student_data = [
            ('id_1', 'John'),
            ('id_3', 'Bob'),
            ('id_4', 'Eve'),
            ('id_2', 'Alice'),
            ('id_43', 'Chris'),
            ('id_12', 'Mariya'),
        ]
        course_data = {
            'id_1': 'Course 1',
            'id_3': 'Course 2',
            'id_12': 'Course 3',
        }

        result = softuni_students(*student_data, **course_data)
        expected_output = '''*** A student with the username Bob has successfully finished the course Course 2!
*** A student with the username John has successfully finished the course Course 1!
*** A student with the username Mariya has successfully finished the course Course 3!
!!! Invalid course students: Alice, Chris, Eve'''

        self.assertEqual(result.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()