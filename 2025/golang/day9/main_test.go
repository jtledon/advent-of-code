package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
`

func TestPart1(t *testing.T) {
	expected := 50
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
