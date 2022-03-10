/*
 * Prime sieve and other prime-related algorithms such as factorization into primes.
 */
#include <bits/stdc++.h>
#define ll long long int
using namespace std;

// Sieve of Eratosthenes O(N*log(logN))
void prime_sieve(vector<int>& primes) {
    // 0 and 1 are not primes
    ll n = primes.size();
    primes[0] = primes[1] = 0;

    for (ll i = 2; i <= n; i++) {
        // all multiples of a prime number are not prime -> cross them out!
        // optimization: start from squared number (composite number)
        if (primes[i]) {
            for (ll k = i; k * i <= n; k++) {
                primes[k * i] = 0;
            }
        }
    }
}

// O(N)
vector<int> prime_factorization(int n) {
    vector<int> factors;
    int i = 2;

    while (i <= n) {
        if (n % i == 0) {
            factors.push_back(i);
            n /= i;
        } else {
            i++;
        }
    }

    return factors;
}

int total_primes(int l, int r) {
    vector<int> primes(r + 1, 1);
    vector<int> acc(r + 1, 0);
    prime_sieve(primes);

    for (int i = 0; i <= r; i++) {
        acc[i] = primes[i] ? acc[i - 1] + 1 : acc[i - 1];
    }

    return acc[r] - acc[l - 1];
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n;
    cin >> n;

    // primes sieve
    vector<int> primes(n + 1, 1);
    prime_sieve(primes);

    for (int i = 0; i <= n; i++)
        if (primes[i])
            cout << i << " ";
    cout << endl;

    // primes range
    cout << total_primes(2, 7) << endl;

    // primes factorization
    vector<int> factors;
    cin >> n;
    factors = prime_factorization(n);

    for (int i = 0; i < factors.size(); i++)
        cout << factors[i] << " ";

    return 0;
}
