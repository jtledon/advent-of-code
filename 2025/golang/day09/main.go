package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strconv"
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

type Point struct {
	x, y int
}
type Rect struct {
	a, b Point
}

func (r Rect) swapOrder() Rect {
	return Rect{
		a: r.b,
		b: r.a,
	}
}

func Part1(fileContents string) int {
	fileContents = strings.TrimSpace(fileContents)

	pointCombos := make(map[Rect]bool)
	lines := strings.Split(fileContents, "\n")
	for i, a := range lines {
		for j, b := range lines {
			aCoords := strings.Split(a, ",")
			aX, _ := strconv.Atoi(aCoords[0])
			aY, _ := strconv.Atoi(aCoords[1])
			bCoords := strings.Split(b, ",")
			bX, _ := strconv.Atoi(bCoords[0])
			bY, _ := strconv.Atoi(bCoords[1])
			r := Rect{
				a: Point{aX, aY},
				b: Point{bX, bY},
			}
			if _, ok := pointCombos[r.swapOrder()]; !ok && i != j {
				// fmt.Println(r)
				pointCombos[r] = true
			}
		}
	}

	maxArea := 0
	for combo := range pointCombos {
		xDiff := combo.a.x - combo.b.x + 1
		yDiff := combo.a.y - combo.b.y + 1

		area := xDiff * yDiff
		if area < 0 { area *= -1 }

		if area > maxArea {
			maxArea = area
		}
	}

	return maxArea
}

func Part2(fileContents string) int {
	return 0
}
