<script setup lang="ts">
import { onMounted } from 'vue'
import { useMainStore } from './stores/useMainStore'
import Clock from './components/Clock.vue'
import TodoList from './components/TodoList.vue'

const store = useMainStore()

onMounted(() => {
  store.fetchTodos()
  store.fetchWidgets()
})
</script>

<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Clock />
        <TodoList />
      </div>
    </div>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
