#include "registers.h"
#include <iostream>

Registers reg;

int construct(){
    for(int n=0;n<8;n++){reg.pipe[n]=false;}
    for(int n=0;n<16;n++){reg.imm[n]=false;}
    for(int n=0;n<8;n++){reg.rsrc1[n]=false;}
    for(int n=0;n<8;n++){reg.rsrc2[n]=false;}
    for(int n=0;n<8;n++){reg.rdest[n]=false;}
    for(int n=0;n<8;n++){reg.lo[n]=false;}
    for(int n=0;n<8;n++){reg.hi[n]=false;}
    return 0;
}
