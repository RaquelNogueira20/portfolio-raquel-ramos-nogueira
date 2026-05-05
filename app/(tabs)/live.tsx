import { useState } from 'react';
import { ActivityIndicator, Alert, Linking, Platform, ScrollView, Text, TouchableOpacity, View } from 'react-native';
import * as WebBrowser from 'expo-web-browser';
import { useKeepAwake } from 'expo-keep-awake';
import { router } from 'expo-router';

import { IconSymbol } from '@/components/ui/icon-symbol';
import { ScreenContainer } from '@/components/screen-container';
import { getJitsiUrl, lessons } from '@/lib/culinary-data';

export default function LiveScreen() {
  useKeepAwake('culinaria-live-class');
  const lesson = lessons[0];
  const jitsiUrl = getJitsiUrl(lesson.jitsiRoom);
  const [opening, setOpening] = useState(false);
  const [activeStep, setActiveStep] = useState(0);

  const openJitsi = async () => {
    try {
      setOpening(true);
      if (Platform.OS === 'web') {
        await Linking.openURL(jitsiUrl);
      } else {
        await WebBrowser.openBrowserAsync(jitsiUrl, {
          presentationStyle: WebBrowser.WebBrowserPresentationStyle.FULL_SCREEN,
          controlsColor: '#FF0000',
        });
      }
    } catch {
      Alert.alert('Não foi possível abrir a chamada', 'Verifique sua conexão e tente novamente.');
    } finally {
      setOpening(false);
    }
  };

  return (
    <ScreenContainer className="px-5 pt-3">
      <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{ paddingBottom: 34 }}>
        <Text className="text-sm font-semibold text-primary">Aula ao vivo</Text>
        <Text className="text-4xl font-extrabold text-foreground mt-1 leading-10">Cozinhe com o chef em tempo real</Text>
        <Text className="text-base text-muted mt-3 leading-6">A chamada usa uma sala Jitsi Meet dedicada para a aula, enquanto a receita fica visível para consulta rápida.</Text>

        <View className="bg-foreground rounded-[32px] p-5 mt-6 overflow-hidden">
          <View className="h-52 rounded-3xl bg-black items-center justify-center border border-red-400">
            <View className="w-20 h-20 rounded-full bg-primary items-center justify-center mb-4">
              <IconSymbol name="video.fill" size={42} color="#FFFFFF" />
            </View>
            <Text className="text-white text-2xl font-extrabold">Sala Jitsi pronta</Text>
            <Text className="text-white/70 text-center mt-2 px-4">{lesson.jitsiRoom}</Text>
          </View>

          <TouchableOpacity activeOpacity={0.84} onPress={openJitsi} disabled={opening} className="bg-primary rounded-full py-5 items-center mt-5">
            {opening ? <ActivityIndicator color="#FFFFFF" /> : <Text className="text-white font-extrabold text-base">Abrir chamada ao vivo no Jitsi</Text>}
          </TouchableOpacity>
          <Text className="text-white/60 text-xs text-center mt-3 leading-4">Ao tocar, a sala abre em navegador seguro do sistema ou aba externa, preservando a experiência móvel.</Text>
        </View>

        <View className="bg-surface border border-border rounded-3xl p-5 mt-6">
          <Text className="text-sm font-bold text-primary">RECEITA DA AULA</Text>
          <Text className="text-2xl font-extrabold text-foreground mt-2 leading-8">{lesson.title}</Text>
          <Text className="text-base text-foreground leading-6 mt-3">{lesson.description}</Text>
        </View>

        <View className="flex-row gap-3 mt-5">
          <TouchableOpacity activeOpacity={0.82} onPress={() => router.push('/assistant')} className="flex-1 bg-surface border border-border rounded-2xl p-4 items-center">
            <IconSymbol name="sparkles" size={28} color="#FF0000" />
            <Text className="text-foreground font-extrabold mt-2">Assistente</Text>
          </TouchableOpacity>
          <TouchableOpacity activeOpacity={0.82} onPress={() => router.push('/voice')} className="flex-1 bg-surface border border-border rounded-2xl p-4 items-center">
            <IconSymbol name="mic.fill" size={28} color="#FF0000" />
            <Text className="text-foreground font-extrabold mt-2">Voz</Text>
          </TouchableOpacity>
        </View>

        <Text className="text-2xl font-bold text-foreground mt-7 mb-3">Passo atual da receita</Text>
        {lesson.steps.map((step, index) => {
          const active = index === activeStep;
          return (
            <TouchableOpacity key={step} activeOpacity={0.78} onPress={() => setActiveStep(index)} className={`rounded-2xl p-4 border mb-3 ${active ? 'bg-red-50 border-primary' : 'bg-surface border-border'}`}>
              <Text className={`text-sm font-extrabold ${active ? 'text-primary' : 'text-muted'}`}>PASSO {index + 1}</Text>
              <Text className="text-base text-foreground leading-6 mt-1">{step}</Text>
            </TouchableOpacity>
          );
        })}

        <Text className="text-2xl font-bold text-foreground mt-4 mb-3">Dicas da chef</Text>
        {lesson.tips.map((tip) => (
          <View key={tip} className="bg-surface border border-border rounded-2xl p-4 mb-3">
            <Text className="text-base text-foreground leading-6">{tip}</Text>
          </View>
        ))}
      </ScrollView>
    </ScreenContainer>
  );
}
