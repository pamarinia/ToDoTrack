<template>
  <div class="flex h-full w-full">
    <div class="flex rounded-lg m-4 w-1/2 bg-black items-center justify-center">
      <img src="~/assets/LogoHome.png" />
    </div>

    <div class="p-4 flex justify-center items-center w-1/2">
      <div class="w-96">
        <p class="text-3xl font-bold">Productive Mind</p>
        <p class="py-4">
          With only the features you need, Organic Mind is customized for
          individuals seeking a stress-free way to stay focused on their goals,
          projects and tasks.
        </p>
        <NuxtLink
          to="/signup"
          class="p-2 flex items-center justify-center bg-amber-400 rounded-lg"
          >Get Started</NuxtLink
        >

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
