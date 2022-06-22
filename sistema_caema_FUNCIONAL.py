import os
import mysql.connector
from mysql.connector import Error






opc = 3
opc2 = 3

def novo_nome():
     os.system("cls")
     acessar_banco()
     global concac
     consulta = "SELECT * FROM micros ORDER BY contador DESC"
     cursor = conexao.cursor()
     cursor.execute(consulta)
     linhas = cursor.fetchall()
     
     incremento = 0
     
     for linha in linhas:
            
       nome_temp1 = linha[2][:4]
       nome_temp2 = int(linha[2][4:]) # [COLUNA] [QNT DE LETRAS A SEREM EXIBIDAS]
       nome_temp2 = nome_temp2 + 1
       nome_temp2 = str(nome_temp2)
       concac = nome_temp1+nome_temp2
       incremento += 1
       print("---------------------------------")
       print("-     NOVO NOME: "+concac+"        -")
       print("---------------------------------\n\n")
       
       if incremento == 1: #CONDIÇÃO DE PARADA DO FOR (INCREMENTO = 0, CASO SEJA IGUAL A 1 = BREAK)
         #os.system("pause")
         break
def cadastro_micro():
    opc2 = 3
    while opc2 != 2:   
      opc2 = int(input("DESEJA CONTINUAR O CADASTRO?       [1] SIM     [2] NAO:\n\nR: "))
      if opc2 == 2:
         print("FECHANDO")
         break   
      if opc2 == 1:
          os.system("cls")
          
          print("-  CADASTRO DE MICROS   -")
          print("-------------------------\n\n")
          print("NOME: "+concac)
          bp = input("BP: ").upper()
          #nome = input("NOME: ")
          local = input("LOCAL: ").upper()
          setor = input("SETOR: ").upper()
          modelo = input("MODELO: ").upper()
          sistemaop = input("SISTEMA OPERACIONAL: ").upper()
          office = input("OFFICE: ").upper()
          licenca = str(input("LICENCA: ")).upper()
          observacao = input("OBSERVACAO: ").upper()

          dados = bp+", \'"+concac+"\', \'"+local+"\', \'"+setor+"\', \'"+modelo+"\', \'"+sistemaop+"\', \'"+office+"\', \'"+licenca+"\', \'"+observacao+"\')"
          declaracacao = """ INSERT INTO micros (bp, nome, local, setor, modelo, sistemaOperacional, office, licencaSistema, observacao) VALUES ("""

          sql = declaracacao + dados 

     
      try:

          acessar_banco()
          inserir = sql
          cursor = conexao.cursor()
          cursor.execute(inserir)
          conexao.commit()
          print("\nDADOS INSERIDOS COM SUCESSO!")
          cursor.close()
          os.system("pause")
          break

      except Error as erro:
       print("FALHA AO INSERIR DADOS NO SQL: {}" .format(erro))    
       break
def funcao_altera(opc_escolhida, cont, bp, nome):
          altera_nome = str(input("NOVO: ")).upper()
          altera_banco = "UPDATE `meusistema`.`micros` SET `"+opc_escolhida+"` = \'"+altera_nome+"\' WHERE (`contador` = \'"+cont+"\') and (`bp` = \'"+bp+"\') and (`nome` = \'"+nome+"\');" 
          try:

           acessar_banco()
           inserir = altera_banco
           cursor = conexao.cursor()
           cursor.execute(inserir)
           conexao.commit()
           print("DADOS ATUALIZADOS COM SUCESSO!")
           cursor.close()        

          except Error as erro:
            print("FALHA AO INSERIR DADOS NO SQL: {}" .format(erro))
            os.system("pause")
def exibir():
           
           consulta = "SELECT * FROM meusistema.micros WHERE `bp`=\'"+bp_name+"\' OR `nome` =\'"+bp_name+"\'"  #\' SIGNIFICA ASPAS DENTRO DE OUTRA ASPAS
           cursor = conexao.cursor()
           cursor.execute(consulta)
           linhas = cursor.fetchall()
           aux=0
           
           for linha in linhas:
             aux = aux+1
           if not linhas: #VERIFICANDO SE A VARIÁVEL ESTÁ VAZIA
             os.system("cls")
             print("NADA FOI ENCONTRADO\n.\n.\n.\n.")
             
           else:
            os.system("cls")
            print(aux," REGISTROS ENCONTRADOS\n")
            for linha in linhas:
              
              print("BP: ", linha[1])
              print("NOME: ", linha[2])
              print("LOCAL: ", linha[3])
              print("SETOR: ", linha[4])
              print("MODELO: ", linha[5])
              print("SISTEMA OPERACIONAL: ", linha[6])
              print("OFFICE: ", linha[7])
              print("LICENCA: ", linha[8])
              print("OBSERVACAO: ",linha[9])
              print("\n")
              global cont
              global bp
              global nome
              cont = str(linha[0])
              bp = linha[1]
              nome = linha[2]              
