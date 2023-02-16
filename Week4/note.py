#input = array of numbers (integers)
#output = sorted array of numbers (integers)
# expected output = [1,2,3,4,5,6,7]
# Insertion algorithm
def sort(input):
    for i in range(len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and key < input[j]:
            
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = key
        
   
    return input
     
def main():
    input = [4,5,1,3,2,7,6]
    print(sort(input))
    
if __name__ == "__main__":
    main()