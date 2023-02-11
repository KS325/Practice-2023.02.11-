import ita

def count_neighbor(data, i, j):
    #i行，j列の周囲8マスの生命数
    count = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if (0 <= k < len(data) and 0 <= l < len(data[k])):
                #盤の範囲内
                count = count + data[k][l]
    return(
        count - data[i][j] #自分のセルもカウントしたので引く
    )

def lifegame_rule(cur, neighbor):
    #cur : セルの現在状態, neighbor : 周囲の生命数
    if cur == 0:
        if neighbor == 3:
            return 1
        else:
            return 0
    else:
        if neighbor == 2 or neighbor == 3:
            return 1
        else:
            return 0

def lifegame_step(data):
    #盤面dataの次世代を計算
    new_data = ita.array.make2d(len(data), len(data[0]))
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            n = count_neighbor(data, i, j)
            new_data[i][j] = lifegame_rule(data[i][j], n)
    return new_data

def lifegame(data, steps):
    results = ita.array.make1d(steps)
    for i in range(0, steps):
        results[i] = data
        data = lifegame_step(data)
    return results

data = [
    [1, 1, 1, 0], 
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0], 
]

ani = lifegame(data, 10)
ita.plot.animation_show(ani)

