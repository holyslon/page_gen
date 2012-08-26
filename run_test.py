from unittest import TestLoader, TextTestRunner

all_tests = TestLoader().discover("tests", "test_*.py", ".")
TextTestRunner().run(all_tests)
