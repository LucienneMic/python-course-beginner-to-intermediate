import unittest
from src.student import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()
        self.manager.add_student("Alice", {"Math":90,"English":80})
    def test_average(self):
        self.assertEqual(self.manager.get_average("Alice"),85)
    def test_remove(self):
        self.manager.remove_student("Alice")
        self.assertEqual(len(self.manager.students),0)

if __name__=="__main__":
    unittest.main()
