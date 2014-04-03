#include "registers.h"
#include <iostream>
using namespace std;

Registers::Registers(){
    for(int n=0;n<8;n++){pipe[n]=false;}
    for(int n=0;n<16;n++){imm[n]=false;}
    for(int n=0;n<8;n++){rsrc1[n]=false;}
    for(int n=0;n<8;n++){rsrc2[n]=false;}
    for(int n=0;n<8;n++){rdest[n]=false;}
    for(int n=0;n<8;n++){lo[n]=false;}
    for(int n=0;n<8;n++){hi[n]=false;}
}
