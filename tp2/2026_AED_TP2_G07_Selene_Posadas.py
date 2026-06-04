def extraer_montos_adicionales(linea):
    cad1 = ""
    cad2 = ""
    cad3 = ""
    pos = 0
    for car in linea:
        if 2 <= pos <= 7:
            if car != " ":
                cad1 += car
        elif 8 <= pos <= 13:
            if car != " ":
                cad2 += car
        elif 14 <= pos <= 19:
            if car != " ":
                cad3 += car
        pos += 1
    return int(cad1), int(cad2), int(cad3)


def desarmar_paciente(linea):
    nombre_sucio = ""
    icd10_sucio = ""
    base_str = ""
    es_alta_complejidad = False
    pos = 0
    for car in linea:
        if 0 <= pos <= 24:
            nombre_sucio += car
        elif 25 <= pos <= 30:
            icd10_sucio += car
        elif 31 <= pos <= 38:
            if car != " ":
                base_str += car
        elif pos == 39:
            if car == "X":
                es_alta_complejidad = True
        pos += 1
    monto_base = int(base_str)
    icd10 = ""
    for car in icd10_sucio:
        if car != " ":
            icd10 += car
    nombre = ""
    espacios_acumulados = ""
    for car in nombre_sucio:
        if car == " ":
            espacios_acumulados += car
        else:
            nombre += espacios_acumulados + car
            espacios_acumulados = ""
    return nombre, icd10, monto_base, es_alta_complejidad


def obtener_porcentaje_enfermedad(icd10):
    porcentaje_str = ""
    encontro_punto = False
    for car in icd10:
        if encontro_punto:
            porcentaje_str += car
        if car == ".":
            encontro_punto = True
    return int(porcentaje_str)


def calcular_monto_final(letra, porcentaje, base, es_complejo, ad_al, ad_mz, ad_u):
    monto = base
    if "A" <= letra <= "L":
        monto += ad_al
    elif letra == "U":
        monto += ad_u
    elif "M" <= letra <= "Z":
        monto += ad_mz
    monto += (monto * porcentaje) / 100
    if es_complejo:
        monto += (monto * 5) / 100
    return monto


def procesar_linea_paciente(linea, ad_al, ad_mz, ad_u):
    nom, icd, base, complejo = desarmar_paciente(linea)
    letra = icd[0]
    porcentaje = obtener_porcentaje_enfermedad(icd)
    monto_final = calcular_monto_final(letra, porcentaje, base, complejo, ad_al, ad_mz, ad_u)
    return nom, letra, complejo, monto_final


def calcular_segunda_pasada(promedio_general):
    complejos_que_superan = 0
    ad_al = 0
    ad_mz = 0
    ad_u = 0
    archivo = open("tratamientos.txt", "r")
    for linea in archivo:
        if len(linea) > 2:
            if linea[0] == "#":
                ad_al, ad_mz, ad_u = extraer_montos_adicionales(linea)
            else:
                nom, letra, complejo, monto_final = procesar_linea_paciente(linea, ad_al, ad_mz, ad_u)
                if complejo and monto_final > promedio_general:
                    complejos_que_superan += 1
    archivo.close()
    return complejos_que_superan


def principal():
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    suma_cap19 = 0
    cont_cap19 = 0
    mayor_importe = 0
    paciente_mayor = ""
    es_primer_paciente_valido = True
    acumulador_dinero_global = 0
    total_complejos = 0
    ad_al = 0
    ad_mz = 0
    ad_u = 0

    archivo = open("tratamientos.txt", "r")
    for linea in archivo:
        if len(linea) > 2:
            if linea[0] == "#":
                ad_al, ad_mz, ad_u = extraer_montos_adicionales(linea)
            else:
                nom, letra, complejo, monto_final = procesar_linea_paciente(linea, ad_al, ad_mz, ad_u)
                
                r1 += 1
                acumulador_dinero_global += monto_final
                
                if letra == "A":
                    r2 += 1
                elif letra == "B":
                    r3 += 1
                elif letra == "C":
                    r4 += 1
                elif letra == "E":
                    r5 += 1
                elif letra == "P":
                    r6 += 1
                    
                if letra == "S" or letra == "T":
                    suma_cap19 += monto_final
                    cont_cap19 += 1
                    
                if letra != "U":
                    if es_primer_paciente_valido:
                        mayor_importe = monto_final
                        paciente_mayor = nom
                        es_primer_paciente_valido = False
                    elif monto_final > mayor_importe:
                        mayor_importe = monto_final
                        paciente_mayor = nom
                        
                if complejo:
                    total_complejos += 1
    archivo.close()
    
    promedio_general = acumulador_dinero_global / r1 if r1 > 0 else 0
    r7 = round(suma_cap19 / cont_cap19, 2) if cont_cap19 > 0 else 0
    r8 = paciente_mayor
    r9 = round(mayor_importe, 2) if mayor_importe > 0 else 0
    
    complejos_que_superan = calcular_segunda_pasada(promedio_general)
    
    r10 = 0
    if total_complejos > 0:
        r10 = int((complejos_que_superan * 100) // total_complejos)
        
    print('(r1) Cantidad de tratamientos cargados:', r1)
    print('(r2) Cantidad de tratamientos "A":', r2)
    print('(r3) Cantidad de tratamientos "B":', r3)
    print('(r4) Cantidad de tratamientos "C":', r4)
    print('(r5) Cantidad de tratamientos "E":', r5)
    print('(r6) Cantidad de tratamientos "P":', r6)
    print('(r7) Importe final promedio (capitulo 19):', r7)
    print('(r8) Paciente (no tipo "U") que pago el mayor importe final:', r8)
    print('(r9) Mayor importe pagado por ese paciente:', r9)
    print('(r10) Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)


principal()
