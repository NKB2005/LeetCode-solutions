class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest_candies = max(candies)
        result = []

        for candy in candies:
            new_total = candy + extraCandies

            if new_total >= highest_candies:
                result.append(True)
            else:
                result.append(False)

        return result