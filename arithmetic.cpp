#include <iostream>
#include <windows.h>
#include "registers.h"
#include "arithmetic.h"

int zy = 0;
bool sum[8] = {false};
bool carry[8] = {false};

void op_add(){
    Registers areg1;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "add";

    if((areg1.rsrc1[7] != areg1.rsrc2[7]) && (areg1.rsrc1[7] == true)){
        sum[7] = true;
    }
    if((areg1.rsrc1[7] == areg1.rsrc2[7]) && areg1.rsrc1[7] == true){
        carry[7] = true;
    }

    for(zy=6;zy>=0;zy--){
        if((areg1.rsrc1[zy] != areg1.rsrc2[zy]) && (areg1.rsrc1[zy] == true)){
            if((areg1.rsrc1[zy] != areg1.rsrc2[zy]) && (carry[zy+1] != true)){
                sum[zy] = true;
            }
            if(carry[zy+1] == true){
                carry[zy] = true;
            }
        } else if((areg1.rsrc1[zy] == areg1.rsrc2[zy]) && (carry[zy+1] == true)){
            sum[zy] = true;
        }
        if((areg1.rsrc1[zy] == areg1.rsrc2[zy]) && (areg1.rsrc1[zy] == true)){
            carry[zy] = true;
        }
    }

    for(zy=0;zy<8;zy++){
        areg1.rdest[zy] = sum[zy];
    }

    areg1.regvals();
    areg1.Update();
}
