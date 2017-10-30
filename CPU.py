from Extrenal_controlers import ExternalControllers as ec


class CPU:
    rr = 0

    def NOPO(self):
        self.rr = self.rr
        ec.flag_0 = 1

    def LD(self):
        self.rr = ec.data

    def LDC (self):
        self.rr = ~ec.data

    def AND(self):
        self.rr &= ec.data

    def ANDC(self):
        self.rr &= ~ec.data

    def OR(self):
        self.rr |= ec.data

    def ORC(self):
        self.rr |= ~ec.data

    def XNOR(self):
        self.rr = ~(ec.data ^ self.rr)

    def STO(self):
        ec.data = self.rr

    def STOC(self):
        ec.data = ~self.rr

    def IEN(self):
        ec.IEN = ec.data

    def OEN(self):
        ec.OEN = ec.data

    def JMP(self):
        ec.flag_JMP = 1

    def RTN(self):
        ec.flag_RTN = 1

    def SKZ(self):
        ec.pc += ~self.rr

    def NOPF(self):
        self.rr = self.rr
        ec.flag_F = 1

    def __init__(self):
        self.opcode_table = {0x0: self.NOPO, 0x1: self.LD, 0x2: self.LDC, 0x3: self.AND, 0x4: self.ANDC, 0x5: self.OR, 0x6: self.ORC, 0x7: self.XNOR,
                             0x8: self.STO, 0x9: self.STOC, 0xA: self.IEN, 0xB: self.OEN, 0xC: self.JMP, 0xD: self.RTN, 0xE: self.SKZ, 0xF: self.NOPF}

    def clock(self):
        while True:
            ec.data = ec.put[ec.mem[(ec.pc & 0b00001111)]]
            self.opcode_table[ec.mem[(ec.pc & 0b11110000) >> 4]]()
            ec.put[ec.pc & 0b00001111] = ec.data
            print(ec.put, self.opcode_table)

cpu = CPU()
cpu.clock()
