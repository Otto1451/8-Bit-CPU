# 8-Bit-CPU
This is simply a personal project where I used Logisim Evolution in order to build a CPU ground up from logic gates. The design is not supposed to be efficient or complex in any way, but to only serve as a learning experience for me.
The design uses 22 instructions, and has 6 registers including the CIR, MAR, MDR, ACC, B and the Stack Pointer. In the folder called "figures" I included all the circuits I've built along the way leading up to the CPU. 
However, some components such as the RAM I've built is too inconvenient to use due to the need to manually enter the address to read data, therefore, I used the RAM provided by Logisim Evolution for ease in debugging. Finally,
writing programs in binary would be tedious, therefore, I used python to build a simple "assembler" so that I don't have to remember specific codes for instructions. 
