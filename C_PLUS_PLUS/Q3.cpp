// C++ Coding test 
// Question 3) ������� ��: �ڿ��� N�� �־����� �ڿ��� N�� ������� ���� ���İ� �Բ� ����ϴ� ���α׷��� �ۼ��ϼ���(������� N���� ������ ���)
// �Է¼���: ù �ٿ� �ڿ��� N�� �־���
// ��¼���: ù �ٿ� ���ϴ� ���İ� �Բ� ���� �����

#include <iostream>
using namespace std;

// 1) i+ ���·� �������� ������, 1�̰� +i ���·� ����Ѵ�.
int main()
{
	int n, i, sum = 0;

	cin >> n;

	for (i = 1; i <= n / 2; i++)
	{
		if (n % i == 0)
		{
			if (i == 1)
			{
				cout << i;
				sum += i;
			}
			else
			{
				cout << "+" << i;
				sum += i;
			}
		}
	}
	cout << "=" << sum;

	return 0;
}


// 1-2) 1�� for���� �ƿ� ���� ������� (�Ʊ� ������ ���ڸ� ���� ���� �ϴ°ɷ�)
int main()
{
	int n, i, sum = 1;

	cin >> n;
	cout << 1;

	for (i = 2; i <= n / 2; i++)
		if (n % i == 0)
		{
			cout << "+" << i;
			sum += i;
		}
	cout << "=" << sum;

	return 0;
}
