#include <fstream>
#include <iostream>


using std::cout;
using std::endl;
using std::ifstream;
using std::string;


char translate(char own)
{
  if (own == 'X')
    return 'A';
  else if (own == 'Y')
    return 'B';
  else
    return 'C';
}


int winPoints(char opp, char own)
{
  int result = 0;
  if (opp == own)
    result = 3;
  else if (((own - opp) + 3) % 3 == 1)
    result = 6;
  return result;
}


int choicePoints(char own)
{
  return own - 'A' + 1;
}


int dutyCalls(char opp, char own)
{
  int result;
  if (own == 'B')
    result = choicePoints(opp);
  else if (own == 'A')
    result = choicePoints(opp + 2) % 3;
  else
    result = choicePoints(opp + 1) % 3;
  if (result == 0)
    result = 3;
  return result;
}


int main()
{
  ifstream input("input_2.txt");
  string cur_line;
  char opp,
       own;
  int p1 = 0,
      p2 = 0;

  while (getline(input, cur_line))
  {
    opp = cur_line[0];
    own = translate(cur_line[2]);

    p1 += winPoints(opp, own);
    p1 += choicePoints(own);
    
    p2 += 3 * choicePoints(own) - 3;
    p2 += dutyCalls(opp, own);
  }
  cout << p1 << endl;
  cout << p2 << endl;
  return 0;
}
