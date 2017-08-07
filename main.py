#!/usr/bin/python3
import sys
from math import inf


class Node(object):
	def __init__(self,label):
		#neighbors = (Node, cost)
		self.label = label
		self.neighbors = list()
		self.cost = inf
		self.visited = False
		self.prev = None
	def __eq__(self,other):
		return True if other.label == self.label else False

class Graph(object):
	def __init__(self):
		self.__paths = list()
		self.__nodes = dict()
		self.__start_node = None
	def __repr__(self):
		return '\n'.join([str(k) + '\n\t' + '\n\t'.join([str(x[1]) + '->' + str(x[0].label) + '({})'.format(x[0].cost) for x in v.neighbors]) for k,v in self.__nodes.items()])
	def __get_lowest_available_node(self):
		lowest_node = None
		for key, node in self.__nodes.items():
			if node.visited:
				continue
			else:
				if lowest_node:
					if lowest_node.cost > node.cost:
						lowest_node = node
				else:
					lowest_node = node
		return lowest_node
	def load(self,filename):
		for path in open(filename).read().splitlines():
			lbl_a, cost, lbl_b = path.split('-')
			if lbl_a not in self.__nodes:
				self.__nodes[lbl_a] = Node(lbl_a)
			if lbl_b not in self.__nodes:
				self.__nodes[lbl_b] = Node(lbl_b)
			self.__nodes[lbl_a].neighbors.append((self.__nodes[lbl_b], int(cost)))
			self.__nodes[lbl_b].neighbors.append((self.__nodes[lbl_a], int(cost)))
		return len(self.__nodes)
	def reset(self):
		for k,v in self.__nodes.items():
			v.visited = False
	def spf(self,start_node,end_node):
		self.__nodes[start_node].cost = 0
		prev = list()
		while True:
			node = self.__get_lowest_available_node()
			if node:
				for n_node, cost in node.neighbors:
					alt = cost + node.cost
					if alt < n_node.cost:
						n_node.cost = alt
						n_node.prev = node
				node.visited = True
			else:
				break
	def get_path(self,start_node,end_node):
		self.spf(start_node,end_node)
		ret = list()
		current_node = self.__nodes[end_node]
		while start_node not in ret:
			ret.append(current_node.label)
			current_node = current_node.prev
		ret.reverse()
		return ret

def main(file='main.graph'):
	"""Nodes: 
	A-10-B
	...
	"""
	graph = Graph()
	l = graph.load(file)
	print("Loaded {0} node{1} to graph.".format(l,'s' if l>1 else ''))
	print(graph)
	print("#############")
	start_node = input("Input start node: ")
	end_node = input("Input end node: ")
	print("Calculating the shortest path from node {0} to {1}.".format(start_node,end_node))
	print("#############")
	try:
		print(str(graph.get_path(start_node,end_node)))
	except KeyError:
		print("One or more nodes do not exist.")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		main()
	else:
		main(sys.argv[1])