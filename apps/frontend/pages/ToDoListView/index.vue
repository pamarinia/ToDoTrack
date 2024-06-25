<template>
  <div class="flex">
    <Menu />
    <TasksList />
    <Task v-show="isNewTaskVisible" />
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();

console.log(isNewTaskVisible.value);
</script>
