Este diretório permite gerar um pacote deb que se limita a instalar
alguns ficheiros em localizações pré-determinadas, de acordo com o
ficheiro debian/install.

Igual so sample-mergefiles-1.0.0 , mas é usado o source format
'3.0 (quilt)', isto é, tudo o que vem de upstream assume-se que foi
previamente montado a partir de uma tarball à parte.

É importante reter que, antes de chamar o dpkg-buildpackage, o
diretório final tem que ser montado, com um comando do tipo:
    tar xzvf ../sample-quilt-mergefiles-1.0.0.tar.gz
Só depois poderemos dar o devido:
    time LC_ALL=C dpkg-buildpackage -uc -us

Caso não o façamos, o dpkg-buildpackage entra em modo contra-mundum
e começa a reclamar que os ficheiros foram alterados à mão.

Isto é, o dpkg-buildpackage precisa de saber que estamos no modo
quilt, não para montar o pacote, mas sim para que possa verificar
se estamos a compilar o deb a partir de uma fonte correta, e para
nos ajudar a gerar os novos patches (ver flag --commit).
