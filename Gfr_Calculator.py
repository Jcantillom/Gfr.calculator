salir = 'y'

while salir =='y':
    print (80 * '*')
    print (30 * ' ', 'GFR CALCULATOR', 30 * ' ')
    print (80 * '*')
    print ('')
    print ('--------------- PROGRAMA PARA CALCULAR TAZA FILTRACION GLOMERULAR ---------------')
    print('')
    paciente = input('Nombre Del Paciente : ')
    Edad = int(input('Edad Del Paciente: '))
    print (f' {Edad} Años ')
    sexo = input('Indique Si es Femenino (F) o Masculino (M): ')
    Creatinina = float(input('Ingrese el Valor de la Creatinina (mg/dL), No mayor a 30 dias: '))
    print (f' {Creatinina} mg/dL')
    peso = float(input('Ingrese el Peso (Kg) Del Paciente : '))
    print(f'  {peso} Kg')

    if Edad <= 16:
        print(f'          Acudiente de Paciente Debe Firmar Consentimiento Informado       ')

#Formula  Femenina
    if Creatinina <= 0.7 and sexo == 'F' or Creatinina <= 0.7 and sexo == 'f':
        GFR = 144 * (Creatinina/0.7)**(-0.329) * (0.993 ** Edad)
    if Creatinina > 0.7 and sexo == 'F' or Creatinina > 0.7 and sexo == 'f':
        GFR = 144 * (Creatinina / 0.7) ** (-1.209) * (0.993 ** Edad)

#Formula Masculina
    if Creatinina <= 0.9 and sexo == 'M' or Creatinina <= 0.9 and sexo == 'm':
        GFR = 141 * (Creatinina / 0.9) ** (-0.411) * (0.993 ** Edad)
    if Creatinina > 0.9 and sexo == 'M' or Creatinina > 0.9 and sexo == 'm':
        GFR = 141 * (Creatinina / 0.9) ** (-1.209) * (0.993 ** Edad)

    print('                            ----------------------------')
    print (f'                                     GFR = {round(GFR, 1)}')
    print('                            ----------------------------')

    if GFR >= 60 :
        print(f'La Taza De Filtracion (Gfr) Del Paciente {paciente} Esta Dentro de Los Parametros Normales')
        print(f'                 PUEDE ADMINISTRAR MEDIO DE CONTRASTE               ')
    elif GFR <= 30:
        print (f' " ADVERTENCIA " Consulte Con el Dpto. De Nefrologia, paciente {paciente}, necesita "DIALISIS" ')
        print (f' NO ADMINISTE MEDIO DE CONTRASTE IV')
    else:
        print(f'                   Paciente {paciente}, Necesita " NefroProteccion "                 ')


    print(f' CALCULANDO EL VOLUMEN DE MEDIO DE CONTRASTE PERMITIDO PARA {paciente} ... ')

    print (f'  {peso} Kg')
    dosis = 2 * peso
    print (f'   La Dosis Maxima De Medio de Contraste para {paciente} es : {round(dosis, 1)} cc')

    salir = input(f' Desea Continuar y/n : ')
    if salir == 'n' or salir == 'N':
        salir=False
        break
    else:
        salir = 'y'
print('\n FIN \n')