package main

import (
	"flag"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"testing"
)

var input *string
var target *int

func init() {
	input = flag.String("input", "", "string-valued path to an input file")
	target = flag.Int("target", 0, "integer-valued number to sum to")
}

func BenchmarkSeqPartOne(b *testing.B) {
	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	vals := strings.SplitAfter(string(content), "\n")
	vals = vals[:len(vals)-1]
	nums := make([]int, len(vals))

	for i, val := range vals {
		x, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			log.Fatal(err)
		}
		nums[i] = x
	}

	for n := 0; n < b.N; n++ {
		seqPartOne(nums, *target)
	}
}

func BenchmarkParPartOne(b *testing.B) {
	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	vals := strings.SplitAfter(string(content), "\n")
	vals = vals[:len(vals)-1]
	nums := make([]int, len(vals))

	for i, val := range vals {
		x, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			log.Fatal(err)
		}
		nums[i] = x
	}

	for n := 0; n < b.N; n++ {
		parPartOne(nums, *target)
	}
}

func BenchmarkSeqPartTwo(b *testing.B) {
	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	vals := strings.SplitAfter(string(content), "\n")
	vals = vals[:len(vals)-1]
	nums := make([]int, len(vals))

	for i, val := range vals {
		x, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			log.Fatal(err)
		}
		nums[i] = x
	}

	for n := 0; n < b.N; n++ {
		seqPartTwo(nums, *target)
	}
}

func BenchmarkParPartTwo(b *testing.B) {
	content, err := ioutil.ReadFile(*input)
	if err != nil {
		log.Fatal(err)
	}

	vals := strings.SplitAfter(string(content), "\n")
	vals = vals[:len(vals)-1]
	nums := make([]int, len(vals))

	for i, val := range vals {
		x, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			log.Fatal(err)
		}
		nums[i] = x
	}

	for n := 0; n < b.N; n++ {
		parPartTwo(nums, *target, 100000)
	}
}