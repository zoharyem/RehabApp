import { HapticTab } from "@/app-example/components/haptic-tab";
import { Colors } from "@/app-example/constants/theme";
import Ionicons from "@expo/vector-icons/Ionicons";
import { Tabs } from "expo-router";
import React from "react";
import { useColorScheme } from "react-native";

export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors[colorScheme ?? "light"].tint,
        headerShown: false,
        tabBarButton: HapticTab,
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: "Home",
          tabBarIcon: ({ color }) => (
            <Ionicons size={28} name="home" color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="routines"
        options={{
          title: "Routines",
          tabBarIcon: ({ color }) => (
            <Ionicons size={28} name="barbell" color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="goals"
        options={{
          title: "Goals",
          tabBarIcon: ({ color }) => (
            <Ionicons size={28} name="trophy" color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="progress"
        options={{
          title: "Progress",
          tabBarIcon: ({ color }) => (
            <Ionicons size={28} name="analytics" color={color} />
          ),
        }}
      />
    </Tabs>
  );
}
