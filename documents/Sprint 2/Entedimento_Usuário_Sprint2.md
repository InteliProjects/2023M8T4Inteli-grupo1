# 2. Entendimento do Usuário

&emsp;&emsp;No âmbito empresarial, o entendimento do usuário é um componente fundamental para o sucesso de qualquer empreendimento. Compreender as necessidades, preferências e comportamentos dos usuários não apenas orienta o desenvolvimento de produtos e serviços, mas também influencia diretamente as estratégias de marketing, vendas e a experiência geral do cliente. Nesta seção, exploraremos a importância desse entendimento aprofundado, destacando como ele impacta positivamente as operações e o relacionamento entre a empresa e seus consumidores.

## 2.1 Personas

&emsp;&emsp;Personas é uma técnica comum de pesquisa de mercado e design de experiência do usuário (UX), que tem como função o entendimento das necessidades, desejos, objetivos e comportamentos de um determinado grupo de pessoas. Com esse conhecimento, os desenvolvedores conseguem criar soluções mais adequadas, já que é possível entender melhor as dores, comportamentos e motivações dos usuários. <br>

### 2.1.1 Persona 1: Juliana Santos

&emsp;&emsp;Abaixo tem-se a primeira persona: Juliana Santos, uma profissional de marketing e vendas determinada na empresa de consultoria Integration. Ela enfrenta grande desafios em lidar com grande volume de dados no dia-a-dia da empresa, que por conta da alta quantidade de dados, acaba não conseguindo ter uma boa análise aprofundada, ou seja, há muitas informações que acabam ficando dispersas por conta do alto volume de dados. Sendo assim, há uma grande falta de insights detalhados para suas estratégias. Portanto, suas necessidades incluem acesso a dados detalhados sobre o consumo, insights valiosos para direcionar suas estratégias e acesso rápido a dados relevantes para tomar decisões informadas em tempo real. Logo, deseja ter uma ferramenta que proporcione uma visualização mais personalizada sobre os dados. `<br>`
`<img src=./assets/Persona1_Mod8.png>`

&emsp;**Dores:**

- Dificuldade em lidar com informações dispersas e falta de insights detalhados para direcionar estratégias de marketing e vendas eficazes.
- Falta de acesso rápido a dados relevantes para tomar decisões informadas.

&emsp;**Necessidades:**

- Precisa de acesso a dados detalhados sobre o consumo em diferentes categorias e canais, de forma a compreender o mercado em profundidade;
- Obter insights valiosos obtidos a partir da análise de dados, que podem apoiar suas estratégias de marketing e vendas;
- Precisa de acesso rápido a dados relevantes, permitindo tomar decisões em tempo real para aproveitar oportunidades ou responder a desafios de mercado.

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Persona1_Mod8.png" width="500"/>
</div>

### 2.1.2 Persona 2: Augusto Ribeiro

&emsp;&emsp;Abaixo tem-se a segunda persona: Augusto sempre teve uma ótima visão de negócio e se aprimorou ainda mais após ter iniciado sua jornada na Integration Consulting. Porém com o passar do tempo ele notou que sentia falta de estar mais próximo da área de tecnologia. Atualmente está atuando na equipe de Tech & Digital onde ele consegue juntar seus conhecimentos de negócio criando novas ferramentas tecnológicas e ajustar as já existentes que auxiliam o trabalho dos consultores da Integration.`<br>`

&emsp;**Dores:**

- Gasto de tempo em atividades repetitivas;
- Desorganização pelo uso de muitas planilhas;
- Falta de tempo para automatizar processos;
- Pouca eficiência e sofisticação ao criar soluções para consultores de Marketing e vendas;
- Abandono de dados na criação de soluções;
- Consultores com pouco contato com tecnologias de dados;

&emsp;**Necessidades:**

