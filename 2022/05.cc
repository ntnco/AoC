#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <regex>
#include <stack>


using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::vector;
using std::regex;
using std::smatch;
using std::stack;


void getInput(vector<string> &piles, vector<string> &steps)
{
  ifstream input("input_5.txt");
  string s;

  while (getline(input, s) && !s.empty())
    piles.push_back(s);

  while (getline(input, s))
    steps.push_back(s);
}


vector<stack<char>> fill_vector(vector<string> piles)
{
  vector<stack<char>> vs(9);

  for (int i = 7; i >=0; --i)
    for (int j = 0; j < 9; ++j)
    {
      char c = piles[i][j*4 + 1];
      if (isalpha(c))
        vs[j].push(c); 
    }
  return vs;
}


void get_vals(string step, int &a, int &b, int &c)
{
  regex e("move (\\d+) from (\\d+) to (\\d+)");
  smatch m;
  regex_search(step, m, e);
  a = stoi(m[1]);
  b = stoi(m[2]) - 1;
  c = stoi(m[3]) - 1;
}


void executeAll(vector<string> steps, vector<stack<char>> &vs, bool is9000)
{
  for (auto step : steps)
  {
    int times, init, dest;
    get_vals(step, times, init, dest);
    if (is9000) {
      for (int i = 0; i < times; ++i)
      {
        vs[dest].push(vs[init].top());
        vs[init].pop();
      }
    } else
    {
      stack<int> tmp;
      for (int i = 0; i < times; ++i)
      {
        tmp.push(vs[init].top());
        vs[init].pop();
      }
      for (int i = 0; i < times; ++i)
      {
        vs[dest].push(tmp.top());
        tmp.pop();
      }
    }
  }
}


void printTops(vector<stack<char>> vs)
{
  string solution;

  for (auto v : vs)
    solution += v.top();
  cout << solution << endl;
}


int main()
{
  vector<string> piles, steps;
  getInput(piles, steps);

  vector<stack<char>> vs = fill_vector(piles);
  executeAll(steps, vs, true);
  printTops(vs);

  vector<stack<char>> vs2 = fill_vector(piles);
  executeAll(steps, vs2, false);
  printTops(vs2);
  return 0;
}
