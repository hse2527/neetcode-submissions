func isAnagram(s string, t string) bool {
	cntMap := map[rune]int{}

	for _, ch := range s {
		cntMap[ch]++
	}

	for _, ch := range t {
		count := cntMap[ch]
		count--

		if count < 0 {
			return false
		}

		cntMap[ch] = count
	}

	for _, cnt := range cntMap {
		if cnt > 0 {
			return false
		}
	}

	return true
}
