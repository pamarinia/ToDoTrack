<template>
  <div
    class="flex flex-col justify-between w-96 bg-zinc-100 p-3 m-3 rounded-lg"
  >
    <div>
      <div class="pb-2 flex justify-between">
        <p class="font-bold">Task:</p>
        <IconsClose @click="closeNewTask" />
      </div>

      <!-- Conditionally render inputs or task details -->
      <input
        v-if="isNewTask"
        v-model="newTask.title"
        placeholder="Title"
        class="p-2 mb-4 border border-zinc-200 rounded-lg w-full"
      />
      <div v-else class="p-2 mb-4 border border-zinc-200 rounded-lg">
        {{ task.title }}
      </div>

      <textarea
        v-if="isNewTask"
        v-model="newTask.description"
        placeholder="Description"
        class="p-2 mb-4 w-full h-32 border border-zinc-200 rounded-lg"
      ></textarea>

      <div v-else class="p-2 mb-4 h-32 border border-zinc-200 rounded-lg">
        {{ task.description }}
      </div>

      <div class="flex items-center mb-2">
        <p class="w-20">List</p>
        <div class="flex items-center p-2 border border-zinc-200 rounded-lg">
          <p class="pr-2">Personnal</p>
          <IconsArrowDown />
        </div>
      </div>

      <!-- <div class="flex items-center">
        <p class="w-20">Due Date</p>
        <div class="flex items-center p-2 border border-zinc-200 rounded-lg">
          <input
            v-if="isNewTask"
            v-model="newTask.date"
            type="date"
            class="appearance-none"
          />
          <p v-else class="pr-2">{{ task.date }}</p>
          <IconsArrowDown />
        </div>
      </div> -->
      <div class="flex items-center">
        <p class="w-20">Due Date</p>
        <input
          v-if="isNewTask"
          v-model="newTask.date"
          type="date"
          class="appearance-none flex items-center p-2 border border-zinc-200 rounded-lg"
        />
        <p v-else class="pr-2">{{ task.date }}</p>
      </div>
    </div>

    <div>
      <div class="px-2 flex justify-between">
        <div
          class="w-40 flex items-center justify-center border border-zinc-200 rounded-lg"
        >
          Delete Task
        </div>
        <div
          class="w-40 p-2 flex items-center justify-center bg-amber-400 border border-zinc-200 rounded-lg"
        >
          Save Changes
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const isNewTaskVisible = useIsNewTaskVisible();

function closeNewTask() {
  isNewTaskVisible.value = false;
  console.log(isNewTaskVisible.value);
}

// const route = useRoute();
const isNewTask = ref(false);

const { data: task } = await useFetch(
  "http://127.0.0.1:8000/api/v1/todolist/tasks/1/"
);

const newTask = ref({
  title: "",
  description: "",
  date: "",
});
</script>
