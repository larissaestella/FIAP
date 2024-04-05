import { Link } from "react-router-dom";

function Header() {
  return (
    <header>
      <h1>Meu site</h1>
      <nav>
            <ul>
            <li><Link to='/'>Home</Link></li>
            <li><Link to='sobre'>Sobre</Link></li>
            <li><Link to='servicos'>Serviço</Link>s</li>
            <li><Link to='contato'>Contato</Link></li>
            </ul>
        </nav>
    </header>
  );
}

export default Header;
