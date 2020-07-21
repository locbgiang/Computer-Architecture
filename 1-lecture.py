memory = [
    1,  #print loc 
    3,  #save_reg r2, 99 register to save in, the value save there
    2,      # R2
    99,          # 99
    4,     # print reg
    2,
    2,      # HALT

]

register = [0] * 8

pc = 0  # program counter, index into memory of the currrent instruction
        # aka a pointer to the current instruction
running = True
while running:
    inst = memory[pc]
    if inst == 1:
        print('Loc')
        pc += 1
    elif inst == 2:
        running = False
    elif inst == 3:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        pc += 3
    elif inst == 4:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 1
    else:
        print(f'Unknown instruction {inst}')
        pc += 1

print(register)