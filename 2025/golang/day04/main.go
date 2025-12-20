package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

var day string = "04"

func main() {
	// fmt.Printf("%s\n\n", "main() function being invoked!")
	// defer fmt.Println("\nCompleted main() function")

	filename := fmt.Sprintf("../../input-files/day%s.txt", day)
	fileContents, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	part1(string(fileContents))
	part2(string(fileContents))
}

func part1(fileContents string) {
	borderChar := "o"
	arr := make([]string, 0)
	for line := range strings.SplitSeq(fileContents, "\n") {
		if len(line) == 0 { continue }
		arr = append(arr, borderChar + line + borderChar) // side border
	}

	verticalBorder := strings.Repeat(borderChar, len(arr[0]))
	arr = append(arr, verticalBorder) // bottom border
	arr = append([]string{verticalBorder}, arr...) // top border

	count := 0
	for i, line := range arr {
		// fmt.Printf("%3d : %s\n", i, line)
		for j, char := range line {
			if string(char) == borderChar { continue }
			if string(char) != "@" { continue }

			// surrounding := make([]string, 0)
			surrounding := ""
			for n := -1; n <= 1; n++ {
				// surrounding = append(surrounding, arr[i+n][j-1 : j+1 +1])
				surrounding = surrounding + arr[i+n][j-1 : j+1 +1]
			}

			atCount := 0
			for _, adjacent := range surrounding {
				if string(adjacent) == "@" {
					atCount++
				}
			}
			if atCount - 1 < 4 { // -1 for itself
				count++
			}
		}
	}
	fmt.Println(count)
}

func part2(fileContents string) {
	borderChar := "o"
	arr := make([][]string, 0)
	for line := range strings.SplitSeq(fileContents, "\n") {
		if len(line) == 0 { continue }
		arr = append(arr, strings.Split(borderChar + line + borderChar, "")) // side border
	}

	verticalBorder := strings.Repeat(borderChar, len(arr[0]))
	arr = append(arr, strings.Split(verticalBorder, "")) // bottom border
	arr = append([][]string{strings.Split(verticalBorder, "")}, arr...) // top border

	overallCount := 0
	for {
		iterationCount := 0

		for i, line := range arr {
			for j, char := range line {
				if string(char) == borderChar { continue }
				if string(char) != "@" { continue }

				surrounding := make([]string, 0)
				for n := -1; n <= 1; n++ {
					surrounding = slices.Concat(surrounding, arr[i+n][j-1 : j+1 +1])
				}

				atCount := 0
				for _, adjacent := range surrounding {
					if string(adjacent) == "@" {
						atCount++
					}
				}
				if atCount - 1 < 4 { // -1 for itself
					overallCount++
					iterationCount++
					arr[i][j] = "."
				}
			}
		}

		if iterationCount == 0 { break }
	}

	fmt.Println(overallCount)
}
