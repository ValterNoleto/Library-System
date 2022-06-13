class Biblioteca:

    def __init__(self):
        self.livros = []
        self.funcionario = []
        self.emprestimos = []

    def cadastrarLivro(self, livro):
        self.livros.append(livro)

    def procurarLivro(self, livro):
        if livro in self.livros:
            return "Livro encontrado!"
        else:
            return "O livro procurado, não foi encontrado!"

    def cadastrarFuncionario(self, funcionario):
        self.funcionario.append(funcionario)

    def validarFuncionario(self, funcionario):
        for func in self.funcionario:
            if func.cpf == funcionario.cpf:
                return True
        return False

    def realizarEmprestimo(self, funcionario, livro, usuario):
        if self.validarFuncionario(funcionario):
            emprestimo = Emprestimo(usuario, livro)
            if len(self.emprestimos) < 3:
                self.emprestimos.append(emprestimo)
                return "Empréstimo realizado com sucesso!"
            else:
                return "O limite máximo de empréstimos foi atingido!"
        return "Funcionário inválido!"

    def realizarDevolucao(self, funcionario, livro):
        if self.validarFuncionario(funcionario):
            for emprestimo in self.emprestimos:
                if livro.id == emprestimo.livro.id:
                    self.emprestimos.remove(emprestimo)
                    return "Devolução realizada com sucesso!"
            return "A devolução não pôde ser concluída, o livro não foi emprestado!"
        return "Funcionário inválido!"


class Livro:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario:

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

class Usuario:

    def __init__(self, nome):
        self.nome = nome

class Emprestimo:

    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro