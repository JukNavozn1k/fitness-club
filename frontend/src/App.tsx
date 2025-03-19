import { BrowserRouter } from 'react-router-dom'
import { AuthProvider } from '@/contexts/AuthContext'
import Sidebar from "@/components/ui/Sidebar"
import MobileNavbar from "@/components/ui/navbar"
import Login from './pages/login'
import Home from './pages/home'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Sidebar />
        <div className='md:ml-[var(--sidebar-width,256px)] transition-all duration-200'>
          <Home />     
        </div>
        {/* Mobile Navigation */}
        <MobileNavbar />
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App
