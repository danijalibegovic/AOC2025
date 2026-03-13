#include <map>
#include <unordered_map>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;

string END_NODE = "out";
long long brojPuteva = 0;
int MAX_DEPTH = 200;   // or whatever limit you want

unordered_map<string, vector<string>> graph;
unordered_map<string, int> id; 
vector<string> id_to_name;
vector<bool> visited;

int get_id(const string& s) {
    if (id.count(s)) return id[s];
    int new_id = id.size();
    id[s] = new_id;
    id_to_name.push_back(s);
    return new_id;
}

void dfs(int current, bool dac, bool fft, int depth) {
    if (depth > MAX_DEPTH) return;

    visited[current] = true;
    string name = id_to_name[current];

    if (name == "dac") dac = true;
    if (name == "fft") fft = true;

    if (!graph[name].empty() && graph[name][0] == END_NODE) {
        if (dac && fft) brojPuteva++;
        visited[current] = false;
        return;
    }

    for (auto &nx_name : graph[name]) {
        int nx = id[nx_name];
        if (!visited[nx]) {
            dfs(nx, dac, fft, depth + 1);
        }
    }

    visited[current] = false;
}
    
int main() {
    ifstream file("reactor.txt");
    string line;

    while (getline(file, line)) {
        string key = line.substr(0, 3);
        string rest = line.substr(4);

        stringstream ss(rest);
        string v;

        while (ss >> v) {
            graph[key].push_back(v);
            get_id(v);
        }
        get_id(key);
    }

    visited.assign(id.size(), false);

    dfs(id["svr"], false, false, 0);

    cout << brojPuteva << endl;
    return 0;
}
