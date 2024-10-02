import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { Auth0Provider } from '@auth0/auth0-react'
import './index.css'


/* const clientId = import.meta.env.VITE_APP_CLIENT_ID;
const domain = import.meta.env.VITE_APP_DOMAIN; */

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Auth0Provider
    domain="dev-85kjznb2qyq6rnuv.us.auth0.com"
    clientId="byEkx5Y5l4U7MC8w8cI2R0umcDHnc8ME"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
      <App />
    </Auth0Provider>
  </StrictMode>,
)
