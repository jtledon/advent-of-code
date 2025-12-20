package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
`

func TestPart1(t *testing.T) {
	expected := 4277556
	result := Part1(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	expected := 3263827
	result := Part2(sampleInput)
	if expected != result {
		t.Fatalf("Expected: %d, Received: %d", expected, result)
	}
}
