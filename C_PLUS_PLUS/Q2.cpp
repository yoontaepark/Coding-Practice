// C++ Coding test 
// Question 2) �ڿ����� ��:  �ڿ��� A, B�� �־����� A���� B������ ���� ���İ� �Բ� ����Ͻÿ�
// �Է¼���: ù �ٿ� �ڿ��� A,B�� ������ ���̿� �ΰ� ���ʴ�� �Է��Ѵ�. (1<=A<B<=100)
// ��¼���: ù �ٿ� ���ϴ� ���İ� �Բ� ���� ����Ѵ�. (ex. 3 7 �� 3+4+5+6+7 = 25)

#include <iostream>
using namespace std;

// Ǯ��1: �� �����ڰ�, ������ ���ڸ� for�� �ȿ��� if������ ����
int main()
{
	int a, b, sum = 0;

	cin >> a >> b;

	for (int i = a; i <= b; i++)
	{
		if (i == b)
		{
			sum += i;
			cout << i << "=" << sum << endl;
		}
		else
		{
			sum += i;
			cout << i << "+";
		}
	}
	return 0;
}

// Ǯ��2: ������ ���������� i+ �� for�� ������, ������ ���ڸ� for�� �ۿ��� ���� ó���Ѵ�. (�̰ɷ�����)
int main()
{
	int a, b, i, sum = 0;

	cin >> a >> b;

	for (i = a; i < b; i++)
	{
		sum += i;
		cout << i << "+";
	}
	cout << i << "=";
	cout << sum + i;

	return 0;
}

