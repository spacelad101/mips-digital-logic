#include <iostream>
#include <windows.h>
#include "registers.h"
#include "logic.h"
#include "arithmetic.h"
#include "misc.h"

using namespace std;

//declare zeroed memory bank
bool memory [256][256];

//memory address
//2 address registers to control vertical and horizontal position of memory
bool address_r1[4] = {true, false, false, true};
bool address_r2[4] = {true, false, false, true};

// vars for binary memory address' converted to decimal
int int_address_r1 = 0;
int int_address_r2 = 0;

Registers regz;

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
    while(true){
        //when all of the operations are finished, run everything in here
        cout << "Nothing left to do!";
        return false;
    }
    return 0;
}
