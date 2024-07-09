let loginForm = document.querySelector("#loginForm")

loginForm.addEventListener('submit', async function(event){
    event.preventDefault()
    let postData = {
        'username': loginForm.username.value,
        'password': loginForm.password.value
    }
    let response = await fetch("http://localhost:8000/auth/token/", {
        method: 'POST',
        body: JSON.stringify(postData),
        headers: {
            'Content-type': 'application/json'
        }
    })
    let resData = await response.json()
    if (response){
        localStorage.setItem('token', resData.access)
    }
})