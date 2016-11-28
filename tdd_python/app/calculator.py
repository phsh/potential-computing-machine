class Calculator(object):
	number_types = (int, long, float, complex)	

	def validateNumber(self, *args):
		for x in args:
			if not ( isinstance(x, Calculator.number_types) ):
				errorMessage = "'" + str(x) + "' isn't a number";				
				raise ValueError (errorMessage)

	def cantBeZero(self, x):
		if (x == 0):
			errorMessage = "y can't be 0 (Zero)"
			raise ValueError (errorMessage)
		pass

	def add(self, x, y):		
		self.validateNumber( x, y )
		return x + y

	def sub(self, x,y):
		self.validateNumber( x, y )
		return x - y

	def multy(self,x,y):
		self.validateNumber( x, y )
		return x * y

	def divi(self, x, y):
		self.validateNumber( x, y )
		self.cantBeZero(y)
		return x / y
	def character(self, a_char):
		if a_char == "+":
			return "add"
		if a_char == "-":
			return "sub"
		return
	def legal(self):
		return [ "add", "sub", "multy", "divi", "+", "-" ,"/" ]

	def isLegal(self, s):
		return s in self.legal()