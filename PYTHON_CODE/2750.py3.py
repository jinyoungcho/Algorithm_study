input_list = []

x= int(input())
for i in range(x):
    input_list.append(int(input()))
        
        
def insertionSort(input_list):
    for idx in range(1,len(input_list)):
        value = input_list[idx]
        i = idx
        while i>0 and input_list[i-1]>value:
            input_list[i] = input_list[i-1]
            i-=1
        input_list[i]=value
    output_list = input_list
    return output_list
    
output = insertionSort(input_list)
                
for j in output:
    print(j)