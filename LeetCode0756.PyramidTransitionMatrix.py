class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        # Step 1: Build adjacency map
        mp = defaultdict(list)
        for a in allowed:
            mp[a[:2]].append(a[2])

        memo = {}

        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            # Generate all possible next rows
            def build_next(i, cur):
                if i == len(row) - 1:
                    return dfs(cur)
                pair = row[i:i+2]
                if pair not in mp:
                    return False
                for c in mp[pair]:
                    if build_next(i + 1, cur + c):
                        return True
                return False

            memo[row] = build_next(0, "")
            return memo[row]

        return dfs(bottom)
