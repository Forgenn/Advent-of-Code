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

func parseInstruction(instruction string) ([]string, bool) {
	if string(instruction[0]) == "$" {
		return strings.Split(instruction[2:], " "), true
	}
	return []string{instruction}, false
}

func getSizeofDirs(dirVals []string, dirMap map[string][]string) int {
	dirSize := 0

	for _, value := range dirVals {
		if strings.Contains(value, " ") {
			tmp, _ := strconv.Atoi(strings.Split(value, " ")[0])
			dirSize += tmp
		} else {
			dirSize += getSizeofDirs(dirMap[value], dirMap)
		}
	}

	return dirSize
}

func stackToString(dirStack []string) string {
	path := ""

	for i := len(dirStack) - 1; i >= 0; i-- {
		path += dirStack[i]
	}

	return path
}
func solve1(input []string) int {

	currentDir := make([]string, 0)
	dirMap := make(map[string][]string, 0)
	totalSize := 0

	for _, value := range input {
		parsedInstruction, isInstruction := parseInstruction(value)
		switch {
		case len(parsedInstruction) > 1 && isInstruction:
			if string(parsedInstruction[1]) == ".." {
				currentDir = currentDir[1:]
			} else {
				currentDir = append([]string{parsedInstruction[1]}, currentDir...)
			}
		case len(parsedInstruction) == 1 && isInstruction:
			continue

		case len(parsedInstruction) == 1 && !isInstruction:
			if strings.Contains(parsedInstruction[0], "dir") {
				dirMap[stackToString(currentDir)] = append(dirMap[stackToString(currentDir)], stackToString(currentDir)+parsedInstruction[0][strings.LastIndex(parsedInstruction[0], " ")+1:])
			} else {
				dirMap[stackToString(currentDir)] = append(dirMap[stackToString(currentDir)], parsedInstruction...)
			}

		}
	}

	for dir, values := range dirMap {
		sizeDir := getSizeofDirs(values, dirMap)
		_ = dir
		if sizeDir <= 100000 {
			totalSize += sizeDir
		}

	}
	return totalSize
}

func solve2(input []string) int {

	currentDir := make([]string, 0)
	dirMap := make(map[string][]string, 0)

	for _, value := range input {
		parsedInstruction, isInstruction := parseInstruction(value)
		switch {
		case len(parsedInstruction) > 1 && isInstruction:
			if string(parsedInstruction[1]) == ".." {
				currentDir = currentDir[1:]
			} else {
				currentDir = append([]string{parsedInstruction[1]}, currentDir...)
			}
		case len(parsedInstruction) == 1 && isInstruction:
			continue

		case len(parsedInstruction) == 1 && !isInstruction:
			if strings.Contains(parsedInstruction[0], "dir") {
				dirMap[stackToString(currentDir)] = append(dirMap[stackToString(currentDir)], stackToString(currentDir)+parsedInstruction[0][strings.LastIndex(parsedInstruction[0], " ")+1:])
			} else {
				dirMap[stackToString(currentDir)] = append(dirMap[stackToString(currentDir)], parsedInstruction...)
			}

		}
	}

	minSize := 9999999999999999
	spaceNeeded := 0
	dirSizes := make([]int, 0)
	_, _ = spaceNeeded, minSize

	for dir, values := range dirMap {
		sizeDir := getSizeofDirs(values, dirMap)
		dirSizes = append(dirSizes, sizeDir)

		if dir == "/" {
			unusedSpace := 70000000 - sizeDir
			spaceNeeded = 30000000 - unusedSpace
		}

	}
	for _, sizeDir := range dirSizes {
		if sizeDir >= spaceNeeded && sizeDir < minSize {
			minSize = sizeDir
		}
	}
	return minSize
}

func main() {
	input := readInput("input.txt")

	fmt.Println("Part 1:", solve1(input))
	fmt.Println("Part 2:", solve2(input))
}
