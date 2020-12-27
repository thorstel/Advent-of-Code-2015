#include <bits/stdc++.h>

using namespace std;
#define sz(X) ((int)(X).size())

void incr(string& pw)
{
	for (int i = sz(pw) - 1; i >= 0; --i) {
		++pw[i];
		if (pw[i] > 'z') { pw[i] = 'a'; }
		else { break; }
	}
}

bool valid(string& pw)
{
	bool straight = false, overlap = false;
	int cnt_pairs = 0;
	for (int i = 0; i < sz(pw); ++i) {
		if (pw[i] == 'i' || pw[i] == 'o' || pw[i] == 'l') {
			return false;
		}
		if (i < sz(pw) - 2) {
			if ((pw[i] + 1 == pw[i + 1]) && (pw[i + 1] + 1 == pw[i + 2])) {
				straight = true;
			}
		}
		if (i < sz(pw) - 1) {
			if (!overlap && pw[i] == pw[i + 1]) {
				++cnt_pairs;
				overlap = true;
			}
			else {
				overlap = false;
			}
		}
	}
	return cnt_pairs >= 2 && straight;
}

int main()
{
	string pw = "vzbxkghb";
	do { incr(pw); } while (!valid(pw));
	cout << pw << endl;
	do { incr(pw); } while (!valid(pw));
	cout << pw << endl;
	return 0;
}
