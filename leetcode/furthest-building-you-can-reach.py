import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        distance = 0
        delta_greater_height = []
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i + 1]:
                distance += 1
                continue

            if ladders == 0:
                break

            delta_height = heights[i + 1] - heights[i]
            distance += 1
            ladders -= 1
            delta_greater_height.append(delta_height)

        heapq.heapify(delta_greater_height)
        for i in range(distance, len(heights) - 1):
            if heights[i] >= heights[i + 1]:
                distance += 1
                continue

            delta_height = heights[i + 1] - heights[i]
            if not delta_greater_height:
                if delta_height > bricks:
                    break
                bricks -= delta_height
                distance += 1
                continue

            smallest_height = heapq.heappop(delta_greater_height)
            if smallest_height < delta_height:
                if smallest_height > bricks:
                    break
                bricks -= smallest_height
                distance += 1
                heapq.heappush(delta_greater_height, delta_height)
            else:
                if delta_height > bricks:
                    break
                bricks -= delta_height
                distance += 1
                heapq.heappush(delta_greater_height, smallest_height)

        return distance
