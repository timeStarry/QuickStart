<script setup lang="ts">
import { ref } from 'vue'
import { useMainStore } from '@/stores/useMainStore'

const store = useMainStore()
const newTodo = ref('')

const addTodo = async () => {
  if (!newTodo.value.trim()) return
  await store.addTodo(newTodo.value)
  newTodo.value = ''
}
</script>

<template>
  <div class="todo-widget bg-white rounded-lg shadow-lg p-6">
    <h2 class="text-xl font-bold mb-4">待办事项</h2>
    
    <form @submit.prevent="addTodo" class="mb-4">
      <div class="flex gap-2">
        <input
          v-model="newTodo"
          type="text"
          placeholder="添加新待办..."
          class="flex-1 px-3 py-2 border rounded-lg"
        />
        <button
          type="submit"
          class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
        >
          添加
        </button>
      </div>
    </form>

    <ul class="space-y-2">
      <li
        v-for="todo in store.todos"
        :key="todo.id"
        class="flex items-center gap-2 p-2 hover:bg-gray-50 rounded"
      >
        <input
          type="checkbox"
          :checked="todo.is_completed"
          @change="store.toggleTodo(todo.id)"
          class="w-4 h-4"
        />
        <span :class="{ 'line-through': todo.is_completed }">
          {{ todo.title }}
        </span>
      </li>
    </ul>
  </div>
</template> 