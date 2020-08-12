
import collections

dq = collections.deque([6,7])

# adding 5 on left
dq.appendleft(5)
print("Append 5 to the left: ", list(dq))

# adding 8 on right 
dq.append(8)
print("Append 8 to the right: ", list(dq))


# adding two elements 9 and 10 on right
dq.extend([9, 10])
print("Append  9 and 10 to the right: ", list(dq))

# adding two elements 3 and 2 on left:
dq.extendleft([3,2])
print("Append 2 and 3 to the left: ", list(dq))

# Inserting 4 at index 2
dq.insert(2,4)
print("Insert 4 at index 2: ", list(dq))

# To Pop element from the right end:
dq.pop()
print("Remove element from the right: ", list(dq))

# To Pop element from the left end:
dq.popleft()
print("Remove element from the left: ", list(dq))

# Removing 4 from the queue
dq.remove(4)
print("Remove 4:", list(dq))

