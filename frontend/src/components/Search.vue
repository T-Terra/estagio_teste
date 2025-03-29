<script setup>
import List from "./List.vue";
import { ref } from "vue"
import axios from "axios";
    
const searchQuery = ref("")
const operadoras = ref([])
const statusResponse = ref(200)

const apiUrl = import.meta.env.VITE_URL_API

const fetchOperadoras = async () => {
  if (searchQuery.value === "") {
    operadoras.value = []
    return
  } else {
    try {
      const response = await axios.get(
        `${apiUrl}/api/list/?razao_social__icontains=${searchQuery.value}`
      )
      operadoras.value = response.data
      statusResponse.value = response.status
    } catch (error) {
      console.error("Erro ao buscar operadoras:", error)
    }
  }
}
</script>

<template>
    <div>
      <input
        class="input"
        v-model="searchQuery"
        placeholder="Digite para buscar..."
      />
      <button class="btn" @click="fetchOperadoras">Buscar</button>
      <List :operadoras="operadoras" :searchQuery="searchQuery" :statusResponse="statusResponse"/>
    </div>
</template>

<style scoped>
.input {
  padding: 0.5rem;
  margin-bottom: 2rem;
}
</style>
  