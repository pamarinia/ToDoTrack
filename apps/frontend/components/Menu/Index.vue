<template>
  <div v-show="isMenuVisible" class="bg-zinc-100 w-1/6 rounded-lg m-3 p-3">
    <div class="flex justify-between">
      <p class="font-bold">Menu</p>
      <IconsLogoMenu @click="toggleMenu" />
    </div>
    <div class="py-4">
      <div class="flex items-center border border-zinc-200 rounded px-2 py-1">
        <IconsSearch />
        <p class="px-2">Search</p>
      </div>
    </div>
    <MenuTasks />
    <MenuLists />
    <div class="h-10" />
    <div class="flex items-center py-1">
      <IconsSettings />
      <p class="px-2">Settings</p>
    </div>
    <div class="flex items-center py-1">
      <IconsSignout />
      <p class="px-2">Sign out</p>
    </div>
  </div>

  <div v-show="!isMenuVisible" class="w-16 m-3 p-3">
    <IconsLogoMenu @click="toggleMenu" />
  </div>
</template>

<script setup>
import { ref } from "vue";

const isMenuVisible = ref(true);

function toggleMenu() {
  isMenuVisible.value = !isMenuVisible.value;
}
</script>
