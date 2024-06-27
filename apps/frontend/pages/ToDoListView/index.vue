<template>
  <div class="flex">
    <Menu />
    <TasksList />
    <Task v-show="isNewTaskVisible" />
    <Task v-show="isDetailTaskVisible" />
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();
const isDetailTaskVisible = useIsDetailTaskVisible();

console.log(isNewTaskVisible.value);
</script>
