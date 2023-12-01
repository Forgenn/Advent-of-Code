package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type instruction struct {
	ins        string
	val        int
	cyclesToGo int
}

func readInput(filePath string) []instruction {
	file, err := os.Open(filePath)
	input := make([]instruction, 0)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := strings.Split(fileScanner.Text(), " ")
		moves := -1
		if len(line) != 1 {
			moves, _ = strconv.Atoi(line[1])
		}
		cycles := 0
		if line[0] == "addx" {
			cycles = 1
		}
		input = append(input, instruction{ins: line[0], val: moves, cyclesToGo: cycles})
	}
	return input
}

func solve1(input []instruction) (int, [][40]string) {
	CRT := make([][40]string, 6)
	currentRow := 0
	currentCol := 0
	currentSignal := 1
	signalSum := 0
	nOp := 0

	for cycle := 1; ; cycle++ {

		if nOp >= len(input) {
			break
		}

		if cycle != 1 && cycle%40 == 1 {
			currentRow += 1
			currentCol = 0
		}

		if currentCol >= currentSignal-1 && currentCol <= currentSignal+1 {
			CRT[currentRow][currentCol] = "#"
		} else {
			CRT[currentRow][currentCol] = "."
		}

		if cycle == 20 || (cycle+20)%40 == 0 {
			signalSum += currentSignal * cycle
		}

		switch input[nOp].ins {
		case "addx":
			if input[nOp].cyclesToGo != 0 {
				input[nOp].cyclesToGo -= 1
			} else {
				currentSignal += input[nOp].val
				nOp += 1
			}
		case "noop":
			nOp += 1
			//NOOP
		}
		currentCol += 1
	}

	return signalSum, CRT
}

func main() {
	input := readInput("input.txt")
	part1, part2 := solve1(input)
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:")
	for _, val := range part2 {
		fmt.Println(val)
	}
}
