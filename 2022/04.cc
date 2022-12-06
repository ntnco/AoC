#include <iostream>
#include <regex>
#include <string>


using std::cout;
using std::cin;
using std::endl;
using std::smatch;
using std::regex;
using std::string;
using std::regex_search;


void p1() {
  regex e("(\\d+)-(\\d+),(\\d+)-(\\d+)");
  smatch m;
  string s;

  while (getline(cin, s))
  {
    regex_search(s, m, e);
    string a = m[1], b = m[2], c = m[3], d = m[4];
    cout << a << " " << b << " " << c << " " << d;
  }
}


int main()
{
  p1();
  return 0;
}
