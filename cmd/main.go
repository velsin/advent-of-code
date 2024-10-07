package main

import (
	"flag"
	"fmt"
)

// Central runner for all the Go solutions
// type Solution struct {
// 	year int
// 	day int
// 	solve func
// }

func main() {
	yearFlag := flag.Int("year", 0, "Year to run")
	dayFlag := flag.Int("day", 0, "Day to run")

	flag.Parse()

	fmt.Printf("Running Year %d Day %d\n", *yearFlag, *dayFlag)

}