#!/usr/bin/env python3
import yaml
import os
import sys

with open(sys.argv[1], "r") as stream:
    try:
        fstab = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

entries = []
output = ""


def parse_yaml():
    '''
    This function iterates over imported yaml and creates a list containing each fstab entry.
    '''
    for k, v in fstab.items():
        for i in fstab[k].items():
            entries.append(i)


def write_fstab_file():
    f = open('fstab', 'w')
    original = ""
    origin = open(sys.argv[2], 'r')
    f.writelines(origin.readlines())
    
    for i in entries:
        if i[1]['type'] == "nfs":
            f.write(i[0])
            f.write(':')
            f.write(i[1]['export'])
            f.write('\t')
            f.write(i[1]['mount'])
            f.write('\t')
            f.write(i[1]['type'])
            if 'options' in i[1]:
                f.writelines(",".join(i[1]['options']))
            else:
                f.write('defaults')
            f.write('\t')
            f.write('0\t0')
            f.write('\n')
        else:
            f.write(i[0])
            f.write('\t')
            f.write(i[1]['mount'])
            f.write('\t')
            f.write(i[1]['type'])
            f.write('\t')
            if 'options' in i[1]:
                f.writelines(",".join(i[1]['options']))
            else:
                f.write('defaults')
            f.write('\t')
            f.write('0\t0')
            f.write('\n')
    
    f.close()
    origin.close()


def main():
    parse_yaml()
    write_fstab_file()
    print(entries)

if __name__ == "__main__":
    main()