# Arquitetura da Solução

A arquitetura de dados é concebida para suportar um fluxo contínuo e eficiente de informações. Com base nos dados fornecidos pelo cliente, os requisitos identificados incluem:

- **Cubo de Informações**: Estruturado para acumular dados como o total de CNPJs, número de clientes atendidos, transações de vendas e potencial de mercado.
- **Automatização do Pipeline**: Configuração de um pipeline de dados automatizado para processamento e análise contínuos.
- **Data Lake**: Criação de um Data Lake estruturado para armazenar dados em grande escala.
- **Streaming de Dados**: Implementação de um fluxo de dados baseado em streaming para dados específicos, visando a redução do ruído informacional e a eficiência na transmissão de dados.
- **Preparação de Dados**: Desenvolvimento de um pipeline de dados dedicado à preparação e transformação de informações, alinhando-as aos objetivos do projeto.
- **Governança de Dados**: A API do cliente é projetada para não armazenar informações diretamente no cubo de dados, mantendo a governança e segurança das informações.
- **Análise Histórica**: Capacidade de analisar dados históricos ao longo de uma década.
- **Flexibilidade do Pipeline**: Construção e incremento facilitados do pipeline para acomodar novas fontes de dados e mudanças nos requisitos de negócios.
- **Visualização**: Disponibilização de ferramentas de visualização para interpretar informações diretamente dos dados armazenados.
- **Atualizações Anuais**: Estratégia para atualizar os dados anualmente conforme novas informações governamentais são disponibilizadas.
- **Segurança**: Implementação de autenticações de segurança robustas para proteger os dados em todas as fases do fluxo.

![Arquitetura da Sprint 3](../../assets/Arquitetura_S3.png)

    Arquitetura de Ingestão Sprint 3 (Fonte: Confecção própria)

A arquitetura projetada, ilustrada no diagrama anexo, proporciona um ciclo de vida completo dos dados, desde a coleta até a visualização, integrando uma variedade de serviços AWS para maximizar a eficiência e a escalabilidade.

## Componentes da Arquitetura

1. **API do cliente**: Essa API atua como ponto de entrada para os dados. A "API do cliente" aceita dados enviados por clientes.
2. **CSVs**: São formatos de arquivo que contêm dados tabulares. Os dados são melhores descritos na Análise Exploratória da seção abaixo.
3. **Script Python**: são aplicados para processar dados de várias fontes abertas, incluindo POF, INEP, Open DataSUS, MEC, ZipCode, além de CNPJs e também dos dados da API do cliente, preparando-os para o upload no S3. Além disso, um script específico é aplicado no Lambda para processar os dados mais recentes do cliente a cada determinado período de tempo.
4. **Bucket S3**:  é um serviço de armazenamento de objetos oferecido pela Amazon Web Services que oferece escalabilidade, disponibilidade de dados, segurança e performance. Ele organiza dados em 'buckets', que funcionam como contêineres básicos onde os dados são armazenados, e dentro dos quais são gerenciados através de chaves únicas (identificadores de objeto). Além disso, possui alta escalabilidade em termos de quantidade de dados armazenados e quantidade de solicitações por segundo, atendendo a necessidades de aplicações de todos os tamanhos. O Bucket S3 será utilizado para o armazenamento de Data Lake dos dados.
5. **Lambda**: é um serviço de computação sem servidor que executa código em resposta a eventos e gerencia automaticamente os recursos de computação necessários. Ele é responsável por disparar funções de processamento de dados em resposta a eventos específicos, como uploads de dados da API para o RedShift. Além disso, escala automaticamente ao processar cada evento individual, garantindo que a carga de trabalho seja gerenciada sem intervenção manual e executa códigos sem a necessidade de provisionar ou gerenciar servidores, o que reduz a complexidade e o custo de operação.
6. **Spark**: Apache Spark é uma plataforma para processamento de dados em grande escala. Os dados do DynamoDB podem ser importados para o Spark para análises avançadas, processamento distribuído e aplicação de métodos ensamble.
7. **AWS Quicksight**: Uma vez processados e analisados, os dados são encaminhados para o AWS Quicksight para visualização. Quicksight é uma ferramenta de business intelligence da AWS que permite criar infográficos e visualizações interativas.
8. **VPC (Virtual Private Cloud)**: Representa um ambiente isolado na AWS onde todos esses serviços e operações estão ocorrendo. Isso garante que os dados e serviços sejam seguros, isolados de outros recursos e facilmente gerenciáveis.
9. **AWS CloudWatch**: Implementado para o monitoramento contínuo dos logs e da telemetria, assegurando a disponibilidade e integridade dos dados.
10. **AWS Redshift**: O AWS Redshift é um serviço de armazenamento de dados rápido, escalável e totalmente gerenciado da Amazon Web Services, projetado especificamente para análise de grandes volumes de dados. A escolha do Redshift para um cubo de dados OLAP (Online Analytical Processing) é baseada em várias de suas características e capacidades que o tornam apropriado para essa finalidade:

