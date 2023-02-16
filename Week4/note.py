#input = array of numbers (integers)
#output = sorted array of numbers (integers)
# expected output = [1,2,3,4,5,6,7]
# Insertion algorithm
'''
def sort(input):
    for i in range(len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and key < input[j]:
            
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = key
        
   
    return input
'''
# partition(a,p,r) algorithm 

def partition(a,p,r):
    x = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j] <= x:
            i = i + 1
            a[i],a[j] = a[j],a[i]
    a[i + 1],a[r] = a[r],a[i + 1]
    return i + 1

# quicksort(a,p,r) algorithm

def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q - 1)
        quicksort(a,q + 1,r)
    return a


            
    
def main():
    input = [4,5,1,3,2,7,6,9,8]
    print(quicksort(input,0,len(input) - 1))
    
if __name__ == "__main__":
    main()