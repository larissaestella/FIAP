import ContactForm from "../ContactForm";
import PersonalInfo from "../PersonalInfo";
import Skills from "../Skills";

function ConteudoPrincipal(){
    return (
        <div className="mainInfo">
        <section id='info'>
            <PersonalInfo />
            <Skills />
        </section>
        <ContactForm />
      </div>
    );
}

export default ConteudoPrincipal;