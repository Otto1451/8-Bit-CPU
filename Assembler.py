# The format of the code with be: <OPCODE> <DESTINATION>, <SOURCE> 
# A stands for ACC, [address] is used to get data at that address in RAM written in hex

instruction_set = [
    ["LOD", "10"],
    ["STO", "11"],
    ["ADD", "20"],
    ["SUB", "21"],
    ["ADC", "22"],
    ["JMP", "30"],
    ["JZ", "31"],
    ["JC", "32"],
    ["JNZ", "33"],
    ["JNC", "34"],
    ["HLT", "FF"]
]

def main():
    # The file Assembly_Code_Editor.txt will act as a code editor where assembly is written
    # Once assembled, it will be stored in the file Assembled_Code.txt to be transfered to the RAM
    editor = open("Assembly_Code_Editor.txt", "r")
    assembled_code = open("Assembled_Code.txt", "a")
    lines = editor.readlines()
    # Remove the /n in each line of lines and remove spacing
    for i in range(len(lines)):
        lines[i] = lines[i].replace(" ", "")
        line = lines[i]
        if i != len(lines) - 1:
            lines[i] = line[0:len(line) - 1]
    print(lines)
            

    editor.close()
    assembled_code.close()
main()