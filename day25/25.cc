#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using ll = long long;
using namespace std;

void solve(istream& ins)
{
	assert(ins.good());
	string line; getline(ins, line);
	smatch m;
	if (!regex_search(line, m, regex {R"(row (\d+), column (\d+).)"})) { assert(false); }
	ll row = stoll(m[1]), col = stoll(m[2]);

	ll val = 20151125;
	ll diag = 1;
	for (;;) {
		for (ll c = 1; c < diag; ++c) {
			ll r = diag - c;
			if (r == row && c == col) {
				cout << val << endl;
				return;
			}
			val = (val * 252533) % 33554393;
		}
		++diag;
	}
}

////////////////////////////////////////////////////////////////////////
//                            SETUP STUFF                             //
////////////////////////////////////////////////////////////////////////

static const string actual_input =
R"""(To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083.)""";

int main(int argc, const char *argv[])
{
	if (argc > 1) {
		ifstream ifs {argv[1]};
		solve(ifs);
	} else {
		auto iss = istringstream {actual_input};
		solve(iss);
	}
	return 0;
}
