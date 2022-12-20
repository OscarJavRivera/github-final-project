##----------------------------------------------------------------------------------------------------------
## Create your ModifiedMergeSort class here ##
class ModifiedMergeSort:
    
	def __init__(self,data):
		self.data=data
		self.pieces=[]


	def sorting(self):
		if len(self.data)==0: return self.data
		else:
			self.__make_atoms()
			self.__combine()
			print('New sorted list: ',self.data)
			len_pieces=len(self.pieces[0])
			for i in range(len(self.pieces[0])):
				self.data[i]=self.pieces[0][i]
			return self.data
	
	def display(self):
		print('Hello, the sorted list is', self.data)

	##__make_atoms updates the pieces attribute by looping over all the elements of the data attribute
	## and inserting them inside the pieces attribute
	def __make_atoms(self):
		for i in range(len(self.data)):
			self.pieces.append([self.data[i]])
		print('new Pieces list',self.pieces)
	
	##__combine does the upward combine par of the Mergesort
	def __combine(self):
		updated_pieces = [] ## This variable will holde the combined (sorted) result of the left subpiece and the righ subpiece
		len_pieces=len(self.pieces)
		mid_point=len_pieces//2 # Finding the middle point of pieces
		
		if len_pieces>1:
			i=0
			while i < len_pieces:
				if len_pieces%2==0:	subpiece=[self.pieces[i],self.pieces[i+1]]
				else:subpiece=[self.pieces[i],self.pieces[i-1]]
				subpiece=self.__subpiece_sort(subpiece)
				updated_pieces.append(subpiece) 
				i=i+2
			self.pieces=updated_pieces
			print('length of self.pieces: ',len(self.pieces))
			print('combined Pieces list',self.pieces)
			self.__combine()
		else: 
			return self.pieces
	
	##__subpiece_sort compares the two elements of the subpiece list
	def __subpiece_sort(self,subpiece):
		sort_ps=[]
		subpiece_aux=subpiece.copy()
		len_subpiece=len(subpiece[0])
		subpiece=[]
		if len_subpiece==1: # if the subpieces is has one single element, then compare one to one
			elm_0=subpiece_aux[0][0]
			elm_1=subpiece_aux[1][0]
			if elm_0>elm_1:
				subpiece_aux[0]=elm_1
				subpiece_aux[1]=elm_0
			else:
				subpiece_aux[0]=elm_0
				subpiece_aux[1]=elm_1
			subpiece=subpiece_aux
		else:					#if the subpieces has two arrays, the compare max vs min of the arrays
			elm_0=subpiece_aux[0]
			elm_1=subpiece_aux[1]
			if elm_1[1]<=elm_0[0]:
				subpiece.append(elm_1[0])
				subpiece.append(elm_1[1])
				subpiece.append(elm_0[0])
				subpiece.append(elm_0[1])
			
			elif elm_1[0]>=elm_0[1]:
				subpiece.append(elm_0[0])
				subpiece.append(elm_0[1])
				subpiece.append(elm_1[0])
				subpiece.append(elm_1[1])
				
			elif elm_1[0]>=elm_0[0] and elm_1[1]<=elm_0[1]:
				subpiece.append(elm_0[0])
				subpiece.append(elm_1[0])
				subpiece.append(elm_1[1])
				subpiece.append(elm_0[1])

			elif elm_1[0]<=elm_0[0] and elm_1[1]>=elm_0[1]:
				subpiece.append(elm_1[0])
				subpiece.append(elm_0[0])
				subpiece.append(elm_0[1])
				subpiece.append(elm_1[1])
			
			
		return subpiece

##Testing the ModifiedMergeSort class
#[8], [2], [2], [1], [5], [6]
list1 = ModifiedMergeSort([22, 11, 3, 44])
list1.sorting()
list1.display()


##----------------------------------------------------------------------------------------------------------
## Create your BinarySearch class here ##
class BinarySearch:
	def __init__(self,data):
		self.data=data
		

	def search(self,data):
		self.data=data
		print(range(len(self.data)))
		if range(len(self.data))==0: return True
		else: return False











					# for i in range(len_subpiece):
		# 	for j in range(len(subpiece[i])):
		# 		sort_ps.append(subpiece[i][j])
		# subpiece=[]

		# while x<len(sort_ps):
		# 	if sort_ps[x]>=sort_ps[x+3]:
		# 		subpiece.append(x+2)
		# 		subpiece.append(x+3)
		# 		subpiece.append(x)
		# 		subpiece.append(x+1)
				
		# 	if sort_ps[x+1]>=sort_ps[x+2]:
		# 		subpiece.append(x)
		# 		subpiece.append(x+1)
		# 		subpiece.append(x+3)
		# 		subpiece.append(x+2)
			
		# 	if sort_ps[x]<=sort_ps[x+2] and sort_ps[x+1]>=sort_ps[x+3]:
		# 		subpiece.append(x)
		# 		subpiece.append(x+2)
		# 		subpiece.append(x+3)
		# 		subpiece.append(x+1)

		# 	elif sort_ps[x]<=sort_ps[x+2] and sort_ps[x+1]<=sort_ps[x+3]:
		# 		subpiece.append(x)
		# 		subpiece.append(x+2)
		# 		subpiece.append(x+1)
		# 		subpiece.append(x+3)
		# 	else:
				

		# 	if sort_ps[x]>sort_ps[x+2] and sort_ps[x+1]<sort_ps[x+3]:
		# 		subpiece.append(x+2)
		# 		subpiece.append(x)
		# 		subpiece.append(x+1)
		# 		subpiece.append(x+3)
		# 	x=x+4
		# for x in range(len(sort_ps)-1):
		# 	if sort_ps[x]<=sort_ps[x+1]:
		# 		subpiece.append(sort_ps[x])
		# 		subpiece.append(sort_ps[x+1])
		# 	else:
		# 		subpiece.append(sort_ps[x+1])
		# 		subpiece.append(sort_ps[x])