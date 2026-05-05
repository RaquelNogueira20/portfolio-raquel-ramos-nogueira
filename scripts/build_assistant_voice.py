from pathlib import Path

ROOT = Path('/home/ubuntu/culinaria_live_app')

def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')

write('app/(tabs)/assistant.tsx', r'''
import { useState } from 'react';
import { FlatList, KeyboardAvoidingView, Platform, Text, TextInput, TouchableOpacity, View } from 'react-native';

import { IconSymbol } from '@/components/ui/icon-symbol';
import { ScreenContainer } from '@/components/screen-container';
import { answerCookingQuestion, quickQuestions } from '@/lib/assistant';
import { lessons } from '@/lib/culinary-data';

type Message = {
  id: string;
  role: 'assistant' | 'user';
  text: string;
};

const initialMessages: Message[] = [
  {
    id: 'intro',
    role: 'assistant',
    text: 'Estou dentro da aula para ajudar com a receita. Pergunte sobre substituições, tempo, ponto de cozimento ou organização da bancada.',
  },
];

export default function AssistantScreen() {
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [question, setQuestion] = useState('');
  const lesson = lessons[0];

  const sendQuestion = (value = question) => {
    const trimmed = value.trim();
    if (!trimmed) return;
    const userMessage: Message = { id: `u-${Date.now()}`, role: 'user', text: trimmed };
    const assistantMessage: Message = { id: `a-${Date.now()}`, role: 'assistant', text: answerCookingQuestion(trimmed, lesson.id) };
    setMessages((current) => [assistantMessage, userMessage, ...current]);
    setQuestion('');
  };

  return (
    <ScreenContainer className="px-5 pt-3">
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} className="flex-1">
        <Text className="text-sm font-semibold text-primary">Assistente inteligente de cozinha</Text>
        <Text className="text-4xl font-extrabold text-foreground mt-1 leading-10">Um ChatGPT focado na receita da aula</Text>
        <Text className="text-base text-muted mt-3 leading-6">As respostas são contextualizadas para {lesson.title}, com foco prático no que acontece durante o preparo.</Text>

        <View className="bg-surface border border-border rounded-3xl p-4 mt-5">
          <Text className="text-sm font-bold text-primary">Perguntas rápidas</Text>
          <View className="flex-row flex-wrap gap-2 mt-3">
            {quickQuestions.map((item) => (
              <TouchableOpacity key={item} activeOpacity={0.76} onPress={() => sendQuestion(item)} className="bg-red-50 border border-red-100 rounded-full px-4 py-3">
                <Text className="text-primary font-bold text-sm">{item}</Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>

        <View className="flex-row bg-surface border border-border rounded-full px-4 py-2 items-center mt-4 mb-4">
          <IconSymbol name="sparkles" size={24} color="#FF0000" />
          <TextInput
            value={question}
            onChangeText={setQuestion}
            onSubmitEditing={() => sendQuestion()}
            returnKeyType="send"
            placeholder="Pergunte algo sobre a receita"
            placeholderTextColor="#7A4A4A"
            className="flex-1 px-3 py-3 text-foreground"
          />
          <TouchableOpacity activeOpacity={0.75} onPress={() => sendQuestion()} className="bg-primary rounded-full px-4 py-3">
            <Text className="text-white font-extrabold">Enviar</Text>
          </TouchableOpacity>
        </View>

        <FlatList
          data={messages}
          inverted
          keyExtractor={(item) => item.id}
          showsVerticalScrollIndicator={false}
          renderItem={({ item }) => {
            const assistant = item.role === 'assistant';
            return (
              <View className={`mb-3 rounded-3xl p-4 border ${assistant ? 'bg-surface border-border mr-8' : 'bg-primary border-primary ml-8'}`}>
                <Text className={`text-xs font-extrabold mb-1 ${assistant ? 'text-primary' : 'text-white/80'}`}>{assistant ? 'ASSISTENTE DA RECEITA' : 'VOCÊ'}</Text>
                <Text className={`text-base leading-6 ${assistant ? 'text-foreground' : 'text-white'}`}>{item.text}</Text>
              </View>
            );
          }}
        />
      </KeyboardAvoidingView>
    </ScreenContainer>
  );
}
''')

write('app/(tabs)/voice.tsx', r'''
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
''')

print('Telas de assistente e voz criadas com sucesso.')
