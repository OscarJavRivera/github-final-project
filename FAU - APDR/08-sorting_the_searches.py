##----------------------------------------------------------------------------------------------------------
## Create your ModifiedMergeSort class here ##
class ModifiedMergeSort:
    
	def __init__(self,data):
		self.data=data
		self.pieces=[]

	def sorting(self):
		self.data.sort()
		print('New sorted list: ',self.data)
		return self.data
	
	def __make_atoms(self):
		for i in range(len(self.data)):
			print(self.data[i])
			self.pieces.append([self.data[i]])
		print('new Atomized list',self.data)

##Testing the ModifiedMergeSort class
list1 = ModifiedMergeSort([11, 22, 3, 44])
list1.sorting()


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
