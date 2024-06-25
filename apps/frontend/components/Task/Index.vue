<template>
  <div
    class="flex flex-col justify-between w-96 bg-zinc-100 p-3 m-3 rounded-lg"
  >
    <div>
      <div class="pb-2 flex justify-between">
        <p class="font-bold">Task:</p>
        <IconsClose @click="closeNewTask" />
      </div>

      <div class="p-2 mb-4 border border-zinc-200 rounded-lg">Title</div>

      <div class="p-2 mb-4 h-32 border border-zinc-200 rounded-lg">
        Description
      </div>

      <div class="flex items-center mb-2">
        <p class="w-20">List</p>
        <div class="flex items-center p-2 border border-zinc-200 rounded-lg">
          <p class="pr-2">Personnal</p>
          <IconsArrowDown />
        </div>
      </div>
      <div class="flex items-center">
        <p class="w-20">Due Date</p>
        <div class="flex items-center p-2 border border-zinc-200 rounded-lg">
          <p class="pr-2">11-03-22</p>
          <IconsArrowDown />
        </div>
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
</script>
