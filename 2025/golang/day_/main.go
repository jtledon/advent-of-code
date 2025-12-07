package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func main() {
	_, file, _, ok := runtime.Caller(0)
	if !ok { panic("Unable to fetch path of current file") }
	dir := filepath.Base(filepath.Dir(file))
	day := string(dir[len(dir) - 1])

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
	fileContents = strings.TrimSpace(fileContents)
	for line := range strings.SplitSeq(fileContents, "\n") {
		fmt.Println(line)
	}
	return 0
}

func Part2(fileContents string) int {
	return 0
}
