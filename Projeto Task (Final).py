import tkinter as tk
from tkinter import messagebox

# Lista de tarefas
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa.strip() == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa válida.")
    else:
        tarefas.append({"tarefa": tarefa, "status": "pendente"})
        entrada.delete(0, tk.END)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")

# Atualiza a lista na interface
def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for i, item in enumerate(tarefas):
        texto = f"{i + 1}. {item['tarefa']} - {item['status']}"
        lista_tarefas.insert(tk.END, texto)

# Conclui tarefa selecionada
def concluir_tarefa():
    selecionado = lista_tarefas.curselection()
    if selecionado:
        indice = selecionado[0]
        tarefas[indice]["status"] = "concluída"
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")

# Remove tarefa selecionada
def remover_tarefa():
    selecionado = lista_tarefas.curselection()
    if selecionado:
        indice = selecionado[0]
        tarefas.pop(indice)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

# ------------------ Interface ------------------

janela = tk.Tk()
janela.title("TaskTerminal - Lista de Tarefas")
janela.geometry("400x400")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, width=30, font=("Arial", 12))
entrada.pack(pady=10)

# Botões
btn_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

btn_concluir = tk.Button(janela, text="Concluir Tarefa", command=concluir_tarefa)
btn_concluir.pack(pady=5)

btn_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(pady=5)

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=50, height=10, font=("Arial", 10))
lista_tarefas.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()
