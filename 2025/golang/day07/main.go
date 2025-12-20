package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strings"
)

func main() {
	_, file, _, ok := runtime.Caller(0)
	if !ok { panic("Unable to fetch path of current file") }

	dir := filepath.Base(filepath.Dir(file))
	day:= regexp.MustCompile(`\d+`).FindString(dir)

	filename := fmt.Sprintf("day%s.txt", day)
	path := filepath.Join("../../", "input-files", filename)
	fileContents, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	fmt.Printf("=== Part1 Answer: %d ===\n", Part1(string(fileContents)))
	fmt.Printf("=== Part2 Answer: %d ===\n", Part2(string(fileContents)))
}

func turnInto2dGrid(lines string) [][]string {
	grid := make([][]string, 0)
	for line := range strings.SplitSeq(lines, "\n") {
		arrLine := make([]string, 0)
		for _, char := range line {
			arrLine = append(arrLine, string(char))
		}
		grid = append(grid, arrLine)

	}
	return grid
}

var memoizer map[Location][]Location = make(map[Location][]Location)

type Location struct {
	row, col int;
}

/**
 * Acting on a location, given a grid, return all locations where the beam will
 * be next. Also
 */
func (l Location) nextLocations(grid Grid) []Location {
	if memoizedRet, ok := memoizer[l]; ok {
		return memoizedRet
	}

	downChar := grid[l.row+1][l.col]

	var retVal []Location
	switch downChar {
	case "^":
		retVal = []Location{
			{
				row: l.row+1,
				col: l.col-1,
			},
			{
				row: l.row+1,
				col: l.col+1,
			},
		}
	default:
		retVal = []Location{
			{
				row: l.row+1,
				col: l.col,
			},
		}
	}

	memoizer[l] = retVal
	return retVal
}

func Part1(fileContents string) int {

	fileContents = strings.TrimSpace(fileContents)
	grid := turnInto2dGrid(fileContents)
	splitterCount := 0
	for r, line := range grid {
		if r == len(grid) - 1 { break } // all beams made it to the last line, can stop now

		for c, char := range line {
			if char != "S" && char != "|" { continue } // not a beam
			downChar := grid[r+1][c]
			switch downChar {
			case "^":
				splitterCount++
				grid[r+1][c] = "x"
				fallthrough
			case "x":
				grid[r+1][c+1] = "|"
				grid[r+1][c-1] = "|"
			default:
				grid[r+1][c] = "|"
			}
		}
	}
	return splitterCount
}

func Part2(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)

	grid := turnInto2dGrid(fileContents)
	locationsPerLevel := make(map[int]map[Location]int)

	startLocation, _ := func(l []string) (Location, error) {
		for col, char := range l {
			if char == "S" {
				return Location{
					row: 0,
					col: col,
				}, nil
			}
		}
		return Location{}, fmt.Errorf("Couldnt find start location in line: %+v", l)
	}(grid[0])
	locationsPerLevel[0] = make(map[Location]int)
	locationsPerLevel[0][startLocation] = 1

	for r := range grid {
		if r == len(grid) - 1 { break } // all beams made it to the last line, can stop now
		locationsPerLevel[r+1] = make(map[Location]int)
		for loc, cnt := range locationsPerLevel[r] {
			nextLocs := loc.nextLocations(grid)
			for _, nextLoc := range nextLocs {
				if nextLocCnt, ok := locationsPerLevel[r+1][nextLoc]; ok { // location already exists in next level. Add 1 to the count
					locationsPerLevel[r+1][nextLoc] = nextLocCnt + cnt
				} else {
					locationsPerLevel[r+1][nextLoc] = cnt
				}
			}
		}
	}

	total := 0
	for _, cnt := range locationsPerLevel[len(locationsPerLevel)-1] {
		total += cnt
	}
	return total
}

// ====================================================

func Part1Broken(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)
	lines := strings.Split(fileContents, "\n")
	grid := turnInto2dGrid(fileContents)

	beamLocationsByLine := make(map[int]map[Location]bool)
	splitterCount := 0

	beamLocationsByLine[0] = make(map[Location]bool)
	for c, char := range lines[0] {
		if string(char) == "S" {
			location := Location{
				row: 0,
				col: c,
			}
			beamLocationsByLine[0][location] = true
		}
	}

	for rowIdx := range lines {
		if rowIdx == 0 { continue }
		beamLocationsByLine[rowIdx] = make(map[Location]bool)

		prevBeams := beamLocationsByLine[rowIdx-1]
		for beam := range prevBeams {
			nextLocs := beam.nextLocations(grid)
			if len(nextLocs) > 1 { splitterCount++ }
			for _, nextLocation := range nextLocs {
				beamLocationsByLine[rowIdx][nextLocation] = true
			}
		}
	}

	return splitterCount
}

type Grid [][]string
func (g Grid) deepCopy() Grid {
	gridCopy := make(Grid, len(g))
	// for x, l := range g {
	// 	line := make([]string, len(l))
	// 	copy(line, l)
	// 	gridCopy[x] = line
	// }
	for i := range g {
		gridCopy[i] = append([]string(nil), g[i]...)
	}

	return gridCopy
}

func Part2Slow(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)

	gridsPerLevel := make(map[int][]Grid)
	grid := turnInto2dGrid(fileContents)
	gridsPerLevel[0] = []Grid{
		grid,
	}

	for r := range grid {
		gridsPerLevel[r+1] = make([]Grid, 0)
		for _, g := range gridsPerLevel[r] {
			if r == len(g) - 1 { break } // all beams made it to the last line, can stop now

			for c, char := range g[r] {
				if char != "S" && char != "|" { continue } // not a beam
				downChar := g[r+1][c]
				switch downChar {
				case "^":
					g1 := g.deepCopy()
					g2 := g.deepCopy()
					g1[r+1][c-1] = "|"
					g2[r+1][c+1] = "|"
					gridsPerLevel[r+1] = append(gridsPerLevel[r+1], g1)
					gridsPerLevel[r+1] = append(gridsPerLevel[r+1], g2)
				default:
					gPrime := g.deepCopy()
					gPrime[r+1][c] = "|"
					gridsPerLevel[r+1] = append(gridsPerLevel[r+1], gPrime)
				}
			}
		}
	}
	return len(gridsPerLevel[len(grid)-1])
}
