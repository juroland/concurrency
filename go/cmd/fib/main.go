package main

import (
	"flag"
	"fmt"
	"math/rand"

	"github.com/juroland/concurrency-and-parallelism/go/compute"
)

func apply(data []int, f func(int) int) []int {
	results := make([]int, len(data))
	for i, x := range data {
		results[i] = f(x)
	}
	return results
}

func main() {
	numbers := make([]int, 200)
	for i := range numbers {
		numbers[i] = 30 + rand.Intn(5)
	}

	var parallel bool
	flag.BoolVar(&parallel, "parallel", false, "enable parallel computation")
	flag.Parse()

	if !parallel {
		results := apply(numbers, compute.Fib)
		fmt.Println(results)
		return
	}

	half := len(numbers) / 2

	c := make(chan []int)

	go func() {
		results := apply(numbers[:half], compute.Fib)
		c <- results
	}()

	go func() {
		results := apply(numbers[half:], compute.Fib)
		c <- results
	}()

	fmt.Println(<-c)
	fmt.Println(<-c)
}
