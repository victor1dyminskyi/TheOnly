
#          |betray| be silent|
# betray   | pair1| pair2    |
# be silent| pair3| pair4    |
# def prisoner_delema(pair1, pair2, pair3, pair4):
#     #player1
#     if pair1[0] <= pair3[0] and pair2[0] <= pair4[0]:
#         strategy1 = "betray"
#     elif pair1[0] > pair3[0] and pair2[0] > pair4[0]:
#         strategy1 = "be silent"
#     else:
#         print("Player1 doesn't have dominant strategy, try again")
#         return
#     #player2
#     if pair1[1] <= pair2[1] and pair3[1] <= pair4[1]:
#         strategy2 = "betray"
#     elif pair1[1] > pair2[1] and pair3[1] > pair4[1]:
#         strategy2 = "be silent"
#     else:
#         print("Player1 doesn't have dominant strategy, try again")
#         return
#     print("Player1 strategy: ", strategy1)
#     print("Player2 strategy: ", strategy2)
# prisoner_delema((5,5),(2,10),(10,2),(1,1))

# def prisoner_dil(paer1, paer2, paer3, paer4):
#     # player1
#     if paer1[0] < paer3[0] and paer2 < paer4:
#         strategy1 = "Betray"
#     else:
#         strategy1 = "Silence"
#     # player2
#     if paer1[1] < paer2[1] and paer3[1] < paer4[1]:
#         strategy2 = "batrey"
#     else:
#         strategy2 = "Silence"
#
#     print(strategy1)
#     print(strategy2)
# prisoner_dil((5,5), (2,10), (10,2), (1,1))

# --------------------------------------------------------

# import numpy as np
# import nashpy as nash
# A = np.array([[2,0],[4,2]]) # A is the row player
# B = np.array([[4,2],[2,0]]) # B is the column player
# game1 = nash.Game(A,B)
# game1
#
# equilibria = game1.support_enumeration()
# for eq in equilibria:
#     print(eq)

# --------------------------------------------------------

