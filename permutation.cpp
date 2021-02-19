#include <iostream>
using namespace std;

void permutation(string arr, int l, int r)
{
  if (l == r)
  {
    cout << arr << endl;
  }
  else
  {
  for (int i(l); i<=r; i++)
  {
    swap(arr[l], arr[i]);
    permutation(arr, l+1,r);
    swap(arr[l], arr[i]);
  }
}
}

int main()
{
  string a = "ABC";
  int l = 0;
  int r = a.size()-1;
  permutation(a, l, r);
  return 0;
}
