from flask import Flask, request
import pyodbc
from fastapi import FastAPI


# Configuração da conexão com o banco de dados
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-I5DV782;"
    "Database=Projeto AWS;"
)

# Função para criar um novo aluno
def criar_aluno(nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Alunos (Nome, Idade, NotaPrimeiroSemestre, NotaSegundoSemestre, NomeProfessor, NumeroSala) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala))
    conn.commit()


# Função para ler todos os alunos
def ler_alunos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    for row in cursor:
        print(f"ID: {row.ID}, Nome: {row.Nome}, Idade: {row.Idade}, "
              f"Nota 1º Semestre: {row.NotaPrimeiroSemestre}, Nota 2º Semestre: {row.NotaSegundoSemestre}, "
              f"Professor: {row.NomeProfessor}, Sala: {row.NumeroSala}")

# Função para atualizar os dados de um aluno
def atualizar_aluno(id, nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala):
    cursor = conn.cursor()
    cursor.execute("UPDATE Alunos SET Nome=?, Idade=?, NotaPrimeiroSemestre=?, NotaSegundoSemestre=?, NomeProfessor=?, NumeroSala=? WHERE ID=?", 
                   (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala, id))
    conn.commit()

# Função para deletar um aluno
def deletar_aluno(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alunos WHERE ID=?", (id,))
    conn.commit()

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("Escolha uma ação:")
        print("1 - Criar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = input("Idade do aluno: ")
            nota_primeiro_semestre = float(input("Nota do primeiro semestre: "))
            nota_segundo_semestre = float(input("Nota do segundo semestre: "))
            nome_professor = input("Nome do professor: ")
            numero_sala = input("Número da sala: ")
            criar_aluno(nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala)
        elif opcao == "2":
            ler_alunos()
        elif opcao == "3":
            id = input("ID do aluno a ser atualizado: ")
            nome = input("Novo nome: ")
            idade = input("Nova idade: ")
            nota_primeiro_semestre = float(input("Nova nota do primeiro semestre: "))
            nota_segundo_semestre = float(input("Nova nota do segundo semestre: "))
            nome_professor = input("Novo nome do professor: ")
            numero_sala = input("Novo número da sala: ")
            atualizar_aluno(id, nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala)
        elif opcao == "4":
            id = input("ID do aluno a ser deletado: ")
            deletar_aluno(id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida")
