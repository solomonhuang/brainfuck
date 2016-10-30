class Brainfuck:
    pc = 0
    pointer = 0
    buffer = bytearray(30000)
    code = ''

    def __init__(self, code=''):
        self.code = code

    def next_pc(self):
        self.pc = self.pc + 1

    def pointer_incr(self):
        self.pointer = (self.pointer + 1) % len(self.buffer)

    def pointer_decr(self):
        self.pointer = (self.pointer - 1) % len(self.buffer)

    def value_incr(self):
        self.buffer[self.pointer] = (self.buffer[self.pointer] + 1) % 256
    
    def value_decr(self):
        self.buffer[self.pointer] = (self.buffer[self.pointer] - 1) % 256

    def output(self):
        print(chr(self.buffer[self.pointer]), end="")

    def input(self):
        data = input()
        self.buffer[self.pointer] = int(data[0].encode('ascii'))

    def jmp_forward(self):
        if self.buffer[self.pointer] == 0:
            for i in range(self.pc + 1, len(self.code)):
                if self.code[i] == ']':
                    self.pc = i
                    return
            raise Exception('Can not find "]"')

    def jmp_backward(self):
        if self.buffer[self.pointer] != 0:
            for i in range(self.pc - 1, 0, -1):
                if self.code[i] == '[':
                    self.pc = i
                    return
            raise Exception('Can not find "["')

    instruction_table = {
        '>': pointer_incr,
        '<': pointer_decr,
        '+': value_incr,
        '-': value_decr,
        '.': output,
        ',': input,
        '[': jmp_forward,
        ']': jmp_backward
    }

    def run(self):
        while(True):
            try:
                if self.code[self.pc] in self.instruction_table: 
                    self.instruction_table[self.code[self.pc]](self)
                self.next_pc()
            except IndexError:
                return


bf = Brainfuck('''++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.''')

bf.run()

bf = Brainfuck(''',>++++++[<-------->-],,[<+>-],<.>.''')
bf.run()
