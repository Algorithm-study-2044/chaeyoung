class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        sorted_index = sorted(range(N), key = lambda i: score[i], reverse=True)

        result = [""] * N
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank_num in range(N):
            index = sorted_index[rank_num]
            if rank_num <3:
                result[index] = medals[rank_num]

            else:
                result[index] = str(rank_num + 1)

        return result