from mtranslate import translate
import argparse

parser = argparse.ArgumentParser(description='CLI переводчик основанный на Google translate API')
parser.add_argument("-l", "--language", help="язык на который выполняется перевод (default ru).", default="ru")
parser.add_argument("-t", "--text", help="быстрый перевод без оболочки")
args = parser.parse_args()

def shell_CLI():
        while True:
            text = input("Translate-CLI>")
            if text == "exit()" or text == "quit()":
                print("bye", "\n")
                break
            results = translate(text, args.language)
            print("\n", results, "\n")
            
def noshell_CLI():
    results = translate(args.text, args.language)
    print("\n", results, "\n")

try:
    if args.text == None:
        shell_CLI()
    else:
        noshell_CLI()

except:
    pass