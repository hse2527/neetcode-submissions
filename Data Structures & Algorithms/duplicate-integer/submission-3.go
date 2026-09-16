func hasDuplicate(nums []int) bool {
	set := map[int]struct{}{}
    for _, num := range nums {
		if _, exists := set[num]; !exists {
			set[num] = struct{}{}
		} else {
			return true
		}
	}
	return false
}
