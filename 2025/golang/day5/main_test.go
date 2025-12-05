package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
3-5
10-14
16-20
12-18

1
5
8
11
17
32
`

func TestPart1(t *testing.T) {
	expected := 3
	result := Part1(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	expected := 14
	result := Part2(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}
