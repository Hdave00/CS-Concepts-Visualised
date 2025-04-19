#include <stdio.h>
#include <string.h>

// set buffer size/limit of output chars  
char output[256];

// set a constant variable, which will be a string of output, wich takes as argument a string input, and prints it out, after the value
// is passed to the flask template
const char* process_input(const char* input) {
    snprintf(output, sizeof(output), "%s", input);
    return output;
}