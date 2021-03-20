// C++ Coding test 
// Question 8) 올바른 괄호: 괄호가 입력되면 올바른 괄호이면 "YES", 올바르지 않으면 "NO' 를 출력합니다. 
// (())() 이것은 괄호의 창이 올바르게 위치하는 것이지만, (()()))은 올바른 괄호가 아니다. 
// 입력설명: 첫번째 줄에 괄호 문자열이 입력됨. 문자열의 최대 길이는 30
// 출력설명: 첫 번째 줄에 YES, NO를 출력한다 
// (이후 Stack 배우면 다시 stack으로 풀 예정)

// 입력예제: (()(()))(()
// 출력예제: NO

#include <stdio.h>
using namespace std;

// 양쪽 괄호수가 같아야 한다, 가면서 ) 갯수가 (보다 많으면 안된다. 
// cnt 개수가 0인 걸 찾으면서, -1이 되면 break 시키기 
int main()
{
	//freopen("input.txt", "rt", stdin);
	char a[100];
	int i, cnt = 0;
	scanf("%s", &a);


	for (i = 0; a[i] != '\0'; i++)
	{
		if (a[i] == '(')
			cnt++;
		else if (a[i] == ')')
			cnt--;

		// cnt가 -1이 되는 순간 = ( ')' ) 개수가 많아지는 순간 break)
		if (cnt < 0)
			break;
	}

	if (cnt == 0)
		printf("YES\n");

	//0이 아니거나, 음수로 break한 경우도 포함 
	else
		printf("NO\n");


	return 0;
}