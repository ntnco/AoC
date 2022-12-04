#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>


using std::cout;
using std::endl;
using std::ifstream;
using std::string;
using std::unordered_set;


char getCommon(unordered_set<char> uset, string s)
{
  for (char c : s)
    if (uset.count(c) == 1)
      return c;
  exit(1);  // exercise constraints prevent this
}


int valueChar(char c)
{
  if (c <= 'Z')
    return c - 'A' + 27;
  else
    return c - 'a' + 1;
}


int main()
{
  string cur;
  ifstream lines("input_3.txt");
  int p1 = 0;

  while (getline(lines, cur))
  {
    unordered_set<char> uset{};
    int mid = cur.size() / 2;

    for (char c : cur.substr(0, mid))
      uset.insert(c);

    char common = getCommon(uset, cur.substr(mid, 2 * mid));
    p1 += valueChar(common);
  }
  cout << p1 << endl;

  int p2 = 0;
  lines.clear();
  lines.seekg(0);
  int i = 0;
  unordered_set<char> uset{};
  unordered_set<char> uset2{};

  while (getline(lines, cur))
  {
    if (i % 3 == 0)
    {
      uset.clear();
      for (char c : cur)
        uset.insert(c);
    } 
    else if (i % 3 == 1)
    {
      uset2.clear();
      for (char c : cur)
        if (uset.count(c) == 1)
          uset2.insert(c);
    }
    else
    {
      char common = getCommon(uset2, cur);
      p2 += valueChar(common);
    }
    i += 1;
  }
  cout << p2 << endl;

  return 0;
}
