class Solution:
    def trap(self, height):
        lp = 0
        rp = len(height) - 1
        left = right = 0
        water = 0

        while lp < rp:
            if height[lp] < height[rp]:
                if height[lp] >= left:
                    left = height[lp]
                else:
                    water += left - height[lp]
                lp += 1
            else:
                if height[rp] >= right:
                    right = height[rp]
                else:
                    water += right - height[rp]
                rp -= 1

        return water