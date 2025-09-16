# Gerenciamento de Memória com Python

## Simulador de Gerenciamento de Memória em Python

**Autor:** Marcelo de Mello Copelli

Este projeto é um simulador interativo desenvolvido em **Python** para demonstrar e visualizar duas técnicas fundamentais de gerenciamento de memória em Sistemas Operacionais: **Alocação Contígua Dinâmica** e **Paginação Pura**. O objetivo principal é oferecer uma ferramenta didática que permite ao usuário interagir e compreender os conceitos de alocação, fragmentação e otimização de espaço.

---

### Funcionalidades do Simulador

O simulador foi projetado para oferecer uma experiência de aprendizado prática, permitindo que você:

* **Adicione e remova processos** da memória.
* **Visualize o estado da memória** em tempo real.
* **Alterne entre diferentes algoritmos** de alocação contígua.
* **Analise os efeitos da fragmentação** (interna e externa) e a eficiência de cada técnica.

#### 1. Simulação de Alocação Contígua

Esta seção do simulador demonstra a alocação de blocos de memória em um espaço contíguo. Os seguintes algoritmos estão disponíveis para estudo:

* **First-Fit:** Aloca o processo no primeiro espaço livre que for grande o suficiente.
* **Best-Fit:** Procura o menor espaço livre que possa acomodar o processo, minimizando o desperdício.
* **Worst-Fit:** Procura o maior espaço livre para alocar o processo, deixando o maior fragmento restante.
* **Circular-Fit:** Similar ao First-Fit, mas a busca pelo espaço começa a partir da última alocação.

#### 2. Simulação de Paginação Pura

A simulação de Paginação Pura demonstra como um processo é dividido em partes menores (**páginas**) que podem ser alocadas em locais não contíguos (**frames**) na memória. Você pode configurar o tamanho total da memória e o das páginas para observar como a fragmentação interna é gerada.

---

### Tecnologias e Dependências

O projeto utiliza apenas bibliotecas padrão do Python, o que significa que não é necessário instalar dependências externas. As bibliotecas usadas são:

