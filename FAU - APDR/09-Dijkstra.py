import sys
## Write your algorithm here ##
class Dijkstra:
    def __init__(self, graph,start_node,end_node):
        self.graph=graph
        self.start_node=start_node
        self.end_node=end_node
        
        #Store Nodes of the Graph
        self.nodes=[]
        self.node_val=[]
        self.base_val=[]
        self.visited={}
        self.route={}
        self.__initiliaze()

    def __initiliaze(self):
        
        #Initialize nodes
        self.nodes.append(self.start_node)
        for i in self.graph:
            if i!=self.start_node:
                self.nodes.append(i)
        
        #'node_val' is a list whose length is equal to the number of nodes
        self.node_val={}
        for i in self.nodes:
            #self.node_val.append('')
            self.node_val.update({i:sys.maxsize})
        ini_node=self.nodes[0]
        self.node_val.update({self.start_node:0})

        # 'base_val' captures the current node's base value
        self.base_val=0

        # Use to check if a node is visited or not. It is a list of length of total number of nodes
        for i in self.nodes:
            #self.visited.append(False)
            self.visited.update({i:False})
        self.visited.update({self.start_node:True})

    def __get_neighbours(self,node):
        '''(string) -> dictionary
        It returns the neighbours of the node from the graph along with the weights
        '''
        return self.graph[node]

    def __visited_node(self,node):
        '''(string)-->None
        which takes in one argument node and sets the visited attribute of this node as True.
        '''
        self.visited[node]=True
        

    def __is_neighbour(self,node_1,node_2):
        '''(strin, string)-->Boolean
        This method returns True in case node_2 is a neighbour of node_1, else returns False.
        '''
        node1_neighbour=self.__get_neighbours(node_1)
        if node_2 in node1_neighbour: return True
        else: return False
    
    def __update_node_val(self,current_node):
        '''(strin, string)-->
        looks at all the neighbours of the current_node and if any neighbour is unvisited sets
        the node_val attribute of the neighbour node to the minimum of the previous value it had 
        or current value of the base_val attribute plus the edge weight of going from 
        current_node to this neighbour node.

        If a change in value occurs for a node, add the node as a key and the current_node as.
        the value to the attribute route
        '''
        temp_value=0
        neighbourhood=self.__get_neighbours(current_node)
        for neighbour in neighbourhood:
            if self.visited[neighbour]==False:
                temp_value=self.node_val[current_node]+neighbourhood[neighbour]
                if self.node_val[neighbour]>temp_value:
                    self.node_val[neighbour] = temp_value
                    self.route[neighbour]=current_node
    
    def __get_min_val(self):
        '''(None)-->int
        It returns the minimum node_val of the unvisited nodes. 
        '''
        current_min_val = ''
        for node in self.visited:
            if self.visited[node]==False: 
                if current_min_val=='':
                    current_min_val = node
                
                elif self.node_val[current_min_val]> self.node_val[node]:
                    current_min_val = node
                
        return current_min_val

    def __next_node(self,current_node):
        '''(String)-->String
        It takes in an argument current_node and returns the next node to be visited.
        In this method you need to update the node values by passing the current node. 
        Then you need to set the base_val attribute by grabbing the minimum value of 
        the unvisited nodes. Finally you need to return the next node which is nothing 
        but the node which is unvisited and has the least node_val.
        '''
        self.__update_node_val(current_node)
        self.__visited_node(current_node)
        next_node=self.__get_min_val()
        return next_node   
   
    def find_path(self):
        '''(None)-->None
        This method returns the path at the end by using the route attribute
        '''
        print('The graph is: ',self.graph)
        #Look for the next node with the shortest value
        next_node=self.start_node
        while next_node!='':
            next_node= self.__next_node(next_node)

        #Find the shortest path and reverse it
        shortest_path=[]
        node=self.end_node
        shortest_path.append(node)
        while node!=self.start_node:
            node=self.route[node]
            shortest_path.append(node)
        shortest_path.reverse()
        return shortest_path


#Testing the Dijkstra Algorithm
graph={
        'B': {'C': 5, 'A': 5, 'E': 1},
        'C': {'B': 5, 'D': 5, 'A': 3, 'E': 7}, 
        'D': {'C': 5, 'A': 2, 'E': 8}, 
        'A': {'B': 5, 'C': 3, 'D': 2}, 
        'E': {'B': 1, 'C': 7, 'D': 8, 'F': 2, 'S': 9}, 
        'F': {'E': 2, 'S': 11},
        'S': {'E': 9, 'F': 11}}
g1=Dijkstra(graph,'S','A')
print(g1.find_path())


