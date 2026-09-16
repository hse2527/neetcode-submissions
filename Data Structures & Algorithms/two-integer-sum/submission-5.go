import "slices"

func twoSum(nums []int, target int) []int {
	orig := make([]int, len(nums))
	for i, val := range nums {
		orig[i] = val
	}
    slices.Sort(nums)

	i, j := 0, len(nums)-1
	k, l := 0,0
	for i < j {
		if nums[i] + nums[j] == target {
			k,l = nums[i], nums[j]
			break 
		} else if nums[i] + nums[j] > target {
			j--
		} else {
			i ++
		}
	}

	iSet := false
	for ind, val := range orig {
		if val == k && !iSet{
			i = ind
			iSet = true
		} else if val == l {
			j = ind
		}
	}

	tmp := 0
	if i > j {
		tmp = i
		i=j
		j=tmp
	}

	return []int{i, j}
}