* **`os`:** Utilizada para interagir com o sistema operacional, como limpar a tela do console.
    * **Link para a documentação oficial:** [https://docs.python.org/pt-br/3/library/os.html](https://docs.python.org/pt-br/3/library/os.html)
* **`time`:** Usada para criar pausas intencionais, o que é fundamental para a visualização didática dos algoritmos **Best-Fit** e **Worst-Fit**.
    * **Link para a documentação oficial:** [https://docs.python.org/pt-br/3/library/time.html](https://docs.python.org/pt-br/3/library/time.html)

---

### Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o **Python** instalado em seu sistema.
2.  **Abra o arquivo:** No seu ambiente de desenvolvimento, como o VS Code, abra o arquivo-fonte do projeto.
3.  **Execute o código:** Clique em "Run Code" ou use o comando apropriado no terminal.
4.  **Interaja:** O terminal exibirá um menu interativo que guiará você pelas diferentes opções de simulação.

---

### Como Funciona o Menu Interativo

O menu será dividio em duas partes, Alocação Contígua Dinâmica e Paginação Pura.

* **Menu Inicial:** No menu inicial, que será aquele com primeira interação do usuário, iremos ter 3 opções, a da alocação, da paginação e uma opção de sair da simulação.
* **Alocação Contígua Dinâmica:** Indo para a opção da alocação contígua, você terá a informação de qual algoritmo está sendo usado atualmente(First-fit, best...), um desenho da memória com seus espaços e blocos, informações complementares, fragmentação externa e outro menu interativo. O menu da alocação tem 5 opções, a primeira delas sendo de alterar o algoritmo para o desejado, a segunda será para adicionar processos na memória, podendo colocar o PID desejado e seu tamanho em KB, a terceira será de remover o processo desejado, na quarta opção você poderá resetar a simulação e a cinco você poderá voltar para o menu inicial.
* **Paginação Pura:** A opção da paginação nos da 2 opção de início, uma para configurar a memória, para poder colocar o tamanho total da memória e o tamanho da página, ambos em KB. Já a outra opção será de voltar para o menu inicial. Após configurar a memória, nos é dado um desenho da memória física com seus quadros, junto da fragmentação interna e nosso menu interativo, que conta com 4 opções. Todas as opções da paginação seguem o mesmo modelo da alocação.

---

### Decisões de Projeto e Arquitetura

O simulador foi construído com as seguintes escolhas de design para garantir a melhor experiência didática e organização do código:

* **Modularidade:** A lógica para cada técnica de gerenciamento de memória foi encapsulada em classes separadas (`ContiguousMemory` e `PagingMemory`), facilitando a manutenção e a clareza.
* **Visualização Didática:** Para os algoritmos **Best-Fit** e **Worst-Fit**, o simulador faz uma pausa de 10 segundos antes de alocar o processo. Durante essa pausa, ele destaca todos os "buracos" candidatos e o escolhido, permitindo que você visualize o "processo de pensamento" do algoritmo.
* **Representação Abstrata da Memória:** A memória é representada por uma lista simples em Python, uma abstração eficaz e de baixo custo computacional para os objetivos do projeto.
* **Feedback em Tempo Real:** As métricas de fragmentação são calculadas e exibidas a cada atualização, fornecendo um feedback imediato sobre as consequências das suas ações.

---

### Funções Usadas no Código

O código conta com várias funções para determinados propósitos, sendo elas:

#### Alocação Contígua Dinâmica:

* **clear_screen():** Essa função é responsável por limpar o terminal ou console, proporcionando uma interface mais limpa a cada atualização do menu ou da visualização da memória. Ela verifica o sistema operacional: se for Windows (os.name == 'nt'), executa o comando cls, caso contrário, utiliza clear, que é o comando equivalente em sistemas Unix/Linux/macOS. Isso permite que o código tenha uma aparência visual mais amigável e funcional em diferentes plataformas.
*  **pause():** A função pause serve para interromper a execução do programa até que o usuário pressione a tecla Enter. Isso é especialmente útil em momentos onde há uma exibição de informações que o usuário precisa ler antes de prosseguir, como após uma ação de alocação ou remoção de processos. Com isso, o controle do tempo de leitura fica com o usuário, melhorando a experiência interativa do simulador.
*  **_init_() da classe MemoriaContigua:** Esse método é o construtor da classe MemoriaContigua, que simula a memória principal usando o modelo de alocação contígua. Ele recebe como parâmetros o tamanho total da memória (em KB) e o tamanho de cada bloco. A memória é representada como uma lista de blocos, inicialmente todos vazios (None), e a estrutura também armazena os processos alocados e um índice para controle do algoritmo Circular-Fit. Com isso, a classe é preparada para realizar simulações de diferentes estratégias de alocação.
*  **imprimir_memoria_com_destaques():** Essa função imprime o estado atual da memória, mas com destaque para os buracos livres considerados candidatos à alocação, identificando visualmente qual foi o buraco escolhido pelo algoritmo. Essa visualização facilita o entendimento do comportamento do algoritmo selecionado (como Best-Fit ou Worst-Fit), ajudando a demonstrar como e por que certas áreas da memória são escolhidas.
*  **imprimir_memoria():** A função imprimir_memoria exibe a situação atual da memória, bloco por bloco. Cada bloco é indicado como "Livre" (quando estiver vazio) ou como pertencente a um processo específico (exibindo o PID do processo). Essa visualização é essencial para o usuário acompanhar a ocupação da memória ao longo do tempo durante a simulação.
*  **imprimir_tabela_processos():** Essa função exibe uma tabela contendo informações sobre todos os processos atualmente alocados na memória. Para cada processo, são mostrados o PID, a base (posição inicial na memória), o limite (posição final) e o tamanho total em KB. Essa tabela fornece uma visão consolidada dos processos ativos e sua respectiva alocação na memória.
*  **calcular_fragmentacao_externa():** Esta função calcula e exibe a fragmentação externa da memória. A fragmentação externa ocorre quando há espaço livre suficiente para alocar um processo, mas esse espaço está dividido em partes menores que o tamanho do processo. A função percorre a memória identificando blocos livres e calcula a diferença entre o total de memória livre e o maior bloco contínuo de memória. O resultado é exibido tanto em KB quanto em percentual, auxiliando na análise da eficiência da alocação.
*  **first_fit():** O método first_fit implementa o algoritmo de alocação First-Fit. Ele percorre a lista de blocos procurando o primeiro buraco (sequência contínua de blocos livres) que seja grande o suficiente para acomodar o número de blocos requeridos. Ao encontrar tal buraco, retorna o índice inicial para alocação. Caso não encontre, retorna -1 indicando falha.
*  **_encontrar_buracos_livres():** Essa função auxiliar percorre a memória e identifica todos os buracos (espaços livres contínuos) que tenham tamanho suficiente para alocar um processo. Cada buraco identificado é adicionado a uma lista de dicionários contendo a posição inicial e o tamanho do buraco. Essa função é utilizada principalmente pelos algoritmos Best-Fit e Worst-Fit para selecionar o buraco mais adequado.
*  **best_fit():** O método best_fit aplica a estratégia Best-Fit, que escolhe o menor buraco possível que ainda seja suficiente para alocar o processo. Ele utiliza a função _encontrar_buracos_livres para obter os candidatos, e seleciona aquele com menor tamanho. Retorna o buraco escolhido e a lista de candidatos para visualização e análise.
*  **worst_fit():** Este método aplica o algoritmo Worst-Fit, que procura o maior buraco disponível na memória. Após encontrar todos os buracos possíveis usando _encontrar_buracos_livres, seleciona aquele com o maior número de blocos. Assim como no Best-Fit, ele retorna o buraco escolhido e todos os candidatos para permitir destaque visual.
*  **circular_fit():** O método circular_fit implementa uma variação do First-Fit chamada Circular-Fit, que começa a busca por um buraco adequado a partir do último ponto de alocação, circulando até o início da memória. Essa abordagem busca distribuir os processos de forma mais uniforme e evita concentrar as alocações sempre no início da memória.
*  **_explicar_candidatos():** Esta função imprime, em formato textual, a lista de buracos livres candidatos para alocação, indicando o início e o tamanho de cada um. O buraco selecionado pelo algoritmo também é marcado com um texto indicando que foi o escolhido. Essa função serve para explicar de forma clara e didática o processo de decisão do algoritmo.
*  **alocar_processo():** A função alocar_processo coordena todo o processo de alocação de memória para um novo processo. Ela calcula quantos blocos são necessários e aplica o algoritmo de alocação correspondente (First-Fit, Best-Fit, Worst-Fit ou Circular-Fit). Em caso de sucesso, atualiza os blocos de memória e a lista de processos. No caso de Best-Fit e Worst-Fit, há ainda uma simulação visual com tempo de espera, explicando a decisão tomada pelo algoritmo.
*  **remover_processo():** Essa função remove um processo da memória, liberando os blocos que estavam ocupados por ele e removendo-o da lista de processos ativos. A função localiza o processo pelo PID e atualiza a memória para que os blocos fiquem marcados como livres novamente.

#### Paginação Pura

*  **_init_() da classe MemoriaPaginacao:** O construtor da classe MemoriaPaginacao inicializa a estrutura da memória para simular o esquema de paginação. Define o tamanho total da memória, o tamanho das páginas (e, consequentemente, dos quadros), e inicializa a lista de quadros como vazia. Também mantém uma lista de processos, cada um com suas páginas mapeadas para quadros físicos.
*  **imprimir_memoria() da classe MemoriaPaginacao:** Essa função imprime o estado atual da memória física, onde cada quadro é mostrado como "Livre" ou associado a uma página de um processo. Essa representação permite visualizar como os quadros estão ocupados na memória e como diferentes processos compartilham o espaço.
*  **imprimir_tabela_paginas():** Esse método exibe a tabela de páginas de um processo específico, identificando quais quadros físicos estão associados a cada página lógica. Isso ajuda a entender o mapeamento lógico-físico da memória no modelo de paginação e permite diagnosticar onde cada parte do processo está armazenada.
*  **calcular_fragmentacao_interna():** A função calcula a fragmentação interna, que ocorre na última página de um processo quando o tamanho total do processo não é múltiplo do tamanho da página. Essa área "sobrando" representa espaço desperdiçado. A função acumula essa perda de todos os processos e apresenta o total em KB e em percentual da memória.
*  **alocar_processo() da classe MemoriaPaginacao:** Esse método realiza a alocação de um processo no esquema de paginação. Ele verifica se há quadros livres suficientes para alocar todas as páginas necessárias e, se houver, associa cada página a um quadro livre. As informações são armazenadas no processo e atualizadas na lista de quadros. A fragmentação interna é considerada implicitamente e pode ser visualizada depois.
*  **remover_processo() da classe MemoriaPaginacao:** A função remove um processo da memória paginada, liberando todos os quadros físicos ocupados por suas páginas. Após isso, o processo é removido da lista de processos ativos, e a memória fica disponível para futuras alocações.

#### Paineis e Menus

*  **renderizar_painel_contiguo_destaque():** Essa função limpa a tela e exibe uma visão geral do estado atual da memória contígua, destacando os buracos candidatos e o buraco escolhido pelo algoritmo. Ela é usada em alocações com visualização mais interativa (Best-Fit e Worst-Fit), incluindo detalhes como o algoritmo em uso, tabela de processos e fragmentação externa.
*  **renderizar_painel_contiguo():** Semelhante à anterior, essa função exibe o estado atual da memória contígua, mas sem destaque visual de candidatos. Mostra o algoritmo selecionado, os blocos ocupados ou livres, os processos alocados e a fragmentação externa. É usada durante a navegação no menu principal da simulação contígua.
*  **menu_contiguo():** A função menu_contiguo representa a interface principal da simulação para o modelo de alocação contígua dinâmica. Ela instancia um objeto da classe MemoriaContigua e apresenta um menu interativo onde o usuário pode escolher qual algoritmo de alocação deseja utilizar (First-Fit, Best-Fit, Worst-Fit ou Circular-Fit), adicionar ou remover processos, ou resetar a simulação. A cada ação do usuário, o painel de memória é atualizado para refletir as mudanças, e, dependendo do algoritmo selecionado, pode haver uma visualização interativa do processo de decisão de alocação. Essa função também garante tratamento de erros, como tentativas de alocar com PID repetido ou com tamanhos inválidos.
*  **menu_paginacao():** A função menu_paginacao implementa o menu principal para a simulação do modelo de paginação pura. Quando a simulação começa, solicita ao usuário as configurações iniciais da memória, como o tamanho total da memória física e o tamanho da página. Uma vez configurada, o menu permite adicionar ou remover processos, bem como resetar a simulação. O estado da memória (quadros) e a tabela de páginas dos processos são atualizados a cada ação. A função também trata entradas inválidas, como tamanhos não numéricos ou inconsistentes, e evita a alocação de PIDs duplicados.
*  **renderizar_painel_paginacao():** Essa função é responsável por exibir o painel visual da memória no modo de paginação. Ela limpa a tela e imprime os quadros da memória física, além de mostrar as tabelas de páginas de todos os processos alocados. Também exibe a fragmentação interna calculada com base no desperdício nas últimas páginas de cada processo. Esse painel é atualizado constantemente enquanto o usuário interage com o menu de paginação, fornecendo feedback visual contínuo sobre o estado da memória.
*  **menu_principal():** A função menu_principal é o ponto de entrada da aplicação. Ela exibe o menu inicial do simulador, permitindo ao usuário escolher entre os dois modos de gerenciamento de memória disponíveis: alocação contígua dinâmica e paginação pura. Também oferece a opção de sair do programa. A função fica em um loop contínuo até que o usuário decida encerrar a simulação, garantindo uma navegação fluida entre os modos de simulação.

#### Main

* **if _name_ == "_main_":** Este bloco final define o ponto de execução do programa. Ele verifica se o arquivo está sendo executado diretamente (e não importado como módulo em outro script). Caso esteja, ele chama a função menu_principal(), iniciando a interface do simulador. Isso garante que o simulador só será executado interativamente quando for o programa principal.























































