import heapq
import random

def main():
	tam_fila_prior = 5
	pedidos_prioritarios = []
	pedidos_preparacao = []

	while True:
		print("\n*************")
		print("*** Tamanho maximo da fila de prioridades: ", tam_fila_prior, "***")
		print("*** Quantidade de pedidos na fila de prioridades: ",
		      len(pedidos_prioritarios), "***")
		print("*** Quantidade de pedidos na fila de preparação: ",
		      len(pedidos_preparacao), "***")
		print("*************")
		print("***")
		print("*** 1 Definir tamanho da fila com prioridades")
		print("*** 2 Adicionar novo grupo na fila com prioridades")
		print("*** 3 Mostrar próximo grupo aguardando")
		print("*** 4 Preparar próxima refeição")
		print("*** 5 Entregar refeição")
		print("*** 6 Gerar simulação")
		print("*** 0 Sair")
		print("***")
		print("*************")
		print("Digite a opção escolhida:")

		opcao = int(input())

		if opcao == 1:
			print("\n* Digite o tamanho da fila de prioridades: ")
			tam_fila_prior = int(input())
			pedidos_prioritarios = []

		elif opcao == 2:
			if (len(pedidos_prioritarios) >= tam_fila_prior):
				print(
				 "\n~~Não foi possível adicionar grupo, aguarde algum pedido ser liberado")
			else:
				print("\n* Cadastro de grupo: ")
				print("** Quantidade de pessoas: ")
				qtd_pessoas = int(input())
				print("** Tempo de preparo: ")
				tmp_preparo = int(input())
				print("** Nome da reserva: ")
				nome = str(input())

				heapq.heappush(pedidos_prioritarios, (tmp_preparo, qtd_pessoas, nome))
				print("\n~~Adicionado a lista de prioridades\n")

		elif opcao == 3:
			if (len(pedidos_prioritarios) == 0):
				print("\n~~Não temos pedidos priorizados para serem mostrados.")
			else:
				proximo_grupo = pedidos_prioritarios[
				 0]  # retorna menor valor mas não remove

				print("\n* Próximo grupo a ser chamado:")
				print("** Nome da reserva:", proximo_grupo[2])
				print("** Tempo de preparo:", proximo_grupo[0])
				print("** Quantidade de pessoas:", proximo_grupo[1])

		elif opcao == 4:
			if (len(pedidos_prioritarios) == 0):
				print("\n~~Não temos pedidos priorizados para serem preparados.")
			else:
				# retorna menor valor e remove da fila 1 (prioridades)
				proximo_em_preparacao = heapq.heappop(pedidos_prioritarios)

				# soma tempo de espera
				tmp_espera = proximo_em_preparacao[0]
				for pedido in pedidos_preparacao:
					tmp_espera += pedido[0]

				# adiciona a fila 2 (preparação)
				pedidos_preparacao.append(proximo_em_preparacao)

				print("\n~~ ", proximo_em_preparacao[2],
				      "entrou em preparação. O tempo de espera estimado é de ", tmp_espera,
				      " minutos.")

		elif opcao == 5:
			if (len(pedidos_preparacao) == 0):
				print("\n~~Não temos pedidos para serem entregues.")
			else:
				# retorna e remove pedido da fila 2(preparação)
				pedido_entregue = pedidos_preparacao.pop(0)
				print("\n~~ Oba! o pedido", pedido_entregue[2], "está pronto.")

		elif opcao == 6:
			print("\n* Gerar simulação:")

			print("** Digite a quantidade de simulações a serem geradas:")
			num_simulacoes = int(input())

			# valida se o tamanho da lista + qtd de simulações é maior que o tamanho max. da fila 1 (prioridades)
			if (len(pedidos_prioritarios) + num_simulacoes > tam_fila_prior):
				print("\n~~Aumente o tamanho da fila de prioridades.")
				continue

			print("** Digite o valor máximo de tempo de preparo:")
			max_tmp_preparo = int(input())

			# gera N pedidos com valores aleatorios e adiciona na fila 1(prioridades)
			for index in range(1, num_simulacoes + 1):
				tempo_preparo = random.randint(0, max_tmp_preparo)
				qtd_pessoas = random.randint(1, 15)
				nome = "Reserva " + str(index)

				heapq.heappush(pedidos_prioritarios, (tempo_preparo, qtd_pessoas, nome))

		elif opcao == 0:
			print("\n~~Finalizando.")
			break
		else:
			print("\n~~Opção inválida. Tente novamente.")
			
main()
