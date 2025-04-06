<template>
  <div class="admin-login">
    <h1>Admin Login</h1>
    <AdminLoginForm @login="handleLogin" />
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
  </div>
</template>

<script>
import AdminLoginForm from '@/components/AdminLoginForm.vue';
import axios from 'axios';

export default {
  components: {
    AdminLoginForm,
  },
  data() {
    return {
      errorMessage: '',
    };
  },
  methods: {
    async handleLogin(credentials) {
      try {
        const response = await axios.post('/api/admin/login/', credentials);
        // Store the token in local storage or Vuex store
        localStorage.setItem('adminToken', response.data.token);
        this.$router.push('/admin/dashboard');
      } catch (error) {
        this.errorMessage = 'Invalid credentials. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
.admin-login {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>