## Infográficos
   A criação de infográficos é uma prática do design e visualização de dados, que proporciona de uma maneira eficaz a transmissão de informações de forma clara, concisa e atraente. Nesta etapa, os infográficos foram desenvolvidos com o propósito de medir o potencial de consumo por canal, região e categoria. O foco principal é fornecer insights valiosos para a Integration, uma empresa de consultoria, para que possa tomar decisões mais informadas e estratégicas.

### Objetivos
  O desenvolvimento destes infográficos tem como objetivos principais fornecer uma análise detalhada e multifacetada sobre o potencial de consumo, canalizando informações específicas e insights acionáveis em várias dimensões. Primeiramente, buscamos assegurar uma Clareza de Objetivo nítida: é fundamental que os infográficos sejam imediatamente compreensíveis, destacando sem ambiguidades as informações críticas acerca do potencial de consumo, englobando categorias, canais e regiões específicas.
  
  Em seguida, nosso foco se direciona para a Análise de Canal, Região e Venda, onde o intuito é proporcionar uma visão holística do desempenho dos canais de venda em diferentes regiões. Esta análise é vital para identificar tanto oportunidades quanto desafios existentes, permitindo uma melhor adaptação e estratégia de mercado. Paralelamente, colocamos ênfase no Estado por Consumo Alimentício, oferecendo uma análise especializada sobre os padrões de consumo alimentar. Este aspecto visa destacar as variações significativas de consumo entre os estados, oferecendo uma perspectiva mais granular e específica.
  
  Além disso, é de grande importância a apresentação de dados sobre a Renda Total, que se relaciona diretamente ao potencial de consumo. Esta visão permite uma compreensão mais aprofundada da capacidade financeira das regiões, sendo um indicador chave para a tomada de decisão estratégica. Ademais, planejamos incorporar um Perfil do Consumidor por Estado, utilizando um gráfico de teia (spider web) para uma representação visual e intuitiva do perfil do consumidor em diferentes estados, levando em conta uma variedade de atributos relevantes.
  
  Por fim, reconhecemos a importância de uma Avaliação Contínua e aprimoramento dos infográficos. Entendemos que estes são recursos dinâmicos, que devem evoluir constantemente para refletir mudanças e tendências de mercado. Essa avaliação contínua tem como objetivo identificar tanto os pontos fortes quanto os fracos dos infográficos atuais, assegurando sua eficácia e valor contínuo para a Integration. Este processo de aperfeiçoamento contínuo é crucial para manter os infográficos como ferramentas valiosas e relevantes para a análise de mercado.


### Gráficos gerados no Metabase
   A análise de dados é uma prática que visa a compreensão de padrões, tendências e oportunidades em diferentes conjuntos de dados. Neste contexto, após as análises iniciais com os infográficos no Power Bi, novos gráficos foram gerados no ambiente Metabase, utilizando correlações de dados e SQL, em que foi possível criar visualizações intuitivas e acessíveis, facilitando a interpretação e a extração de insights. Este conjunto diversificado de infográficos abrange dados provenientes de bases públicas e dados da API do cliente.

   
### Infográficos Criados no Metabase
  Os gráficos gerados no Metabase foram baseados nas VIEWs criadas no Redshift, a partir dos modelos Ensemble.
  
  O link a seguir permite a visualização na plataforma:http://ec2-52-3-247-124.compute-1.amazonaws.com/dashboard/2-go-to-market-zero-acucar
  
  Abaixo estão descritos seus objetivos:

  
  1) O gráfico "Consumo Total por Região" é uma ferramenta poderosa para analisar o volume de consumo em diferentes áreas geográficas. Ele permite às empresas identificar mercados com alta demanda, otimizando estratégias de distribuição e marketing.

  
  2) O "Dieta mais frequente por Estado" oferece uma visão clara das tendências alimentares regionais, ajudando a moldar ofertas de produtos conforme os hábitos locais de consumo, o que é crucial para o planejamento de estratégias de mercado segmentadas.
  
  3) O gráfico "Média de Consumo por Dia da Semana e Tipo de Despesa" revela os padrões de consumo em diferentes dias da semana, divididos por categorias de despesa. Este insight é vital para planejar promoções e ajustar operações para atender às variações na demanda.
  
  4) O "Média de Despesa por Horário de Consumo" fornece uma análise detalhada dos gastos dos consumidores em diferentes momentos do dia, permitindo a otimização de horários de funcionamento e promoções.
  
  5) "Média de gasto por Categoria" e "Média do Valor de Compra por Estado" destacam as preferências de consumo e o poder de compra em várias regiões, oferecendo informações valiosas para estratégias de precificação e distribuição de produtos.
  
