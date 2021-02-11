import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data import RegisterMultipleCoursesTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterMultipleCoursesTests)

smoketest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoketest)