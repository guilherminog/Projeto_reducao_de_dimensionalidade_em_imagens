# Projeto_reducao_de_dimensionalidade_em_imagens
Realizando a implementação em Python para transformar uma imagem colorida para níveis de cinza (0 a 255) e para binarizada (0 e 255), preto e branco.



Redução de dimensão no espaço de cor: 

Espera-se usar o número reduzido de tons de cinza, preservando o máximo possível, o contraste da imagem original. Inevitavelmente há perdas de informação de cor. 


A redução de dimensionalidade é um processo que tem por objetivo diminuir o número de variáveis — ou dimensões — de um conjunto de dados (*dataset*) visando a menor perda de informações possível.



Há diversas razões pelas quais trabalhar com um dataset dotado de um número grande de features, isto é, com muitas dimensões, pode se configurar em uma desvantagem. Em primeira instância, vale ressaltar que quanto maior o número de features, maior também o número de amostras necessárias. Isso porque, nessa condição, é preciso um número maior delas para ter um dataset plural o suficiente para contemplar todas as possíveis combinações de features, a fim de possibilitar a construção de modelos generalistas. Este fenômeno é chamado de *Maldição da Dimensionalidade.*

As técnicas de redução de dimensionalidade têm vasta aplicação, já que podem ser utilizadas em qualquer contexto no qual haja dezenas, centenas ou até mesmo milhares de features a serem analisadas e processadas em um único conjunto de dados. Dados do mundo real, como sinais de fala, fotografias digitais ou imagens por ressonância magnética funcional (fMRI), geralmente possuem alta dimensionalidade e para manusear esses dados reais adequadamente, a sua dimensionalidade deve ser reduzida (VAN DER MAATEN; POSTMA; VAN DEN HERIK, 2009). Sendo assim, as técnicas de redução — lineares ou, mais recentemente, não lineares — são especialmente utilizadas para o processamento de sinais, reconhecimento de voz, neuroinformática e bioinformática.



Nesse projeto  usamos a imagem da Lena

![resultado.jpg](https://github.com/guilherminog/Projeto_reducao_de_dimensionalidade_em_imagens/blob/main/Projeto_reducao_de_dimensionalidade_em_imagens/img/resultado.jpg)





