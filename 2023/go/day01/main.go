package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Let's just start with naive implementation of putting everything in main.
// TODO: Create a file reader (and parser?) util in the root?
func main() {
	data, err := os.ReadFile("/home/vidar/code/advent-of-code/2023/data/day01.txt")

	if err != nil {
		fmt.Println("Error reading file.")
		panic(err)
	}

	input := string(data)
	lines := strings.Split(strings.TrimSpace(input), "\n")

	var lineSum int

	// Iterate, parse, convert, sum
	for _, line := range lines {
		lineValue, err := strconv.Atoi(parseLine(line))
		if err != nil {
			fmt.Println("Error during type conversion.")
			panic(err)
		}
		lineSum += lineValue
	}

	fmt.Println("Part 1: ", lineSum)
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
