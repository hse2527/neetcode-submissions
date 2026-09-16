func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
	total := 0

	for _, ch := range s {
		total += int(ch) * int(ch)
	}

	for _, ch := range t {
		total -= int(ch) * int(ch)
	}

	if total != 0 {
		return false
	}

	return true
}
