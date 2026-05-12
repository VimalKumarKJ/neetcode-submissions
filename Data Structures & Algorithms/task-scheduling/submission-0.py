import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        counter = 0
        tasks = [(-val, key) for key, val in task_frequency.items()]
        heapq.heapify(tasks)

        while tasks:
            temp_tasks_tracker = []

            for _ in range(n+1):
                counter += 1
                if tasks:
                    curr_task = heapq.heappop(tasks)

                    if curr_task[0] + 1 < 0:
                        temp_tasks_tracker.append((curr_task[0]+1, curr_task[1]))
                    
                    if not tasks and not temp_tasks_tracker:
                        break
            for temp_tasks in temp_tasks_tracker:
                heapq.heappush(tasks, temp_tasks)
        return counter