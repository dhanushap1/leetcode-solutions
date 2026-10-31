
"""
LeetCode 121 - Best Time to Buy and Sell Stock

Problem:
Given an array prices where prices[i] represents the
stock price on the ith day, choose one day to buy and
a different future day to sell.

Return the maximum profit. If no profit is possible,
return 0.

Example 1:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5

Example 2:
Input: prices = [7, 6, 4, 3, 1]
Output: 0

--------------------------------------------------
Approach 1: Brute Force
--------------------------------------------------
Check every possible buying and selling combination.

Time Complexity: O(n^2)
Space Complexity: O(1)

Approach 2: Greedy (Single Pass)
--------------------------------------------------
Track the minimum price seen so far.
Calculate the profit for each day using the current
price minus the minimum price.
Update the maximum profit whenever a better profit
is found.

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

# Approach 1: Brute Force
class SolutionBruteForce(object):
    def maxProfit(self, prices):
        p = 0

        for n in range(len(prices)):
            c = prices[n]

            for j in range(n + 1, len(prices)):
                d = prices[j] - c

                if d > p:
                    p = d

        return p


# Approach 2: Optimized Greedy
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p

            profit = p - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
