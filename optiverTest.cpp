int DaysInMonth(int month, int year);
// Do not edit above this line. It is only shown so you can see the function signature.
/*
 * Complete the function below.
 1. Need to store the number of days for each month -> Could use a map but since
 this most likely won't change can store in an array where indexes reference month
    - This is haandled by Days in Month
 2. Will hvae to deal with leap years some way each year if divisible by 4 gets 
 an extra day in Februrary
    - This case only needs to be considered if DaysInMonth does not handle leap years
We could go month by month and just add it all up but this will make the O(m) m = number of months between dates

 */

int countLeapYears(int year, int month) {
    if(month <= 2) {
        year--;
    }
    return year/4 - year/100 + year/400
}
int countDays(int year, int month, int day) {
    int numDays = year*365 + day;
    for(int i = 1; i < month; i++) {
        numDays += DaysInMonth(i, year);
    }
    numDays += countLeapYears(year, month);
    return numDays;
}
int DaysBetween(int year1, int month1, int day1, int year2, int month2, int day2) {
    int numDays1 = countDays(year1, month1, day1);
    int numDays2 = countDays(year2, month2, day2);

    return numDays2 - numDays1; 
}

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
/*
1. For input format we need to make sure
    - one line
    - leading/trailing white space not allowed
    - (A, B) format
    - All values are uppercase
    - Only one space between pairs
    
2. Have a list of edges and see if pair already exists or can look up in a map<letter, set> grpah type
to handle duplicate pairs
3. Parent has more than two children would mean that the root has to have max 2 children and interior nodes
will have max 3 children so have to identify root somehow
4. Multiple roots will only happen when we have a completely new node that hasn't been in an edge yet
5. Input contains a cycle could use DFS everytime we add a node (Adds a lot of complexity)
    - Could implement a set disjoint structure which would make checking for each edge O(1) 
*/
using namespace std;

class Graph {
    public:
        unordered_map<string, unordered_set<string>> graph;
        unordered_map<string, int> childrenCount;
        unordered_set<string> parents;
        unordered_set<string> children;
        unordered_set<string> visitedPairs;
        bool duplicatePairError = false;
        bool childrenCountError = false;
        bool multipleRootError = false;
        bool cycleError = false;
        int getChildrenCount(string vertex);
        int incrementChildrenCount(string vertex);
        int addEdge(string parent, string child);
        int detectCycle();
        string lexicographicPrint(string node);
        void printGraph();
        
    
};

int Graph::getChildrenCount(string vertex) {
    auto it = childrenCount.find(vertex);
    if (it == childrenCount.end()) {
        return -1;
    }
    return it->second;
}

int Graph::incrementChildrenCount(string vertex) {
    auto it = childrenCount.find(vertex);
    if (it == childrenCount.end()) {
        childrenCount[vertex] = 1;
        return 1;
    }
    childrenCount[vertex] += 1;
    return childrenCount[vertex];
}

int Graph::addEdge(string parent, string child) {
    if(visitedPairs.find(parent+child) != visitedPairs.end()) {
        duplicatePairError = true;
    } else {
        visitedPairs.insert(parent+child);
    }
    auto pIt = parents.find(parent);
    auto cIt = children.find(parent);
    if(pIt == parents.end() && cIt == children.end()) {
        parents.insert(parent);
    }
    if(pIt != parents.end() && cIt != children.end()) {
        parents.erase(pIt);
    }
    children.insert(child);
    
    if(parent == child) {
        cycleError = true;
    }
    if(visitedPairs.find(child+parent) != visitedPairs.end()) {
        cycleError = true;
    }
    
    auto it = graph.find(parent);
    if(it == graph.end()) {
        unordered_set<string> children;
        children.insert(child);
        graph[parent] = children;
        incrementChildrenCount(parent);
        if(getChildrenCount(parent) > 2) {
            childrenCountError = true;
        }
    } else {
        incrementChildrenCount(parent);
        if(getChildrenCount(parent) > 2) {
            childrenCountError = true;
        }
        graph[parent].insert(child);
    }
    it = graph.find(child);
    if(it == graph.end()) {
        unordered_set<string> parents;
        parents.insert(parent);
        graph[child] = parents;
    } else {
        graph[child].insert(parent);
    }
    
    return 1;
}

int Graph::detectCycle() {
    auto it = graph.begin();
    unordered_set<string> visited;
    stack<tuple<string, string>> s;
    while(it != graph.end()) {
        s.push(make_tuple(it->first, "None"));
        while(!s.empty()){
            auto item = s.top();
            auto node = get<0>(item);
            auto parent = get<1>(item);
            s.pop();
            if(visited.find(node) != visited.end()) {
                continue;
            }
            visited.insert(node);
            auto graphIt = graph.find(node); //This node should always exist
            for (const auto& el: graphIt->second) {
                if(visited.find(el) != visited.end() && el != parent) {
                    cycleError = true;
                    return 1;
                }
                s.push(make_tuple(el, node));
            }
            
        }
        it++;
            
    }
    return 0;
        
}

string Graph::lexicographicPrint(string node) {
    if(graph[node].size() == 0) {
        return "("+ node + ")";
    } else if(graph[node].size() == 1) {
        return "(" + node + lexicographicPrint(*(graph[node].begin())) + ")";
    } else if(graph[node].size() == 2){
        auto i1 = *(graph[node].begin());
        auto i2 = *(graph[node].end());
        if(i1 < i2) {
            return "(" + node + lexicographicPrint(i1) + lexicographicPrint(i2) + ")";
        }
        return  "(" + node + lexicographicPrint(i2) + lexicographicPrint(i1) + ")";
    } else {
        return "";
    }
}

void Graph::printGraph() {
    auto vertex = graph.begin();
    
    for(auto i : graph) {
        cout << "Vertex "; 
        cout << i.first; 
        cout << " : ";
        for(auto j : i.second) {
            cout << " "; 
            cout << j;
        }
        cout << endl;
    }
}

//I checked this function
int ValidateInput(string input, string empty) {
    if(input[0] == ' ' || input[input.length()-1] == ' ' || empty.length() != 0) {
        return 0;
    }
    return 1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string input;
    string empty;
    getline(cin, input);
    getline(cin, empty);
    
    vector<int> errors(5, 1);
    errors[0] = ValidateInput(input, empty);
    Graph tree;
    for(int i = 0; i <= input.length()-5; i+=6) {
        string parent;
        string child;
        if(i+5 < input.length()) {
            if(input[i] != '(' || !isupper(input[i+1]) || input[i+2] != ',' || !isupper(input[i+3]) || input[i+4] != ')' || input[i+5] != ' ') {
                cout << "E1";
                return 0;
            }
        } else {
            if(input[i] != '(' || !isupper(input[i+1]) || input[i+2] != ',' || !isupper(input[i+3]) || input[i+4] != ')') {
                cout << "E1";
                return 0;
            }
        }
        parent = input[i+1];
        child = input[i+3];
        tree.addEdge(parent, child);
    }
    if(tree.parents.size() > 1) {
        tree.multipleRootError = true;
    }
    tree.detectCycle();
    if(tree.duplicatePairError) {
        cout << "E2";
        return 0;
    } else if(tree.childrenCountError) {
        cout << "E3";
        return 0;
    } else if(tree.multipleRootError) {
        cout << "E4";
        return 0;
    } else if(tree.cycleError) {
        cout << "E5";
        return 0;
    }
    tree.printGraph();
    // cout << *(tree.parents.begin());
    // cout << tree.lexicographicPrint(*(tree.parents.begin()));
    return 1;

}