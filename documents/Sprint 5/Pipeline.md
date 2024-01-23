## Pipeline de BigData na AWS

O pipeline de Big Data é um sistema complexo que abrange várias etapas, desde a coleta até a visualização de dados. Ele é projetado para processar, armazenar e analisar grandes volumes de informações, permitindo que as organizações tomem decisões informadas com base em dados.
Nesse contexto, a arquitetura proposta envolve diversos componentes e serviços da AWS (Amazon Web Services), cada um desempenhando um papel específico no fluxo de dados.

### Fluxo de dados
A primeira etapa, a fonte de dados, marca o ponto inicial do processo. Aqui, os dados são coletados de diversas fontes externas, como APIs, bancos de dados, arquivos CSV, e outros. A variedade de origens é ampla, incluindo informações sobre clientes, transações, vendas e dados governamentais, entre outros. Nesta fase, os dados brutos são adquiridos e preparados para a próxima etapa.


O conjunto de dados referente aos CNPJs, armazenado em formato CSV na Storage Account, é composto por registros oficiais sobre empresas no Brasil, categorizados pelo Código Nacional de Atividade Econômica (CNAE). Essas bases foram estrategicamente divididas em quatro partes, cada uma representando um subconjunto distinto de CNAEs. Outra fonte essencial é a Pesquisa de Orçamentos Familiares (POF) do IBGE, apresentada em formato CSV. Realizada a cada cinco anos, essa pesquisa detalhada visa coletar informações sobre os gastos e o padrão de vida das famílias brasileiras, proporcionando uma visão abrangente das mudanças nos hábitos de consumo e nas condições de vida da população. Além disso, a base de dados simulada de vendas fictícias, disponibilizada através de uma API em formato JSON, oferece transações diárias de um distribuidor fictício, conectando-se aos CNPJs previamente mencionados. Por fim, a base "Zip and Postal Codes of All Countries" em formato CSV, proveniente do Database Hub, fornece informações cruciais sobre códigos postais de todos os países, acompanhados de suas coordenadas geográficas, enriquecendo ainda mais o panorama de dados disponíveis.


Na segunda fase, ingestão de dados, os dados coletados são processados e encaminhados para o pipeline de ingestão. Isso é realizado por meio de scripts Python e AWS Lambda. Os dados são armazenados nos buckets S3 da AWS (Amazon Simple Storage Service), garantindo escalabilidade e durabilidade para futuras análises.
No processo de ETL (Extração, Transformação e Carga), a ingestão de dados é uma etapa crítica que visa preparar e armazenar as informações de forma adequada. Esses dados, muitas vezes heterogêneos em formato e qualidade, podem conter redundâncias e inconsistências.
Após a coleta, entra em cena a transformação de dados, uma fase crucial de limpeza e organização. A limpeza envolve a remoção de duplicatas e valores nulos, enquanto a transformação inclui a normalização e estruturação dos dados para facilitar análises futuras. Essa etapa é essencial para garantir a integridade e qualidade dos dados.
Os dados limpos e transformados são, então, carregados no AWS S3. O formato escolhido é o CSV, devido à sua simplicidade e interoperabilidade. O S3 atua como um repositório temporário e não estruturado, data lake, mantendo os dados acessíveis e prontos para transferência para o data warehouse.


O DataLake, como conceito centralizado de armazenamento, permite o processamento e uso de grandes volumes de dados em sua forma original. A escalabilidade e flexibilidade do AWS S3 tornam-no ideal para acomodar diversos tipos de dados, desde estruturados até não estruturados. Essas características, como escalabilidade, armazenamento de todos os dados e eliminação da gestão de servidores, tornam o serviço propício ao Data Lake.


Para as etapas de transformação e carga dos dados, a escolha recai sobre o uso de scripts Python. Essa decisão é respaldada pela facilidade de uso e manutenção, bibliotecas diretamente integradas às ferramentas AWS e Azure, além de portabilidade e interoperabilidade.


É relevante observar que, para dados provenientes da API do cliente, a ingestão ocorre de duas maneiras distintas. Dados mais antigos são adquiridos diretamente do API Gateway, sendo acionados pelo Lambda. Em contraste, dados diários são ingeridos por scripts Python e armazenados no bucket. O expurgo desses dados também é realizado pelo Lambda, conforme solicitação do parceiro, completando o ciclo de ingestão de forma eficiente e organizada.


No terceiro estágio, o armazenamento, os dados são transferidos para o AWS Redshift, um serviço de armazenamento de dados rápido e escalável. Cada tipo de dado (POF, CNPJ, CEP e API) possui seu próprio bucket S3 dedicado, organizando eficientemente as informações. O Redshift é otimizado para executar consultas complexas de forma ágil.
A arquitetura do Data Warehouse adota uma abordagem trifásica, composta pelas fases Worker, Raw e Trusted, para garantir a eficácia do processamento e armazenamento de dados. Na Fase Worker, que marca o início do pipeline de dados, ocorre a coleta inicial de dados brutos de diversas fontes, capturando-os em seu estado mais puro, sem tratamento prévio. Em seguida, na Fase Raw, os dados coletados são armazenados no Data Lake em seu formato original, proporcionando flexibilidade e atuando como um repositório temporário para grandes volumes de dados em diversas estruturas. A Fase Trusted, última etapa do pipeline, representa o momento em que os dados brutos passam por transformações e limpezas, sendo então carregados no Data Warehouse. Nesta fase, os dados estão estruturados e confiáveis, prontos para análises e relatórios.
No contexto do Data Warehouse, a utilização de views é fundamental. Essas views agem como representações virtuais de tabelas derivadas de uma ou mais fontes de dados, não armazenando dados fisicamente, mas facilitando consultas e manipulação de dados de maneira simplificada e eficiente.


