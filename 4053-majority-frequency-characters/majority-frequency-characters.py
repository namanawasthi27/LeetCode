class Solution:

    def majorityFrequencyGroup(self, s: str) -> str:

        d = {}
        n = len(s)

        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        groups = {}

        for char, freq in d.items():
            if freq not in groups:
                groups[freq] = ""
            groups[freq] += char

        ans = ""
        max_len = 0
        best_freq = 0

        for freq in groups:
            if len(groups[freq]) > max_len:
                max_len = len(groups[freq])
                best_freq = freq
                ans = groups[freq]

            elif len(groups[freq]) == max_len and freq > best_freq:
                best_freq = freq
                ans = groups[freq]

        return ans