package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"math/big"
	"strings"
)

func countTrees(c chan int64, chart *[]string, dX *int, dY *int) {
	trees := 0
	x := 0
	y := 0
	for y < len(*chart) {
		if (*chart)[y][x] == '#' {
			trees++
		}
		x += *dX
		x %= len((*chart)[0])
		y += *dY
	}
	c <- int64(trees)
}

func findTrees(input *string) *big.Int {

	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	chart := strings.Split(strings.Replace(string(content), "\r\n", "\n", -1), "\n")
	chart = chart[:len(chart)-1]
	slopesX := []int{ 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 54, 64 }
	slopesY := []int{ 1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 47 }

	prod := big.NewInt(1)

	c := make(chan int64)

	for i, _ := range slopesX {
		for j, _ := range slopesY {
			go countTrees(c, &chart, &slopesX[i], &slopesY[j])
		}
	}

	for i := 0; i < len(slopesX) * len(slopesY); i++ {
		prod.Mul(prod, big.NewInt(<-c))
	}
	return prod
}

func main() {
	input := flag.String("input", "", "string-valued path to an input file")
	flag.Parse()
	fmt.Println(findTrees(input))
	return
}
