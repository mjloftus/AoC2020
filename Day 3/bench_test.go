package main

import (
	"flag"
	"fmt"
	"testing"
)

var input *string

func init() {
	input = flag.String("input", "", "string-valued path to an input file")
}

func BenchmarkFindProd(b *testing.B) {
	for n := 0; n < b.N; n++ {
		fmt.Println(findTrees(input))
	}
}