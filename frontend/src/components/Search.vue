<script setup>
import List from "./List.vue";
import { ref, watch } from "vue"
import axios from "axios";
    
const searchQuery = ref("")
const operadoras = ref([])

const apiUrl = import.meta.env.VITE_URL_API

const fetchOperadoras = async () => {
    if (searchQuery.value.length < 2) {
      operadoras.value = []
      return
    }

    try {
      const response = await axios.get(
        `${apiUrl}/api/list/?razao_social__icontains=${searchQuery.value}`
      )
      operadoras.value = response.data
    } catch (error) {
      console.error("Erro ao buscar operadoras:", error)
    }
}

watch(searchQuery, () => {
  fetchOperadoras()
})
</script>

<template>
    <div>
      <input
        class="input"
        v-model="searchQuery"
        @input="fetchOperadoras"
        placeholder="Digite para buscar..."
      />
      <List :operadoras="operadoras" :searchQuery="searchQuery"/>
    </div>
</template>

<style scoped>
.input {
  padding: 0.5rem;
  margin-bottom: 2rem;
}
</style>
  