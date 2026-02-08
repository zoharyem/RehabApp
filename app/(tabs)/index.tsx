import { LinearGradient } from "expo-linear-gradient";
import { StyleSheet, Text, View } from "react-native";

/** ==================== Sample Data =======================*/
const name = "Zohar";
const routines = [
  {
    name: "Shoulder Streches",
    image: null,
    status: "Incompete",
    exercises: ["Overhead Strech", "External Rotation"],
  },
  {
    name: "Shoulder Stength Work",
    image: null,
    status: "Complete",
    exercises: ["Bench Press", "Seated Row"],
  },
];
/** ========================================================*/

export default function Index() {
  return (
    <LinearGradient
      colors={["#1e3a8a", "#3b82f6", "#60a5fa"]}
      style={styles.gradient}
    >
      <View style={styles.view}>
        <Text style={styles.title}>Welcome back, {name}</Text>
        <Text style={styles.text}>Here's whats on for today.</Text>
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  // A style sheet defining the styles of the text, view and gradient.
  gradient: {
    flex: 1,
  },
  text: {
    color: "#fff",
    fontSize: 16,
  },
  title: {
    color: "#fff",
    fontSize: 32,
    fontWeight: "700",
    marginTop: 60,
    marginBottom: 20,
    paddingHorizontal: 20,
    letterSpacing: 0.5,
  },
  view: {
    flex: 1,
    alignItems: "center",
  },
});
