
class TokenBuffer:

	def __init__(self, token_type, token_value):
		self.token_type = token_type
		self.token_value = token_value


	def __str__(self):
		return f"<{self.token_type}, {self.value}>"


class TokenLexicalAnalyzer:

	def __init__(self, file_name):
		self.file_name = file_name
		self.file = None #Default value of file
		self.buffer = "" #Default value of buffer
		self.pointer_position = 0 #Default place for the pointer to look at in the file
  		self.symbol_buffer = []