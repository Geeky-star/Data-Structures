#1. Build a maxheap from array

#1. Build a binary tree
#2. Find the last non-leaf node and start heapifying each node.

def heapify(arr,n,i):

    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[l]>arr[largest]:
        largest = l

    if r<n and arr[r]>arr[largest]:
        largest = r

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def buildHeap(arr,n):

    startIdx = n//2-1

    #perform reverse level order traversal from last non-leaf node
    #from given array

    for i in range(startIdx,-1,-1):
        heapify(arr,n,i)


def printHeap(arr,n):

    print("array representation of heap is : ")
    for i in range(n):
        print(arr[i], end=" ")

arr = [1,3,5,4,6,13,10,9,8,15,17]
n=len(arr)
buildHeap(arr,n)
printHeap(arr,n)

#2. heap sort

def heapify(arr,n,i):

    largest = i
    l = 2*i+1
    r = 2*i+2

    if(l<n and arr[l]>arr[largest]):
        largest = l

    if r<n and arr[r]>arr[largest]:
        largest = r


    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def heapSort(arr):
    n = len(arr)

    #Build heap

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    #one by one extract elements

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)


arr = [12,11,13,5,6,7]
heapSort(arr)
n=len(arr)
print("sorted array is :")
printHeap(arr,n)

    
#3. k largest elements

#build a max-heap

def heapify(arr,n,i):

    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[l]>arr[largest]:
        largest = l

    if r<n and arr[r]>arr[largest]:
        largest = r

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def kLargest(arr,k,n):
    a = []

    for i in range(k):
        a.append(arr[i])

    return a

def heapSort(arr,n):

    for i in range(n//2,-1,-1):

        heapify(arr,n,i)



    
n=5
k=2
arr = [7,10,4,3,20,15]

print()
heapSort(arr,n)
print("k large elements are : ", arr)
printHeap(arr,n)
#printHeap(arr,n)



































        
    

    
        
