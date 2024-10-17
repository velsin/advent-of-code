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
			return 0
		}
	}
	return g.id
}

func (g *Game) returnPower() int {
	var maxDraws = map[string]int{
		"red":   0,
		"green": 0,
		"blue":  0,
	}
	for _, draw := range g.draws {
		if draw.count > maxDraws[draw.color] {
			maxDraws[draw.color] = draw.count
		}
	}

	var res int = 1
	for _, val := range maxDraws {
		res *= val
	}
	return res
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

	id, err := strconv.Atoi(strings.Split(game_string, " ")[1])
	if err != nil {
		panic(err)
	}
	var draw_slice = []Draw{}

	for _, draws_string := range strings.Split(draws, ";") {
		for _, draw_string := range strings.Split(draws_string, ",") {
			draw_slice = append(draw_slice, NewDraw(strings.Trim(draw_string, " ")))
		}
	}
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
		res := game.returnValue(maxCountMap)
		sum += res
	}

	return sum
}

func part2(input string) int {

	lines := utils.SplitLines(input)
	var games = []*Game{}

	for _, line := range lines {
		games = append(games, parseLine(line))
	}

	var sum int = 0
	for _, game := range games {
		res := game.returnPower()
		sum += res

	return sum
}