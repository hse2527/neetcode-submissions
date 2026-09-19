class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def section(h, l) -> int:
            num = h//3 * 3 + l//3

            return num

        lmap = [[False for _ in range(9)] for _ in range(9)]
        hmap = [[False for _ in range(9)] for _ in range(9)]
        bmap = [[False for _ in range(9)] for _ in range(9)]

        for h in range(9):
            for l in range(9):
                if board[h][l] == '.':
                    continue
                
                val = int(board[h][l]) - 1
                s = section(h,l)

                if lmap[l][val] or hmap[h][val] or bmap[s][val]:
                    return False

                hmap[h][val] = True
                lmap[l][val] = True
                bmap[s][val] = True
        
        return True
