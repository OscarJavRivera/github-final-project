#[ ] The metal stick must know who are there in the queue. 
# For that reason, initialize a constructor which receives an argument data of the datatype list.
# Store this argument as a class attribute, data, for further use.

# ## Create your Queue class here ##
class Queue:

	# init method or constructor
	def __init__(self, data):
		self.data = data

	# Show the current Queue
	def display(self):
		print('Hello, the current queue is', self.data)
		

    # Remove the first element of the list
	def dequeue(self):
		if len(self.data)>0:
			del self.data[0]
    
    # Add new members to the queue
	def enqueue(self,person):
		if type(person)==int or type(person)==float:
			if person>0: self.data.append(person)    

    # Check if the person is member
	def is_member(self, person):
		if person in self.data: return True
		else: return False

class PriorityQueue(Queue):
	# init method or constructor
	def __init__(self, data, priority):
		super().__init__(data)

	def sorted_queue(self):
		print('Sorting list')
	
	def enqueue(self, person, priority):
		print('Enqueuen list')
	def dequeue(self):
		print('Dequeuen list')
	def is_member(self, person):
		print('is member')

#Testing the creation of the Queue
list1=[1,2,3]
print(len(list1))
q1 = Queue(list1)

q1.dequeue()
q1.enqueue(1)
q1.enqueue(1.5)
q1.display()
print(q1.is_member(10))




