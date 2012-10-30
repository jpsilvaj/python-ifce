from lettuce import *
from ../todo_list/tarefa import tarefa

@step('Eu tenho a tarefa (\s+)')
def tenho_uma_tarefa(step, tarefa):
	world.tarefa = str(tarefa)

@step('Eu guardar isso')
def salvo_minha_tarefa(step):
	world.reposta = banco.salvar(world.tarefa)

@step ('Eu vejo a resposta (\s+)')
def checo_minha_mensagem(step,expected):
	expected = str(expected)
	assert world.resposta == expected, 'Com %s' % world.tarefa

