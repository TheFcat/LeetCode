class Solution:
    def openLock(self, deadends, target: str) -> int:
        start = [0, 0, 0, 0]
        if target == start:
            return 0
        elif '0000' in deadends:
            return -1

        bfs_list = [(0, start)]
        checked = [False] * 10000
        checked[0] = True
        for d in deadends:
            checked[int(d)] = True

        while bfs_list:
            step, pos = bfs_list.pop(0)
            if pos == target:
                return step
            else:
                for i in range(4):
                    for j in [1, -1]:
                        new_pos = pos[:]
                        new_pos[i] = (int(new_pos[i]) + j) % 10
                        index = new_pos[0] * 1000 + new_pos[1] * 100 + new_pos[2] * 10 + new_pos[3]
                        if not checked[index]:
                            if str(index).zfill(4) == target:
                                return step + 1
                            checked[index] = True
                            bfs_list.append((step + 1, new_pos))
        return -1

print(Solution().openLock(["0201","0101","0102","1212","2002"], '0202'))