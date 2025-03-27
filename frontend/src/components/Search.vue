<template>
    <div>
      <input
        class="input"
        v-model="searchQuery"
        @input="fetchOperadoras"
        placeholder="Digite para buscar..."
      />
      
      <ul v-if="operadoras.length">
        <li v-for="operadora in operadoras" :key="operadora.id">
          {{ operadora.nome_fantasia }} ({{ operadora.razao_social }})
        </li>
      </ul>
      
      <p v-else-if="searchQuery">Nenhuma operadora encontrada.</p>
    </div>
</template>
  
<script setup>
import { ref, watch } from "vue"
import axios from "axios";
    
const searchQuery = ref("")
const operadoras = ref([])

const fetchOperadoras = async () => {
    if (searchQuery.value.length < 2) {
        operadoras.value = []
        return
    }

    try {
        const response = await axios.get(`http://localhost:8000/api/list/?razao_social__icontains=${searchQuery.value}`)
        operadoras.value = response.data
    } catch (error) {
        console.error("Erro ao buscar operadoras:", error)
    }
}

watch(searchQuery, () => {
    fetchOperadoras()
})
</script>

<style scoped>
.input {
    padding: 0.5rem;
}
</style>
  