class Livro:
  ListaLivros = []
  def __init__(self, titulo, genero, autor, StatusDisponibilidade, identificador):
    self.titulo = titulo
    self.genero = genero
    self.autor = autor
    self.StatusDisponibilidade = StatusDisponibilidade
    self.identificador = identificador
    Livro.ListaLivros.append(self)

Memorias = Livro("Memorias", "Classica", "Machado de Assis", "Disponível", "1")
Casmurro = Livro("Dom Casmurro", "Romance", "Machado de Assis", "Disponível", "2")
Iliada = Livro("Iliada", "Épico", "Homero", "Disponível", "3")

class User:
  def __init__(self, nome, senha, CPF):
    self.nome = nome
    self.senha = senha
    self.CPF = CPF

  def ConsultarLivro(Livro):
    print(Livro.titulo)
    print(Livro.genero)
    print(Livro.autor)
    print(Livro.StatusDisponibilidade)
    print(Livro.identificador)

  def PegarLivro(Livro):
    if Livro.StatusDisponibilidade == "Disponível":
      Livro.StatusDisponibilidade = "Emprestado"
    elif Livro.StatusDisponibilidade == "Reservado":
      validacao = str(input("Insira o número identificador do livro /n"))
      if validacao != str(Livro.identificador):
        print("Indentificador inválido")
      else:
        Livro.StatusDisponibilidade = "Emprestado"
    else:
      print("O livro escolhido não está disponível para empréstimo")

  def ReservarLivro(Livro):
    if Livro.StatusDisponibilidade == "Disponível":
      Livro.StatusDisponibilidade = "Reservado"
    else:
      print("Este livro já está reservado")

  def DevolverLivro(Livro):
    if Livro.StatusDisponibilidade == "Emprestado" or "Reservado":
      Livro.StatusDisponibilidade = "Disponível"
      print("Livro Devolvido")
    else:
      print("O livro não está em sua posse.")
#

def ListarLivros():
  for livro in Livro.ListaLivros:
    print(f"Título: {livro.titulo} | Autor: {livro.autor} | Status: {livro.StatusDisponibilidade} | Identificador: {livro.StatusDisponibilidade}")

Paciente0 = User("Robertinho", "12345678", "000.000.000-00")

print(Paciente0)
print(Paciente0.nome)
print(Paciente0.senha)
print(Paciente0.CPF)

User.ConsultarLivro(Memorias)
User.ReservarLivro(Memorias)

ListarLivros()