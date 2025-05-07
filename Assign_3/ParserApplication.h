#ifndef PARSERAPPLICATION_H
#define PARSERAPPLICATION_H


//Librarie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// Global variables
extern bool ERROR;
extern char NEXT_TOKEN;
extern FILE* INPUT_FILE;

// Function prototypes
void LEX();
char* UNCONSUMED_INPUT();
void G();
void E();
void R();
void T();
void S();
void F();
void N();

#endif // PARSERAPPLICATION_H
