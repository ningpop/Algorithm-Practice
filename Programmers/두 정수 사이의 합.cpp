#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    
    if (a > b)
		while (true)
		{
			answer += b;
			b++;
			if (a == b)
			{
				answer += b;
				break;
			}
		}
	else if (a < b)
	{
		while (true)
		{
			answer += a;
			a++;
			if (a == b)
			{
				answer += a;
				break;
			}
		}
	}
	else
		answer = a;
    
    return answer;
}