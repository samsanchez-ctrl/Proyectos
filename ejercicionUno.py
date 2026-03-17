# Simulacion de aprobador de contraseñas seguras
def validar_password(password):
    # 1. Validacion de longitud
    if len(password) < 8:
        return "Insegura: Debe tener al menos 8 caracteres"
    
    # 2. Inicializar "Banderas" de control
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    caracteres_especiales = "!@#$%&*(),.?:|<>"

    # 3. Recorrer la cadena caracter por caracter
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True

    # 4. Verificar si se cumplieron todos los requisitos
    if tiene_mayuscula and tiene_numero and tiene_especial and tiene_minuscula:
        return " ¡Segura! Tu contraseña cumple con todos los requisitos. "
    else:
        # Construyo un mensaje indicando que falta
        mensaje_error = []
        if not tiene_mayuscula: mensaje_error.append("una mayuscula")
        if not tiene_minuscula: mensaje_error.append("una minuscula")
        if not tiene_numero: mensaje_error.append("un numero")
        if not tiene_especial: mensaje_error.append("un caracter especial")

        return f"Insegura: Falta {', ' .join(mensaje_error)}."
    

# --- Bloque de ejecucion ---
mi_pass = input(" Introduce una contraseña para probar: ")
resultado = validar_password(mi_pass)
print(resultado)