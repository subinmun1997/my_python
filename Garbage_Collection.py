r=[1,2,3] # 리스트 객체에 r이라는 이름이 붙은 상황 Reference count=1
r='simple'#변수 r이 참조 대상을 문자열로 바꿈. 리스트는 Reference count=0 이므로 소멸 대상

r=[1,2,3] #리스트의 Reference count = 1
r2=r # Reference count=2
r = 'happy' #R.C=1
r2 = 'happy' #가비지 컬렉션 대상