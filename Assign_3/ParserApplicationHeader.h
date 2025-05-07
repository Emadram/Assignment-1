#ifndef PARSERAPPLICATION_H
#define PARSERAPPLICATION_H


//Librarie
#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

// Global variables
extern bool ERROR;
extern char NEXT_TOKEN;
extern std::ifstream INPUT_FILE;

// Function prototypes
void LEX();
std::string UNCONSUMED_INPUT();
void G();
void E();
void R();
void T();
void S();
void F();
void N();


#endif // PARSERAPPLICATION_H
