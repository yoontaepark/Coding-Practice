// C++ Coding test 
// Question 2) 자연수의 합:  자연수 A, B가 주어지면 A부터 B까지의 합을 수식과 함께 출력하시오
// 입력설명: 첫 줄에 자연수 A,B가 공백을 사이에 두고 차례대로 입력한다. (1<=A<B<=100)
// 출력설명: 첫 줄에 더하는 수식과 함께 합을 출력한다. (ex. 3 7 → 3+4+5+6+7 = 25)

#include <iostream>
using namespace std;

// 풀이1: 다 때려박고, 마지막 숫자만 for문 안에서 if문으로 구분
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

// 풀이2: 마지막 숫자전까지 i+ 로 for문 돌리고, 마지막 숫자만 for문 밖에서 따로 처리한다. (이걸로하자)
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

