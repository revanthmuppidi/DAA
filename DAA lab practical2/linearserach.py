import time

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

start = time.perf_counter()

found = False

for i in range(n):
    if arr[i] == key:
        found = True
        position = i
        break

end = time.perf_counter()

if found:
    print("Element found at index", position)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
print("Time Complexity:")
print("Best Case: O(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")
print("Space Complexity: O(1)")
