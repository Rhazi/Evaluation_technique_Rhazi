#include <iostream>
using namespace std;



void drawback(int arr[], int n)
{
  int i(0);
  while (i < n-1)
  {
    while ((i < n-1) && (arr[i] < arr[i+1]))
    {
      i++;
    }
    if (i == n-1)
    {
      break;
    }
    int buy(i);
    while ((i<n-1) && (arr[i] > arr[i+1]))
    {
      i++;
    }
    int sell(i);
    cout << buy << sell << -arr[buy] + arr[sell] << endl;
}
}

int main()
{
  int arr[] = {1,9,3,0,1,8,2};
  int n = sizeof(arr)/sizeof(arr[0]);
  drawback(arr, n);
  return 0;
}