- Aumentar produtividade ao automatizar processos repetitivos;
- Diminuir o uso de planilhas de Excel;
- Aumentar a robustez ao criar soluções para os consultores;
- Facilitar a procura de dados;
- Criar interface didática para uso dos consultores;
- Flexibilidade da ferramenta para uso com diferentes tipos de dados;
- Compatibilidade com outras ferramentas tecnológicas;

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Persona2.png" width="500"/>
</div>

## 2.2 User Stories

User stories desempenham um papel crucial na construção de projetos. Elas oferecem uma abordagem centrada no usuário para definir funcionalidades, garantindo que as soluções desenvolvidas sejam verdadeiramente relevantes e atendam às necessidades reais dos usuários. Ao utilizar linguagem simples e direta, as user stories facilitam a comunicação entre todos os envolvidos no projeto, desde desenvolvedores até stakeholders, criando um entendimento compartilhado do que precisa ser alcançado. Esta clareza ajuda a evitar mal-entendidos e retrabalhos, otimizando o processo de desenvolvimento. Além disso, por representarem as funcionalidades do sistema, elas guiam a organização da equipe em relação às Sprints, sendo divididas em tarefas no quadro Kan Ban e produzidas dentro de uma sprint. Dessa maneira, foram desenvolvidas 14 user stories para as personas descritas acima: Consultor de Marketing e Vendas e Consultor de Tech&Digital.

| Número                   | User story 1                                                                                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de marketing e vendas                                                                                                                                                                                   |
| História                 | Eu, como consultor de marketing e vendas, quero visualizar dados sobre a localização geográfica dos nossos potenciais clientes, seus segmentos de mercado e informações sobre concorrentes.                  |
| Critérios de Aceitação | 1. O sistema deve categorizar clientes por localização geográfica (cidade, estado, país) e segmento de mercado.<br />2. O sistema deve fornecer gráficos dos canais de venda com base nos dados de clientes. |
| Testes de Aceitação     | 1. Verificar se o sistema destaca os canais de venda ao inserir dados de clientes.<br />2. Confirmar a categorização automática de um novo cliente no painel de controle.                                      |

| Número                   | User story 4                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                                                                                                                                                                                                                    |
| História                 | Eu, como consultor de Tech&Digital, quero integrar uma solução automatizada para acessar e analisar dados rapidamente.                                                                                                                                                                                                                                                                                     |
| Critérios de Aceitação | 1. O sistema deve oferecer uma interface intuitiva que permita a visualização de dados através de dashboards interativos e outros formatos relevantes.<br />2. O sistema deve mostrar métricas de desempenho do processo de coleta de dados. <br />3. O sistema deve demonstrar uma redução significativa no tempo necessário para buscar e processar os dados, quando comparado ao método anterior. |
| Testes de Aceitação     | 1. Comparar o tempo de coleta e análise de dados antes e depois da implementação.<br />2. Confirmar a visualização de dados através de dashboards. <br />3. Verificar as métricas de desempenho apresentadas pelo sistema.                                                                                                                                                                            |

| Número                   | User story 5                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor Tech&Digital                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| História                 | Eu, como consultor Tech&Digital, quero um sistema que me forneça uma compreensão clara e objetiva dos propósitos e metas do projeto, para que possa alinhar minhas análises e decisões de forma mais eficaz.                                                                                                                                                                                                                                         |
| Critérios de Aceitação | 1. O sistema deve integrar uma funcionalidade de automatização na coleta e leitura de dados, evitando retrabalhos e falhas manuais.<br /> 2. O sistema deve ser adaptável e aceitar diferentes formatos de dados do cliente, permitindo uma inserção sem complicações. <br />3. A plataforma deve possuir um módulo ou seção dedicada a apresentar, de forma clara e concisa, os objetivos e metas do projeto.                                  |
| Testes de Aceitação     | 1. Ao acessar o sistema, o consultor deve ser capaz de identificar facilmente os objetivos e metas do projeto sem necessidade de busca extensiva.<br />2. Ao inserir diversos formatos de dados do cliente, o sistema deve processá-los sem erros e de forma eficiente. <br />3. Ao ativar a funcionalidade de automatização, o sistema deve realizar a coleta e leitura de dados sem intervenção manual e apresentar os resultados em tempo hábil. |

