package majorityelement169

func MajorityElement(nums []int) int {
	majority := nums[0]
	count := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] == majority {
			count++
		} else {
			count--
			if count == 0 {
				majority = nums[i]
				count = 1
			}
		}
	}
	return majority
}
