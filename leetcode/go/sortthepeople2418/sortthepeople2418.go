package sortthepeople2418

import "sort"

type People struct {
	Names   []string
	Heights []int
}

// Sorting implementation requires Swap(), Len() and Less() functions
func (p People) Swap(i, j int) {
	p.Names[i], p.Names[j] = p.Names[j], p.Names[i]
	p.Heights[i], p.Heights[j] = p.Heights[j], p.Heights[i]
}

func (p People) Len() int {
	return len(p.Names)
}

func (p People) Less(i, j int) bool {
	return p.Heights[i] > p.Heights[j]
}

func SortPeople(names []string, heights []int) []string {
	p := People{names, heights}
	sort.Sort(p)
	return p.Names
}
