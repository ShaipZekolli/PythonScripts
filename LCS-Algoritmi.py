# Dynamic Programming implementation of LCS problem
def lcs(X, Y):
	# Gjetja e gjatsive të stringjeve
	m = len(X)
	n = len(Y)
	# Lista për ruajtjen e dp values
	L = [[None]*(n + 1) for i in range(m + 1)]

	# Build L[m + 1][n + 1] in bottom up fashion
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
		
	return L[m][n]
# Testimi i funksionit
X = "XY"
Y = "XPYQ"
print("LCS është: ", lcs(X, Y))