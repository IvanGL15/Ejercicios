name = input("What is your name?")
age = int(input("How old are you?"))
pending_live = "0"

#En python no es necesario usar corchetes en el condicional. Se usa dos puntos en el if y el else
if (age >= 100):
        print( "Hey " + name + ", you are a dinosaurio!!")
    
else:
        pending_live = str(100 - age)
        #Para hacer un salto de linea basta con utilizar 2 comandos de print
        print("Hi " + name + ", nice to meet you")
        print("You still have "+ pending_live + " years to enjoy your life")
    