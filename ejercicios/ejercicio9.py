# Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente,
#para ello solo necesita establecer el precio de su trabajo por hora. Se estiman 40 horas de
#trabajo a la semana.

Pre_Hora = int(input('Escriba el precio de la hora '))

Sem = 40
Mes = 160

Cobro_S = Pre_Hora * Sem
Cobro_M = Pre_Hora * Mes

print ("Usted puede cobrar en una semana", Cobro_S, "$", "y puede cobrar al mes", Cobro_M, "$")