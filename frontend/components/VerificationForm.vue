<template>
  <div class="verification-form">
    <h2>Verificación de Email</h2>
    <form @submit.prevent="verifyEmail">
      <div>
        <label for="password">Nueva Contraseña:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="confirmPassword">Confirmar Contraseña:</label>
        <input type="password" v-model="confirmPassword" required />
      </div>
      <button type="submit">Establecer Contraseña</button>
    </form>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    <div v-if="successMessage" class="success">{{ successMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      password: '',
      confirmPassword: '',
      errorMessage: '',
      successMessage: '',
    };
  },
  computed: {
    ...mapGetters(['getToken']),
  },
  methods: {
    async verifyEmail() {
      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Las contraseñas no coinciden.';
        return;
      }

      const token = this.$route.query.token; // Obtener el token de la URL
      try {
        const response = await axios.post('/api/verify-email/', {
          token,
          password: this.password,
        });
        this.successMessage = 'Contraseña establecida con éxito. Puedes iniciar sesión ahora.';
        this.errorMessage = '';
      } catch (error) {
        this.errorMessage = error.response.data.detail || 'Error al verificar el email.';
        this.successMessage = '';
      }
    },
  },
};
</script>

<style scoped>
.verification-form {
  max-width: 400px;
  margin: auto;
}
.error {
  color: red;
}
.success {
  color: green;
}
</style>