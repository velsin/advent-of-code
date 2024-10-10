package main

import (
	"flag"
	"fmt"

	"github.com/velsin/advent-of-code/2023/go/day01"
)

// Central runner for all the Go solutions
// type Solution struct {
// 	year int
// 	day int
// 	solve func
// }

func main() {
	// Currently no support for other years, we only have 2023. Refactory once we do
	yearFlag := flag.Int("year", 2023, "Year to run")
	dayFlag := flag.Int("day", 0, "Day to run")

	flag.Parse()

	fmt.Printf("Running year %d day %d\n", *yearFlag, *dayFlag)

	switch *dayFlag {
	case 1:
		day01.Day01()
	default:
		fmt.Println("Day not implemented.")
	}
}
