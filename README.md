This script tries to parse a yaml file containing variety of fstab configs and provide fstab entries.

## Usage

```bash
./main.py fstab.yml /etc/fstab
```
## Limitations

Currently script cannot parse anyting other than default fstab fields. 

In this example Yaml `root_reserve` is not being used. 

## Breakdown of the code

This part is reading Yaml file and assigning its values to a variable named `fstab`.

```python
with open(sys.argv[1], "r") as stream:
    try:
        fstab = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
```

This function iterates over imported yaml and creates a list containing each fstab entry.

```python
def parse_yaml():
    '''
    This function iterates over imported yaml and creates a list containing each fstab entry.
    '''
    for k, v in fstab.items():
        for i in fstab[k].items():
            entries.append(i)
```

In here we are reading original `/etc/fstab` file to keep original values and adding new values by iterating over the imported `entries` list. `entries` is basically a list of tuples like below. 

```
[('/dev/sda1', {'mount': '/boot', 'type': 'xfs'}), ('/dev/sda2', {'mount': '/', 'type': 'ext4'}), ('/dev/sdb1', {'mount': '/var/lib/postgresql', 'type': 'ext4', 'root-reserve': '10%'}), ('192.168.4.5', {'mount': '/home', 'export': '/var/nfs/home', 'type': 'nfs', 'options': ['noexec', 'nosuid']})]
```

We are doing two simple checks based on entry is an nfs mount point or not. Since nfs entries are a bit more different.


```python
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
```