#ifndef REGISTERS_H
#define REGISTERS_H
#include <iostream>
#include <windows.h>
using namespace std;
class Registers{
    public:
        Registers();
        bool pipe[8];
        bool imm[16];
        bool rsrc1[8];
        bool rsrc2[8];
        bool rdest[8];
        bool lo[8];
        bool hi[8];

        int n1;
        void regvals(){
            cout << endl << "\tPipe: \t\t";
            for(n1=0;n1<8;n1++){cout << pipe[n1];}
            cout << endl << "\tImm: \t";
            for(n1=0;n1<16;n1++){cout << imm[n1];}
            cout << endl << "\tRsrc1: \t\t";
            for(n1=0;n1<8;n1++){cout << rsrc1[n1];}
            cout << endl << "\tRsrc2: \t\t";
            for(n1=0;n1<8;n1++){cout << rsrc2[n1];}
            cout << endl << "\tRdest: \t\t";
            for(n1=0;n1<8;n1++){cout << rdest[n1];}
            cout << endl << "\tHi: \t\t";
            for(n1=0;n1<8;n1++){cout << hi[n1];}
            cout << endl << "\tLo: \t\t";
            for(n1=0;n1<8;n1++){cout << lo[n1];}
            cout << endl;
            Sleep (500);
        }
};
#endif
