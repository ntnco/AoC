from aoc_get import get_input
from functools import reduce
from operator import *


def binarize(x: int):
    b = bin(x)[2:]
    mod = len(b) % 4
    padding = 0 if mod == 0 else 4 - mod
    return '0' * padding + b


inp = get_input()
binary = binarize(int(inp, 16))
p1 = 0


class PacketNode:
    def __init__(self, i):
        self.length = 0
        self.start = i
        self.type = int(binary[i + 3:i + 6], 2)
        global p1
        p1 += int(binary[i:i + 3], 2)

        if self.type == 4:
            self.value = self.get_value(self.start + 6)

        elif binary[i + 6] == '0':
            self.sub_bits = int(binary[i + 7:i + 22], 2)
            max_i = i + 22 + self.sub_bits
            self.children = []
            i += 22
            while i < max_i:
                pn = PacketNode(i)
                self.children.append(pn)
                i += pn.length
            self.length = i - self.start

        elif binary[i + 6] == '1':
            self.num_subs = int(binary[i + 7:i + 18], 2)
            self.children = []
            i += 18
            packet_count = 0
            while packet_count < self.num_subs:
                pn = PacketNode(i)
                self.children.append(pn)
                i += pn.length
                packet_count += 1
            self.length = i - self.start


    def eval(self):
        if self.type == 4:
            return self.value

        values = [c.eval() for c in self.children]
        lambdas = [add, mul, min, max, None, gt, lt, eq]

        return reduce(lambdas[self.type], values)


    def get_value(self, i):
        value_string = ''
        while binary[i] == '1':
            value_string += binary[i + 1:i + 5]
            i += 5
        value_string += binary[i + 1:i + 5]
        self.length += i + 5 - self.start
        mod = self.length % 4
        return int(value_string, 2)


root = PacketNode(0)
p2 = root.eval()
print(p1, p2)
