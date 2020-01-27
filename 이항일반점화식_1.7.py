def a(FirstSequence,MultipliedConstant,IndependentConstant,SequenceNumber): #a(n+1)=(MultipliedConstant)*a(n)+(IndependentConstant)
    if int(SequenceNumber)==1:
        return FirstSequence
    else:
        return float(MultipliedConstant)* a(float(FirstSequence),float(MultipliedConstant),float(IndependentConstant),int(SequenceNumber)-1) +float(IndependentConstant)

print('이항 점화식 계산기')
print('ver 1.7')
print('제작: bcchickadee, Jan 26 2020\n')
print('프로그램 설명:')
print('수열 a(n)에 대하여 a(n+1)=p×a(n)+q가 성립할 때, 초항, p, q, 타깃 항수를 입력하여 a(n)을 산출합니다.\n\n')
while 0==0:
    FirstSequence = input('첫번째 항을 입력하십시오 - a(1).\n')
    MultipliedConstant = input('a(n+1)=p×a(n)+q에서 실수 p를 입력하십시오.\n')
    IndependentConstant = input('a(n+1)=p×a(n)+q에서 실수 q를 입력하십시오.\n')
    SequenceNumber = input('구하고자 하는 타깃 항수, 즉 a(n)의 n을 입력하십시오 이때 n은 자연수여야 합니다.\n')
    print('제 '+SequenceNumber+' 번째 항은:')
    print(a(FirstSequence,MultipliedConstant,IndependentConstant,SequenceNumber))
    print('입니다.\n\n')
