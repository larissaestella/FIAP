import PersonalInfo from '../Componentes/PersonalInfo';
import Skills from '../Componentes/Skills';
import ContactForm from '../Componentes/ContactForm'

function Home() {
  const baseUsuarios = [
  { nome: 'Larissa', email: 'larissa@gmail.com', telefone: '999999999'},
  { nome: 'Caio', email: 'caio@gmail.com', telefone: '888888888'},
]
  return (
    <div className="mainInfo">
      <section id='info'>
          <PersonalInfo usuarios={baseUsuarios}/>
          <Skills 
          habilidade1="HMTL"
          nivel1="Intermediário"
          habilidade2="CSS"
          nivel2="Avançado"
          habilidade3="JavaScript"
          nivel3="Básico"
          />
        </section>
        <ContactForm />
    </div>
  );
}

export default Home;