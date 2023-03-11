const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = loginForm.elements.email.value;
    const password = loginForm.elements.senha.value;   

    console.log('Email:', email);
    console.log('Password:', password);

    try {
        const response = await fetch(`http://127.0.0.1:8000/auth/login?email=${email}&senha=${password}`, {
            method: 'POST',
            body: JSON.stringify({ email, password }),
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Login successful', data);
            alert('Logado com sucesso');
            // Store the user token or other data you may need
            // Redirect to a dashboard page or other content
            loginForm.reset();
            window.location.replace("inicio.html");
        } else {
            throw new Error('Invalid login credentials');
        }
    } catch (error) {
        console.error(error);
        alert('Falha ao fazer login!');
    }
});
