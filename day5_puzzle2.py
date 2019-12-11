from enum import Enum


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATE = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Instruction:
    def __init__(self, number):
        number = str(number).zfill(5)

        self.opcode = Operation(int(number[3:]))
        self.modes = list(map(Mode, map(int, list(number)[0:3])))[::-1]


def getValues(array, params, modes):
    return list(
        map(
            lambda param, mode: array[param] if mode is Mode.POSITION else param,
            params,
            modes,
        )
    )


def runProgram(program):
    array = program.copy()
    pointer = 0
    while True:
        instruction = Instruction(array[pointer])
        if instruction.opcode is Operation.ADD:
            params = array[pointer + 1 : pointer + 4]
            values = getValues(array, params, instruction.modes)
            array[params[2]] = values[0] + values[1]

            pointer += 4
        elif instruction.opcode is Operation.MULTIPLY:
            params = array[pointer + 1 : pointer + 4]
            values = getValues(array, params, instruction.modes)
            array[params[2]] = values[0] * values[1]

            pointer += 4
        elif instruction.opcode is Operation.INPUT:
            userInput = input("Please enter ID :: ")
            param = array[pointer + 1]
            array[param] = int(userInput)

            pointer += 2
        elif instruction.opcode is Operation.OUTPUT:
            param = array[pointer + 1]
            print(array[param])

            pointer += 2
        elif instruction.opcode is Operation.JUMP_IF_TRUE:
            params = array[pointer + 1 : pointer + 3]
            values = getValues(array, params, instruction.modes)

            if values[0] != 0:
                pointer = values[1]
            else:
                pointer += 3
        elif instruction.opcode is Operation.JUMP_IF_FALSE:
            params = array[pointer + 1 : pointer + 3]
            values = getValues(array, params, instruction.modes)

            if values[0] == 0:
                pointer = values[1]
            else:
                pointer += 3
        elif instruction.opcode is Operation.LESS_THAN:
            params = array[pointer + 1 : pointer + 4]
            values = getValues(array, params, instruction.modes)

            if values[0] < values[1]:
                array[params[2]] = 1
            else:
                array[params[2]] = 0

            pointer += 4
        elif instruction.opcode is Operation.EQUALS:
            params = array[pointer + 1 : pointer + 4]
            values = getValues(array, params, instruction.modes)

            if values[0] == values[1]:
                array[params[2]] = 1
            else:
                array[params[2]] = 0

            pointer += 4
        elif instruction.opcode is Operation.TERMINATE:
            break
    return array


program = "3,225,1,225,6,6,1100,1,238,225,104,0,1002,36,25,224,1001,224,-2100,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,31,84,225,1102,29,77,225,1,176,188,224,101,-42,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,2,196,183,224,1001,224,-990,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,102,14,40,224,101,-1078,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1001,180,64,224,101,-128,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,24,17,224,1001,224,-408,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,9,66,224,1001,224,-75,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,18,33,225,1101,57,64,225,1102,45,11,225,1101,45,9,225,1101,11,34,225,1102,59,22,225,101,89,191,224,1001,224,-100,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,629,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"
program = list(map(int, program.split(",")))

runProgram(program)
