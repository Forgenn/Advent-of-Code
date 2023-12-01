package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readInputandSolvePart1(filePath string) int {
	file, err := os.Open(filePath)
	var result = 0

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		var lineRes string

		var foundFirst = false
		var lastVal string

		for _, value := range line {
			switch {
			case value >= '0' && value <= '9':
				if !foundFirst {
					lineRes += fmt.Sprint(int(value) - 48)
					foundFirst = true
				}
				lastVal = fmt.Sprint(int(value) - 48)
			}
		}
		fmt.Println(lineRes + lastVal)
		val, _ := strconv.ParseInt(lineRes+lastVal, 10, 64)
		result += int(val)
	}
	return result
}

func readInputandSolvePart2(filePath string) int {
	file, err := os.Open(filePath)
	var result = 0

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	d := strings.NewReplacer( //:DD
		"oneight", "18",
		"twone", "21",
		"fiveight", "58",
		"sevenine", "79",
		"eightwo", "82",
		"threeight", "38",
		"eighthree", "83",
		"nineight", "98",

		"one", "1",
		"two", "2",
		"three", "3",
		"four", "4",
		"five", "5",
		"six", "6",
		"seven", "7",
		"eight", "8",
		"nine", "9",
	)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		line = d.Replace(line)
		var lineRes string

		var foundFirst = false
		var lastVal string

		for _, value := range line {
			switch {
			case value >= '0' && value <= '9':
				if !foundFirst {
					lineRes += fmt.Sprint(int(value) - 48)
					foundFirst = true
				}
				lastVal = fmt.Sprint(int(value) - 48)
			}
		}
		val, _ := strconv.ParseInt(lineRes+lastVal, 10, 64)
		result += int(val)
	}
	return result
}

func main() {
	fmt.Println(readInputandSolvePart2("input.txt"))
}
