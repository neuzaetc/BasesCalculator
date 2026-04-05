class UtilModel:
    
    BASES_VALIDAS = {
        2:  "01",
        8:  "01234567",
        10: "0123456789",
        16: "0123456789ABCDEF"
    }

    LIMITE_CARACTERES = {
        "2":  16,
        "8":  12,
        "10": 10,
        "16": 8
    }

    LABEL_BASES = {
        "2":  "Binário",
        "8":  "Octal",
        "10": "Decimal",
        "16": "Hexadecimal"
    }

    # filtra os caracteres invalidos consoante a base numerica
    @staticmethod
    def validar_caracteres(valor: str, base: int) -> str:
        permitido = UtilModel.BASES_VALIDAS.get(base, "0123456789")
        return ''.join([c for c in valor.upper() if c in permitido])

    # retorna o numero maximo de caracteres permitidos para a base
    @staticmethod
    def limite_caracteres(base: str) -> int:
        return UtilModel.LIMITE_CARACTERES.get(base, 10)

    # retorna o nome da base em pt
    @staticmethod
    def label_base(base: str) -> str:
        return UtilModel.LABEL_BASES.get(base, f"Base {base}")
    
    # limpa o valor de um ou mais campos de input
    @staticmethod
    def limpar_campos(*campos):
        for campo in campos:
            campo.value = ""