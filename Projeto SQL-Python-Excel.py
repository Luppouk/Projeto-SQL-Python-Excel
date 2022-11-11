import mysql.connector
from mysql.connector import Error
import pandas as pd

arquivo = pd.ExcelWriter('2FID-POOI-Leonardo_Torres-Luan_Groppo-Carlos_Eduardo.xlsx', engine = 'openpyxl')

try:
    db = mysql.connector.connect(host="localhost",
    database="univap",
    user="root",
    password="")

    if db.is_connected():
        db_Info = db.get_server_info()
        print("Conectado ao mysql versão", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Você está conectado: ", record)
except Error as e:
        print("Erro na conexão", e)

def planilha1(reg):
        dic = {'codigodisciplinanocurso': [], 'coddisciplina': [], 'codprofessor': [], 'curso': [], 'cargahoraria': [], 'anoletivo': []}
        values = [reg]
        cursor.execute("select * from disciplinasxprofessores inner join professores on codprofessor = registro and registro = %s and anoletivo = '2021';", values)
        result = cursor.fetchall()
        for x in result:
                dic['codigodisciplinanocurso'].append(x[0])
                dic['coddisciplina'].append(x[1])
                dic['codprofessor'].append(x[2])
                dic['curso'].append(x[3])
                dic['cargahoraria'].append(x[4])
                dic['anoletivo'].append(x[5])
        df = pd.DataFrame(dic)
        df['cargahorariatotal'] = df['cargahoraria'].sum()
        df.to_excel(arquivo, sheet_name = 'Planilha1', header = True, index = False) 

def planilha2():
        y = 1
        dic = {'codigodisciplinanocurso': [], 'codprofessor': [], 'curso': [], 'cargahoraria': [], 'anoletivo': [], 'quantidadeprofessoresnocurso':[]}
        cursor.execute("select codigodisciplinanocurso from disciplinasxprofessores;")
        result = cursor.fetchall()
        for y in range (0, len(result)-1):
                values = [y]
                cursor.execute("select codigodisciplinanocurso, codprofessor, curso, cargahoraria, anoletivo from disciplinasxprofessores inner join professores on codprofessor = registro and anoletivo = '2021' and curso = %s;", values)
                result = cursor.fetchall()
                qtyprof = 0
                exe = 0
                for x in result:
                        dic['codigodisciplinanocurso'].append(x[0])
                        dic['codprofessor'].append(x[1])
                        qtyprof+=1
                        dic['curso'].append(x[2])
                        dic['cargahoraria'].append(x[3])
                        dic['anoletivo'].append(x[4])
                        exe+=1
                for a in range (0, exe):
                        dic['quantidadeprofessoresnocurso'].append(qtyprof)
        df = pd.DataFrame(dic)
        df.to_excel(arquivo, sheet_name = 'Planilha2', header = True, index = False) 

def planilha3():
        y = 1
        dic = {'codigodisciplinanocurso': [], 'coddisciplina': [], 'curso': [], 'cargahoraria': [], 'anoletivo': [], 'cargahorariatotal':[]}
        cursor.execute("select codigodisciplinanocurso from disciplinasxprofessores;")
        result = cursor.fetchall()
        for y in range (0, len(result)-1):
                values = [y]
                cursor.execute("select codigodisciplinanocurso, coddisciplina, curso, cargahoraria, anoletivo from disciplinasxprofessores inner join disciplinas on coddisciplina = codigodisc and anoletivo = '2021' and curso = %s;", values)
                result = cursor.fetchall()
                cht = 0
                exe = 0
                for x in result:
                        dic['codigodisciplinanocurso'].append(x[0])
                        dic['coddisciplina'].append(x[1])
                        dic['curso'].append(x[2])
                        dic['cargahoraria'].append(x[3])
                        cht+=x[3]
                        dic['anoletivo'].append(x[4])
                        exe+=1
                for a in range (0, exe):
                        dic['cargahorariatotal'].append(cht)
        df = pd.DataFrame(dic)
        df.to_excel(arquivo, sheet_name = 'Planilha3', header = True, index = False) 
                
print('='*40)

planilha1(input('Digite o registro do professor que deseja buscar:'))
planilha2()
planilha3()
arquivo.save()