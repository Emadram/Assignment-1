#include "ParserApplicationHeader.h"

// E → T R
void E() {
    if (Error) return;
    std::cout << "E -> T R" << std::endl;
    T();
    R();
}

// R → + T R | - T R | ε
void R() {
    if (Error) return;
    if (NextToken == '+') {
        std::cout << "R -> + T R" << std::endl;
        LEX();
        T();
        R();
    } else if (NextToken == '-') {
        std::cout << "R -> - T R" << std::endl;
        LEX();
        T();
        R();
    } else {
        std::cout << "R -> e" << std::endl;
    }
}

// T → F S
void T() {
    if (Error) return;
    std::cout << "T -> F S" << std::endl;
    F();
    S();
}

// S → * F S | / F S | ε
void S() {
    if (Error) return;
    if (NextToken == '*') {
        std::cout << "S -> * F S" << std::endl;
        LEX();
        F();
        S();
    } else if (NextToken == '/') {
        std::cout << "S -> / F S" << std::endl;
        LEX();
        F();
        S();
    } else {
        std::cout << "S -> e" << std::endl;
    }
}