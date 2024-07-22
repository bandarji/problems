package sortthepeople2418

import (
	"reflect"
	"testing"
)

func TestSortPeople(t *testing.T) {
	type args struct {
		names   []string
		heights []int
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{"case 1", args{[]string{"Mary", "John", "Emma"}, []int{180, 165, 170}}, []string{"Mary", "Emma", "John"}},
		{"case 2", args{[]string{"Alice", "Bob", "Bob"}, []int{155, 185, 150}}, []string{"Bob", "Alice", "Bob"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SortPeople(tt.args.names, tt.args.heights); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("SortPeople() = %v, want %v", got, tt.want)
			}
		})
	}
}
