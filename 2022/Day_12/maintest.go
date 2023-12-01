package main

import (
	"fmt"
	"image"
	"os"
	"strings"
)

func main() {
	input, _ := os.ReadFile("input.txt")

	var start, end image.Point
	height := map[image.Point]rune{}
	for x, s := range strings.Fields(string(input)) {
		for y, r := range s {
			height[image.Point{x, y}] = r
			if r == 'S' {
				start = image.Point{x, y}
			} else if r == 'E' {
				end = image.Point{x, y}
			}
		}
	}
	height[start], height[end] = 'a', 'z'

	dist := map[image.Point]int{end: 0}
	queue := []image.Point{end}
	var shortest *image.Point

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if height[cur] == 'a' && shortest == nil {
			shortest = &cur
		}

		for _, d := range []image.Point{{0, -1}, {1, 0}, {0, 1}, {-1, 0}} {
			newCoord := cur.Add(d)

			if newCoord.X < 0 || newCoord.X >= len(input) || newCoord.Y < 0 || newCoord.Y >= len(input[0]) {
				continue
			}
			if visited[newCoord] {
				continue
			}

		}
	}

	fmt.Println(dist[start])
	fmt.Println(dist[*shortest])
}
