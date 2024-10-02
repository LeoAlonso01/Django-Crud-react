import { useEffect, useState } from "react";
import { getUsers, createUser } from "../api/users.api"; // Suponiendo que tienes una API para obtener usuarios
import { UserForm } from "../components/UserForm"; // Importa el formulario de usuarios
import { useAuth0 } from "@auth0/auth0-react";
import {toast } from 'react-hot-toast';


export function Users() {

  const { user, isAuthenticated } = useAuth0();
  const [users, setUsers] = useState([]);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    const loadUsers = async () => {
      const users = await getUsers();
      setUsers(users);
    };

    loadUsers();
  }, []);

  const handleUserSubmit = (userData) => {
    if (!isAuthenticated) {
      toast.error('No estas autenticado', {
        duration: 4000,
        position: 'top-right',
      });
      return;
    }
    createUser(userData);
    toast.success('Usuario creado correctamente', {
      duration: 4000,
      position: 'top-right',
    });
    setShowForm(false); // Ocultar el formulario después de crear el usuario
  };

  return (
    <div className="container">
      <h1>Lista de Usuarios</h1>
      <div>
        <button
          onClick={() => setShowForm(!showForm)} // Alternar entre mostrar/ocultar formulario
          className="btn add-btn"
        >
          {showForm ? "Cancelar" : "Agregar Usuario"}
        </button>
      </div>
      {showForm ? (
        <UserForm onSubmit={handleUserSubmit} /> // Mostrar formulario si `showForm` es true
      ) : (
        <table>
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Teléfono</th>
              <th>Rol</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id_user}>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.phone}</td>
                <td>{user.role === 1 ? "Administrador" : "Usuario"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
