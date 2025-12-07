package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"slices"

	// "regexp"
	"runtime"
	"strconv"
	"strings"
)

type Interval struct {
	Start int
	End   int
}

func main() {
	_, file, _, ok := runtime.Caller(0)
	if !ok {
		panic("Unable to fetch path of current file")
	}
	dir := filepath.Base(filepath.Dir(file))
	day := string(dir[len(dir)-1])

	filename := fmt.Sprintf("day%s.txt", day)
	path := filepath.Join("../../", "input-files", filename)
	fileContents, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	fmt.Printf("=== Part1 Answer: %d ===\n", Part1(string(fileContents)))
	fmt.Printf("=== Part2 Answer: %d ===\n", Part2(string(fileContents)))
}

func Part1(fileContents string) int {
	numbersGrid := make([][]int, 0)
	var operations []string

	fileContents = strings.TrimSpace(fileContents)
	lines := strings.Split(fileContents, "\n")
	for idx, line := range lines {
		row := make([]int, 0)

		// whitespaceRegex := regexp.MustCompile(`\s+`)
		// splitLine := whitespaceRegex.Split(line)
		splitLine := strings.Fields(line)
		if idx == len(lines)-1 { // last line: line of operations
			operations = splitLine
		} else { // parse numbers line into numbers grid
			for _, number := range splitLine {
				numberInt, _ := strconv.Atoi(number)
				row = append(row, numberInt)
			}
			numbersGrid = append(numbersGrid, row)
		}

	}

	totalSum := 0
	for operIdx, operation := range operations {
		var colTotal int
		for numIdx, numRow := range numbersGrid {
			// set the identity val for the given column operation
			if numIdx == 0 {
				if operation == "*" {
					colTotal = 1
				} else {
					colTotal = 0
				}
			}

			switch operation {
			case "*":
				colTotal = colTotal * numRow[operIdx]
			case "+":
				colTotal = colTotal + numRow[operIdx]
			case "-":
				colTotal = colTotal - numRow[operIdx]
			}
		}
		totalSum += colTotal
	}

	return totalSum
}

func Part2(fileContents string) int {
	lines := strings.Split(fileContents, "\n")
	lines = slices.DeleteFunc(lines, func(e string) bool { return len(e) == 0 }) // remove empty lines

	operationsLine := lines[len(lines)-1]
	numberLines := lines[:len(lines)-1]

	operations := strings.Fields(operationsLine)
	// operationsIndexs := regexp.MustCompile(`\S\s*`).FindAllIndex([]byte(operationsLine), -1)

	vertGrid := make([][]int, 0)
	vertArr := make([]int, 0)
	for col := range numberLines[0] {
		vertNum := ""
		for row := range numberLines {
			vertNum += string(numberLines[row][col])
		}

		if len(strings.TrimSpace(vertNum)) == 0 {
			vertGrid = append(vertGrid, vertArr)
			vertArr = make([]int, 0)
		} else {
			removedWhitespace := regexp.MustCompile(`\s+`).ReplaceAll([]byte(vertNum), []byte(""))
			vertInt, _ := strconv.Atoi(string(removedWhitespace))
			vertArr = append(vertArr, vertInt)
		}
	}
	vertGrid = append(vertGrid, vertArr)




	total := 0
	var subtotal int
	for rowIdx, numRow := range vertGrid {
		for numIdx, number := range numRow {
			operation := operations[rowIdx]

			// set the identity val for the given column operation
			if numIdx == 0 {
				if operation == "*" {
					subtotal = 1
				} else {
					subtotal = 0
				}
			}

			switch operation {
			case "*":
				subtotal = subtotal * number
			case "+":
				subtotal = subtotal + number
			case "-":
				subtotal = subtotal - number
			}
		}
		total += subtotal
	}

	return total
}
