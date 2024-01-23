# 1. Curadoria dos dados

O presente documento é responsável por fornecer os insumos necessários à justificativa de escolha de base de dados utilizados para as posteriores análises no cubo de dados. Foram selecionados até 15GB de dados que auxiliam no principal objetivo: retirar insights sobre potencial de consumo por categoria, canal e região.

## 1.1. POF (Pesquisa de Orçamento Familiar)

A POF é a pesquisa que detalha informações sobre a composição dos gastos das famílias em todo o Brasil. Esta pesquisa é crítica para o projeto, porque pode fornecer insights sobre o comportamento do consumidor, preferências e padrões de gasto dentro do setor alimentício, ou seja, o perfil do consumidor. Ao analisar os dados da POF, é possível entender quais tipos de produtos alimentícios são mais populares entre diferentes grupos demográficos, quanto eles estão dispostos a gastar e como esses padrões variam em diferentes regiões. Isso ajudará na segmentação do mercado e no direcionamento mais eficaz de grupos específicos de consumidores.

## 1.2. CNPJ

A base de dados do CNPJ é uma rica fonte de informações sobre as empresas no Brasil. Para os clientes da consultoria, esta base de dados é essencial porque inclui informações sobre a localização, tamanho e tipo de cada negócio registrado. É possível usá-la para identificar concorrentes no setor alimentício, analisar a saturação do mercado em diferentes regiões e avaliar o potencial para novos negócios. Ao saber quantos e quais tipos de empresas do setor alimentício estão operando em uma região, é possível aconselhar melhor os clientes sobre onde podem existir lacunas no mercado ou áreas de alta concorrência.

## 1.3. CEP

A base de dados de CEPs (Códigos de Endereçamento Postal) do Brasil é extremamente relevante para o projeto de análise do potencial de consumo para o setor alimentício. Aqui estão os motivos:

1. **Geo-Referenciamento e Segmentação Regional** : CEPs permitem a localização precisa de estabelecimentos e consumidores. Isso é crucial para entender a distribuição geográfica dos clientes potenciais e para a segmentação de mercado baseada em localização. É possível identificar áreas com alta concentração de bares, restaurantes, supermercados ou quaisquer outros estabelecimentos e, assim, cruzar essas informações com dados de consumo e demográficos para identificar regiões com alto potencial de consumo.
2. **Logística e Distribuição** : A análise de CEPs pode ajudar a otimizar a logística de distribuição dos clientes. Entender onde estão localizados os estabelecimentos permite planejar rotas de entrega mais eficientes e reduzir custos operacionais. Isso é particularmente importante para empresas de alimentos e bebidas que dependem de entregas rápidas e frescor dos produtos.
3. **Análise de Mercado e Expansão** : Ao combinar dados de CEP com informações de consumo e dados demográficos, é possível identificar áreas não atendidas ou com demanda insatisfeita. Isso pode direcionar estratégias de expansão para os clientes, indicando onde novos estabelecimentos poderiam ter sucesso ou onde poderiam aumentar sua participação no mercado.
4. **Planejamento Urbano e Demanda Futura** : Os CEPs também são úteis para analisar tendências de crescimento urbano e desenvolvimento de novas áreas. Isso pode antecipar a demanda futura e ajudar os clientes a planejar estrategicamente a abertura de novos negócios ou a expansão de negócios existentes.

# 2. Análise dos dados

Para compreender melhor as bases de dados primeiramente selecionadas, foram feitas análises para compreender os dados disponíveis em cada base, ou seja, suas colunas, e o que elas significam, além de como seus valores estão distribuídos. A partir disso, foi possível analisar se elas seriam interessantes para aplicação no projeto, ou seja, vão de acordo e podem gerar insights interessantes ao objetivo de potencial de consumo por canal, categoria e região. Todas as análises estão disponíveis em: https://github.com/2023M8T4Inteli/grupo1/tree/main/src/Analise%20Exploratoria
As bases escolhidas estão na seção acima de 'Curadoria dos Dados'.

