#!/usr/bin/env python3

from functools import reduce
from itertools import islice
from operator import mul


def code(inp):
    return ''.join(
        [bin(int(c, 16))[2:].rjust(4, '0') for c in inp])


def take(count, it):
    return ''.join(islice(it, count))


def drop(count, it):
    return ''.join(islice(it, count, None))


def log(label, val):
    print(label, f"{bin(val)} ({val})")


def read(n, lst):
    val = take(n, lst)
    lst = drop(n, lst)
    return val, lst


def read_chunk(lst):
    chunk = ""
    while True:
        piece, lst = read(5, lst)
        d = int(piece, 2)
        chunk += bin(d & 0b1111)[2:].rjust(4, '0')
        if not d & (1 << 4):
            break
    return chunk, lst


def part1(inp):
    versions = 0
    while inp and int(inp, 2):
        version, inp = read(3, inp)
        version = int(version, 2)
        versions += version

        type_id, inp = read(3, inp)
        type_id = int(type_id, 2)

        if type_id == 4:
            chunk, inp = read_chunk(inp)
            # chunk = int(chunk, 2)
        else:
            packet_type_id, inp = read(1, inp)
            packet_type_id = int(packet_type_id, 2)
            if packet_type_id:
                packet_len, inp = read(11, inp)
            else:
                packet_len, inp = read(15, inp)
            # packet_len = int(packet_len, 2)
    return versions


print("part 1:", part1(code(open('input-16.txt').read())))


def parse(inp):
    if not inp or not int(inp, 2):
        return

    version, inp = read(3, inp)
    type_id, inp = read(3, inp)
    type_id = int(type_id, 2)

    if type_id == 4:  # literal /1
        literal, inp = read_chunk(inp)
        literal = int(literal, 2)
        return literal, inp

    packet_type_id, inp = read(1, inp)
    packet_type_id = int(packet_type_id, 2)

    results = []
    if packet_type_id:
        num_packets, inp = read(11, inp)
        num_packets = int(num_packets, 2)
        for _ in range(num_packets):
            result, inp = parse(inp)
            results.append(result)
    else:
        packets_size, inp = read(15, inp)
        packets_size = int(packets_size, 2)
        sub, inp = read(packets_size, inp)
        while sub:
            result, sub = parse(sub)
            results.append(result)
    return {
               0: lambda: sum(results),
               1: lambda: reduce(mul, results, 1),
               2: lambda: min(results),
               3: lambda: max(results),
               5: lambda: int(results[0] > results[1]),
               6: lambda: int(results[0] < results[1]),
               7: lambda: int(results[0] == results[1])
           }[type_id](), inp


assert parse(code("C200B40A82"))[0] == 3
assert parse(code("04005AC33890"))[0] == 54
assert parse(code("880086C3E88112"))[0] == 7
assert parse(code("CE00C43D881120"))[0] == 9
assert parse(code("D8005AC2A8F0"))[0] == 1
assert parse(code("F600BC2D8F"))[0] == 0
assert parse(code("9C005AC2F8F0"))[0] == 0
assert parse(code("9C0141080250320F1802104A08"))[0] == 1
print("part 2:", parse(code(open('input-16.txt').read()))[0])
