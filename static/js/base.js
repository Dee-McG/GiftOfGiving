let currentUrl = window.location.href;

function createSnow() {
    let snow = document.createElement('i');

    snow.classList.add('fas')
    snow.classList.add('fa-circle')

    snow.style.left = Math.random() * window.innerWidth - 30 + 'px';
    snow.style.animationDuration = Math.random()  *3 + 2 + 's';
    snow.style.opacity = Math.random();
    snow.style.fontSize = Math.random() + 'rem';


    document.body.appendChild(snow);

    setTimeout(() => {
        snow.remove()
    }, 6000 )
}

if (currentUrl === 'https://8000-red-bass-pzg6c36t.ws-eu23.gitpod.io/' || currentUrl === 'https://gift-of-giving.herokuapp.com/' ) {
    setInterval(createSnow, 10)
}


