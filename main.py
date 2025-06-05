alunos = []

def cadastrar_alunos():
  while True:
    # try/except pra não quebrar o código quando há erro
    try:
      aluno = {
        "nome": input("Digite o nome do aluno."),
        "idade": int(input("Digite a idade do aluno.")),
        "nota": float(input("Digite a nota do aluno."))
      }
      if aluno["nota"] > 10.0: aluno["nota"] = 10.0
      elif aluno["nota"] < 0.0: aluno["nota"] = 0.0
    except:
      print("Informações inválidas. Tente novamente.")
    else:
      alunos.append(aluno)

    continuar = input("aCadastrar novo aluno? (Sim/Não)")
    if continuar.lower() not in ["sim","si","s",]:
      break

def listar_alunos():
  print("Lista de alunos:\n----------")
  for aluno in alunos:
    if aluno["nota"] >= 7.0:
      print("- Nome: {} | Idade: {} | Nota: {} | Situação: Aprovado".format(aluno["nome"],aluno["idade"],aluno["nota"]))
    else:
      print("- Nome: {} | Idade: {} | Nota: {} | Situação: Reprovado".format(aluno["nome"],aluno["idade"],aluno["nota"]))

def calcular_media():
  notas_soma = 0
  for aluno in alunos:
    notas_soma += aluno["nota"]
  media = notas_soma / len(alunos)
  print("A média da turma é: {:.2f}".format(media))

while True:
  print("""
  Selecione uma opção.
  ---------
  1 - Cadastrar alunos.
  2 - Listar alunos.
  3 - Calcular média dos alunos.
  4 - Sair.
  ---------
  """)
  escolha = input()
  if escolha == "1":
    cadastrar_alunos()
  elif escolha == "2":
    if len(alunos) > 0: listar_alunos()
    else: print("Lista de alunos vazia. Cadastre alunos!")
  elif escolha == "3":
    if len(alunos) > 0: calcular_media()
    else: print("Lista de alunos vazia. Cadastre alunos!")
  elif escolha == "4": break
  else: print("Comando não reconhecido. Tente Novamente.")
