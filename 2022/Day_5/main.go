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

type instruction struct {
	quantity int
	from     int
	to       int
}

func parseInstructions(arrangement string) instruction {
	splitArrangement := strings.Split(arrangement, " ")

	quantity, _ := strconv.Atoi(splitArrangement[1])
	from, _ := strconv.Atoi(splitArrangement[3])
	to, _ := strconv.Atoi(splitArrangement[5])

	return instruction{quantity: quantity,
		from: from - 1,
		to:   to - 1}

}

var stacksNum = 9

func solve1(input []string) string {

	readInstructions := false
	instructionsSlice := make([]instruction, 0)
	cratesQueuesSlice := make([][]string, stacksNum)

	for _, val := range input {
		if val == "" {
			readInstructions = true
			continue
		}

		if readInstructions {
			instructionsSlice = append(instructionsSlice, parseInstructions(val))
			continue
		}

		ranges := strings.ReplaceAll(strings.ReplaceAll(val, "[", " "), "]", " ")
		stackN := 0
		for i := 0; i < stacksNum; i += 1 {

			if string(ranges[(i*4)+1]) != " " {
				cratesQueuesSlice[stackN] = append(cratesQueuesSlice[stackN], string(ranges[(i*4)+1]))
				stackN += 1
			} else {
				stackN += 1
			}
		}

	}

	for _, instruction := range instructionsSlice {
		for i := 0; i < instruction.quantity; i++ {
			if len(cratesQueuesSlice[instruction.from]) != 0 {
				cratesQueuesSlice[instruction.to] = append([]string{cratesQueuesSlice[instruction.from][0]}, cratesQueuesSlice[instruction.to]...)
				cratesQueuesSlice[instruction.from] = cratesQueuesSlice[instruction.from][1:]
			}
		}
	}
	topCrates := ""
	for _, crateSlice := range cratesQueuesSlice {
		topCrates = topCrates + crateSlice[0]
	}
	return topCrates
}

func solve2(input []string) string {
	readInstructions := false
	instructionsSlice := make([]instruction, 0)
	cratesQueuesSlice := make([][]string, stacksNum)

	for _, val := range input {
		if val == "" || string(val[1]) == "1" {
			readInstructions = true
			continue
		}

		if readInstructions {
			instructionsSlice = append(instructionsSlice, parseInstructions(val))
			continue
		}

		ranges := strings.ReplaceAll(strings.ReplaceAll(val, "[", " "), "]", " ")
		stackN := 0
		for i := 0; i < stacksNum; i += 1 {

			if string(ranges[(i*4)+1]) != " " {
				cratesQueuesSlice[stackN] = append(cratesQueuesSlice[stackN], string(ranges[(i*4)+1]))
				stackN += 1
			} else {
				stackN += 1
			}
		}

	}

	for _, instruction := range instructionsSlice {
		if len(cratesQueuesSlice[instruction.from]) != 0 {
			cratesQueuesSlice[instruction.to] = append(append([]string(nil), cratesQueuesSlice[instruction.from][0:instruction.quantity]...), cratesQueuesSlice[instruction.to]...)
			cratesQueuesSlice[instruction.from] = cratesQueuesSlice[instruction.from][instruction.quantity:]
		}
	}
	topCrates := ""
	for _, crateSlice := range cratesQueuesSlice {
		topCrates = topCrates + crateSlice[0]
	}
	return topCrates
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
