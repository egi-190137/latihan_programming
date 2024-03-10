class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        rooms = [{"no": i, "end": -1, "count_used": 0} for i in range(n)]
        for meeting in meetings:
            rooms.sort(key=lambda room: room["end"])
            res_idx = 0
            for i in range(1, len(rooms)):
                if rooms[res_idx]["end"] == rooms[i]["end"]:
                    if rooms[i]["no"] < rooms[res_idx]["no"]:
                        res_idx = i
                    continue
                if rooms[i]["end"] < meeting[0]:
                    if rooms[i]["no"] < rooms[res_idx]["no"]:
                        res_idx = i
                    continue
                if rooms[i]["end"] >= meeting[0]:
                    break

            if meeting[0] > rooms[res_idx]["end"]:
                rooms[res_idx]["end"] = meeting[1] - 1
            else:
                rooms[res_idx]["end"] += (meeting[1] - meeting[0])

            rooms[res_idx]["count_used"] += 1

        rooms.sort(key=lambda room: room["count_used"], reverse=True)
        res_idx = 0
        for i in range(1, len(rooms)):
            if rooms[i]["count_used"] < rooms[res_idx]["count_used"]:
                break
            if rooms[i]["no"] < rooms[res_idx]["no"]:
                res_idx = i
        return rooms[res_idx]["no"]


solution = Solution()
# print(solution.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
# print(solution.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
#
# expexted 1
# output 0
print(solution.mostBooked(n=4, meetings=[[12,44],[27,37],[48,49],[46,49],[24,44],[32,38],[21,49],[13,30]]))


