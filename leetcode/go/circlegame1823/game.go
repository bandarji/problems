package circlegame1823

func FindTheWinner(n int, k int) int {
	pick := 0
	for i := 2; i <= n; i++ {
		pick = (pick + k) % i
	}
	return pick + 1
}
