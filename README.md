# Culinária Live 🍳

**Aulas de culinária ao vivo com chefs profissionais, assistente inteligente e comando por voz**

## 📋 Visão Geral

**Culinária Live** é um aplicativo móvel que conecta alunos e chefs profissionais em aulas de culinária em tempo real. O app oferece uma experiência imersiva com videoconferência integrada (Jitsi Meet), explicação passo a passo de receitas, assistente inteligente contextual focado em culinária, e comando por voz para facilitar o acompanhamento durante o preparo. O aplicativo aprende com o uso do usuário, criando um perfil culinário personalizado que melhora as recomendações ao longo do tempo.

### Problema Resolvido

Muitas pessoas gostariam de aprender culinária com chefs profissionais, mas enfrentam barreiras como:
- Falta de acesso a aulas ao vivo de qualidade
- Dificuldade em acompanhar receitas complexas enquanto cozinha
- Necessidade de consultar múltiplos aplicativos (videoconferência, receitas, chat)
- Impossibilidade de fazer perguntas contextualizadas durante a aula

**Culinária Live** resolve todos esses problemas em uma única plataforma integrada, com foco em experiência prática e real.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| **React Native** | 0.81 | Framework para desenvolvimento móvel multiplataforma |
| **Expo SDK** | 54 | Plataforma de desenvolvimento e distribuição |
| **TypeScript** | 5.9 | Tipagem estática e segurança de código |
| **NativeWind** | 4.2 | Tailwind CSS para React Native |
| **Expo Router** | 6 | Navegação e roteamento |
| **Jitsi Meet** | Integração Web | Videoconferência ao vivo |
| **expo-speech** | 14.0.8 | Síntese de fala (text-to-speech) |
| **expo-keep-awake** | 15.0.8 | Manter tela ativa durante aulas |
| **expo-web-browser** | 15.0.10 | Abertura segura de URLs externas |
| **React Query** | 5.90.12 | Gerenciamento de dados assíncronos |
| **Vitest** | 2.1.9 | Testes unitários |

---

## 🚀 Instruções de Instalação

### Pré-requisitos

- **Node.js** 18+ e **pnpm** 9.12.0+
- **Expo Go** instalado no seu dispositivo móvel (iOS App Store ou Google Play)
- Conexão com internet estável

### Passo 1: Clonar o Repositório

```bash
git clone <seu-repositorio-url>
cd culinaria_live_app
```

### Passo 2: Instalar Dependências

```bash
pnpm install
```

### Passo 3: Iniciar o Servidor de Desenvolvimento

```bash
pnpm dev
```

O servidor iniciará em `http://localhost:8081` e exibirá um QR Code no terminal.

### Passo 4: Abrir no Dispositivo Móvel

#### Opção A: Via QR Code (Recomendado)

1. Abra o **Expo Go** no seu dispositivo
2. Toque em "Scan QR Code"
3. Aponte a câmera para o QR Code exibido no terminal ou veja abaixo

#### Opção B: Via URL

1. Abra o **Expo Go**
2. Toque em "Enter URL manually"
3. Digite: `exps://8081-i32l9xdb528g5i3pjcui7-4330e5a9.us1.manus.computer`

#### Opção C: Na Web (Simulação)

```bash
# Já está disponível em http://localhost:8081
# Abra no navegador para visualizar a versão web
```

---

## 📱 Pré-visualização

### URL de Acesso

