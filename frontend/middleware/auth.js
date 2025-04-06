export default function ({ store, redirect }) {
  // Check if the user is authenticated as an admin
  if (!store.state.auth.isAdminAuthenticated) {
    // If not authenticated, redirect to the admin login page
    return redirect('/admin/login');
  }
}