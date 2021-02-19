#include <iostream>
using namespace std;


void sub(int arr[], int n, int s)
{
  int l = 0;
  int r = n-1;

  while (l<r)
  {
    if (arr[l] + arr[r] == s)
    {
      cout << "("<<l<<","<<r<<")"<<endl;
      cout << "("<<r<<","<<l<<")"<<endl;
    }

    if (arr[l] + arr[r] > s)
    {
      r--;
    }

    else
    {
      l++ ;
    }
  }



}

int main()
{
  int arr[] = {2,5,7,2,8};
  int n = sizeof(arr)/sizeof(arr[0]);
  int s = 7;
  sub(arr, n, s);
  return 0;
}
