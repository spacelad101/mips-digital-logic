#include "registers.h"
#include <iostream>

bool initial = true;

bool t_pipe[8] = {false};
bool t_imm[16] = {false};
bool t_rsrc1[8] = {false};
bool t_rsrc2[8] = {false};
bool t_rdest[8] = {false};
bool t_lo[8] = {false};
bool t_hi[8] = {false};

Registers::Registers(){
    if(initial == true){
        for(int n=0;n<8;n++){pipe[n]=false;}
        for(int n=0;n<16;n++){imm[n]=false;}
        for(int n=0;n<8;n++){rsrc1[n]=false;}
        for(int n=0;n<8;n++){rsrc2[n]=false;}
        for(int n=0;n<8;n++){rdest[n]=false;}
        for(int n=0;n<8;n++){lo[n]=false;}
        for(int n=0;n<8;n++){hi[n]=false;}
        initial = false;
    } else{
        for(int n=0;n<8;n++){pipe[n]=t_pipe[n];}
        for(int n=0;n<16;n++){imm[n]=t_imm[n];}
        for(int n=0;n<8;n++){rsrc1[n]=t_rsrc1[n];}
        for(int n=0;n<8;n++){rsrc2[n]=t_rsrc2[n];}
        for(int n=0;n<8;n++){rdest[n]=t_rdest[n];}
        for(int n=0;n<8;n++){lo[n]=t_lo[n];}
        for(int n=0;n<8;n++){hi[n]=t_hi[n];}
    }
}

void Registers::Update(){
    for(int n=0;n<8;n++){t_pipe[n]=pipe[n];}
    for(int n=0;n<16;n++){t_imm[n]=imm[n];}
    for(int n=0;n<8;n++){t_rsrc1[n]=rsrc1[n];}
    for(int n=0;n<8;n++){t_rsrc2[n]=rsrc2[n];}
    for(int n=0;n<8;n++){t_rdest[n]=rdest[n];}
    for(int n=0;n<8;n++){t_lo[n]=lo[n];}
    for(int n=0;n<8;n++){t_hi[n]=hi[n];}
}
