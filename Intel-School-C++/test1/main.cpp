#include <stdio.h>
#include <iostream>

using namespace std;

int search(int* _arr, int _n, int tofind)
{
    for (int i = 0; i < _n; i++)
    {
        if (_arr[i] == tofind)
            return i;
    }
    return -1;
}


int main()
{
    int N, X;
    cout << "Enter size of array: ";
    cin >> N;
    cout << "Enter element to find: ";
    cin >> X;
    int* arr = new int[N];
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    int tmp = search(arr, N, X);
    delete arr;
    return tmp;
}