"""
*---------------------------------------------------------*
*              Fatec São Caetano do Sul                   *
* Autor: 1681432612002 - Augusto Conti                    *
* Objetivo: Implementação de uma Árvore Binária de Busca  *
*           (Binary Search Tree - BST) em Python          *
* Data: 12/05/2026                                        *
*---------------------------------------------------------*
"""


class Nodo:
    """Representa um elemento (nodo) da árvore binária de busca."""

    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    """
    Implementação de uma Árvore Binária de Busca (BST).

    Em uma BST, para qualquer nodo N:
      - todos os nodos da subárvore esquerda possuem chave < N.chave
      - todos os nodos da subárvore direita possuem chave > N.chave
    """

    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------
    # INSERÇÃO
    # ------------------------------------------------------------------

    def inserir(self, chave):
        """Insere uma nova chave na árvore, mantendo a propriedade BST."""
        if self.raiz is None:
            self.raiz = Nodo(chave)
        else:
            self._inserir_aux(self.raiz, chave)

    def _inserir_aux(self, nodo, chave):
        """Auxiliar recursivo para posicionar a nova chave corretamente."""
        if chave < nodo.chave:
            if nodo.esquerda is None:
                nodo.esquerda = Nodo(chave)
            else:
                self._inserir_aux(nodo.esquerda, chave)
        elif chave > nodo.chave:
            if nodo.direita is None:
                nodo.direita = Nodo(chave)
            else:
                self._inserir_aux(nodo.direita, chave)
        # chaves iguais são ignoradas (sem duplicatas)

    # ------------------------------------------------------------------
    # BUSCA
    # ------------------------------------------------------------------

    def _buscar_nodo(self, nodo, chave):
        """Retorna o nodo com a chave buscada, ou None se não encontrado."""
        if nodo is None:
            return None
        if chave == nodo.chave:
            return nodo
        if chave < nodo.chave:
            return self._buscar_nodo(nodo.esquerda, chave)
        return self._buscar_nodo(nodo.direita, chave)

    # ------------------------------------------------------------------
    # CLASSIFICAÇÃO DOS NODOS
    # ------------------------------------------------------------------

    def _obter_nos_internos(self, nodo, acumulador):
        """
        Coleta nodos internos (possuem ao menos um filho).
        Percurso em pré-ordem.
        """
        if nodo is None:
            return
        if nodo.esquerda is not None or nodo.direita is not None:
            acumulador.append(nodo.chave)
        self._obter_nos_internos(nodo.esquerda, acumulador)
        self._obter_nos_internos(nodo.direita, acumulador)

    def _obter_folhas(self, nodo, acumulador):
        """
        Coleta nodos folha (sem filhos).
        Percurso em pré-ordem.
        """
        if nodo is None:
            return
        if nodo.esquerda is None and nodo.direita is None:
            acumulador.append(nodo.chave)
        self._obter_folhas(nodo.esquerda, acumulador)
        self._obter_folhas(nodo.direita, acumulador)

    def listar_nos_internos(self):
        resultado = []
        self._obter_nos_internos(self.raiz, resultado)
        print("