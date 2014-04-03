#ifndef REGISTERS_H
#define REGISTERS_H
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
};
Registers::Registers(){
    for(int n=0;n<8;n++){pipe[n]=false;}
    for(int n=0;n<16;n++){imm[n]=false;}
    for(int n=0;n<8;n++){rsrc1[n]=false;}
    for(int n=0;n<8;n++){rsrc2[n]=false;}
    for(int n=0;n<8;n++){rdest[n]=false;}
    for(int n=0;n<8;n++){lo[n]=false;}
    for(int n=0;n<8;n++){hi[n]=false;}
}
#endif
