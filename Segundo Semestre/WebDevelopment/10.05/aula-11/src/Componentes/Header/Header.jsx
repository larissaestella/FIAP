import NavBar from "../NavBar/NavBar";

function Header() {
    return ( 
        <header className="flex justify-around bg-black text-white p-5 mb-4">
            <span>Ola, Visitante</span>
            <h1>Bem-vindo ao MovieApp</h1>
            <NavBar/>
        </header>
    );
}

export default Header;