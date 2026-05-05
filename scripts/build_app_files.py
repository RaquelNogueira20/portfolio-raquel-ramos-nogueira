from pathlib import Path

ROOT = Path('/home/ubuntu/culinaria_live_app')

def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')

write('lib/culinary-data.ts', r'''
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
''')

write('lib/assistant.ts', r'''
import { getLessonById, profile } from './culinary-data';

const normalize = (value: string) => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

export function answerCookingQuestion(question: string, lessonId = 'moqueca-baiana') {
  const lesson = getLessonById(lessonId);
  const text = normalize(question);

  if (text.includes('substituir') || text.includes('trocar')) {
    return `Para a receita ${lesson.title}, faça substituições mantendo a função do ingrediente. Se faltar leite de coco, use creme vegetal leve com um pouco de água; se faltar coentro, use salsinha, sabendo que o sabor ficará mais suave.`;
  }

  if (text.includes('tempo') || text.includes('quanto falta')) {
    return `Nesta aula, acompanhe o tempo pelo passo atual. A etapa mais sensível é o cozimento principal: mantenha fogo médio e observe textura, aroma e ponto, em vez de depender apenas do relógio.`;
  }

  if (text.includes('proximo') || text.includes('próximo')) {
    return `Próximo passo: ${lesson.steps[1] ?? lesson.steps[0]}. Antes de avançar, confirme que sua bancada está organizada e que os ingredientes principais estão ao alcance.`;
  }

  if (text.includes('ponto') || text.includes('cozimento')) {
    return `O ponto ideal aparece quando a textura muda sem ressecar. No seu perfil ${profile.level}, recomendo observar cor, firmeza e aroma, e reduzir o fogo se a panela estiver borbulhando demais.`;
  }

  return `Pensando na receita ${lesson.title}, minha orientação é seguir a ordem da chef, separar ingredientes antes de cozinhar e perguntar sempre que uma etapa parecer rápida demais. Dica contextual: ${lesson.tips[0]}`;
}

export const quickQuestions = [
  'Qual é o próximo passo?',
  'Posso substituir algum ingrediente?',
  'Como sei o ponto correto?',
  'Quanto tempo falta?',
];

export const voiceCommands = [
  'Próximo passo',
  'Repetir ingredientes',
  'Quanto tempo falta?',
  'Posso substituir manteiga?',
];
''')

write('components/lesson-card.tsx', r'''
import { Text, TouchableOpacity, View } from 'react-native';
import type { Lesson } from '@/lib/culinary-data';

type Props = {
  lesson: Lesson;
  onPress: () => void;
};

export function LessonCard({ lesson, onPress }: Props) {
  return (
    <TouchableOpacity activeOpacity={0.78} onPress={onPress} className="bg-surface rounded-3xl p-5 border border-border mb-4">
      <View className="flex-row items-center justify-between mb-3">
        <Text className="text-xs font-bold text-primary bg-red-50 px-3 py-1 rounded-full">{lesson.time}</Text>
        <Text className="text-xs text-muted">{lesson.duration}</Text>
      </View>
      <Text className="text-xl font-bold text-foreground leading-7">{lesson.title}</Text>
      <Text className="text-sm text-muted mt-1">com {lesson.chef}</Text>
      <Text className="text-sm text-foreground mt-3 leading-5">{lesson.scenario}</Text>
      <View className="flex-row flex-wrap gap-2 mt-4">
        {lesson.tags.map((tag) => (
          <Text key={tag} className="text-xs text-foreground bg-background px-3 py-1 rounded-full border border-border">{tag}</Text>
        ))}
      </View>
    </TouchableOpacity>
  );
}
''')

write('app/(tabs)/_layout.tsx', r'''
import { Tabs } from 'expo-router';
import { Platform } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

import { HapticTab } from '@/components/haptic-tab';
import { IconSymbol } from '@/components/ui/icon-symbol';
import { useColors } from '@/hooks/use-colors';

export default function TabLayout() {
  const colors = useColors();
  const insets = useSafeAreaInsets();
  const bottomPadding = Platform.OS === 'web' ? 12 : Math.max(insets.bottom, 8);
  const tabBarHeight = 58 + bottomPadding;

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: colors.tint,
        tabBarInactiveTintColor: colors.muted,
        headerShown: false,
        tabBarButton: HapticTab,
        tabBarLabelStyle: { fontSize: 11, fontWeight: '700' },
        tabBarStyle: {
          paddingTop: 8,
          paddingBottom: bottomPadding,
          height: tabBarHeight,
          backgroundColor: colors.background,
          borderTopColor: colors.border,
          borderTopWidth: 0.5,
        },
      }}
    >
      <Tabs.Screen name="index" options={{ title: 'Agenda', tabBarIcon: ({ color }) => <IconSymbol size={26} name="calendar.badge.clock" color={color} /> }} />
      <Tabs.Screen name="live" options={{ title: 'Ao vivo', tabBarIcon: ({ color }) => <IconSymbol size={26} name="video.fill" color={color} /> }} />
      <Tabs.Screen name="assistant" options={{ title: 'Assistente', tabBarIcon: ({ color }) => <IconSymbol size={26} name="sparkles" color={color} /> }} />
      <Tabs.Screen name="voice" options={{ title: 'Voz', tabBarIcon: ({ color }) => <IconSymbol size={26} name="person.wave.2.fill" color={color} /> }} />
      <Tabs.Screen name="profile" options={{ title: 'Perfil', tabBarIcon: ({ color }) => <IconSymbol size={26} name="person.crop.circle.fill" color={color} /> }} />
    </Tabs>
  );
}
''')

