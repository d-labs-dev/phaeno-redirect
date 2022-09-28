const NEW_PHAENO_URL = 'https://d-labs.com'

function redirctPhaenoToNewUrl(){
    // Simulate an HTTP redirect:
    const path = window.location.pathname;
    console.log(path);
    window.location.replace(NEW_PHAENO_URL + path);
}

redirctPhaenoToNewUrl();