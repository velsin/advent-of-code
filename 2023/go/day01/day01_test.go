package day01

import (
	"testing"
)

var testInput1 = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

var testInput2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

// Look at some edge cases where we can have overlapping runes contributing to the same number
// This can happen with: 'twone', 'nineight', 'oneight', 'threeight', 'fiveight', 'eightwo',
// 'eighthree'. These DO occur in the data, and trailing ones will affect total.
var testInput3 = `1vvtcclvnineight
fbnbj5two3twoneg
sqrdkpzeight936oneighth
three7qfnzmbqmnh563six55eightwot
`

func TestSplitLines(t *testing.T) {
	res := splitLines(testInput1)

	expected := []string{
		"1abc2",
		"pqr3stu8vwx",
		"a1b2c3d4e5f",
		"treb7uchet",
	}

	if len(res) != len(expected) {
		t.Errorf("splitLines returned an array with %d lines, expected %d", len(res), len(expected))
	}

	for i, val := range res {
		if val != expected[i] {
			t.Errorf("splitLines error on line %d. Result: %q, Expected: %q", i, val, expected[i])
		}
	}
}

func TestParseLine(t *testing.T) {
	input := splitLines(testInput1)

	var res = make([]string, len(input))
	for i, line := range input {
		res[i] = parseLine(line)
	}

	expected := []string{
		"12",
		"38",
		"15",
		"77",
	}

	for i, val := range res {
		if val != expected[i] {
			t.Errorf("parseLine error on line %d with value %q. Result: %q, Expected: %q",
				i, input[i], val, expected[i])
		}
	}

}

func TestParseLine2(t *testing.T) {
	input := splitLines(testInput2)

	var res = make([]string, len(input))
	for i, line := range input {
		res[i] = parseLine2(line)
	}

	expected := []string{
		"29",
		"83",
		"13",
		"24",
		"42",
		"14",
		"76",
	}

	for i, val := range res {
		if val != expected[i] {
			t.Errorf("parseLine error on line %d with value %q. Result: %q, Expected: %q",
				i, input[i], val, expected[i])
		}
	}
}

func TestParseLine2EdgeCases(t *testing.T) {
	input := splitLines(testInput3)

	var res = make([]string, len(input))
	for i, line := range input {
		res[i] = parseLine2(line)
	}

	expected := []string{
		"18",
		"51",
		"88",
		"32",
	}

	for i, val := range res {
		if val != expected[i] {
			t.Errorf("parseLine error on line %d with value %q. Result: %q, Expected: %q",
				i, input[i], val, expected[i])
		}
	}
}
