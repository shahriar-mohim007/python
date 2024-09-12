package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanln(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	left, right := 0, len(arr)-1

	for left <= right {
		if arr[left] > 0 && arr[right] < 0 {
			arr[left], arr[right] = arr[right], arr[left]
			right--
			left++
		} else if arr[left] > 0 && arr[right] < 0 {
			arr[left], arr[right] = arr[right], arr[left]
			left++
			right--
		} else if arr[left] < 0 {
			left++
		} else if arr[right] > 0 {
			right--
		}
	}
	fmt.Println(arr)
}
