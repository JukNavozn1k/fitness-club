import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AuthProvider } from '@/contexts/AuthContext'
import { PrivateRoute } from '@/components/PrivateRoute'

import { Toaster } from 'sonner'

import Sidebar from "@/components/ui/sidebar"
import MobileNavbar from "@/components/ui/navbar"
import Login from '@/pages/login'
import Home from '@/pages/home'
import NotFound from '@/pages/404'
import Schedule from '@/pages/schedule'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
      <Toaster/>
      <Sidebar />
      <div className='md:ml-[var(--sidebar-width,256px)] transition-all duration-200'>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/" element={<Home />} />
          <Route path="/schedule" element={<Schedule />} />
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Routes>
                  {/* <Route path="/me" element={<Home />} /> */}
                </Routes>
              </PrivateRoute>
            }
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
        </div>
        <MobileNavbar />
      </BrowserRouter>
     
    </AuthProvider>
  )
}

export default App
