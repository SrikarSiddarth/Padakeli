'''
	First  try on building word-maker 
'''

import numpy as np
import csv

# Node class in the form of linked lists
# class Node: 
   
#     # Function to initialize the node object 
#     def __init__(self, data): 
#         self.data = data  # Assign data 
#         self.next = None  # Initialize  
#                           # next as null 

class TeluguPoti():

	def __init__(self):

		self.ka = [[]]
		with open('ka.csv') as file:
			file = csv.reader(file, delimiter=',')
			line_count = 0
			for row in file:
				for i in range(len(row)):
					self.ka[line_count].append(row[i])
				self.ka.append([])
				line_count += 1
			print('Processed '+str(line_count)+' lines.')
		# self.grid = [['స','క','వి','త'],
		# 		['చా','మ','ర','ము'],
		# 		['కు','ల','కం','న'],
		# 		['కి','ము','ళ','గ']]
		self.grid = [['కు','కూ','ల','ము'],
					['కు','ఠా','ర','ము'],
					['కు','డ','ప','ము'],
					['కు','పి','తు','డు']]
		# self.g = self.grid[0]+self.grid[1]+self.grid[2]+self.grid[3]
		self.buf = []
		self.l = len(self.grid[0])


	def save(self, k):
		# with open('output.csv','w',newline='') as file:
			# writer = csv.writer(file)
			# writer.writerow(self.ka[8])
		f = open("output.txt", "w")
		for i in k:
			f.write(i)
			f.write('\n')
		f.close()


	def filterFromDictionary(self):
		s = []
		for i in [0,4,8,12]:
			for n in range(2,6):
				print(i,n)
				s += self.getWords(i,n)
				self.buf = []
		s = list(dict.fromkeys(s))
		print(len(s))
		final = []
		for k in s:
			for i in range(len(self.ka)):
				for j in self.ka[i]:
					if k==j:
						final.append(k)
						break
				else:
					continue
				break
		print(len(final))
		return final
		

	def getNeighbours(self, index):
		# 	int [][][] neighbours = {
		#         {
		#             {1,3,5,8},//0
		#             {3,4,6,5}
		#         },
		#         {
		#             {0,2,3,4,6,8,9},//1
		#             {9,3,8,4,6,7,5}
		#         },
		#         {
		#             {1,4,7,9},//2
		#             {9,8,6,7}
		#         },
		#         {
		#             {0,1,4,5,6,8,10,11},//3
		#             {10,2,3,8,4,6,7,5}
		#         },
		#         {
		#             {1,2,3,6,7,9,11,12},//4
		#             {10,2,9,8,4,6,7,5}
		#         },
		#         {
		#             {0,3,6,8,10,13},//5
		#             {0,2,3,4,6,5}
		#         },
		#         {
		#             {1,3,4,5,7,8,9,11,13,14},//6
		#             {0,10,2,9,3,8,4,6,7,5}
		#         },
		#         {
		#             {2,4,6,9,12,14},//7
		#             {0,10,9,8,6,7}
		#         },
		#         {
		#             {0,1,3,5,6,9,10,11,13,15,16},//8
		#             {11,1,0,10,2,3,8,4,6,7,5}
		#         },
		#         {
		#             {1,2,4,6,7,8,11,12,14,16,17},//9
		#             {11,1,0,10,2,9,8,4,6,7,5}
		#         },
		#         {
		#             {3,5,8,11,13,15},//10
		#             {1,0,2,3,4,6}
		#         },
		#         {
		#             {3,4,6,8,9,10,12,13,14,16},//11
		#             {11,1,0,10,2,9,3,8,4,6}
		#         },
		#         {
		#             {4,7,9,11,14,17},//12
		#             {11,0,10,9,8,6}
		#         },
		#         {
		#             {5,6,8,10,11,14,15,16},//13
		#             {11,1,0,10,2,3,8,4}
		#         },
		#         {
		#             {6,7,9,11,12,13,16,17},//14
		#             {11,1,0,10,2,9,8,4}
		#         },
		#         {
		#             {8,10,13,16},//15
		#             {1,0,2,3}
		#         },
		#         {
		#             {8,9,11,13,14,15,17},//16
		#             {11,1,0,10,2,9,3}
		#         },
		#         {
		#             {9,12,14,16},//17
		#             {11,0,10,9}
		#         }
		# };
		r = []
		i = int(index/self.l)
		j = index%self.l
		r += [ [i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j]]
		r2 = []
		for k in r:
			if k[0]>=0 and k[0]<self.l and k[1]>=0 and k[1]<self.l:
				r2.append(k)
		return r2


	def getWords(self, index, num):
		words = []
		# print(index, num)
		if num>2:
			self.buf.append(index)
			for i in self.getNeighbours(index):
				if self.l*i[0]+i[1] not in self.buf:
					a = self.grid[int(index/self.l)][index%self.l]
					for j in self.getWords(self.l*i[0]+i[1], num - 1):
						a+= j
						words.append(a)
						# print(self.buf)
						a = a[:-(len(j))]
			self.buf.pop()
		elif num==2:
			for i in self.getNeighbours(index):
				if self.l*i[0]+i[1] not in self.buf:
					a = self.grid[int(index/self.l)][index%self.l]
					a += self.grid[i[0]][i[1]]
					words.append(a)

		return words





	
if __name__=='__main__':
	T = TeluguPoti()
	T.save(T.filterFromDictionary())
	# T.save(T.getWords(0,2))
