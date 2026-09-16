func groupAnagrams(strs []string) [][]string {
	sol := [][]string{}

	for _, cur := range strs {
		process(cur, &sol)
	}

	return sol
}

func process(str string, sol *[][]string) {
	for i, entries := range *sol {
		entry := entries[0]

		if compare(entry, str) {
			(*sol)[i] = append(entries,str)
			return 
		}
	}

	*sol = append(*sol, []string{str})
}

func compare(a, b string) bool {
	if len(a) != len(b) {
		return false
	}

	var counts [26]int

	for i, _ := range a {
		counts[a[i] - 'a']++
		counts[b[i] - 'a']--
	}

	for _, val := range counts {
		if val != 0 {
			return false
		}
	}

	return true
}
