package main

import (
	"bufio"
	"fmt"
	"image"
	"math"
	"os"
	"strconv"
	"strings"
)

type move struct {
	direction string
	nMoves    int
}

func readInput(filePath string) []move {
	file, err := os.Open(filePath)
	input := make([]move, 0)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := strings.Split(fileScanner.Text(), " ")
		moves, _ := strconv.Atoi(line[1])
		input = append(input, move{direction: line[0], nMoves: moves})
	}
	return input
}

func isNear(head image.Point, tail image.Point) bool {
	distance := math.Sqrt(math.Pow(float64(tail.X-head.X), 2) + math.Pow(float64(tail.Y-head.Y), 2))
	return distance < 2
}

func moveTail(head image.Point, tail image.Point) image.Point {

	if tail.X != head.X {
		if tail.X < head.X {
			tail.X += 1
		} else {
			tail.X -= 1
		}
	}

	if tail.Y != head.Y {
		if tail.Y < head.Y {
			tail.Y += 1
		} else {
			tail.Y -= 1
		}
	}
	return tail
}
func solve1(input []move) int {
	tailVisitedPostions := make(map[image.Point]int)
	headPosition := image.Point{}
	tailPosition := image.Point{}

	for _, instruction := range input {
		for i := 0; i < instruction.nMoves; i++ {
			switch instruction.direction {
			case "R":
				headPosition = headPosition.Add(image.Point{Y: 1})
			case "L":
				headPosition = headPosition.Add(image.Point{Y: -1})
			case "U":
				headPosition = headPosition.Add(image.Point{X: -1})
			case "D":
				headPosition = headPosition.Add(image.Point{X: 1})
			}

			if isNear(headPosition, tailPosition) {
				continue
			}

			tailPosition = moveTail(headPosition, tailPosition)

			if _, ok := tailVisitedPostions[tailPosition]; !ok {
				tailVisitedPostions[tailPosition] = 1
			}

		}
	}
	return len(tailVisitedPostions) + 1
}

func solve2(input []move) int {
	tailVisitedPostions := make(map[image.Point]int)
	knots := make([]image.Point, 10)

	for _, instruction := range input {
		for i := 0; i < instruction.nMoves; i++ {
			for j := 1; j < len(knots); j++ {
				if j == 1 {
					switch instruction.direction {
					case "R":
						knots[j-1] = knots[j-1].Add(image.Point{Y: 1})
					case "L":
						knots[j-1] = knots[j-1].Add(image.Point{Y: -1})
					case "U":
						knots[j-1] = knots[j-1].Add(image.Point{X: -1})
					case "D":
						knots[j-1] = knots[j-1].Add(image.Point{X: 1})
					}
				}

				if isNear(knots[j-1], knots[j]) {
					continue
				}

				knots[j] = moveTail(knots[j-1], knots[j])

				if j == len(knots)-1 {
					if _, ok := tailVisitedPostions[knots[j]]; !ok {
						tailVisitedPostions[knots[j]] = 1
					}
				}
			}

		}
	}
	return len(tailVisitedPostions) + 1
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
