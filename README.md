MIPS-I Digital Logic
==================
The goal of this project is to make a (somewhat) accurate recreation of the digital logic used in the 1985 MIPS-I architecture, and create a full MIPS-I CPU. I am basing the all of the digital logic off of the instruction set for the architecture found at http://www.ece.umd.edu/~manoj/759M/MIPSALM.html

The 'circuits' directory will contain the bulk of the work, .circ files, which can be opened in Logisim (http://ozark.hendrix.edu/~burch/logisim/) in order to view the designs, which is included in the 'tools' directory.

Also included in this repo is a MIPS assembly compiler which can compile assembly written for the MIPS processor into a binary format that is compatible with the CPU. This compiler will also be able to compile the assembly into a file format which is readable by Logisim which allows user written assembly to be run on the CPU from ROM.

This project will likely contain unoptimized and possibly redundant digital logic which may or may not be fixed at a later date. Since this is a homebrew design, I may or may not choose to include new instructions.
