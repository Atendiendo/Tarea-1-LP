import re

texto = "((3 + 1) * (500 - 34) + ANS30 // 4)"

patron = r'[^+\-*//()\d\s]'
match = re.search(patron, texto)

if match:
    print("Hay match")
else:
    print("No hay match")
