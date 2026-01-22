




print("""      -------      ¿Quieres saber si te da la nota para entrar?      ----------------------
      -------      Calcula tu nota real de acceso a la universidad   ----------------------
      -------      Según el sistema oficial de la EvAU               ----------------------
      -_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-

      """)

obj = float(input("   ·Nota a la que quieres llegar (sobre 14): "))
evau = float(input("   ·Nota EvAU fase general (0-10): "))
bat = float(input("   ·Nota media de Bachillerato (0-10): "))
ponderaciones = float(input("   ·Puntos por ponderaciones (0-4): "))
NotaFinal = (bat * 0.6) + (evau * 0.4) + ponderaciones

if NotaFinal < obj:
    if ponderaciones < 2:
        print("   Deberías mejorar las asignaturas específicas.")
    elif bat < 8:
        print("   Subir la media de Bachillerato es clave.")
    else:
        print("   La carrera está cara... necesitarás muy buenas específicas.")

else: print("   Bravissimo! ")

print(f"   Tu nota real de acceso es: {NotaFinal:.2f} / 14")

fin = input("   Pulsa ENTER para salir: ")

