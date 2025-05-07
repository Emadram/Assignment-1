#include "ParserApplicationHeader.h"

// Lexical analyzer - gets the next character from the file
void Lex();

// For Returns the remaining input in the file
std::string RemainingInput() {
    std::string remaining = "";
    char c;
    
    // Save the current position
    std::streampos CurrentP = InputFile.tellg();
    
    // Read the rest of the file
    while (InputFile.get(c))
        remaining += c;
    
    // Reset the file pointer to where it was
    InputFile.clear(); // Clear any EOF flags
    InputFile.seekg(currentP);
    
    return remaining;
}

// G → E TODO
void G();

// N → a | b | c | d TODO
void N();

// F → (E) | N TODO
void F();
