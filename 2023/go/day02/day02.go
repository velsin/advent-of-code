package day02

import (
	"fmt"
	"strconv"
	"strings"

	utils "github.com/velsin/advent-of-code/utils/go"
)

func Day02() {

	input := utils.ReadInput(2023, 2)

	res1 := part1(input)
	fmt.Println("Part 1: ", res1)

	res2 := part2(input)
	fmt.Println("Part 2: ", res2)

}

// Let's try out a more object oriented approach instead of straight string processing, even though
// it will be less efficient in this case
type Game struct {
	id    int
	draws []Draw
}

func (g *Game) returnValue(maxCountMap map[string]int) int {
	for _, draw := range g.draws {
		if draw.isInvalid(maxCountMap[draw.color]) == true {
			fmt.Println("invalid draw:", draw)
			return 0
		}
	}
	return g.id
}

type Draw struct {
	count int
	color string
}

func (d *Draw) isInvalid(maxCount int) bool {
	if d.count > maxCount {
		return true
	}
	return false
}

func NewDraw(input string) Draw {
	split := strings.Split(input, " ")
	count, err := strconv.Atoi(split[0])
	if err != nil {
		panic(err)
	}
	return Draw{count: count, color: strings.Trim(split[1], ",")}

}

func parseLine(input string) *Game {

	game_string := strings.Split(input, ":")[0]
	draws := strings.Split(input, ":")[1]
	// fmt.Println("game string", game_string)
	// fmt.Println("draws", draws)

	id, err := strconv.Atoi(strings.Split(game_string, " ")[1])
	if err != nil {
		panic(err)
	}
	var draw_slice = []Draw{}

	for _, draws_string := range strings.Split(draws, ";") {
		// fmt.Println("draws_string:", draws_string)
		for _, draw_string := range strings.Split(draws_string, ",") {
			draw_slice = append(draw_slice, NewDraw(strings.Trim(draw_string, " ")))
		}
		// fmt.Println("draw slice", draw_slice)
	}

	fmt.Println("draw slice from line parse: ", draw_slice)

	var game = &Game{
		id:    id,
		draws: draw_slice,
	}

	return game
}

func part1(input string) int {

	lines := utils.SplitLines(input)
	var games = []*Game{}

	var maxCountMap = map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	for _, line := range lines {
		games = append(games, parseLine(line))
	}

	var sum int = 0
	for _, game := range games {
		fmt.Println("game:", game.id, game.draws)
		res := game.returnValue(maxCountMap)
		fmt.Println("game is valid:", res > 0)
		sum += res
		fmt.Println("sum:", sum, "\n")
	}

	return sum
}

func part2(input string) int {
	return 1
}
