Alunos: Charlan Matter e Henrique Engers

Disciplina: Estrutura de Dados Avançada (Prof. Me. Fahad Kalil)

# DESAFIO (Fila com Prioridades) - Restaurante

Estrutura de dados a ser utilizada: MIN HEAP (retorna o item de menor valor)

CENÁRIO: Imagine que você é o gerente de uma rede de fast food e possui como desafio otimizar o negócio para servir o máximo de pessoas possível cada dia. Você decide que a melhor estratégia para maximizar a rotatividade de clientes é priorizar grupos pequenos ao invés de grupos grandes. Para quaisquer grupos que possuem a mesma quantidade de pessoas, é priorizado o grupo cujas refeições são preparadas mais rapidamente. Considere que o restaurante possui apenas 1 cozinha e as refeições são preparadas de forma sequencial. Agora, sua tarefa é implementar um software que automatize esse cenário fazendo uso do conceito de
Fila com Prioridades (com Binary Heap) e Fila Comum (FIFO).

- FILA 1: Fila com Prioridades (onde são acumulados os pedidos a serem preparados)
- FILA 2: Fila FIFO (onde são armazenados os pedidos que estão em preparo)

TAREFA:
Cada item dentro da fila com prioridades deverá ser representado por uma tupla com o padrão: quantidade de pessoas [int], tempo de preparo [int], nome da reserva [str]

O app deve ter interação com o usuário e terá as seguintes opções em um Menu:
- Definir tamanho da fila com prioridades
- Adicionar novo grupo na fila com prioridades
    - Apresentar mensagem de erro quando tentar inserir e a fila já estiver lotada
- Mostrar próximo grupo aguardando
    - Printar na tela todas as informações da tupla que está no topo da estrutura
    - Não remover o item
- Preparar próxima refeição
    - Retirar da fila e apresentar o nome do grupo, além do tempo estimado de espera pela refeição. (**)
    - Incluir a tupla do grupo retirado da fila 1 na fila 2, que possui as refeições que estão em preparo.
- Entregar refeição
    - Retirar pedido da fila 2 e apresentar a mensagem de que o pedido está pronto, incluindo o nome do grupo.
- Gerar simulação
    - Gerar aleatoriamente vários grupos de diferentes tamanhos, nomes e tempo de preparo e realizar a adição a uma fila previamente vazia, para então o usuário interagir através das opções já existentes no menu, sem ter que ficar digitando os dados.
(**) O tempo de espera da refeição é: tempo de preparo do grupo + soma do tempo de preparo dos grupos que estão atualmente na fila 2.
