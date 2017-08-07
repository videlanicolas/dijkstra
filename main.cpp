#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Neighbor
{
	Node * self;
	Node * next;
	unsigned path_cost;
}

class Node
{	
	Neighbors * neighbor_list;
public:
	Node(string);
	string label;
	unsigned cost;
	Node * prev;
};

Node::Node(string input_string)
{
	label = input_string;	
}

class Graph
{
	Node * nodes[];
public:
	Graph();
};

Graph::Graph()
{
	
}

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cout << "Please input the filename with the graph to load." << endl;
		return 1;
	}
	ifstream file;
	file.open(argv[1]);
	if (file.is_open())
	{
		string line;
		while (getline(file,line))
		{
			cout << line << endl;
		}
		file.close();
	}
	else
	{
		cout << "Could not open file." << endl;
		return 1;
	}
	string mystring("hola");
	Node node (mystring);
	cout << node.label << endl;
	return 0;
}