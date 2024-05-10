import data from "../../artigos.json"

function Home() {
   
    return ( 
        <>
        <input 
        type="text" 
        name="buscaFilme" 
        id="buscaFilme" 
        placeholder="Digite sua busca aqui"/>

    <div id="listaFilmes">
        {
            data.map(
                (post, index)=> (
                    <div id="card" key={index}>
                        <h1>{post.title}</h1>
                        <img src={post.image}/>
                    </div>
            ))
        }
    </div>
        </>
    );
}

export default Home ;

/* <div id="listaFilmes">
            <div>
                <h1>Título do Filme</h1>
                <img src="" alt="" />
                <div id="tags">
                    <span></span>
                    <span></span>
                </div>
                <div id="textos">
                    <p></p>
                    <p></p>
                </div>
            </div>
        </div> */