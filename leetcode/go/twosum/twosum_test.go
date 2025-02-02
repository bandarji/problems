package twosum

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"case 1", args{[]int{2, 7, 11, 15}, 9}, []int{0, 1}},
		{"case 2", args{[]int{3, 2, 4}, 6}, []int{1, 2}},
		{"case 3", args{[]int{3, 3}, 6}, []int{0, 1}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := TwoSum(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("TwoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
