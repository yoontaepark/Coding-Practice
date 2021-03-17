// C++ Coding test 
// Question 4) 나이차이: N(2<=N<=100)명의 나이가 입력됩니다. N명의 사람 중 가장 나이차이가 많이 나는 경우는 몇 살일까요? 
//					    최대 나이 차이를 출력하는 프로그램을 작성하세요
// 입력설명: 입력파일은 input.txt로 한다, 첫줄에 자연수 N이 입력되고, 그 다음 줄에 N개의 나이가 입력된다. 
//			(ex. 10 13 15 34 23 45 65 33 11 26 42)
// 출력설명: 출력파일은 output.txt로 한다. 첫 출에 최대 나이차이를 출력합니다. (54)

#include <iostream>
using namespace std;

int main()
{
	// 최대 최소 찾는 문제 나오면 max를 -최대, min을 +최대로 놓고 시작한다.
	// 약 2147000000 이 최대/최소를 쓸때 사용됨 
	// 텍스트 파일을 읽어오는 함수를 사용
	freopen("input.txt", "rt", stdin);
	int i, n, a, max = -2147000000, min = 2147000000;

	cin >> n;
	for (i = 1; i <= n; i++)
	{
		cin >> a;
		if (a > max)
			max = a;

		if (a < min)
			min = a;
	}
	cout << max - min << endl;

	return 0;
}