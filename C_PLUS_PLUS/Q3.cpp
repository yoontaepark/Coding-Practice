// C++ Coding test 
// Question 3) 진약수의 합: 자연수 N이 주어지면 자연수 N의 진약수의 합을 수식과 함께 출력하는 프로그램을 작성하세요(진약수는 N빼고 나머지 약수)
// 입력설명: 첫 줄에 자연수 N이 주어짐
// 출력설명: 첫 줄에 더하는 수식과 함께 합을 출력함

#include <iostream>
using namespace std;

// 1) i+ 형태로 뽑을수가 없으니, 1뽑고 +i 형태로 출력한다.
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


// 1-2) 1을 for문에 아예 빼서 출력하자 (아까 마지막 숫자만 따로 빼서 하는걸로)
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