A quarta fase, análise de dados, faz uso do Apache Spark para análises avançadas e processamento distribuído. Os dados são transformados e otimizados para consultas eficientes, enquanto análises exploratórias são realizadas para obter insights valiosos.
A utilização de modelos ensemble, como o Random Forest, no pipeline de Big Data é uma estratégia valiosa para aprimorar a precisão e o desempenho geral do sistema. O modelo ensemble combina as previsões de vários modelos mais simples, explorando a diversidade e complementaridade de cada um. Duas abordagens comuns são o "bagging", onde cada modelo é treinado em um conjunto de dados diferente e suas previsões são combinadas, e o "boosting", que treina modelos sequencialmente, concentrando-se em corrigir os erros dos modelos anteriores.


A implementação desses modelos ensemble no pipeline de Big Data oferece diversas vantagens. Primeiramente, busca-se equilibrar a variância e o viés dos modelos, proporcionando uma performance mais robusta. Além disso, esses métodos geralmente apresentam melhor desempenho, sendo mais robustos e complexos, com um custo computacional ligeiramente maior, mas com resultados superiores. Essa abordagem permite a adição de múltiplos vetores de preferência, enriquecendo a qualidade das análises ao observar comportamentos específicos em indivíduos com características semelhantes.


No contexto específico do pipeline, foram aplicados modelos como o algoritmo K-means, utilizado para agrupar dados em clusters, e o Random Forest, que cria várias árvores de decisão de maneira aleatória. A análise dos resultados inclui a visualização da distribuição de valores únicos em colunas específicas, a utilização do método do cotovelo para determinar o número ideal de clusters, a previsão de valores dos produtos pelo Random Forest e a avaliação dos resultados através do Mean Squared Error (Erro Quadrático Médio).


### Avaliação e validação dos resultados
A avaliação e validação dos resultados foram conduzidas de acordo com o CRISP-DM, um modelo padrão para projetos de análise de dados, composto por fases como a Compreensão do Negócio, Compreensão dos Dados, Preparação dos Dados, Modelagem, Avaliação e Implantação. Este modelo é iterativo, permitindo ajustes contínuos e refinamentos para garantir resultados desejados.
Na etapa de visualização, a ferramenta Metabase, conectada ao AWS Redshift, entra em cena. O Metabase permite a criação do infográfico, facilitando a análise de dados de maneira intuitiva.
Para atender às necessidades do parceiro, propõe-se a criação de um infográfico informativo e visualmente apelativo. A estratégia de visualização contempla diversas dimensões, cada uma respondendo a uma pergunta-chave sobre os consumidores e o mercado.


### Perguntas-chave sobre os consumidores e o mercado
A primeira pergunta, "Quem são meus clientes consumidores?", é abordada considerando diferentes aspectos. A distribuição de renda dos consumidores será apresentada destacando as faixas de renda mais prevalentes. Além disso, entende-se os gastos médios dos consumidores em diferentes momentos de consumo e os horários mais comuns.


A segunda pergunta, "Quais canais quero estar presente?", é explorada através de um gráfico de barras, onde cada barra representa um canal de compra, e a altura indica a preferência relativa dos consumidores.


A terceira pergunta, "Em quais geografias quero atuar?", tem suas informações visualizadas em um mapa geográfico, destacando as regiões desejadas para atuação. 


A quarta pergunta, sobre as dietas seguidas nos estados do país, é respondida através de um gráfico de mapa que destaca as dietas mais populares em diferentes regiões, padrões para representar os diferentes tipos de dietas.


A quinta pergunta, sobre os valores nutricionais dos alimentos consumidos no Brasil, será abordada por um gráfico de barras empilhadas. Cada barra representa uma unidade federativa, e as diferentes cores indicam os diversos componentes nutricionais.


Por fim, a sexta pergunta aborda a previsão de preço fornecida pelo modelo. Essa informação ressalta as tendências ou variações ao longo do tempo.
Já a última fase do pipeline aborda Segurança e Monitoramento. A segurança é mantida através do uso de TLS em várias partes do pipeline, e o AWS CloudWatch é empregado para monitorar métricas e logs, assegurando o desempenho e a confiabilidade do sistema.


No âmbito da segurança, foram minuciosamente considerados diversos aspectos para assegurar a integridade e atender aos requisitos da Lei Geral de Proteção de Dados (LGPD) no pipeline de Big Data. A criptografia desempenha um papel central nesse contexto, sendo aplicada de maneira estratégica.
Cada serviço é acessado somente por indivíduos autorizados, com autenticação necessária para garantir que apenas pessoas autorizadas tenham acesso aos recursos pertinentes. Tanto os consultores de Tech&Digital quanto os de Marketing e Vendas têm acesso restrito apenas às funcionalidades essenciais para suas atividades, fortalecendo a segurança global do sistema.


Essas medidas abrangentes, integradas em todas as fases do pipeline, não apenas preservam a confidencialidade dos dados sensíveis, mas também garantem a conformidade com regulamentações de privacidade. O compromisso com práticas robustas de segurança estabelece um ambiente confiável e protegido para o tratamento de dados críticos, consolidando a solução como uma base sólida para as operações da organização.
Em última análise, o pipeline de Big Data não apenas atende às necessidades atuais de análise de dados, mas também estabelece uma base sólida e adaptável para futuras evoluções. Sua abordagem iterativa e integrada, combinada com práticas sólidas de segurança, posiciona-o como uma solução robusta e confiável para impulsionar a tomada de decisões e insights estratégicos na organização.
