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
