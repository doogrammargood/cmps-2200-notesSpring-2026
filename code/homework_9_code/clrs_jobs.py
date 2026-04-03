"""
This code helps you check your answer to Problem 2 Homework 9.

This implementation stores the values table[j][t] where 
table[j][t] stores the optimum payoff when considering jobs j and after, when t amount of time has passed.

The implementation loops through the jobs in reverse order of their deadlines and time in reverse order.

Other implementations are possible. In particular, it may be more natural to loop in order of increasing deadlines.

However, it seems that we need to keep the jobs sorted by deadline.
"""

jobs = [ #time profit deadline
    (1, 12, 3),
    (2, 25, 5),
    (3, 18, 6),
    (1, 7, 2),
    (2, 30, 4),
    (3, 45, 7),
    (1, 5, 3),
    (2, 22, 6),
    (3, 35, 8),
    (1, 9, 5),
]
def access_table(table,j,t):
        """
        Provides a way to safely access entries of the table, handling indexing errors.
        """
        try:
            return table[j][t]
        except IndexError:
            return 0
        
def create_table(jobs:list[tuple[int]]) -> list[list[int]]:
    """
    Input: jobs is a list of 3-tuples of integers, representing (time, profit, deadline) for each job.
    Returns: A table where table[j][t] stores the optimum payoff when considering jobs j and after, when t amount of time has passed.

    Notes:
    process jobs one at a time in reverse order of their deadline
    table[n-1][0] stores the optimal solution.
    """
    n=len(jobs)
    sorted_jobs = sorted(jobs, key= lambda x: -x[2])
    table = [[0 for x in range(n+1)] for y in range(n)]
    for j, job in enumerate(sorted_jobs): #loop through the jobs in reverse order of finish times.
        for t in range(n,-1,-1):
            #TODO: complete this function.~6 lines
            pass
    return table

def decode_table(table:list[list[int]],jobs:list[tuple[int]]) -> list[tuple[int]]:
    """
    Input: table is an ouput of create_table. jobs is a list of jobs to be performed. Each job has the format (time, profit, deadline).
    Returns: A list of the jobs that are performed to optimize profit.
    Note: Applies backtracking to the table to recover the optimal jobs.
    """
    optimal_job_indices = []
    t=0
    sorted_jobs = sorted(jobs, key= lambda x: -x[2])

    for j in range(n-1,-1,-1):
        #TODO: Complete this function, ~3 lines.
        pass
    optimal_jobs = [job for j, job in enumerate(sorted_jobs) if j in optimal_job_indices]
    return optimal_jobs

if __name__=="__main__":
    #This is a basic check that the code is correct. It is not comprehensive.
    n=len(jobs)
    table = create_table(jobs)
    assert sum([job[1] for job in decode_table(table,jobs)])==table[n-1][0]==110
    print("passed")