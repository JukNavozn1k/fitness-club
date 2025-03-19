import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from '@/contexts/AuthContext'
import { PrivateRoute } from '@/components/PrivateRoute'
import Sidebar from "@/components/ui/sidebar"
import MobileNavbar from "@/components/ui/navbar"
import Login from './pages/login'
import Home from './pages/home'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/*"
            element={
              <PrivateRoute>
                <>
                  <Sidebar />
                  <div className='md:ml-[var(--sidebar-width,256px)] transition-all duration-200'>
                    <Routes>
                      <Route path="/" element={<Home />} />
                      <Route path="*" element={<Navigate to="/" />} />
                    </Routes>
                  </div>
                  <MobileNavbar />
                </>
              </PrivateRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App
