// C++ Coding test 
// Question 7) 영어단어 복구: 에러로 표시되는 영어단어를 원래의 표현대로 공백을 제거하고 소문자화 시켜 출력하는 프로그램을 작성
// 입력설명: 첫줄에 바이러스가 걸린 단어가 주어짐. 길이는(공백포함) 100을 넘지 않는다. 문자사이의 공백은 연속적으로 존재가능. 입력은 알파벳과 공백만 존재
// 출력설명: 첫 줄에 소문자로 된 정상적인 영어단어를 출력한다. 

// 입력예제: bE    AU T l fu     L
// 출력예제: beautiful


#include <stdio.h>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);

	//입력할 배열과, 이후 옮길 배열을 모두 정의한다
	char a[101], b[101];
	int i, j = 0;

	//get은 이제 못쓰니까 fgets를 쓰도록 하자
	fgets(a, sizeof a, stdin);

	//루프돌리면서 소문자면 새배열에 그대로, 대문자면 32더해서 새배열에 넣기, 아니면 아무것도 하지말기
	for (i = 0; a[i] != '\0'; i++)
	{
		if (a[i] >= 97 && a[i] <= 122)
			b[j++] = a[i];
		else if (a[i] >= 65 && a[i] <= 90)
			b[j++] = a[i] + 32;
	}

	// 매우중요, 배열의 마지막에 항상 '\0'(NULL)을 넣어줘야 함. 그래야 에러가 안남
	b[j] = '\0';

	printf("%s", b);

	return 0;
}

