package twosum

func TwoSum(nums []int, target int) []int {
	imap := map[int]int{}
	for i, n := range nums {
		imap[n] = i
	}
	for i, n := range nums {
		oN := target - n
		if v, ok := imap[oN]; ok {
			if v == i {
				continue // skip same index
			}
			return []int{i, v}
		}
	}
	return nil
}
