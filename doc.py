from fastapi import FastAPI
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Configuração da conexão com o banco de dados
conn = pyodbc.connect(
    'Driver={SQL Server};'
    "Server=DESKTOP-I5DV782;"
    "Database=Projeto AWS;"
)

# Modelo Pydantic para representar um aluno
class Aluno(BaseModel):
    nome: str
    idade: int
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    nome_professor: str
    numero_sala: int

# Criar aluno
@app.post("/alunos/")
def criar_aluno(aluno: Aluno):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Alunos (Nome, Idade, NotaPrimeiroSemestre, NotaSegundoSemestre, NomeProfessor, NumeroSala) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (aluno.nome, aluno.idade, aluno.nota_primeiro_semestre, aluno.nota_segundo_semestre, aluno.nome_professor, aluno.numero_sala))
    conn.commit()
    return {"mensagem": "Aluno criado com sucesso"}

# Listar alunos
@app.get("/alunos/")
def listar_alunos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = []
    for row in cursor:
        alunos.append({
            "ID": row.ID,
            "Nome": row.Nome,
            "Idade": row.Idade,
            "NotaPrimeiroSemestre": row.NotaPrimeiroSemestre,
            "NotaSegundoSemestre": row.NotaSegundoSemestre,
            "NomeProfessor": row.NomeProfessor,
            "NumeroSala": row.NumeroSala
        })
    return alunos

# Atualizar aluno
@app.put("/alunos/{aluno_id}/")
def atualizar_aluno(aluno_id: int, aluno: Aluno):
    cursor = conn.cursor()
    cursor.execute("UPDATE Alunos SET Nome=?, Idade=?, NotaPrimeiroSemestre=?, NotaSegundoSemestre=?, NomeProfessor=?, NumeroSala=? WHERE ID=?", 
                   (aluno.nome, aluno.idade, aluno.nota_primeiro_semestre, aluno.nota_segundo_semestre, aluno.nome_professor, aluno.numero_sala, aluno_id))
    conn.commit()
    return {"mensagem": f"Aluno ID {aluno_id} atualizado com sucesso"}

# Deletar aluno
@app.delete("/alunos/{aluno_id}/")
def deletar_aluno(aluno_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alunos WHERE ID=?", (aluno_id,))
    conn.commit()
    return {"mensagem": f"Aluno ID {aluno_id} deletado com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
