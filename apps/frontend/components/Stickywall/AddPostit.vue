<template>
  <div class="min-w-72 min-h-72 size-1/3 p-2 aspect-square" @click="addNewTask">
    <div
      class="size-full bg-zinc-300 rounded p-4 shadow-md flex items-center justify-center"
    >
      <IconsPlus class="size-16" />
    </div>
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();

function addNewTask() {
  isNewTaskVisible.value = true;
  console.log(isNewTaskVisible.value);
}
</script>
