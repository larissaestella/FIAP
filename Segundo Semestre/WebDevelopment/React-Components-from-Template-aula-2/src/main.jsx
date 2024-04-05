import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import Sobre from './Pages/Sobre.jsx'
import Servicos from './Pages/Servicos.jsx'
import Contatos from './Pages/Contatos.jsx'
import PageNotFound from './Pages/PageNotFound.jsx'
import ConteudoPrincipal from './Componentes/ConteudoPrincipal/index.jsx'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App/>,
    children: [
      {index: true, element: <ConteudoPrincipal/>},
      {path:'sobre', element: <Sobre/>},
      {path:'servicos', element: <Servicos/>},
      {path:'contatos', element: <Contatos/>},
      {path:'*', element: <PageNotFound/>},
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
