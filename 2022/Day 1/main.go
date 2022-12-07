package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readInputandSolvePart1(filePath string) []string {
	file, err := os.Open(filePath)
	input := make([]string, 0)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	currentCalVal := 0
	currentElf := 1
	maxElvesCalories := make([]int, 3)

	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
		val, _ := strconv.Atoi(fileScanner.Text())
		if fileScanner.Text() == "" {

			if currentCalVal > maxElvesCalories[0] {
				maxElvesCalories[2] = maxElvesCalories[1]
				maxElvesCalories[1] = maxElvesCalories[0]
				maxElvesCalories[0] = currentCalVal
			} else if currentCalVal > maxElvesCalories[1] {
				maxElvesCalories[2] = maxElvesCalories[1]
				maxElvesCalories[1] = currentCalVal
			} else if currentCalVal > maxElvesCalories[2] {
				maxElvesCalories[2] = currentCalVal
			}

			currentElf += 1
			currentCalVal = 0
		}
		currentCalVal += val
	}

	totalCal := 0
	for _, value := range maxElvesCalories {
		totalCal += value
	}
	fmt.Println("Star 1: ", maxElvesCalories[0])
	fmt.Println("Star 2: ", totalCal)
	file.Close()
	return input
}

func main() {
	readInputandSolvePart1("input.txt")
}
