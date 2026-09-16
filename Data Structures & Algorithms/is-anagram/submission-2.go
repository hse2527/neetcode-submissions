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

		if count == 0 {
			delete(cntMap, ch)
		} else {
			cntMap[ch] = count
		}
	}

	if len(cntMap) > 0 {
		return false
	}

	return true
}
