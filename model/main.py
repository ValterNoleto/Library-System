class Biblioteca:

    def __init__(self):
        self.livros = []
        self.funcionario = []
        self.emprestimos = []

    def cadastrarLivro(self, livro):
        self.livros.append(livro)

    def cadastrarFuncionario(self, funcionario):
        self.funcionario.append(funcionario)

    def validarFuncionario(self, funcionario):
        for func in self.funcionario:
            if func.cpf == funcionario.cpf:
                return True
        return False

    def realizarEmprestimo(self, funcionario, livro, usuario):
        if self.validarFuncionario(funcionario) and usuario.limite < 3:
            emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(emprestimo)
            usuario.limite += 1
            return "Emprestimo realizado com sucesso"
        return "Funcionario invalido"

    def realizarDevolucao(self, funcionario, livro, usuario):
        if self.validarFuncionario(funcionario):
            for emprestimo in self.emprestimos:
                if livro.id == emprestimo.livro.id:
                    self.emprestimos.remove(emprestimo)
                    usuario.limite -= 1
                    return "Devolucao realizada com sucesso"
            return "Devolucao nao realizada pois o livro n encontra-se emprestado"
        return "Funcionario invalido"


class Livro:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario:

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

class Usuario:

    def __init__(self, nome, endereco):
        self._limite = 0
        self.nome = nome
        self.endereco = endereco

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if self._limite + valor > 3 or self._limite + valor < 0:

            self._limite = valor
            raise "Limite maximo atigindo"
class Emprestimo:

    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro


if __name__ == "__main__":
    biblioteca = Biblioteca()
    livro = Livro("001", "Harry Potter")
    funcionario = Funcionario("45427950063", "Irvayne")
    
