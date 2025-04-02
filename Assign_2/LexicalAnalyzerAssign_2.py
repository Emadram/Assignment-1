import re

class TokenBuffer:
    """
    TokenBuffer is the class that stores token's type and value
    @param token_type = type of token can be (INTEGER, FLOAT, ID, BITWISE_OR, LOGICAL_OR, BITWISE_AND, LOGICAL_AND, ERROR)
    @param token_value = given token value
    """
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value

    def __str__(self):
        # return format = <type, value>
        return f"<{self.token_type}, {self.token_value}>"

class TokenLexicalAnalyzer:
    """
    Reads inputs from file and breaks the text into tokens
    @param file_name given file name
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None  # File reference
        self.buffer = ""  # File content buffer
        self.pointer_position = 0  # Pointer for traversal
        self.symbol_buffer = []  # Symbol table

    def openFile(self):
        """Opens the input file and reads its contents into a buffer."""
        try:
            self.file = open(self.file_name, 'r')
            self.buffer = self.file.read()
            return True
        except FileNotFoundError:
            print(f"Error: No such file found {self.file_name}")
            return False

    def closeFile(self):
        """Closes the input file if it's open."""
        if self.file:
            self.file.close()

    def ignoreWhiteSpace(self):
        """Moves the pointer past whitespace characters."""
        while self.pointer_position < len(self.buffer) and self.buffer[self.pointer_position].isspace():
            self.pointer_position += 1

    def lex(self):
        """Processes the next token in the buffer."""
        self.ignoreWhiteSpace()
        if self.pointer_position >= len(self.buffer):
            return None
        
        char = self.buffer[self.pointer_position]
        
        if char.isdigit() or (char == '-' and self.pointer_position + 1 < len(self.buffer) and self.buffer[self.pointer_position + 1].isdigit()):
            return self.checkNumber()
        elif char.isalpha() or char == '_':
            return self.checkIdentifier()
        elif char == '&':
            return self.checkAnd()
        elif char == '|':
            return self.checkOr()
        else:
            self.pointer_position += 1
            return TokenBuffer("ERROR", f'Unrecognized token: {char}')
    
    def checkNumber(self):
        """Extracts an integer or floating point number from the buffer."""
        num_pattern = re.compile(r'-?\d+\.?\d*')
        match = num_pattern.match(self.buffer, self.pointer_position)
        if match:
            num_str = match.group()
            temp_position = self.pointer_position + len(num_str)
            # Check if the number is followed by letters (invalid token)
            invalid_pattern = re.compile(r'-?\d+\.?\d*[a-zA-Z]+')
            invalid_match = invalid_pattern.match(self.buffer, self.pointer_position)
            if invalid_match:
                invalid_token = invalid_match.group()
                self.pointer_position += len(invalid_token)
                return TokenBuffer("ERROR", f'"{invalid_token}"')
            # Valid number
            self.pointer_position = temp_position
            if '.' in num_str:
                return TokenBuffer("FLOAT", float(num_str))
            return TokenBuffer("INTEGER", int(num_str))
        return TokenBuffer("ERROR", "Invalid number format")
    
    def checkIdentifier(self):
        """Extracts an identifier from the buffer."""
        id_pattern = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        match = id_pattern.match(self.buffer, self.pointer_position)
        if match:
            identifier = match.group()
            self.pointer_position += len(identifier)
            if identifier not in self.symbol_buffer:
                self.symbol_buffer.append(identifier)
            return TokenBuffer("ID", self.symbol_buffer.index(identifier))
        return TokenBuffer("ERROR", "Invalid identifier format")
    
    def checkAnd(self):
        """Handles bitwise and logical AND operators."""
        if self.pointer_position + 1 < len(self.buffer) and self.buffer[self.pointer_position + 1] == '&':
            self.pointer_position += 2
            return TokenBuffer("LOGICAL_AND", "nothing")
        self.pointer_position += 1
        return TokenBuffer("BITWISE_AND", "nothing")
    
    def checkOr(self):
        """Handles bitwise and logical OR operators."""
        if self.pointer_position + 1 < len(self.buffer) and self.buffer[self.pointer_position + 1] == '|':
            self.pointer_position += 2
            return TokenBuffer("LOGICAL_OR", "nothing")
        self.pointer_position += 1
        return TokenBuffer("BITWISE_OR", "nothing")
    
    def getSymbolBuffer(self):
        """Returns the symbol table."""
        return self.symbol_buffer

def main():
#TODO BY BESTE

if __name__ == "__main__":
    main()
