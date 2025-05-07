#include "ParserApplicationHeader.h"
#include <cctype>   // std::isspace
#include <fstream>  // file handling

// Lexical analyzer - gets the next character from the file
void LEX() {
    char c;
    
    // Skip whitespace
    do {
        if (!InputFile.get(c)) {
            // End of file or error
            NextToken = '$';
            return;
        }
    } while (std::isspace(c));
    
    NextToken = c;
}

// Returns the remaining input in the file
std::string RemainingInput() {
    std::string remaining = "";
    char c;
    
    // Save the current position
    std::streampos currentPos = InputFile.tellg();
    
    // Read the rest of the file
    while (InputFile.get(c)) {
        remaining += c;
    }
    
    // Reset the file pointer to where it was
    InputFile.clear(); // Clear any EOF flags
    InputFile.seekg(currentPos);
    
    return remaining;
}


// G → E
void G() {
    LEX();
    std::cout << "G -> E" << std::endl;
    E();
    
    if (NextToken == '$' && !Error) {
        std::cout << "success" << std::endl;
    } else {
        std::cout << "failure: unconsumed input=" << RemainingInput() << std::endl;
    }
}

// N → a | b | c | d
void N() {
    if (Error) return;
    
    if (NextToken == 'a' || NextToken == 'b' || NextToken == 'c' || NextToken == 'd') {
        std::cout << "N -> " << NextToken << std::endl;
        LEX();
    } else {
        Error = true;
        std::cout << "error: unexpected token " << NextToken << std::endl;
        std::cout << "unconsumed input: " << RemainingInput() << std::endl;
    }
}

// F → (E) | N
void F() {
    if (Error) return;
    
    if (NextToken == '(') {
        std::cout << "F -> ( E )" << std::endl;
        LEX();
        E();
        
        if (NextToken == ')') {
            LEX();
        } else {
            Error = true;
            std::cout << "error: unexpected token " << NextToken << std::endl;
            std::cout << "unconsumed input: " << RemainingInput() << std::endl;
        }
    } else if (NextToken == 'a' || NextToken == 'b' || NextToken == 'c' || NextToken == 'd') {
        std::cout << "F -> N" << std::endl;
        N();
    } else {
        Error = true;
        std::cout << "error: unexpected token " << NextToken << std::endl;
        std::cout << "unconsumed input: " << RemainingInput() << std::endl;
    }
}

void InitializeParser(const std::string& filename) {
    // Open the input file
    InputFile.open(filename);

    if (!InputFile.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    // Call the main parsing function
    G();
    
    // Close the file after processing
    InputFile.close();
}
