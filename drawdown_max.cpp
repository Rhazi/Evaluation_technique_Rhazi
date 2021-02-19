#include <iostream>
using namespace std;


void drawback(int arr[], int n)
{
  int i(0);
  int max(0);
  int ind_buy;
  int ind_sell;

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
  if (max > -arr[buy] + arr[sell])
  {
    ind_buy = buy;
    ind_sell = sell;
    max = -arr[buy] + arr[sell];
  }
  }

  cout << ind_buy << ind_sell << max << endl;
}

int main()
{
  int arr[] = {1,9,3,0,1,8,2};
  int n = sizeof(arr)/sizeof(arr[0]);
  drawback(arr, n);
  return 0;
}
