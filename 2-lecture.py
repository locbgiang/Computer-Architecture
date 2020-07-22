import sys

memory = [0] * 256
address = 0

if len(sys.argv) != 2:
    print('Usage: 2-lecture.py filename')
    sys.exit(1) 

try:
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                line = line.split('#', 1)[0]
                line = int(line)
                memory[address] = line
                address += 1 
            except ValueError:
                pass
except FileNotFoundError:
    print(f'Couldnt find file {sys.argv[1]}')
    sys.exit(1)

register = [0] * 8
pc = 0
running = True

while running:
    inst = memory[pc]
    if inst == 1:
        print('Loc')
        pc += 1
    elif inst == 2:
        running = False
    elif inst == 3:
        reg_num =  memory[pc+1]
        value = memory[pc+2]
        register[reg_num] = value
        pc += 3
    elif inst == 4:
        reg_num = memory[pc+1]
        print(register[reg_num])
        pc += 2
    else:
        print(f'Uknown instruction {inst}')
        running = False
