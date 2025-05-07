#include "ParserApplicationHeader.h"


bool Error = false;
char NextToken = '%';
std::ifstream InputFile;

int main() {
    std::string FilePath;
    
    // Get file path from user
    std::cout << "Enter the input file path: ";
    std::cin >> FilePath;
    
    // Open the file
    InputFile.open(FilePath);
    
    if (!InputFile.is_open()) {
        std::cout << "Error: Unable to open file." << std::endl;
        return 1;
    }
    
    // Start parsing
    G();
    
    // Close the file
    InputFile.close();
    
    return 0;
}