# 3. ETL (Extração, carregamento e transformação)

Também foram realizados ajustes nos scripts que realizam o carregamento dos dados para os buckets S3 (Data Lake). A fim de reduzir custos e facilitar o tratamento dos dados, foram adicionadas etapas em todos os scripts para a realização da transformação deles:

1) Tratamento de caracteres especiais e acentuações;
2) Preenchimento de nulos por vazios;
3) Transformação de separadores menos utilizados para ',' e
4) Aceitação de outros tipos de arquivos além de CSV, como XML e TXT.

Além disso, foi identificado na análise exploratória que diversos dados são categóricos e, visando a usabilidade final do cubo de dados, que será fonte principal para a criação de dashboards e infográficos pela equipe de Marketing & Vendas da Integration, também foi adicionada uma etapa de mapeamento para estes dados. Esse mapeamento, agora visando a usabilidade e praticidade para a equipe de Tech&Digital, responsável pela manutenção dos dados, é automatizada a partir de dicionários em arquivos CSV. Essa automação funciona a partir do nome do arquivo de dicionário e da coluna em que se deseja realizar o tratamento; por exemplo, para transformar os códigos das Unidades Federativas para seu nome, basta ter o arquivo CSV com o nome 'UF.csv', caso a coluna da tabela seja essa, que a transformação será feita.
Esse mapeamento foi realizado em todas as fontes de dados utilizadas (POF, CNPJ e CEP).

# 4. Views

## 4.1. Consumo Individual `(consumo_individual)`

Junção das tabelas de 'Despesa Individual (POF)' e 'Consumo Alimentar', com o intuito de visualizar como as despesas estão relacionadas ao consumo dos indivíduos. 

## 4.2. Características do Consumo `(caracteristica_consumo)`

Junção das tabelas 'Consumo Alimentar (POF)' e 'Características da Dieta (POF)' para entender os padrões de consumo e perfil dos consumidores, ou seja, como as dietas impactam no seu consumo, por região (estado).

## 4.3. CNPJs e Sales `(cnpj_union_view)`

Junção das 4 tabelas de 'CNPJs' e 'Sales' da API do cliente para obter insights relacionados às vendas do cliente nas Unidades Federativas do país

## 4.4. CNPJs, Sales e Category `(cnpj_union_view_category)`

Junção das 4 tabelas de 'CNPJs', 'Sales' da API do cliente e 'Category', também da API do cliente, para entender, além das vendas, as categorias em granularidade de Unidades Federativas do país em relação apenas ao que se refere ao cliente.

# 5. Modelos ensemble

Modelo ensemble é uma técnica em aprendizado de máquina que combina as previsões de vários modelos mais simples para melhorar a precisão e o desempenho geral do sistema. A ideia por trás dos modelos ensemble é aproveitar a diversidade e a complementaridade de vários modelos individuais para obter um desempenho mais robusto e generalizável.

Existem diferentes abordagens para implementar modelos ensemble, mas duas das mais comuns são o "bagging" e o "boosting".

- **Bagging (Bootstrap Aggregating):** No bagging, cada modelo é treinado em um conjunto de dados diferente, criado por meio de amostragem com reposição (bootstrap) do conjunto de dados original. Em seguida, as previsões de cada modelo são combinadas por votação (no caso de classificação) ou por média (no caso de regressão) para produzir a previsão final.
- **Boosting:** No boosting, os modelos são treinados sequencialmente, e cada novo modelo se concentra em corrigir os erros cometidos pelos modelos anteriores.

A utilização de um modelo ensemble em um pipeline de big data é benéfica por várias razões. Primeiro, os métodos ensemble são uma tentativa de encontrar um equilíbrio entre variância e viés. Alguns modelos, por suas peculiaridades matemáticas, possuem maior variância ou maior potencial de overfitting e obter um viés. Segundo, os métodos ensemble geralmente têm uma performance melhor. Eles são mais robustos e complexos, envolvem mais operações, com um custo computacional um pouco maior, mas que, geralmente, têm uma performance melhor. Terceiro, eles permitem a adição de uma multiplicidade de novos vetores de preferência, complementando e enriquecendo a qualidade das análises devido à observação de comportamentos específicos em indivíduos com características similares

