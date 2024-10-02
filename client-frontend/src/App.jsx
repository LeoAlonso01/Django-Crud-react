import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import { Users } from './pages/Users'
import { Products } from './pages/Products'
import { Sales } from './pages/Sales'
import { Nav } from './components/Nav'
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <Nav />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={ <Navigate to="/users" />} />
          <Route path="/sales" element={<Sales />} />
          <Route path="/users" element={<Users />} />
          <Route path="/products" element={<Products />} />
        </Routes>
        <Toaster />
      </BrowserRouter>


    </>
  )
}

export default App
