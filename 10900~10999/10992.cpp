/*
별 찍기 - 17 (https://www.acmicpc.net/problem/10992)

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

--입력--
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

--출력--
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*/

#include <iostream>

using namespace std;

int main()
{
	int n;

	cin >> n;

	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n - i; j++)
			cout << " ";
		cout << "*";

		if (i != 1)
		{
			for (int j = 0; j < 2 * i - 3; j++)
				cout << " ";

			cout << "*";
		}

		cout << endl;
	}

	for (int i = 0; i < 2 * n - 1; i++)
		cout << "*";

	return 0;
}