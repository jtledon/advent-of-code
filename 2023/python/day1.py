wordNums = [
        "one"
      , "two"
      , "three"
      , "four"
      , "five"
      , "six"
      , "seven"
      , "eight"
      , "nine"
]

# TODO: this could have just been the index of the wordNums list but maybe this is more clear?
def wordToInt(word):
    match word:
      case "one":
          return 1
      case "two":
          return 2
      case "three":
          return 3
      case "four":
          return 4
      case "five":
          return 5
      case "six":
          return 6
      case "seven":
          return 7
      case "eight":
          return 8
      case "nine":
          return 9
      case _:
          return 0

def part1():
    with open('../input-files/adventofcode.com_2023_day_1_input.txt', 'r') as f:
        lines = f.readlines()

    vals = list()
    for line in lines:
        nums = [int(x) for x in line if x.isnumeric() ]
        # print(line, nums)
        first, last = nums[0], nums[len(nums)-1]
        vals.append(first * 10 + last)

    return sum(vals)

def part2():
    with open('../input-files/adventofcode.com_2023_day_1_input.txt', 'r') as f:
        lines = f.readlines()

    vals = list()
    res = 0
    for line in lines:
        line = line.strip()

        foundFirst = False
        foundLast = False
        first = 0
        last = 0

        i = 0
        j = len(line)
        while i != j:
            if foundFirst and foundLast:
                break
            substr = line[i:j]
            if not foundFirst:
                if substr[0].isnumeric():
                    first = int(substr[0])
                    foundFirst = True
                else:
                    for word in wordNums:
                        if substr.startswith(word):
                            first = wordToInt(word)
                            foundFirst = True
            if not foundLast:
                if substr[len(substr) - 1].isnumeric():
                    last = int(substr[len(substr)-1])
                    foundLast = True
                else:
                    for word in wordNums:
                        if substr.endswith(word):
                            last = wordToInt(word)
                            foundLast = True
            if not foundFirst:
                i += 1
            if not foundLast:
                j -= 1
        res += (first * 10) + last
    return res



if __name__ == "__main__":
    print(part1())
    print(part2())