def mostrar_menu():  
         
         opc3 = 1
         while (opc3 != 0):
          
          opc3 = int(input("\n----------------------------------------\nESCOLHA UMA OPCAO:\n\n[1] BP\n[2] NOME\n[3] LOCAL\n[4] SETOR\n[5] MODELO\n[6] SISTEMA OPERACIONAL\n[7] OFFICE\n[8] LICENCA WINDOWS\n[9] OBSERVACAO\n\nR: "))
          if opc3 == 1:
           opc_escolhida = "bp"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 2:
           opc_escolhida = "nome"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break 
          if opc3 == 3:
           opc_escolhida = "local"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 4:
           opc_escolhida = "setor"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 5:
           opc_escolhida = "modelo"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 6:
           opc_escolhida = "sistemaOperacional"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break 
          if opc3 == 7:
           opc_escolhida = "office"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 8:
           opc_escolhida = "licencaSistema"
           funcao_altera(opc_escolhida, cont, bp, nome)
           break
          if opc3 == 9:
           opc_escolhida = "observacao"
           funcao_altera(opc_escolhida, cont, bp, nome)     
           break
def acessar_banco():
    global conexao
    conexao = mysql.connector.connect(host='meusistema.cxemn8yg51zh.us-east-1.rds.amazonaws.com',database='meusistema',user='root',password='caema#2022')
def apagar_linha():
     acessar_banco()

     consulta = "SELECT * FROM meusistema.micros WHERE `bp`=\'"+bp_name+"\' OR `nome` =\'"+bp_name+"\'"  #\' SIGNIFICA ASPAS DENTRO DE OUTRA ASPAS

     cursor = conexao.cursor()
     cursor.execute(consulta)
     linhas = cursor.fetchall()
     
     for linha in linhas:
       converter = str(linha[0])     
       bp_temp = str(linha[1])
       name_temp = str(linha[2])
     
     apagar = "DELETE FROM `meusistema`.`micros` WHERE (`contador` = \'"+converter+"\') and (`bp` = \'"+bp_temp+"\') and (`nome` = \'"+name_temp+"\');"
     
     cursor = conexao.cursor()
     cursor.execute(apagar)
     conexao.commit()
    
     print("DADOS APAGADOS!")
def apagar_apagar():
    opcoes = int(input("DESEJA APAGAR? [1] SIM  [2] NAO\n\nR: "))
    if opcoes == 1:              
              apagar_linha()
              
    else:
            print("\nFECHANDO SESSÃO")
def teste():
           consulta = "SELECT * FROM meusistema.micros;"  #\' SIGNIFICA ASPAS DENTRO DE OUTRA ASPAS
           cursor = conexao.cursor()
           cursor.execute(consulta)
           linhas = cursor.fetchall()
           
           for linha in linhas:
            global cont
            global bp
            global nome
            cont = str(linha[0])
            bp = linha[1]
            nome = linha[2]        
def verifica():
        global linhas
        global bp_name
        os.system("cls")
        bp_name = input("DIGITE O NOME OU NUMERO DO BP: ")       
        consulta = "SELECT * FROM meusistema.micros WHERE `bp`=\'"+bp_name+"\' OR `nome` =\'"+bp_name+"\'"  #\' SIGNIFICA ASPAS DENTRO DE OUTRA ASPAS
        cursor = conexao.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
def sem_dados():
  os.system("cls")
  print("NENHUM DADO ENCONTRADO!!\n.\n.\n.\n.")   
  os.system("pause")

print("CADASTRO DE MAQUINAS:\n_______________________\n\n")
while (opc != 0 ): 

 os.system("cls")
 acessar_banco()
 
 opc = int(input("[1] CADASTRAR  |  [2] CONSULTAR  |  [3]  EDITAR INFORMACOES  |  [4] APAGAR CADASTRO  |  [0] SAIR\n\nR: "))
 
 if opc == 1:
     novo_nome()     
     cadastro_micro()
 if opc == 2:
        verifica()       
        exibir()
        os.system("pause")
 if opc == 3:
        verifica()
        if not linhas: #VERIFICANDO SE A VARIÁVEL ESTÁ VAZIA
          sem_dados()            
        else:
          exibir()
          mostrar_menu()
          os.system("pause")   
 if opc == 4:
        os.system("cls")
        verifica()
        if not linhas:
             sem_dados()       
        else:
         exibir()
         apagar_apagar()
         os.system("pause")
 
  