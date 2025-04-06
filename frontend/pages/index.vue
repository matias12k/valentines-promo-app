<template>
  <div class="container">
    <h1>Bienvenido al Sorteo de San Valentín</h1>
    <p>Participa para tener la oportunidad de ganar una estancia en nuestro hotel.</p>
    <nuxt-link to="/register" class="btn">Inscríbete Ahora</nuxt-link>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Sorteo de San Valentín',
      meta: [
        { hid: 'description', name: 'description', content: 'Participa en nuestro sorteo de San Valentín y gana una estancia en el hotel.' }
      ]
    }
  }
}
</script>

<style scoped>
.container {
  text-align: center;
  margin-top: 50px;
}

.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #ff4081;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #e91e63;
}
</style>