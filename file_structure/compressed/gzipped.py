import gzip

from ..utils.writer import main

opener = gzip.open

if __name__ == "__main__":
    main(opener)