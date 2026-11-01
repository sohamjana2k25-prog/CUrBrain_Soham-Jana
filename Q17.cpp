#include <bits/stdc++.h>
using namespace std;
void Frequency(int arr[], int n) {
    unordered_map<int, int> map;
    for (int i = 0; i < n; i++) {
        map[arr[i]]++;
    }
    int largest=0;
    int corr=0;
    for (auto x : map) {
        if (largest < x.second) {
            largest = x.second;
            corr = x.first;
        } else if (largest == x.second) {
            if (x.first < corr) {
                corr = x.first;
            }
        }
    }
    cout << corr << " " << endl;
}
int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Frequency(arr, n);
    return 0;
}
