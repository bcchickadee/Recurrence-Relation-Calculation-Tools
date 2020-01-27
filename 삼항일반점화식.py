def a(FirstSequence,SecondSequence,FirstMultipliedConstant,SecondMultipliedConstant,IndependentConstant,SequenceNumber):
    #a(n+2)=(FirstMultipliedConstant)*a(n+1)+(SecondMultipliedConstant)*a(n)+(IndependentConstant)
    if int(SequenceNumber)==1:
        return FirstSequence
    elif int(SequenceNumber)==2:
        return SecondSequence
    else:
        return float(FirstMultipliedConstant)* a(float(FirstSequence),float(SecondSequence),float(FirstMultipliedConstant),float(SecondMultipliedConstant),float(IndependentConstant),int(SequenceNumber)-1) + float(SecondMultipliedConstant) * a(float(FirstSequence),float(SecondSequence),float(FirstMultipliedConstant),float(SecondMultipliedConstant),float(IndependentConstant),int(SequenceNumber)-2) +float(IndependentConstant)

print('삼항 점화식 계산기')
print('ver 1.0')
print('제작: bcchickadee, Jan 27 2020\n')
print('프로그램 설명:')
print('수열 a(n)에 대하여 a(n+2)=p×a(n+1)+qa(n)+r 가 성립할 때, 첫 번째 항(a(1)), 두 번째 항(a(2)), p, q, r, 타깃 항수를 입력하여 a(n)을 산출합니다.\n\n')
while 0==0:
    FirstSequence = input('첫 번째 항을 입력하십시오 - a(1).\n')
    SecondSequence = input('두 번째 항을 입력하십시오 - a(2).\n')
    FirstMultipliedConstant = input('a(n+2)=p×a(n+1)+qa(n)+r 에서 실수 p를 입력하십시오.\n')
    SecondMultipliedConstant = input('a(n+2)=p×a(n+1)+qa(n)+r 에서 실수 q를 입력하십시오.\n')
    IndependentConstant = input('a(n+2)=p×a(n+1)+qa(n)+r 에서 실수 r을 입력하십시오.\n')
    SequenceNumber = input('구하고자 하는 타깃 항수, 즉 a(n)의 n을 입력하십시오. 이때 n은 자연수여야 합니다.\n')
    print('제 '+SequenceNumber+' 번째 항은:')
    print(a(FirstSequence,SecondSequence,FirstMultipliedConstant,SecondMultipliedConstant,IndependentConstant,SequenceNumber))
    print('입니다.\n\n')
