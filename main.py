#!/usr/bin/env python3
"""
hello-github-browser
Exemplo simples que imprime uma mensagem e a hora atual.
"""
from datetime import datetime

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Olá, GitHub! Commit feito pelo navegador.")
    print(f"Horário local: {now}")

if __name__ == "__main__":
    main()
