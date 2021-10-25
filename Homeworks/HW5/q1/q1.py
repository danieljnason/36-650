# problem 1
def transpose(X):
    X_t = []
    for col_t in range(len(X[0])):
        inner_collect = []
        for row_t in range(len(X)):
            inner_collect.append(X[row_t][col_t])
        X_t.append(inner_collect)
        
    for i in range(len(X_t)):
        print(X_t[i])

X = [[10,8],
 [2 ,4],
 [1 ,7]]
transpose(X)