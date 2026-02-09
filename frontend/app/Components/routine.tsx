import { StyleSheet, Text, View } from "react-native";

export default function Routine({ name, status, exercises }: routine) {
  return (
    <View style={styles.card}>
      <View style={styles.header}>
        <Text style={styles.name}>{name}</Text>
        <Text style={styles.status}>{status}</Text>
      </View>
      <Text style={styles.exercises}>{exercises.length} exercises</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: "#fff",
    borderRadius: 12,
    padding: 16,
    marginHorizontal: 20,
    marginBottom: 12,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3, // For Android shadow
  },
  header: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 8,
  },
  name: {
    fontSize: 18,
    fontWeight: "600",
    color: "#1e3a8a",
  },
  status: {
    fontSize: 14,
    color: "#666",
    fontWeight: "500",
  },
  exercises: {
    fontSize: 14,
    color: "#999",
  },
});

type routine = {
  name: string;
  image: any;
  status: string;
  exercises: string[];
};
