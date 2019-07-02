for t in range(1,11):

    N = int(input())

    class Node:
        def __init__(self,op,num,left,right):
            self.op = op
            self.num = num
            self.left = left
            self.right = right

        def __repr__(self):
            return str(self.op) + str(self.num)
    node_li=[]

    for _ in range(N):

        a = input().split()

        ip = a[1:]

        # print(ip)

        if len(ip) == 1:
            node_li.append(Node(None,int(ip[0]),-1,-1))

        else:
            node_li.append(Node(ip[0],None,int(ip[1])-1 ,int(ip[2])-1))

    # print(node_li)

    def dfs(idx):

        if node_li[idx].num != None:
            # print(idx,node_li[idx].num)
            return node_li[idx].num

        else:
            pn = node_li[idx]

            if pn.op == '-':

                return dfs(pn.left) - dfs(pn.right)

            elif pn.op == '/':

                return dfs(pn.left) / dfs(pn.right)

            elif pn.op == '*':

                return dfs(pn.left) * dfs(pn.right)

            elif pn.op == '+':

                return dfs(pn.left) + dfs(pn.right)
    print("#",end='')
    print(t, int(dfs(0)))

