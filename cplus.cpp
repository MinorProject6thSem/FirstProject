#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
 
// data structure to store graph edges
struct Edge {
    int src, dest;
};
 
// class to represent a graph object
class Graph
{
    public:
    // An array of vectors to represent adjacency list
    vector<vector<int>> adj;
 
    // Constructor
    Graph(vector<Edge> const &edges, int N)
    {
        // resize the vector to N elements of type vector<int>
        adj.resize(N);
 
        // add edges to the undirected graph
        for (int i = 0; i < edges.size(); i++)
        {
            int src = edges[i].src;
            int dest = edges[i].dest;
 
            adj[src].push_back(dest);
            adj[dest].push_back(src);
        }
    }
};
 
// string array to store colors (10-colorable graph)
string COLORS[] = {"", "sub1", "sub2", "sub3", "sub4"};
 
// Function to check if it is safe to assign color c to vertex v
bool isSafe(Graph const &graph, vector<int> color, int v, int c)
{
    // check color of every adjacent vertex of v
    for (int u : graph.adj[v])
        if (color[u] == c)
            return false;
 
    return true;
}
 
void kColorable(Graph const &graph, vector<int> &color, int k, int v, int N)
{
    // if all colors are assigned, print the solution
    if (v == N)
    {
        for (int v = 0; v < N; v++)
            cout << setw(8) << left << COLORS[color[v]];
        cout << endl;
 
        return;
    }
 
    // try all possible combinations of available colors
    for (int c = 1; c <= k; c++)
    {
        // if it is safe to assign color c to vertex v
        if (isSafe(graph, color, v, c))
        {
            // assign color c to vertex v
            color[v] = c;
 
            // recur for next vertex
            kColorable(graph, color, k, v + 1, N);
 
            // backtrack
            color[v] = 0;
        }
    }
}
 
// main function
int main()
{
    // vector of graph edges as per above diagram
    vector<Edge> edges = {
        {0, 1}, {0, 2}, {0, 3}, {1,2}, {1, 3}, {2,3}
    };
 
    // Number of vertices in the graph
    int N = 4;
 
    // create a graph from edges
    Graph g(edges, N);
 
    int k = 4;
 
    vector<int> color(N, 0);
 
    // print all k-colorable configurations of the graph
    kColorable(g, color, k, 0, N);
 
    return 0;
}