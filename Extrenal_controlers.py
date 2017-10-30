class ExternalControllers:
    with open("data", "rb") as f:
        mem = f.read()
    put = [0] * 16
    pc = 0
    data = 0
    flag_0 = 0
    write = 1
    flag_JMP = 0
    flag_RTN = 0
    flag_F = 0
    IEN = 0
    OEN = 0
