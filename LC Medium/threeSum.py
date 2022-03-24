class Solution:
    def threeSum1(self, nums: list) -> list:
        """
        Elegant 3 sum solution, breaking up +ve, -ve and 0 into lists
        """
        # no duplicated nested tuples
        res = set()

        n, p, z = [], [], []
        # split up -ve, +ve and 0 into their individual lists
        for number in nums:
            if number > 0:
                p.append(number)
            elif number < 0:
                n.append(number)
            else:
                z.append(number)

        # create a set of +ve and -ve array for fast O(1) look up
        P, N = set(p), set(n)

        # if there are more than three 0s, it is a viable solution
        if len(z) >= 3:
            res.add((0, 0, 0))

        # for every combination with a 0, we can find a complementary +ve and -ve number
        # e.g., (-1, 0, 1) or (-64, 0, 64)
        if z:
            for num in P:
                if -num in N:
                    res.add((num, 0, -num))

        # for a set of negative numbers, we can try and find its complementary sum
        # e.g., (-1, -4, 5) or (-10, -20, 30)
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                # target is the positive number we want to use to look in the pos set
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # similary, for a set of positive numbers, we can find its complementary deduct
        # e.g., (1, 4, -5) or (10, 20, -30)
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
