# Veranstalter

## Organizador de pastas, porque as minhas estão uma bagunça...


```console
    python -m venv venv
```

### Windows

```bat
    venv\Scripts\activate
```

### Linux

```bash
    source venv/bin/activate
``` 

## Testes

- todo arquivo de teste deve ficar na pasta /tests na raiz do projeto
- toda classe de teste deve seguir o formato com Test****.py
- todo arquivo de teste deve seguir o formato **_test.py

```bash
    pytest tests
```

## Bibliotecas utilizadas
- [typer](https://typer.tiangolo.com/)
- [python-fsutil](https://pypi.org/project/python-fsutil/)
- [pytest](https://docs.pytest.org/en/stable/index.html)
- [pytest-mock](https://pypi.org/project/pytest-mock/)


## Exemplo de Comandos 

```bash
    python main.py organize organize-by-extension D:\downloads
```