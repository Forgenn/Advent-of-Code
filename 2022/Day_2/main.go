package main

import (
	"bufio"
	"fmt"
	"os"
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

func solve1(input []string) int {
	/*const (
		A = "ROCK"
		X = "ROCK"
		B = "PAPER"
		Y = "PAPER"
		C = "SCISSOR"
		Z = "SCISSOR"
	)*/

	totalScore := 0

	for _, val := range input {
		moves := strings.Split(val, " ")
		oppMove, myMove := moves[0], moves[1]

		switch myMove {
		case "X":
			totalScore += 1

			if oppMove == "C" {
				totalScore += 6
			}

			if oppMove == "A" {
				totalScore += 3
			}

		case "Y":
			totalScore += 2

			if oppMove == "A" {
				totalScore += 6
			}

			if oppMove == "B" {
				totalScore += 3
			}

		case "Z":
			totalScore += 3

			if oppMove == "B" {
				totalScore += 6
			}

			if oppMove == "C" {
				totalScore += 3
			}
		}

	}

	return totalScore
}

func solve2(input []string) int {
	/*const (
		A = "ROCK"
		X = "ROCK"
		B = "PAPER"
		Y = "PAPER"
		C = "SCISSOR"
		Z = "SCISSOR"
	)*/

	totalScore := 0

	for _, val := range input {
		moves := strings.Split(val, " ")
		oppMove, myMove := moves[0], moves[1]

		switch oppMove {
		case "A":

			if myMove == "Z" {
				totalScore += 8
			}

			if myMove == "Y" {
				totalScore += 3 + 1
			}

			if myMove == "X" {
				totalScore += 3
			}

		case "B":
			if myMove == "Z" {
				totalScore += 6 + 3
			}

			if myMove == "Y" {
				totalScore += 3 + 2
			}

			if myMove == "X" {
				totalScore += 1
			}

		case "C":
			if myMove == "Z" {
				totalScore += 6 + 1
			}

			if myMove == "Y" {
				totalScore += 3 + 3
			}

			if myMove == "X" {
				totalScore += 2
			}
		}

	}

	return totalScore
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
