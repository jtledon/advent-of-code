package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
`

func TestPart1(t *testing.T) {
	expected := 7
	result := Part1(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	expected := 0
	result := Part2(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}
