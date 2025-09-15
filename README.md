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

### Como Executar

Este projeto utiliza apenas bibliotecas padrão do Python, o que significa que não é necessário instalar dependências externas.

1.  **Pré-requisitos:** Certifique-se de ter o **Python** instalado em seu sistema.
2.  **Abra o arquivo:** No seu ambiente de desenvolvimento, como o VS Code, abra o arquivo-fonte do projeto.
3.  **Execute o código:** Clique em "Run Code" ou use o comando apropriado no terminal.
4.  **Interaja:** O terminal exibirá um menu interativo que guiará você pelas diferentes opções de simulação.

---

### Decisões de Projeto e Arquitetura

O simulador foi construído com as seguintes escolhas de design para garantir a melhor experiência didática e organização do código:

* **Modularidade:** A lógica para cada técnica de gerenciamento de memória foi encapsulada em classes separadas (`ContiguousMemory` e `PagingMemory`), facilitando a manutenção e a clareza.
* **Visualização Didática:** Para os algoritmos **Best-Fit** e **Worst-Fit**, o simulador faz uma pausa de 15 segundos antes de alocar o processo. Durante essa pausa, ele destaca todos os "buracos" candidatos e o escolhido, permitindo que você visualize o "processo de pensamento" do algoritmo.
* **Representação Abstrata da Memória:** A memória é representada por uma lista simples em Python, uma abstração eficaz e de baixo custo computacional para os objetivos do projeto.
* **Feedback em Tempo Real:** As métricas de fragmentação são calculadas e exibidas a cada atualização, fornecendo um feedback imediato sobre as consequências das suas ações.
