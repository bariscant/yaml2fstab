import yaml

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

    for i in entries:
        print(i[0], i[1])




def main():
    parse_yaml()

if __name__ == "__main__":
    main()