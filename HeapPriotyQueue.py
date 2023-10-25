# Import the heapq module
import heapq as hq

# Initialize an empty list to use as a min-heap
myheap = []

# Initialize a variable to store the total cost
cost = 0.0

# Read the number of operations to perform from the user
n = int(input())

# Iterate through the operations
for i in range(0, n):
    # Read the current operation from the user
    cur = input()
    
    if cur == "dojob":
        # If the operation is "dojob," remove the smallest element from the heap
        cur_cost = hq.heappop(myheap)
        print(cur_cost)
        
        # Update the total cost by adding the cost of the removed element multiplied by the remaining elements in the heap
        cost += (cur_cost[1]) * (len(myheap))
    else:
        # If the operation is not "dojob," it's assumed to be an operation to add a new job
        # Parse the input to extract the job's priority and cost
        cur = list(map(float, cur.split()[1:]))
        
        # Add the job to the heap with priority as a negative value (to use the heap as a min-heap)
        hq.heappush(myheap, (-cur[0], cur[1]))
        print(myheap)

# Print the total cost after all operations are performed
print(cost)
