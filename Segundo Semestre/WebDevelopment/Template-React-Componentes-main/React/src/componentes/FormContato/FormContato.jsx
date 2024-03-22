function FormContato(){
    return(
    <div class="mainInfo">
        <section id="contact">
            <h2>Entre em Contato</h2>
            <form>
                <input type="text" placeholder="Nome"/>
                <input type="email" placeholder="Email"/>
                <textarea placeholder="Mensagem"></textarea>
                <button type="submit">Enviar</button>
            </form>
        </section>
    </div>
    )
}

export default FormContato