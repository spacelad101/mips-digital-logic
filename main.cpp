#include <iostream>
#include <vector>
#include <windows.h>
#include "registers.h"

using namespace std;

//general vars
int n = 0;
int x = 0;
int temp = 0;

/*
//declare registers
bool pipe[8] = {false};
bool imm[16] = {false};
bool rsrc1[8] = {false};
bool rsrc2[8] = {false};
bool rdest[8] = {false};
bool lo[8] = {false};
bool hi[8] = {false};*/

//declare zeroed memory bank
bool memory [256][256];

//memory address
//2 address registers to control vertical and horizontal position of memory
bool address_r1[4] = {true, false, false, true};
bool address_r2[4] = {true, false, false, true};

// vars for binary memory address' converted to decimal
int int_address_r1 = 0;
int int_address_r2 = 0;

void regvals(){
    Registers reg;
    cout << endl << "\tPipe: \t\t";
    for(n=0;n<8;n++){cout << reg.pipe[n];}
    cout << endl << "\tImm: \t";
    for(n=0;n<16;n++){cout << reg.imm[n];}
    cout << endl << "\tRsrc1: \t\t";
    for(n=0;n<8;n++){cout << reg.rsrc1[n];}
    cout << endl << "\tRsrc2: \t\t";
    for(n=0;n<8;n++){cout << reg.rsrc2[n];}
    cout << endl << "\tRdest: \t\t";
    for(n=0;n<8;n++){cout << reg.rdest[n];}
    cout << endl << "\tHi: \t\t";
    for(n=0;n<8;n++){cout << reg.hi[n];}
    cout << endl << "\tLo: \t\t";
    for(n=0;n<8;n++){cout << reg.lo[n];}
    cout << endl;
    Sleep (500);
}

void op_and(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "and";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == reg.rsrc2[n])&&(reg.rsrc1[n] == true)){
            reg.rdest[n] = reg.rsrc1[n];
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_andi(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "andi";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == reg.imm[n+8])&&(reg.rsrc1[n] == true)){
            reg.rdest[n] = reg.rsrc1[n];
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_nand(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nand";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] != reg.rsrc2[n])||((reg.rsrc1[n] == false)&&(reg.rsrc2[n] == false))){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_nandi(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nandi" << endl << "------";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] != reg.rsrc2[n])||((reg.rsrc1[n] == false)&&(reg.rsrc2[n] == false))){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_or(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "or" << endl << "------";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == true)||(reg.rsrc2[n] == true)){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_ori(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "ori" << endl << "------";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == true)||(reg.imm[n+8] == true)){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_nor(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nor" << endl << "------";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == true)||(reg.rsrc2[n] == true)){
            reg.rdest[n] = false;
        } else{
            reg.rdest[n] = true;
        }
    }
    regvals();
}

void op_nori(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nori" << endl << "------";
    for(n=0; n<8; n++){
        if((reg.rsrc1[n] == true)||(reg.imm[n+8] == true)){
            reg.rdest[n] = false;
        } else{
            reg.rdest[n] = true;
        }
    }
    regvals();
}

void op_xor(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xor" << endl << "------";
    for(n=0; n<8; n++){
        if(reg.rsrc1[n] != reg.rsrc2[n]){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_xori(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xori" << endl << "------";
    for(n=0; n<8; n++){
        if(reg.rsrc1[n] != reg.imm[n+8]){
            reg.rdest[n] = true;
        } else{
            reg.rdest[n] = false;
        }
    }
    regvals();
}

void op_xnor(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xnor" << endl << "------";
    for(n=0; n<8; n++){
        if(reg.rsrc1[n] != reg.rsrc2[n]){
            reg.rdest[n] = false;
        } else{
            reg.rdest[n] = true;
        }
    }
    regvals();
}

void op_xnori(){
    Registers reg;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xnori" << endl << "------";
    for(n=0; n<8; n++){
        if(reg.rsrc1[n] != reg.imm[n+8]){
            reg.rdest[n] = false;
        } else{
            reg.rdest[n] = true;
        }
    }
    regvals();
}

int main(){
    cout << "          _____                   _____                   _____                   _____          ";
    cout << endl << "         /\\    \\                 /\\    \\                 /\\    \\                 /\\    \\         ";
    cout << endl << "        /::\\____\\               /::\\    \\               /::\\    \\               /::\\    \\        ";
    cout << endl << "       /::::|   |               \\:::\\    \\             /::::\\    \\             /::::\\    \\       ";
    cout << endl << "      /:::::|   |                \\:::\\    \\           /::::::\\    \\           /::::::\\    \\      ";
    cout << endl << "     /::::::|   |                 \\:::\\    \\         /:::/\\:::\\    \\         /:::/\\:::\\    \\     ";
    cout << endl << "    /:::/|::|   |                  \\:::\\    \\       /:::/__\\:::\\    \\       /:::/__\\:::\\    \\    ";
    cout << endl << "   /:::/ |::|   |                  /::::\\    \\     /::::\\   \\:::\\    \\      \\:::\\   \\:::\\    \\   ";
    cout << endl << "  /:::/  |::|___|______   ____    /::::::\\    \\   /::::::\\   \\:::\\    \\   ___\\:::\\   \\:::\\    \\  ";
    cout << endl << " /:::/   |::::::::\\    \\ /\\   \\  /:::/\\:::\\    \\ /:::/\\:::\\   \\:::\\____\\ /\\   \\:::\\   \\:::\\    \\ ";
    cout << endl << "/:::/    |:::::::::\\____/::\\   \\/:::/  \\:::\\____/:::/  \\:::\\   \\:::|    /::\\   \\:::\\   \\:::\\____\\";
    cout << endl << "\\::/    / ~~~~~/:::/    \\:::\\  /:::/    \\::/    \\::/    \\:::\\  /:::|____\\:::\\   \\:::\\   \\::/    /";
    cout << endl << " \\/____/      /:::/    / \\:::\\/:::/    / \\/____/ \\/_____/\\:::\\/:::/    / \\:::\\   \\:::\\   \\/____/ ";
    cout << endl << "             /:::/    /   \\::::::/    /                   \\::::::/    /   \\:::\\   \\:::\\    \\     ";
    cout << endl << "            /:::/    /     \\::::/____/                     \\::::/    /     \\:::\\   \\:::\\____\\    ";
    cout << endl << "           /:::/    /       \\:::\\    \\                      \\::/____/       \\:::\\  /:::/    /    ";
    cout << endl << "          /:::/    /         \\:::\\    \\                      ~~              \\:::\\/:::/    /     ";
    cout << endl << "         /:::/    /           \\:::\\    \\                                      \\::::::/    /      ";
    cout << endl << "        /:::/    /             \\:::\\____\\                                      \\::::/    /       ";
    cout << endl << "        \\::/    /               \\::/    /                                       \\::/    /        ";
    cout << endl << "         \\/____/                 \\/____/                                         \\/____/         ";
    cout << endl << "                                                                                                 " << endl;
    Sleep (1000);
    cout << endl << "/* MIPS-I Emulator Started /*" << endl << "-----------------------------" << endl << "-----------------------------" << endl;
    op_and();
    op_andi();
    op_nand();
    op_nandi();
    op_or();
    op_ori();
    op_nor();
    op_nori();
    op_xor();
    op_xori();
    op_xnor();
    op_xnori();
    while(true){
        //when all of the operations are finished, run everything in here
        return false;
    }
    return 0;
}
