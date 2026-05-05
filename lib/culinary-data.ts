export type Lesson = {
  id: string;
  title: string;
  chef: string;
  time: string;
  duration: string;
  level: string;
  scenario: string;
  description: string;
  jitsiRoom: string;
  ingredients: string[];
  steps: string[];
  tips: string[];
  tags: string[];
};

export type CulinaryProfile = {
  name: string;
  level: string;
  preferences: string[];
  restrictions: string[];
  learnedSignals: string[];
  favoriteTechniques: string[];
};

export const lessons: Lesson[] = [
  {
    id: 'moqueca-baiana',
    title: 'Moqueca baiana de noite corrida',
    chef: 'Chef Marina Costa',
    time: 'Hoje, 19:30',
    duration: '55 min',
    level: 'Intermediário',
    scenario: 'Vida real: jantar depois do trabalho, com bancada pequena e tempo controlado.',
    description:
      'Nesta aula ao vivo, a chef ensina uma moqueca baiana aromática, explicando a ordem dos ingredientes, o ponto do peixe e como organizar tudo sem bagunçar a cozinha.',
    jitsiRoom: 'CulinariaLiveMoquecaBaianaNoiteCorrida',
    ingredients: ['600 g de peixe em postas', '1 pimentão vermelho', '1 pimentão amarelo', '2 tomates', '1 cebola', '200 ml de leite de coco', '2 colheres de azeite de dendê', 'Coentro, limão e sal'],
    steps: ['Temperar o peixe com limão e sal por 10 minutos.', 'Montar camadas de cebola, tomate, pimentões e peixe.', 'Adicionar leite de coco e cozinhar em fogo médio.', 'Finalizar com dendê e coentro, ajustando o sal.', 'Servir com arroz branco e farofa rápida.'],
    tips: ['Separe os vegetais antes da chamada começar.', 'Evite mexer demais para não quebrar o peixe.', 'Use panela baixa para cozinhar por igual.'],
    tags: ['Ao vivo', 'Peixe', 'Jantar prático'],
  },
  {
    id: 'massa-domingo',
    title: 'Massa fresca para almoço de domingo',
    chef: 'Chef Rafael Neri',
    time: 'Sábado, 11:00',
    duration: '70 min',
    level: 'Iniciante',
    scenario: 'Vida real: família chegando em casa e preparo com ingredientes simples.',
    description:
      'A aula mostra como preparar massa fresca com poucos utensílios, incluindo explicação do ponto da massa, descanso e molho rápido de tomate com manjericão.',
    jitsiRoom: 'CulinariaLiveMassaFrescaDomingo',
    ingredients: ['300 g de farinha de trigo', '3 ovos', '1 pitada de sal', '4 tomates maduros', '2 dentes de alho', 'Manjericão fresco', 'Azeite e parmesão'],
    steps: ['Formar um vulcão com a farinha e adicionar ovos no centro.', 'Sovar até obter massa lisa e elástica.', 'Descansar a massa por 20 minutos.', 'Abrir, cortar e cozinhar em água salgada.', 'Preparar molho rápido e finalizar com parmesão.'],
    tips: ['Se a massa grudar, polvilhe pouca farinha.', 'Abra por partes para manter controle.', 'Reserve água do cozimento para o molho.'],
    tags: ['Família', 'Massa', 'Domingo'],
  },
  {
    id: 'sobremesa-improviso',
    title: 'Sobremesa de improviso com frutas',
    chef: 'Chef Helena Duarte',
    time: 'Quarta, 20:00',
    duration: '40 min',
    level: 'Iniciante',
    scenario: 'Vida real: visita inesperada e poucos ingredientes na geladeira.',
    description:
      'A chef ensina uma sobremesa flexível com frutas, creme rápido e crocante de frigideira, explicando substituições para o que houver em casa.',
    jitsiRoom: 'CulinariaLiveSobremesaImproviso',
    ingredients: ['2 xícaras de frutas picadas', '1 lata de creme de leite', '2 colheres de açúcar', '1 limão', 'Aveia ou castanhas', 'Canela'],
    steps: ['Misturar creme, açúcar e raspas de limão.', 'Aquecer aveia ou castanhas na frigideira até dourar.', 'Montar camadas de fruta, creme e crocante.', 'Finalizar com canela e gelar rapidamente.', 'Servir em taças ou copos.'],
    tips: ['Use banana, maçã, manga ou morango.', 'Monte em copos para porções rápidas.', 'A acidez do limão equilibra o doce.'],
    tags: ['Sobremesa', 'Improviso', 'Rápido'],
  },
];

export const profile: CulinaryProfile = {
  name: 'Cozinheiro(a) da casa',
  level: 'Intermediário em evolução',
  preferences: ['Receitas brasileiras', 'Aulas ao vivo', 'Pratos de até 1 hora', 'Técnicas explicadas passo a passo'],
  restrictions: ['Evitar excesso de lactose', 'Preferir temperos frescos'],
  learnedSignals: ['Você costuma abrir dicas de substituição.', 'Você acompanha melhor receitas com etapas curtas.', 'O app recomenda aulas com organização prévia da bancada.'],
  favoriteTechniques: ['Refogar', 'Finalizar molhos', 'Preparar mise en place', 'Ajustar ponto de cozimento'],
};

export const getLessonById = (id?: string) => lessons.find((lesson) => lesson.id === id) ?? lessons[0];
export const getJitsiUrl = (room: string) => `https://meet.jit.si/${encodeURIComponent(room)}#config.prejoinPageEnabled=false&userInfo.displayName="Aluno Culinária Live"`;
