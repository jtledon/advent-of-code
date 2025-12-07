package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
`

func TestPart1(t *testing.T) {
	expected := 0
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
