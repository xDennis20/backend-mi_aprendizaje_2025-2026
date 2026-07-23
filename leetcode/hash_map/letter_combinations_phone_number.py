def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    letras_digits = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }
    resultado = []

    def backtracking(indice: int, cadena_actual: str = ""):
        if len(cadena_actual) == len(digits):
            resultado.append(cadena_actual)
            return
        digito = digits[indice]
        for letra in letras_digits[digito]:
            backtracking(indice + 1, cadena_actual + letra)
    backtracking(0, "")
    return resultado

print(letter_combinations("23"))
print(letter_combinations("2"))