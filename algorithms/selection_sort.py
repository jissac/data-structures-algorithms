'''
# Selection sort, sort by ascending or descending
TIME COMPLEXITY: O(n^2)
KEY CONCEPTS: append to new sorted array requires popping from old array
'''

def findSmallest(arr:[int])->int:
    smallest= arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def findLargest(arr:[int])->int:
    largest = arr[0]
    largest_index = 0
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def selectionSort(arr:[int],ascending=True)->int:
    sorted = []
    for i in range(len(arr)):
        if ascending:
            smallest = findSmallest(arr)
            sorted.append(arr.pop(smallest))
        else:
            largest = findLargest(arr)
            sorted.append(arr.pop(largest))
    return sorted

if __name__ == '__main__':
    arr = [3,2,5,78,2,1,5]
    out = selectionSort(arr)
    print(out)
