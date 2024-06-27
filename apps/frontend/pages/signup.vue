<template>
  <div class="flex h-full w-full">
    <div class="flex rounded-lg m-4 w-1/2 bg-black justify-center">
      <img src="~/assets/LogoHome.png" />
    </div>

    <div class="p-4 w-1/2 flex justify-center">
      <div class="w-96 h-full flex flex-col justify-center">
        <p class="py-2 text-3xl font-bold">Sign up</p>
        <form @submit.prevent="submitForm">
          <input
            v-model="email"
            type="email"
            class="p-2 mb-2 w-full border border-zinc-200 rounded-lg"
            placeholder="email@mail.com"
          />
          <input
            v-model="password1"
            type="password"
            class="p-2 mb-2 w-full border border-zinc-200 rounded-lg"
            placeholder="Password"
          />
          <input
            v-model="password2"
            type="password"
            class="p-2 mb-2 w-full border border-zinc-200 rounded-lg"
            placeholder="Confirm Password"
          />
          <div
            v-if="errors.length"
            class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl"
          >
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
          <button
            class="p-2 my-4 w-full flex items-center justify-center bg-amber-400 rounded-lg"
          >
            Sign up
          </button>
        </form>

        <div class="mb-4 flex justify-between items-center">
          <div class="bg-gray-200 h-px w-44" />
          <p>or</p>
          <div class="bg-gray-200 h-px w-44" />
        </div>
        <div class="flex">
          <div class="w-1/2 content-center">
            <button class="p-2 w-44 bg-zinc-200 text-center rounded-lg">
              Google
            </button>
          </div>
          <div class="w-1/2 flex justify-end">
            <button class="w-44 p-2 bg-zinc-200 text-center rounded-lg">
              Facebook
            </button>
          </div>
        </div>
        <div class="p-2 flex justify-center">
          <p class="mr-2">Already have an account?</p>
          <p>
            <NuxtLink to="/signin" class="text-blue-500 hover:underline"
              >Sign in</NuxtLink
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

interface User {
  email: string;
  password: string;
}

const router = useRouter();
const email: Ref<string> = ref("");
const password1: Ref<string> = ref("");
const password2: Ref<string> = ref("");
const errors: Ref<string[]> = ref([]);

async function submitForm() {
  try {
    const user: User = {
      email: email.value,
      password: password1.value,
    };

    await $fetch("http://127.0.0.1:8000/api/v1/users/", {
      method: "POST",
      body: JSON.stringify(user),
    }).then((response) => {
      console.log("response", response);
      router.push("/signin");
    });

    // Handle successful response
  } catch (error) {
    console.error("Error submitting form:", error);

    if (error instanceof Error) {
      // Check for error response structure
      const e = error as any; // Use `any` type temporarily
      if (
        e.response &&
        e.response.data &&
        typeof e.response.data.message === "string"
      ) {
        errors.value = [e.response.data.message];
      } else {
        errors.value = ["An unexpected error occurred. Please try again."];
      }
    } else {
      errors.value = ["An unexpected error occurred. Please try again."];
    }
  }
}
</script>