* **Desempenho de Consulta** : Otimizado para executar consultas complexas rapidamente, permitindo análises de dados eficientes.
* **Escalabilidade** : Capacidade de expandir recursos conforme a necessidade de processamento e armazenamento de dados aumenta.
* **Gerenciamento Simplificado** : Automatiza tarefas operacionais, facilitando o gerenciamento de data warehouses.
* **Integração com Ferramentas de BI** : Conecta-se facilmente com ferramentas de Business Intelligence para visualização e análise de dados.
* **Custo-Eficiência** : Oferece um modelo de pagamento flexível, adequado para orçamentos variados.
* **Segurança Robusta** : Inclui recursos avançados de segurança para proteger dados.
* **Conformidade Regulatória** : Adere a padrões de conformidade, essencial para setores regulados.
* **Análise Multidimensional** : Suporta a criação de cubos OLAP para uma análise de dados rica e multidimensional.
* **Insights Profundos** : Habilita as organizações a extrair insights valiosos dos seus dados para informar a tomada de decisão estratégica.

Além disso, foram considerados aspectos de segurança, a fim de garantir a integridade e LGPD aos dados:
1.**Criptografia de dados em trânsito**: Como os dados de CNPJ e POF são de fontes governamentais, portanto públicas, não é necessário criptografá-los até chegarem no Dynamo DB, onde se juntam aos dados do cliente. A criptografia em trânsito é feita com o protocolo TLS.
2.**Criptografia de dados em repouso**: Todos os serviços que usam os dados do cliente devem ser configurados com opções de criptografia selecionadas, portanto AWS Lambda, Dynamo, Apache Spark e AWS Quicksight.
3.**Grupos de acesso**: Cada serviço deve ser acessado por pessoas autorizadas, ou seja, devem possuir a autenticação para seu devido acesso. Visto que tanto consultores de Tech&Digital, quanto de Marketing e Vendas se beneficiarão com a solução, cada um deve ter o acesso restrito à apenas sua necessidade na solução.
5.**AWS Key Managment Service**: Para controlar os acessos, é utilizado o serviço da AWS.

## Análise exploratória

