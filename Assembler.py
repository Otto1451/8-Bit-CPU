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
    code = open("Assembly_Code.txt", "r")
    assembled_code = open("Assembled_Code.txt", "a")
    read_content = code.read().split()

    # Remove commas in instruction
    for i in range(len(read_content)):
        word = read_content[i]
        if word[len(word) - 1] == ",":
            read_content[i] = word[0: len(word) - 1]

    for word in read_content:
        opcode = False
        for j in range(len(instruction_set)):
            if instruction_set[j][0] == word:
                assembled_code.write(instruction_set[j][1])
                opcode = True
                break
        if opcode == False:
            if word[0] == "[" and word[len(word) - 1] == "]":
                assembled_code.write(word[1:(len(word) - 1)])
        assembled_code.write(" ")
    code.close()
    assembled_code.close()
main()