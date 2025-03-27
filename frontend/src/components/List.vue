<script setup>
const props = defineProps({
    operadoras: Array,
    searchQuery: String
})

</script>

<template>
    <div v-if="operadoras.length" class="container-operadora">
        <table>
            <thead>
            <tr>
                <th>Registro ANS</th>
                <th>Razão Social</th>
                <th>CNPJ</th>
                <th>Nome Fantasia</th>
                <th>Modalidade</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="operadora in props.operadoras" :key="operadora.id">
                <td>{{ operadora.registro_ans }}</td>
                <td>{{ operadora.razao_social }}</td>
                <td>{{ operadora.cnpj }}</td>
                <td>{{ operadora.nome_fantasia }}</td>
                <td>{{ operadora.modalidade }}</td>
            </tr>
            </tbody>
        </table>
    </div>
    <p v-else-if="props.searchQuery">Nenhuma operadora encontrada.</p>
</template>

<style scoped>
.container-operadora {
  background-color: rgba(255, 255, 255, 0.87);
  color: black;
  border-radius: 1rem;
  padding: 0.6rem;
  box-shadow: 1rem;
}
th, td {
  font-size: 14px;
  border: 1px solid black; /* Bordas nas células */
  padding: 5px;
  text-align: center;
}
</style>