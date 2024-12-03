import re

def part1(lines):
    joinedLines = ''.join(lines)
    mulPairs = re.findall(r"mul\((\d+),(\d+)\)", joinedLines)
    prods = [int(x[0]) * int(x[1]) for x in mulPairs]
    return sum(prods)

def part2(lines):
    joinedLines = str()
    for line in lines:
        joinedLines += line.strip()
    joinedLines = "do()" + joinedLines
    # print(joinedLines)

    # split on the dos and donts
    dosAndDonts = re.sub(
            pattern=r"(do\(\)|don't\(\))",
            repl=r"\n\1",
            string=joinedLines
          )
    dosAndDonts = dosAndDonts.splitlines()
    # print(dosAndDonts)

    # filter out the donts
    dos = [x for x in dosAndDonts if x.startswith("do()") ]
    dos = ''.join(dos)
    # print(dos)

    mulPairs = re.findall(r"mul\((\d+),(\d+)\)", dos)
    prods = [int(x[0]) * int(x[1]) for x in mulPairs]
    return sum(prods)

if __name__ == "__main__":

    with open('../input-files/adventofcode.com_2024_day_1_input.txt', 'r') as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
