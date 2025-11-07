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
      validacao = str(input("Insira o número identificador do livro \n"))
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

def ListarLivros():
  """Lista todos os livros no acervo com seus detalhes."""
  print("\n--- ACERVO COMPLETO ---")
  if not Livro.ListaLivros:
      print("O acervo está vazio.")
      return
      
  for livro in Livro.ListaLivros:
    print(f"Título: {livro.titulo} | Autor: {livro.autor} | Status: {livro.StatusDisponibilidade} | Identificador: {livro.identificador}")
  print("-----------------------")

def menu_principal():
    """Exibe o menu principal e solicita a escolha do usuário."""
    print("\n" + "="*40)
    print("📚 SISTEMA DE BIBLIOTECA DIGITAL 📚")
    print("="*40)
    print("Selecione uma opção:")
    print("  1 - Cadastro de Usuário (Pedro Almeida)")
    print("  2 - Listar Usuários (Sophia)")
    print("  3 - Cadastro de Livro (Pedro Rodrigo)")
    print("  4 - Listar Livros (Pedro Rodrigo)")
    print("  5 - Visualizar Status de Livro (Emilly)")
    print("  6 - Realizar Empréstimo (Pedro Almeida)")
    print("  7 - Contagem de Livros por Status (Sophia)")
    print("  8 - Devolver Livro") 
    print("  0 - Sair do Sistema")
    print("="*40)
    
    escolha = input("Digite o número da opção desejada: ")
    return escolha

def rodar_sistema():
    """Loop principal do sistema que exibe o menu e processa as escolhas."""
    while True:
        opcao = menu_principal() 

        if opcao == '1':
            print("\n--- Opção 1: Cadastro de Usuário (A FAZER) ---") 
            input("Pressione Enter para continuar...") 

        elif opcao == '2':
            print("\n--- Opção 2: Listagem de Usuários (A FAZER) ---")
            input("Pressione Enter para continuar...") 
        
        elif opcao == '3':
            print("\n--- Opção 3: Cadastro de Livro (A FAZER) ---")
            input("Pressione Enter para continuar...") 

        elif opcao == '4':
            print("\n--- Opção 4: Listagem de Livros ---")
            ListarLivros() 
            input("Pressione Enter para continuar...")
        
        elif opcao == '5':
            print("\n--- Opção 5: Visualizar Status do Livro (A FAZER) ---")
            input("Pressione Enter para continuar...")
            
        elif opcao == '6':
            print("\n--- Opção 6: Realizar Empréstimo (A FAZER) ---")
            input("Pressione Enter para continuar...")

        elif opcao == '7':
            print("\n--- Opção 7: Contagem de Livros por Status (A FAZER) ---")
            input("Pressione Enter para continuar...")
        
        elif opcao == '8':
            print("\n--- Opção 8: Devolver Livro ---")
            print("Tentando devolver o livro Memorias...")
            User.DevolverLivro(Memorias)
            input("Pressione Enter para continuar...")

        elif opcao == '0':
            print("\n👋 Saindo do Sistema. Obrigado por usar a Biblioteca Digital!")
            break  
            
        else:
            print("\n⚠️ Opção inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    rodar_sistema()

Paciente0 = User("Robertinho", "12345678", "000.000.000-00")