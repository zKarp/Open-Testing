import unittest

from main import start


class TestLikes(unittest.TestCase):
    def test_name_initializaiton(self):
        """
        Test that it can sum a list of integers
        """
        result = start('Zach')
        self.assertEqual('Zach', result.name)
    
    def test_name_initializaiton_no_var(self):
        """
        Test that it can sum a list of integers
        """
        result = start()
        self.assertEqual('Test', result.name)

    def test_returns_B(self):
        results = start().ReturnsB()
        self.assertEqual('A',results)



if __name__ == '__main__':
    unittest.main()