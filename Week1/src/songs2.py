def compute():
	songs = [1,2,5,4,3]
	# add your code here to compute min
	temp = songs[0]
	res = 1
	for i in range(len(songs)):
		if (songs[i] < temp):
			temp = songs[i]
			res = i+1
	print("Min song count", temp)
	print("Min song number", res)
if __name__ == "__main__":
    compute()