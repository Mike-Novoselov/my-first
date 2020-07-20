myname=input("введите логин: ")
mypass=input("введите пароль: ")
if(((myname=="Mike") and (mypass=="superhacker")) or ((myname=="Alexander") and (mypass=="mamkinhacker"))):
    print("привет " + myname + ". Добро пожаловать")
else:
    print("Ты хто такой, давай досвидания...")