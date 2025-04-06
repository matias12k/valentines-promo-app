<template>
  <div class="register">
    <h1>Registro para el Sorteo de San Valentín</h1>
    <RegistrationForm @submit="handleSubmit" />
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="success" class="success">{{ success }}</div>
  </div>
</template>

<script>
import RegistrationForm from '@/components/RegistrationForm.vue';
import axios from 'axios';

export default {
  components: {
    RegistrationForm,
  },
  data() {
    return {
      error: null,
      success: null,
    };
  },
  methods: {
    async handleSubmit(formData) {
      try {
        const response = await axios.post('/api/register/', formData);
        this.success = 'Registro exitoso. Revisa tu correo para verificar tu cuenta.';
        this.error = null;
      } catch (err) {
        this.error = err.response.data.detail || 'Error en el registro. Intenta de nuevo.';
        this.success = null;
      }
    },
  },
};
</script>

<style scoped>
.register {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.error {
  color: red;
}

.success {
  color: green;
}
</style>