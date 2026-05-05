import { useState } from 'react';
import { Alert, ScrollView, Text, TouchableOpacity, View } from 'react-native';
import * as Speech from 'expo-speech';

import { IconSymbol } from '@/components/ui/icon-symbol';
import { ScreenContainer } from '@/components/screen-container';
import { answerCookingQuestion, voiceCommands } from '@/lib/assistant';
import { lessons } from '@/lib/culinary-data';

export default function VoiceScreen() {
  const [listening, setListening] = useState(false);
  const [lastCommand, setLastCommand] = useState('Toque em um comando para simular a fala durante a aula.');
  const [answer, setAnswer] = useState('A resposta por voz aparecerá aqui para você continuar cozinhando sem tocar muito no celular.');
  const lesson = lessons[0];

  const runCommand = async (command: string) => {
    setListening(true);
    const response = answerCookingQuestion(command, lesson.id);
    setLastCommand(command);
    setAnswer(response);
    try {
      const isSpeaking = await Speech.isSpeakingAsync();
      if (isSpeaking) {
        await Speech.stop();
      }
      Speech.speak(response, {
        language: 'pt-BR',
        rate: 0.94,
        pitch: 1,
        onDone: () => setListening(false),
        onError: () => setListening(false),
      });
    } catch {
      setListening(false);
      Alert.alert('Voz indisponível', 'A orientação foi exibida em texto. Em alguns dispositivos iOS, o modo silencioso pode impedir a fala.');
    }
  };

  const stopSpeaking = async () => {
    await Speech.stop();
    setListening(false);
  };

  return (
    <ScreenContainer className="px-5 pt-3">
      <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{ paddingBottom: 34 }}>
        <Text className="text-sm font-semibold text-primary">Voz assistente</Text>
        <Text className="text-4xl font-extrabold text-foreground mt-1 leading-10">Comando por voz útil na cozinha</Text>
        <Text className="text-base text-muted mt-3 leading-6">A tela exibe um ícone de pessoa falando e simula comandos curtos para seguir a receita sem perder o ritmo.</Text>

        <View className="bg-primary rounded-[36px] p-6 mt-6 items-center">
          <View className="w-36 h-36 rounded-full bg-white items-center justify-center border-8 border-red-200">
            <IconSymbol name="person.wave.2.fill" size={82} color="#FF0000" />
          </View>
          <Text className="text-white text-2xl font-extrabold mt-5">{listening ? 'Falando com você' : 'Pronto para ouvir'}</Text>
          <Text className="text-white/80 text-center mt-2 leading-5">Use comandos simples como próximo passo, repetir ingredientes e ponto correto.</Text>
        </View>

        <View className="bg-surface border border-border rounded-3xl p-5 mt-6">
          <Text className="text-xs font-extrabold text-primary">ÚLTIMO COMANDO</Text>
          <Text className="text-xl font-bold text-foreground mt-2">{lastCommand}</Text>
          <Text className="text-base text-muted leading-6 mt-4">{answer}</Text>
        </View>

        <Text className="text-2xl font-bold text-foreground mt-7 mb-3">Comandos rápidos</Text>
        {voiceCommands.map((command) => (
          <TouchableOpacity key={command} activeOpacity={0.8} onPress={() => runCommand(command)} className="bg-surface border border-border rounded-2xl p-4 mb-3 flex-row items-center">
            <View className="w-11 h-11 rounded-full bg-red-50 items-center justify-center mr-3">
              <IconSymbol name="mic.fill" size={24} color="#FF0000" />
            </View>
            <Text className="flex-1 text-base font-bold text-foreground">{command}</Text>
          </TouchableOpacity>
        ))}

        <TouchableOpacity activeOpacity={0.8} onPress={stopSpeaking} className="bg-foreground rounded-full py-5 items-center mt-3">
          <Text className="text-background font-extrabold">Parar fala</Text>
        </TouchableOpacity>
      </ScrollView>
    </ScreenContainer>
  );
}
