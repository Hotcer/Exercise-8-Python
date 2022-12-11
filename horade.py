import time

def es_hora_de_ir_a_casa():
  # Obtenemos la hora actual del sistema
  hora_actual = time.localtime()

  # Si la hora actual es después de las 7 PM, es hora de ir a casa
  if hora_actual.tm_hour >= 19:
    print("¡Es hora de ir a casa!")
  else:
    # Calculamos el tiempo que queda hasta las 7 PM
    tiempo_restante = (19 - hora_actual.tm_hour) * 60 + (0 - hora_actual.tm_min)
    print(f"Faltan {tiempo_restante} minutos para ir a casa.")

# Ejecutamos la función
es_hora_de_ir_a_casa()
