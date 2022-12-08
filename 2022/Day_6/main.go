package main

import (
	"bufio"
	"fmt"
	"os"
)

func readInput(filePath string) []string {
	file, err := os.Open(filePath)
	input := make([]string, 0)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}
	return input
}

func solve1(input []string) int {
	nMaker := 0
	gotMarker := 0

	for _, value := range input {
		charMap := make(map[string]int, 0)
		for i := 0; i < len(value)-4; i++ {
			if _, ok := charMap[string(value[i])]; ok {
				charMap[string(value[i])] += 1
			} else {
				charMap[string(value[i])] = 1
			}
			if i >= 3 {
				for _, val := range charMap {
					if val == 1 {
						gotMarker += 1
					}
				}
				if gotMarker == 4 {
					return i + 1
				} else {
					gotMarker = 0
				}
				charMap[string(value[i-3])] -= 1
			}

		}
	}

	return nMaker
}

func solve2(input []string) int {
	nMaker := 0
	gotMarker := 0

	for _, value := range input {
		charMap := make(map[string]int, 0)
		for i := 0; i < len(value); i++ {
			if _, ok := charMap[string(value[i])]; ok {
				charMap[string(value[i])] += 1
			} else {
				charMap[string(value[i])] = 1
			}
			if i >= 13 {
				for _, val := range charMap {
					if val == 1 {
						gotMarker += 1
					}
				}
				if gotMarker == 14 {
					return i + 1
				} else {
					gotMarker = 0
				}
				charMap[string(value[i-13])] -= 1

			}

		}
	}

	return nMaker
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
