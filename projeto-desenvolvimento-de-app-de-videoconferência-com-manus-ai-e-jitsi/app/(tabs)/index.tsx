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
