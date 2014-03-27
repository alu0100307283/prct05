#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
import sys 

argumentos =sys.argv[1:]

print argumentos
for k in argumentos[k]:
  if (len(argumentos)==1):
    n=int(argumentos[k])
  
  else:			   #	2. O que el usuario, introduzca el intervalo por teclado.
    print "Introduzca el intervalo (n>0)"
    n=int(raw_input())
  if (n>=0):
    valor_pi= 3.1415926535897931159979634685441852
    sumatorio=0.0
    ini=0
    intervalo= 1.0 / float(n)
    print "**********************Calculo iterativo de PI***************************"
    print "************************************************************************"
    for i in range (n):
      x_i= ((i+1) - 1.0 / 2.0) /n     # así lo hacemos ahora
      #x_i=calcular_xi (n,i+1)     # así, si utilizáramos la función definida aal principio.
      fx_i= 4.0/(1.0+ x_i * x_i)
      print " " ,i+1,". Subintervalo:[", ini,"," ,ini+intervalo,"] x_",i+1,":" ,x_i,"f(x_",i+1,"):",fx_i
      ini += intervalo               #Incrementamos ini con el valor de intervalo.
      sumatorio += fx_i                  #Incrementamos el sumatorio con cada pasada por fx_i
    pi=sumatorio / n                    #calculamos la aproximación de π (notar que tiene que estar fuera del for¡¡)
    print "************************************************************************"
    print "El valor aproximado de PI es: %10.35f " % pi
    print "El valor de PI con 35 decimales es: %10.35f" % valor_pi  # el % le indica que tiene formato¡¡
    print "El error de aproximación es de: ", abs(valor_pi - pi)
    print "*********************************************************"
  else:
    print "El valor del numero de intervalos debe ser positivo."
    



