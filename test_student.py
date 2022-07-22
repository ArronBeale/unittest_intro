import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('john', 'Doe')

        self.assertEqual(student.full_name, 'john Doe')


    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()
        self.assertTrue(student.naughty_list)


if __name__ == '__main__':
    unittest.main()
