import { useState } from 'react'
import { BrowserRouter } from 'react-router-dom'


import './App.css'

import  Sidebar from '@/components/ui/sidebar'
import MobileNavbar from './components/ui/navbar'
function App() {
 

  return (
    <>
      <BrowserRouter>
      <Sidebar />
      <MobileNavbar/>
      </BrowserRouter>
    </>
  )
}

export default App
