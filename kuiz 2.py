#Pendahuluan sambut pengguna
print(" Hai! Welcome to quiz game !!")

# memastikan pengguna bersedia menjawab
print('NOTE: Sila jawab dengan ejaan yang betul')
score = 0
question_no = 0
playing = input('Adakah anda bersedia untuk bermain? (ya/tidak) ? ').lower()

# soalan pertama
if playing == 'ya':
    question_no += 1
    ques = input(f'\n{question_no}. Apakah maksud CPU? ').lower()
    if ques == 'central processing unit':
        score +=1
        print('Betul! Anda dapat 1 markah')
        
    else:
        print('Salah!')
        print(f'Jawapannya ialah --> central processing unit')

# soalan kedua
    question_no += 1
    ques = input(f'\n{question_no}. Apakah maksud AI? ').lower()
    
    if ques == 'artificial intelligence':
        score +=1
        print('Betul! Anda dapat 1 markah')
        
    else:
        print('Salah!')
        print(f'Jawapannya ialah --> artificial intelligence')

# soalan ketiga
    question_no += 1
    ques = input(f'\n{question_no}. Apakah maksud RAM? ').lower()
    
    if ques == 'random access memory':
        score +=1
        print('Betul! Anda dapat 1 markah')
        
    else:
        print('Salah!')
        print(f'Jawapannya ialah --> random access memory')

# soalan keempat
    question_no += 1
    ques = input(f'\n{question_no}. Apakah maksud PSU? ').lower()
    
    if ques == 'power supply unit':
        score +=1
        print('Betul! Anda dapat 1 markah')
        
    else:
        print('Salah!')
        print(f'Jawapannya ialah --> power supply unit')


# soalan kelima
    question_no += 1
    ques = input(f'\n{question_no}. Apakah maksud ROM ? ').lower()
    
    if ques == 'read only memory':
        score +=1
        print('Betul! Anda dapat 1 markah')
        
    else:
        print('Salah!')
        print(f'Jawapannya ialah --> read only memory')


# komen keluar jika tidak bersedia menjawab

else:
    print('Terima kasih. Cuba lagi untuk menjawab')
    quit()

# paparan markah dan peratus yang pengguna dapat

print(f'\nJumlah soalan ialah {question_no}')
print(f'Markah anda ialah {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% bagi jawapan yang betul')

print(f'{percentage}% jawapan yang betul.')
