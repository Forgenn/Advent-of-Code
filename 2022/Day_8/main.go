package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type coord struct {
	x int
	y int
}

func readInput(filePath string) (map[coord]int, int) {
	file, err := os.Open(filePath)
	input := make(map[coord]int, 0)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	lines := 0

	for fileScanner.Scan() {
		for i, val := range fileScanner.Text() {

			input[coord{x: lines, y: i}], _ = strconv.Atoi(string(val))
		}
		lines += 1
	}

	/*for x := 0; x < lines; x++ {
		for y := 0; y < lines; y++ {
			if x == 0 || y == 0 || y == lines-1 || x == lines-1 {
				input[coord{x: x, y: y}] = true
				input[coord{x: x, y: y}] = true
			}
		}
	}*/
	return input, lines
}

func isVisible(currentPoint coord, height int, input map[coord]int) (bool, int) {
	visibility := false
	score := 1
	directionsToCheck := []coord{{0, -1}, {1, 0}, {0, 1}, {-1, 0}}

	for _, nextDir := range directionsToCheck {
		direction := nextDir
		for i := 1; ; i++ {
			newCoord := coord{x: currentPoint.x + direction.x, y: currentPoint.y + direction.y}
			nextHeight, exists := input[newCoord]

			if !exists { // We have reached the end of the map without findign a tree bigger
				visibility = true
				score *= i - 1
				break
			} else if nextHeight >= height { // If tree bigger, check next direction
				score *= i
				break
			}

			direction = coord{x: direction.x + nextDir.x, y: direction.y + nextDir.y}
		}
	}

	return visibility, score
}

func solve1(input map[coord]int, length int) (int, int) {
	visibleTrees := 0
	maxScore := -99999
	for x := 1; x < length-1; x++ {
		for y := 1; y < length-1; y++ {
			visibility, score := isVisible(coord{x: x, y: y}, input[coord{x: x, y: y}], input)
			if visibility {
				visibleTrees += 1
			}
			if score > maxScore {
				maxScore = score
			}
		}
	}
	return visibleTrees + ((length * 4) - 4), maxScore
}

func main() {
	input, length := readInput("input.txt")
	part1, part2 := solve1(input, length)
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}
