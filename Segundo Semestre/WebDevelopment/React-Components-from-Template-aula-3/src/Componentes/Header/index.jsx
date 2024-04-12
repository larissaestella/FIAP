import {Link} from 'react-router-dom';

function Header(props) {
  return (
    <header>
      <h1 id={props.identificador}>{props.titulo}</h1>
      <nav>
        <ul>
         <li><Link to="/">Home</Link></li>
         <li><Link to="sobre">Sobre</Link></li>
         <li><Link to="servicos">Serviços</Link></li>
         <li><Link to="contato">Contato</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
