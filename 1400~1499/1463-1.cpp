/*
1�� ����� (https://www.acmicpc.net/problem/1463)

���� X�� ����� �� �ִ� ������ ������ ���� �� ���� �̴�.

	1. X�� 3���� ������ ��������, 3���� ������.
	2. X�� 2�� ������ ��������, 2�� ������.
	3. 1�� ����.

���� N�� �־����� ��, ���� ���� ���� �� ���� ������ ����ؼ� 1�� ������� �Ѵ�.
������ ����ϴ� Ƚ���� �ּڰ��� ����Ͻÿ�.

--�Է�--
ù° �ٿ� 1���� ũ�ų� ����, 10^6���� �۰ų� ���� ���� N�� �־�����.

--���--
ù° �ٿ� ������ �ϴ� Ƚ���� �ּڰ��� ����Ѵ�.
*/

// Top-down ��� Ǯ��
#include <iostream>

using namespace std;

int d[1000000];

int go(int n)
{
	if (n == 1)
		return 0;
	if (d[n] > 0) // memoization
		return d[n];

	d[n] = go(n - 1) + 1;
	if (n % 3 == 0)
	{
		int temp = go(n / 3) + 1;
		if (d[n] > temp) // d[n]�� ��� �ּ� Ƚ���� �� �� �� �ּҶ�� Update
			d[n] = temp;
	}
	if (n % 2 == 0)
	{
		int temp = go(n / 2) + 1;
		if (d[n] > temp) // d[n]�� ��� �ּ� Ƚ���� �� �� �� �ּҶ�� Update
			d[n] = temp;
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