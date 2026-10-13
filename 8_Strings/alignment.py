template = "{hex:<6}{name:<10}"
print(template.format(hex = "#FF0000", name ="Red"))

template = "{hex:>7}{name:>10}"
print(template.format(hex = "#FF0000", name ="Red"))

template = "{hex:^7}{name:^10}"
print(template.format(hex = "#FF0000", name ="Red"))