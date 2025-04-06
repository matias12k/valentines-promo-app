<template>
  <div class="admin-login">
    <h1>Admin Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    ...mapActions(['setAdminToken']),
    async login() {
      try {
        const response = await axios.post('/api/admin/login/', {
          email: this.email,
          password: this.password
        });
        this.setAdminToken(response.data.token);
        this.$router.push('/admin/dashboard');
      } catch (error) {
        this.errorMessage = 'Invalid email or password.';
      }
    }
  }
};
</script>

<style scoped>
.admin-login {
  max-width: 400px;
  margin: auto;
}
.error {
  color: red;
}
</style>