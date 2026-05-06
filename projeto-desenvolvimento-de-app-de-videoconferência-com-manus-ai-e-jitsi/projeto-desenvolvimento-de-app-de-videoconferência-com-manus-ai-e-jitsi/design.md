# Plano de Design — Culinária Live

**Autor:** Manus AI

O aplicativo **Culinária Live** será desenhado como uma experiência móvel em orientação retrato, com uso confortável em uma mão e aparência alinhada aos padrões contemporâneos de aplicativos iOS. A proposta visual combina uma marca predominante em **vermelho #FF0000** com superfícies claras, cartões arredondados, tipografia hierárquica e ações principais posicionadas na metade inferior da tela sempre que possível. O objetivo é permitir que o usuário agende aulas de culinária, entre em aulas ao vivo com chefs, acompanhe a explicação da receita em contexto realista de cozinha e use um assistente inteligente por texto ou voz durante a preparação.

## Diretrizes de Interface

A navegação principal será organizada por abas inferiores, pois esse padrão favorece o acesso rápido às áreas essenciais em telas móveis. Os botões primários usarão vermelho sólido, estados pressionados discretos e contraste alto. As telas de aula priorizarão elementos grandes e legíveis, pois o usuário pode estar com as mãos ocupadas na cozinha. O layout será pensado para leitura rápida, com cartões de receita, status da aula, ingredientes e ações de voz em áreas facilmente tocáveis.

| Elemento | Decisão de Design | Justificativa de Uso |
|---|---|---|
| Cor predominante | **#FF0000** | Reforça energia, urgência e identidade visual culinária solicitada. |
| Orientação | Retrato 9:16 | Mantém o app adequado para uso em balcão, suporte de celular ou uma mão. |
| Navegação | Abas inferiores | Facilita alternância entre agenda, aula, assistente e perfil. |
| Cartões | Bordas arredondadas e sombras leves | Organizam receitas, aulas e preferências sem poluir a tela. |
| Ações críticas | Botões grandes na parte inferior | Ajudam durante o uso prático na cozinha. |

## Lista de Telas

| Tela | Conteúdo Principal | Funcionalidade |
|---|---|---|
| **Início / Agenda** | Aula em destaque, próximas aulas, simulações do dia a dia e botão de entrada rápida | Permitir ver aulas, selecionar um agendamento e iniciar uma aula ao vivo. |
| **Detalhe da Aula** | Chef, horário, nível, cenário realista, ingredientes e etapas da receita | Explicar a receita antes da chamada e preparar o usuário para a aula. |
| **Aula Ao Vivo** | Área de chamada Jitsi, status do chef, receita ativa e passos acompanháveis | Abrir a sala de videoconferência e manter a explicação da receita junto da aula. |
| **Assistente de Cozinha** | Chat contextual sobre a receita, sugestões rápidas e respostas simuladas | Simular um assistente inteligente focado na aula e na receita. |
| **Voz Assistente** | Ícone grande de pessoa falando, estado de escuta e comandos prontos | Abrir uma tela dedicada para comando por voz útil durante o preparo. |
| **Perfil Culinário** | Preferências, restrições, nível, histórico e recomendações | Fazer o app parecer que aprende com o uso local e personaliza sugestões. |

## Conteúdo e Funcionalidade por Tela

A tela **Início / Agenda** mostrará um cabeçalho com saudação, uma aula ao vivo em destaque e uma lista de próximas aulas. Cada aula terá chef, horário, duração, receita e um rótulo de contexto real, como “jantar corrido de terça-feira” ou “almoço de domingo em família”. O toque em uma aula levará ao detalhe, enquanto a aula em destaque permitirá acesso direto à chamada ao vivo.

A tela **Detalhe da Aula** funcionará como preparação. Ela exibirá a explicação da receita, ingredientes, utensílios e etapas resumidas. O usuário poderá visualizar o cenário do dia a dia em que a aula se aplica, como organizar a bancada, separar ingredientes e acompanhar o tempo estimado. A ação principal será “Entrar na aula ao vivo”.

A tela **Aula Ao Vivo** será o centro da experiência. Ela apresentará uma área de videoconferência baseada em sala Jitsi por URL, com opção de abrir a chamada em navegador interno ou externo conforme a compatibilidade da plataforma. Abaixo, haverá um painel com receita, etapas, ingredientes importantes e botões para abrir o assistente ou ativar voz.

A tela **Assistente de Cozinha** será uma simulação funcional de um assistente inteligente dentro da aula. Ele responderá a dúvidas comuns sobre substituições, ponto de cozimento, tempo, organização e adaptação ao perfil culinário do usuário. O foco será manter a resposta contextual à receita ativa, evitando um chat genérico.

A tela **Voz Assistente** terá um ícone visual de pessoa falando em destaque. A interface indicará estados como “toque para falar”, “ouvindo comando” e “resposta do assistente”. Como o uso é em cozinha, os comandos serão curtos e práticos, como “próximo passo”, “repetir ingrediente”, “quanto tempo falta?” e “posso substituir manteiga?”.

A tela **Perfil Culinário** apresentará preferências alimentares, nível de habilidade, pratos favoritos, alergias simuladas e insights de uso. A personalização será local, sem exigir login ou armazenamento em nuvem, respeitando o requisito de criar uma experiência funcional sem adicionar autenticação desnecessária.

## Fluxos Principais

| Fluxo | Etapas |
|---|---|
| **Agendar e entrar na aula** | Usuário abre Início → toca em aula agendada → revisa ingredientes e receita → toca em “Entrar na aula ao vivo” → abre a tela com Jitsi. |
| **Usar assistente dentro da aula** | Usuário está em Aula Ao Vivo → toca em “Assistente” → pergunta sobre a receita → recebe resposta contextual → retorna à aula. |
| **Usar comando por voz** | Usuário toca em “Voz” → vê ícone de pessoa falando → ativa escuta simulada → escolhe ou fala comando → recebe orientação de cozinha. |
| **Personalização culinária** | Usuário abre Perfil → ajusta nível e preferências → app destaca recomendações compatíveis nas próximas aulas. |

## Paleta de Cores

| Uso | Cor | Aplicação |
|---|---|---|
| Primária | **#FF0000** | Botões principais, abas ativas, destaques e marca. |
| Fundo claro | **#FFF8F8** | Telas principais, mantendo o vermelho mais confortável. |
| Superfície | **#FFFFFF** | Cartões, listas e painéis de receita. |
| Texto principal | **#1C1111** | Títulos e conteúdo de maior importância. |
| Texto secundário | **#7A4A4A** | Metadados, descrições e apoio visual. |
| Sucesso | **#16A34A** | Aula confirmada e etapas concluídas. |
| Atenção | **#F59E0B** | Tempo de preparo e alertas culinários. |

## Observações de Implementação

O aplicativo será implementado inicialmente com dados locais simulados, pois isso permite demonstrar todos os fluxos sem exigir cadastro, backend externo ou chaves de API. A integração com Jitsi será feita por meio de uma sala nomeada e aberta via URL, garantindo que o recurso de videoconferência seja utilizável em ambiente móvel. O assistente inteligente será implementado como uma experiência contextual simulada e preparada para futura conexão com um backend de IA, sem solicitar segredos ao usuário nesta primeira versão.

## Referências

[1]: https://developer.apple.com/design/human-interface-guidelines/ios "Apple Human Interface Guidelines — iOS"
[2]: https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-iframe/ "Jitsi Meet Handbook — IFrame API"
[3]: https://docs.expo.dev/ "Expo Documentation"
