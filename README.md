# Criador de Grupos
> Um programa que sortea grupos de qualquer tamanho, para a realização de trabalhos, dinâmicas e afins.


O Criador de Grupos foi idealizado e criado pela turma de calouros do Curso ADS1B - Noite da Faculdade Impacta.

O intuito do programa é randomizar a criação de squads com base nos criterios definidos pelo usuario, facilitando e simplificando a utilização de grupos dentro do ambiente de estudos. Além de incentivar a diversidade, engajamento e colaboração entre os alunos. 


## Instalação

Necessario python 3 ou superior instalado no equipamento.

Com o python instalado, clone ou baixe o repositorio em seu computador.

## Exemplo de uso

Abra o arquivo 'nomes.txt' e adicione os nomes desejados, respeitando sempre a regra de 1 (um) nome por linha

Após adicionar os nomes salve o arquivo.

Execute o programa 'lista_random.py' e siga as instruções que aparecem.

Ao termino da execução os grupos são formados e salvos no arquivo 'grupos.txt'.

## Configuração para Desenvolvimento

Descreva como instalar todas as dependências para desenvolvimento e como rodar um test-suite automatizado de algum tipo. Se necessário, faça isso para múltiplas plataformas.

```sh
make install
npm test
```

## Histórico de lançamentos

* 0.1.0
    * Adicionado melhorias ao codigo
    * Alterado o sistema de imput/output para arquivos.txt
    * Adicionado a função de escolha do numero de pessoas em cada grupo
* 0.0.1
    * Primeira versão funcional

## Meta

Em construção

## Contributing

1. Faça o _fork_ do projeto
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_