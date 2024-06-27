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

    <div v-for="task in tasks" :key="task.id">
      <div
        class="flex items-center p-2 justify-between"
        @click="openDetailTask(task.id)"
      >
        <div class="flex items-center">
          <p class="rounded border size-4 border-zinc-200" />
          <p class="pl-3">{{ task.title }}</p>
          <p class="pl-3">{{ task.id }}</p>
        </div>
        <IconsArrow />
      </div>

      <div class="bg-gray-200 h-px w-full" />
    </div>
  </div>
</template>

<script setup>
const { data: tasks } = await useFetch(
  "http://127.0.0.1:8000/api/v1/todolist/tasks"
);

const emit = defineEmits(["addNewTask", "openDetailTask"]);

const isNewTaskVisible = useIsNewTaskVisible();

function addNewTask() {
  isNewTaskVisible.value = true;
}

const isDetailTaskVisible = useIsDetailTaskVisible();
const isTaskid = useTaskId();

function openDetailTask(TaskId) {
  isTaskid.value = TaskId;
  isDetailTaskVisible.value = true;
}


</script>
