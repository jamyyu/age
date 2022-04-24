driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有': #and後面主詞要記得再寫一次
    print('請輸入有/沒有')
    raise SystemExit 

age = input('請問你的年齡？')
age = int(age)   #age 不加單引號
if driving == '有': 
    if age >= 18:
        print('你通過測驗了！')
    else:
        print('你還不能開車吧！')
elif driving == '沒有':
    if age >= 18:
        print('趕快去考駕照啦～')
    else:
        print('再耐心等個幾年囉～')



