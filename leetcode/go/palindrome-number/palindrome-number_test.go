package main

import "testing"

func Test_isPalindrome(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"test1", args{121}, true},
		{"test2", args{-121}, false},
		{"test3", args{10}, false},
		{"test4", args{-101}, false},
		{"test5", args{12321}, true},
		{"test6", args{0}, true},
		{"test7", args{1}, true},
		{"test8", args{1234321}, true},
		{"test9", args{123456}, false},
		{"test10", args{-12321}, false},
		{"test11", args{1001}, true},
		{"test12", args{100}, false},
		{"test13", args{1221}, true},
		{"test14", args{123321}, true},
		{"test15", args{123421}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.n); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
