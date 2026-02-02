class Window:
    def __init__(self, k: int):
        self.k = k
        self.minheap = []  # other values
        self.maxheap = []  # k lowest values
        self.cost = 0  # sum of k lowest values

        # Lazy deletion elements
        self.del_min = defaultdict(int)
        self.del_max = defaultdict(int)

        # Sizes of heaps without lazy deleted elements
        self.sz_min = 0
        self.sz_max = 0

    def __len__(self):
        return self.sz_min + self.sz_max

    def prune(self):
        """Method to remove deleted elements from top of heaps"""

        def _prune(heap, vals, sign):
            while heap:
                x = sign * heap[0]
                if vals[x] == 0:
                    break
                
                heapq.heappop(heap)
                vals[x] -= 1

        _prune(self.maxheap, self.del_max, sign=-1)
        _prune(self.minheap, self.del_min, sign=1)

    def rebalance(self):
        """Method to make maxheap store exactly k elements or all if len < k"""

        self.prune()

        target = min(self.k, len(self))

        while self.sz_max > target:
            x = -heapq.heappop(self.maxheap)
            self.sz_max -= 1
            self.cost -= x

            heapq.heappush(self.minheap, x)
            self.sz_min += 1
            
            self.prune()

        while self.minheap and self.sz_max < target:
            x = heapq.heappop(self.minheap)
            self.sz_min -= 1

            heapq.heappush(self.maxheap, -x)
            self.sz_max += 1
            self.cost += x

            self.prune()

    def add(self, x):
        if not self.maxheap or x <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -x)
            self.sz_max += 1
            self.cost += x
        else:
            heapq.heappush(self.minheap, x)
            self.sz_min += 1

        self.rebalance()

    def remove(self, x):
        if self.maxheap and x <= -self.maxheap[0]:
            self.del_max[x] += 1
            self.sz_max -= 1
            self.cost -= x
        else:
            self.del_min[x] += 1
            self.sz_min -= 1

        self.rebalance()


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        # Build window of size dist + 1
        window = Window(k - 1)
        for i in range(1, dist + 2):
            window.add(nums[i])

        # Iterate and update
        result = window.cost
        for i in range(2, n - dist):
            window.remove(nums[i - 1])
            window.add(nums[i + dist])
            result = min(result, window.cost)

        return nums[0] + result
