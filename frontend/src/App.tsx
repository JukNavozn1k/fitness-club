import { BrowserRouter } from 'react-router-dom'
import Sidebar from "@/components/ui/Sidebar"
import MobileNavbar from "@/components/ui/navbar"
import Login from './pages/login'
import Home from './pages/home'

function App() {
  return (
    <BrowserRouter>
    <Sidebar />
    <div className='md:ml-[var(--sidebar-width,256px)] transition-all duration-200'>
      <Login />     
      </div>
      {/* Mobile Navigation */}
      <MobileNavbar />
     
    </BrowserRouter>
  )
}

export default App