| Número                   | User story 6                                                                                                                                                                                                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor Tech&Digital                                                                                                                                                                                                                                                                        |
| História                 | Como consultor Tech&Digital, desejo um sistema que priorize a segurança e a conformidade dos dados, garantindo que as informações sensíveis do cliente não sejam armazenadas no cubo de dados, a fim de manter a integridade e cumprir com as regulamentações de governança de dados. |
| Critérios de Aceitação | 1. Qualquer dado sensível ou identificável do cliente inserido no sistema não deve ser retido ou armazenado no cubo de dados sem criptografia.                                                                                                                                             |
| Testes de Aceitação     | 1. Ao inserir dados sensíveis do cliente, realizar uma busca no cubo de dados após um período estabelecido e confirmar a criptografia desses dados.                                                                                                                                        |

| Número                   | User story 7                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                                                                                                                                                                             |
| História                 | Eu, como consultor de Tech&Digital, quero que o sistema acelere a busca e análise de dados no processo "go to market".                                                                                                                                                                                                                                               |
| Critérios de Aceitação | 1. O sistema deve possuir algoritmos avançados para análises rápidas sem comprometer a precisão.<br />2. A plataforma deve fornecer resultados de análise em no máximo 3 minutos.<br />3. A solução deve incluir ferramentas de automação que reduzam o esforço manual na coleta e processamento de dados.                                               |
| Testes de Aceitação     | 1. Comparar o tempo médio gasto na busca e análise de dados antes e após a implementação do sistema.<br />2. Submeter um conjunto de dados ao sistema e verificar o tempo necessário para receber os resultados.<br />3. Utilizar a automação do sistema para coletar e processar dados e monitorar a eficiência em relação ao método manual anterior. |

| Número                   | User story 8                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                                                                                                                                                                                                       |
| História                 | Como consultor Tech&Digital, quero que o sistema suporte a integração nativa com plataformas de visualização como PowerBI e permita a execução e aplicação de scripts Python, possibilitando análises mais aprofundadas e visualizações personalizadas dos dados.                                                                                                                    |
| Critérios de Aceitação | 1. O sistema deve possuir uma API ou interface que permita a fácil integração com PowerBI e outras ferramentas de visualização.<br />2. A plataforma deve ter um ambiente seguro onde scripts Python possam ser carregados e executados.<br />3. As visualizações e análises criadas através dessas integrações devem ser precisas e refletir os dados reais do sistema.           |
| Testes de Aceitação     | 1. Importar um conjunto de dados para o PowerBI a partir do sistema e criar uma visualização para confirmar a integração.<br />2. Carregar e executar um script Python que processe e analise um conjunto de dados do sistema.<br />3. Comparar os resultados da análise e visualização criados através das integrações com os dados originais do sistema para garantir precisão. |

| Número                   | User story 9                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Persona                   | Consultor de Marketing e Vendas                                                                                                                                                                                                                                                                                                                                                                                                            |
| História                 | Como consultor de marketing e vendas, quero que o sistema identifique e categorize onde os potenciais clientes mais frequentemente realizam suas compras, permitindo uma compreensão detalhada dos canais de venda, áreas geográficas e segmentos de cliente para que possamos ajustar e focar nossa estratégia de marketing de forma mais eficaz.                                                                                     |
| Critérios de Aceitação | 1. O sistema deve coletar e processar dados de compras de potenciais clientes.<br />2. Deve oferecer visualizações geográficas claras que destaquem áreas de alta concentração de vendas.<br />3. O sistema deve ser capaz de segmentar clientes com base em comportamentos de compra e categorias de produtos.<br />4. Precisa identificar, listar e classificar os canais de venda mais populares entre os potenciais clientes. |
| Testes de Aceitação     | 1. Inserir dados de compras e verificar se o sistema categoriza corretamente os canais de venda.<br />2. Visualizar um mapa que destaca as áreas geográficas com maior concentração de compras.<br />3. Analisar segmentos de clientes para confirmar a correta segmentação baseada em comportamento e categorias de produtos.                                                                                                    |

