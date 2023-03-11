const registerForm = document.getElementById('register-form');
const registerBtn = document.getElementById('register-btn');

registerBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    const name = registerForm.elements.name.value;
    const address = registerForm.elements.address.value;
    const email = registerForm.elements.email.value;
    const phone = registerForm.elements.phone.value;
    const whatsapp = registerForm.elements.whatsapp.checked;
    const password = registerForm.elements.password.value;
    
    const data = { name, address, email, phone, whatsapp, password };
    
    fetch(`http://127.0.0.1:8000/user`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => {
        if (response.ok) {
            alert('Cadastro realizado com sucesso!');
            registerForm.reset();
            window.location.replace("login.html");
        } else {
            throw new Error('Falha ao registrar!');
        }
    })
    .catch(error => {
        console.error(error);
        alert(error.message);
    });
});
