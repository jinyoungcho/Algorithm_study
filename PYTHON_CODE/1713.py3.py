N_panel = int(input())

num_vote = int(input())

student_votes = [0] * 101


panel = []
vote_li = list(map(int,input().split()))
for vote in vote_li:

    if student_votes[vote] > 0:
        student_votes[vote] += 1

    elif len(panel) < N_panel:

        panel.append(vote) # 2 1 4

        student_votes[vote] += 1

    else:
        #search for student who has the minimum num of vote
        # print(vote, student_votes[vote])
        drop_student = panel[0] #oldest

        for num in range(1,N_panel):
            drop_student2 = panel[num]
            if student_votes[drop_student] > student_votes[drop_student2]:
                drop_student = drop_student2


        #delete drop_student from panel
        panel.remove(drop_student)
        student_votes[drop_student] = 0

        student_votes[vote] += 1
        panel.append(vote)

    # print(vote)
    # print(student_votes[1:])
    # print(panel)

panel.sort()

for _ in panel:
    print(_,end=" ")