package main

import (
	"testing"
)

// go test [-v]
// go test ./...

var sampleInput string = `
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
`

func TestPart1(t *testing.T) {
	expected := 5
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
