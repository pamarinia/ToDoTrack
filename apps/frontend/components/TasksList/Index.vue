<template>
  <div class="m-3 p-3 flex-grow">
    <div class="flex pb-6">
      <p class="font-bold text-4xl pr-10">Today</p>
      <p class="text-3xl px-2 rounded border border-zinc-200">5</p>
    </div>

    <div
      class="flex items-center p-2 rounded border border-zinc-200"
      @click="addNewTask"
    >
      <IconsPlus />
      <div class="pl-3">Add New Task</div>
    </div>

    <div
      v-for="task in tasks"
      :key="task.id"
      class="flex items-center p-2 justify-between"
    >
      <div class="flex items-center">
        <p class="rounded border size-4 border-zinc-200" />
        <p class="pl-3">{{ task.title }}</p>
      </div>
      <IconsArrow />
    </div>

    <div class="bg-gray-200 h-px w-full" />

    <div class="flex items-center p-2 justify-between">
      <div class="flex items-center">
        <p class="rounded border size-4 border-zinc-200" />
        <p class="pl-3">Create a database of guest authors</p>
      </div>
      <IconsArrow />
    </div>

    <div class="bg-gray-200 h-px w-full" />

    <div class="flex items-center p-2 justify-between">
      <div class="flex items-center">
        <p class="rounded border size-4 border-zinc-200" />
        <p class="pl-3">Renew driver's license</p>
      </div>
      <IconsArrow />
    </div>
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();

function addNewTask() {
  isNewTaskVisible.value = true;
  console.log(isNewTaskVisible.value);
}

const { data: tasks } = await useFetch(
  "http://127.0.0.1:8000/api/v1/todolist/newest/"
);
</script>
