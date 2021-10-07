import yaml

with open("fstab.yml", "r") as stream:
    try:
        fstab = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

entries = []

def parse_yaml():
    for k, v in fstab.items():
        for i in fstab[k].items():
            entries.append(i)

    for i in entries:
        print(i)




def main():
    parse_yaml()

if __name__ == "__main__":
    main()