- Base dos [dados.org](http://dados.org/) - Base dos Dados

**Organização sem fins lucrativos - GitHub -** “Base dos Dados” é uma organização sem fins lucrativos que tem como missão universalizar o acesso a dados de qualidade para todos. Eles fornecem uma variedade de dados, incluindo estimativas populacionais, dados geográficos, informações sobre educação básica, inflação, Produto Interno Bruto (PIB).

- IBGE Dados Abertos - Dados Abertos | IBGE

**Governamentais - CSV -** “Dados Abertos | IBGE” é uma iniciativa do Instituto Brasileiro de Geografia e Estatística (IBGE) que visa promover a transparência e a acessibilidade dos dados coletados pelo instituto. O IBGE é uma das principais fontes de dados estatísticos sobre o Brasil, fornecendo informações valiosas em diversas áreas, como demografia, economia, geografia.

- POF (pesquisa orçamento familiar - POF 2017-2018 | IBGE

**Governamentais - CSV -** A Pesquisa de Orçamentos Familiares (POF) é um levantamento realizado pelo Instituto Brasileiro de Geografia e Estatística (IBGE) no Brasil. A POF tem como objetivo coletar informações detalhadas sobre os gastos e o padrão de vida das famílias brasileiras. O levantamento é conduzido a cada 5 anos, o que permite ao IBGE monitorar e analisar as mudanças nos hábitos de consumo e nas condições de vida da população.

- RAIS e CAGED Microdados - Microdados RAIS e CAGED — Ministério do Trabalho e Emprego ([www.gov.br](https://colab.research.google.com/corgiredirector?site=http%3A%2F%2Fwww.gov.br))

**Governamentais - CSV -** RAIS (Relação Anual de Informações Sociais) é um sistema de informação criado pelo Ministério do Trabalho e Emprego (atualmente incorporado ao Ministério da Economia) que reúne dados das empresas e estabelecimentos empregadores no Brasil. Já o CAGED (Cadastro Geral de Empregados e Desempregados**)** é outro sistema relacionado ao mercado de trabalho brasileiro, também mantido pelo Ministério da Economia. Ele é utilizado para registrar as admissões e demissões de empregados sob o regime da Consolidação das Leis do Trabalho (CLT).

- Receita Federal Dados Abertos - Dados Abertos — Receita Federal ([www.gov.br](https://colab.research.google.com/corgiredirector?site=http%3A%2F%2Fwww.gov.br))

**Governamentais - CSV -** Os "Dados Abertos" disponibilizados pela Receita Federal se referem a informações e conjuntos de dados que a Receita Federal do Brasil torna disponíveis ao público em geral para consulta e uso. Esses dados abertos geralmente incluem informações relacionadas a tributação, arrecadação, cadastros de contribuintes, normas fiscais e outros aspectos relacionados à administração fiscal e aduaneira no Brasil.

**Governamentais - CSV -** Dados Abertos MEC é um sistema de informação mantido pelo Ministério da Educação que oferece diversos dados sobre a educação no Brasil.

- Dados Abertos - MEC - Página inicial ([www.gov.br](https://www.gov.br/))

**Governamentais - CSV -** Dados Abertos INEP é um sistema do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira que reúne microdados educacionais detalhados.

- Microdados — Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira | Inep ([www.gov.br](https://www.gov.br/))

**Governamentais - CSV -** Open Data SUS é uma plataforma mantida pelo Ministério da Saúde que disponibiliza dados abertos relacionados à saúde no Brasil.

- Bem vindo - OPENDATASUS ([saude.gov.br](https://datasus.saude.gov.br/))

**Internacionais - CSV -** From-to Zip Code to Lat-Long é uma base de dados que oferece informações sobre códigos postais de todos os países e suas respectivas coordenadas geográficas.

- ✉️ Zip and Postal Codes of All Countries | Database Hub ([back4app.com](https://back4app.com/))

**CNPJs - CSV -** Storage Account com as bases de CNPJ é um conjunto de dados que provêm de registros oficiais sobre empresas no Brasil, categorizados pelo Código Nacional de Atividade Econômica (CNAE). As bases foram divididas em quatro partes, cada uma representando um subconjunto distinto de CNAEs:

- CNPJs - Parte 1 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_1.csv))
- CNPJs - Parte 2 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_2.csv))
- CNPJs - Parte 3 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_3.csv))
- CNPJs - Parte 4 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_4.csv))

**CNPJs - CSV -** Estes dados são derivados de registros oficiais de empresas, especificamente relacionados aos CNPJs e categorizados pelo Código Nacional de Atividade Econômica (CNAE):

- CNPJs - Parte 1 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_1.csv))
- CNPJs - Parte 2 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_2.csv))
- CNPJs - Parte 3 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_3.csv))
- CNPJs - Parte 4 ([cnpjlake.blob.core.windows.net](https://cnpjlake.blob.core.windows.net/cnpjbases/cnpjs_4.csv))

**API - JSON -** BASE DE VENDAS FICTÍCIA VIA ENDPOINT INTEGRATION é uma base de dados simulada que representa as transações de vendas de um distribuidor fictício. Esta base é disponibilizada através de um endpoint específico e é formatada em JSON, uma linguagem leve de intercâmbio de dados de fácil leitura para humanos e máquinas. O conteúdo deste dataset é atualizado diariamente, incorporando novas vendas que são associadas a alguns dos CNPJs listados anteriormente, e se concentra nas categorias de produtos de interesse. Esta simulação serve para testes, análises e desenvolvimento sem comprometer dados reais ou sensíveis.

## Anexos

![Arquitetura Sprint 1](../../assets/Arquitetura_S1.png)
					Arquitetura da Sprint 1 (Fonte: Confecção própria)

![Arquitetura Sprint 2](../../assets/Arquitetura_S2.png)
					Arquitetura da Sprint 2 (Fonte: Confecção própria)
