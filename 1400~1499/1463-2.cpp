/*
1로 만들기 (https://www.acmicpc.net/problem/1463)

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

	1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
	2. X가 2로 나누어 떨어지면, 2로 나눈다.
	3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

--입력--
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

--출력--
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
*/

// Bottom-up 방식 풀이
#include <iostream>

using namespace std;

int d[1000000];

int go(int n)
{
	d[1] = 0;
	
	for (int i = 2; i <= n; i++)
	{
		d[i] = d[i - 1] + 1;
		if (i % 2 == 0 && d[i] > d[i / 2] + 1) // d[n]에 담긴 최소 횟수와 비교 후 더 최소라면 Update
			d[i] = d[i / 2] + 1;
		if (i % 3 == 0 && d[i] > d[i / 3] + 1) // d[n]에 담긴 최소 횟수와 비교 후 더 최소라면 Update
			d[i] = d[i / 3] + 1;
	}
	return d[n];
}

int main()
{
	int input;

	cin >> input;

	cout << go(input);

	return 0;
}