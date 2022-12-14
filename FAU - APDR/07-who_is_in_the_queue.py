#[ ] The metal stick must know who are there in the queue. 
# For that reason, initialize a constructor which receives an argument data of the datatype list.
# Store this argument as a class attribute, data, for further use.

# ## Managing Queue ##
class Queue:
	# init method or constructor
	def __init__(self, data):
		if type(data)== int or type(data)==float:
			self.data=[data]
		else: self.data = data

	# Show the current Queue
	def display(self):
		print('Hello, the current queue is', self.data)
		

    # Remove the first element of the list
	def dequeue(self):
		print('Trying to DEQUEUE: ', self.data)
		if len(self.data)>0:
			del self.data[len(self.data)-1]
    
    # Add new members to the queue
	def enqueue(self,person):
		print('Trying to ENQUEUE: ', self.data, " and person: ", person)
		if type(person)==int or type(person)==float:
			if person>0: self.data.append(person)    
		if type(person)==list:
			self.data.extend(person)
		if type(person)==tuple:
			self.data.append(person)    

    # Check if the person is member
	def is_member(self, person):
		print('Trying to check is_member for: ', self.data, " and person: ", person)
		if person in self.data: return True
		else: return False


## Write your PriorityQueue class here ##
class PriorityQueue(Queue):
	# init method or constructor
	def __init__(self, data, priority):
		print('for data:', data,' and for Priority', priority)
		super().__init__(list(zip(data,priority)))		
	
	#Sort the priorizized queue
	def sorted_queue(self):
		print('Priority Queue - Sorting list')
		print('for data:', self.data)
		self.data= sorted(self.data, key=lambda x:x[1], reverse= True)
	
	#Add a new element to the Queue (person,priority)
	def enqueue(self, person, priority):
		print('Priority Queue - Enqueuen list')
		print('for data:', self.data,' and for Person', person,' and for Priority', priority)
		newPerson=(person,priority)
		super().enqueue(newPerson)
		self.sorted_queue()

	#Take the last element of the Queue
	def dequeue(self):
		print('Priority Queue - Dequeuen list')
		print('for data:', self.data)
		super().dequeue()

	#Check if the element (person, priority) is part of the queue
	def is_member(self, person):
		print('Priority Queue - is member')
		print('for data:', self.data,' and for Person', person)
		onlyMembers = list(zip(*self.data))[0]
		if person in onlyMembers: return True
		else: return False
	
	#Show the current Queue	
	def display(self):
		print('Hello, the current queue is', self.data)

#Testing the creation of the Queue
list1=[1,2,3]
print(len(list1))
q1 = Queue(1.5)
q1.dequeue()
q1.enqueue(1)
person=[5,2,4]
q1.enqueue(person)
q1.display()
print(q1.is_member(10))

#Testing the Prioritized Queue
data=[1,2,3]
priority=[22,11,44]
priority_q1=PriorityQueue(data,priority)
priority_q1.sorted_queue()
priority_q1.display()
#priority_q1.dequeue()
#priority_q1.display()
print(priority_q1.is_member(11))
priority_q1.enqueue(10,35)
priority_q1.display()






