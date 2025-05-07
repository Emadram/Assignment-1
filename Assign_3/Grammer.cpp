#include "ParserApplicationHeader.h"

// E → T R
void E();

// R → + T R | - T R | ε
void R();

// T → F S
void T();

// S → * F S | / F S | ε
void S();
