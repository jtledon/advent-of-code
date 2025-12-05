package main

import (
	"cmp"
	"fmt"
	"os"
	"path/filepath"
	"slices"
	"strconv"
	"strings"
)

var day int = 5

type Interval struct {
	Start int
	End   int
}

func main() {
	filename := fmt.Sprintf("day%d.txt", day)
	path := filepath.Join("../../", "input-files", filename)
	fileContents, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	fmt.Printf("=== Part1 Answer: %d ===\n", Part1(string(fileContents)))
	fmt.Printf("=== Part2 Answer: %d ===\n", Part2(string(fileContents)))
}

func Part1(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)

	sections := strings.Split(fileContents, "\n\n")
	ranges := sections[0]
	ingredients := sections[1]

	intervals := make([]Interval, 0)
	for line := range strings.SplitSeq(ranges, "\n") {
		split := strings.Split(line, "-")
		start, end := split[0], split[1]
		startInt, _ := strconv.Atoi(start)
		endInt, _ := strconv.Atoi(end)

		intervals = append(intervals, Interval{
			Start: startInt,
			End:   endInt,
		})
	}

	var freshCount int
	for line := range strings.SplitSeq(ingredients, "\n") {
		line = strings.TrimSpace(line)
		id, _ := strconv.Atoi(line)
		for _, interval := range intervals {
			if id >= interval.Start && id <= interval.End {
				freshCount++
				break
			}
		}
	}

	return freshCount
}

func Part2(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)

	sections := strings.Split(fileContents, "\n\n")
	ranges := sections[0]

	intervals := make([]Interval, 0)
	for line := range strings.SplitSeq(ranges, "\n") {
		split := strings.Split(line, "-")
		start, end := split[0], split[1]
		startInt, _ := strconv.Atoi(start)
		endInt, _ := strconv.Atoi(end)

		intervals = append(intervals, Interval{
			Start: startInt,
			End:   endInt,
		})
	}

	// merge ranges
	slices.SortFunc(intervals, func(a, b Interval) int {
		return cmp.Compare(a.Start, b.Start)
	})

	nonoverlappingIntervals := make([]Interval, 0)
	runningInterval := intervals[0]
	for _, interval := range intervals {
		if runningInterval.End >= interval.Start {
			runningInterval.Start = min(interval.Start, runningInterval.Start)
			runningInterval.End = max(interval.End, runningInterval.End)
		} else {
			nonoverlappingIntervals = append(nonoverlappingIntervals, runningInterval)
			runningInterval = interval
		}
	}
	nonoverlappingIntervals = append(nonoverlappingIntervals, runningInterval)


	// sum remaining ranges
	ingredientSum := 0
	for _, interval := range nonoverlappingIntervals {
		ingredientSum += (interval.End - interval.Start + 1)
	}

	return ingredientSum
}
