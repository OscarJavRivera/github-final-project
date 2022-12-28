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
#list1 = ModifiedMergeSort([22, 11, 3, 44])
#list1.sorting()
#list1.display()


##----------------------------------------------------------------------------------------------------------
## Create your BinarySearch class here ##
class BinarySearch:
	def __init__(self,data):
		self.data=data
		print('This is the list: ',self.data)

	def search(self,val):
		len_data=len(self.data)
		if len_data==0:return False # Check base case
		else:
		#Store the List indixes (min and max
			min_in=0
			max_in=len_data-1
			return self.__bs_helper(val,min_in,max_in)

			
	def __bs_helper(self,val,min_in,max_in):
		# Check the base case when the array has more than 2 elements
		if max_in>=min_in: 
			mid=min_in+(max_in-min_in)//2
			
			if self.data[mid]==val:
				return True#The element was found
			elif self.data[mid]>val:#Check if Value is located in the left of right part of the List
				return self.__bs_helper(val,min_in,mid-1)#Look in the left side of the List
			else:
				return self.__bs_helper(val,mid+1,max_in)
		else:
			return False


#Testing the Binary Seach
list_bs=BinarySearch([1, 11, 22, 44])
#list_bs=BinarySearch([])
val=22
val_found=list_bs.search(val)
print(val_found)
