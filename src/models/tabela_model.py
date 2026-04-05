class TabelaModel:
    
    LIMITE_BITS = 12

    @staticmethod
    def validar_bits(n_bits: int) -> tuple[bool, str]:
        """Valida o número de bits. Retorna (valido, mensagem_erro)"""
        if n_bits < 1:
            return False, "O número de bits deve ser maior que 0."
        if n_bits > TabelaModel.LIMITE_BITS:
            return False, f"Por questões de performance o limite máximo é {TabelaModel.LIMITE_BITS} bits."
        return True, ""

    @staticmethod
    def total_entradas(n_bits: int) -> str:
        """Retorna o texto com o total de entradas."""
        total = 2 ** n_bits
        return f"Total de entradas: 2^{n_bits} = {total}"

    @staticmethod
    def inteiro_para_binario(num: int, bits: int) -> str:
        """Converte um inteiro para binário com número fixo de bits."""
        binario = ""
        for i in range(bits - 1, -1, -1):
            binario += "1" if (num & (1 << i)) else "0"
        return binario

    @staticmethod
    def gerar_tabela_gray(n: int) -> list:
        """Gera a tabela de código Gray para n bits."""
        resultados = []
        for i in range(2 ** n):
            binario = TabelaModel.inteiro_para_binario(i, n)
            gray_valor = i ^ (i >> 1)
            gray = TabelaModel.inteiro_para_binario(gray_valor, n)
            resultados.append((i, binario, gray))
        return resultados