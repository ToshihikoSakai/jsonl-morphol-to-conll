import sys


def transform(conllfile):
    with open(conllfile) as f:
        pre_tag = ""
        for line in f:
            if(line == "\n"):
                print("")
                continue

            w, tag = line.split()

            if(tag == "O"):
                print("{} O".format(w))
                pre_tag = ""
                continue

            head, tail = tag.split('-')
            if(pre_tag == tail):
                print("{} I-{}".format(w, tail))

            else:
                print("{} B-{}".format(w, tail))

            pre_tag = tail


if __name__ == "__main__":
    transform(sys.argv[1])
