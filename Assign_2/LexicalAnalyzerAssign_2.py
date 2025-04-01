
class TokenBuffer:

	def __init__(self, token_type, token_value):
		self.token_type = token_type
		self.token_value = token_value


	def __str__(self):
		return f"<{self.token_type}, {self.value}>"


class TokenLexicalAnalyzer:

	def __init__(self, file_name):
		self.file_name = file_name
		self.file = None #Init value of file
		self.buffer = "" #Init value of buffer
		self.pointer_position = 0 #Init place for the pointer to look at in the file
  		self.symbol_buffer = [] #Init of symbol buffer


  	def openFile(self):

  		try:
  			self.file = open(self.file_name, 'r')
  			self.buffer = self.file.read()
  			return True

  		except FileNotFoundError:
  			print(f"Error: No such File found {self.file_name}")
  			return False


  	def closeFile(self):

  		if self.file == True:
  			self.file.close()


  	def ignoreWhiteSpace(self):
  		while self.pointer_position < len(self.buffer) and self.buffer[self.pointer_position] == " ":
  			self.pointer_position += 1


  	#TODO def lex(self)

  	#TODO def checkNumber(self)

  	#TODO def checkIdentifier(self)

  	#TODO def checkAnd(self)

  	#TODO def checkOr(self)

  	#TODO def getSymbolBuffer



 def main():
 	yield #TODO
 	#USER INTERFACE AND INPUT CODE







if __name__ == "__main__":
	main()
