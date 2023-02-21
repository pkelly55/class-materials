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
def partition(ls):
    pivot = ls[0]
    i = 1
    for j in range(1, len(ls)):
        if ls[j] < pivot:
            ls[j], ls[i] = ls[i], ls[j]
            i += 1
    ls[0], ls[i-1] = ls[i-1], ls[0]
    return i-1

def quicksort(ls):
    if len(ls) <= 1:
        return ls
    else:
        pivot = partition(ls)
        left = quicksort(ls[:pivot])
        right = quicksort(ls[pivot+1:])
        ls = left + [ls[pivot]] + right
    return ls
            
    
def main():
    input = [9,4,5,0,7,2,8,6]

    print(quicksort(ls))
    
if __name__ == "__main__":
    main()