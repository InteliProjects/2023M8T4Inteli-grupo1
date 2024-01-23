# 1. Infográficos Iniciais

## 1.1 Introdução

&emsp;&emsp; A criação de infográficos é uma prática do design e visualização de dados, que proporcinoa de uma maneira eficaz a transmissão de informações de forma clara, concisa e atraente. Nesta etapa, os infográficos foram desenvolvidos com o propósito de medir o potencial de consumo por canal, região e categoria. O foco principal é fornecer insights valiosos para a Integration, uma empresa de consultoria, para que possa tomar decisões mais informadas e estratégicas.

## 1.2 Objetivos

&emsp;&emsp;O desenvolvimento destes infográficos tem como objetivos principais fornecer uma análise detalhada e multifacetada sobre o potencial de consumo, canalizando informações específicas e insights acionáveis em várias dimensões. Primeiramente, buscamos assegurar uma **Clareza de Objetivo** nítida: é fundamental que os infográficos sejam imediatamente compreensíveis, destacando sem ambiguidades as informações críticas acerca do potencial de consumo, englobando categorias, canais e regiões específicas.

&emsp;&emsp;Em seguida, nosso foco se direciona para a **Análise de Canal, Região e Venda**, onde o intuito é proporcionar uma visão holística do desempenho dos canais de venda em diferentes regiões. Esta análise é vital para identificar tanto oportunidades quanto desafios existentes, permitindo uma melhor adaptação e estratégia de mercado. Paralelamente, colocamos ênfase no **Estado por Consumo Alimentício**, oferecendo uma análise especializada sobre os padrões de consumo alimentar. Este aspecto visa destacar as variações significativas de consumo entre os estados, oferecendo uma perspectiva mais granular e específica.

&emsp;&emsp;Além disso, é de grande importância a apresentação de dados sobre a **Renda Total**, que se relaciona diretamente ao potencial de consumo. Esta visão permite uma compreensão mais aprofundada da capacidade financeira das regiões, sendo um indicador chave para a tomada de decisão estratégica. Ademais, planejamos incorporar um **Perfil do Consumidor por Estado**, utilizando um gráfico de teia (spider web) para uma representação visual e intuitiva do perfil do consumidor em diferentes estados, levando em conta uma variedade de atributos relevantes.

&emsp;&emsp;Por fim, reconhecemos a importância de uma **Avaliação Contínua e Aprimoramento** dos infográficos. Entendemos que estes são recursos dinâmicos, que devem evoluir constantemente para refletir mudanças e tendências de mercado. Essa avaliação contínua tem como objetivo identificar tanto os pontos fortes quanto os fracos dos infográficos atuais, assegurando sua eficácia e valor contínuo para a Integration. Este processo de aperfeiçoamento contínuo é crucial para manter os infográficos como ferramentas valiosas e relevantes para a análise de mercado.

## 1.3 Gráficos iniciais com o Power BI

&emsp;&emsp;Através de um conjunto diversificado de gráficos disponíveis no [PDF](https://github.com/2023M8T4Inteli/grupo1/blob/main/documents/Sprint%204/infograficos_iniciais.pdf), aprimoramos significativamente a compreensão das bases de dados públicos escolhidas (CNPJs, POF e CEP) e da API Cliente - Sale. Esses gráficos facilitam o entendimento de cada base, destacando informações que podem ser decisivas ou irrelevantes na construção dos infográficos finais.

&emsp;&emsp;Primeiramente, na **Base POF**, temos gráficos variados, como o *Gráfico de Barras de Renda Total por Unidade de Federação*, que visa demonstrar a distribuição da renda em diferentes estados. Outro exemplo é a *Tabela com o Local de Aquisição*, mostrando a quantidade de compras em diferentes locais. O *Filtro por Estado* permite uma visualização personalizada, enquanto o *Cartão com o Total de Renda Bruta* oferece uma visão geral da renda, com a opção de filtrar por região.

&emsp;&emsp;Além disso, há gráficos que analisam a forma de aquisição, a situação do domicílio entre rural e urbano, e até a distribuição por cor ou raça. A idade e o ano de nascimento dos indivíduos são exibidos em gráficos de linhas, enquanto os padrões de consumo durante a semana e as ocasiões de consumo são detalhados em gráficos de barras.

&emsp;&emsp;Já na **Base de Dados API Cliente - Sale**, os gráficos incluem *Gráficos de Barras* com a contagem de produtos mais vendidos por categoria, permitindo identificar os itens mais populares. Um *Gráfico de Linhas de Série Temporal* ilustra padrões de venda de produtos ao longo do tempo, e um *Cartão com o Total de Vendas* destaca o volume de vendas. Um Filtro por *Categoria* é providenciado para análises mais específicas.

&emsp;&emsp;Cada um desses gráficos desempenha um papel crucial na análise, ajudando a identificar tendências, padrões e insights. Eles são ferramentas essenciais para a compreensão profunda das bases de dados, auxiliando na determinação de quais informações são relevantes para a construção dos infográficos finais, assegurando que as decisões baseadas nesses dados sejam tão informadas e precisas quanto possível.

# 2. Gráficos gerados no Metabase

## 2.1 Introdução

&emsp;&emsp; A análise de dados é uma prática que visa a compreensão de padrões, tendências e oportunidades em diferentes conjuntos de dados. Neste contexto, após as análises iniciais com os infográficos no Power Bi, novos gráficos foram gerados no ambiente Metabase, utilizando correlações de dados e SQL, em que foi possível criar visualizações intuitivas e acessíveis, facilitando a interpretação e a extração de insights. Este conjunto diversificado de infográficos abrange dados provenientes de bases públicas e dados da API do cliente.

## 2.1 Infográficos Criados no Metabase

&emsp;&emsp;Os gráficos gerados no Metabase foram baseados nas VIEWs criadas no Redshift, a partir dos modelos ensemble. Abaixo estão descritos seus objetivos:

&emsp;&emsp;1) O gráfico "Consumo Total por Região" no é uma ferramenta poderosa para analisar o volume de consumo em diferentes áreas geográficas. Ele permite às empresas identificar mercados com alta demanda, otimizando estratégias de distribuição e marketing.

