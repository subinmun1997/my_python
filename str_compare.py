print('A'<'Z') #알파벳 순서상 뒤로 갈수록 크다
print('AA'<'ZZ') #첫 번째 문자가 같다면 두 번째 문자를 비교한다
print('AA'<'AAA') #비교하는 문자들이 모두 같다면, 하나라도 긴 문자열이 크다
print('A'<'a') #소문자가 대문자보다 크다

print('가'<'나') #가나다순으로 뒤로 갈수록 크다
print('가'<'구') #아야어여오요우유으의 순으로 뒤로 갈수록 크다
print('가가'<'가나')
print('하하'<'하하하')