#include <iostream>
using namespace std;



void swap( int *a, int *b)
{
  int u = *a;
  *a = *b;
  *b = u;

}

void tri_selection ( int arr[], int n)
{

  for (int k = 0; k < n-1; k++)
  {
    int min = k;
    for (int j = k; j < n; j++)
      if (arr[j] < arr[min])
      {
        min = j;
      }
    swap(&arr[min], &arr[k]);
  }
}

void printex(int arr[], int n)
{
  for (int k = 0; k <n; k++ )
  {
    cout << arr[k]  << endl;

  }
}

int main()
{
  int arr[] = {1,9,7,3,6,5};
  int n = sizeof(arr)/sizeof(arr[0]);
  tri_selection(arr, n);
  printex(arr,n);
}
