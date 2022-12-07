package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

func parseString(in string) int {
	val, _ := strconv.Atoi(in)
	return val
}

func solve1(input []string) int {

	globalCounter := 0

	for _, value := range input {
		ranges := strings.Split(value, ",")
		firstRange := strings.Split(ranges[0], "-")
		secondRange := strings.Split(ranges[1], "-")

		strconv.Atoi(firstRange[0])

		if (parseString(firstRange[0]) >= parseString(secondRange[0]) && parseString(firstRange[1]) <= parseString(secondRange[1])) ||
			(parseString(secondRange[0]) >= parseString(firstRange[0]) && parseString(secondRange[1]) <= parseString(firstRange[1])) {
			globalCounter += 1
		}

	}

	return globalCounter
}

func solve2(input []string) int {

	globalCounter := 0

	for _, value := range input {
		ranges := strings.Split(value, ",")
		firstRange := strings.Split(ranges[0], "-")
		secondRange := strings.Split(ranges[1], "-")

		strconv.Atoi(firstRange[0])

		if (parseString(firstRange[0]) >= parseString(secondRange[0]) && parseString(firstRange[0]) <= parseString(secondRange[1])) ||
			(parseString(secondRange[0]) >= parseString(firstRange[0]) && parseString(secondRange[0]) <= parseString(firstRange[1])) {
			globalCounter += 1
		}

	}

	return globalCounter
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
