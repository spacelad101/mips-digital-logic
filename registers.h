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
#endif
