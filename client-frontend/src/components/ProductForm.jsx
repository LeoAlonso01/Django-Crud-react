import { useState } from "react";

export function ProductForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    name: "",
    category: "",
    brand: "",
    price: 0,
    stock: 0,
    isAviable: false,
    description: "",
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Nombre del producto:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Categoría:</label>
        <input
          type="text"
          name="category"
          value={formData.category}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Marca:</label>
        <input
          type="text"
          name="brand"
          value={formData.brand}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Precio:</label>
        <input
          type="number"
          name="price"
          value={formData.price}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Stock:</label>
        <input
          type="number"
          name="stock"
          value={formData.stock}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label>Disponible:</label>
        <input
          type="checkbox"
          name="isAviable"
          checked={formData.isAviable}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Descripción:</label>
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
      </div>

      <button type="submit">Enviar</button>
    </form>
  );
}





