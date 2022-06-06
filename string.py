num_of_tries=0
while num_of_tries !=3:
    username= input("please enter your username: ")
    password= input ('please enter your password: ')
    if username == 'ahmed' and password == '123':
        print('welcome to your page') 
    else:
        print('error')
        num_of_tries +=1
        print('you have' + str (3 - num_of_tries) + "left")
