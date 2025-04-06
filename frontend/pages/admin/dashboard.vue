<template>
  <div class="dashboard">
    <h1>Admin Dashboard</h1>
    <button @click="generateWinner" class="generate-winner-button">Generar Ganador</button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

export default {
  data() {
    return {
      message: ''
    };
  },
  computed: {
    ...mapState(['isAuthenticated'])
  },
  methods: {
    async generateWinner() {
      try {
        const response = await axios.post('/api/generate-winner/', {}, {
          headers: {
            Authorization: `Bearer ${this.$store.state.token}`
          }
        });
        this.message = response.data.message;
      } catch (error) {
        this.message = 'Error al generar el ganador. Inténtalo de nuevo.';
      }
    }
  },
  mounted() {
    if (!this.isAuthenticated) {
      this.$router.push('/admin/login');
    }
  }
};
</script>

<style scoped>
.dashboard {
  text-align: center;
  margin-top: 20px;
}

.generate-winner-button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>