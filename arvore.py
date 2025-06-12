import tkinter as tk
from tkinter import messagebox

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)
        return no

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None:
            return None
        if valor < no.valor:
            no.esquerda = self._remover(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            sucessor = self._minimo(no.direita)
            no.valor = sucessor.valor
            no.direita = self._remover(no.direita, sucessor.valor)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar(no.esquerda, valor)
        else:
            return self._buscar(no.direita, valor)

    def em_ordem(self):
        return self._em_ordem(self.raiz)

    def _em_ordem(self, no):
        if no:
            return self._em_ordem(no.esquerda) + [no.valor] + self._em_ordem(no.direita)
        return []

    def pre_ordem(self):
        return self._pre_ordem(self.raiz)

    def _pre_ordem(self, no):
        if no:
            return [no.valor] + self._pre_ordem(no.esquerda) + self._pre_ordem(no.direita)
        return []

    def pos_ordem(self):
        return self._pos_ordem(self.raiz)

    def _pos_ordem(self, no):
        if no:
            return self._pos_ordem(no.esquerda) + self._pos_ordem(no.direita) + [no.valor]
        return []

class ArvoreGUI:
    def __init__(self, root):
        self.arvore = ArvoreBinariaBusca()
        self.root = root
        self.root.title("Árvore Binária de Busca - GUI")

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.btn_inserir = tk.Button(root, text="Inserir", command=self.inserir)
        self.btn_inserir.pack()

        self.btn_remover = tk.Button(root, text="Remover", command=self.remover)
        self.btn_remover.pack()

        self.btn_buscar = tk.Button(root, text="Buscar", command=self.buscar)
        self.btn_buscar.pack()

        self.btn_em_ordem = tk.Button(root, text="Em Ordem", command=self.mostrar_em_ordem)
        self.btn_em_ordem.pack()

        self.btn_pre_ordem = tk.Button(root, text="Pré-Ordem", command=self.mostrar_pre_ordem)
        self.btn_pre_ordem.pack()

        self.btn_pos_ordem = tk.Button(root, text="Pós-Ordem", command=self.mostrar_pos_ordem)
        self.btn_pos_ordem.pack()

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

    def inserir(self):
        try:
            valor = int(self.entry.get())
            if valor == 8:
                messagebox.showinfo("Parar", "Valor 8 digitado. Inserção finalizada.")
                return
            self.arvore.inserir(valor)
            self.entry.delete(0, tk.END)
            self.redesenhar()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro.")

    def remover(self):
        try:
            valor = int(self.entry.get())
            self.arvore.remover(valor)
            self.entry.delete(0, tk.END)
            self.redesenhar()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro.")

    def buscar(self):
        try:
            valor = int(self.entry.get())
            encontrado = self.arvore.buscar(valor)
            msg = "Valor encontrado." if encontrado else "Valor não encontrado."
            messagebox.showinfo("Busca", msg)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro.")

    def mostrar_em_ordem(self):
        valores = self.arvore.em_ordem()
        messagebox.showinfo("Em Ordem", f"{valores}")

    def mostrar_pre_ordem(self):
        valores = self.arvore.pre_ordem()
        messagebox.showinfo("Pré-Ordem", f"{valores}")

    def mostrar_pos_ordem(self):
        valores = self.arvore.pos_ordem()
        messagebox.showinfo("Pós-Ordem", f"{valores}")

    def redesenhar(self):
        self.canvas.delete("all")
        if self.arvore.raiz:
            self._desenhar_no(self.arvore.raiz, 400, 30, 200)

    def _desenhar_no(self, no, x, y, espaco):
        if no is None:
            return
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="lightblue")
        self.canvas.create_text(x, y, text=str(no.valor))

        if no.esquerda:
            self.canvas.create_line(x, y+15, x - espaco, y + 70 - 15)
            self._desenhar_no(no.esquerda, x - espaco, y + 70, espaco // 2)

        if no.direita:
            self.canvas.create_line(x, y+15, x + espaco, y + 70 - 15)
            self._desenhar_no(no.direita, x + espaco, y + 70, espaco // 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArvoreGUI(root)
    root.mainloop()
# arvore.py