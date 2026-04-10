from src.models.util_model import UtilModel

class ConversorModel:

    # algarismos conversao ate base 16
    ALGARISMOS = "0123456789ABCDEF"
    
    # formata o binario em grupos de 4 
    @staticmethod
    def formatar_binario(valor: str) -> str:
        # remove espaços existentes
        valor = valor.replace(" ", "")
        # preenche com zeros à esquerda para ser múltiplo de 4
        while len(valor) % 4 != 0:
            valor = "0" + valor
        # agrupa em grupos de 4
        return " ".join(valor[i:i+4] for i in range(0, len(valor), 4))

    # converte valor de qualquer base para decimal
    @staticmethod
    def para_decimal(valor: str, base: int) -> int:
        negativo = valor.startswith("-")
        valor = valor.lstrip("-")
        
        decimal = 0
        for i, digito in enumerate(reversed(valor.upper())):
            decimal += ConversorModel.ALGARISMOS.index(digito) * (base ** i)
        
        return -decimal if negativo else decimal

    # converte valor decimal para qualquer base
    @staticmethod
    def de_decimal(valor: int, base: int) -> str:
        if valor == 0:
            return "0"
        
        negativo = valor < 0
        valor = abs(valor)
        
        resultado = ""
        while valor > 0:
            resultado = ConversorModel.ALGARISMOS[valor % base] + resultado
            valor //= base
        
        return f"-{resultado}" if negativo else resultado

    # converte valor de uma base para outra
    @staticmethod
    def converter(valor: str, base_origem: int, base_destino: int) -> str:
        decimal = ConversorModel.para_decimal(valor, base_origem)
        return ConversorModel.de_decimal(decimal, base_destino)
    
    # converte um valor para todas as bases 2 8 10 16
    # se o decimal for muito grande usa notação cientifica
    @staticmethod
    def converter_para_todas(valor: str, base_origem: int) -> dict:
        if not valor:
            return {"2": "", "8": "", "10": "", "16": ""}
        try:
            decimal = ConversorModel.para_decimal(valor, base_origem)  
            # limite maximo 9999999999 10 digitos
            if decimal > 9999999999:
                return {
                    "2":  ConversorModel.formatar_binario(ConversorModel.de_decimal(decimal, 2)),
                    "8":  ConversorModel.de_decimal(decimal, 8),
                    # notação científica para números muito grandes
                    "10": f"{decimal:.15e}",  
                    "16": ConversorModel.de_decimal(decimal, 16),
                }
                
            return {
                "2":  ConversorModel.formatar_binario(ConversorModel.de_decimal(decimal, 2)),
                "8":  ConversorModel.de_decimal(decimal, 8),
                "10": str(decimal),
                "16": ConversorModel.de_decimal(decimal, 16),
            }
        except:
            return {"2": "", "8": "", "10": "", "16": ""}