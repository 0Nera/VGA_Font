from font import vgafnt

data = ""
ntemp = []


def norm(data):
    ndata = str(data)
    ndata = ndata.replace('0b', '')
    b = ''
    if len(ndata) != 8:
        b = '0' * (8 - len(ndata))
    ndata = '0b' + b + ndata
    return ndata

def load():
    for i in vgafnt['data']:
        data += f"{norm(bin(i))},\n"

    with open('font.txt', 'w+') as f:
        f.write(data + "end")


def write():
    nfile = """#include <stdint.h>

int vgafnt_size = 4096;

uint8_t vgafnt[] = {\n"""
    with open('font.txt', 'r') as f:
        ntemp = f.read().split(",\n")  

    with open('vgafnt.c', 'w+') as f:
        for i in ntemp:
            if i != "end":
                t = hex(int(i, 2))
                if t == "0x0":
                    t = "0x00"
                nfile += f"\t{t}, // {i}\n"
            else:
                nfile += "};"
        f.write(nfile)

if __name__ == "__main__":
    x = "0"
    while(x != "9"):
        print("""Menu:
    0 - загрузить vgafnt из font.py
    1 - создать vgafnt.c из font.txt
    9 - выход""")
        x = input()
        if x == "0":
            load()
        elif x == "1":
            write()
        elif x == "9":
            print("Выход")
        else:
            print("Неизвестная команда")
