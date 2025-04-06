export default {
  head: {
    title: 'Valentines Giveaway App',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Sorteo de San Valentín del hotel' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  css: [
    '@/assets/styles/main.css'
  ],
  plugins: [
    '@/plugins/axios'
  ],
  modules: [
    
    '@nuxtjs/auth-next'
  ],
  axios: {
    baseURL: 'http://localhost:8000/api/', // Cambia esto según tu configuración
  },
  build: {
    extend(config, ctx) {
    }
  },
  router: {
    middleware: ['auth']
  }
}