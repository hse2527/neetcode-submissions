func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[[26]int][]string)

	for _, str := range strs {
		var counts [26]int

		for _, val := range str {
			counts[val-'a']++
		}

		anagramMap[counts] = append(anagramMap[counts], str)
	}

	sol := make([][]string,0,len(anagramMap))
	for _, group := range anagramMap {
		sol = append(sol, group)
	}
	return sol
}
