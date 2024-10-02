import { useEffect, useState } from "react"
import { getProducts, createProduct } from "../api/products.api"
import { useAuth0 } from "@auth0/auth0-react";
import { ProductForm } from "../components/ProductForm"
import {toast } from 'react-hot-toast';

import './product.css'

export function Products() {

  const { user, isAuthenticated } = useAuth0();
  const [showForm, setShowForm] = useState(false)
  const [products, setProducts] = useState([])
 
  useEffect(() => {

    const loadProducts = async () => {
      const products = await getProducts()
      console.log(products)
      setProducts(products)
    }

    loadProducts()

    return () => {
      console.log('Products component unmounted')
    }

  }, [])


  const handleProductSubmit = (product) => {
    if (!isAuthenticated) {
      toast.error('No estas autenticado', {
        duration: 4000,
        position: 'top-right',
      });
      return;
    }
    setShowForm(false)
    createProduct(product)
    toast.success('Producto creado correctamente', {
      duration: 4000,
      position: 'top-right',
    });
  }
  return (

    <div className="container">
      <h1>Tabla de Products</h1>

      <div>
        <button onClick={() => setShowForm(!showForm)  } className="btn add-btn">
          {showForm ? 'Cerrar Formulario' : 'Agregar Producto'}
        </button>
      </div>
      {showForm ? (
        <div>
          <h1>Formulario de Productos</h1>

          <ProductForm  onSubmit={ handleProductSubmit } />
        </div>
      ) : (<table>
        <thead>
          <tr>
            <th>Producto</th>
            <th>Precio</th>
            <th>Categoria</th>
            <th>Descripcion</th>
            <th>Stock</th>
            <th>Marca</th>
            <th>Disponible</th>
          </tr>
        </thead>
        <tbody>
          {products.map((producto) => (
            <tr key={producto.id_product}>
              <td>{producto.name}</td>
              <td>{producto.price}</td>
              <td>{producto.category}</td>
              <td>{producto.description}</td>
              <td>{producto.is_aviable ? producto.stock : 0}</td>
              <td>{producto.brand}</td>
              <td>{producto.is_aviable ? 'Dispoonible ' : 'Agotado'}</td>
            </tr>
          ))}
        </tbody>
      </table>)}
      <div />
    </div>
  )
}
