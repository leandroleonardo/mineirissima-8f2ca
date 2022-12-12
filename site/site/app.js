const config = {
    apiKey: "AIzaSyBmbnXefOzYkNvhHO2lbFvd1j9vx0Ewa_Y",
    authDomain: "mineirissima-8f2ca.firebaseapp.com",
    databaseURL: "https://mineirissima-8f2ca-default-rtdb.firebaseio.com",
    projectId: "mineirissima-8f2ca",
    storageBucket: "mineirissima-8f2ca.appspot.com",
    messagingSenderId: "1055631491220",
    appId: "1:1055631491220:web:5a805023cf73847a08b481"
};

firebase.initializeApp(config);

function adicina_usuario(){
    
    let db = firebase.firestore();
    
    let nome_input = document.getElementById("name").value;
    let email_input = document.getElementById("email").value;

    if(nome_input == "" || email_input == "") return

    db.collection('usuarios').add({
        Nome: nome_input,
        Email: email_input
    }).then((doc) => {
        closeModal()
    }).cacth(err => {
        closeModal()
    })
}

const form = document.getElementById('enviar-form-email')

form.addEventListener('submit', e => {
    
    e.preventDefault()
    
    let db = firebase.firestore();

    let nome_input = document.getElementById("name_contact").value;
    let email_input = document.getElementById("email_contact").value;
    let mensagem_input = document.getElementById("mensagem_contact").value;

    if(nome_input == "" || email_input == "" || mensagem_input == "") return

    db.collection('contatos').add({
        Nome: nome_input,
        Email: email_input,
        Mensagem: mensagem_input
    }).then((doc) => {
        openModal_sucesso()
        nome_input = document.getElementById("name_contact").value = "";
        email_input = document.getElementById("email_contact").value = "";
        mensagem_input = document.getElementById("mensagem_contact").value = "";
    }).cacth(err => {
        console.log(err)
    })

})