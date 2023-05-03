#include "c-vars.c"
int main() {
    int* intData = (int*)(data);
    int intAry[varCount/2];
    for(int ii = 0;ii<1024;ii++) {
        for(int i = 0;i<varCount;i+=2) {
            intAry[i/2] = intData[i] + intData[i+1];
        }
    }
}