<template>
  <div class="flex">
    <Menu class="flex-shrink-0" />
    <Stickywall />
    <Task v-show="isNewTaskVisible" />
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();

console.log(isNewTaskVisible.value);
</script>
