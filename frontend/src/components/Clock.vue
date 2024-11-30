<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import dayjs from 'dayjs'

const time = ref(new Date())

let timer: number
onMounted(() => {
  timer = setInterval(() => {
    time.value = new Date()
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>

<template>
  <div class="clock-widget bg-white rounded-lg shadow-lg p-6 text-center">
    <div class="text-4xl font-bold">
      {{ dayjs(time).format('HH:mm:ss') }}
    </div>
    <div class="text-gray-500 mt-2">
      {{ dayjs(time).format('YYYY-MM-DD') }}
    </div>
  </div>
</template> 