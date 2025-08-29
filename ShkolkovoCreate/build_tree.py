from itertools import product
from sys import argv


def check_good_key(key_vals, key):
    if key in key_vals:
        return True
    for k in key_vals:
        if key.startswith(k):
            return False
    return True


INTRO = \
    """
digraph
{
    graph [dpi = 300];
    rankdir = TB;
    edge[color = "#f646dc"]
    node[shape = record, color = "#000000", fontsize = 10, style = \
    "filled", fillcolor = "#fae2f6", label = ""];
    bgcolor = "#00000000";
    root
    """
OUTRO = \
    """
}
    """

if len(argv) != 2:
    print(f"Usage: {argv[0]} <output_file>")
    exit(-1)

print("Введите <код> <буква> построчно. Когда закончите, введите\
      пустую строку")

result_file = open(argv[1], "w")

levels = 0
key_vals = {}
s = input()
while s:
    key_val = s.split()
    key_vals[key_val[0]] = key_val[1]
    levels = max(len(key_val[0]), levels)
    s = input()

keys = []
invisible_keys = []

for i in range(1, levels + 1):
    for k in product("01", repeat=i):
        key = "".join(k)
        keys.append(key)
        if not check_good_key(key_vals, key):
            invisible_keys.append(key)

print(INTRO, file=result_file)

for k in keys:
    val = ""
    if k in key_vals:
        print(f"    t{k}[label = \"{{{k}|{key_vals[k]}}}\"];", file=result_file)
    elif k in invisible_keys:
        print(f"    t{k}[style = invis];", file=result_file)
    else:
        print(f"    t{k}[label = \"{{{k}}}\"];", file=result_file)


print("    root->{t0, t1}", file=result_file)

for k in keys[:2 ** levels - 2]:
    key0 = f"{k}0"
    key1 = f"{k}1"
    print(f"    t{k}->t{k}0", end="", file=result_file)
    if key0 in invisible_keys:
        print("[style = invis]", end="", file=result_file)
    print(";", file=result_file)
    print(f"    t{k}->t{k}1", end="", file=result_file)
    if key1 in invisible_keys:
        print("[style = invis]", end="", file=result_file)
    print(";", file=result_file)

print(OUTRO, file=result_file)

result_file.close()
