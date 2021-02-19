#include <iostream>
#include <string>
using namespace std;


void swap(int *a , int *b)
{
  int u = *a;
  *a = *b;
  *b = u;
}

void BubbleSort(int arr[], int n)

{
  for ( int i = 0; i<n; i++)
  {
    bool test = true;
    for ( int j=0; j < n-i-1; j++)
    {
      if (arr[j] > arr[j+1])
      {
        swap(&arr[j], &arr[j+1]);
        test = false;
      }
    }
    if (test == true)
    {
      break;
    }
  }
}


void printex(int arr[], int n)
{
  cout << " la liste:" << endl;
  for (int k=0; k<n; k++)
  {
    cout << arr[k] << endl;
  }
}

int main()
{
  int arr[] = {1,8,3,2,9};
  int n = sizeof(arr)/sizeof(arr[0]);
  BubbleSort(arr, n);
  printex(arr, n);
  return 0;
}
