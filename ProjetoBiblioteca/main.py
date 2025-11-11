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
  ListaUsuarios = []  # Lista compartilhada com todos os usuários

  def __init__(self, nome, senha, CPF):
    self.nome = nome
    self.senha = senha
    self.CPF = CPF
    User.ListaUsuarios.append(self)

  @classmethod
  def validar_usuario(cls, nome, senha, CPF):
    """Valida o acesso de um usuário específico."""
    for usuario in cls.ListaUsuarios:
      if usuario.nome == nome and usuario.senha == senha and usuario.CPF == CPF:
          print(f"\n✅ Acesso permitido! Bem-vindo(a), {usuario.nome}.")
          return usuario
    print("\n❌ Acesso negado. Dados incorretos.")
    return None

  def ConsultarLivro(self, Livro):
    print(Livro.titulo)
    print(Livro.genero)
    print(Livro.autor)
    print(Livro.StatusDisponibilidade)
    print(Livro.identificador)

  def PegarLivro(self, Livro):
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

  def ReservarLivro(self, Livro):
    if Livro.StatusDisponibilidade == "Disponível":
      Livro.StatusDisponibilidade = "Reservado"
    else:
      print("Este livro já está reservado")

  def DevolverLivro(self, Livro):
    if Livro.StatusDisponibilidade == "Emprestado" or "Reservado":
      Livro.StatusDisponibilidade = "Disponível"
      print("Livro Devolvido")
    else:
      print("O livro não está em sua posse.")

def autenticar_usuario():
    """Solicita os dados do usuário e valida o login."""
    print("\n--- LOGIN DE USUÁRIO ---")
    nome = input("Nome: ").strip()
    senha = input("Senha: ").strip()
    CPF = input("CPF: ").strip()

    usuario_logado = User.validar_usuario(nome, senha, CPF)
    return usuario_logado


def ListarLivros():
  """Lista todos os livros no acervo com seus detalhes."""
  print("\n--- ACERVO COMPLETO ---")
  if not Livro.ListaLivros:
      print("O acervo está vazio.")
      return
      
  for livro in Livro.ListaLivros:
    print(f"Título: {livro.titulo} | Autor: {livro.autor} | Status: {livro.StatusDisponibilidade} | Identificador: {livro.identificador}")
  print("-----------------------")

def ListarUsuarios():
  """Lista todos os usuários cadastrados no sistema."""
  print("\n--- LISTA DE USUÁRIOS CADASTRADOS ---")
  
  if not User.ListaUsuarios:
      print("Nenhum usuário cadastrado.")
  else:
      for i, usuario in enumerate(User.ListaUsuarios): 
          print(f"Usuário {i+1}: Nome: {usuario.nome} | CPF: {usuario.CPF}")       
  print("--------------------------------------")

def CadastrarLivro():
    """Permite cadastrar um novo livro pelo terminal."""
    print("\n--- Cadastro de Novo Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Gênero: ").strip()

    status_inicial = "Disponível"
    
    # 2. Gerar um Identificador Único (baseado no total de livros + 1)
    # Convertemos para string, pois seus IDs existentes ("1", "2", "3") são strings.
    novo_identificador = str(len(Livro.ListaLivros) + 1) 

    # 3. Passar TODOS os 5 argumentos para o construtor da classe Livro
    novo = Livro(titulo, genero, autor, status_inicial, novo_identificador) 
    
    print(f"✅ Livro '{novo.titulo}' cadastrado com sucesso! ID: {novo.identificador}")

def RealizarEmprestimo(usuario):
    """Permite realizar o empréstimo de um livro pelo identificador."""
    print("\n--- Realizar Empréstimo ---")
    ListarLivros()

    ident = input("Digite o identificador do livro que deseja emprestar: ").strip()
    livro_encontrado = None

    for livro in Livro.ListaLivros:
        if livro.identificador == ident:
            livro_encontrado = livro
            break

    if livro_encontrado:
        usuario.PegarLivro(livro_encontrado)
    else:
        print("❌ Nenhum livro encontrado com esse identificador.")

def ContarLivrosPorStatus():
  """Conta e exibe quantos livros existem para cada status."""
  print("\n--- CONTAGEM DE LIVROS POR STATUS ---")
  
  contagem = {
      "Disponível": 0,
      "Emprestado": 0,
      "Reservado": 0
  }
  status_outros = []
  if not Livro.ListaLivros:
      print("O acervo está vazio.")
      return
  for livro in Livro.ListaLivros:
      status = livro.StatusDisponibilidade
      if status in contagem:
          contagem[status] += 1
      else:
          status_outros.append(status)

  print(f"Livros Disponíveis: {contagem['Disponível']}")
  print(f"Livros Emprestados: {contagem['Emprestado']}")
  print(f"Livros Reservados: {contagem['Reservado']}")

  if status_outros:
      print(f"Status não categorizados encontrados: {set(status_outros)}")
  print("-----------------------------------")

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

    # Criação de usuários de exemplo
    User("Robertinho", "12345678", "000.000.000-00")
    User("Sophia", "abcd1234", "111.111.111-11")

    # Autenticação antes de acessar o sistema
    usuario = autenticar_usuario()
    if not usuario:
      print("Encerrando o sistema por falha de login.")
      return

    while True:
        opcao = menu_principal() 

        if opcao == '1':
            print("\n--- Opção 1: Cadastro de Usuário (A FAZER) ---") 
            input("Pressione Enter para continuar...") 

        elif opcao == '2':
            ListarUsuarios()
            input("Pressione Enter para continuar...") 
        
        elif opcao == '3':
            CadastrarLivro()
            print("\n--- Opção 3: Cadastro de Livro (A FAZER) ---")
            input("Pressione Enter para continuar...") 

        elif opcao == '4':
            ListarLivros()
            print("\n--- Opção 4: Listagem de Livros ---")
            input("Pressione Enter para continuar...")
        
        elif opcao == '5':
            print("\n--- Opção 5: Visualizar Status do Livro (A FAZER) ---")
            input("Pressione Enter para continuar...")
            
        elif opcao == '6':
            RealizarEmprestimo(usuario)
            print("\n--- Opção 6: Realizar Empréstimo (A FAZER) ---")
            input("Pressione Enter para continuar...")

        elif opcao == '7':
            ContarLivrosPorStatus()
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
