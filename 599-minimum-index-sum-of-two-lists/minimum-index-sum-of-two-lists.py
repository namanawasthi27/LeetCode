class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        ans=[]
        mini=float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                indexsum=i+list2.index(list1[i])
                if indexsum<mini:
                    mini=indexsum
                    ans=[list1[i]]
                elif indexsum==mini:
                    ans.append(list1[i])
        return ans