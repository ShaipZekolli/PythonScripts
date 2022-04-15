import re
import num2words
from deep_translator import GoogleTranslator
import sys
try:
    text=""
    input = sys.argv[1]
    with open(input) as f_input:
        text = f_input.read()
except:
    print("Jepni një file si input.\np.sh 'python Normalizimi AL.py shembull.txt'")
text = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), text)

with open('output.txt', 'w') as f_output:
    f_output.write(text)
translated = GoogleTranslator(source='english', target='albanian').translate_file('output.txt')
with open('output.txt', 'w') as f_output:
    f_output.write(translated)
print(translated)