## 5.1 Algoritmo K-means

O algoritmo **K-means** é um método de aprendizado não supervisionado que é usado para agrupar dados em clusters. Primeiro, é preciso definir um ‘K’, correspondente ao número de  agrupamentos que se deseja formar. Em seguida, define-se, de forma aleatória, um centroide para cada cluster. O centroide é basicamente o centro do cluster. O próximo passo é calcular, para cada ponto, a distância até o centroide mais próximo. Cada ponto será atribuído ao cluster do centroide mais próximo. Agora, reposiciona-se o centróide. A nova posição do centroide deve ser a média da posição de todos os pontos do cluster. Os dois últimos passos são repetidos, iterativamente, até que os centroides não mudem mais de posição.

Inicialmente, a fim de observar a relação entre os dados do dataframe, utiliza-se o comando**`feat_categorical_nunique.hist()`** para criar um histograma dos valores únicos na coluna. Este é um método para visualizar a distribuição de valores únicos na coluna.

![Histograma](https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/histograma.png)

Em seguida, utiliza-se o método cotovelo para determinar o número ideal de clusters em um conjunto de dados. Ao plotar o gráfico da inércia em função do número de clusters, o eixo x representa o número de clusters e o eixo y representa a inércia. O ponto onde a inércia começa a diminuir de forma linear é considerado o número ideal de clusters.

![Método do Cotovelo](https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Metodo_cotovelo.png)

A partir de tal análise, é possível compreender que alguns estados do país possuem tendências no valor das suas compras. A escolha da quantidade de cluster (k = 5), é justificável ao selecionar o entendimento de região de compra.

![Clusterização](https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/cluster.png)

## 5.2 Modelo Random Forest

A Floresta Aleatória é um método de aprendizado conjunto que faz parte dos métodos ensemble. Ele cria várias árvores de decisão de maneira aleatória. Cada árvore é utilizada na escolha do resultado final, em uma espécie de votação.

As árvores de decisão, ou Decision Trees, estabelecem regras para tomada de decisão. O algoritmo cria uma estrutura similar a um fluxograma, com “nós” onde uma condição é verificada, e se atendida o fluxo segue por um ramo, caso contrário, por outro, sempre levando ao próximo nó, até a finalização da árvore.

A abordagem do Random Forest é ao mesmo tempo mais precisa e mais robusta para mudanças nas variáveis preditoras do que uma única árvore de classificação ou regressão. Portanto, o Random Forest é uma forma de combinar vários modelos de machine learning em um único resultado.

O objetivo do modelo utilizado, alinhado ao projeto, é o de prever o valor com base nas colunas ‘id’ e ‘idcategoria’.

O Mean Squared Error (Erro Quadrático Médio) de aproximadamente 103818.88 indica que o modelo pode estar enfrentando dificuldades para ajustar-se bem aos dados de teste. Isso significa que as previsões do modelo estão, em média, afastadas dos valores reais por uma quantidade significativa, em termos quadráticos. 

As previsões [801.66, 725.04] para os novos dados indicam os valores previstos pelo modelo para os pontos de dados **`[1, 10]`** e **`[2, 15]`**. Os valores demonstrados pelo modelo são justificáveis pois foram utilizados os dados da API do parceiro, dado que, são dados criados aleatoriamente e podem não fazer sentido. Entretanto, é fundamental ressaltar que o modelo está estruturado para a utilização em dataframes reais.

## 5.3 Métodos de avaliação e validação com o CRISP-DM

O **CRISP-DM** (Cross Industry Standard Process for Data Mining) é um modelo padrão que define um processo estruturado e organizado para projetos de análise de dados. 

