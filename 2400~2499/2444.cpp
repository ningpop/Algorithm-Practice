/*
�� ��� - 7 (https://www.acmicpc.net/problem/2444)

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

	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < n - i; j++)
		{
			cout << " ";
		}
		for (int j = 0; j < 2 * i + 1; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
	
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			cout << " ";
		}
		for (int j = 1; j < 2 * (n - i); j++)
		{
			cout << "*";
		}
		cout << endl;
	}

	return 0;
}