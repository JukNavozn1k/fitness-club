import { BrowserRouter } from 'react-router-dom'


import Home from './pages/Home'

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen flex flex-col">
        <Home />     
      </div>
    </BrowserRouter>
  )
}

export default App
