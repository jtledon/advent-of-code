package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
	// "io"
	// "bytes"
	// "regexp"
	// "sort"
)

var day int = 3

func main() {
	// fmt.Printf("%s\n\n", "main() function being invoked!")
	// defer fmt.Println("\nCompleted main() function")

	filename := fmt.Sprintf("../../input-files/day%d.txt", day)
	fileContents, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	part1(string(fileContents))
	part2(string(fileContents))
}

func part1(fileContents string) {

	var largestPairSum int = 0

	fileContents = strings.TrimSpace(fileContents)
	for line := range strings.SplitSeq(fileContents, "\n") {

		largestVal, largestIdx := 0, 0
		secondLargestVal := 0

		for idx, voltage := range line {
			v, err := strconv.Atoi(string(voltage))
			if err != nil { panic(err) }

			if v > largestVal {
				if idx == len(line) - 1 {
					secondLargestVal = largestVal
				} else {
					secondLargestVal = 0
				}
				largestVal = v
				largestIdx = idx
			} else if v > secondLargestVal {
				secondLargestVal = v
			}
		}

		if largestIdx == len(line) - 1 {
			pair, err := strconv.Atoi(fmt.Sprintf("%d%d", secondLargestVal, largestVal))
			if err != nil { panic(err) }
			// fmt.Println(line, pair)
			largestPairSum += pair
		} else {
			pair, err := strconv.Atoi(fmt.Sprintf("%d%d", largestVal, secondLargestVal))
			if err != nil { panic(err) }
			// fmt.Println(line, pair)
			largestPairSum += pair
		}
	}
	fmt.Println(largestPairSum)
}

func part2(fileContents string) {

	var combinedVoltageSum int = 0
	var numBatteries int = 12

	fileContents = strings.TrimSpace(fileContents)
	for line := range strings.SplitSeq(fileContents, "\n") {

		voltages := strings.Split(line, "")
		voltagesInts := turnSliceOfStringsToInts(voltages)
		// fmt.Println(voltagesInts)

		agg := make([]int, 0)
		startingIndex := 0

		for i := numBatteries; i > 0; i-- {
			candidateSlice := voltagesInts[startingIndex : len(voltages)+1-i]

			maxInCandidateSlice := slices.Max(candidateSlice)
			startingIndex = slices.Index(candidateSlice, maxInCandidateSlice) + startingIndex + 1
			agg = append(agg, maxInCandidateSlice)

			// fmt.Println(candidateSlice, agg, maxInCandidateSlice, startingIndex)
		}

		maxBatteryCombination := turnSliceOfIntsToSingleString(agg)
		maxBatteryCombinationAsInt, _ := strconv.Atoi(maxBatteryCombination)
		combinedVoltageSum += maxBatteryCombinationAsInt

		// fmt.Println(maxBatteryCombinationAsInt)
		// fmt.Println("\n\n")
	}
	fmt.Println(combinedVoltageSum)
}

func turnSliceOfStringsToInts(arr []string) []int {
	intArr := make([]int, 0)
	for _, val := range arr {
		num, err := strconv.Atoi(val)
		if err != nil { panic(err) }
		intArr = append(intArr, num)
	}
	return intArr
}

func turnSliceOfIntsToSingleString(arr []int) string {
	s := ""
	for _, val := range arr {
		s = fmt.Sprintf("%s%d", s, val)
	}
	return s
}
