package main

import (
	"bufio"
	"fmt"
	"image"
	"os"
)

func readInput(filePath string) (map[image.Point]rune, image.Point, image.Point) {
	file, err := os.Open(filePath)
	input := make([]string, 0)
	adjacencySlice := make(map[image.Point]rune, 0)
	source := image.Point{}
	destination := image.Point{}

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}

	for i, line := range input {
		for j, char := range line {
			adjacencySlice[image.Point{X: i, Y: j}] = char

			if string(char) == "S" {
				source.X = i
				source.Y = j
			}
			if string(char) == "E" {
				destination.X = i
				destination.Y = j
			}
		}

	}

	return adjacencySlice, source, destination
}

func solve1(input map[image.Point]rune, source image.Point, destination image.Point) (int, int) {
	var shortest *image.Point
	dist := map[image.Point]int{destination: 0}
	queue := []image.Point{destination}

	dist[destination] = 0

	input[source] = 'a'
	input[destination] = 'z'

	for len(queue) > 0 {

		cur := queue[0]
		queue = queue[1:]

		for _, d := range []image.Point{{0, -1}, {1, 0}, {0, 1}, {-1, 0}} {
			next := cur.Add(d)

			if input[cur] == 'a' && shortest == nil {
				shortest = &image.Point{X: cur.X, Y: cur.Y}
			}

			_, exists := dist[next]
			_, valid := input[next]
			if !exists && valid && input[cur] <= input[next]+1 {
				dist[next] = dist[cur] + 1
				queue = append(queue, next)

			}
		}
	}
	return dist[source], dist[*shortest]
}

func main() {
	input, source, destination := readInput("input.txt")
	part1, part2 := solve1(input, source, destination)

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}
