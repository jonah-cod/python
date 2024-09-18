import sys
from itertools import count, islice
# basic open and read file contents
# f = open(sys.argv[1], mode="rt", encoding="utf-8")

# for line in f:
#     sys.stdout.write(line)
# f.close()

def sequence():
    """Generate Recaman's sequence
    """
    seen =set()
    a =0
    
    for n in count(1):
        yield a
        seen.add(a)
        c = a-n

        if c<0 or c in seen:
            c = a + n
            
        a = c

def write_sequenc_to_file(filename, num):
    """Write Recama's squence to a file
    """
    
    with open(filename, mode="wt", encoding="utf-8") as f:
        f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
    


def read_series(filename):
    
    with open(filename, mode="rt", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]
    
def main(filename):
    seq = read_series(filename)
    print(seq)
    
if __name__ == '__main__':
    # write_sequenc_to_file(sys.argv[1], num=int(sys.argv[2]))
    main(sys.argv[1])