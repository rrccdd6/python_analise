import pandas as pd
import tkinter as tk

# ler o arquivo Excel
df = pd.read_excel("dados_binance.xlsx")

# filtrar os dados para o símbolo (symbol) "BTCUSDT" ou qualquer outra crypto. Basta trocar o ticker
btc_df = df[df['symbol'] == 'BTCUSDT']

# criar a janela
window = tk.Tk()
window.title("Dados do Bitcoin das ultimas 24 horas")

# criar a tabela (preciso melhorar a tabela)
table = tk.Label(window, text=btc_df.to_string(index=False), justify='left', font=('Arial', 12))
table.pack()

# exibir a janela
window.mainloop()

## python3.10 analise_dados_cripto.py