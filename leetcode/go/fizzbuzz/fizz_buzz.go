package fizzbuzz

import "fmt"

func FizzBuzz(n int) []string {
	fb := []string{}
	tmp := ""
	for i := 1; i <= n; i++ {
		if i%3 == 0 {
			tmp += "Fizz"
		}
		if i%5 == 0 {
			tmp += "Buzz"
		}
		if len(tmp) == 0 {
			tmp = fmt.Sprintf("%d", i)
		}
		fb = append(fb, tmp)
		tmp = ""
	}
	return fb
}
