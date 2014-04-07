#include <iostream>
#include "registers.h"
#include "misc.h"

int zx = 0;

void mfhi(){
    Registers mreg1;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "mfhi";
    for(zx=0;zx<8;zx++){
        mreg1.rdest[zx] = mreg1.hi[zx];
    }
    mreg1.regvals();
    mreg1.Update();
}

void mflo(){
    Registers mreg2;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "mflo";
    for(zx=0;zx<8;zx++){
        mreg2.rdest[zx] = mreg2.lo[zx];
    }
    mreg2.regvals();
    mreg2.Update();
}

void mthi(){
    Registers mreg3;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "mthi";
    for(zx=0;zx<8;zx++){
        mreg3.hi[zx] = mreg3.rdest[zx];
    }
    mreg3.regvals();
    mreg3.Update();
}

void mtlo(){
    Registers mreg4;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "mtlo";
    for(zx=0;zx<8;zx++){
        mreg4.lo[zx] = mreg4.rdest[zx];
    }
    mreg4.regvals();
    mreg4.Update();
}
