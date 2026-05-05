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
