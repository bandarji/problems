package circlegame1823

import "testing"

func TestFindTheWinner(t *testing.T) {
	type args struct {
		n int
		k int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{5, 2}, 3},
		{"2", args{6, 5}, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindTheWinner(tt.args.n, tt.args.k); got != tt.want {
				t.Errorf("FindTheWinner() = %v, want %v", got, tt.want)
			}
		})
	}
}