| Número                   | User story 10                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                     |
| História                 | Como consultor de Tech&Digital, quero garantir a autenticação adequada no sistema para proteger os dados sensíveis dos clientes.                                                                           |
| Critérios de Aceitação | 1. O sistema deve exigir autenticação para acesso.<br />2. Os dados do cliente não devem ser armazenados permanentemente no storage após a análise.                                                     |
| Testes de Aceitação     | 1. Tentar acessar o sistema sem autenticação e verificar se o acesso é negado.<br />2. Verificar se os dados do cliente são removidos automaticamente do armazenamento após a análise ser concluída. |

| Número                   | User story 11                                                                                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                                                                                                    |
| História                 | Como consultor de Tech&Digital, quero garantir que o sistema seja ágil e eficiente na coleta e análise de dados, permitindo-nos tomar decisões em tempo hábil.                                                                                                                           |
| Critérios de Aceitação | 1. O sistema deve processar solicitações em menos de 5 minutos.<br />2. As análises de dados devem ser concluídas em um tempo definido.                                                                                                                                                 |
| Testes de Aceitação     | 1. Medir o tempo de resposta do sistema durante diferentes solicitações e analisar se passam de 5 minutos.<br />2. Medir o tempo necessário para a conclusão das análises de dados e verificar se passa de 5 minutos.<br />3. Avaliar a precisão dos dados coletados e processados. |

| Número                   | User story 12                                                                                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor Tech&Digital                                                                                                                                                                               |
| História                 | Como consultor de Tech&Digital, desejo ter a capacidade de atualizar automaticamente os dados sempre que o governo lançar novos dados, assegurando que nossas análises estejam sempre atualizadas. |
| Critérios de Aceitação | 1. O sistema deve permitir a inserção automática de novos dados.<br />2. O sistema deve validar a integridade dos dados inseridos.                                                               |
| Testes de Aceitação     | 1. Inserir novos dados automaticamente e verificar se são aceitos.<br />2. Tentar inserir dados inválidos e garantir que o sistema os recuse.                                                    |

| Número                   | User story 13                                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Épico                    | Integração e Interoperabilidade                                                                                                                                                                   |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                           |
| História                 | Como consultor de Tech&Digital, desejo que o sistema seja compatível com diferentes plataformas e bancos de dados, a fim de maximizar a flexibilidade e eficiência na coleta e análise de dados. |
| Critérios de Aceitação | 1. O sistema deve ser compatível com diferentes bancos de dados NoSQL e SQL.<br />2. O sistema deve garantir a integridade dos dados ao integrar com diferentes plataformas..                     |
| Testes de Aceitação     | 1. Integrar o sistema com diferentes bancos de dados e verificar a compatibilidade.<br />2. Verificar a integridade dos dados após a integração com diferentes plataformas.                     |

| Número                   | User story 14                                                                                                                                                                                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persona                   | Consultor de Tech&Digital                                                                                                                                                                                                                                                               |
| História                 | Como consultor de Tech&Digital, quero que o sistema permita a migração de um serviço cloud para outro de forma simples e eficiente, para garantir flexibilidade e otimização de custos conforme as necessidades da empresa.                                                        |
| Critérios de Aceitação | 1. O sistema deve suportar a integração com múltiplos provedores de serviços cloud.<br />2. O sistema deve garantir a integridade e segurança dos dados durante a migração.<br />3. A migração deve ser realizada sem interrupções significativas ou tempo de inatividade. |
| Testes de Aceitação     | 1. Integrar o sistema com diferentes provedores de serviços cloud e confirmar a compatibilidade.<br />2. Confirmar a integridade dos dados após a migração.<br />3. Monitorar o tempo de inatividade durante a migração e garantir que esteja dentro de um limite aceitável   |

