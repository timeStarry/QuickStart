import { defineStore } from 'pinia'

interface Todo {
  id: number
  title: string
  is_completed: boolean
}

export const useMainStore = defineStore('main', {
  state: () => ({
    todos: [] as Todo[]
  }),
  
  actions: {
    async addTodo(title: string) {
      // TODO: 实现添加待办的API调用
      this.todos.push({
        id: Date.now(),
        title,
        is_completed: false
      })
    },

    async toggleTodo(id: number) {
      // TODO: 实现更新待办状态的API调用
      const todo = this.todos.find(t => t.id === id)
      if (todo) {
        todo.is_completed = !todo.is_completed
      }
    }
  }
}) 