#include "ParserApplicationHeader.h"

// E → T R TODO
void E();

// R → + T R | - T R | ε TODO
void R();

// T → F S TODO
void T();

// S → * F S | / F S | ε TODO
void S();
