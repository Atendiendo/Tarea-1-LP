import re

pattern = r'[^+\-*//()\d]'
input_text = "Tu texto con + algunos -123 caracteres * // ((que) no quieres capturar."

result = re.findall(pattern, input_text)
output_text = ''.join(result)

print(output_text)
