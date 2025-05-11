from aluno import Aluno
from livro import Livro
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# test-drive

# criar biblioteca
bibif = Biblioteca('123', 'Rua A, 123')

# cadastrar alunos
aluno1 = Aluno('123', 'Gustavo Wagner')
aluno2 = Aluno('124', 'Yan Douglas')
aluno3 = Aluno('125', 'Kauã wanderley')
aluno4 = Aluno('126', 'Pedro torres')


bibif.cadastrar_aluno(aluno1)
bibif.cadastrar_aluno(aluno2)
bibif.cadastrar_aluno(aluno3)
bibif.cadastrar_aluno(aluno4)

print("=== Alunos Cadastrados ===")
bibif.imprimir_alunos()

# cadastrar livros

livro1 = Livro('123', 'Aprendendo Python', '978-3-16-148410-0', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro2 = Livro('124', 'Aprendendo Java', '978-3-16-148410-1', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro3 = Livro('125', 'Aprendendo C++', '978-3-16-148410-2', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro4 = Livro('126', 'Aprendendo JavaScript', '978-3-16-148410-3', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro5 = Livro('127', 'aprendendo JavaScript avançado', '978-3-16-148410-4', ['Kaua wanderley', 'Gustavo Wagner'], '2024-05-17', 'Tecnologia')
livro6 = Livro('128', 'aprendendo comutação', '978-3-16-148410-5', ['Kaua wanderley', 'Gustavo Wagner'], '2024-10-25', 'tecnologia')

bibif.cadastrar_livro(livro1)
bibif.cadastrar_livro(livro2)
bibif.cadastrar_livro(livro3)
bibif.cadastrar_livro(livro4)
bibif.cadastrar_livro(livro5)
bibif.cadastrar_livro(livro6)


print("\n=== Livros Cadastrados ===")
bibif.imprimir_livros()

# realizar empréstimo
emprestimo1 = Emprestimo(123, '2025-05-07', [livro1], aluno1, '2025-06-15')
emprestimo2 = Emprestimo(127, '2025-11-15', [livro5], aluno3, '2026-01-15')
emprestimo3 = Emprestimo(128, '2025-09-11', [livro6], aluno4, '2025-12-11')

bibif.realizar_emprestimo(emprestimo1)
bibif.realizar_emprestimo(emprestimo2)
bibif.realizar_emprestimo(emprestimo3)


print("\n=== Empréstimos Ativos ===")
bibif.imprimir_emprestimos_ativos()
