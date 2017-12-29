
import {{cookiecutter.package_name}}
import unittest


class BasicTestCase(unittest.TestCase):
    ''' Basic test cases '''

    def test_basic(self):
        ''' check True is True '''
        self.assertTrue(True)

    def test_version(self):
        ''' check {{cookiecutter.package_name}} exposes a version attribute '''
        self.assertTrue(hasattr({{cookiecutter.package_name}}, '__version__'))
        self.assertIsInstance({{cookiecutter.package_name}}.__version__, str)


if __name__ == '__main__':
    unittest.main()