## Relatório de Análise de Eficácia dos Infográficos
  Teste de Usabilidade com feedback do usuário: Durante a última sprint retrospective, dia 08/12/2023, o cliente pode ter a primeira visualização do infográfico e pudemos coletar vários feedbacks positivos e negativos. O cliente achou a navegação intuitiva e clara, mas apontou áreas de confusão em gráficos onde as barras estavam supostamente todas com mesmo tamanho, legendas de colunas e etc; Em 'Sugestões de Melhoria' será destacado onde é necessário e interessante de ocorrer mudanças na entrega do infográfico. Em geral, as avaliações revelaram uma satisfação, mas será preciso personalizar e processar (limpar) alguns dados para uma melhor navegação dentro da ferramenta.

#### Sugestões de Melhoria:
Pensando sobre o visual da infográfico foi apontado a necessidade de facilitar a visualização dos dados nos gráficos. A seguir é apresentado o que é/seria interessante ser alterado em cada gráfico.

**Gráfico 1 - Mapa de maior venda em cada estado**

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final1.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar um título à legenda das cores pois gerou confusão ao identificar o que estava sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de vendas gerais pelo estado.


**Gráfico 2 - Venda de carne por tempo**

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final2.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar uma linha que indica a média do número de vendas para facilitar a visualização de outliers.


**Gráfico 3 - Média de despesa por horário de consumo**

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final3.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar uma linha que indica a média de despesa e facilitar a visualização de outliers.


**Gráfico 4 - Refeições mais realizadas**

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final4.png" width="700"/> <br>
</div>


Ponto de melhoria: Melhorar a escrita da legenda da coluna Y (número de refeições). Como são números grandes ficam difíceis de visualizar e acabam poluindo o design.


**Gráfico 5 - Categoria mais vendida**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final5.png" width="700"/> <br>
</div>


Ponto de melhoria: Facilitar a visualização da diferença de tamanho entre as barras. Pode ser feito retirando talvez a coluna 'outros'.


**Gráfico 6 - Quantidade consumida por hora**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final6.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar uma linha que indica a média de quantidade consumida para facilitar a visualização de outliers.


**Gráfico 7 - Consumo por local de refeição em dias atípicos**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final7.png" width="700"/> <br>
</div>


Ponto de melhoria: Melhorar a escrita da legenda da coluna Y (Total de consumo). Como são números grandes ficam difíceis de visualizar e acabam poluindo o design. Além disso, estudar se é necessário manter as colunas que estão muito pequenas como 'restaurante a quilo' ou 'não identificado', talvez deixar só 3 colunas principais.


**Gráfico 8 - Média de valor de compra por estado**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final8.png" width="700"/> <br>
</div>


Ponto de melhoria: Retirar a coluna 'EX' pois não faz sentido para análises de território brasileiro. Além disso é necessário destacar de alguma forma quais seguem a média e quais se sobressaem, pode-se fazer isso com uma linha talvez. Por outro lado, pode se imaginar de adicionar mais um filtro dentro deste mesmo gráfico, criando clusters de padrões por estado, por exemplo colunas que estiverem da mesma cor consomem mais carne e colunas de outra cor consomem mais notebooks.


**Gráfico 9 - Tipo de dieta por estado**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final9.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar um título à legenda das cores pois gerou confusão ao identificar o que estava sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de consumo geral pelo estado.

**Gráfico 10 - Tipo de dieta por estado**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final10.png" width="700"/> <br>
</div>

**Gráfico 11 - Tipo de dieta por estado**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final11.png" width="700"/> <br>
</div>

**Gráfico 12 - Tipo de dieta por estado**


<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/final12.png" width="700"/> <br>
</div>


Ponto de melhoria: Adicionar um título à legenda das cores pois gerou confusão ao identificar o que estava sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de consumo geral pelo estado.

Ponto de melhoria: Adicionar um título à legenda das cores pois gerou confusão ao identificar o que estava sendo exposto pelas cores. Por exemplo, indicar que quanto mais escuro o tom de vermelho, maior é o número de consumo geral pelo estado.


### Conclusão
  Em conclusão, o cliente gostou da entrega e achou que temos que aprimorar no tratamento e limpeza dos dados durante a criação dos gráficos até a próxima e última entrega. As sugestões propostas visam otimizar a experiência do usuário, garantindo que o infográfico cumpra de maneira efetiva seu propósito de facilitar a criação de estratégias Go-to-market. A implementação dessas melhorias promoverá um impacto significativo, proporcionando aos usuários uma ferramenta mais eficaz e personalizada para a análise de informações complexas e massivas.
