#include <iostream>
#include <vector>
#include <chrono>

using namespace std;


vector<int> find_primes_until(int n){
    vector<int> primes = {2, 3};
    for (int i = 5; i < n; i += 2)
    {
        for (int j = 0; j < primes.size(); j++)
        {
            if (i % primes[j] == 0)
            {
                break;
            }
            else if (j == primes.size() - 1)
            {
                primes.push_back(i);
                
            }
        }
    }
    return primes;
}

int main(){
    /*
    n = 100_000 -> 0.365629 seconds
    n = 1_000_000 -> 22.5729 seconds
    */
    int n = 1000000;
    chrono::system_clock::time_point start = chrono::system_clock::now();
    vector<int> primes = find_primes_until(n);
    chrono::system_clock::time_point end = chrono::system_clock::now();
    chrono::duration<double> elapsed_seconds = end - start;
    cout << "Elapsed time: " << elapsed_seconds.count() << "s\n";
    //for (int i = 0; i < primes.size(); i++) cout << primes[i] << endl;
    return 0;
}