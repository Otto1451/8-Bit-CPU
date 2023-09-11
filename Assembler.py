# The format of the code with be: <OPCODE> <DESTINATION>, <SOURCE> 
# A stands for ACC, [address] is used to get data at that address in RAM written in hex

INSTRUCTION_SET = [
    ["LODA,[]", "10"], ["STO[],A", "11"], ["LODB,[]", "12"], ["STO[],B", "13"], ["LODSP,[]", "14"], ["STOSP,A", "15"], ["LODB,SP", "16"],
    ["ADDA,[]", "20"], ["SUBA,[]", "21"], ["ADCA,[]", "22"],
    ["JMP[]", "30"], ["JZ[]", "31"], ["JC[]", "32"], ["JNZ[]", "33"], ["JNC[]", "34"],
    ["MOVA,B", "40"], ["MOVB,A", "41"], ["MOVA,SP", "42"], ["MOVSP,A", "43"],
    ["PUSHSP,A", "41 00 42 00 21 01 43 00 40 00 15 "],
    ["POPA,SP", "16 00 10 02 15 00 42 00 20 01 43 "],
    ["HLT", "ff"]
]

error = False

def main():
    # The file Assembly_Code_Editor.txt will act as a code editor where assembly is written
    # Once assembled, it will be stored in the file Assembled_Code.txt to be transfered to the RAM
    global error
    editor = open("Assembly_Code_Editor.txt", "r")
    assembled_code = open("Assembled_Code.txt", "w")
    assembled_code.writelines("v2.0 raw\n")
    instructions = extract_input(remove_comments(format_lines(editor.readlines())))
    if len(instructions) > 256:
        print("ERROR: TOO MANY INSTRUCTIONS")
        error = True
        return
    assembled_instructions = assemble(instructions)
    assembled_code.writelines(assembled_instructions)
    if error == False:
        print("ASSEMBLED SUCCESSFULLY")
    editor.close()
    assembled_code.close()


def format_lines(lines):
    # Remove the /n in each line of lines and remove spacing
    for i in range(len(lines)):
        lines[i] = lines[i].replace(" ", "")
        line = lines[i]
        if i != len(lines) - 1:
            lines[i] = line[0:len(line) - 1]
    return lines

def remove_comments(lines):
    # If a line begins with #, then it is a comment
    uncommented_lines = []
    for line in lines:
        if line[0] != "#":
            uncommented_lines.append(line)
    return uncommented_lines

def extract_input(lines):
    global error
    # For each instruction, return [instruction, input] where the [address] is removed from instruction
    instructions = []
    for line in lines:
        for i in range(len(line)):
            if line[i] == "[":
                if line[i + 3] != "]":
                    print("ERROR: Length of memory address should be 2")
                    error = True
                    return
                instructions.append([line[0:i + 1] + line[i + 3:len(line)], line[i + 1: i + 3]])
                break
            # No [], i.e one byte instructions
            if i == len(line) - 1:
                instructions.append([line, "00"])
    return instructions

def assemble(instructions):
    global error
    assembled_instructions = []
    for instruction in instructions:
        for i in range(len(INSTRUCTION_SET)):
            if INSTRUCTION_SET[i][0] == instruction[0]:
                assembled_instructions.append(INSTRUCTION_SET[i][1] + " " + instruction[1] + " ")
                break
            if i == len(INSTRUCTION_SET) - 1:
                print("ERROR: Instruction not in instruction set")
                error = True

    return assembled_instructions
main()