package utils

import (
	"testing"
)

var testInput1 = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

func TestSplitLines(t *testing.T) {
	res := SplitLines(testInput1)

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
