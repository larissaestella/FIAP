function ContactForm() {
  return (
    <section id="contact">
      <h2>Entre em Contato</h2>
      <form>
        <input type="text" placeholder="Nome" />
        <input type="email" placeholder="Email" />
        <textarea placeholder="Mensagem" />
        <button type="submit">Enviar</button>
      </form>
    </section>
  );
}

export default ContactForm;