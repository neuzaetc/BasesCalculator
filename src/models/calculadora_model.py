from src.models.conversor_model import ConversorModel

class CalculadoraModel:

    OPERACOES = ["+", "-"]

    @staticmethod
    def calcular(valor1: str, valor2: str, base1: int, base2: int, operacao: str) -> int:
        n1 = ConversorModel.para_decimal(valor1, base1)
        n2 = ConversorModel.para_decimal(valor2, base2)

        if operacao == "+":
            return n1 + n2
        elif operacao == "-":
            return n1 - n2
        elif operacao == "*":
            return n1 * n2
        elif operacao == "/":
            if n2 == 0:
                raise ValueError("Divisão por zero!")
            return n1 // n2
        else:
            raise ValueError(f"Operação inválida: {operacao}")
        
        
    @staticmethod
    def calcular_para_todas(valor1: str, valor2: str, base1: int, base2: int, operacao: str) -> dict:
        try:
            resultado = CalculadoraModel.calcular(valor1, valor2, base1, base2, operacao)
            return {
                "decimal": resultado,
                "2":       ConversorModel.de_decimal(resultado, 2),
                "8":       ConversorModel.de_decimal(resultado, 8),
                "10":      ConversorModel.de_decimal(resultado, 10),
                "16":      ConversorModel.de_decimal(resultado, 16),
                "erro":    None,
            }
        except Exception as ex:
            return {
                "decimal": None,
                "2": "", "8": "", "10": "", "16": "",
                "erro": str(ex),
            }


    @staticmethod
    def resultado_para_base(resultado_decimal: int, base_saida: str) -> dict:
        try:
            negativo = resultado_decimal < 0

            bin_res = "Não suportado" if negativo else ConversorModel.de_decimal(resultado_decimal, 2)
            oct_res = "Não suportado" if negativo else ConversorModel.de_decimal(resultado_decimal, 8)
            dec_res = str(resultado_decimal)
            hex_res = "Não suportado" if negativo else ConversorModel.de_decimal(resultado_decimal, 16)

            return {
                "2":  f"Binário: {bin_res}"    if base_saida in ("all", "2")  else "",
                "8":  f"Octal: {oct_res}"      if base_saida in ("all", "8")  else "",
                "10": f"Decimal: {dec_res}"    if base_saida in ("all", "10") else "",
                "16": f"Hexadecimal: {hex_res}" if base_saida in ("all", "16") else "",
                "erro": None,
            }
        except Exception as ex:
            return {
                "2": "", "8": "", "10": "", "16": "",
                "erro": str(ex),
            }