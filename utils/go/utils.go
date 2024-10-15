package utils

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func ReadInput(year int, day int) string {
	data, err := os.ReadFile(filepath.Join(
		os.Getenv("AOC_DIRECTORY"),
		fmt.Sprintf("%d/data/day%02d.txt", year, day),
	))

	if err != nil {
		fmt.Println("Error reading file.")
		panic(err)
	}

	return string(data)
}

func SplitLines(input string) []string {
	return strings.Split(strings.TrimSpace(input), "\n")
}
