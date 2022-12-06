#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::vector;
using std::sort;


int main()
{
  ifstream input("input_1.txt"); 
  string cur_line;
  vector<int> totals;
  int running_sum = 0;

  while (getline(input, cur_line))
  {
    if (cur_line.empty())
    {
      totals.push_back(running_sum);
      running_sum = 0;
    }
    else
      running_sum += stoi(cur_line);
  }

  sort(totals.rbegin(), totals.rend());
  cout << totals[0] << endl;
  int solution = totals[0] + totals[1] + totals[2];
  cout << solution << endl;

  return 0;
}
