#include <iostream>
#include <regex>
#include <string>
#include <fstream>


using std::cout;
using std::endl;
using std::smatch;
using std::regex;
using std::string;
using std::regex_search;
using std::ifstream;


int main()
{
  ifstream lines("input_4.txt");
  regex e("(\\d+)-(\\d+),(\\d+)-(\\d+)");
  smatch m;
  string s;
  int p1 = 0,
      p2 = 0;

  while (getline(lines, s))
  {
    regex_search(s, m, e);
    int a = stoi(m[1]), b = stoi(m[2]), c = stoi(m[3]), d = stoi(m[4]);

    p1 += ((a >= c && b <= d) || (a <= c && b >=d));
    p2 += (a >= c && a <= d) || (b >= c && b <= d)
       || (c >= a && c <= b) || (d >= a && d <= b);
  }
  cout << p1 << endl << p2 << endl;
  return 0;
}
