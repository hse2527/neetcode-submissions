func twoSum(nums []int, target int) []int {
	numMap := map[int]int{}

	for i, val := range nums {
		if j, exists := numMap[target-val]; exists {
			return []int{j, i}
		}

		numMap[val] = i
	}

	return []int{}
}
