import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def count_tasks(tasks):
            task_dict = {}
            for task in tasks:
                if task in task_dict:
                    task_dict[task] += 1
                else:
                    task_dict[task] = 1
            return task_dict

        def check_cool_down(cycle):
            if cool_down_queue:
                if cool_down_queue[0][1] == cycle:
                    freq_and_task, _ = cool_down_queue.pop(0)
                    heapq.heappush_max(task_counter, freq_and_task)

        task_dict = count_tasks(tasks)
        task_counter = [[task_dict[task], task, ]for task in task_dict]
        heapq.heapify_max(task_counter)
        cool_down_queue = []

        cycles = 0
        while task_counter or cool_down_queue:
            cycles += 1
            if task_counter:
                freq_and_task = heapq.heappop_max(task_counter)
                freq_and_task[0] -= 1
                if freq_and_task[0] != 0:
                    cool_down_queue.append([freq_and_task, cycles+n])

            check_cool_down(cycles)


        return cycles
            
                


        
