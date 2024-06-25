<template>
  <div class="py-2">
    <div>Tasks</div>
    <div class="flex justify-between p-2">
      <div class="flex items-center">
        <IconsDoubleArrow />
        <p class="px-2">Upcoming</p>
      </div>
      <p class="bg-zinc-200 rounded w-8 text-center">12</p>
    </div>
    <NuxtLink to="todolistview" class="flex justify-between p-2">
      <div class="flex items-center">
        <IconsCheckList />
        <p class="px-2">Today</p>
      </div>
      <p class="bg-zinc-200 rounded w-8 text-center">5</p>
    </NuxtLink>
    <div class="flex justify-between p-2">
      <div class="flex items-center">
        <IconsCalendar />
        <p class="px-2">Calendar</p>
      </div>
      <p />
    </div>
    <NuxtLink to="/stickywallview" class="flex justify-between p-2">
      <div to="/stickywallview" class="flex items-center">
        <IconsStickyWall />
        <p class="px-2">Sticky Wall</p>
      </div>
      <p />
    </NuxtLink>
  </div>
</template>
