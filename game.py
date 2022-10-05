from tkinter import *
import random
import time

window = Tk()
window.title('tai si ja')
window.minsize(700,800)


game_finished = False
score=0
lives=4


status_str = StringVar()
status_str.set('ຄະແນນ :' + str(score)+ ' | ' + 'ຊີວິດ :' + '❤'*lives)
show_status=Label(window,textvariable=status_str,font=('Arial',20))
show_status.pack(pady=20)

word_dict={
    'sear':{'hints':['tub kawv','xeem thor']},
    'khamsy':{'hints':['tub kawv','xeem hawj']},
}
words = list(word_dict.keys())


def get_new_secret_word():
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word))
    return secret_word,clue
secret_word,clue=get_new_secret_word()



clue_str=StringVar()
clue_str.set(' | '.join(clue))
show_clue = Label(window,textvariable=clue_str,font=('Arial',30))
show_clue.pack(pady=30,padx=20)





hints=word_dict[secret_word]['hints']
hint_text=StringVar()
hint_text.set('ຄໍາໃບ້')
hints_str=StringVar()
hints_str.set('\n'.join(hints))

show_hints_text = Label(window,textvariable=hint_text,font=('Arial',15) )
show_hints_text.pack()

show_hints = Label(window,textvariable=hints_str,font=('Arial',15) )
show_hints.pack(pady=20)

textentry = Entry(window,width=5,borderwidth=1,font=('Arial',20),justify='center')
textentry.pack()


def update_clue(guess,secret_word,clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i]=guess
    clue_str.set(' | '.join(clue))
    win = ''.join(clue)==secret_word
    return win




def update_screen():
    global game_finished,score,lives,secret_word,clue,hints

    guess= textentry.get().strip()
    guess=guess.lower()

    if guess in secret_word:
        win = update_clue(guess,secret_word,clue)
        if win:
            print('yog lawm tu ntawv yog :'+secret_word)
            score=score+1
            print("score = "+str(score))
            clue_str.set('Yay! yog lawm :'+secret_word)
            window.update()
            time.sleep(2)

            if len(words)<1:
                game_finished=True
                clue_str.set('Congrats!')
            else:
                secret_word,clue=get_new_secret_word()
                clue_str.set(' | '.join(clue))
                hints=word_dict[secret_word]['hints']
                hints_str.set(' \n '.join(hints))

    else:
        print('tsis yog')
        lives = lives-1
        if lives < 1:
            clue_str('Game Over!')
            game_finished= True
    status_str.set('score :' +str(score) + ' | ' + 'lives :' + str(lives))
    textentry.delete(0,'end')

submit_btn = Button(window,text='OK',command=update_screen)
submit_btn.pack(pady=10)

def mian():
    if not game_finished:
        window.after(1000,mian)
    else:
        submit_btn['state']='disable'
        print('Quitting...')
        window.quit()


window.after(1000,mian)
window.mainloop()