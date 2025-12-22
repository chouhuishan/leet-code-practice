import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort()

        available_tasks = []

        current_time = 0
        task_index = 0

        res = []

        while available_tasks or task_index < len(tasks):
            if available_tasks == []:
                current_time = max(current_time, tasks[task_index][0])

            while task_index < len(tasks) and tasks[task_index][0] <= current_time:
                heapq.heappush(
                    available_tasks, (tasks[task_index][1], tasks[task_index][2])
                )
                task_index += 1

            processing_time, index = heapq.heappop(available_tasks)

            res.append(index)

            current_time += processing_time

        return res


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
# tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
print(Solution().getOrder(tasks))
