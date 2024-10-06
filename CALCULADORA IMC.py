def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc
def clasificar_imc(imc):
    if imc < 18.9: 
        return "Peso bajo"
    elif  18.9 >= imc < 24.99:
        return "Peso normal"
    elif 25 <= imc < 29.99:
        return "Sobrepeso"
    elif 30 <= imc < 34.99:
        return "Obesidad leve"
    elif 35 <= imc < 39.99:
        return "Obesidad media"
    else:
        return "Obesidad mórbida"
    #con esto solicité los datos de lo usuarios
personas = int(input( "personas: "))
#Dato para validar que el programa continue al siguiente paso
while personas > 0:
    #Aquí solicito el nombre completo del usuario y no utilicé n sino nombre para no confundirme, así lo hice en cada una de las abreviaturas
    nombre = input("Introduzca su nombre completo: ")
    #Aquí solicito la edad en años que es un número entero y por eso usé int y soliciitó sea mayor de edad para que la formúla aplique
    edad = int(input("ïndique su edad en años: "))
    if edad < 18: 
        print("es menor de edad el cálculo de IMC dará un valor erróneo")
    else: 
        peso = float(input("Introduce tu peso (Kg): "))
        estatura = float(input("Introduce tu estatura (m): "))

        imc = calcular_imc(peso, estatura)
        clasificacion = clasificar_imc(imc)
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Peso: {peso} Kg")
        print(f"Estatura: {estatura} m")
        print(f"IMC: {imc: .2f}")
        print(f"Clasificación: {clasificacion}")
    personas -= 1

    




