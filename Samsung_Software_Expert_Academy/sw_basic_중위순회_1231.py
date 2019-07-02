
for t in range(1,11):

    class Node:

        def __init__(self,number,word,lc,rc):
            self.number = number
            self.word = word
            self.leftchild = lc
            self.rightchild = rc

            self.visited = False

        def __repr__(self):
            return str(self.number)+self.word+str(self.leftchild)+str(self.rightchild)
    N = int(input())

    node_li=[]

    for _ in range(N):

        li = list(input().split())

        if len(li) == 2:
            node_li.append(Node(int(li[0])-1, li[1], -1, -1))
        elif len(li) == 3:
            node_li.append(Node(int(li[0])-1, li[1], int(li[2])-1, -1))
        else:
            node_li.append(Node(int(li[0])-1, li[1], int(li[2])-1, int(li[3])-1))

    ans = ''

    # print(node_li)

    def in_order_dfs(idx):


        if node_li[idx].leftchild != -1:

            in_order_dfs(node_li[idx].leftchild)

        print(node_li[idx].word,end='')

        if node_li[idx].rightchild != -1:
            in_order_dfs(node_li[idx].rightchild)

    print("#",end='')
    print(t,end=' ')
    in_order_dfs(0)
    print("")

