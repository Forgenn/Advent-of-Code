package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type monkey struct {
	items          []int
	operation      string
	operationVal   string
	testVal        int
	monkeyIfTrue   int
	monkeyIfFalse  int
	itemsInspected int
}

func readInput(filePath string) []monkey {
	file, err := os.Open(filePath)
	input := make([]monkey, 8)
	nMonkey := 0
	var curMonkey []string

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for {
		reachedEnd := !fileScanner.Scan()
		line := fileScanner.Text()
		curMonkey = append(curMonkey, line)
		if line == "" || reachedEnd {
			//Parse items
			monkeyItems := strings.Split(strings.Replace(curMonkey[1][18:], " ", "", -1), ",")
			for _, item := range monkeyItems {
				val, _ := strconv.Atoi(item)
				input[nMonkey].items = append(input[nMonkey].items, val)
			}
			//Parse operation
			operation := strings.Split(curMonkey[2][23:], " ")
			input[nMonkey].operation = operation[0]
			value := operation[1]
			input[nMonkey].operationVal = value
			//Parse test
			testVal := strings.Split(curMonkey[3], " ")
			testValInt, _ := strconv.Atoi(testVal[len(testVal)-1])
			input[nMonkey].testVal = testValInt
			//Parse true cond
			trueMonkey := strings.Split(curMonkey[4], " ")
			trueMonkeyInt, _ := strconv.Atoi(trueMonkey[len(trueMonkey)-1])
			input[nMonkey].monkeyIfTrue = trueMonkeyInt
			//Parse false cond
			falseMonkey := strings.Split(curMonkey[5], " ")
			falseMonkeyInt, _ := strconv.Atoi(falseMonkey[len(falseMonkey)-1])
			input[nMonkey].monkeyIfFalse = falseMonkeyInt
			nMonkey++
			curMonkey = []string{}
		}
		if reachedEnd {
			break
		}
	}
	return input
}

func solve1(input []monkey, rounds int) int {
	monkeyBusiness := 0

	for i := 0; i < rounds; i++ {
		for nMonkey, currentMonkey := range input {
			for _, item := range currentMonkey.items {
				input[nMonkey].itemsInspected += 1
				newWorry := 0

				switch currentMonkey.operation {
				case "*":
					if currentMonkey.operationVal == "old" {
						newWorry = item * item
					} else {
						val, _ := strconv.Atoi(currentMonkey.operationVal)
						newWorry = item * val
					}
				case "+":
					val, _ := strconv.Atoi(currentMonkey.operationVal)
					newWorry = item + val
				}

				newWorry = int(math.Round(float64(newWorry / 3)))

				if newWorry%currentMonkey.testVal == 0 {
					input[currentMonkey.monkeyIfTrue].items = append(input[currentMonkey.monkeyIfTrue].items, newWorry)
				} else {
					input[currentMonkey.monkeyIfFalse].items = append(input[currentMonkey.monkeyIfFalse].items, newWorry)
				}

				/*if len(input[nMonkey].items) == nItem {
					newItems = input[nMonkey].items[:len(input[nMonkey].items)-1]
				} else if len(input[nMonkey].items) > 1 {
					newItems = append(input[nMonkey].items[:nItem], input[nMonkey].items[nItem+1:]...)
				} else if len(input[nMonkey].items) == 1 {
					newItems = []int{}
				}*/
			}
			input[nMonkey].items = []int{}
		}

	}
	inspections := []int{}
	for _, monkeyN := range input {
		inspections = append(inspections, monkeyN.itemsInspected)
	}
	sort.Ints(inspections)
	monkeyBusiness = inspections[len(inspections)-1] * inspections[len(inspections)-2]
	return monkeyBusiness
}

func solve2(input []monkey, rounds int) int {
	monkeyBusiness := 0
	newModulo := 1
	for _, cMonkey := range input {
		newModulo *= cMonkey.testVal
	}

	for i := 0; i < rounds; i++ {
		for nMonkey, currentMonkey := range input {
			for _, item := range currentMonkey.items {
				input[nMonkey].itemsInspected += 1
				newWorry := 0

				switch currentMonkey.operation {
				case "*":
					if currentMonkey.operationVal == "old" {
						newWorry = item * item
					} else {
						val, _ := strconv.Atoi(currentMonkey.operationVal)
						newWorry = item * val
					}
				case "+":
					val, _ := strconv.Atoi(currentMonkey.operationVal)
					newWorry = item + val
				}

				newWorry = newWorry % newModulo

				if newWorry%currentMonkey.testVal == 0 {
					input[currentMonkey.monkeyIfTrue].items = append(input[currentMonkey.monkeyIfTrue].items, newWorry)
				} else {
					input[currentMonkey.monkeyIfFalse].items = append(input[currentMonkey.monkeyIfFalse].items, newWorry)
				}
			}
			input[nMonkey].items = []int{}
		}

	}
	inspections := []int{}
	for _, monkeyN := range input {
		inspections = append(inspections, monkeyN.itemsInspected)
	}
	sort.Ints(inspections)
	monkeyBusiness = inspections[len(inspections)-1] * inspections[len(inspections)-2]
	return monkeyBusiness
}

func main() {
	input := readInput("input.txt")
	fmt.Println("Part 1:", solve1(input, 20))
	input = readInput("input.txt")
	fmt.Println("Part 2:1000", solve2(input, 10000))

}
