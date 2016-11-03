import unittest
from app.calculator import Calculator

class TddInPyhton(unittest.TestCase):

	def test_calculator_add_method_return_correct_result(self):
		calc = Calculator()
		result = calc.add(2,2)
		self.assertEqual(4,result)

if __name__ == '__main__':
	unittest.main()