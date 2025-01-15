#include <iostream>
#include <array>
using namespace std;

int main()
{
    int temp1;
    cin >> temp1;
    int ans[temp1];

    for (int i = 0; i < temp1; i++)
    {
        int temp2;
        cin >> temp2;

        ans[i] = (temp2 / 10) + (temp2 % 10);
    }

    for (int i = 0; i < temp1; i++)
    {
        cout << ans[i] << endl;
    }

    return 0;
}