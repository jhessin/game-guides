#! python3

from typing import Dict

K = 1_000
M = 1_000_000
B = 1_000_000_000
T = 1_000_000_000_000
q = 1_000_000_000_000_000
Q = 1_000_000_000_000_000_000

Heroes: Dict[str, int] = {
    'Bruenor': 3468 // 4,
    'Celeste': 76.7 * K // 6,
    'Nayeli': 841 * K // 6.7,
    'Jarlaxle': 11.1 * M // 5,
    'Calliope': 114 * M // 3.7,
    'Ashara': 578 * M // 7,
    'Minsc': 9.29 * B // 4.5,
    'Delina': 44.5 * B // 6,
    'Makos': 164 * B // 5.7,
    'Tyril': 38.8 * B // 4.7,
}

def keyfunc(item: (str, int)):
    return item[1]

print(sorted(Heroes.items(), key=keyfunc, reverse=True))