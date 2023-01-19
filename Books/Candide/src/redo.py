import re

def intToRoman(num):
# Storing roman values of digits from 0-9
# when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    ans = (thousands + hundreds +
           tens + ones)
    return ans


for i in range(2,31):
    with open("chapter"+str(i)+".tex","r+") as f:
        text = f.read()
        text = re.sub(r"\\chapter\{([^}]*)\}",r"\\begin{center}\n"+str(intToRoman(i))+r"\\\\\n\\textsc{\1}\n\\end{center}",text)
        text = re.sub(r"\\let\\clearpage\\relax\n","",text)
        text = re.sub(r"\\begingroup\n","",text)
        text = re.sub(r"\\vspace\{1cm\}\n","",text)
        text = re.sub(r"\\endgroup\n","",text)
        text = re.sub(r"\\thispagestyle\{pter\}\n","",text)
        text = re.sub(r"\\vspace\{-1cm\}",r"\\vspace{-0.5cm}\n\\rule{\\textwidth}{0.5pt}",text)
        f.truncate(0)
        f.seek(0)
        f.write(text)

