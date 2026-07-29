def encode(strs: list[str]) -> str:
    codificado = ""
    for palabra in strs:
        codificado += f"{len(palabra)}#{palabra}"
    return codificado

def decode(s: str) -> list[str]:
    list_str = []
    long_str = ""
    contador = 0
    while s:
        for number in s:
            if number == "#":
                break
            contador +=1
            long_str += number
        long_content = int(long_str)
        list_str.append(s[contador+1:long_content + contador + 1])
        s = s[long_content + contador + 1:]
        contador = 0
        long_str = ""
    return list_str

print(decode("12#abcdefghijkl"))
print(decode(encode(["hola","mundo"])))
print(decode(encode(["123", "ok"])))

