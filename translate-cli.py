from mtranslate import translate
import argparse
import os

parser = argparse.ArgumentParser(description='CLI переводчик основанный на Google translate API')
parser.add_argument("-lf", "--language_from", help="язык с которого выполняется перевод (default auto).", default="auto")
parser.add_argument("-lt", "--language_to", help="язык на который выполняется перевод (default ru).", default="ru")
parser.add_argument("-t", "--text", help="быстрый перевод без оболочки")
args = parser.parse_args()


def core_of_translate(text):
    print(f"{translate('current translate is',args.language_to,'en')}:"
          f"\n{translate(text, args.language_to, args.language_from)}")


def shell_cli():
    while True:
        text = input("Translate-CLI>")
        if text in ["exit()", "quit()"]:
            print("bye", "\n")
            break
        if text == "clear()":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        core_of_translate(text)


try:
    shell_cli() if args.text is None else core_of_translate(args.text)

except Exception as e:
    print(f"uncatched error {e=}")
    pass
