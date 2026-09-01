class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):
            start = timeSeries[i]
            end = timeSeries[i] + duration

            if end <= timeSeries[i + 1]:
                total += duration
            else:
                total += timeSeries[i + 1] - start

        total += duration

        return total