## 2.3 Jornada do usuário

A Jornada do Usuário é uma representação visual das etapas que um usuário percorre ao interagir com um produto ou serviço, incluindo desde o primeiro contato com a solução até a conclusão de suas tarefas ou objetivos. Ela descreve o passo a passo percorrido, detalhando todos os pontos de contato e interações do ponto de vista do usuário, seus sentimentos e sensações em cada fase. Por mapear realmente como é a experiência do usuário, ela é essencial para identificar áreas de melhoria e criar soluções mais intuitivas e centradas no usuário.

Segue jornada do usuário produzida a partir das personas e user stories apresentadas anteriormente:

Para melhor visualização, segue o link: https://miro.com/app/board/uXjVNU1a7B0=/?share_link_id=523674542118
#### 1º Jornada do Usuário
- Persona: Augusto Ribeiro, Tech Digital
<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Jornada_do_Usuário.png" width="900"/>
</div>

#### 2º Jornada do Usuário
- Persona: Juliana Santos, Consultora de Marketing e Vendas
<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Jornada_do_Usu%C3%A1rio_2.png" width="860"/>
</div>

## 2.4 Wireframe 

&emsp;&emsp;O processo de desenvolvimento de um dashboard eficaz é essencial para proporcionar uma experiência de usuário intuitiva e informativa. Antes de qualquer codificação ou design final, a etapa inicial envolve a criação de wireframes. Estes esboços esquemáticos servem como uma representação visual preliminar do layout, estrutura e disposição de gráficos e infográficos no dashboard. Nesta seção, apresentaremos o nosso wireframe antes do nosso design final, o qual possui um design que mostra quais serão os principais dados para o desenvolvimento do nosso projeto.

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Wireframe_1.png" width="900"/>
</div>

<div align="center">
<img src="https://github.com/2023M8T4Inteli/grupo1/blob/main/assets/Wireframe_2.png" width="900"/>
</div>

Para melhor visualização, segue o link: https://www.figma.com/file/c6xWg8T5VXaamlURXYTpMT/wireframe-doc?type=whiteboard&node-id=0-1&t=wiPYqSl1WMNprcXz-0

**1. KPI’s** - A técnica de design de páginas que segue o padrão de leitura em "Z" é uma abordagem que otimiza a disposição do conteúdo. Ela acompanha a trajetória natural dos olhos durante a leitura, iniciando no canto superior esquerdo e se movendo em um padrão em "Z". Com esta técnica, os KPIs são estrategicamente posicionados no início da página para chamar atenção imediatamente, facilitar a rápida compreensão e direcionar o foco do usuário para as informações essenciais. Os KPIs são enfatizados para oferecer uma visibilidade imediata das métricas mais importantes, permitindo que a equipe concentre sua atenção e esforços nas áreas mais críticas para o sucesso do negócio. Isso ajuda a manter o foco na estratégia geral da empresa. Além disso, a apresentação clara e concisa dos KPIs facilita a rápida compreensão por todos os membros da equipe, independentemente de seu nível de experiência ou conhecimento técnico.<br>

**2. Filtro** - Os filtros em dashboards proporcionam personalização e flexibilidade, permitindo aos usuários ajustar a visualização de dados conforme suas necessidades. Essa funcionalidade facilita a análise dinâmica, o foco em dados relevantes, a identificação de problemas, a adaptação a diferentes públicos, a melhoria da usabilidade, o aumento da eficiência e o suporte à tomada de decisões informadas. Em resumo, os filtros aprimoram a utilidade e a experiência do usuário em dashboards, tornando a interação com os dados mais eficaz e personalizada.<br>

- **2.1. Filtro de Lugar** - Durante a Lean Inception, identificamos algumas necessidades da Intergation. Uma delas foi a necessidade de ter os dados geográficos mais detalhados possíveis. Isso permitirá que eles criem estratégias mais diretas e tenham alvos específicos para suas consultorias de mercado.<br>
    
