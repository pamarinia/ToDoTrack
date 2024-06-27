<template>
  <div>
    <form @submit.prevent="signup">
      <input v-model="email" type="email" placeholder="Email" required />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
      />
      <button type="submit">Sign Up</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const error = ref<string | null>(null); // Ajout d'une référence pour gérer les erreurs

const router = useRouter();

async function signup() {
  try {
    const response = await $fetch("http://127.0.0.1:8000/api/v1/users/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json", // Ajout de l'en-tête Content-Type
      },
      body: JSON.stringify({
        email: email.value, // Assurez-vous que ce champ correspond à ce que l'API attend
        username: "polochon",
        password: password.value,
      }),
    });
    console.log("Signup success", response);
    // Rediriger l'utilisateur après une inscription réussie
    router.push("/signin");
  } catch (err) {
    console.error("Signup error:", err);
    if (err.response && err.response.data) {
      // Extraire le message d'erreur spécifique de la réponse
      error.value =
        err.response.data.message || "An error occurred during signup.";
    } else {
      error.value = "An unexpected error occurred. Please try again.";
    }
  }
}
</script>
