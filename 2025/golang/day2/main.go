package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	// "io"
	// "bytes"
	// "regexp"
	// "sort"
)

var day int = 2

func main() {
	fmt.Printf("%s\n\n", "main() function being invoked!")
	defer fmt.Println("\nCompleted main() function")

	filename := fmt.Sprintf("../../input-files/day%d.txt", day)
	fileContents, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	part1(string(fileContents))
	part2(string(fileContents))
}

func part1(fileContents string) {
	// for i, line := range strings.Split(fileContents, "\n") {
	// 	fmt.Printf("index(%d)\nline: %s\n", i, line)
	// }

	var invalidSum int = 0

	fileContents = strings.TrimSpace(fileContents)
	for rng := range strings.SplitSeq(fileContents, ",") {

		splitRange := strings.Split(rng, "-")

		start, err := strconv.Atoi(splitRange[0])
		if err != nil { panic(err) }

		end, err := strconv.Atoi(splitRange[1])
		if err != nil { panic(err) }

		for i := start; i <= end; i++ {
			iAsStr := strconv.Itoa(i)
			if len(iAsStr) % 2 == 1 {
				continue
			}

			frontHalf := iAsStr[:len(iAsStr)/2]
			backHalf := iAsStr[len(iAsStr)/2:]
			if frontHalf == backHalf {
				invalidSum += i
			}
		}

	}
	fmt.Println(invalidSum)
}

func part2(fileContents string) {
	var invalidSum int = 0
	// invalidNumberRegex := regexp.MustCompile(`^(.+?)\1+$`)
	// if invalidNumberRegex.MatchString(iAsStr) {

	fileContents = strings.TrimSpace(fileContents)
	for rng := range strings.SplitSeq(fileContents, ",") {

		splitRange := strings.Split(rng, "-")

		start, err := strconv.Atoi(splitRange[0])
		if err != nil { panic(err) }

		end, err := strconv.Atoi(splitRange[1])
		if err != nil { panic(err) }

		for i := start; i <= end; i++ {
			iAsStr := strconv.Itoa(i)
			if isRepeated(iAsStr) {
				invalidSum += i
			}
		}

	}
	fmt.Println(invalidSum)
}

func isRepeated(s string) bool {
    n := len(s)
    for i := 1; i <= n/2; i++ {
        if n%i == 0 {
            unit := s[:i]
            ok := true
            for j := i; j < n; j += i {
                if s[j:j+i] != unit {
                    ok = false
                    break
                }
            }
            if ok {
                return true
            }
        }
    }
    return false
}
