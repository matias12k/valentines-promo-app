<template>
  <div class="registration-form">
    <h2>Inscripción para el Sorteo de San Valentín</h2>
    <form @submit.prevent="register">
      <div>
        <label for="name">Nombre:</label>
        <input type="text" v-model="name" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="personalData">Datos Personales:</label>
        <textarea v-model="personalData" required></textarea>
      </div>
      <button type="submit">Registrar</button>
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
      <div v-if="successMessage" class="success">{{ successMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      personalData: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async register() {
      this.errorMessage = '';
      this.successMessage = '';
      try {
        const response = await axios.post('/api/register/', {
          name: this.name,
          email: this.email,
          personalData: this.personalData
        });
        this.successMessage = 'Registro exitoso. Revisa tu correo para verificar tu cuenta.';
        this.name = '';
        this.email = '';
        this.personalData = '';
      } catch (error) {
        if (error.response && error.response.data) {
          this.errorMessage = error.response.data.detail || 'Error en el registro. Intenta de nuevo.';
        } else {
          this.errorMessage = 'Error en el registro. Intenta de nuevo.';
        }
      }
    }
  }
};
</script>

<style scoped>
.registration-form {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.error {
  color: red;
}

.success {
  color: green;
}
</style>