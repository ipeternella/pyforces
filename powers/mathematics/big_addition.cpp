/*
 * Algorithm for handling big sums using the approach of reversing the two numbers in order
 * to easily handle carries during the sum which adds new digits to the output.
 */
#include <bits/stdc++.h>
using namespace std;

int to_digit(char ch) {
    return ch - '0';  // digits will have sequential ascii codes from '0'
}

char to_char(int digit) {
    return digit + '0';
}

string big_add(string n1, string n2) {
    string result = "";

    // n2 must have more digits to simplify!
    if (n1.length() > n2.length())
        swap(n1, n2);

    // reverse numbers to simplify carrying numbers to the right
    reverse(n1.begin(), n1.end());
    reverse(n2.begin(), n2.end());

    // perform addition up to all n1 digits
    int carry = 0;
    int d = 0;
    for (int i = 0; i < n1.length(); i++) {
        int d1 = to_digit(n1[i]);
        int d2 = to_digit(n2[i]);
        int sum = d1 + d2 + carry;

        d = sum % 10;  // must convert back to digit
        carry = sum / 10;
        result.push_back(to_char(d));
    }

    // add remaining digits of n2 - carry may still be used
    for (int i = n1.length(); i < n2.length(); i++) {
        int d2 = to_digit(n2[i]);
        int sum = d2 + carry;
        d = sum % 10;
        carry = sum / 10;

        result.push_back(to_char(d));
    }

    // final possible carry
    if (carry == 1)
        result.push_back('1');

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    string n1, n2, result;
    cin >> n1 >> n2;

    cout << big_add(n1, n2);
}