**Versão Web (Simulação):**  
[https://8081-i32l9xdb528g5i3pjcui7-4330e5a9.us1.manus.computer](https://8081-i32l9xdb528g5i3pjcui7-4330e5a9.us1.manus.computer)

**Versão Nativa (Expo Go):**  
`exps://8081-i32l9xdb528g5i3pjcui7-4330e5a9.us1.manus.computer`

### QR Code para Acesso Rápido

![Culinária Live QR Code](https://d2xsxph8kpxj0f.cloudfront.net/310519663628148319/RigkWFohVDZU8L8iY8h9Gq/culinaria-live-qr-code.png)

**Instruções:**
1. Abra o **Expo Go** no seu smartphone
2. Toque em "Scan QR Code"
3. Aponte para a imagem acima
4. O app carregará automaticamente

---

## 🎯 Funcionalidades Principais

### 1. **Agenda de Aulas ao Vivo** 📅

- Visualize todas as aulas programadas com chefs profissionais
- Horários, durações e descrições de cada aula
- Modo vida real com simulações de cenários do dia a dia

### 2. **Tela de Chamada ao Vivo** 🎥

- Integração com **Jitsi Meet** para videoconferência segura
- Abertura da sala de aula em navegador protegido
- Explicação completa da receita visível durante a transmissão
- Passos da receita com dicas da chef

### 3. **Assistente Inteligente de Cozinha** 🤖

- ChatGPT focado em culinária dentro da aula
- Respostas contextualizadas para a receita atual
- Sugestões de substituições, tempos de cozimento, pontos corretos
- Perguntas rápidas pré-configuradas para acesso instantâneo

### 4. **Comando por Voz** 🎤

- Tela de voz assistente com ícone de pessoa falando
- Comandos simples como "Próximo passo", "Repetir ingredientes"
- Síntese de fala em português brasileiro
- Ideal para manter as mãos livres durante o preparo

### 5. **Perfil Culinário Personalizado** 👨‍🍳

- O app aprende com cada aula que você assiste
- Preferências de ingredientes e técnicas
- Histórico de aulas e receitas favoritas
- Recomendações personalizadas (local, sem cloud)

### 6. **Design Intuitivo** 🎨

- Tema predominante em **vermelho (#FF0000)**
- Ícone personalizado refletindo a identidade do app
- Otimizado para uso com uma mão em modo retrato
- Seguindo padrões iOS Human Interface Guidelines

---

## 📂 Estrutura do Projeto

```
culinaria_live_app/
├── app/
│   ├── (tabs)/
│   │   ├── index.tsx           # Tela inicial com agenda
│   │   ├── live.tsx            # Tela de aula ao vivo com Jitsi
│   │   ├── assistant.tsx       # Assistente inteligente
│   │   ├── voice.tsx           # Tela de comando por voz
│   │   ├── class/
│   │   │   └── [id].tsx        # Detalhe da aula
│   │   └── profile.tsx         # Perfil culinário do usuário
│   ├── _layout.tsx             # Layout raiz com providers
│   └── oauth/                  # Callbacks de autenticação
├── components/
│   ├── screen-container.tsx    # Wrapper SafeArea
│   ├── themed-view.tsx         # View com tema automático
│   └── ui/
│       └── icon-symbol.tsx     # Mapeamento de ícones
├── lib/
│   ├── culinary-data.ts        # Dados locais de aulas e receitas
│   ├── assistant.ts            # Lógica do assistente inteligente
│   ├── assistant.test.ts       # Testes unitários
│   └── utils.ts                # Funções utilitárias
├── hooks/
│   ├── use-colors.ts           # Hook de cores do tema
│   ├── use-color-scheme.ts     # Detecção light/dark mode
│   └── use-auth.ts             # Hook de autenticação
├── assets/
│   └── images/                 # Ícones e splash screen
├── theme.config.js             # Configuração de cores
├── tailwind.config.js          # Configuração Tailwind
├── app.config.ts               # Configuração Expo
├── package.json                # Dependências do projeto
└── README.md                   # Este arquivo
```

---

## 🧪 Testes

O projeto inclui testes unitários para validar funcionalidades críticas:

```bash
# Executar todos os testes
pnpm test

# Resultado esperado:
# ✓ Provides scheduled live cooking lessons with recipe steps
# ✓ Creates a valid Jitsi Meet URL for a live class room
# ✓ Answers recipe-specific substitution questions
# ✓ Answers voice-style next step commands with contextual guidance
```

---

## 🔧 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `pnpm dev` | Inicia servidor de desenvolvimento |
| `pnpm test` | Executa testes unitários |
| `pnpm check` | Verifica tipos TypeScript |
| `pnpm lint` | Valida código com ESLint |
| `pnpm format` | Formata código com Prettier |
| `pnpm qr` | Gera QR Code para acesso rápido |
| `pnpm ios` | Abre no simulador iOS |
| `pnpm android` | Abre no simulador Android |

---

## 📦 Distribuição

### APK (Android)

Para gerar um APK para distribuição:

1. Acesse o painel de controle do projeto
2. Clique em **"Publish"** (requer checkpoint salvo)
3. Selecione **"Build APK"**
4. Aguarde a conclusão do build
5. Baixe o APK gerado

**Nota:** O build pode levar 10-15 minutos. Você receberá um link de download quando estiver pronto.

### IPA (iOS)

Para distribuição no iOS:

1. Configure sua conta Apple Developer
2. Use o painel de controle para iniciar o build
3. Selecione **"Build IPA"**
4. Siga as instruções de assinatura de código
5. Distribua via TestFlight ou App Store

---

## 🎓 Como Usar o App

### Fluxo Principal

1. **Abra o app** → Visualize a agenda de aulas
2. **Toque em uma aula** → Veja detalhes completos da receita
3. **Clique "Entrar na aula ao vivo"** → Abre a sala Jitsi
4. **Use o assistente** → Faça perguntas sobre a receita
5. **Use comandos por voz** → Navegue sem tocar no celular
6. **Veja seu perfil** → Acompanhe seu aprendizado

### Tela de Aula ao Vivo

- **Painel Jitsi:** Videoconferência com o chef
- **Receita:** Ingredientes e modo de preparo
- **Passos:** Navegue entre as etapas
- **Dicas:** Conselhos práticos da chef
- **Botões rápidos:** Assistente e Voz

### Assistente Inteligente

- Pergunte sobre substituições de ingredientes
- Solicite dicas de tempo de cozimento
- Peça orientações sobre técnicas
- Use perguntas rápidas para respostas instantâneas

### Comando por Voz

- "Próximo passo" → Avança para a próxima etapa
- "Repetir ingredientes" → Lê os ingredientes novamente
- "Qual é o ponto correto?" → Dica sobre o ponto de cozimento
- Toque em qualquer comando para simular fala

---

## 🌐 Integração Jitsi Meet

O app usa **Jitsi Meet** para videoconferência segura:

- **Sem necessidade de conta:** Acesso direto via URL
- **Salas dedicadas:** Cada aula tem sua própria sala
- **Controles nativos:** Microfone, câmera, compartilhamento
- **Compatibilidade:** Funciona em navegadores modernos

**Sala de exemplo:** `https://meet.jit.si/CulinariaLiveMoquecaBaianaNoiteCorrida`

---

## 🔐 Privacidade e Segurança

- **Dados locais:** Perfil e histórico armazenados localmente no dispositivo
- **Sem rastreamento:** Nenhum dado pessoal é enviado para servidores
- **Conexão segura:** HTTPS para todas as comunicações
- **Jitsi privado:** Salas de videoconferência encriptadas

---

## 🐛 Troubleshooting

### "QR Code não funciona"

- Certifique-se de que o Expo Go está instalado
- Verifique se está na mesma rede WiFi
- Tente digitar a URL manualmente

### "Jitsi não abre"

- Verifique sua conexão com a internet
- Certifique-se de que o navegador está atualizado
- Tente abrir em um navegador diferente

### "Voz não funciona"

- Verifique as permissões de áudio do app
- Em iOS, desative o modo silencioso
- Reinicie o app

### "Testes falhando"

```bash
# Limpe cache e reinstale dependências
rm -rf node_modules pnpm-lock.yaml
pnpm install
pnpm test
```

---

## 📞 Suporte e Contribuições

Para reportar bugs, sugerir melhorias ou contribuir:

1. Abra uma **Issue** descrevendo o problema
2. Faça um **Fork** do repositório
3. Crie uma **Branch** para sua feature
4. Envie um **Pull Request**

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.

---

## 🙏 Agradecimentos

- **Expo Team** pela excelente plataforma de desenvolvimento
- **Jitsi Meet** pela videoconferência de código aberto
- **React Native Community** pelo ecossistema robusto
- Todos os chefs e alunos que inspiram este projeto

---

## 📊 Roadmap Futuro

- [ ] Cadastro real de alunos e chefs
- [ ] Painel administrativo para criar novas aulas
- [ ] Notificações de lembrete antes das aulas
- [ ] Integração com redes sociais
- [ ] Certificados de conclusão
- [ ] Sistema de avaliações e reviews
- [ ] Receitas salvas e favoritas
- [ ] Modo offline com cache de receitas
- [ ] Suporte a múltiplos idiomas
- [ ] Integração com plataformas de pagamento

---

**Desenvolvido com ❤️ para amantes de culinária e aprendizado contínuo.**

*Última atualização: Maio de 2026*
