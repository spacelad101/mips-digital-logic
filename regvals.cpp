#include <iostream>
#include <windows.h>
#include "registers.h"

using namespace std;

int n1 = 0;

void regvals(){
    Registers reg;
    cout << endl << "\tPipe: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.pipe[n1];}
    cout << endl << "\tImm: \t";
    for(n1=0;n1<16;n1++){cout << reg.imm[n1];}
    cout << endl << "\tRsrc1: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.rsrc1[n1];}
    cout << endl << "\tRsrc2: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.rsrc2[n1];}
    cout << endl << "\tRdest: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.rdest[n1];}
    cout << endl << "\tHi: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.hi[n1];}
    cout << endl << "\tLo: \t\t";
    for(n1=0;n1<8;n1++){cout << reg.lo[n1];}
    cout << endl;
    Sleep (500);
}