write('components/ui/icon-symbol.tsx', r'''
import MaterialIcons from '@expo/vector-icons/MaterialIcons';
import { SymbolWeight, SymbolViewProps } from 'expo-symbols';
import { ComponentProps } from 'react';
import { OpaqueColorValue, type StyleProp, type TextStyle } from 'react-native';

type IconMapping = Record<SymbolViewProps['name'], ComponentProps<typeof MaterialIcons>['name']>;
type IconSymbolName = keyof typeof MAPPING;

const MAPPING = {
  'house.fill': 'home',
  'paperplane.fill': 'send',
  'chevron.left.forwardslash.chevron.right': 'code',
  'chevron.right': 'chevron-right',
  'calendar.badge.clock': 'event',
  'video.fill': 'videocam',
  'sparkles': 'auto-awesome',
  'person.wave.2.fill': 'record-voice-over',
  'person.crop.circle.fill': 'account-circle',
  'fork.knife': 'restaurant',
  'list.bullet.clipboard': 'checklist',
  'mic.fill': 'mic',
  'speaker.wave.2.fill': 'volume-up',
} as IconMapping;

export function IconSymbol({
  name,
  size = 24,
  color,
  style,
}: {
  name: IconSymbolName;
  size?: number;
  color: string | OpaqueColorValue;
  style?: StyleProp<TextStyle>;
  weight?: SymbolWeight;
}) {
  return <MaterialIcons color={color} size={size} name={MAPPING[name]} style={style} />;
}
''')

write('app/(tabs)/index.tsx', r'''
import { FlatList, Text, TouchableOpacity, View } from 'react-native';
import { router } from 'expo-router';

import { LessonCard } from '@/components/lesson-card';
import { ScreenContainer } from '@/components/screen-container';
import { lessons } from '@/lib/culinary-data';

export default function HomeScreen() {
  const featured = lessons[0];

  return (
    <ScreenContainer className="px-5 pt-3">
      <FlatList
        data={lessons}
        keyExtractor={(item) => item.id}
        showsVerticalScrollIndicator={false}
        ListHeaderComponent={
          <View className="pb-4">
            <Text className="text-sm font-semibold text-primary">Culinária Live</Text>
            <Text className="text-4xl font-extrabold text-foreground mt-1 leading-10">Aulas ao vivo com chefs na sua cozinha</Text>
            <Text className="text-base text-muted mt-3 leading-6">Agende, entre na chamada e cozinhe em situações reais do dia a dia com receita explicada passo a passo.</Text>

            <View className="bg-primary rounded-[32px] p-5 mt-6">
              <Text className="text-white/80 text-sm font-bold">AO VIVO EM DESTAQUE</Text>
              <Text className="text-white text-2xl font-extrabold mt-2 leading-8">{featured.title}</Text>
              <Text className="text-white/90 text-sm mt-2 leading-5">{featured.scenario}</Text>
              <TouchableOpacity activeOpacity={0.82} onPress={() => router.push('/live')} className="bg-white rounded-full px-5 py-4 mt-5 items-center">
                <Text className="text-primary font-extrabold">Entrar na aula ao vivo</Text>
              </TouchableOpacity>
            </View>

            <View className="flex-row items-center justify-between mt-7 mb-3">
              <Text className="text-2xl font-bold text-foreground">Próximas aulas</Text>
              <Text className="text-sm font-semibold text-primary">3 agendadas</Text>
            </View>
          </View>
        }
        renderItem={({ item }) => <LessonCard lesson={item} onPress={() => router.push({ pathname: '/class/[id]', params: { id: item.id } })} />}
        ListFooterComponent={<View className="h-8" />}
      />
    </ScreenContainer>
  );
}
''')

