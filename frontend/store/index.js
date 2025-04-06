import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    isAuthenticated: false,
    admin: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user
      state.isAuthenticated = !!user
    },
    SET_ADMIN(state, admin) {
      state.admin = admin
    },
    LOGOUT(state) {
      state.user = null
      state.isAuthenticated = false
      state.admin = null
    },
  },
  actions: {
    async register({ commit }, userData) {
      try {
        const response = await axios.post('/api/register/', userData)
        return response.data
      } catch (error) {
        throw error.response.data
      }
    },
    async verifyEmail({ commit }, tokenData) {
      try {
        const response = await axios.post('/api/verify-email/', tokenData)
        return response.data
      } catch (error) {
        throw error.response.data
      }
    },
    async setPassword({ commit }, passwordData) {
      try {
        const response = await axios.post('/api/set-password/', passwordData)
        return response.data
      } catch (error) {
        throw error.response.data
      }
    },
    async adminLogin({ commit }, credentials) {
      try {
        const response = await axios.post('/api/admin/login/', credentials)
        commit('SET_ADMIN', response.data)
        commit('SET_USER', response.data.user)
      } catch (error) {
        throw error.response.data
      }
    },
    async generateWinner({ commit }) {
      try {
        const response = await axios.post('/api/admin/generate-winner/')
        return response.data
      } catch (error) {
        throw error.response.data
      }
    },
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    user: state => state.user,
    admin: state => state.admin,
  },
})