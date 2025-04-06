import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/', // Cambia esto según la URL de tu backend
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para manejar el token de autenticación
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token'); // Asumiendo que guardas el token en localStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// Interceptor para manejar respuestas de error
apiClient.interceptors.response.use(response => {
  return response;
}, error => {
  if (error.response && error.response.status === 401) {
    // Manejar el error de no autorizado (401)
    console.error('No autorizado, redirigiendo al login...');
    // Aquí puedes redirigir al usuario al login o mostrar un mensaje
  }
  return Promise.reject(error);
});

export default apiClient;