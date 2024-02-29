A,B=input(),chr(102)
def C(txt,s):
	A=txt.find(s)
	if A!=-1:B=txt.find(s,A+1);return B if B!=-1 else-1
	else:return-2
print(C(A,B))