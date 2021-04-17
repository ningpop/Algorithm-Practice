#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer;
	int p = 0, y = 0;

	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == 80 || s[i] == 112)
			p++;
		if (s[i] == 89 || s[i] == 121)
			y++;
	}

	if (p == y)
		answer = true;
	else
		answer = false;

	return answer;
}