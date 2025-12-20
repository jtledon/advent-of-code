package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	// "io"
	// "bytes"
)

func main() {
	fmt.Printf("%s\n\n", "main() function being invoked!")
	defer fmt.Println("\nCompleted main() function")

	filename := "../../input-files/day01.txt"
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	// data, err := io.ReadAll(file)
	// if err != nil {
	// 	panic(err)
	// }

	// part1(reader)
	part2(reader)
}

func part1(reader *bufio.Reader) {
	currPosition := 50
	maxPosition := 100
	zeroCount := 0
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}

		direction := line[0]
		movementAmount, err := strconv.Atoi(strings.TrimSpace(line[1:]))
		if err != nil {
			panic(err)
		}

		fmt.Printf("%d", currPosition)
		switch direction {
		case 'L':
			currPosition = (currPosition - movementAmount) % maxPosition
			if currPosition < 0 { currPosition += maxPosition }
			fmt.Printf(" - %d = ", movementAmount)
		case 'R':
			currPosition = (currPosition + movementAmount) % maxPosition
			fmt.Printf(" + %d = ", movementAmount)
		}
		fmt.Println(currPosition)

		if currPosition == 0 { zeroCount++ }
	}
	fmt.Printf("Part1 Answer: %d\n", zeroCount)
}

func part2(reader *bufio.Reader) {
	currPosition := 50
	maxPosition := 100
	zeroCount := 0
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}

		direction := line[0]
		movementAmount, err := strconv.Atoi(strings.TrimSpace(line[1:]))
		if err != nil {
			panic(err)
		}

		// for i := 0; i < movementAmount; i++ {
		for range movementAmount {
			switch direction {
			case 'L':
				currPosition--
				if currPosition < 0 { currPosition += maxPosition }
			case 'R':
				currPosition++
				currPosition = currPosition % maxPosition
			}
			if currPosition == 0 { zeroCount++ }
		}

	}
	fmt.Printf("Part2 Answer: %d\n", zeroCount)
}
