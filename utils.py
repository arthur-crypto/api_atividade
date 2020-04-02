from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Arthur', idade=41)
    print(pessoa)
    pessoa.save()


# realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Arthur').first()
    print(pessoa.idade)


# altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Arthur').first()
    pessoa.nome = 'Ribeiro'
    pessoa.save()


# Exclui dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Arthur').first()
    pessoa.delete()


if __name__ == '__main__':
    insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