O modelo é composto por seis fases:

- **Compreensão do Negócio**[:](https://awari.com.br/crisp-dm/) Nesta fase, é feita uma definição clara do objetivo do projeto, dos recursos necessários e da estratégia para atingir os resultados esperados.
- **Compreensão dos Dados**: Os dados são coletados, limpos e organizados de forma apropriada.
- **Preparação dos Dados**: Nesta fase, os dados são preparados para a modelagem.
- **Modelagem**: São selecionados os modelos que serão utilizados na análise de dados.
- **Avaliação**: Os resultados são avaliados e refinados até que o modelo alcance o desempenho desejado.
- **Implantação**: A solução final é implementada e monitorada para garantir que está funcionando de acordo com o esperado.

O CRISP-DM é um modelo iterativo, ou seja, as etapas são realizadas em ciclos até que os resultados esperados sejam alcançados. Isso significa que, após a fase de implantação, a solução deve ser monitorada continuamente e refinada sempre que necessário. 

## 5.4 Proposta de otimização do modelo

Ao analisar os resultados do modelo inicial, identificamos oportunidades para otimização e melhoria do desempenho.

1. **Ajuste de Hiperparâmetros:**
    - **Objetivo:** O ajuste de hiperparâmetros envolve a modificação dos parâmetros do modelo que não são aprendidos durante o treinamento, mas influenciam o desempenho do modelo.
    - **Estratégia:** Testar diferentes valores para hiperparâmetros, como o número de estimadores na floresta (**`n_estimators`**), profundidade máxima das árvores (**`max_depth`**), entre outros. Isso pode ser feito usando técnicas como busca em grade (**`Grid Search`**) ou busca aleatória (**`Random Search`**).
2. **Engenharia de Recursos (Feature Engineering):**
    - **Objetivo:** Identificar e criar novas características que possam melhorar a capacidade do modelo de capturar padrões nos dados.
    - **Estratégia:** Avalia se há outras características no conjunto de dados ou se é possível criar novas características que possam ser mais informativas para a previsão da variável alvo ('value').
3. **Outros Algoritmos:**
    - **Objetivo:** Explorar diferentes algoritmos de aprendizado de máquina para determinar se algum deles se ajusta melhor ao seu conjunto de dados.
    - **Estratégia:** Experimentar outros modelos, como regressão linear, support vector machines, gradient boosting,
4. **Validação Cruzada:**
    - **Objetivo:** Avaliar o desempenho do modelo de uma maneira mais robusta, garantindo que ele generalize bem para dados não vistos.
    - **Estratégia:** Utilizar técnicas de validação cruzada, como k-fold cross-validation, para avaliar a performance do modelo em diferentes conjuntos de treino/teste.
  
Além disso, é essencial uma análise detalhada dos resultados de cada ajuste, assegurando uma iteração constante e refinada do modelo. Esta abordagem iterativa não apenas visa alcançar a máxima eficácia na previsão da variável alvo, mas também proporciona uma otimização progressiva, o que resulta em um modelo mais robusto e preciso ao longo do tempo.
  
# 6. Expurgo de dados do parceiro
Para realizar a exclusão de dados do cliente armazenados no Amazon Redshift de forma automatizada, foi projetada uma função Lambda com um gatilho configurado para executar o expurgo periodicamente. 

O propósito deste código é remover informações do cliente que não devem ser armazenadas no banco de dados para garantir a conformidade com políticas de proteção de dados. 

A função Lambda está associada a uma função IAM para conceder as permissões necessárias de interação com o Redshift e é responsável por executar a exclusão dos dados específicos. O expurgo pode ser acionado por meio de um gatilho configurável, como por exemplo, a chegada de novos dados.

A implementação deste código de expurgo foi uma demanda do próprio cliente pela necessidade de garantir que informações confidenciais, relacionadas aos seus parceiros, fossem excluídas de maneira regular e automática, respeitando assim as normativas de privacidade e proteção de dados.
