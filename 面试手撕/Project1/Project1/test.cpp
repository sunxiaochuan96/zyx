#include <iostream>
#include <vector>

using namespace std;

long long jiecheng(int n) {
	vector<long long> dp(n + 1, 0);
	dp[0] = 0;
	dp[1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i] = dp[i - 1] * i;
	}
	return dp[n];
}

int trailingZeroes(int n) {
	long long num = jiecheng(n);
	return num;
}

//void main() {
//	long long res = trailingZeroes(13);
//	cout << res << endl;
//}