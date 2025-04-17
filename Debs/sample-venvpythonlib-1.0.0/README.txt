Exemplo de geração de pacote deb para uma biblioteca python que se
instala dentro de um virtualenv previamente criado.

Fonte em formato nativo.

Antes de gerar o deb, criar o virtualenv com o comando:
    sudo /usr/bit/python3.11 -m venv /opt/thizizavenv/

Depois de gerar e instalar o pacote, experimentar:
    /opt/thizizavenv/bin/python3 -c "import samplepythonlibmodules ; samplepythonlibmodules.printhings()"
    # Deverá responder "Things".
    /bin/python3 -c "import samplepythonlibmodules ; samplepythonlibmodules.printhings()"
    # Deverá dar erro de pacote não encontrado.
