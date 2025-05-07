#ifndef PARSERAPPLICATIONHEADER_H
#define PARSERAPPLICATIONHEADER_H

//Libraries
#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

// Global variables
extern bool Error;
extern char NextToken;
extern std::ifstream InputFile;

// Function prototypes
void LEX();
std::string RemainingInput();
void G();
void E();
void R();
void T();
void S();
void F();
void N();
void InitializeParser(const std::string& filename);

#endif // PARSERAPPLICATIONHEADER_H
//-----------------------------------//