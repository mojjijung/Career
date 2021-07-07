from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['702044']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
         q.append(adj[tmp].pop())
    #answer.reverse()
    return answer


print(solution([
    [ "702044", "702049" ], 
    [ "702049", "702047" ] ,[ "702047", "702049"], 
    [ "702049", "702044" ], [ "702047", "702053"]]
))