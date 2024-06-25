<template>
  <div class="flex h-full w-full">
    <div class="flex rounded-lg m-4 w-1/2 bg-black justify-center">
      <img src="~/assets/LogoHome.png" />
    </div>

    <div class="p-4 w-1/2 flex justify-center">
      <div class="w-96 h-full flex flex-col justify-center">
        <p class="py-2 text-3xl font-bold">Sign in</p>
        <input
          type="email"
          class="p-2 mb-2 w-full border border-zinc-200 rounded-lg"
          placeholder="email@mail.com"
        />
        <input
          type="password"
          class="p-2 mb-2 w-full border border-zinc-200 rounded-lg"
          placeholder="Password"
        />
        <NuxtLink
          to="/todolistview"
          class="p-2 my-4 w-full flex items-center justify-center bg-amber-400 rounded-lg"
          >Sign in</NuxtLink
        >

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
          <p class="mr-2">Don't have an account?</p>
          <p>
            <NuxtLink to="/signup" class="text-blue-500 hover:underline"
              >Sign up</NuxtLink
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
