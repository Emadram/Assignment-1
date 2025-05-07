#include "ParserApplicationHeader.h"

// Lexical analyzer - gets the next character from the file
void Lex();

// For Returns the remaining input in the file
std::string UnconsumedInput();

// G → E
void G();

// N → a | b | c | d
void N();

// F → (E) | N
void F();
