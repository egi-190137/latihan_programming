class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        last_arrow = points[0]
        counter = 1
        for i in range(1, len(points)):
            if last_arrow[1] < points[i][0]:
                last_arrow = points[i]
                counter += 1
            else:
                last_arrow[0] = points[i][0]
                last_arrow[1] = min(last_arrow[1], points[i][1])
        return counter
