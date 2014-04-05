#include <iostream>
#include <windows.h>
#include "registers.h"
#include "logic.h"

int zz = 0;

Registers reg;

void op_and(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "and";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == reg.rsrc2[zz])&&(reg.rsrc1[zz] == true)){
            reg.rdest[zz] = reg.rsrc1[zz];
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_andi(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "andi";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == reg.imm[zz+8])&&(reg.rsrc1[zz] == true)){
            reg.rdest[zz] = reg.rsrc1[zz];
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_nand(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nand";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] != reg.rsrc2[zz])||((reg.rsrc1[zz] == false)&&(reg.rsrc2[zz] == false))){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_nandi(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nandi" << endl << "------";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] != reg.rsrc2[zz])||((reg.rsrc1[zz] == false)&&(reg.rsrc2[zz] == false))){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_or(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "or" << endl << "------";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == true)||(reg.rsrc2[zz] == true)){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_ori(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "ori" << endl << "------";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == true)||(reg.imm[zz+8] == true)){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_nor(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nor" << endl << "------";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == true)||(reg.rsrc2[zz] == true)){
            reg.rdest[zz] = false;
        } else{
            reg.rdest[zz] = true;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_nori(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "nori" << endl << "------";
    for(zz=0; zz<8; zz++){
        if((reg.rsrc1[zz] == true)||(reg.imm[zz+8] == true)){
            reg.rdest[zz] = false;
        } else{
            reg.rdest[zz] = true;
        }reg.Update();
    }
    reg.regvals();
    reg.Update();
}

void op_xor(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xor" << endl << "------";
    for(zz=0; zz<8; zz++){
        if(reg.rsrc1[zz] != reg.rsrc2[zz]){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_xori(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xori" << endl << "------";
    for(zz=0; zz<8; zz++){
        if(reg.rsrc1[zz] != reg.imm[zz+8]){
            reg.rdest[zz] = true;
        } else{
            reg.rdest[zz] = false;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_xnor(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xnor" << endl << "------";
    for(zz=0; zz<8; zz++){
        if(reg.rsrc1[zz] != reg.rsrc2[zz]){
            reg.rdest[zz] = false;
        } else{
            reg.rdest[zz] = true;
        }
    }
    reg.regvals();
    reg.Update();
}

void op_xnori(){
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "xnori" << endl << "------";
    for(zz=0; zz<8; zz++){
        if(reg.rsrc1[zz] != reg.imm[zz+8]){
            reg.rdest[zz] = false;
        } else{
            reg.rdest[zz] = true;
        }
    }
    reg.regvals();
    reg.Update();
}
