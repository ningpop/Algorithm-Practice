/*
�� ��� - 9 (https://www.acmicpc.net/problem/2446)

������ ���� ��Ģ�� ������ �ڿ� ���� ��� ������.

--�Է�--
ù° �ٿ� N(1 �� N �� 100)�� �־�����.

--���--
ù° �ٺ��� 2��N-1��° �ٱ��� ���ʴ�� ���� ����Ѵ�.
*/

#include <iostream>

using namespace std;

int main()
{
	int n;

	cin >> n;

	for (int i = n; i > 0; i--)
	{
		for (int j = 0; j < n - i; j++)
			cout << " ";

		for (int j = 2 * i - 1; j > 0; j--)
			cout << "*";

		cout << endl;
	}
	
	for (int i = 1; i < n; i++)
	{
		for (int j = 1; j < n - i; j++)
			cout << " ";

		for (int j = 0; j < 2 * i + 1; j++)
			cout << "*";

		cout << endl;
	}

	return 0;
}