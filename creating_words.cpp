#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    string ans[t];

    for (int i = 0; i < t; i++)
    {

        string a, b;
        cin >> a >> b;

        char temp = a[0];
        a[0] = b[0];
        b[0] = temp;

        ans[i] = a + " " + b;
    }

    for (int i = 0; i < t; i++)
    {

        cout << ans[i] << endl;
    }

    return 0;
}