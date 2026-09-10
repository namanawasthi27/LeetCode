class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = []
        g = []
        x = 0
        y = 0

        for i in range(len(secret)):
            s.append(int(secret[i]))

        for i in range(len(guess)):
            g.append(int(guess[i]))

        # A
        i = 0
        while i < len(g):
            if g[i] == s[i]:
                x += 1
                g.pop(i)
                s.pop(i)
            else:
                i += 1

        # B
        i = 0
        while i < len(g):
            j = 0

            while j < len(s):
                if g[i] == s[j]:
                    y += 1
                    g.pop(i)
                    s.pop(j)
                    break
                j += 1

            if i < len(g) and g[i] not in s:
                i += 1

        return str(x) + "A" + str(y) + "B"