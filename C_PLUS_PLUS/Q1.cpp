// C++ Coding test 
// Question 1) 1부터 N까지 M의 배수합: 
// 자연수 N이 입력되면 1부터 N까지의 수 중 M의 배수합을 출력하는 프로그램을 작성하세요 
// 입력설명: 첫줄에 자연수 N과 M이 차례로 입력됩니다(3<=M<N<=1000)
// 출력설명: 첫 줄에 M의 배수합을 출력한다. (ex. 15 3 → 3+6+9+12+15 = 45)

#include <iostream>
using namespace std;

int main()
{
	int n, m, sum = 0;
	
	// 자연수 n과 m을 차례로 입력한다
	cin >> n >> m;


	// m의 배수를 뽑아서 미리 정해둔 변수에 더한다
	for (int i = 1; i <= n; i++)
	{
		if (i % m == 0)
			sum += i;
	}

	// 더한 값을 출력한다 
	cout << sum;

	return 0;
}