package day02

import (
	"testing"
)

var testInput1 = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`

func TestParseLine(t *testing.T) {
	// Test that line parsing into our intended struct works
	// input := utils.SplitLines(testInput1)

	// var res = make([]string, len(input))
	// for i, line := range input {
	// 	res[i] = parseLine(line)
	// }

	// expected := []string{
	// 	"12",
	// 	"38",
	// 	"15",
	// 	"77",
	// }

	// for i, val := range res {
	// 	if val != expected[i] {
	// 		t.Errorf("parseLine error on line %d with value %q. Result: %q, Expected: %q",
	// 			i, input[i], val, expected[i])
	// 	}
	// }
}

func TestPart1(t *testing.T) {
	res := part1(testInput1)
	expected := 8

	if res != expected {
		t.Errorf("Part 1 solution is incorrect on test input. Result: %d, Expected: %d",
			res, expected)
	}

}

func TestPart2(t *testing.T) {
	res := part2(testInput1)
	expected := 2286

	if res != expected {
		t.Errorf("Part 2 solution is incorrect on test input. Result: %d, Expected: %d",
			res, expected)
	}

}
