#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N1, N2;
    cout << "Enter size of arrays 1 and 2: ";
    cin >> N1 >> N2;
    int* arr1 = new int[N1];
    int* arr2 = new int[N2];
    cout << "Enter elements of arr1: ";
    for (int i = 0; i < N1; i++)
        cin >> arr1[i];
    cout << "Enter elements of arr2: ";
    for (int i = 0; i < N2; i++)
        cin >> arr2[i];

    int* result = new int[N1 + N2];

    for (int i = 0; i < N1; i++)
        result[i] = arr1[i];
    for (int i = N1; i < N1 + N2; i++)
        result[i] = arr2[i-N1];

    sort(result, result+N1+N2);
    cout << "[";
    for (int i = 0; i < N1+N2-1; i++)
        cout << result[i] << ",";
    cout << result[N1+N2-1] << "]";
    return 0;
}