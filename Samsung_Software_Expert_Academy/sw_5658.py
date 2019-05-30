# 5
# 12 10
# 1B3B3B81F75E
# 16 2
# F53586D76286B2D8
# 20 14
# 88F611AE414A751A767B
# 24 16
# 044D3EBA6A647B2567A91D0E
# 28 11
# 8E0B7DD258D4122317E3ADBFEA99



T = int(input())
N,K = 0,0
answer = 0
answer_set = set()
len_b = 0
answer_list = []
# fuction



def get_set(string):
    string = string

    for i in range(4):
        # print(string[i*len_b:i*len_b+len_b])
        answer_set.add(string[i*len_b:i*len_b+len_b])

    # print(answer_set)
    # for s in string:

def rotate(string):
    string=string

    string += string[0]
    string = string[1:]

    return string

def get_dec():

    # print(answer_set)
    for s in answer_set:
        temp = 0
        for po,ch in zip(range(len_b-1,-1,-1),s):
            if '0'<= ch <= '9':
                temp_i = ord(ch) - ord('0')
                temp += temp_i*pow(16,po)
            else:
                temp_i = ord(ch)-ord('A')+10
                temp += temp_i*pow(16,po)

        answer_list.append(temp)




def get_answer(string):
    string = string

    #get set
    for _ in range(len_b):
        get_set(string)
        string = rotate(string)

    get_dec()




for t in range(1,T+1):

    answer = 0
    N,K = list(map(int,input().split()))
    len_b = N // 4
    string = str(input())
    answer_list=[]
    answer_set = set()
    get_answer(string)

    answer_list = sorted(answer_list,reverse=True)

    # print(answer_list)

    answer = answer_list[K-1]



    print("#", end="")
    print(t,answer)