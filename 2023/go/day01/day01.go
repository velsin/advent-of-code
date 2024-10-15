package day01

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	utils "github.com/velsin/advent-of-code/utils/go"
)

func Day01() {
	lines := utils.SplitLines(utils.ReadInput(2023, 1))

	// Part 1
	var lineSumPart1 int

	// Iterate, parse, convert, sum
	for _, line := range lines {
		lineValue, err := strconv.Atoi(parseLine(line))
		if err != nil {
			fmt.Println("Error during type conversion.")
			panic(err)
		}
		lineSumPart1 += lineValue
	}

	fmt.Println("Part 1: ", lineSumPart1)

	// Part 2

	var lineSumPart2 int

	for _, line := range lines {
		lineValue, err := strconv.Atoi(parseLine2(line))
		if err != nil {
			panic(err)
		}
		lineSumPart2 += lineValue
	}

	fmt.Println("Part 2: ", lineSumPart2)
}

func parseLine(line string) string {
	// Extract all the digit characters

	var b strings.Builder

	for _, char := range line {
		if char >= '0' && char <= '9' {
			b.WriteRune(char)
		}
	}

	digits := b.String()
	// Return only the first and last digit characters
	return string(digits[0]) + string(digits[len(digits)-1])

}

func parseLine2(line string) string {
	// Extract all the digit characters, along with text representation of them, using a regex

	var b strings.Builder

	// Can't do lookahead regex in Go stdlib due to linear time guarantee.
	digitRe := regexp.MustCompile(`[0-9]|one|two|three|four|five|six|seven|eight|nine|zero`)

	// To get overlaps, iterate character by character through string and do first match, however
	// this will give O(n^2) complexity
	matches := []string{}
	for i := range line {
		match := digitRe.FindString(line[i:])
		if match == "" {
			break
		} else {
			matches = append(matches, match)
		}
	}

	// Remap the matches to actual digits
	replaceMap := map[string]rune{
		"one":   '1',
		"two":   '2',
		"three": '3',
		"four":  '4',
		"five":  '5',
		"six":   '6',
		"seven": '7',
		"eight": '8',
		"nine":  '9',
		"zero":  '0',
	}

	for _, digit := range matches {
		mappedDigit := replaceMap[digit]
		if mappedDigit == 0 {
			b.WriteString(digit)
		} else {
			b.WriteRune(mappedDigit)
		}
	}

	digits := b.String()
	// Return only the first and last digit characters
	return string(digits[0]) + string(digits[len(digits)-1])
}
