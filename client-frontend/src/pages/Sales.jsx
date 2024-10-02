import { useEffect, useState } from 'react'
import { getSales } from '../api/sales.api'


export function Sales() {

  const [sales, setSales] = useState([])

  useEffect(() => {
    const loadSales = async () => {
      const sales = await getSales()
      setSales(sales)
      console.log(sales)
    }
    loadSales()
  }, [])
  return (
    <>
      <h1>Tabla de Ventas</h1>
      <div>
        <button disabled className="btn add-btn">Agregar</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>Fecha</th>
            <th>Cantidad</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          {
            sales.map((sale) => (
              <tr key={sale.id_sale}>
                <td>{sale.date}</td>
                <td>{sale.quantity}</td>
                <td>{sale.total}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    </>
  )
}

