# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end 를 공란으로 두겠다 = 다음라인 안넘어가게 막기(한줄로 표현)
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")  # lang을 가변적으로 조정할 수는 없고, 무조건 갯수를 맞춰줘야 하는 단점


# *변수명으로 선언하고 for문을 돌리면 갯수를 출력문에서 조정할 수 있다.  
def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end 를 공란으로 두겠다 = 한칸 띄면서 다음라인 안넘어가게 막기(한줄로 표현)
    for lang in language:
        print(lang, end = " ") 
    print()  # language를 다 출력하고 한줄 넘기기 위해서 공란 프린트문 하나 추가 

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile2("김태호", 25, "Kotlin", "Swift")  # lang을 가변적으로 조정할 수는 없고, 무조건 갯수를 맞춰줘야 하는 단점

