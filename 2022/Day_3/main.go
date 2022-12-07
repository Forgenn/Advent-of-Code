package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
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
	prioritySum := 0
	globalCommonChar := make([]string, 0)

	for _, value := range input {
		strLen := len(value)
		firstCompMap := make(map[string]bool, 0)
		commonChars := make(map[string]bool, 0)

		firstComp := value[0 : strLen/2]
		secondComp := value[strLen/2:]

		for i := 0; i < len(firstComp); i++ {
			firstCompMap[string(firstComp[i])] = true
		}

		for i := 0; i < len(secondComp); i++ {
			if _, ok := firstCompMap[string(secondComp[i])]; ok {
				if _, ok := commonChars[string(secondComp[i])]; !ok {
					commonChars[string(secondComp[i])] = true
				}
			}
		}

		for i := range commonChars {
			globalCommonChar = append(globalCommonChar, i)
		}

	}

	var charVal rune

	for _, val := range globalCommonChar {
		charVal = []rune(val)[0]
		if unicode.IsUpper(charVal) {
			prioritySum += int(charVal) - 38
		}
		if unicode.IsLower(charVal) {
			prioritySum += int(charVal) - 96
		}
	}

	return prioritySum
}

func getCommon(ruckOne string, ruckTwo string, ruckThree string) string {
	commonChars := ""

	charMap := make(map[string]int, 0)

	for i := 0; i < len(ruckOne); i++ {
		if _, ok := charMap[string(ruckOne[i])]; !ok {
			charMap[string(ruckOne[i])] += 1
		}
	}

	for i := 0; i < len(ruckTwo); i++ {
		if charMap[string(ruckTwo[i])] == 1 {
			charMap[string(ruckTwo[i])] += 1
		}
	}

	for i := 0; i < len(ruckThree); i++ {
		if charMap[string(ruckThree[i])] == 2 {
			charMap[string(ruckThree[i])] += 1
		}
	}

	for i, val := range charMap {
		if val == 3 {
			commonChars = i
		}
	}

	return commonChars

}
func solve2(input []string) int {
	prioritySum := 0
	globalCommonChar := make([]string, 0)

	for i := 0; i < len(input); i += 3 {
		globalCommonChar = append(globalCommonChar, getCommon(input[i], input[i+1], input[i+2]))
	}

	var charVal rune

	for _, val := range globalCommonChar {
		charVal = []rune(val)[0]
		if unicode.IsUpper(charVal) {
			prioritySum += int(charVal) - 38
		}
		if unicode.IsLower(charVal) {
			prioritySum += int(charVal) - 96
		}
	}

	return prioritySum
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
