from day_7_input import input
from pprint import pprint

t_input = """$ cd /
$ ls
dir a.py
14848514 b.txt
8504156 c.dat
dir d
$ cd a.py
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


if __name__ == '__main__':
    current_dir = []
    full_dir = ''
    directory = {'/': []}
    for i in input.splitlines():
        if i[0] == '$':
            command_line = i[2:]
            if 'cd' in command_line:
                [command, attr] = command_line.split(' ')
                if attr == '..':
                    current_dir = current_dir[:-1]
                else:
                    current_dir.append(attr)
        else:
            [size, file] = i.split(' ')
            dir = ''
            i_size = -1
            try:
                i_size = int(size)
            except:
                dir = file
                if len(current_dir) > 0:
                    full_dir = '_'.join(current_dir) + '_' + dir
                else:
                    full_dir = current_dir[0]
                if full_dir not in directory:
                    directory[full_dir] = []
            if i_size >= 0:
                cp_current_dir = current_dir
                while len(cp_current_dir) > 0:
                    directory['_'.join(cp_current_dir)].append(i_size)
                    cp_current_dir = cp_current_dir[:-1]

    sub_result_1 = [d for d in directory.values() if sum(d) < 100000]
    result_1 = sum([item for sublist in sub_result_1 for item in sublist])
    print(f"Ergebnis 1: {result_1}")

    current_usage = sum(directory['/'])
    min_delete_size = 30_000_000 - (70_000_000 - current_usage)

    result_2 = current_usage
    for key, value in directory.items():
        if sum(value) > min_delete_size:
            if sum(value) < result_2:
                result_2 = sum(value)
    print(f"Ergebnis 2: {result_2}")


