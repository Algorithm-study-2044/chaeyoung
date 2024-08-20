class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        limited_time = []
        cnt = 0

        for d, s in zip(dist, speed):
            if d % s == 0:
                time = d // s
            else:
                time = d // s + 1
            limited_time.append(time)

        limited_time.sort()

        for i in range(len(limited_time)):
            if limited_time[i] <= i:
                return i

        return len(limited_time)