- **2.2. Filtro de tempo** - Essa funcionalidade proporciona uma visão dinâmica e personalizada dos dados, sendo essencial para a compreensão temporal e identificação de padrões.<br>
   
- **2.3. Filtros Gerais** - Outras necessidades observadas incluem a habilidade de filtrar dados por tipo de Canais. No caso deste projeto, todos são do ramo alimentício, como mercados, restaurantes, etc. Também é necessário filtrar por tipo de CNAE, categorias de produto e tipo de consumo. Assim a Integration terá como personalizar quais dados são mais importantes para suas análises específicas.<br>
    
**3. Possíveis gráficos** <br>

- 3.1. Identificar o número de CNPJs por canal/região é crucial para localizar potenciais clientes do produto e garantir uma estratégia eficiente de "go to market" (entrada no mercado). Em outras palavras, o número de CNPJs por canal/região possibilita uma abordagem mais personalizada para atender às necessidades de cada cliente. As diferentes regiões podem apresentar demandas e preferências distintas, portanto, adaptar a oferta às características específicas dessas regiões pode ser uma estratégia eficaz.<br>
    
- 3.2. Os cinco canais em maior quantidade na região ajuda a empresa entender onde a demanda pelos canais são mais concentradas. Isso permite direcionar esforços de marketing e vendas para esses canais específicos, maximizando o alcance aos clientes potenciais.<br>
    
- 3.3. Entender as vendas por canal e renda da região é importante para adaptar estratégias de vendas e marketing, o que permite a personalização de ofertas, ajuste de preços por local/região e alinhamento com as preferências de cada segmento de mercado. Essa análise possibilita uma alocação eficiente de recursos, maximizando assim, o retorno sobre o investimento em cada canal e região.<br>
    
- 3.4. Os dados sobre o consumo por categoria/canal, possibilita que a empresa consiga adaptar estoques, distribuição e também estratégias de marketing. Essa análise pode identificar tendências e aprimorar a experiência do cliente. Além disso, aloca os recursos de uma maneira mais estratégica, promovendo competitividade e eficiência operacional.<br>
    
- 3.5. Entender as vendas por canal e renda da região é importante para adaptar estratégias de vendas e marketing, o que permite a personalização de ofertas, ajuste de preços por local/região e alinhamento com as preferências de cada segmento de mercado. Essa análise possibilita uma alocação eficiente de recursos, maximizando assim, o retorno sobre o investimento em cada canal e região.<br>
    
- 3.6. Venda por CNPJ por cada categoria/região é importante para direcionar estratégias de vendas, otimizar recursos, personalizar ofertas e também identificar oportunidades específicas, de acordo com o entendimento de quais categorias mais estão sendo vendidas e em quais regiões que elas estão sendo mais consumidas.<br>
    
- 3.7. Saber o gasto médio das famílias por produto é importante, pois permite ajustar os preços para atender às possibilidades financeiras das famílias, maximizando a aceitação. Além disso, ajuda a empresa a identificar oportunidades de mercado e personalizar ofertas. Essa informação possibilita à empresa alinhar seus produtos com o poder de compra das famílias, garantindo uma abordagem mais eficaz nas estratégias de vendas e marketing.<br>
    
- 3.8. Compreender a quantidade de pessoas e a renda em cada região é importante, para ajustar a abordagem de negócios de maneira precisa. Ou seja, adaptar os preços para garantir acessibilidade e personalizar ofertas de acordo com as necessidades locais, garantindo que as estratégias de marketing e vendas estejam alinhadas com as realidades socioeconômicas de cada localidade.<br>

- 3.8. A análise de um gráfico de canais por tipo de consumo pode oferecer insights sobre várias áreas como tendências de consumo, eficácia dos canais de distribuição, segmentação de público, otimização de recursos e avaliação do desempenho de campanhas. Também pode ajudar a entender a concorrência, benchmarking, feedback do consumidor, sazonalidade, adaptação às mudanças no comportamento do consumidor e a eficácia das estratégias multicanal.
