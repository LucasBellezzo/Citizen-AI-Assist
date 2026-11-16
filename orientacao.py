class Orientacao:
    """Representa uma orientacao verificada da base de conhecimento."""

    def __init__(self, id, categoria, titulo, palavras_chave, resposta, documentos, onde, fonte, verificado_em):
        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em

    def exibir(self, pontos=None, confianca=None):
        """Exibe os detalhes completos da orientacao formatados no terminal."""
        print("\n" + "=" * 65)
        if pontos is not None and confianca is not None:
            print(f"Confianca da resposta: {confianca} ({pontos} pontos)")
        print(f">> {self.titulo} [{self.categoria}] (ID: {self.id})")
        print("-" * 65)
        print(f"{self.resposta}\n")
        print("Documentos / Requisitos necessarios:")
        for doc in self.documentos:
            print(f"  - {doc}")
        print(f"\nOnde acessar: {self.onde}")
        print(f"Fonte: {self.fonte} (verificado em {self.verificado_em})")
        print("Aviso: este assistente NAO e um canal oficial. Confirme nos orgaos competentes.")
        print("=" * 65)
