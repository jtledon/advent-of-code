import heapq
import sys, os

# def FileInteraction():
#     filename
#     get the input-files dir by going up 2 levels
#     create the file name based on the name of the curr directory
#     os.join the path and the filename
#     open the file 
#     read the contents
#     return the data and close the file
#     return data

def main():
    
    with open('../../input-files/adventofcode.com_2022_day_1_input.txt', 'r') as f:
        data = f.read()
    groups = data.split('\n\n')
    parsed = [group.strip().split('\n') for group in groups]
    nums = list(map(lambda groups: sum(map(int, groups)), parsed))
    heapq.heapify(nums)
    return sum(heapq.nlargest(3, nums))


if __name__ == '__main__':
    print(main())
