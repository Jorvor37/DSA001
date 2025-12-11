class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict
        import bisect

        row = defaultdict(list)
        col = defaultdict(list)

        # Build row and column maps
        for x, y in buildings:
            row[x].append(y)
            col[y].append(x)

        # Sort lists for binary search
        for k in row:
            row[k].sort()
        for k in col:
            col[k].sort()

        covered = 0

        for x, y in buildings:
            ys = row[x]
            xs = col[y]

            # Check left and right
            pos_y = bisect.bisect_left(ys, y)
            has_left = pos_y > 0
            has_right = pos_y < len(ys) - 1

            # Check above and below
            pos_x = bisect.bisect_left(xs, x)
            has_above = pos_x > 0
            has_below = pos_x < len(xs) - 1

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
