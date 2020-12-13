package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"sync"
)

func seqPartOne(nums []int, target int) int {
	for i, num1 := range nums {
		for j, num2 := range nums {
			if i == j {
				continue
			}
			if num1 + num2 == target {
				return num1 * num2
			}
		}
	}
	return 0
}

func seqPartTwo(nums []int, target int) int {
	for i, num1 := range nums {
		for j, num2 := range nums {
			if i == j {
				continue
			}
			for k, num3 := range nums {
				if i == k || j == k {
					continue
				}
				if num1 + num2 + num3 == target {
					return num1 * num2 * num3
				}
			}
		}
	}
	return 0
}

func searchForMatch(c chan int, nums *[]int, ind int, target *int) {
	num := (*nums)[ind]
	for i, _ := range *nums {
		if ind == i {
			continue
		}
		if num + (*nums)[i] == *target {
			c <- num * (*nums)[i]
		}
	}
}

func parPartOne(nums []int, target int) int {
	c := make(chan int)
	for i, _ := range nums {
		go searchForMatch(c, &nums, i, &target)
	}
	res :=<- c
	return res
}

var activeWorkers = 0
var mtx = &sync.Mutex{}

func searchForMatchTwoSum(c chan int, nums *[]int, ind1 int, ind2 int, target *int) {
	num := (*nums)[ind1] + (*nums)[ind2]
	for i, _ := range *nums {
		if ind1 == i || ind2 == i {
			continue
		}
		if num + (*nums)[i] == *target {
			c <- (*nums)[ind1] * (*nums)[ind2] * (*nums)[i]
		}
	}
	mtx.Lock()
	activeWorkers--
	mtx.Unlock()
}

func searchTwoSum(c chan int, nums *[]int, ind int, target *int, maxWorkers int) {
	for i, _ := range *nums {
		if ind == i {
			continue
		}
		for true {
			if activeWorkers < maxWorkers {
				mtx.Lock()
				go searchForMatchTwoSum(c, nums, ind, i, target)
				activeWorkers++
				mtx.Unlock()
				break
			}
		}
	}
	mtx.Lock()
	activeWorkers--
	mtx.Unlock()
}

func manageSearch(c chan int, nums []int, target int, maxWorkers int) {
	for i, _ := range nums {
		for true {
			if activeWorkers < maxWorkers {
				mtx.Lock()
				go searchTwoSum(c, &nums, i, &target, maxWorkers)
				activeWorkers++
				mtx.Unlock()
				break
			}
		}
	}
}

func parPartTwo(nums []int, target int, maxWorkers int) int {
	c := make(chan int)
	go manageSearch(c, nums, target, maxWorkers)
	res :=<- c
	return res
}

//big boy target sum is 99920044
func main() {
	input := flag.String("input", "", "string-valued path to an input file")
	target := flag.Int("target", 0, "integer-valued number to sum to")
	flag.Parse()

	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	vals := strings.SplitAfter(string(content), "\n")
	vals = vals[:len(vals)-1]
	nums := make([]int, len(vals))

	for i, val := range vals {
		b, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			log.Fatal(err)
		}
		nums[i] = b
	}

	//fmt.Println(seqPartTwo(nums, *target))
	fmt.Println(parPartTwo(nums, *target, 100000))

	return
}