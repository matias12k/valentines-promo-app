<template>
  <div class="verify">
    <h1>Verificación de Email</h1>
    <VerificationForm @verified="handleVerification" />
  </div>
</template>

<script>
import VerificationForm from '@/components/VerificationForm.vue';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  components: {
    VerificationForm,
  },
  setup() {
    const router = useRouter();
    const errorMessage = ref('');

    const handleVerification = async (token, password) => {
      try {
        await axios.post('/api/verify/', { token, password });
        alert('Tu cuenta ha sido verificada y la contraseña ha sido establecida.');
        router.push('/'); // Redirigir a la página principal o a donde desees
      } catch (error) {
        errorMessage.value = error.response.data.detail || 'Error en la verificación. Intenta de nuevo.';
      }
    };

    return {
      errorMessage,
      handleVerification,
    };
  },
};
</script>

<style scoped>
.verify {
  max-width: 400px;
  margin: auto;
  text-align: center;
}
</style>