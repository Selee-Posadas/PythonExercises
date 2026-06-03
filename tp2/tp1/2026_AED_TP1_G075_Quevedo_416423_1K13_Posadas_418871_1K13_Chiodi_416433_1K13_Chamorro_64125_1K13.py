beneficiario = input("Ingrese nombre completo: ")
codigo = input("Ingrese ICD10 X##.#: ")
monto_base = int(input("Ingrese un monto base: "))
letra = codigo[0]
bloque = int(codigo[1] + codigo[2])

if len(codigo) > 5:
    porcentaje = int(codigo[4:6])
else:
    porcentaje = int(codigo[4])


monto_final = monto_base + 25000

if "A" <= letra <= "L":
    monto_final += 25000
elif letra == "U":
    monto_final += 100000
elif "M" <= letra <= "Z":
    monto_final += 40000

monto_final += monto_final * porcentaje / 100

if letra == "A" or letra == "B":
    capitulo = "Ciertas enfermedades infecciosas y parasitarias"

elif letra == "C":
    capitulo = "Tumores[neoplasias]"
elif letra == "D":
    if bloque <= 48:
        capitulo = "Tumores[neoplasias]"
    else:
        capitulo = "Enfermedades de la sangre y de los organos hematopoyoticos y ciertos trastornos que afectan el mecanismo de la inmunidad"
elif letra == "E":
    capitulo = "Enfermedades endocrinas, nutricionales y metabolicas"
elif letra == "F":
    capitulo = "Trastornos mentales y del comportamiento"
elif letra == "G":
    capitulo = "Enfermedades del sistema nervioso"
elif letra == "H":
    if bloque <= 59:
        capitulo = "Enfermedades del ojo y sus anexos"
    else:
        capitulo = "Enfermedades del oido y de la apofisis mastoides"
elif letra == "I":
    capitulo = "Enfermedades del sistema circulatorio"
elif letra == "J":
    capitulo = "Enfermedades del sistema respiratorio"
elif letra == "K":
    capitulo = "Enfermedades del sistema digestivo"
elif letra == "L":
    capitulo = "Enfermedades de la piel y del tejido subcutaneo"
elif letra == "M":
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif letra == "N":
    capitulo = "Enfermedades del sistema genitourinario"
elif letra == "O":
    capitulo = "Embarazo, parto y puerperio"
elif letra == "P":
    capitulo = "Ciertas afecciones originadas en el periodo perinatal"
elif letra == "Q":
    capitulo = "Malformaciones congenitas, deformidades y anomalias cromosomicas"
elif letra == "R":
    capitulo = "Sintomas, signos y hallazgos anormales clinicos y de laboratorio, no clasificados en otra parte"
elif letra == "S" or letra == "T":
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif letra == "V" or letra == "W" or letra == "X" or letra == "Y":
    capitulo = "Causas externas de morbilidad y de mortalidad"
elif letra == "Z":
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra == "U":
    capitulo = "Codigos para propositos especiales"
else:
    capitulo = "Capitulo no valido"

if (letra == "A") or (letra == "B"):
    valor_testigo = ((monto_final * 30)/100)

    if valor_testigo > 10000 and valor_testigo <= 22000:
        monto_final -= valor_testigo
    elif valor_testigo > 22000 and valor_testigo <= 25000:
        monto_final -= ((monto_final * 22)/100)


print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)
