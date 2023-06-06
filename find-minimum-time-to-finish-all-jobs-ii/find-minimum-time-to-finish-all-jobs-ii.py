class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:

        workers.sort()
        jobs.sort()

        m=0

        for i in range(len(jobs)):
            m=max(m,math.ceil(jobs[i]/workers[i]))

        return m
