# Gerenciamento-de-Memória-com-Python

Simulador de Gerenciamento de Memória em Python

Nome: Marcelo de Mello Copelli

*Descrição do Projeto e Tópico Escolhido*

Este projeto é um simulador interativo desenvolvido em Python para demonstrar e visualizar duas técnicas fundamentais de gerenciamento de memória utilizadas em Sistemas Operacionais: Alocação Contígua Dinâmica e Paginação Pura.

O objetivo principal é oferecer uma ferramenta didática que permita ao usuário:

•	Adicionar e remover processos da memória.

•	Visualizar o estado da memória em tempo real.

•	Alternar entre diferentes algoritmos de alocação na simulação contígua.

•	Analisar os efeitos da fragmentação interna (na paginação) e externa (na alocação contígua).


A simulação de Alocação Contígua inclui os seguintes algoritmos:

1.	First-Fit: Aloca o processo no primeiro espaço livre grande o suficiente.
   
2.	Best-Fit: Procura o menor espaço livre que possa acomodar o processo, minimizando o desperdício.
   
3.	Worst-Fit: Procura o maior espaço livre, deixando o maior fragmento restante.
   
4.	Circular-Fit: Similar ao First-Fit, mas começa a busca a partir de onde a última alocação terminou.
   
A simulação de Paginação Pura permite ao usuário configurar o tamanho total da memória e o das páginas/frames, demonstrando como um processo pode ser dividido em partes não contíguas para otimizar o uso do espaço.


*Linguagem de Programação e Tipo de Interface*

•	Linguagem: Python. Escolhida por questão de familiaridade e fácil compreendimento.

•	Interface: A interface utilizada foi o próprio terminal do VS Code. Escolhida por ser objetiva e de fácil compreensão.

*Dependências e Bibliotecas Necessárias*

O projeto utiliza apenas bibliotecas padrão do Python, portanto, não há necessidade de instalar pacotes externos.

•	os: Utilizada para a função os.system(), que limpa a tela do console (cls no Windows, clear em Unix/Linux/macOS), melhorando a experiência do usuário.

•	time: Utilizada para a função time.sleep(), que cria pausas intencionais para fins didáticos, permitindo que o usuário observe o processo de decisão dos algoritmos Best-Fit e Worst-Fit.

*Instruções de Compilação e Execução*

1.	Instale a extensão do Python para o VS Code.
   
2.	Abra o arquivo do código no mesmo.
   
3.	Clique no botão ‘Run Code’ para executaro código.
   
4.	Seguindo os passos acima, o terminal abrirá com o menu interativo.

*Decisões de Projeto e Arquitetura Adotadas*

1.	Modularidade com Classes (ContiguousMemory e PagingMemory):
   
o	A lógica de cada técnica de gerenciamento de memória foi encapsulada em sua própria classe. Isso separa as responsabilidades, tornando o código mais organizado, legível e fácil de manter. Cada classe gerencia seu próprio estado (lista de blocos/frames, tabela de processos) e comportamento (alocar, remover, calcular fragmentação).

2.	Foco na Visualização Didática (Visualização em Duas Etapas):
   
o	Para os algoritmos Best-Fit e Worst-Fit, foi implementada uma visualização especial em duas etapas.

   Etapa 1: O simulador primeiro exibe a memória destacando todos os "buracos" candidatos que poderiam abrigar o novo processo e marca qual deles foi o escolhido.
 
   Etapa 2: Após uma pausa de 15 segundos, a tela é atualizada para mostrar o processo efetivamente alocado.
  
o	Justificativa: Essa decisão foi crucial para o propósito didático do projeto. Em vez de apenas mostrar o resultado final, o simulador revela o "processo de pensamento" do algoritmo, ajudando o usuário a entender por que uma determinada escolha foi feita.

3.	Representação Abstrata da Memória:
   
o	A memória principal é representada por uma simples lista (array).

  Na ContiguousMemory, cada índice da lista representa um bloco de memória, contendo ‘Livre’ – se não houver PID na memória – ou o PID do processo que o ocupa.
  
  Na PagingMemory, cada índice representa um frame, contendo ‘Livre’ ou um dicionário com o PID e o número da página do processo.
  
o	Justificativa: Essa é uma abstração eficaz e de baixo custo computacional que simula com precisão o estado de ocupação da memória para os fins deste projeto.

4.	Interface Orientada por Menus:
   
o	A navegação é controlada por um loop while True em cada função de menu (main_menu, contiguous_menu, paging_menu). Funções de render_dashboard_* são chamadas a cada iteração para redesenhar a tela.

o	Justificativa: Este padrão é robusto, fácil de implementar para aplicações de console e oferece uma experiência de usuário clara e controlada.

5.	Cálculo de Fragmentação em Tempo Real:
    
o	As métricas de fragmentação (externa para contígua, interna para paginação) são calculadas e exibidas a cada atualização do dashboard.

o	Justificativa: Isso fornece feedback imediato ao usuário sobre as consequências de suas ações (adicionar/remover processos) e ajuda a comparar a eficiência dos diferentes algoritmos e técnicas de alocação.
