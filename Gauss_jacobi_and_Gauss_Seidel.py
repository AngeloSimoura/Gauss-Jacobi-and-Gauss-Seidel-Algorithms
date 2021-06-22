# -*- coding: utf-8 -*-
"""Atividade Avaliativa - Implementação de Gauss-Jacobi e Gauss-Seidel.ipynb
"""

def CriterioLinhas():
  ak=[]
  lista=[0,1,2]
  soma=0
  for k in lista:
    soma=0
    for j in lista:
      if j==k:
        soma+=0
      else:
        soma+=abs(A[k][j])
    ak.append(1/abs(A[k][k])*soma)
  if max(ak)<1:
    return CL
  else:
    return NCL

def CriterioSassenfeld():
  Beta=[]
  somaB1,soma1,soma2=0,0,0
  for j in range(1,n):
    somaB1+=abs(A[0][j])
  Beta.append(1/abs(A[0][0])*somaB1)
  for i in range(1,n):
    for j in range(0,i):
      soma1+=abs(A[i][j])*B[j]
    for j in range(i+1,n):
      soma2+=abs(A[i][j])
    Beta.append(1/abs(A[0][0])*(soma1+soma2))
    soma1,soma2=0,0    
  if max(Beta)<1:
    return CS
  else:
    return NCS

def Calculo():  
  x1=[]
  x2=[]
  x3=[]
  i,e=0,0
  dr=e+1
  x1.append(B[0]/A[0][0])
  x2.append(B[1]/A[1][1])
  x3.append(B[2]/A[2][2])
  opcao=input(print('Escolha 0 se deseja que o critério de parada seja a tolerância ou qualquer outro número inteiro para que seja o número de iterações: '))
  if opcao=='0':
    e=float(input(print('\nDigite a tolerância desejada: ')))
  else:
    IT=int(input(print('\nDigite o número desejado de iterações: ')))
  print('IT=',i)
  print('x1(',i,')= ', x1[i] ,'\nx2(',i,')= ',x2[i],'\nx3(',i,')= ',x3[i],'\n')
  if opcao=='0':
    while dr>e:
      print('IT=',i+1)
      x1.append(round(1/A[0][0]*(B[0]-A[0][1]*x2[i]-A[0][2]*x3[i]),4))
      x2.append(round(1/A[1][1]*(B[1]-A[1][0]*x1[i]-A[1][2]*x3[i]),4))
      x3.append(round(1/A[2][2]*(B[2]-A[2][0]*x1[i]-A[2][1]*x2[i]),4))
      print('x1(',i+1,')= ', x1[i+1] ,'\nx2(',i+1,')= ',x2[i+1],'\nx3(',i+1,')= ',x3[i+1])
      dr=round(max(abs(x1[i+1]-x1[i]),abs(x2[i+1]-x2[i]),abs(x3[i+1]-x3[i]))/max(abs(x1[i+1]),abs(x2[i+1]),abs(x3[i+1])),4)
      print('dr(',i+1,')= ',dr,'\n')
      i+=1
  else:
    while i<IT:
      print('IT=',i+1)
      x1.append(round(1/A[0][0]*(B[0]-A[0][1]*x2[i]-A[0][2]*x3[i]),4))
      x2.append(round(1/A[1][1]*(B[1]-A[1][0]*x1[i]-A[1][2]*x3[i]),4))
      x3.append(round(1/A[2][2]*(B[2]-A[2][0]*x1[i]-A[2][1]*x2[i]),4))
      print('x1(',i+1,')= ', x1[i+1] ,'\nx2(',i+1,')= ',x2[i+1],'\nx3(',i+1,')= ',x3[i+1])
      dr=round(max(abs(x1[i+1]-x1[i]),abs(x2[i+1]-x2[i]),abs(x3[i+1]-x3[i]))/max(abs(x1[i+1]),abs(x2[i+1]),abs(x3[i+1])),4)
      print('dr(',i+1,')= ',dr,'\n')
      i+=1

def MatrizOpcao():
  A=[]
  B=[]
  for i in range(n):
    A = A + [[0]*n]
  option =int(input('Digite 0 para usar a matriz de exemplo ou qualquer outro número inteiro para entrar com os valores da matriz:'))
  if option==0 :
    A=[
      [10 ,2  ,1],
      [1,5,1],
      [2,3  ,10]
      ]
    B=[
      7,
      -8,
      6
      ]
  else:
    for i in range(0,n):
      for j in range(0,n):
        print('Digite o valor da linha ', i, 'e coluna ', j, ':')
        A[i][j]=int(input())
      print(i)
      B.append(int(input(print('\nDigite o valor do termo independente para a linha ', i))))
  return A,B

n=3
CL="\nAtende ao Critério de Linhas\n"
NCl="\nNão atende ao Critério de Linhas\n"
CS="\nAtende ao Critério de Sassenfeld\n"
NCS="\nNão atende ao Critério de Sassenfeld\n"

A,B=MatrizOpcao()

print("\nMatriz A:")
for i in range(n):    
  print(A[i])

print("\nVetor dos Termos Independentes B:")
for i in range(n):    
  print(B[i])

option =int(input('\nDigite 0 para usar Gauss-Jacobi ou qualquer outro número inteiro para usar Gauss-Seidel:\n'))
if option==0:
  auxS=CriterioLinhas()
else:
  auxS=CriterioSassenfeld()

print(auxS)
if auxS==CL or auxS==CS:
  Calculo()

print('Fim do Algoritmo')
