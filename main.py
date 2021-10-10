import yaml
import os
import sys

with open("fstab.yml", "r") as stream:
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
    origin = open('/etc/fstab', 'r')
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
            options = str(i[1]['options']).split(',')
            f.writelines(options)
            for option in i[1]['options']:
                f.write(option)
                f.write(',')
            f.write('\t')
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
            f.write('defaults')
            f.write('\t')
            f.write('0\t0')
            f.write('\n')
    
    f.close()
    origin.close()


def main():
    parse_yaml()
    write_fstab_file()

if __name__ == "__main__":
    main()