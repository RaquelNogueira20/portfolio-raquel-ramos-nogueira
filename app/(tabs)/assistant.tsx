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
