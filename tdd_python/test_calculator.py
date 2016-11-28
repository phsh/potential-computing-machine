import unittest
from app.calculator import Calculator

class TddInPyhton(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()
		self.values = range(10)

	def test_add_method_return_correct_result(self):		
		result = self.calc.add(2,2)
		self.assertEqual(4,result)

	def test_sub_method_return_correct_result(self):		
		result = self.calc.sub(4,2)
		self.assertEqual(2,result)

	def test_multy_return_correct_result(self):
		result = self.calc.multy(2,3)
		self.assertEqual(6,result)

	def test_divi_return_correct_result(self):
		result = self.calc.divi(6,3)		
		self.assertEqual(2,result)

	def test_isLegal_add_random(self):
		result = self.calc.isLegal("add")		
		self.assertTrue(result)

	def test_isLegal_addSign_random(self):
		result = self.calc.isLegal("+")
		self.assertTrue(result)

	def test_isLegal_sub_true(self):
		result = self.calc.isLegal("sub")		
		self.assertTrue(result)

	def test_isLegal_divi_true(self):
		result = self.calc.isLegal("divi")		
		self.assertTrue(result)

	def test_isLegal_multy_true(self):
		result = self.calc.isLegal("multy")		
		self.assertTrue(result)
	
	def test_isLegal_random_false(self):
		result = self.calc.isLegal("false")		
		self.assertFalse(result)

	def test_divi_return_error_result(self):
		self.assertRaises(ValueError, self.calc.cantBeZero, 0)
		self.assertRaises(ValueError, self.calc.divi,5,0)

	def test_error_message(self):
		self.assertRaises(ValueError, self.calc.validateNumber, 'two','three')
		self.assertRaises(ValueError, self.calc.validateNumber, 1	,'three')
		self.assertRaises(ValueError, self.calc.validateNumber, '1'	,'three')
		self.assertRaises(ValueError, self.calc.validateNumber, '1'	,'6')
	
	def test_none_error_message(self):
		try:
			self.calc.validateNumber(2,3)
			self.calc.validateNumber(0,3)
			self.calc.validateNumber(0,0)
		except ValueError:			
			self.fail("validateNumber() raised ValueError unexpectedly!")
   	

if __name__ == '__main__':
	unittest.main()