write('app/class/[id].tsx', r'''
import { ScrollView, Text, TouchableOpacity, View } from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';

import { ScreenContainer } from '@/components/screen-container';
import { getLessonById } from '@/lib/culinary-data';

export default function LessonDetailScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const lesson = getLessonById(id);

  return (
    <ScreenContainer className="px-5 pt-3">
      <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{ paddingBottom: 34 }}>
        <TouchableOpacity activeOpacity={0.7} onPress={() => router.back()} className="self-start bg-surface px-4 py-2 rounded-full border border-border mb-4">
          <Text className="font-bold text-foreground">Voltar</Text>
        </TouchableOpacity>

        <Text className="text-sm font-semibold text-primary">{lesson.time} • {lesson.duration}</Text>
        <Text className="text-4xl font-extrabold text-foreground mt-2 leading-10">{lesson.title}</Text>
        <Text className="text-base text-muted mt-2">com {lesson.chef} • {lesson.level}</Text>

        <View className="bg-red-50 border border-red-100 rounded-3xl p-5 mt-6">
          <Text className="text-lg font-extrabold text-foreground">Explicação da receita</Text>
          <Text className="text-base text-foreground leading-6 mt-2">{lesson.description}</Text>
          <Text className="text-sm text-muted leading-5 mt-3">{lesson.scenario}</Text>
        </View>

        <Text className="text-2xl font-bold text-foreground mt-7 mb-3">Ingredientes</Text>
        {lesson.ingredients.map((ingredient) => (
          <View key={ingredient} className="bg-surface rounded-2xl px-4 py-3 border border-border mb-2">
            <Text className="text-base text-foreground">{ingredient}</Text>
          </View>
        ))}

        <Text className="text-2xl font-bold text-foreground mt-7 mb-3">Etapas da aula</Text>
        {lesson.steps.map((step, index) => (
          <View key={step} className="flex-row bg-surface rounded-2xl p-4 border border-border mb-3">
            <View className="w-8 h-8 rounded-full bg-primary items-center justify-center mr-3">
              <Text className="text-white font-extrabold">{index + 1}</Text>
            </View>
            <Text className="flex-1 text-base text-foreground leading-6">{step}</Text>
          </View>
        ))}

        <TouchableOpacity activeOpacity={0.85} onPress={() => router.push('/live')} className="bg-primary rounded-full py-5 items-center mt-4">
          <Text className="text-white font-extrabold text-base">Entrar na aula ao vivo</Text>
        </TouchableOpacity>
      </ScrollView>
    </ScreenContainer>
  );
}
''')

write('app/(tabs)/profile.tsx', r'''
import { ScrollView, Text, View } from 'react-native';

import { ScreenContainer } from '@/components/screen-container';
import { profile } from '@/lib/culinary-data';

export default function ProfileScreen() {
  return (
    <ScreenContainer className="px-5 pt-3">
      <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{ paddingBottom: 34 }}>
        <Text className="text-sm font-semibold text-primary">Perfil culinário</Text>
        <Text className="text-4xl font-extrabold text-foreground mt-1 leading-10">O app aprende com seu jeito de cozinhar</Text>
        <Text className="text-base text-muted mt-3 leading-6">Preferências locais simuladas ajudam a ajustar recomendações, dicas e respostas do assistente sem exigir login.</Text>

        <View className="bg-primary rounded-[32px] p-6 mt-6">
          <Text className="text-white/80 text-sm font-bold">USUÁRIO</Text>
          <Text className="text-white text-3xl font-extrabold mt-2">{profile.name}</Text>
          <Text className="text-white/90 text-base mt-2">{profile.level}</Text>
        </View>

        <Section title="Preferências detectadas" items={profile.preferences} />
        <Section title="Restrições e ajustes" items={profile.restrictions} />
        <Section title="Aprendizado com o uso" items={profile.learnedSignals} />
        <Section title="Técnicas favoritas" items={profile.favoriteTechniques} />
      </ScrollView>
    </ScreenContainer>
  );
}

function Section({ title, items }: { title: string; items: string[] }) {
  return (
    <View className="mt-7">
      <Text className="text-2xl font-bold text-foreground mb-3">{title}</Text>
      {items.map((item) => (
        <View key={item} className="bg-surface border border-border rounded-2xl p-4 mb-3">
          <Text className="text-base text-foreground leading-6">{item}</Text>
        </View>
      ))}
    </View>
  );
}
''')

write('theme.config.js', r'''
/** @type {const} */
const themeColors = {
  primary: { light: '#FF0000', dark: '#FF4D4D' },
  background: { light: '#FFF8F8', dark: '#190A0A' },
  surface: { light: '#FFFFFF', dark: '#241010' },
  foreground: { light: '#1C1111', dark: '#FFF1F1' },
  muted: { light: '#7A4A4A', dark: '#D6A5A5' },
  border: { light: '#F2D4D4', dark: '#5A2424' },
  success: { light: '#16A34A', dark: '#4ADE80' },
  warning: { light: '#F59E0B', dark: '#FBBF24' },
  error: { light: '#DC2626', dark: '#F87171' },
};

module.exports = { themeColors };
''')

print('Arquivos principais criados com sucesso.')
