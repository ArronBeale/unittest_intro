import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('john', 'Doe')

        self.assertEqual(student.full_name, 'john Doe')


if __name__ == '__main__':
    unittest.main()
