import os
import time

def clear_screen():
    ###Limpa a tela do console.###
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    ###Pausa a execução até o usuário pressionar Enter.###
    input("\nPressione Enter para continuar...")

# ============================================================
# ALOCAÇÃO CONTÍGUA
# ============================================================

class MemoriaContigua:
    ###Esta classe simula a memória principal com alocação contígua.
    ###Suporta algoritmos: First-Fit, Best-Fit, Worst-Fit e Circular-Fit.
    ###Permite adicionar/remover processos, visualizar a memória e calcular fragmentação externa.

    def __init__(self, tamanho_kb=1000, tamanho_bloco_kb=10): 
        self.tamanho_kb = tamanho_kb   # Tamanho total da memória em KB
        self.tamanho_bloco_kb = tamanho_bloco_kb  # Tamanho de cada bloco em KB
        self.blocos = [None] * (tamanho_kb // tamanho_bloco_kb)  # Lista representando a memória dividida em blocos
        self.processos = []  # Lista de processos alocados
        self.ultimo_indice_circular = 0  # Posição usada pelo algoritmo Circular-Fit

    def imprimir_memoria_com_destaques(self, candidatos, inicio_escolhido):
        ###Imprime o estado da memória destacando os buracos candidatos.###
        print("\nMemória (Analisando Opções):")
        
        mapa_destaques = {}
        for buraco in candidatos:
            for i in range(buraco['inicio'], buraco['inicio'] + buraco['tamanho']):
                if buraco['inicio'] == inicio_escolhido:
                    mapa_destaques[i] = "Escolhido"
                else:
                    mapa_destaques[i] = "Candidato"

        for i, blk in enumerate(self.blocos):
            if i in mapa_destaques:
                marcador = "<-- Melhor Opção" if mapa_destaques[i] == "Escolhido" else ""
                print(f"[{i:03}] Candidato {marcador}")
            elif blk is None:
                print(f"[{i:03}] Livre")
            else:
                print(f"[{i:03}] Processo {blk}")

    def imprimir_memoria(self):
        ###Imprime o estado atual da memória.###
        print("\nMemória (blocos de {} KB):".format(self.tamanho_bloco_kb))
        for i, blk in enumerate(self.blocos):
            if blk is None:
                print(f"[{i:03}] Livre")
            else:
                print(f"[{i:03}] Processo {blk}")

    def imprimir_tabela_processos(self):
        ###Imprime a tabela de processos alocados.###
        print("\nTabela de Processos:")
        print("-" * 40)
        print(f"{'PID':<8}{'Base':<8}{'Limite':<8}{'Tamanho(KB)':<12}")
        print("-" * 40)
        for p in self.processos:
            print(f"{p['pid']:<8}{p['base']:<8}{p['limite']:<8}{p['tamanho']:<12}")

    def calcular_fragmentacao_externa(self):
        ###Calcula e imprime a fragmentação externa.###
        blocos_livres = 0
        maior_contiguo = 0
        contiguo_atual = 0
        for blk in self.blocos:
            if blk is None:
                blocos_livres += 1
                contiguo_atual += 1
            else:
                maior_contiguo = max(maior_contiguo, contiguo_atual)
                contiguo_atual = 0
        maior_contiguo = max(maior_contiguo, contiguo_atual)
        total_livre_kb = blocos_livres * self.tamanho_bloco_kb
        frag_externa_kb = total_livre_kb - (maior_contiguo * self.tamanho_bloco_kb)
        frag_externa_pct = (frag_externa_kb / self.tamanho_kb) * 100 if self.tamanho_kb else 0
        print(f"\nFragmentação Externa: {frag_externa_kb} KB ({frag_externa_pct:.2f}%)")

    # ---------------------------------------------------------
    # Algoritmos de alocação
    # ---------------------------------------------------------

    def first_fit(self, num_blocos):
        ###Busca o primeiro buraco de tamanho suficiente.###
        contador = 0
        inicio = -1
        for i, blk in enumerate(self.blocos):
            if blk is None:
                if inicio == -1:
                    inicio = i
                contador += 1
                if contador >= num_blocos:
                    return inicio
            else:
                contador = 0
                inicio = -1
        return -1

    def _encontrar_buracos_livres(self, num_blocos):
        ###Encontra todos os buracos livres de tamanho suficiente.###
        candidatos = []
        contador = 0
        inicio = -1
        blocos_temp = self.blocos + ['X']
        for i, blk in enumerate(blocos_temp):
            if blk is None:
                if inicio == -1:
                    inicio = i
                contador += 1
            else:
                if contador >= num_blocos:
                    candidatos.append({'inicio': inicio, 'tamanho': contador})
                contador = 0
                inicio = -1
        return candidatos

    def best_fit(self, num_blocos):
        ###Encontra o buraco livre mais justo.###
        candidatos = self._encontrar_buracos_livres(num_blocos)
        if not candidatos:
            return None, None
        buraco_escolhido = min(candidatos, key=lambda x: x['tamanho'])
        return buraco_escolhido, candidatos

    def worst_fit(self, num_blocos):
        ###Encontra o maior buraco livre.###
        candidatos = self._encontrar_buracos_livres(num_blocos)
        if not candidatos:
            return None, None
        buraco_escolhido = max(candidatos, key=lambda x: x['tamanho'])
        return buraco_escolhido, candidatos

    def circular_fit(self, num_blocos):
        ###Busca o primeiro buraco a partir do último ponto de alocação.###
        n = len(self.blocos)
        inicio_busca = self.ultimo_indice_circular
        for i in range(n):
            indice_atual = (inicio_busca + i) % n
            if self.blocos[indice_atual] is None:
                contador = 0
                inicio_buraco = -1
                for j in range(n):
                    indice_busca = (indice_atual + j) % n
                    if self.blocos[indice_busca] is None:
                        if inicio_buraco == -1:
                            inicio_buraco = indice_busca
                        contador += 1
                        if contador >= num_blocos:
                            self.ultimo_indice_circular = (inicio_buraco + num_blocos) % n
                            return inicio_buraco
                    else:
                        break
        return -1

    def _explicar_candidatos(self, candidatos, inicio_escolhido):
        ###Imprime a lista de buracos candidatos para explicação.###
        print("\nAnalisando buracos disponíveis (início, tamanho):")
        for buraco in candidatos:
            marcador = "<-- ESCOLHIDO" if buraco['inicio'] == inicio_escolhido else ""
            print(f"  - Início: {buraco['inicio']}, Tamanho: {buraco['tamanho']} {marcador}")

    def alocar_processo(self, pid, tamanho_kb, estrategia, dict_algos):
        ###Orquestra a alocação de um processo com visualização.###
        num_blocos = (tamanho_kb + self.tamanho_bloco_kb - 1) // self.tamanho_bloco_kb
        if any(p['pid'] == pid for p in self.processos):
            print("Erro: Processo com PID já existe!")
            return False

        inicio = -1
        
        if estrategia == "1":
            inicio = self.first_fit(num_blocos)
        elif estrategia == "2" or estrategia == "3":
            if estrategia == "2":
                buraco_escolhido, candidatos = self.best_fit(num_blocos)
            else:
                buraco_escolhido, candidatos = self.worst_fit(num_blocos)
            
            if buraco_escolhido:
                inicio = buraco_escolhido['inicio']
                renderizar_painel_contiguo_destaque(self, dict_algos[estrategia], candidatos, inicio)
                self._explicar_candidatos(candidatos, inicio)
                print(f"\nO algoritmo '{dict_algos[estrategia]}' escolheu o buraco em {inicio}. Alocando em 10 segundos...")
                time.sleep(10)
            
        elif estrategia == "4":
            inicio = self.circular_fit(num_blocos)

        if inicio == -1:
            print("Memória insuficiente para alocar o processo.")
            return False

        for i in range(inicio, inicio + num_blocos):
            self.blocos[i] = pid
        
        proc = {
            'pid': pid, 'base': inicio * self.tamanho_bloco_kb,
            'limite': (inicio + num_blocos) * self.tamanho_bloco_kb - 1, 'tamanho': tamanho_kb
        }
        self.processos.append(proc)
        print(f"Processo {pid} alocado com sucesso!")
        return True

    def remover_processo(self, pid):
        ###Remove um processo da memória.###
        a_remover = next((p for p in self.processos if p['pid'] == pid), None)
        if not a_remover:
            print("Processo não encontrado.")
            return False
        
        inicio = a_remover['base'] // self.tamanho_bloco_kb
        fim_inclusive = a_remover['limite'] // self.tamanho_bloco_kb
        
        for i in range(inicio, fim_inclusive + 1):
            self.blocos[i] = None
            
        self.processos.remove(a_remover)
        print(f"Processo {pid} removido com sucesso!")
        return True

# ============================================================
# PAGINAÇÃO
# ============================================================

class MemoriaPaginacao:
    def __init__(self, tamanho_mem_kb=1024, tamanho_pagina_kb=4):
        self.tamanho_mem_kb = tamanho_mem_kb
        self.tamanho_pagina_kb = tamanho_pagina_kb
        self.num_quadros = tamanho_mem_kb // tamanho_pagina_kb
        self.quadros = [None] * self.num_quadros
        self.processos = []

    def imprimir_memoria(self):
        ###Imprime o estado da memória física (quadros).###
        print("\nMemória Física (Quadros de {} KB):".format(self.tamanho_pagina_kb))
        for i, q in enumerate(self.quadros):
            if q is None:
                print(f"[Quadro {i:03}] Livre")
            else:
                print(f"[Quadro {i:03}] P{q['pid']} - Página {q['pagina']}")

    def imprimir_tabela_paginas(self, pid):
        ###Imprime a tabela de páginas de um processo específico.###
        proc = next((p for p in self.processos if p['pid'] == pid), None)
        if not proc:
            print(f"Processo {pid} não encontrado.")
            return
        print(f"\nTabela de Páginas - Processo {pid}")
        print("-" * 30)
        print(f"{'Página':<10}{'Quadro':<10}")
        print("-" * 30)
        for i, quadro in enumerate(proc['paginas']):
            print(f"{i:<10}{quadro if quadro is not None else 'N/A':<10}")

    def calcular_fragmentacao_interna(self):
        ###Calcula e imprime a fragmentação interna.###
        frag_kb = 0
        for p in self.processos:
            tamanho_usado_ultima_pagina = p['tamanho'] % self.tamanho_pagina_kb
            if tamanho_usado_ultima_pagina != 0:
                frag_kb += (self.tamanho_pagina_kb - tamanho_usado_ultima_pagina)
        frag_pct = (frag_kb / self.tamanho_mem_kb) * 100 if self.tamanho_mem_kb else 0
        print(f"\nFragmentação Interna: {frag_kb} KB ({frag_pct:.2f}%)")

    def alocar_processo(self, pid, tamanho_kb):
        ###Aloca um processo na memória por paginação.###
        if any(p['pid'] == pid for p in self.processos):
            print("Erro: Processo com PID já existe!")
            return False

        num_paginas = (tamanho_kb + self.tamanho_pagina_kb - 1) // self.tamanho_pagina_kb
        quadros_livres = [i for i, q in enumerate(self.quadros) if q is None]

        if len(quadros_livres) < num_paginas:
            print("Memória insuficiente para alocar o processo.")
            return False

        paginas = [None] * num_paginas
        for i in range(num_paginas):
            quadro = quadros_livres[i]
            self.quadros[quadro] = {'pid': pid, 'pagina': i}
            paginas[i] = quadro

        proc = {
            'pid': pid,
            'tamanho': tamanho_kb,
            'num_paginas': num_paginas,
            'paginas': paginas
        }
        self.processos.append(proc)
        print(f"Processo {pid} alocado com sucesso!")
        return True

    def remover_processo(self, pid):
        ###Remove um processo da memória de paginação.###
        proc = next((p for p in self.processos if p['pid'] == pid), None)
        if not proc:
            print("Processo não encontrado.")
            return False

        for quadro in proc['paginas']:
            if quadro is not None:
                self.quadros[quadro] = None
        self.processos.remove(proc)
        print(f"Processo {pid} removido com sucesso!")
        return True

# ============================================================
# PAINÉIS E MENUS
# ============================================================

def renderizar_painel_contiguo_destaque(mem, nome_algo_atual, candidatos, inicio_escolhido):
    ###Painel de visualização com destaques para alocação contígua.###
    clear_screen()
    print("==============================================")
    print(" SIMULADOR DE GERENCIAMENTO DE MEMÓRIA (Contíguo)")
    print("==============================================")
    print(f"Algoritmo atual: {nome_algo_atual}")
    mem.imprimir_memoria_com_destaques(candidatos, inicio_escolhido)
    mem.imprimir_tabela_processos()
    mem.calcular_fragmentacao_externa()
    print("\n--- AÇÃO ---")

def renderizar_painel_contiguo(mem, algo_atual, dict_algos):
    ###Painel principal para o menu de alocação contígua.###
    clear_screen()
    print("==============================================")
    print(" SIMULADOR DE GERENCIAMENTO DE MEMÓRIA (Contíguo)")
    print("==============================================")
    print(f"Algoritmo atual: {dict_algos[algo_atual]}")
    mem.imprimir_memoria()
    mem.imprimir_tabela_processos()
    mem.calcular_fragmentacao_externa()
    print("\n--- MENU ---")

def menu_contiguo():
    ###Menu principal para a simulação de alocação contígua.###
    mem = MemoriaContigua()
    dict_algos = {'1': 'First-Fit', '2': 'Best-Fit', '3': 'Worst-Fit', '4': 'Circular-Fit'}
    algo_atual = '1'

    while True:
        renderizar_painel_contiguo(mem, algo_atual, dict_algos)
        print("1. Alterar algoritmo de alocação")
        print("2. Adicionar processo")
        print("3. Remover processo")
        print("4. Resetar simulação")
        print("5. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            print("\nEscolha algoritmo:")
            for k, v in dict_algos.items():
                print(f"{k}. {v}")
            escolha_algo = input("Digite a opção: ").strip()
            if escolha_algo in dict_algos:
                algo_atual = escolha_algo
            else:
                print("Opção inválida.")
                pause()
        elif escolha == '2':
            pid = input("Digite o PID do processo: ").strip()
            try:
                tamanho = int(input("Digite o tamanho do processo (KB): "))
                if tamanho <= 0: raise ValueError
            except ValueError:
                print("Tamanho inválido. Deve ser um número inteiro positivo.")
                pause()
                continue
            
            mem.alocar_processo(pid, tamanho, algo_atual, dict_algos)
            
            if algo_atual not in ['2', '3']:
                pause()

        elif escolha == '3':
            pid = input("Digite o PID do processo para remover: ").strip()
            mem.remover_processo(pid)
            pause()
        elif escolha == '4':
            mem = MemoriaContigua()
            print("Simulação resetada.")
            pause()
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
            pause()

def menu_paginacao():
    ###Menu principal para a simulação de paginação.###
    mem = None
    while True:
        renderizar_painel_paginacao(mem)
        if mem is None:
            print("1. Configurar memória")
            print("2. Voltar ao menu principal")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == '1':
                try:
                    tamanho_mem = int(input("Digite o tamanho total da memória (KB): "))
                    tamanho_pagina = int(input("Digite o tamanho da página (KB): "))
                    if tamanho_mem < tamanho_pagina or tamanho_pagina <= 0 or tamanho_mem <= 0:
                        print("Valores inválidos. Tamanhos devem ser positivos e a memória total maior ou igual à página.")
                        pause()
                        continue
                    mem = MemoriaPaginacao(tamanho_mem, tamanho_pagina)
                except ValueError:
                    print("Entrada inválida. Digite apenas números inteiros.")
                    pause()
            elif escolha == '2':
                break
            else:
                print("Opção inválida.")
                pause()
        else:
            print("1. Adicionar processo")
            print("2. Remover processo")
            print("3. Resetar simulação")
            print("4. Voltar ao menu principal")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                pid = input("Digite o PID do processo: ").strip()
                try:
                    tamanho = int(input("Digite o tamanho do processo (KB): "))
                    if tamanho <= 0: raise ValueError
                except ValueError:
                    print("Tamanho inválido. Deve ser um número inteiro positivo.")
                    pause()
                    continue
                mem.alocar_processo(pid, tamanho)
                pause()

            elif escolha == '2':
                pid = input("Digite o PID do processo para remover: ").strip()
                mem.remover_processo(pid)
                pause()

            elif escolha == '3':
                mem = None
                print("Simulação resetada.")
                pause()

            elif escolha == '4':
                break
            else:
                print("Opção inválida.")
                pause()

def renderizar_painel_paginacao(mem):
    ###Painel principal para o menu de paginação.###
    clear_screen()
    print("==============================================")
    print(" SIMULADOR DE GERENCIAMENTO DE MEMÓRIA (Paginação)")
    print("==============================================")
    if mem:
        mem.imprimir_memoria()
        for p in mem.processos:
            mem.imprimir_tabela_paginas(p['pid'])
        mem.calcular_fragmentacao_interna()
    print("\n--- MENU ---")

def menu_principal():
    ###Menu inicial da aplicação.###
    while True:
        clear_screen()
        print("==============================================")
        print(" SIMULADOR DE GERENCIAMENTO DE MEMÓRIA ")
        print("==============================================")
        print("1. Alocação Contígua Dinâmica")
        print("2. Paginação Pura")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == '1':
            menu_contiguo()
        elif escolha == '2':
            menu_paginacao()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            pause()

if __name__ == "__main__":
    menu_principal()
