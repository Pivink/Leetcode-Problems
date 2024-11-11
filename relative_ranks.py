score = [10,3,8,9,4]
score_map = {score[i]: i for i in range(len(score))}
print(score_map)
score=sorted(score,reverse=True)
print(score)
print(score_map[score[0]])
# def relative_ranks(score):
#     score_map = {score[i]: i for i in range(len(score))}
#     rank=["Gold medal","Silver medal","Bronze medal"]
#     score=sorted(score,reverse=True)
#     res=[]
#     for i in range(len(score)):
#         if score_map[score[i]]<=3:
#             print(score_map[score[i]])
#             res.append(rank[i-1])
#         else:
#             res.append(str(score_map[score[i]]))
#     return res