(function(document) {
    // Cache DOM
    const $goLogin = document.querySelector('#go-login'),
        $goRegister = document.querySelector('#go-register'),
        $container = document.querySelector('.container'),
        $overlayContainer = document.querySelector('.overlay-container');

    _toggleForm = () => {
        if ($container.classList.contains('go-register')) {
            $container.classList.remove('go-register')
            $container.classList.add('go-login')
            $overlayContainer.classList.add('animateWidth')
            $overlayContainer.addEventListener('webkitTransitionEnd', () => $overlayContainer.classList.remove('animateWidth'))
        } else {
            $container.classList.remove('go-login')
            $container.classList.add('go-register')
            $overlayContainer.classList.add('animateWidth')
            $overlayContainer.addEventListener('webkitTransitionEnd', () => $overlayContainer.classList.remove('animateWidth'))
        }
    }


    $goLogin.addEventListener('click', _toggleForm);
    $goRegister.addEventListener('click', _toggleForm);
})(document);