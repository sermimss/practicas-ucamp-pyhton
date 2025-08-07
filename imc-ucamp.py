#practica 1 ucamp fundamentos de python
#este es el codigo del IMC solicitado en la primer tarea 

#primero se da la bienvenida al programa.

print("Bienvenido a: \" LA CALCULADORA DE INDICE DE MASA CORPORAL. \" ")

#se da la opcion de continuar o terminar el programa segun la decicion del usuario
print("sigue las instrucciones o preciona enter para salir.\n")

#si el cliente continua con el programa se entra en el cuerpo del codigo
cliente = input("CUAL ES TU NOMBRE?\n")

#se comienza con la captura de datos
if cliente != "":   
    
    completo = 1

    while (completo == 1):
        try:
            print("cual es tu edad")
            print("(ej: 25)")
            E = int(input()) 
        except:
            print("\nel valor es incorrecto")
            print("intentemoslo nuevamente\n")
        else:
            try:
                #se pregunta su altura
                print("cual seria tu altura en mts.")
                print("(ej: 1.78)")
                A = float(input())
            except:
                print("\nel valor ingresado es invalido")
                print("introduzcamos los datos nuevamente\n")
            else:
                try:
                    #se pregunta el peso del usuario
                    print("cual seria tu peso en kg")
                    print("(ej:88.2)")
                    P = float(input())
                except:
                    print("\nel valor introducido no es correcto")
                    print("ingresemos los datos nuevamente\n")
                else:
                    print("los datos fueron capturados correctamente!!!")
                    completo = completo + 1

         
else:
    #si el ususario decide finalizar el programa desde el inicio 
    #se agradece el tiempo del usuario y se finaliza el programa 
    print("programa finalizado, gracias por su tiempo \nADIOS!")
    exit()

#se muestran todos los datos introducidos por el usuario de forma ordenada
print("\nmuy bien." )
print("tu nombre es: ", cliente , "\ntu edad : ", E, "a;os", "\ntu altura es de:", A, "mts", "\ncon un peso de:", P, "kg")
if E >= 18:
#se calcula y muestra su IMC
    indice = P/(A**2)
    indice1 = round(indice, 2)
    print("Tu IMC es de:" + str(indice1), "\nconciderado:\n")
#se agrega un feedback sobre el estado de su imc
    IMC = indice1
    if IMC >= 0 and IMC <= 15.99:
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99: 
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99:
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    
else:
    print("\nLO SIENTO: se deve ser mayor de edad para usar la calculadora de imc.")
    print("hasta luego.")