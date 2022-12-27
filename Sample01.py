import random

MAX = 1000
MAX_STAGE = 10
print('1~{}の数を{}回以内で当ててください。'.format(MAX,MAX_STAGE))

stage = 1
answer= random.randint(1,MAX) #answerをrandom.randintで1~MAX(1000)から選ぶ。MAXと記入するのはMAXを変更するだけで済むから、ミスや作業量が減る。

#random.random()    : (0.0以上1.0未満の浮動小数点数)
#random.uniform()   : (任意の範囲の浮動小数点数)
#random.randrange() : (任意の範囲・ステップの整数)　例: random.randrange(1,100,3)⇒１～１００を３ステップずつ表示
#random.randint()   : (任意の範囲の整数)           

while stage <= MAX_STAGE:   #stage += 1 で増加していく。それを10回でストップさせる為。

    print(stage,'回目　いくつかな：', end='') #end=''でinputで記入した数値が改行されず横並びになる。
    n = int(input())

    if n < 1 or n > MAX:    #nが0以下、MAXより大きい時に再入力させるコード
        continue
    if n == answer:
        print('正解',stage,'回で当たりました')
        break               #break 必須
    elif n > answer:
        print('もっと小さな数です。')
    else:
        print('もっと大きな数です。')
    
    stage += 1

else:
    print('残念。正解は',answer,'でした。')