&emsp;&emsp;2) O "Dieta mais frequente por Estado" oferece uma visão clara das tendências alimentares regionais, ajudando a moldar ofertas de produtos conforme os hábitos locais de consumo, o que é crucial para o planejamento de estratégias de mercado segmentadas.

&emsp;&emsp;3) O gráfico "Média de Consumo por Dia da Semana e Tipo de Despesa" revela os padrões de consumo em diferentes dias da semana, divididos por categorias de despesa. Este insight é vital para planejar promoções e ajustar operações para atender às variações na demanda.

&emsp;&emsp;4) O "Média de Despesa por Horário de Consumo" fornece uma análise detalhada dos gastos dos consumidores em diferentes momentos do dia, permitindo a otimização de horários de funcionamento e promoções.

&emsp;&emsp;5) "Média de gasto por Categoria" e "Média do Valor de Compra por Estado" destacam as preferências de consumo e o poder de compra em várias regiões, oferecendo informações valiosas para estratégias de precificação e distribuição de produtos.

## 2.2 Relatório de Análise de Eficácia dos Infográficos

&emsp;&emsp;Teste de Usabilidade com feedbeck do usuário :
Durante a última sprint retrospective, dia 08/12/2023, o cliente pode ter a primeira visualização do infográfico e pudemos coletar vários feedbecks positivos e negativos. O cliente achou a navegação intuitiva e clara, mas apontou áreas de confusão em gráficos onde as barras estavam supostamente todas com mesmo tamanho, legendas de colunas e etc; Em 'Sugestões de Melhoria' será destacado onde é necessário e interessante de ocorrer mudanças na entrega do infográfico. Em geral, as avaliações revelaram uma satisfação, mas será preciso personalizar e processar (limpar) alguns dados para uma melhor navegação dentro da ferramenta.

&emsp;&emsp;Sugestões de Melhoria:

Pensando sobre o visual da infográfico foi apontado a necessidade de facilitar a visualização dos dados nos gráficos. A seguir é apresentado o que é/seria interessante ser alterado em cada gráfico.

&emsp;&emsp;Gráfico 1 - Mapa de maior venda em cada estado

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico_1mapa.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Adicionar um título a legenda das cores pois gerou confusão ao identificar o que estavam sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de vendas gerais pelo estado. 

&emsp;&emsp;Gráfico 2 - Venda de carne por tempo

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico2.jpg" width="900"/> <br>
</div>


&emsp;&emsp;Ponto de melhoria: Adicionar uma linha que indica a média do número de vendas para facilitar a vislualização de outliers.


&emsp;&emsp;Gráfico 3 - Média de despesa por horário de consumo

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico3.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Adicionar uma linha que indica a média de despesa facilitar a vislualização de outliers.


&emsp;&emsp;Gráfico 4 - Refeições mais realizadas

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico4.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Melhorar a escrita da legenda da coluna y (número de refeições). Como são números grandes ficam difíveis de visualizar e acabam poluindo o design.


&emsp;&emsp;Gráfico 5 - Categoria mais vendida

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico5.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Facilitar a visualização da diferença de tamanho entre as barras. Pode ser feito retirando talvez a coluna 'outros'.

&emsp;&emsp;Gráfico 6 - Quantidade consumida por hora

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico6.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Adicionar uma linha que indica a média de quantidade consumida para facilitar a vislualização de outliers.


&emsp;&emsp;Gráfico 7 - Consumo por local de refeição em dias atípicos

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico7.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Melhorar a escrita da legenda da coluna y (Total de consumo). Como são números grandes ficam difíveis de visualizar e acabam poluindo o design. Além disso, estudar se é necessário manter as colunas que estão muito pequenas como 'restaurante a quilo' ou 'não identificado', talvez deixar só 3 colunas principais.

&emsp;&emsp;Gráfico 8 - Média de valor de compra por estado

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico8.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Retirar a coluna 'EX' pois não faz sentido para análises de terrítório brasileiro. Além disso é necessário destacar de alguma forma quais seguem a média e quais se sobresaem, pode-se fazer isso com uma linha talvez. Por outro lado, pode se imaginar de adcionar mais um filtro dentro deste mesmo gráfico, criando clusters de padrões por estado, por exemplo colunas que estiverem da mesma cor consomem mais carne e colunas de outra cor consomem mais notebooks.

&emsp;&emsp;Gráfico 9 - Tipo de dieta por estado

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/grafico9.jpg" width="900"/> <br>
</div>

&emsp;&emsp;Ponto de melhoria: Adicionar um título a legenda das cores pois gerou confusão ao identificar o que estavam sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de consumo geral pelo estado. 


&emsp;&emsp;Em conclusão, o cliente gostou da entrega e achou que temos que aprimorar no tratamento e limpeza dos dados durante a criação dos gráficos até a próxima e última entrega. As sugestões propostas visam otimizar a experiência do usuário, garantindo que o infográfico cumpra de maneira efetiva seu propósito de facilitar a criação de estratégias Go-to-market. A implementação dessas melhorias promoverá um impacto significativo, proporcionando aos usuários uma ferramenta mais eficaz e personalizada para a análise de informações complexas e massivas.

