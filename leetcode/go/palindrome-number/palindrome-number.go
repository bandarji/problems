package main

func isPalindrome(n int) bool {
	if n < 0 {
		return false
	}
	original := n
	reversed := 0
	for n > 0 {
		digit := n % 10
		reversed = reversed*10 + digit
		n /= 10
	}
	return original == reversed
}

func main() {
	println("expect true:", isPalindrome(121))   // true
	println("expect false:", isPalindrome(-121)) // false
	println("expect false:", isPalindrome(10))   // false
	println("expect false:", isPalindrome(-101)) // false
}
