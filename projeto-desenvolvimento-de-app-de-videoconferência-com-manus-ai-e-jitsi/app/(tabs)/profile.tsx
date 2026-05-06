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
