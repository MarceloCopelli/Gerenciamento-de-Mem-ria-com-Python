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
