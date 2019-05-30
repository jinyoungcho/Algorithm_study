N = int(input())

MAP = [[0] * N for _ in range(N)]
ans = 0

def dfs(now_row,cnt):
    global ans
    if cnt == N+1:
        # print("~!")
        ans += 1

    else:

        #자리선택
        for j in range(N):
            if MAP[now_row][j] != 0:
                continue
            else:
                # print(now_row, j)

                #열
                for jk in range(N):
                    MAP[now_row][jk] += cnt
                #행
                for ik in range(N):
                    MAP[ik][j] += cnt
                #오른쪽아래 대각선
                sample_i = now_row #현재 i
                sample_j = j       #현재 j
                while(True):
                    if sample_i == N or sample_j == N:
                        break
                    MAP[sample_i][sample_j] += cnt

                    sample_i += 1
                    sample_j += 1

                sample_i2 = now_row-1  # 현재 i
                sample_j2 = j-1  # 현재 j
                while(True):
                    if sample_i2 == -1 or sample_j2 == -1:
                        break
                    MAP[sample_i2][sample_j2] += cnt

                    sample_i2 -= 1
                    sample_j2 -= 1

                sample_i = now_row  # 현재 i
                sample_j = j  # 현재 j
                while (True):
                    if sample_i == N or sample_j == -1:
                        break
                    MAP[sample_i][sample_j] += cnt

                    sample_i += 1
                    sample_j -= 1

                sample_i = now_row  # 현재 i
                sample_j = j  # 현재 j
                while (True):
                    if sample_i == -1 or sample_j == N:
                        break
                    MAP[sample_i][sample_j] += cnt

                    sample_i -= 1
                    sample_j += 1



                # print(cnt, "before")
                # for _ in range(N):
                #     print(MAP[_])
                #next_dfs
                dfs(now_row+1,cnt+1)



                #오른쪽
                for jk in range(N):
                    MAP[now_row][jk] -= cnt
                #아래
                for ik in range(N):
                    MAP[ik][j] -= cnt
                #오른쪽아래 대각선
                sample_i = now_row #현재 i
                sample_j = j       #현재 j
                while(True):
                    if sample_i == N or sample_j == N:
                        break

                    MAP[sample_i][sample_j] -= cnt

                    sample_i += 1
                    sample_j += 1

                sample_i2 = now_row-1  # 현재 i
                sample_j2 = j-1  # 현재 j
                while(True):
                    if sample_i2 == -1 or sample_j2 == -1:
                        break
                    MAP[sample_i2][sample_j2] -= cnt

                    sample_i2 -= 1
                    sample_j2 -= 1


                sample_i = now_row  # 현재 i
                sample_j = j  # 현재 j
                while (True):
                    if sample_i == N or sample_j == -1:
                        break
                    MAP[sample_i][sample_j] -= cnt

                    sample_i += 1
                    sample_j -= 1

                sample_i = now_row  # 현재 i
                sample_j = j  # 현재 j
                while (True):
                    if sample_i == -1 or sample_j == N:
                        break
                    MAP[sample_i][sample_j] -= cnt

                    sample_i -= 1
                    sample_j += 1


                # print(cnt, "after")
                # for _ in range(N):
                #     print(MAP[_])
dfs(0,1)
print(ans)