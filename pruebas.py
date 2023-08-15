import re

texto = "((3 + 1) * (500 - 34) - 30 $+ ANS - CUPON(80))"
patron = r'/([\s\S]*?)(\bANS\b|\bCUPON\(\s*\d+(?:\s*,\s*\d+)*\)\b|\d+|\+|\-|\*|//)/g'

match = re.match(patron,texto)
if match:
    print("Hay match")
else:
    print("No hay match")

